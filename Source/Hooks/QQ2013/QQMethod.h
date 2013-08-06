
/***



***/

#define DECL_STATIC_METHOD_POINTER(cls, method) static TYPE_OF(&cls::method) Stub##method
#define INIT_STATIC_MEMBER(x) DECL_SELECTANY TYPE_OF(x) x = NULL
#define DETOUR_METHOD(cls, method, addr, ...) TYPE_OF(&cls::method) (method); *(PULONG_PTR)&(method) = addr; return (this->*method)(__VA_ARGS__)


struct CTXStringW
{
    PCWSTR Buffer;

    VOID Empty()
    {
        return (this->*StubEmpty)();
    }

    BOOL IsEmpty()
    {
        return (this->*StubIsEmpty)();
    }

    DECL_STATIC_METHOD_POINTER(CTXStringW, Empty);
    DECL_STATIC_METHOD_POINTER(CTXStringW, IsEmpty);
};

INIT_STATIC_MEMBER(CTXStringW::StubEmpty);
INIT_STATIC_MEMBER(CTXStringW::StubIsEmpty);

struct Util
{
    struct ChatSession
    {
        static BOOL (CDECL *OpenContactChatSession)(ULONG_PTR Uin, PVOID TXData);
        static HWND (CDECL *GetContactChatSessionMainHWND)(ULONG_PTR Uin);
    };

    struct Contact
    {
        static ULONG_PTR (*GetSelfUin)();
    };

    struct Group
    {
        static BOOL (CDECL *CheckMsgImage)(PVOID GroupObject, CTXStringW &Message);
    };
};

INIT_STATIC_MEMBER(Util::ChatSession::OpenContactChatSession);
INIT_STATIC_MEMBER(Util::ChatSession::GetContactChatSessionMainHWND);
INIT_STATIC_MEMBER(Util::Contact::GetSelfUin);
INIT_STATIC_MEMBER(Util::Group::CheckMsgImage);


typedef struct
{
    PCWSTR  DllName;
    PCSTR   FunctionName;
    PVOID   FuncAddress;

} FUNCTION_TABLE_INIT_ENTRY, *PFUNCTION_TABLE_INIT_ENTRY;

inline NTSTATUS InitializeQqFunctionTable()
{
    PVOID BaseAddress;
    PFUNCTION_TABLE_INIT_ENTRY Entry;

    static FUNCTION_TABLE_INIT_ENTRY InitEnties[] =
    {
        { L"Common.dll",        "?Empty@CTXStringW@@QAEXXZ",                                            &CTXStringW::StubEmpty },
        { L"Common.dll",        "?IsEmpty@CTXStringW@@QBE_NXZ",                                         &CTXStringW::StubIsEmpty },

        { L"AppUtil.dll",       "?OpenContactChatSession@ChatSession@Util@@YAXKPAUITXData@@@Z",         &Util::ChatSession::OpenContactChatSession },
        { L"AppUtil.dll",       "?GetContactChatSessionMainHWnd@ChatSession@Util@@YAPAUHWND__@@K@Z",    &Util::ChatSession::GetContactChatSessionMainHWND },

        { L"KernelUtil.dll",    "?GetSelfUin@Contact@Util@@YAKXZ",                                      &Util::Contact::GetSelfUin },
        { L"KernelUtil.dll",    "?CheckMsgImage@Group@Util@@YAHPAUITXMsgPack@@AAVCTXStringW@@@Z",       &Util::Group::CheckMsgImage },
    };


    BaseAddress = nullptr;

    FOR_EACH_ARRAY(Entry, InitEnties)
    {
        if (Entry == InitEnties)
        {
            BaseAddress = Ldr::LoadDll(Entry->DllName);
        }
        else if(Entry->DllName != Entry[-1].DllName)
        {
            BaseAddress = Ldr::LoadDll(Entry->DllName);
        }

        *(PVOID *)Entry->FuncAddress = GetRoutineAddress(BaseAddress, Entry->FunctionName);
    }

    return STATUS_SUCCESS;
}
