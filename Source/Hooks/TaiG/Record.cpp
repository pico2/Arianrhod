#include "TaiG2.h"

using ml::String;

enum
{
    STATE_NONE,
    STATE_SERVICE_START,
    STATE_SERVICE_SEND,
    STATE_SERVICE_RECV,
    STATE_AFC_SEND,
    STATE_AFC_READ,
};

LONG (CDECL *StubJailBreak)(HANDLE Device);

TYPE_OF(iTunesApi::AFC::AFCConnectionCreate)            StubAFCConnectionCreate;
TYPE_OF(iTunesApi::AFC::AFCSendData)                    StubAFCSendData;
TYPE_OF(iTunesApi::AFC::AFCReadData)                    StubAFCReadData;

TYPE_OF(iTunesApi::AMD::AMDServiceConnectionSend)       StubAMDServiceConnectionSend;
TYPE_OF(iTunesApi::AMD::AMDServiceConnectionReceive)    StubAMDServiceConnectionReceive;
TYPE_OF(iTunesApi::AMD::AMDeviceSecureStartService)     StubAMDeviceSecureStartService;
TYPE_OF(iTunesApi::AMD::AMDServiceConnectionInvalidate) StubAMDServiceConnectionInvalidate;

LPWSPSTARTUP    StubWSPStartup;
LPWSPSEND       StubWSPSend;
LPWSPRECV       StubWSPRecv;

ULONG_PTR PreviousState = STATE_NONE;
ULONG_PTR JailBreakThreadId;

