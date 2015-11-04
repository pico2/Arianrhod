#include "stdafx.h"
#include "iOSDevice.h"
#include "iOSService.h"

VOID GenerateModuleList(String &ModuleNames)
{
    PVOID                               Address, BaseAddress, LastAllocationBase;
    ULONG_PTR                           Size, Need, BufferSize;
    NTSTATUS                            Status;
    SYSTEM_BASIC_INFORMATION            SystemBasic;
    MEMORY_BASIC_INFORMATION            MemoryBasic;

    union
    {
        MEMORY_MAPPED_FILENAME_INFORMATION2 MappedFile;
        BYTE MappedFileBuffer[0x2000];
    };

    Status = NtQuerySystemInformation(SystemBasicInformation, &SystemBasic, sizeof(SystemBasic), nullptr);
    if (!NT_SUCCESS(Status))
        return;

    LastAllocationBase = IMAGE_INVALID_VA;
    BaseAddress = (PVOID)SystemBasic.MinimumUserModeAddress;
    BaseAddress = nullptr;

    for (; (ULONG_PTR)BaseAddress < SystemBasic.MaximumUserModeAddress; BaseAddress = PtrAdd(BaseAddress, MemoryBasic.RegionSize))
    {
        MemoryBasic.RegionSize = MEMORY_PAGE_SIZE;
        Status = NtQueryVirtualMemory(CurrentProcess, BaseAddress, MemoryBasicInformation, &MemoryBasic, sizeof(MemoryBasic), nullptr);
        FAIL_CONTINUE(Status);

        BaseAddress = MemoryBasic.BaseAddress;

        if (MemoryBasic.Type != MEM_IMAGE || MemoryBasic.AllocationBase == LastAllocationBase)
            continue;

        LastAllocationBase = MemoryBasic.AllocationBase;

        Status = NtQueryVirtualMemory(CurrentProcess, BaseAddress, MemoryMappedFilenameInformation, &MappedFile, sizeof(MappedFileBuffer), nullptr);
        if (NT_FAILED(Status) || MappedFile.Name.Length == 0)
            continue;

        UNICODE_STRING DosPath;

        Status = Io::QueryDosPathFromNtDeviceName(&DosPath, &MappedFile.Name);

        ModuleNames += ml::String::Format(L"%p: %wZ\n", BaseAddress, NT_SUCCESS(Status) ? &DosPath : &MappedFile.Name);

        RtlFreeUnicodeString(&DosPath);
    }
}

NTSTATUS iOSDevice::IsJailbroken()
{
    // kAMDInvalidServiceError
    return iOSService(*this).Start("com.apple.afc2");
}

NTSTATUS iOSDevice::Restart()
{
    NTSTATUS Status;
    iOSService service(*this);

    DebugLog(L"restart");

    Status = service.Start("com.apple.mobile.diagnostics_relay");
    if (Status != kAMDSuccess)
        return Status;

    CFDict request;

    request.SetValue(L"Request", L"Restart");
    service.SendMessage(request);

    return Status;
}

NTSTATUS GetAfsyncResponseSignature(iTunesHelper &helper, ULONG GrappaSessionId, CFData& Response, CFData& SignatureData)
{
    PVOID       Signature;
    ULONG       SignatureLength;
    NTSTATUS    Status;

    Status = helper.AirFairSyncSignData(GrappaSessionId, CFDataGetBytePtr(Response), CFDataGetLength(Response), &Signature, &SignatureLength);
    if (Status != STATUS_SUCCESS)
        return Status;

    SignatureData = CFDataCreate(nullptr, Signature, SignatureLength);
    helper.FreeSessionData(Signature);

    return Status;
}

