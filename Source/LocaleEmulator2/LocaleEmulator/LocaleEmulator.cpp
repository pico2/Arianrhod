#include "stdafx.h"

ML_OVERLOAD_NEW

#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")

PLeGlobalData g_GlobalData;

ForceInline VOID LeSetGlobalData(PLeGlobalData GlobalData)
{
    g_GlobalData = GlobalData;
}

ForceInline VOID LeReleaseGlobalData()
{
    SafeDeleteT(g_GlobalData);
}

BOOL NTAPI DelayInitDllEntry(PVOID BaseAddress, ULONG Reason, PVOID Reserved)
{
    BOOL Success;
    PLDR_MODULE Module = FindLdrModuleByHandle(BaseAddress);
    PIMAGE_NT_HEADERS NtHeaders;

    NtHeaders = PtrAdd((PIMAGE_NT_HEADERS)BaseAddress, ((PIMAGE_DOS_HEADER)BaseAddress)->e_lfanew);
    Module->EntryPoint = PtrAdd(BaseAddress, NtHeaders->OptionalHeader.AddressOfEntryPoint);

    Success = ((API_POINTER(DelayInitDllEntry))Module->EntryPoint)(BaseAddress, Reason, Reserved);

    if (Reason == DLL_PROCESS_ATTACH && !Success)
        return Success;

    switch (Reason)
    {
        case DLL_PROCESS_ATTACH:
            if (!Success)
                return Success;
        case DLL_PROCESS_DETACH:
            break;

        default:
            return Success;
    }

    LeGetGlobalData()->HookModule(BaseAddress, &Module->BaseDllName, Reason == DLL_PROCESS_ATTACH);

    return Success;
}

NTSTATUS GetNlsFile(PUNICODE_STRING NlsFile, ULONG NlsIndex, PCWSTR SubKey)
{
    BOOL        Success;
    WCHAR       NlsIndexBuffer[16];
    NTSTATUS    Status;
    PKEY_VALUE_PARTIAL_INFORMATION FileName;

    swprintf(NlsIndexBuffer, L"%d", NlsIndex);

    Status = GetKeyValue(REGKEY_ROOT, SubKey, NlsIndexBuffer, &FileName);
    FAIL_RETURN(Status);

    Success = RtlCreateUnicodeString(NlsFile, (PWSTR)FileName->Data);
    FreeMemoryP(FileName);

    return Success ? STATUS_SUCCESS : STATUS_NO_MEMORY;
}

NTSTATUS GetLangFile(PUNICODE_STRING LangFile, ULONG LangIndex, PCWSTR SubKey)
{
    BOOL        Success;
    WCHAR       LangIndexBuffer[16];
    NTSTATUS    Status;
    PKEY_VALUE_PARTIAL_INFORMATION FileName;

    swprintf(LangIndexBuffer, L"%04x", LangIndex);

    Status = GetKeyValue(REGKEY_ROOT, SubKey, LangIndexBuffer, &FileName);
    FAIL_RETURN(Status);

    Success = RtlCreateUnicodeString(LangFile, (PWSTR)FileName->Data);
    FreeMemoryP(FileName);

    return Success ? STATUS_SUCCESS : STATUS_NO_MEMORY;
}

NTSTATUS ReadFileInSystemDirectory(NtFileMemory &File, PUNICODE_STRING Path)
{
    PWSTR       Buffer;
    ULONG_PTR   Length;
    NTSTATUS    Status;

    Length = sizeof(ROOTDIR_SYSTEM32) + Path->Length + sizeof(WCHAR);
    Buffer = (PWSTR)AllocateMemoryP(Length);
    if (Buffer == nullptr)
        return STATUS_NO_MEMORY;

    Length = CONST_STRLEN(ROOTDIR_SYSTEM32);
    CopyMemory(Buffer, ROOTDIR_SYSTEM32, Length * sizeof(WCHAR));
    CopyMemory(Buffer + Length, Path->Buffer, Path->Length);
    Buffer[Length + Path->Length / sizeof(WCHAR)] = 0;

    Status = File.Open(Buffer, NFD_NOT_RESOLVE_PATH);

    FreeMemoryP(Buffer);

    return Status;
}

