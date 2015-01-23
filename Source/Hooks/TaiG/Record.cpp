#include "TaiG2.h"

enum
{
    STATE_NONE,
    STATE_SERVICE_SEND,
    STATE_SERVICE_RECV,
    STATE_AFC_SEND,
    STATE_AFC_READ,
};

LONG (CDECL *StubJailBreak)(HANDLE Device);
NTSTATUS (CDECL *StubTGAFCSendData)(AFCConnection Connection, PVOID Buffer, LONG Length);
NTSTATUS (CDECL *StubTGAFCReadData)(AFCConnection Connection, PVOID Buffer, LONG Length);
LONG (CDECL *StubTGAMDServiceConnectionSend)(CFServiceConnection Connection, PVOID Buffer, ULONG Length);
LONG (CDECL *StubTGAMDServiceConnectionReceive)(CFServiceConnection Connection, PVOID Buffer, ULONG Length);

ULONG_PTR PreviousState = STATE_NONE;
ULONG_PTR JailBreakThreadId;

VOID DumpData(ULONG_PTR State, PCWSTR Prefix, PVOID Buffer, ULONG_PTR Size, PCSTR ServiceName = nullptr)
{
    static ULONG_PTR Sequence;

    BOOL CreateNew = FALSE;

    if (CurrentTid() != JailBreakThreadId) return;

    if (PreviousState != State)
    {
        ++Sequence;
        PreviousState = State;

        CreateNew = TRUE;
    }

    ULONG_PTR Length;
    NtFileDisk bin;
    WCHAR name[MAX_NTPATH];

    Length = swprintf(name, L"dumps\\%05d_%s", Sequence, Prefix);
    if (ServiceName != nullptr)
        swprintf(name + Length, L"_%S", ServiceName);

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

NTSTATUS CDECL TGAFCSendData(AFCConnection Connection, PVOID Buffer, LONG Length)
{
    NTSTATUS st = StubTGAFCSendData(Connection, Buffer, Length);

    DumpData(STATE_AFC_SEND, L"AFCSendData", Buffer, Length);

    return st;
}

NTSTATUS CDECL TGAFCReadData(AFCConnection Connection, PVOID Buffer, LONG Length)
{
    NTSTATUS st = StubTGAFCReadData(Connection, Buffer, Length);

    DumpData(STATE_AFC_READ, L"AFCReadData", Buffer, Length);

    return st;
}

LONG CDECL TGAMDServiceConnectionSend(CFServiceConnection Connection, PVOID Buffer, ULONG Length)
{
    LONG ret = StubTGAMDServiceConnectionSend(Connection, Buffer, Length);

    DumpData(STATE_SERVICE_SEND, L"AMDServiceConnectionSend", Buffer, ret, (PCSTR)PtrAdd(Connection, 0x18));

    return ret;
}

LONG CDECL TGAMDServiceConnectionReceive(CFServiceConnection Connection, PVOID Buffer, ULONG Length)
{
    LONG ret = StubTGAMDServiceConnectionReceive(Connection, Buffer, Length);

    DumpData(STATE_SERVICE_RECV, L"AMDServiceConnectionReceive", Buffer, ret, (PCSTR)PtrAdd(Connection, 0x18));

    return ret;
}

LONG CDECL JailBreak(HANDLE Device)
{
    JailBreakThreadId = CurrentTid();
    return StubJailBreak(Device);
}

NTSTATUS Record_Initialize(PVOID TaiGBase)
{
    using namespace Mp;

    NtFileDisk().CreateDirectory(L"dumps");

    iTunesApi::Initialize();

    PATCH_MEMORY_DATA p[] =
    {
        FunctionJumpRva(0x18DD0, JailBreak, &StubJailBreak),
        FunctionJumpVa(iTunesApi::AFC::AFCSendData,                 TGAFCSendData,                  &StubTGAFCSendData),
        FunctionJumpVa(iTunesApi::AFC::AFCReadData,                 TGAFCReadData,                  &StubTGAFCReadData),
        FunctionJumpVa(iTunesApi::AMD::AMDServiceConnectionSend,    TGAMDServiceConnectionSend,     &StubTGAMDServiceConnectionSend),
        FunctionJumpVa(iTunesApi::AMD::AMDServiceConnectionReceive, TGAMDServiceConnectionReceive,  &StubTGAMDServiceConnectionReceive),
    };

    PatchMemory(p, countof(p), TaiGBase);

    return STATUS_SUCCESS;
}