NTSTATUS
GetAfsyncResponse(
    iTunesHelper&           helper,
    PCSTR                   ScInfoPath,
    //ULONG                   GrappaSessionId,
    CFData&                 FairPlayCertificate,
    CFData&                 AFSyncRequest,
    PAIR_FAIR_DEVICE_INFO   DeviceInfo,
    PFAIR_PLAY_HW_INFO         FairPlayGuid,
    GrowableArray<ULONG64>& DsidToAuth,
    GrowableArray<ULONG64>& DsidAuthed,
    CFData&                 Response
)
{
    HANDLE      afsync;
    FAIR_PLAY_HW_INFO   mid, mid2;
    NTSTATUS    status;

    static HANDLE kbsync;

    afsync = nullptr;

    status = STATUS_SUCCESS;

    LOOP_ONCE
    {
        if (kbsync == nullptr)
        {
            ZeroMemory(&mid, sizeof(mid));
            ZeroMemory(&mid2, sizeof(mid2));

            mid2.length = 6;
            *(PULONG)&mid2.deviceId[0] = 0xB5BBE9BE;
            *(PUSHORT)&mid2.deviceId[4] = 0xD149;

            mid.length = 6;
            *(PULONG)&mid.deviceId[0] = 0xDE903948;
            *(PUSHORT)&mid.deviceId[4] = 0x8CE8;

            //helper.GetDeviceId(&mid, &mid2);

            // g_hardware_hash
            //*(PULONG)&mid2.deviceId[0] = 0x41907897;
            //*(PUSHORT)&mid2.deviceId[4] = 0x8CD9;

            // g_local_hash
            //*(PULONG)&mid.deviceId[0] = 0x72003B2F;
            //*(PUSHORT)&mid.deviceId[4] = 0x4E90;

            DebugLog(L"ScInfoPath = %S", ScInfoPath);
            status = helper.KbsyncCreateSession(&kbsync, &mid, &mid2, ScInfoPath);
            DebugLog(L"KbsyncCreateSession = %p", status);
            RETURN_IF(status != 0, status);
        }

        //status = itunes.AirFairVerifyRequest(GrappaSessionId, afsyncRequest, requestSize, afsyncRequestSignature, signatureSize);

        status = helper.AirFairSyncCreateSession(
                    &afsync,
                    kbsync,
                    CFDataGetBytePtr(FairPlayCertificate),
                    CFDataGetLength(FairPlayCertificate),
                    FairPlayGuid,
                    DeviceInfo
                );
        DebugLog(L"AirFairSyncCreateSession = %p", status);
        BREAK_IF(status != 0);

        status = helper.AirFairSyncSetRequest(afsync, CFDataGetBytePtr(AFSyncRequest), CFDataGetLength(AFSyncRequest), nullptr, 0);
        DebugLog(L"AirFairSyncSetRequest = %p", status);
        BREAK_IF(status != 0);

        PAIR_FAIR_AUTHORIZED_DSID authed;
        ULONG_PTR count;

        status = helper.AirFairSyncGetAuthorizedAccount(
                        nullptr,
                        FairPlayGuid,
                        DeviceInfo->deviceType,
                        CFDataGetBytePtr(AFSyncRequest),
                        CFDataGetLength(AFSyncRequest),
                        &authed,
                        &count
                    );

        DebugLog(L"AirFairSyncGetAuthorizedAccount = %p", status);
        BREAK_IF(status != 0);

        helper.FreeSessionData(authed);

        //static ULONG64 dsids[] =
        //{
        //    8306210101,
        //    8306210340,
        //};

        for (ULONG_PTR i = 0; i != DsidToAuth.GetSize(); ++i)
        {
            helper.AirFairSyncAddAccount(kbsync, &mid2, afsync, DsidToAuth[i]);
        }

        helper.AirFairSyncGetAuthorizedAccount(afsync, FairPlayGuid, DeviceInfo->deviceType, nullptr, 0, &authed, &count);

        for (ULONG_PTR i = 0; i != count; ++i)
        {
            DsidAuthed.Add(authed->at(i));
        }

        helper.FreeSessionData(authed);

        PVOID rs;
        ULONG rssize;

        status = helper.AirFairSyncGetResponse(afsync, &rs, &rssize);
        DebugLog(L"AirFairSyncGetResponse = %p", status);
        BREAK_IF(status != 0);

        if (rssize != 0 && rs != nullptr)
            Response = CFDataCreate(nullptr, rs, rssize);

        helper.FreeSessionData(rs);
    }

    if (status != STATUS_SUCCESS && afsync != nullptr)
        helper.AirFairSyncReset(afsync);

    //helper.KbsyncCloseSession(kbsync);

    return status;
}