NTSTATUS LeGlobalData::Initialize()
{
#if !ARCHEAGE_VER

    PLEPEB          LePeb;
    PLDR_MODULE     Ntdll;
    PPEB_BASE       Peb;
    NTSTATUS        Status;
    NLSTABLEINFO    NlsTableInfo;
    UNICODE_STRING  SystemDirectory, NlsFileName, OemNlsFileName, LangFileName;
    PKEY_VALUE_PARTIAL_INFORMATION IndexValue;

    Wow64 = Ps::IsWow64Process();
    Ntdll = GetNtdllLdrModule();

    LePeb = OpenOrCreateLePeb();
    if (LePeb == nullptr)
    {
        PVOID           ReloadedNtdll;
        PUNICODE_STRING FullDllName;

        LePeb = GetLePeb();

        InitDefaultLeb(&LePeb->Leb);

        FullDllName = &FindLdrModuleByHandle(&__ImageBase)->FullDllName;
        CopyMemory(LePeb->LeDllFullPath, FullDllName->Buffer, FullDllName->Length + sizeof(WCHAR));

        Status = LoadPeImage(Ntdll->FullDllName.Buffer, &ReloadedNtdll, nullptr, LOAD_PE_IGNORE_RELOC);
        if (NT_SUCCESS(Status))
        {
            PVOID LdrLoadDllAddress;

            LdrLoadDllAddress = EATLookupRoutineByHashPNoFix(ReloadedNtdll, NTDLL_LdrLoadDll);
            LePeb->LdrLoadDllAddress = PtrAdd(LdrLoadDllAddress, PtrOffset(Ntdll->DllBase, ReloadedNtdll));
            CopyMemory(LePeb->LdrLoadDllBackup, LdrLoadDllAddress, LDR_LOAD_DLL_BACKUP_SIZE);
            LePeb->LdrLoadDllBackupSize = LDR_LOAD_DLL_BACKUP_SIZE;

            UnloadPeImage(ReloadedNtdll);
        }
    }
    else
    {
        *GetLePeb() = *LePeb;

        NtClose(LePeb->Section);
        CloseLePeb(LePeb);
    }

    WriteLog(L"init leb %s", GetLePeb()->LeDllFullPath);

    SystemDirectory = Ntdll->FullDllName;
    SystemDirectory.Length -= Ntdll->BaseDllName.Length;

    Status = RtlDuplicateUnicodeString(RTL_DUPSTR_ADD_NULL, &SystemDirectory, &this->SystemDirectory);
    FAIL_RETURN(Status);

    RtlInitEmptyUnicodeString(&NlsFileName, nullptr, 0);
    RtlInitEmptyUnicodeString(&OemNlsFileName, nullptr, 0);
    RtlInitEmptyUnicodeString(&LangFileName, nullptr, 0);

    SCOPE_EXIT
    {
        RtlFreeUnicodeString(&NlsFileName);
        RtlFreeUnicodeString(&OemNlsFileName);
        RtlFreeUnicodeString(&LangFileName);
    }
    SCOPE_EXIT_END;

    Status = GetNlsFile(&NlsFileName, GetLeb()->AnsiCodePage, REGPATH_CODEPAGE);
    FAIL_RETURN(Status);

    Status = GetNlsFile(&OemNlsFileName, GetLeb()->OemCodePage, REGPATH_CODEPAGE);
    FAIL_RETURN(Status);

    Status = GetLangFile(&LangFileName, GetLeb()->LocaleID, REGPATH_LANGUAGE);
    FAIL_RETURN(Status);

    NtFileMemory AnsiFile, OemFile, LangFile;

    Status = ReadFileInSystemDirectory(AnsiFile, &NlsFileName);
    FAIL_RETURN(Status);

    Status = ReadFileInSystemDirectory(OemFile, &OemNlsFileName);
    FAIL_RETURN(Status);

    Status = ReadFileInSystemDirectory(LangFile, &LangFileName);
    FAIL_RETURN(Status);

    AnsiCodePageOffset      = 0;
    OemCodePageOffset       = ROUND_UP(AnsiFile.GetSize32(), 16);
    UnicodeCaseTableOffset  = OemCodePageOffset + ROUND_UP(OemFile.GetSize32(), 16);

    Status = AllocVirtualMemory(&CodePageMapView, UnicodeCaseTableOffset + LangFile.GetSize32(), PAGE_READWRITE, MEM_COMMIT | MEM_TOP_DOWN);
    FAIL_RETURN(Status);

    CopyMemory(PtrAdd(CodePageMapView, AnsiCodePageOffset),     AnsiFile.GetBuffer(),   AnsiFile.GetSize32());
    CopyMemory(PtrAdd(CodePageMapView, OemCodePageOffset),      OemFile.GetBuffer(),    OemFile.GetSize32());
    CopyMemory(PtrAdd(CodePageMapView, UnicodeCaseTableOffset), LangFile.GetBuffer(),   LangFile.GetSize32());

    ProtectVirtualMemory(CodePageMapView, UnicodeCaseTableOffset + LangFile.GetSize32(), PAGE_READONLY);

    RtlInitNlsTables(
        (PUSHORT)PtrAdd(CodePageMapView, AnsiCodePageOffset),
        (PUSHORT)PtrAdd(CodePageMapView, OemCodePageOffset),
        (PUSHORT)PtrAdd(CodePageMapView, UnicodeCaseTableOffset),
        &NlsTableInfo
    );

    RtlResetRtlTranslations(&NlsTableInfo);

    WriteLog(L"reset nls");

    Peb = CurrentPeb();

    Peb->AnsiCodePageData       = (PUSHORT)PtrAdd(CodePageMapView, AnsiCodePageOffset);
    Peb->OemCodePageData        = (PUSHORT)PtrAdd(CodePageMapView, OemCodePageOffset);
    Peb->UnicodeCaseTableData   = (PUSHORT)PtrAdd(CodePageMapView, UnicodeCaseTableOffset);

#endif

    // LdrInitShimEngineDynamic(&__ImageBase);

    LdrRegisterDllNotification(0,
        [] (ULONG NotificationReason, PCLDR_DLL_NOTIFICATION_DATA NotificationData, PVOID Context)
        {
            return ((PLeGlobalData)Context)->DllNotification(NotificationReason, NotificationData);
        },
        this,
        &DllNotificationCookie
    );

#if ARCHEAGE_VER

    return STATUS_SUCCESS;

#else

    Status = InstallHookPort();
    FAIL_RETURN(Status);

    WriteLog(L"inst hp");

    HookNtdllRoutines(Ntdll->DllBase);

    WriteLog(L"hook ntdll");

    PLDR_MODULE Kernel32Ldr;

    Kernel32Ldr = GetKernel32Ldr();
    if (Kernel32Ldr != nullptr)
    {
        Kernel32Ldr->EntryPoint = DelayInitDllEntry;
        // HookKernel32Routines(Kernel32Ldr->DllBase);
    }

    WriteLog(L"init %p", Status);

    return Status;

#endif
}

