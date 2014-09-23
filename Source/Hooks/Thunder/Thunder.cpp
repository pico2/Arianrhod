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

struct lua_State;

typedef struct
{
    PCSTR name;
    PVOID func;
    ULONG permission;

} XLLRTGlobalAPI, *PXLLRTGlobalAPI;

API_POINTER(NtDeviceIoControlFile)  StubNtDeviceIoControlFile;
int (CDECL *StubCreateAccelerateTaskMap)(lua_State *L);

PCSTR (CDECL *luaL_checklstring)(lua_State *L, int narg, size_t *l);

static union
{
    API_POINTER(SetTimer)               StubSetTimer;
    API_POINTER(SetCoalescableTimer)    StubSetCoalescableTimer;
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

int CDECL CreateAccelerateTaskMap(lua_State *L)
{
    size_t Length;
    PCSTR UserData;
    PSTR Result;

    UserData = luaL_checklstring(L, 5, &Length);

    LOOP_ONCE
    {
        if (UserData == nullptr || Length == 0)
            break;

        // {"CommitGcid":"","Message":"stupid","Result":0,"SubId":10}

        if (strstr(UserData, "CommitGcid") == nullptr)
            break;

        if (strstr(UserData, "Message") == nullptr)
            break;

        if (strstr(UserData, "SubId") == nullptr)
            break;

        Result = strstr(UserData, "\"Result\":");
        if (Result == nullptr)
            break;

        CopyMemory(Result, "\"Result\":0,", 11);
        Result += 11;

        while (*Result != '"' && *Result != '}')
        {
            *Result++ = ' ';
        }
    }

    return StubCreateAccelerateTaskMap(L);
}

PXLLRTGlobalAPI LookupLRTApiEntry(PLDR_MODULE Module, PCSTR ApiName)
{
    PVOID name;

    name = SearchStringReference(Module, (PVOID)ApiName, StrLengthA(ApiName) + 1);

    return name == nullptr ? nullptr : FIELD_BASE(name, XLLRTGlobalAPI, name);
}

PVOID LookupCreateAccelerateTaskMap()
{
    PLDR_MODULE     DownloadKernel;
    PXLLRTGlobalAPI Entry;

    static CHAR FunctionName[] = "CreateAccelerateTaskMap";

    DownloadKernel = FindLdrModuleByName(&USTR(L"DownloadKernel.dll"));
    if (DownloadKernel == nullptr)
        return IMAGE_INVALID_VA;

    Entry = LookupLRTApiEntry(DownloadKernel, "CreateAccelerateTaskMap");
    if (Entry == nullptr)
        return IMAGE_INVALID_VA;

    return Entry->func;
}

BOOL UnInitialize(PVOID BaseAddress)
{
    Exiting = TRUE;
    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    using namespace Mp;

    ml::MlInitialize();

    PLDR_MODULE ExeModule;

    LdrDisableThreadCalloutsForDll(BaseAddress);

    ExeModule = FindLdrModuleByHandle(NULL);

    if (RtlEqualUnicodeString(&ExeModule->BaseDllName, &WCS2US(L"ThunderPlatform.exe"), TRUE))
    {
        PLDR_MODULE User32 = FindLdrModuleByName(&WCS2US(L"USER32.dll"));

        PATCH_MEMORY_DATA f[] =
        {
            FunctionJumpVa(LookupExportTable(User32->DllBase, USER32_SetTimer), TdSetTimer, &StubSetTimer),
            FunctionJumpVa(NtDeviceIoControlFile, TdDeviceIoControlFile, &StubNtDeviceIoControlFile),
        };

        PatchMemory(f, countof(f));

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

                            //Thunk.Pop();

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
        PVOID luart;
        PLDR_MODULE User32;

        User32 = FindLdrModuleByName(&WCS2US(L"USER32.dll"));

        PATCH_MEMORY_DATA f[] =
        {
            FunctionJumpVa(LookupCreateAccelerateTaskMap(), CreateAccelerateTaskMap, &StubCreateAccelerateTaskMap),
            FunctionJumpVa(LookupExportTable(User32->DllBase, USER32_SetTimer), TdSetTimer, &StubSetTimer),
        };

        PatchMemory(f, countof(f));

        luart = LoadDll(L"XLLuaRuntime.dll");
        *(PVOID *)&luaL_checklstring = GetRoutineAddress(luart, "luaL_checklstring");
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
