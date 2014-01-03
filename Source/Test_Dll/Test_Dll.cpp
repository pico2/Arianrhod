#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text /MERGE:.text1=.text /SECTION:.idata,ERW")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")
#pragma comment(linker, "/EXPORT:TransparentBlt=MSIMG32.TransparentBlt")
#pragma comment(lib, "WS2_32.lib")

#include "MyLibrary.cpp"

typedef struct STL60_STRING
{
    DUMMY_STRUCT(4);

    union
    {
        CHAR SmallBuffer[0x10];
        PSTR Buffer;
    };

    ULONG Length;
    ULONG MaximumLength;

    STL60_STRING()
    {
        SmallBuffer[0] = 0;
        Length = 0;
        MaximumLength = countof(SmallBuffer);
    }

    PSTR GetBuffer()
    {
        return this->Length < countof(SmallBuffer) ? SmallBuffer : Buffer;
    }

} STL60_STRING, *PSTL60_STRING;

template<class TYPE>
struct STL60_VECTOR
{
    DUMMY_STRUCT(4);

    TYPE* Begin;
    TYPE* End;

    ULONG_PTR GetSize()
    {
        return End - Begin;
    }

    TYPE& operator[](int index)
    {
        return Begin[index];
    }
};

typedef struct
{
    ULONG   Ip;
    USHORT  Port;

    DUMMY_STRUCT(0x2A);

} NODE_OBJECT, *PNODE_OBJECT;

VOID (CDECL *StubAppendString)(STL60_STRING& NewString, STL60_STRING& String, PCSTR Append);

ULONG NodeIndex;

NAKED VOID SaveNodeIndex()
{
    INLINE_ASM
    {
        mov     eax, [ebp-38h];
        mov     NodeIndex, eax;
        mov     dword ptr [ebp-38h], 0;
        ret;
    }
}

VOID CDECL InitNodeName(STL60_STRING& NewString, STL60_STRING& String, PCSTR Append)
{
    AllocStack(16);

    PVOID*                      Ebp;
    CHAR                        Buffer[0x500];
    STL60_STRING                EmptyString;

    Ebp = (PVOID *)*((PVOID *)_AddressOfReturnAddress() - 1);

    STL60_VECTOR<PNODE_OBJECT>& NodeList = **(STL60_VECTOR<PNODE_OBJECT> **)PtrSub(Ebp, 0x2C);

    snprintf(
        Buffer,
        countof(Buffer),
        "%s %d.%d.%d.%d %s",
        String.GetBuffer(),
        LOBYTE(NodeList[NodeIndex]->Ip),
        HIBYTE(NodeList[NodeIndex]->Ip),
        LOBYTE(HIWORD(NodeList[NodeIndex]->Ip)),
        HIBYTE(HIWORD(NodeList[NodeIndex]->Ip)),
        Append
    );

    StubAppendString(NewString, EmptyString, Buffer);
}

API_POINTER(sendto)     stubsendto;
API_POINTER(recvfrom)   stubrecvfrom;

VOID show(PSOCKADDR_IN addr, PCWSTR prefix)
{
    if (addr->sin_addr.S_un.S_addr == ML_IP_ADDRESS(183, 136, 128, 196))
    {
        SYSTEMTIME st;

        GetLocalTime(&st);

        AllocConsole();
        PrintConsole(
            L"%02d:%02d:%02d.%03d %s %d.%d.%d.%d\n",
            st.wHour, st.wMinute, st.wSecond, st.wMilliseconds,
            prefix,
            addr->sin_addr.S_un.S_un_b.s_b1,
            addr->sin_addr.S_un.S_un_b.s_b2,
            addr->sin_addr.S_un.S_un_b.s_b3,
            addr->sin_addr.S_un.S_un_b.s_b4
        );
    }
}

int NTAPI xy_sendto(SOCKET s, PCSTR buf, int len, int flags, PSOCKADDR_IN to, int tolen)
{
    show(to, L"sendto");
    return stubsendto(s, buf, len, flags, (PSOCKADDR)to, tolen);
}

int NTAPI xy_recvfrom(SOCKET s, char* buf, int len, int flags, struct sockaddr* from, int *fromlen)
{
    int ret;

    ret = stubrecvfrom(s, buf, len, flags, from, fromlen);
    if (ret == SOCKET_ERROR)
        return ret;

    show((PSOCKADDR_IN)from, L"recvfrom");
    return ret;
}

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    LdrDisableThreadCalloutsForDll(BaseAddress);
    ml::MlInitialize();

    BaseAddress = FindLdrModuleByName(&USTR(L"js.dll"))->DllBase;

    MEMORY_PATCH p[] =
    {
        PATCH_MEMORY(0x00, 4, 0x73779),
        PATCH_MEMORY(0xEB, 1, 0x6D382),     // ping
        PATCH_MEMORY(0xEB, 1, 0x6D56D),
        PATCH_MEMORY(0xEB, 1, 0x6D477),
        PATCH_MEMORY(1, 4, 0x6FA73),      // timer
    };

    MEMORY_FUNCTION_PATCH f[] =
    {
        INLINE_HOOK_CALL_RVA_NULL(0x72A17, SaveNodeIndex),
        INLINE_HOOK_CALL_RVA(0x730C3, InitNodeName, StubAppendString),
        INLINE_HOOK_CALL_RVA(0x72F0C, InitNodeName, StubAppendString),
        INLINE_HOOK_JUMP(sendto, xy_sendto, stubsendto),
        INLINE_HOOK_JUMP(recvfrom, xy_recvfrom, stubrecvfrom),
    };

    Nt_PatchMemory(p, countof(p), f, countof(f), BaseAddress);

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