typedef struct
{
    UNICODE_STRING DllName;
    TYPE_OF(&LeGlobalData::HookNtdllRoutines)     HookRoutine;
    TYPE_OF(&LeGlobalData::UnHookNtdllRoutines)   UnHookRoutine;

} DLL_HOOK_ENTRY, *PDLL_HOOK_ENTRY;

PDLL_HOOK_ENTRY LookupDllHookEntry(PCUNICODE_STRING BaseDllName)
{
    static DLL_HOOK_ENTRY DllHookEntries[] =
    {
#if ARCHEAGE_VER

        { RTL_CONSTANT_STRING(L"x2game.dll"),       &LeGlobalData::HookX2GameRoutines },

#else

        { RTL_CONSTANT_STRING(L"USER32.dll"),       &LeGlobalData::HookUser32Routines,      &LeGlobalData::UnHookUser32Routines },
        { RTL_CONSTANT_STRING(L"GDI32.dll"),        &LeGlobalData::HookGdi32Routines,       &LeGlobalData::UnHookGdi32Routines },
        { RTL_CONSTANT_STRING(L"KERNEL32.dll"),     &LeGlobalData::HookKernel32Routines,    &LeGlobalData::UnHookKernel32Routines },

#endif // ARCHEAGE_VER
    };

    PDLL_HOOK_ENTRY Entry;

    FOR_EACH(Entry, DllHookEntries, countof(DllHookEntries))
    {
        if (!RtlEqualUnicodeString(BaseDllName, &Entry->DllName, TRUE))
            continue;

        return Entry;
    }

    return nullptr;
}

