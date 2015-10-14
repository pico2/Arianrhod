#include "iTunesHelper.h"

#define ITUNES_DLL_PATH     L"iTunesDLL"

/************************************************************************
  init
************************************************************************/

#define CORE_FP_KEY_HANDLE  ((HANDLE)-0x1000)

API_POINTER(NtOpenKeyEx)        StubNtOpenKeyEx;
API_POINTER(NtQueryValueKey)    StubNtQueryValueKey;

API_POINTER(RegOpenKeyExA)      StubRegOpenKeyExA;
API_POINTER(RegQueryValueExA)   StubRegQueryValueExA;

LSTATUS
NTAPI
ItRegOpenKeyExA(
    HKEY    hKey,
    PCSTR   lpSubKey,
    DWORD   ulOptions,
    REGSAM  samDesired,
    PHKEY   phkResult
)
{
    LSTATUS r;

    r = StubRegOpenKeyExA(hKey, lpSubKey, ulOptions, samDesired, phkResult);
    if (r == NO_ERROR)
        return r;

    if (hKey != HKEY_LOCAL_MACHINE)
        return r;

    if (StrICompareA(lpSubKey, "Software\\Apple Inc.\\CoreFP") != 0)
        return r;

    *phkResult = (HKEY)CORE_FP_KEY_HANDLE;

    return NO_ERROR;
}

LSTATUS
NTAPI
ItRegQueryValueExA(
    HKEY    hKey,
    PCSTR   lpValueName,
    LPDWORD lpReserved,
    LPDWORD lpType,
    LPBYTE  lpData,
    LPDWORD lpcbData
)
{
    LSTATUS status;

    LOOP_ONCE
    {
        if (StrICompareA(lpValueName, "LibraryPath") != 0)
            continue;

        if (hKey != (HKEY)CORE_FP_KEY_HANDLE)
        {
            OBJECT_NAME_INFORMATION2 name;

            status = NtQueryObject(hKey, ObjectNameInformation, &name, sizeof(name), nullptr);
            if (NT_FAILED(status))
                break;

            if (RtlEqualUnicodeString(&name.Name, PUSTR(L"\\REGISTRY\\MACHINE\\SOFTWARE\\Wow6432Node\\Apple Inc.\\CoreFP"), TRUE) == FALSE &&
                RtlEqualUnicodeString(&name.Name, PUSTR(L"\\REGISTRY\\MACHINE\\SOFTWARE\\Apple Inc.\\CoreFP"), TRUE) == FALSE)
            {
                break;
            }
        }

        String DllPath;
        Rtl::GetModuleDirectory(DllPath, nullptr);

        DllPath += ITUNES_DLL_PATH;
        DllPath += L"\\CoreFP.dll";

        auto CoreFPPath = DllPath.Encode(CP_ACP);

        if (lpData == nullptr)
        {
            if (lpcbData == nullptr)
                return ERROR_INVALID_PARAMETER;

            *lpcbData = CoreFPPath.GetSize();
            return NO_ERROR;
        }

        if (lpcbData == nullptr)
            return ERROR_INVALID_PARAMETER;

        if (*lpcbData < CoreFPPath.GetSize())
        {
            *lpcbData = CoreFPPath.GetSize();
            return ERROR_MORE_DATA;
        }

        CopyMemory(lpData, CoreFPPath.GetData(), CoreFPPath.GetSize());
        *lpcbData = CoreFPPath.GetSize();

        return NO_ERROR;
    }

    return StubRegQueryValueExA(hKey, lpValueName, lpReserved, lpType, lpData, lpcbData);
}

iTunesHelper::iTunesHelper()
{
    this->iTunesBase = nullptr;
    this->Initialized = FALSE;

    RtlInitializeCriticalSectionAndSpinCount(&this->DeviceCallbacksLock, 4000);
}

