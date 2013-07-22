
/***



***/

static union
{
    PVOID QqFunctionTableBegin;

    struct
    {
        struct Util
        {
            struct ChatSession
            {
                BOOL (CDECL *OpenContactChatSession)(ULONG_PTR Uin, PVOID TXData);
                HWND (CDECL *GetContactChatSessionMainHWND)(ULONG_PTR Uin);
            };

            struct Contact
            {
                ULONG_PTR (*GetSelfUin)();
            };

            struct Metadata
            {
                HRESULT (CDECL *Get)(PVOID TXData, PCWSTR Name, PVOID *Data);
                HRESULT (CDECL *Put)(PVOID TXData, PCWSTR Name, PVOID Data);
            };
        };

        PVOID QqFunctionTableEnd;
    };
};

typedef struct
{
    PCWSTR DllName;
    PCSTR  FunctionName;

} FUNCTION_TABLE_INIT_ENTRY, *PFUNCTION_TABLE_INIT_ENTRY;

inline NTSTATUS InitializeQqFunctionTable()
{
    PVOID BaseAddress, *Begin, *End;
    PFUNCTION_TABLE_INIT_ENTRY Entry;

    static FUNCTION_TABLE_INIT_ENTRY InitEnties[] =
    {
        { L"AppUtil.dll",       "?OpenContactChatSession@ChatSession@Util@@YAXKPAUITXData@@@Z" },
        { L"AppUtil.dll",       "?GetContactChatSessionMainHWnd@ChatSession@Util@@YAPAUHWND__@@K@Z" },

        { L"KernelUtil.dll",    "?GetSelfUin@Contact@Util@@YAKXZ" },
    };

    Begin = &QqFunctionTableBegin;
    End = &QqFunctionTableEnd;

    --Begin;

    FOR_EACH_ARRAY(Entry, InitEnties)
    {
        if (++Begin >= End)
            break;

        if (Entry != InitEnties && Entry->DllName != Entry[-1].DllName)
            BaseAddress = Ldr::LoadDll(Entry->DllName);

        *Begin = GetRoutineAddress(BaseAddress, Entry->FunctionName);
    }
}
