#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text /MERGE:.text1=.text /SECTION:.idata,ERW")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")

#include "ml.cpp"
#include "D:\Desktop\Source\Project\AppleIdAuthorizer\AppleIdAuthorizer\iTunesHelper\iTunesHelper.cpp"

#include "D:\Desktop\Source\Project\AppleIdAuthorizer\AppleIdAuthorizer\iTunesHelper/iOSService.h"
#include "D:\Desktop\Source\Project\AppleIdAuthorizer\AppleIdAuthorizer\iTunesHelper/iOSAFC.h"
#include "D:\Desktop\Source\Project\AppleIdAuthorizer\AppleIdAuthorizer\iTunesHelper/iOSDeviceMonitor.h"
#include "D:\Desktop\Source\Project\AppleIdAuthorizer\AppleIdAuthorizer\iTunesHelper/iOSATH.h"

#include "D:\Desktop\Source\Project\AppleIdAuthorizer\AppleIdAuthorizer\iTunesHelper\iOS.cpp"
#include "D:\Desktop\Source\Project\AppleIdAuthorizer\AppleIdAuthorizer\iTunesHelper\iOSDevice.cpp"
#include "D:\Desktop\Source\Project\AppleIdAuthorizer\AppleIdAuthorizer\iTunesHelper/iOSATH.cpp"

ML_OVERLOAD_NEW

NTSTATUS
getAfsyncResponse(
    ULONG                   grappaSessionId,
    PVOID                   fairPlayCertificate,
    ULONG_PTR               certificateSize,
    PVOID                   afsyncRequest,
    ULONG_PTR               requestSize,
    PVOID                   afsyncRequestSignature,
    ULONG_PTR               signatureSize,
    PAIR_FAIR_DEVICE_INFO   deviceInfo,
    PDEVICE_ID              fairPlayGuid
)
{
    HANDLE          kbsync, afsync;
    DEVICE_ID       mid, mid2;
    NTSTATUS        status;
    iTunesHelper    itunes;

    ULONG64 dsids[] =
    {
        0x38AC242C,
    };

    kbsync = nullptr;
    afsync = nullptr;

    LOOP_ONCE
    {
        ZeroMemory(&mid, sizeof(mid));
        ZeroMemory(&mid2, sizeof(mid2));

        mid.length = 6;
        *(PULONG)&mid.deviceId[0] = GetRandom32();
        *(PUSHORT)&mid.deviceId[4] = (USHORT)(GetRandom32() + *(PULONG)&mid.deviceId[0]);

        mid2.length = 6;
        *(PULONG)&mid2.deviceId[0] = GetRandom32() + *(PULONG)&mid.deviceId[1];
        *(PUSHORT)&mid2.deviceId[4] = (USHORT)(GetRandom32() + *(PULONG)&mid2.deviceId[0]);

        *(PULONG)&mid.deviceId[0] = 0x28AE81F3;
        *(PUSHORT)&mid.deviceId[1] = 0x2E1C;

        *(PULONG)&mid2.deviceId[0] = 0xDE903948;
        *(PUSHORT)&mid2.deviceId[1] = 0x8CE8;

        status = itunes.iTunesInitialize();
        //status = itunes.KbsyncCreateSession(&kbsync, &mid, &mid2, "C:\\ProgramData\\Apple Computer\\iTunes\\SC Info");

        kbsync = *(PHANDLE)PtrAdd(FindLdrModuleByName(PUSTR(L"iOSDevice.dll"))->DllBase, 0x63C599BC - 0x63A80000);

        //itunes.AirFairFetchRequest(grappaSessionId, afsyncRequest, requestSize, afsyncRequestSignature, signatureSize);

        // 14 00 00 00 4E 0E 3F 92 17 5D 64 73 50 75 53 8B 57 5E 31 09 5F 3F 9A 30
        // 14 00 00 00 4E 0E 3F 92 17 5D 64 73 F0 75 53 8B F7 FE 31 09 5F 3F 9A 30
        // 14 00 00 00 4E 0E 3F 92 17 5D 64 73 F0 75 53 8B F7 FE 31 09 5F 3F 9A 30

        status = itunes.AirFairSyncCreateSession(
                    &afsync,
                    kbsync,
                    fairPlayCertificate,
                    certificateSize,
                    fairPlayGuid,
                    deviceInfo
                );

        status = itunes.AirFairSyncSetRequest(afsync, afsyncRequest, requestSize, nullptr, 0);

        PAIR_FAIR_AUTHORIZED_DSID authed;
        ULONG_PTR count;

        itunes.AirFairSyncGetAuthorizedAccount(nullptr, fairPlayGuid, deviceInfo->deviceType, afsyncRequest, requestSize, &authed, &count);

        for (ULONG_PTR i = 0; i != countof(dsids); ++i)
        {
            itunes.AirFairSyncAddAccount(afsync, dsids[i]);
        }

        itunes.AirFairSyncGetAuthorizedAccount(afsync, fairPlayGuid, deviceInfo->deviceType, afsyncRequest, requestSize, &authed, &count);
        itunes.FreeSessionData(authed);
    }

    itunes.KbsyncCloseSession(kbsync);

    return 0;
}

