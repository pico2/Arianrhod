#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text /MERGE:.text1=.text /SECTION:.idata,ERW")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")

#pragma comment(linker, "/EXPORT:GetAdaptersInfo=IPHLPAPI.GetAdaptersInfo")
#pragma comment(linker, "/EXPORT:GetAdaptersAddresses=IPHLPAPI.GetAdaptersAddresses")
#pragma comment(linker, "/EXPORT:GetModuleInformation=PSAPI.GetModuleInformation")

#include "ml.cpp"
#include "iTunes/iTunes.h"

ML_OVERLOAD_NEW

using ml::String;
using namespace iTunesApi::AMD;

enum
{
    STATE_NONE,
    STATE_SERVICE_START,
    STATE_SERVICE_SEND,
    STATE_SERVICE_RECV,
    STATE_AFC_SEND,
    STATE_AFC_READ,
    STATE_SOCKET_SEND,
    STATE_SOCKET_RECV,
};

ULONG_PTR PreviousState = STATE_NONE;

TYPE_OF(iTunesApi::AMD::AMDServiceConnectionSend)       StubAMDServiceConnectionSend;
TYPE_OF(iTunesApi::AMD::AMDServiceConnectionReceive)    StubAMDServiceConnectionReceive;

VOID DumpData(ULONG_PTR State, PCWSTR Prefix, PVOID Buffer, ULONG_PTR Size, PCSTR ServiceName = nullptr)
{
    static ULONG_PTR Sequence;

    if (Size == 4)
        return;

    BOOL CreateNew = FALSE;

    if (State == STATE_SOCKET_SEND || State == STATE_SOCKET_RECV)
    {
        CreateNew = TRUE;
    }
    else if (PreviousState != State || State == STATE_SERVICE_START)
    {
        ++Sequence;
        PreviousState = State;
        CreateNew = TRUE;
    }

    ULONG_PTR Length;
    NtFileDisk bin;
    WCHAR name[MAX_NTPATH];

    static SYSTEMTIME LastTime;

    if (CreateNew)
        GetLocalTime(&LastTime);

    Length = swprintf(name, L"dumps\\[%02d-%02d-%02d.%04d] %05d_%s",
                    LastTime.wHour, LastTime.wMinute, LastTime.wSecond, LastTime.wMilliseconds, Sequence, Prefix
                );
    if (ServiceName != nullptr)
        swprintf(name + Length, L"_%S", ServiceName);

    wcscat(name, L".xml");

    if (CreateNew == FALSE)
    {
        bin.Append(name);
    }
    else
    {
        bin.Create(name);
    }

    bin.Write(Buffer, Size);
}

VOID DumpData(ULONG_PTR State, PCWSTR Prefix, const String &str, PCSTR ServiceName = nullptr)
{
    return DumpData(State, Prefix, (PWSTR)str, str.GetCount() * 2, ServiceName);
}

LONG CDECL TGAMDServiceConnectionSend(CFServiceRef Connection, PVOID Buffer, ULONG Length)
{
    LONG ret = StubAMDServiceConnectionSend(Connection, Buffer, Length);

    DumpData(STATE_SERVICE_SEND, L"AMDServiceConnectionSend", Buffer, ret, (PCSTR)PtrAdd(Connection, 0x18));

    return ret;
}

LONG CDECL TGAMDServiceConnectionReceive(CFServiceRef Connection, PVOID Buffer, ULONG Length)
{
    LONG ret = StubAMDServiceConnectionReceive(Connection, Buffer, Length);

    DumpData(STATE_SERVICE_RECV, L"AMDServiceConnectionReceive", Buffer, ret, (PCSTR)PtrAdd(Connection, 0x18));

    return ret;
}

TYPE_OF(iTunesApi::AMD::AMDServiceConnectionSend)       PtrAMDServiceConnectionSend = TGAMDServiceConnectionSend;
TYPE_OF(iTunesApi::AMD::AMDServiceConnectionReceive)    PtrAMDServiceConnectionReceive = TGAMDServiceConnectionReceive;

EXTC_EXPORT VOID CDECL e()
{
    NtFileDisk().CreateDirectory(L"Dumps");

    iTunesApi::Initialize();
    //iTunesApi::AMD::Initialize();

    PrintConsole(L"%s = %p\n", MOBILE_DEVICE_DLL, LoadDll(MOBILE_DEVICE_DLL));
    PrintConsole(L"AMDServiceConnectionSend = %p\n", AMDServiceConnectionSend);
    PrintConsole(L"AMDServiceConnectionReceive = %p\n", AMDServiceConnectionReceive);

    using namespace Mp;

    PATCH_MEMORY_DATA p[] =
    {
        FunctionJumpVa(AMDServiceConnectionSend, TGAMDServiceConnectionSend, &StubAMDServiceConnectionSend),
        FunctionJumpVa(AMDServiceConnectionReceive, TGAMDServiceConnectionReceive, &StubAMDServiceConnectionReceive),
    };

    PatchMemory(p, countof(p), nullptr);

    PrintConsole(L"patch done\n");

    return;

    PLDR_MODULE module;

    module = FindLdrModuleByName(PUSTR(L"iOSDevice.dll"));

    Mm::ProtectMemory(CurrentProcess, PtrAdd(module->DllBase, 0x16b43C), MEMORY_PAGE_SIZE, PAGE_READWRITE);

    *(PVOID *)PtrAdd(module->DllBase, 0x16b43C) = &PtrAMDServiceConnectionSend;
    *(PVOID *)PtrAdd(module->DllBase, 0x16b440) = &PtrAMDServiceConnectionReceive;
}

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    LdrDisableThreadCalloutsForDll(BaseAddress);
    ml::MlInitialize();
    e();

    using namespace Mp;

    static VOID (CDECL *StubStartiOSLayer)(PVOID);

    auto StartiOSLayer = [] (PVOID cb)
    {
        StubStartiOSLayer(cb);
        e();
    };

    BaseAddress = GetExeModuleHandle();

    PATCH_MEMORY_DATA p[] =
    {
        FunctionJumpVa(GetRoutineAddress(BaseAddress, "StartiOSLayer"), (TYPE_OF(StubStartiOSLayer))StartiOSLayer, &StubStartiOSLayer),
    };

    //PatchMemory(p, countof(p), nullptr);

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