VOID LeGlobalData::HookModule(PVOID DllBase, PCUNICODE_STRING DllName, BOOL DllLoad)
{
    PDLL_HOOK_ENTRY Entry;

    Entry = LookupDllHookEntry(DllName);
    if (Entry == nullptr)
        return;

    DllLoad ? (this->*Entry->HookRoutine)(DllBase) : (this->*Entry->UnHookRoutine)();
}

VOID LeGlobalData::DllNotification(ULONG NotificationReason, PCLDR_DLL_NOTIFICATION_DATA NotificationData)
{
    NTSTATUS            Status;
    PVOID               DllBase;
    ULONG_PTR           Length;
    PLDR_MODULE         Module;
    UNICODE_STRING      DllPath;
    PCUNICODE_STRING    DllName;

    switch (NotificationReason)
    {
        case LDR_DLL_NOTIFICATION_REASON_LOADED:
            DllName = NotificationData->Loaded.BaseDllName;
            DllBase = NotificationData->Loaded.DllBase;
            DllPath = *NotificationData->Loaded.FullDllName;
            DllPath.Length -= DllName->Length;
            break;

        case LDR_DLL_NOTIFICATION_REASON_UNLOADED:
            DllName = NotificationData->Unloaded.BaseDllName;
            DllBase = NotificationData->Unloaded.DllBase;
            DllPath = *NotificationData->Unloaded.FullDllName;
            DllPath.Length -= DllName->Length;
            break;

        default:
            return;
    }

    //if (!RtlEqualUnicodeString(&SystemDirectory, &DllPath, TRUE))
    //    return;

    if (LookupDllHookEntry(DllName) == nullptr)
        return;

    Module = FindLdrModuleByHandle(DllBase);
    if (!FLAG_ON(Module->Flags, LDRP_PROCESS_ATTACH_CALLED))
    {
        Module->EntryPoint = DelayInitDllEntry;
    }
    else
    {
        HookModule(DllBase, DllName, NotificationReason == LDR_DLL_NOTIFICATION_REASON_LOADED);
    }
}

#if ARCHEAGE_VER

#pragma comment(linker, "/EXPORT:ShellExecuteA=SHELL32.ShellExecuteA")

LONG WINAPI GetSQLiteKeyExceptionHandler(PEXCEPTION_POINTERS ExceptionInfo)
{
    PDR7_INFO   Dr7;
    PBYTE       SQLiteKeyBuffer;

    switch (ExceptionInfo->ExceptionRecord->ExceptionCode)
    {
        case EXCEPTION_SINGLE_STEP:
            SQLiteKeyBuffer = (PBYTE)ExceptionInfo->ContextRecord->Dr3 - 0xC;

            Dr7 = (PDR7_INFO)&ExceptionInfo->ContextRecord->Dr7;
            Dr7->L3 = 0;
            ExceptionInfo->ContextRecord->Dr3 = 0;

            for (ULONG_PTR Count = 0x10; Count; --Count)
            {
                PrintConsoleW(L"0x%02X, ", *SQLiteKeyBuffer++);
                if (Count == 9)
                    PrintConsoleW(L"\n");
            }

            PrintConsoleW(L"\nPress any key to exit...");
            PauseConsole();
            Ps::ExitProcess(0);

            break;

        default:
            return EXCEPTION_CONTINUE_SEARCH;
    }

    // return EXCEPTION_CONTINUE_EXECUTION;
}