VOID DumpData(ULONG_PTR State, PCWSTR Prefix, PVOID Buffer, ULONG_PTR Size, PCSTR ServiceName = nullptr)
{
    static ULONG_PTR Sequence;

    BOOL CreateNew = FALSE;

    if (CurrentTid() != JailBreakThreadId) return;

    if (PreviousState != State || State == STATE_SERVICE_START)
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

VOID DumpData(ULONG_PTR State, PCWSTR Prefix, const String &str, PCSTR ServiceName = nullptr)
{
    return DumpData(State, Prefix, (PWSTR)str, str.GetCount() * 2, ServiceName);
}

NTSTATUS CDECL TGAFCSendData(AFCConnection Connection, PVOID Buffer, LONG Length)
{
    NTSTATUS st = StubAFCSendData(Connection, Buffer, Length);

    DumpData(STATE_AFC_SEND, String::Format(L"AFCSendData@%p", Connection), Buffer, Length);

    return st;
}

NTSTATUS CDECL TGAFCReadData(AFCConnection Connection, PVOID Buffer, LONG Length)
{
    NTSTATUS st = StubAFCReadData(Connection, Buffer, Length);

    DumpData(STATE_AFC_READ, String::Format(L"AFCReadData@%p", Connection), Buffer, Length);

    return st;
}

LONG CDECL TGAMDServiceConnectionSend(CFServiceConnection Connection, PVOID Buffer, ULONG Length)
{
    LONG ret = StubAMDServiceConnectionSend(Connection, Buffer, Length);

    DumpData(STATE_SERVICE_SEND, L"AMDServiceConnectionSend", Buffer, ret, (PCSTR)PtrAdd(Connection, 0x18));

    return ret;
}

LONG CDECL TGAMDServiceConnectionReceive(CFServiceConnection Connection, PVOID Buffer, ULONG Length)
{
    LONG ret = StubAMDServiceConnectionReceive(Connection, Buffer, Length);

    DumpData(STATE_SERVICE_RECV, L"AMDServiceConnectionReceive", Buffer, ret, (PCSTR)PtrAdd(Connection, 0x18));

    return ret;
}

NTSTATUS
CDECL
TGAMDeviceSecureStartService(
    HANDLE                  Device,
    CFStringRef             ServiceName,
    LONG                    Option,
    PCFServiceConnection    Connection
)
{
    NTSTATUS st = StubAMDeviceSecureStartService(Device, ServiceName, Option, Connection);

    if (st != STATUS_SUCCESS)
        return st;

    CFIndex Length = iTunesApi::CF::CFStringGetLength(ServiceName);
    PWSTR Buffer = (PWSTR)AllocStack(Length * 2 + 2);

    iTunesApi::CF::CFStringGetCString(ServiceName, Buffer, Length * 2 + 2, kCFStringEncodingUTF16LE);

    Buffer[Length] = 0;

    DumpData(
        STATE_SERVICE_START,
        L"AMDeviceSecureStartService",
        String::Format(L"%s: %p: %p", Buffer, iTunesApi::AMD::AMDServiceConnectionGetSocket(*Connection), *Connection)
    );

    return st;
}

VOID CDECL TGAMDServiceConnectionInvalidate(CFServiceConnection Connection)
{
    SOCKET sock = iTunesApi::AMD::AMDServiceConnectionGetSocket(Connection);

    if (sock != INVALID_SOCKET)
    {
        DumpData(
            STATE_SERVICE_START,
            L"AMDServiceConnectionInvalidate",
            String::Format(L"%S: %p: %p", (PSTR)PtrAdd(Connection, 0x18), sock, Connection)
        );
    }

    return StubAMDServiceConnectionInvalidate(Connection);
}

AFCConnection
CDECL
TGAFCConnectionCreate(
    CFAllocatorRef  Allocator,
    SOCKET          ServiceSocket,
    PVOID           Unknown1,
    PVOID           Unknown2,
    ULONG           Timeout
)
{
    AFCConnection Connection = StubAFCConnectionCreate(Allocator, ServiceSocket, Unknown1, Unknown2, Timeout);

    if (Connection != nullptr)
    {
        DumpData(
            STATE_SERVICE_START,
            L"AFCConnectionCreate",
            String::Format(L"Create %p from %p", Connection, ServiceSocket)
        );
    }

    return Connection;
}

INT
NTAPI
WSPSend(
    SOCKET                              s,
    LPWSABUF                            Buffers,
    DWORD                               BufferCount,
    LPDWORD                             NumberOfBytesSent,
    DWORD                               Flags,
    LPWSAOVERLAPPED                     Overlapped,
    LPWSAOVERLAPPED_COMPLETION_ROUTINE  CompletionRoutine,
    LPWSATHREADID                       ThreadId,
    LPINT                               Errno
)
{
    return StubWSPSend(s, Buffers, BufferCount, NumberOfBytesSent, Flags, Overlapped, CompletionRoutine, ThreadId, Errno);
}

INT
NTAPI
WSPRecv(
    SOCKET                              s,
    LPWSABUF                            Buffers,
    DWORD                               BufferCount,
    LPDWORD                             NumberOfBytesRecvd,
    LPDWORD                             Flags,
    LPWSAOVERLAPPED                     Overlapped,
    LPWSAOVERLAPPED_COMPLETION_ROUTINE  CompletionRoutine,
    LPWSATHREADID                       ThreadId,
    LPINT                               Errno
)
{
    return StubWSPRecv(s, Buffers, BufferCount, NumberOfBytesRecvd, Flags, Overlapped, CompletionRoutine, ThreadId, Errno);
}

int
NTAPI
WSPStartup(
  WORD                  VersionRequested,
  LPWSPDATA             WSPData,
  LPWSAPROTOCOL_INFOW   ProtocolInfo,
  WSPUPCALLTABLE        callTable,
  LPWSPPROC_TABLE       ProcTable
)
{
    int r = StubWSPStartup(VersionRequested, WSPData, ProtocolInfo, callTable, ProcTable);

    if (r == 0)
    {
        StubWSPSend = ProcTable->lpWSPSend;
        StubWSPRecv = ProcTable->lpWSPRecv;

        ProcTable->lpWSPSend = WSPSend;
        ProcTable->lpWSPRecv = WSPRecv;
    }

    return r;
}

LONG CDECL JailBreak(HANDLE Device)
{
    JailBreakThreadId = CurrentTid();
    return StubJailBreak(Device);
}

NTSTATUS Record_Initialize(PVOID TaiGBase)
{
    using namespace Mp;

    PVOID mswsock;

    NtFileDisk().CreateDirectory(L"dumps");

    iTunesApi::Initialize();

    mswsock = LoadDll(L"mswsock.dll");

    PATCH_MEMORY_DATA p[] =
    {
        FunctionJumpRva(0x18DD0, JailBreak, &StubJailBreak),

        FunctionJumpVa(iTunesApi::AFC::AFCConnectionCreate,             TGAFCConnectionCreate,              &StubAFCConnectionCreate),
        FunctionJumpVa(iTunesApi::AFC::AFCSendData,                     TGAFCSendData,                      &StubAFCSendData),
        FunctionJumpVa(iTunesApi::AFC::AFCReadData,                     TGAFCReadData,                      &StubAFCReadData),
        FunctionJumpVa(iTunesApi::AMD::AMDServiceConnectionSend,        TGAMDServiceConnectionSend,         &StubAMDServiceConnectionSend),
        FunctionJumpVa(iTunesApi::AMD::AMDServiceConnectionReceive,     TGAMDServiceConnectionReceive,      &StubAMDServiceConnectionReceive),
        FunctionJumpVa(iTunesApi::AMD::AMDeviceSecureStartService,      TGAMDeviceSecureStartService,       &StubAMDeviceSecureStartService),
        FunctionJumpVa(iTunesApi::AMD::AMDServiceConnectionInvalidate,  TGAMDServiceConnectionInvalidate,   &StubAMDServiceConnectionInvalidate),

        FunctionJumpVa(GetRoutineAddress(mswsock, "WSPStartup"), WSPStartup, &StubWSPStartup),
    };

    PatchMemory(p, countof(p), TaiGBase);

    return STATUS_SUCCESS;
}