VOID onconnect(PDEVICE_CONNECTION_INFO Info)
{
    iOSDevice device(Info->Device);

    iOSDeviceConnector conn(device);

    String FairPlayGUID = device.GetFairPlayGUID();
    CFData FairPlayCertificate(*(CFData *)&device.GetFairPlayCertificate());
    CFNumber FairPlayDeviceType(*(CFNumber *)&device.GetFairPlayDeviceType());
    CFNumber KeyTypeSupportVersion(*(CFNumber *)&device.GetKeyTypeSupportVersion());

    DEVICE_ID guid;

    guid.length = __min((ULONG)FairPlayGUID.GetCount() / 2, sizeof(guid.deviceId));

    PBYTE buf = guid.deviceId;
    PCWSTR str = FairPlayGUID.GetBuffer();
    for (LONG_PTR i = guid.length; i > 0; --i)
    {
        *buf++ = (BYTE)(((str[0] >= '0' && str[0] <= '9') ? (str[0] - '0') : ((str[0] & 0xDF) - 'A' + 10)) << 4) |
                 (BYTE)((str[1] >= '0' && str[1] <= '9') ? (str[1] - '0') : ((str[1] & 0xDF) - 'A' + 10));
        str += 2;
    }

    iOSATH ath(device);
    ULONG grappa;

    grappa = 0;

#if 0

    ath.Connect();

    ath.SendPowerAssertion(TRUE);

    while (ath.SyncAllowed == FALSE)
    {
        YieldProcessor();
    }

    PrintConsole(L"SendSyncRequest\n");
    ath.SendSyncRequest();

    while (ath.ReadyForSync == FALSE)
    {
        YieldProcessor();
    }

    grappa = ath.GetGrappaSessionId();

#endif

    AIR_FAIR_DEVICE_INFO deviceInfo;

    deviceInfo.deviceType = (ULONG_PTR)FairPlayDeviceType.ToULong64();
    deviceInfo.keyTypeSupportVersion = (ULONG_PTR)KeyTypeSupportVersion.ToULong64();

    CFData request = iOSAFC::ReadFileToBuffer(device, L"/AirFair/sync/afsync.rq");
    CFData sig = iOSAFC::ReadFileToBuffer(device, L"/AirFair/sync/afsync.rq.sig");

    if (request != nullptr)
    {
        getAfsyncResponse(
            grappa,
            CFDataGetBytePtr(FairPlayCertificate),
            CFDataGetLength(FairPlayCertificate),
            CFDataGetBytePtr(request),
            CFDataGetLength(request),
            CFDataGetBytePtr(sig),
            CFDataGetLength(sig),
            &deviceInfo,
            &guid
        );
    }
}

EXTC_EXPORT VOID CDECL e()
{
    iTunesApi::Initialize();

    iOSDeviceMonitor monitor;

    monitor.NotificationSubscribe(
        [](PDEVICE_CONNECTION_INFO Info, PVOID Context)
        {
            onconnect(Info);
        },
        nullptr
    );

    monitor.WaitForDeviceConnectionChanged();
}

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    LdrDisableThreadCalloutsForDll(BaseAddress);
    ml::MlInitialize();

    return TRUE;
}

BOOL WINAPI DllMain(PVOID BaseAddress, ULONG Reason, PVOID Reserved)
{
    switch (Reason)
    {
        case DLL_PROCESS_ATTACH:
            return Initialize(BaseAddress) || UnInitialize(BaseAddress);

        case DLL_PROCESS_DETACH:
            UnInitialize(BaseAddress);
            break;
    }

    return TRUE;
}