NTSTATUS iTunesHelper::iTunesInitialize()
{
    using namespace Mp;

    NTSTATUS    status;
    PVOID       DllBase;
    PCSTR       DllName;

    status = STATUS_SUCCESS;

    if (this->Initialized)
        return status;

    String ExePath;

    Rtl::GetModuleDirectory(ExePath, nullptr);

#if 0

    Rtl::EnvironmentAppend(PUSTR(L"Path"), ExePath + L"iTunes");
    Rtl::EnvironmentAppend(PUSTR(L"Path"), PUSTR(L"C:\\Program Files (x86)\\iTunes"));

    this->iTunesBase = Ldr::LoadDll(L"iTunes.dll");
    LdrDisableThreadCalloutsForDll(this->iTunesBase);

#else

    status = Rtl::EnvironmentAppend(PUSTR(L"Path"), ExePath + ITUNES_DLL_PATH);
    PrintConsole(L"EnvironmentAppend: %p", status);

    status = Ldr::LoadPeImage(ExePath + ITUNES_DLL_PATH L"\\iTunes.dll", &this->iTunesBase, nullptr, LOAD_PE_DLL_NOT_FOUND_CONTINUE);
    FAIL_RETURN(status);

    ((PIMAGE_TLS_CALLBACK)PtrAdd(this->iTunesBase, ImageNtHeaders(this->iTunesBase)->OptionalHeader.AddressOfEntryPoint))(this->iTunesBase, DLL_PROCESS_ATTACH, nullptr);

    *(PVOID *)&StubRegOpenKeyExA = _InterlockedExchangePointer((PVOID *)LookupImportTable(iTunesBase, "ADVAPI32.dll", KERNEL32_RegOpenKeyExA), ItRegOpenKeyExA);
    *(PVOID *)&StubRegQueryValueExA = _InterlockedExchangePointer((PVOID *)LookupImportTable(iTunesBase, "ADVAPI32.dll", KERNEL32_RegQueryValueExA), ItRegQueryValueExA);

#endif

    status = iTunesApi::Initialize();
    FAIL_RETURN(status);

    this->LoadiTunesRoutines();
    //CopyStruct(PtrAdd(this->iTunesBase, 0x19DC120), L"iTunes", sizeof(L"iTunes"));
    //this->InitScInfo();

    this->Initialized = TRUE;

    return status;
}

/************************************************************************
    device methods
************************************************************************/

NTSTATUS
iTunesHelper::
DeviceNotificationSubscribe(
    DeviceNotificationCallback Callback,
    PVOID Context
)
{
    PROTECT_SECTION(&this->DeviceCallbacksLock)
    {
        this->DeviceCallbacks.Add(CALLBACK_ENTRY{Callback, Context});

        if (this->DeviceCallbacks.GetSize() != 1)
            return STATUS_SUCCESS;
    }

    return this->monitor.NotificationSubscribe(
        [](PDEVICE_CONNECTION_INFO Info, PVOID UserData)
        {
            iTunesHelper* thiz = (iTunesHelper *)UserData;

            PROTECT_SECTION(&thiz->DeviceCallbacksLock)
            {
                for (auto &entry : thiz->DeviceCallbacks)
                {
                    entry.Callback(Info->Device, Info->State, entry.Context);
                }
            }
        },
        this
    );
}

/************************************************************************
    itunes wrapper
************************************************************************/

NTSTATUS iTunesHelper::InitScInfo(PKBSYNC_SESSION *kbsync)
{
    PKBSYNC_SESSION session;

    AllocStack(16); // restore esp for initScInfo

    return iTunes.initScInfo(FALSE, kbsync == nullptr ? &session : kbsync, 0);
}

NTSTATUS iTunesHelper::LoadiTunesRoutines()
{
    PVOID *func;
    ULONG_PTR *p, rva[] =
    {
        0x9D60,         // freeSessionData
        0x3546A0,       // getDeviceId
        0x354570,       // getDeviceId2

        0x3555A0,       // loadCoreFP
        0x355A20,       // initScInfo

        // 0x2D890,        // kbsyncSetupSession
        0x16880,        // kbsyncCreateSession
        0x2D890,        // kbsyncInitSomething
        0x197C0,        // KbsyncAuthorizeDsid
        0x36020,        // KbsyncDsidBindMachine
        0x17780,        // kbsyncCloseSession

        0x7D80,         // sapCreateSession
        0xC960,         // sapCloseSession
        0x8CD0,         // sapExchangeData
        0x2ACE0,        // sapCreateActionSignature
        0x3B100,        // sapUpdateActionSignature
        0x3A350,        // sapSignData

        0x113C0,        // airFairFetchRequest
        0x33090,        // airFairSyncCreateSession
        0x34460,        // airFairSyncSetRequest
        0x35270,        // airFairSyncAddAccount
        0x313B0,        // airFairSyncGetAuthorizedAccount
        0x07DE0,        // airFairSyncGetResponse
        0x10630,        // airFairSyncSignData
    };

    func = (PVOID *)&this->iTunes;
    FOR_EACH(p, rva, countof(rva))
    {
        *func++ = PtrAdd(this->iTunesBase, *p);
    }

    return STATUS_SUCCESS;
}

