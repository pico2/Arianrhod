#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")
#pragma comment(lib, "WS2_32.lib")

#define WINVER  0x602

#include "MyLibrary.cpp"
#include <Mstcpip.h>
#include "Export.h"

ML_OVERLOAD_NEW

#define SELF_THUNK_MAGIC    TAG4('TDAP')

TYPE_OF(NtDeviceIoControlFile)* StubNtDeviceIoControlFile;

static union
{
    TYPE_OF(SetTimer)*              StubSetTimer;
    TYPE_OF(SetCoalescableTimer)*   StubSetCoalescableTimer;
};

#pragma pack(push, 1)

typedef struct
{
    ULONG Code;             // 0x00
    ULONG Index;            // 0x04
    DUMMY_STRUCT(0x14);     // 0x08
    ULONG DataLength;       // 0x1C
    BYTE  Data[1];          // 0x20

} TD_ALIVE_PACKET, *PTD_ALIVE_PACKET;

#pragma pack(pop)

#define TD_ALIVE_PACKET_SIZE    sizeof(*((PTD_ALIVE_PACKET)0)) - sizeof(((PTD_ALIVE_PACKET)0)->Data)

static union
{
    TD_ALIVE_PACKET GlobalPacket;
    BYTE            PacketBuffer[0x1000];
};

BOOL        Exiting;
ULONG_PTR   SendLength;

VOID SaveAlivePacket(PAFD_SEND_INFO_UDP UdpInfo, ULONG_PTR Length)
{
    PTD_ALIVE_PACKET Packet;

    //static BOOL Enable = FALSE; if (!Enable) return;

    if (FindThreadFrame(SELF_THUNK_MAGIC) != NULL)
        return;

    Packet = (PTD_ALIVE_PACKET)UdpInfo->BufferArray->Buffer;

    if (Packet == NULL)
        return;

    if (UdpInfo->BufferArray->Length == 0)
        return;

    if (Length < TD_ALIVE_PACKET_SIZE)
        return;

    if (Packet->Code < 0x60 || Packet->Code > 0xFF)
        return;

    if (Packet->DataLength + TD_ALIVE_PACKET_SIZE > Length)
        return;

    ZeroMemory(&Packet->Data, Packet->DataLength);
    CopyMemory(&GlobalPacket, Packet, Length);

    SendLength = Length;
}

VOID SaveAlivePacketSafe(PAFD_SEND_INFO_UDP UdpInfo, ULONG_PTR Length)
{
    SEH_TRY
    {
        SaveAlivePacket(UdpInfo, Length);
    }
    SEH_EXCEPT(EXCEPTION_EXECUTE_HANDLER)
    {
        ;
    }
}

NTSTATUS
NTAPI
TdDeviceIoControlFile(
    HANDLE              FileHandle,
    HANDLE              Event,
    PIO_APC_ROUTINE     ApcRoutine,
    PVOID               ApcContext,
    PIO_STATUS_BLOCK    IoStatusBlock,
    ULONG               IoControlCode,
    PVOID               InputBuffer,
    ULONG               InputBufferLength,
    PVOID               OutputBuffer,
    ULONG               OutputBufferLength
)
{
    NTSTATUS Status;

    Status = StubNtDeviceIoControlFile(
                FileHandle,
                Event,
                ApcRoutine,
                ApcContext,
                IoStatusBlock,
                IoControlCode,
                InputBuffer,
                InputBufferLength,
                OutputBuffer,
                OutputBufferLength
            );

    FAIL_RETURN(Status);

    switch (IoControlCode)
    {
        case IOCTL_AFD_SEND_DATAGRAM:
            SaveAlivePacketSafe((PAFD_SEND_INFO_UDP)InputBuffer, IoStatusBlock->Information);
            break;
    }

    return Status;
}

UINT_PTR
NTAPI
TdSetTimer(
    HWND        hWnd,
    UINT_PTR    IDEvent,
    UINT        Elapse,
    TIMERPROC   TimerFunction
)
{
    if (Elapse > 55000 && TimerFunction == NULL)
    {
        Elapse = USER_TIMER_MAXIMUM;
        return 0;
    }

    return StubSetTimer(hWnd, IDEvent, Elapse, TimerFunction);
}

BOOL UnInitialize(PVOID BaseAddress)
{
    Exiting = TRUE;
    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    ml::MlInitialize();

    PLDR_MODULE ExeModule;

    LdrDisableThreadCalloutsForDll(BaseAddress);

    ExeModule = FindLdrModuleByHandle(NULL);

    if (RtlEqualUnicodeString(&ExeModule->BaseDllName, &WCS2US(L"ThunderPlatform.exe"), TRUE))
    {
        PLDR_MODULE User32 = FindLdrModuleByName(&WCS2US(L"USER32.dll"));

        MEMORY_FUNCTION_PATCH f[] =
        {
            EAT_HOOK_JUMP_HASH(User32->DllBase, USER32_SetTimer, TdSetTimer, StubSetTimer),
            INLINE_HOOK_JUMP(NtDeviceIoControlFile, TdDeviceIoControlFile, StubNtDeviceIoControlFile),
        };

        Nt_PatchMemory(NULL, 0, f, countof(f));

        Ps::CreateThread(
            (PTHREAD_START_ROUTINE)([](PVOID) -> ULONG
            {
                LARGE_INTEGER   Interval;
                SOCKADDR_IN     Address;

                FormatTimeOut(&Interval, 55000);

                ZeroMemory(&Address, sizeof(Address));

                Address.sin_family      = AF_INET;
                Address.sin_port        = ML_PORT(6200);
                Address.sin_addr.s_addr = ML_IP_ADDRESS(221,238,24,116);

                auto SendAlivePacket = [&] ()
                        {
                            SOCKET Sock;

                            if (SendLength == 0)
                                return;

                            Sock = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
                            if (Sock == INVALID_SOCKET)
                                return;

                            TEB_ACTIVE_FRAME Thunk;

                            Thunk.Context = SELF_THUNK_MAGIC;
                            Thunk.Push();

                            ++GlobalPacket.Index;
                            sendto(Sock, (PCHAR)&GlobalPacket, SendLength, 0, (PSOCKADDR)&Address, sizeof(Address));

                            Thunk.Pop();

                            closesocket(Sock);
                        };

                do
                {
                    SendAlivePacket();
                    NtDelayExecution(FALSE, &Interval);
                } while (!Exiting);

                return 0;
            }),
            0
        );
    }
    else if (RtlEqualUnicodeString(&ExeModule->BaseDllName, &WCS2US(L"Thunder.exe"), TRUE))
    {
        PLDR_MODULE User32;

        User32 = FindLdrModuleByName(&WCS2US(L"USER32.dll"));

        MEMORY_FUNCTION_PATCH f[] =
        {
            EAT_HOOK_JUMP_HASH(User32->DllBase, USER32_SetTimer, TdSetTimer, StubSetTimer),
        };

        Nt_PatchMemory(NULL, 0, f, countof(f));
    }

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