PSTR CDECL x2_strstr(PSTR Str, PCSTR SubStr)
{
    PrintConsole(L"%S -> %S\n", Str, SubStr);

    if (SubStr != nullptr && !StrCompareA(SubStr, "+acpxmk"))
    {
        return Str;
    }

    return strstr(Str, SubStr);
}

VOID (*StubX2_FillDecryptTable)();

VOID X2_FillDecryptTable()
{
    PBYTE       KeyBuffer;
    CONTEXT     Context;
    PDR7_INFO   Dr7;

    INLINE_ASM mov KeyBuffer, esi;

    KeyBuffer += 8 + 0xC;

    PrintConsole(L"return address %p\n", _ReturnAddress());

    Context.ContextFlags = CONTEXT_DEBUG_REGISTERS;
    NtGetContextThread(CurrentThread, &Context);

    Dr7 = (PDR7_INFO)&Context.Dr7;

    Dr7->L3     = 1;
    Dr7->LEN3   = DR7_LEN_4_BYTE;
    Dr7->RW3    = DR7_RW_WRITE;
    Context.Dr3 = (ULONG_PTR)KeyBuffer;

    NtSetContextThread(CurrentThread, &Context);

    RtlAddVectoredExceptionHandler(TRUE, GetSQLiteKeyExceptionHandler);

    StubX2_FillDecryptTable();
}

VOID FASTCALL PrintKey(PBYTE SQLiteKeyBuffer)
{
    NtFileDisk f;

    f.Create(L"dump.bin");
    f.Write(SQLiteKeyBuffer, 0x100);

    SQLiteKeyBuffer += 8;

    for (ULONG_PTR Count = 0x10; Count; --Count)
    {
        PrintConsoleW(L"0x%02X, ", *SQLiteKeyBuffer++);
        if (Count == 9)
            PrintConsoleW(L"\n");
    }

    PrintConsoleW(L"\nPress any key to exit...");
    PauseConsole();
    Ps::ExitProcess(0);
}

NAKED VOID GetKey()
{
    INLINE_ASM
    {
        mov     ecx, esi;
        call    PrintKey
    }
}