/*++

    itunes wrapper

--*/


NTSTATUS
iTunesHelper::
SapExchangeData(
    ULONG_PTR       certType,
    PFAIR_PLAY_HW_INFO      deviceId,
    HANDLE          sapSession,
    PVOID           certData,
    ULONG_PTR       certSize,
    PVOID*          output,
    PULONG_PTR      outputSize
)
{
    BOOLEAN continueSync = TRUE;

    return this->iTunes.sapExchangeData(certType, deviceId, sapSession, certData, certSize, output, outputSize, &continueSync);
}

NTSTATUS
iTunesHelper::
SapSignData(
    HANDLE      sapSession,
    PVOID       data,
    ULONG_PTR   dataSize,
    PVOID*      signature,
    PULONG_PTR  signatureSize
)
{
    return this->iTunes.sapSignData(sapSession, data, dataSize, signature, signatureSize);
}

NTSTATUS iTunesHelper::FreeSessionData(PVOID data)
{
    return data != nullptr ? this->iTunes.freeSessionData(data) : STATUS_SUCCESS;
}

BOOL iTunesHelper::GetDeviceId(PFAIR_PLAY_HW_INFO deviceId, PFAIR_PLAY_HW_INFO deviceId2)
{
    if (deviceId != nullptr)
        this->iTunes.getDeviceId(deviceId);

    if (deviceId2 != nullptr)
        this->iTunes.getDeviceId2(deviceId2);

    return TRUE;
}

NTSTATUS iTunesHelper::KbsyncCreateSession(PHANDLE kbsyncSession, PFAIR_PLAY_HW_INFO machineId, PFAIR_PLAY_HW_INFO machineId2, PCSTR ScInfoPath)
{
    *kbsyncSession = nullptr;

    NTSTATUS st;

#if 0
    PKBSYNC_SESSION session;

    st = this->InitScInfo(&session);

    //this->iTunes.kbsyncInitSomething(session->session, 0, 0);
    *kbsyncSession = session->session;

#else

    st = this->iTunes.kbsyncCreateSession(machineId2, machineId, ScInfoPath, kbsyncSession);

    if (st == 0)
    {
        //st = this->iTunes.kbsyncInitSomething(*kbsyncSession, 0, 0);
    }

#endif

    return st;
}

NTSTATUS iTunesHelper::KbsyncCloseSession(HANDLE session)
{
    if (session == nullptr)
        return STATUS_INVALID_PARAMETER;

    return this->iTunes.kbsyncCloseSession(session);
}

NTSTATUS iTunesHelper::SapCreateSession(PHANDLE sapSession, PFAIR_PLAY_HW_INFO deviceId)
{
    return this->iTunes.sapCreateSession(sapSession, deviceId);
}

NTSTATUS iTunesHelper::SapCloseSession(HANDLE sapSession)
{
    return this->iTunes.sapCloseSession(sapSession);
}

NTSTATUS iTunesHelper::SapCreatePrimeSignature(HANDLE sapSession, PVOID* output, PULONG_PTR outputSize)
{
    return this->iTunes.sapCreateActionSignature(sapSession, 0x64, 0, output, outputSize);
}

NTSTATUS iTunesHelper::SapVerifyPrimeSignature(HANDLE sapSession, PVOID signature, ULONG_PTR signatureSize)
{
    return this->iTunes.sapVerifyPrimeSignature(sapSession, signature, signatureSize, nullptr, nullptr);
}