NTSTATUS
iOSDevice::
AuthorizeDsids(
    iTunesHelper*           helper,
    PCSTR                   SCInfoPath,
    GrowableArray<ULONG64>& DsidToAuth,
    GrowableArray<ULONG64>& DsidAuthed
)
{
    String FairPlayGUID = GetFairPlayGUID();
    CFData FairPlayCertificate(*(CFData *)&GetFairPlayCertificate());
    CFNumber FairPlayDeviceType(*(CFNumber *)&GetFairPlayDeviceType());
    CFNumber KeyTypeSupportVersion(*(CFNumber *)&GetKeyTypeSupportVersion());

    FAIR_PLAY_HW_INFO guid;

    guid.length = __min((ULONG)FairPlayGUID.GetCount() / 2, sizeof(guid.deviceId));

    PBYTE buf = guid.deviceId;
    PCWSTR str = FairPlayGUID.GetBuffer();
    for (LONG_PTR i = guid.length; i > 0; --i)
    {
        *buf++ = (BYTE)(((str[0] >= '0' && str[0] <= '9') ? (str[0] - '0') : ((str[0] & 0xDF) - 'A' + 10)) << 4) |
                 (BYTE)((str[1] >= '0' && str[1] <= '9') ? (str[1] - '0') : ((str[1] & 0xDF) - 'A' + 10));
        str += 2;
    }

    iOSATH ath(*this);

    ath.Connect();

    DebugLog(L"ath connect done");

#if 1

    ath.SendPowerAssertion(TRUE);

    DebugLog(L"waiting SyncAllowed\n");
    while (ath.SyncAllowed == FALSE && ath.SyncFailed == FALSE && ath.ConnectionBroken == FALSE)
    {
        Ps::Sleep(1000);
        //ath.Ping();
    }

    if (ath.SyncFailed || ath.ConnectionBroken)
        return STATUS_UNSUCCESSFUL;

    DebugLog(L"SendSyncRequest\n");
    ath.SendSyncRequest();

    DebugLog(L"waiting ReadyForSync\n");
    while (ath.ReadyForSync == FALSE && ath.SyncFailed == FALSE && ath.ConnectionBroken == FALSE)
    {
        Ps::Sleep(1000);
        //ath.Ping();
    }

    if (ath.SyncFailed || ath.ConnectionBroken)
        return STATUS_UNSUCCESSFUL;

#endif

    AIR_FAIR_DEVICE_INFO deviceInfo;

    deviceInfo.deviceType = (ULONG_PTR)FairPlayDeviceType.ToULong64();
    deviceInfo.keyTypeSupportVersion = (ULONG_PTR)KeyTypeSupportVersion.ToULong64();

    iOSDeviceConnector conn(*this);

    if (conn.connected == FALSE)
        return kAMDDeviceDisconnectedError;

    CFData request = iOSAFC::ReadFileToBuffer(*this, L"/AirFair/sync/afsync.rq");
    CFData response, signature;
    //CFData sig = iOSAFC::ReadFileToBuffer(*this, L"/AirFair/sync/afsync.rq.sig");

    if (request == nullptr)
        return STATUS_REQUEST_ABORTED;

    NTSTATUS status;

    status = GetAfsyncResponse(
            *helper,
            SCInfoPath,
            // ,
            FairPlayCertificate,
            request,
            &deviceInfo,
            &guid,
            DsidToAuth,
            DsidAuthed,
            response
        );
    DebugLog(L"GetAfsyncResponse = %p", status);

    String ml;

    GenerateModuleList(ml);
    //wprintf(L"%s\n", ml);

    if (status != STATUS_SUCCESS)
        return status;

    if (response == nullptr)
        return STATUS_SUCCESS;

    status = GetAfsyncResponseSignature(*helper, ath.GetGrappaSessionId(), response, signature);
    DebugLog(L"GetAfsyncResponseSignature = %p", status);
    if (status != STATUS_SUCCESS)
        return status;

    status = iOSAFC::WriteBufferToFile(*this, L"/AirFair/sync/afsync.rs", response);
    status = iOSAFC::WriteBufferToFile(*this, L"/AirFair/sync/afsync.rs.sig", signature);

    DebugLog(L"SendSyncFinished\n");
    ath.SendSyncFinished();

    while (ath.SyncFinished && ath.SyncFailed == FALSE && ath.ConnectionBroken == FALSE)
    {
        Ps::Sleep(1000);
        //ath.Ping();
    }

    if (ath.SyncFailed || ath.ConnectionBroken)
        status = STATUS_UNSUCCESSFUL;

    ath.SendPowerAssertion(FALSE);

    return status;
}