NTSTATUS LeGlobalData::HookX2GameRoutines(PVOID X2Game)
{
    BYTE StubFillDecryptTable[] =
    {
        0x55, 0x8b, 0xec, 0x81, 0xec, 0x08, 0x08, 0x00, 0x00, 0xa1,
    };

    BYTE StubSaveStackCookie[] =
    {
        0x33, 0xC5,
    };

    SEARCH_PATTERN_DATA Pattern[] =
    {
        ADD_PATTERN(StubFillDecryptTable, 0, sizeof(StubFillDecryptTable) + 4),
        ADD_PATTERN(StubSaveStackCookie),
    };

    ULONG_PTR           SearchLength;
    PVOID               StartAddress, FillDecryptTable, FillDecryptTable2;
    PLDR_MODULE         X2GameModule;
    PIMAGE_NT_HEADERS   NtHeaders;

    //MessageBoxW(0, L"??", 0, 0);

    X2GameModule = FindLdrModuleByHandle(X2Game);

    AllocConsole();

    LOOP_ONCE
    {
        NtHeaders   = ImageNtHeaders(X2GameModule->DllBase);
        StartAddress = PtrAdd(X2GameModule->DllBase, IMAGE_FIRST_SECTION(NtHeaders)->VirtualAddress);
        SearchLength = X2GameModule->SizeOfImage - PtrOffset(StartAddress, X2GameModule->DllBase);

        FillDecryptTable = SearchPatternSafe(Pattern, countof(Pattern), StartAddress, SearchLength);

        if (FillDecryptTable == nullptr)
        {
            PrintConsoleW(L"can't find FillDecryptTable\n");
            continue;
        }

        StartAddress = PtrAdd(FillDecryptTable, 1);
        SearchLength = X2GameModule->SizeOfImage - PtrOffset(StartAddress, X2GameModule->DllBase);

        FillDecryptTable2 = SearchPatternSafe(
                                Pattern,
                                countof(Pattern),
                                StartAddress,
                                SearchLength
                            );

        if (FillDecryptTable2 != nullptr)
        {
            PrintConsoleW(L"found multi FillDecryptTable\n");
            break;
        }

        PVOID MSVCR100 = FindLdrModuleByName(&WCS2US(L"MSVCR100.dll"))->DllBase;
        PVOID STRSTR = GetRoutineAddress(MSVCR100, "strstr");

        MEMORY_FUNCTION_PATCH f[] =
        {
            //INLINE_HOOK_JUMP_NULL(STRSTR, x2_strstr),
            INLINE_HOOK_JUMP(FillDecryptTable, X2_FillDecryptTable, StubX2_FillDecryptTable),
        };

        Nt_PatchMemory(nullptr, 0, f, countof(f), MSVCR100);

        return STATUS_SUCCESS;
    }

    PrintConsoleW(L"Press any key to exit...");
    PauseConsole();
    Ps::ExitProcess(0);
}

#endif // ARCHEAGE_VER

NTSTATUS LeGlobalData::UnInitialize()
{
    if (DllNotificationCookie != nullptr)
    {
        LdrUnregisterDllNotification(DllNotificationCookie);
        DllNotificationCookie = nullptr;
    }

    UnHookGdi32Routines();
    UnHookUser32Routines();
    UnHookKernel32Routines();
    UnHookNtdllRoutines();

    UnInstallHookPort();

    RtlFreeUnicodeString(&SystemDirectory);

    return 0;
}

inline BOOL UnInitialize(PVOID BaseAddress)
{
    LeReleaseGlobalData();
    ml::MlUnInitialize();
    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    NTSTATUS            Status;
    PLDR_MODULE         Kernel32;
    PLeGlobalData       GlobalData;

#if !ARCHEAGE_VER

    Kernel32 = GetKernel32Ldr();

    if (Kernel32 != nullptr && FLAG_ON(Kernel32->Flags, LDRP_PROCESS_ATTACH_CALLED))
    {
        ExceptionBox(L"fuck");
        return FALSE;
    }

#endif

    LdrDisableThreadCalloutsForDll(BaseAddress);
    ml::MlInitialize();

    GlobalData = new LeGlobalData;
    if (GlobalData == nullptr)
        return FALSE;

    LeSetGlobalData(GlobalData);

#if ARCHEAGE_VER

    MEMORY_FUNCTION_PATCH f[] =
    {
        INLINE_HOOK_JUMP_RVA_NULL(0x4FF7FA, GetKey),
    };

    AllocConsole();

    Nt_PatchMemory(0, 0, f, countof(f), FindLdrModuleByName(&USTR(L"x2game.dll"))->DllBase);

    //GlobalData->HookX2GameRoutines(FindLdrModuleByName(&USTR(L"x2game.dll"))->DllBase);

#else

    Status = GlobalData->Initialize();
    if (NT_FAILED(Status))
        return FALSE;

    GlobalData->SetUnhandledExceptionFilter();

#endif

    WriteLog(L"init ret");

    return TRUE;
}

BOOL NTAPI DllMain(PVOID BaseAddress, ULONG Reason, PVOID Reserved)
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