NTSTATUS
iTunesHelper::
AirFairVerifyRequest(
    ULONG_PTR   grappaSessionId,
    PVOID       afsyncRequest,
    ULONG_PTR   requestSize,
    PVOID       afsyncRequestSignature,
    ULONG_PTR   signatureSize
)
{
    return this->iTunes.airFairVerifyRequest((ULONG)grappaSessionId, afsyncRequest, requestSize, afsyncRequestSignature, signatureSize);
}

NTSTATUS
iTunesHelper::
AirFairSyncCreateSession(
    PHANDLE                 afsyncSession,
    HANDLE                  kbsyncSession,
    PVOID                   fairPlayCertificate,
    ULONG_PTR               certificateSize,
    PFAIR_PLAY_HW_INFO              fairPlayGuid,
    PAIR_FAIR_DEVICE_INFO   deviceInfo,
    ULONG                   flags
)
{
    return this->iTunes.airFairSyncCreateSession(
                kbsyncSession,
                fairPlayCertificate,
                certificateSize,
                fairPlayGuid,
                deviceInfo,
                flags,
                afsyncSession
            );
}

NTSTATUS
iTunesHelper::
AirFairSyncSetRequest(
    HANDLE      afsyncSession,
    PVOID       afsyncRequest,
    ULONG_PTR   requestSize,
    PVOID       ICInfo,
    ULONG_PTR   ICInfoSize
)
{
    return this->iTunes.airFairSyncSetRequest(afsyncSession, afsyncRequest, requestSize, ICInfo, ICInfoSize);
}

NTSTATUS
iTunesHelper::
AirFairSyncAddAccount(
    HANDLE      kbsyncSession,
    PFAIR_PLAY_HW_INFO  machineId2,
    HANDLE      afsyncSession,
    ULONG64     dsPersonId,
    ULONG       what1,
    ULONG       what2
)
{
    //((NTSTATUS(CDECL*)(...))(PtrAdd(this->iTunesBase, 0x2E9C0)))(kbsyncSession, machineId2, dsPersonId);
    //this->iTunes.KbsyncAuthorizeDsid(kbsyncSession, dsPersonId, 0);
    //this->iTunes.KbsyncDsidBindMachine(afsyncSession, machineId2, dsPersonId);
    return this->iTunes.airFairSyncAddAccount(afsyncSession, dsPersonId, what1, what2);
}

NTSTATUS
iTunesHelper::
AirFairSyncGetAuthorizedAccount(
    HANDLE                      afsyncSession,
    PFAIR_PLAY_HW_INFO                  fairPlayGuid,
    ULONG_PTR                   deviceType,
    PVOID                       afsyncRequest,
    ULONG_PTR                   requestSize,
    PAIR_FAIR_AUTHORIZED_DSID*  dsid,
    PULONG_PTR                  count
)
{
    *dsid = nullptr;
    *count = 0;
    return this->iTunes.airFairSyncGetAuthorizedAccount(afsyncSession, fairPlayGuid, (USHORT)deviceType, afsyncRequest, requestSize, (PVOID *)dsid, (PULONG)count);
}

NTSTATUS
iTunesHelper::
AirFairSyncGetResponse(
    HANDLE      afsyncSession,
    PVOID*      afsyncResponse,
    PULONG      responseSize
)
{
    PVOID someData = nullptr;
    ULONG dataSize = 0;

    *afsyncResponse = nullptr;
    *responseSize = 0;
    someData = nullptr;

    NTSTATUS st = this->iTunes.airFairSyncGetResponse(afsyncSession, afsyncResponse, responseSize, &someData, &dataSize);

    if (st == STATUS_SUCCESS)
    {
        FreeSessionData(someData);
    }

    return st;
}

NTSTATUS
iTunesHelper::
AirFairSyncReset(
    HANDLE afsyncSession
)
{
    return this->iTunes.airFairSyncGetResponse(afsyncSession, nullptr, nullptr, nullptr, nullptr);
}

NTSTATUS
iTunesHelper::
AirFairSyncSignData(
    ULONG       grappaSessionId,
    PVOID       data,
    ULONG_PTR   dataLength,
    PVOID*      signature,
    PULONG      signatureLength
)
{
    return iTunes.airFairSyncSignData(grappaSessionId, data, dataLength, signature, signatureLength);
}
