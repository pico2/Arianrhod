

#if 0

    /************************************************************************
      ChatFrameApp

        L"exit for invalid version.17
    ************************************************************************/
/*
    module = Ldr::LoadDll(L"ChatFrameApp.dll");

    Mp::PATCH_MEMORY_DATA Function_ChatFrame[] =
    {
        //INLINE_HOOK_JUMP_RVA_NULL(0x93C3, IsTencentTrusted),
        INLINE_HOOK_JUMP_RVA_NULL(SearchChatFrame_CheckModule(module), IsTencentTrusted),
    };

*/


    /************************************************************************
      PreLogin
    ************************************************************************/

    module = Ldr::LoadDll(L"PreloginLogic.dll");

    Mp::PATCH_MEMORY_DATA Function_PreLogin[] =
    {
        //INLINE_HOOK_JUMP(SearchPreLogin_OnConnectionBroken(module), OnConnectionBroken, StubOnConnectionBroken),
        Mp::FunctionJumpVa(SearchPreLogin_OnSysDataCome(module), OnSysDataCome, &StubOnSysDataCome),
    };

#endif



PVOID SearchChatFrame_CheckModule(PVOID ChatFrame)
{
    PBYTE       Buffer;
    PVOID       StringReference, LastCall[3];
    PLDR_MODULE Module;

    static WCHAR String[] = L"exit for invalid version";

    Module = FindLdrModuleByHandle(ChatFrame);

    StringReference = SearchStringReference(Module, String, sizeof(String) - sizeof(WCHAR));
    if (StringReference == nullptr)
        return IMAGE_INVALID_VA;

    Buffer = (PBYTE)StringReference + 4;

    ZeroMemory(LastCall, sizeof(LastCall));

    LOOP_FOREVER
    {
        ULONG_PTR Length;

        if (Buffer[0] == 0xC3 || Buffer[0] == 0xC2)
            break;

        if (Buffer[0] == CALL)
        {
            LastCall[0] = LastCall[1];
            LastCall[1] = LastCall[2];
            LastCall[2] = Buffer;
        }

        Length = GetOpCodeSize(Buffer);
        Buffer += Length;
    }

    return LastCall[0] == nullptr ? IMAGE_INVALID_VA : GetCallDestination(LastCall[0]);
}

PVOID SearchPreLogin_OnConnectionBroken(PVOID ImageBase)
{
    static WCHAR String[] = L"CTXServerConnectionDectecter::OnConnectionBroken Stop CSProcessor";

    return SearchStringAndReverseSearchHeader(ImageBase, String, sizeof(String), 0xB0);
}

PVOID SearchPreLogin_OnSysDataCome(PVOID ImageBase)
{
    static WCHAR String[] = L"CTXServerConnectionDectecter::OnSysDataCome";

    return SearchStringAndReverseSearchHeader(ImageBase, String, sizeof(String) - sizeof(String[0]), 0x20);
}

PVOID Search_QQProtectDir(PVOID ImageBase)
{
    static WCHAR String[] = L"QQProtectDir";

    return SearchStringAndReverseSearchHeader(ImageBase, String, sizeof(String) - sizeof(String[0]), 0x80);
}


VOID FASTCALL OnConnectionBroken(PVOID This, PVOID Dummy, ULONG Param1, ULONG Param2, ULONG Param3, PVOID MessageString, ULONG RetryTimeOut)
{
    if (RetryTimeOut == 0xB)
        return;

    StubOnConnectionBroken(This, Dummy, Param1, Param2, Param3, MessageString, RetryTimeOut);
}

HRESULT FASTCALL OnSysDataCome(PVOID This, PVOID Dummy, USHORT Type, ULONG Param1, PVOID Packet)
{
    HRESULT hr;

    // WCHAR buf[0x100];
    // swprintf(buf, L"被踢了 %p %p %p", Type, Param1, Packet);
    // MessageBoxW(0, buf, 0, 64);

    hr = StubOnSysDataCome(This, Dummy, Type, Param1, Packet);
    return hr;

#if 0

    if (Type == 0x30 && ReloginMgr != nullptr && *(PBYTE)PtrAdd(This, 0x18) == 2)   // cType
    {
        Io::SetAsyncCall(
            []()
            {
                PITXData Data;

                Util::Data::CreateTXData(&Data);
                Data->SetDWord(L"cReloginFlag", 2);

                ReloginMgr->Relogin(nullptr, Data);
                Data->Release();

                return TRUE;

                //MessageBoxW(0, L"done", 0, 64);
            },
            500
        );
    }

    return hr;

#endif
}


HANDLE
NTAPI
QqCreateWaitQQProtectThread(
    PSECURITY_ATTRIBUTES    ThreadAttributes,
    ULONG_PTR               StackSize,
    PTHREAD_START_ROUTINE   StartAddress,
    PVOID                   Parameter,
    ULONG                   CreationFlags,
    PULONG                  ThreadId
)
{
    NTSTATUS    Status;
    PVOID       Ebp, CallCreateQQProtectExchangeWindow;
    PROCESS_BASIC_INFORMATION BasicInfo;

    LOOP_ONCE
    {
        if (PtrAnd(Parameter, 0xFFF00000) != 0)
            continue;

        Status = NtQueryInformationProcess((HANDLE)Parameter, ProcessBasicInformation, &BasicInfo, sizeof(BasicInfo), nullptr);
        FAIL_BREAK(Status);

        if (BasicInfo.UniqueProcessId != CurrentPid())
            break;

        AllocStack(16);
        Ebp = *((PVOID *)_AddressOfReturnAddress() - 1);

        CallCreateQQProtectExchangeWindow = *((PVOID *)Ebp + 1);
        if (*(PBYTE)CallCreateQQProtectExchangeWindow != CALL)
            break;

        NtClose((HANDLE)Parameter);

        *(PULONG_PTR)((PVOID *)Ebp + 1) += GetOpCodeSize(CallCreateQQProtectExchangeWindow);

        return nullptr;
    }

    return HummerCreateThread(ThreadAttributes, StackSize, StartAddress, Parameter, CreationFlags, ThreadId);
}


NTSTATUS
NTAPI
QqNtQueryInformationProcess(
    HANDLE              ProcessHandle,
    PROCESSINFOCLASS    ProcessInformationClass,
    PVOID               ProcessInformation,
    ULONG               ProcessInformationLength,
    PULONG              ReturnLength
)
{
    NTSTATUS Status;

    union
    {
        PVOID Information;
        PPROCESS_BASIC_INFORMATION Basic;
    };

    Status = StubNtQueryInformationProcess(ProcessHandle, ProcessInformationClass, ProcessInformation, ProcessInformationLength, ReturnLength);
    FAIL_RETURN(Status);

    Information = ProcessInformation;

    switch (ProcessInformationClass)
    {
        case ProcessBasicInformation:
            if (Basic->UniqueProcessId == CurrentPid())
            {
                Basic->InheritedFromUniqueProcessId = Basic->UniqueProcessId;
            }
            break;
    }

    return Status;
}

VOID    (FASTCALL *StubOnConnectionBroken)(PVOID This, PVOID, ULONG Param1, ULONG Param2, ULONG Param3, PVOID MessageString, ULONG Type);
HRESULT (FASTCALL *StubOnSysDataCome)(PVOID This, PVOID Dummy, USHORT Type, ULONG Param1, PVOID Packet);


ULONG CDECL GetAtAllGroupMemberUseTimes()
{
    return 1;
}

HRESULT CDECL GetCurrentAtNumber(PVOID Object, PULONG Number)
{
    *Number = 0;
    return S_OK;
}