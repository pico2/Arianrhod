#include "SysCallHook.h"

PVOID                       g_KiFastSystemCall, g_CallSystemCall;
ULONG                       g_SysEnterSize, g_ExplorerPID;
SYSCALL_FILTER_ENTRY       *g_pSysCallFilters;
SYSCALL_FILTER_HASH_TABLE   g_HashTable;
//CRITICAL_SECTION            g_FilterCriticalSection;



HASH_TABLE_ENTRY* FindHashTableEntry(SYSCALL_FILTER_HASH_TABLE *HashTable, ULONG Hash)
{
    ULONG Left, Right, Middle;
    HASH_TABLE_ENTRY *Entry;

    Left    = 0;
    Right   = HashTable->Count - 1;

    if (Hash < HashTable->Entry[Left].Hash ||
        Hash > HashTable->Entry[Right].Hash)
    {
        return NULL;
    }

    if (Hash == HashTable->Entry[Right].Hash)
        return &HashTable->Entry[Right];

    while (Left < Right)
    {
        Middle  = (Right - Left) / 2 + Left;
        Entry   = &HashTable->Entry[Middle];

        if (Entry->Hash == Hash)
            return Entry;

        if (Entry->Hash < Hash)
        {
            Left = Middle + 1;
        }
        else
        {
            Right = Middle - 1;
        }
    }

    Entry = &HashTable->Entry[Left];

    return Entry->Hash == Hash ? Entry : NULL;
}

NTSTATUS AddFunctionToTable(SYSCALL_FILTER_HASH_TABLE *HashTable, ULONG Hash, PVOID Routine)
{
    HASH_TABLE_ENTRY        *Entry;
    SYSCALL_FILTER_ENTRY    *Filter;
    Entry = FindHashTableEntry(HashTable, Hash);
    if (Entry == NULL)
        return STATUS_UNSUCCESSFUL;

    Filter = Entry->Entry;
    Filter->ProxyFunction = Routine;
    SET_FLAG(Filter->Flags, SYSCALL_FILTER_FLAG_ENABLE);

    return STATUS_SUCCESS;
}

NTSTATUS RemoveFunctionFromTable(SYSCALL_FILTER_HASH_TABLE *HashTable, ULONG Hash)
{
    HASH_TABLE_ENTRY        *Entry;
    SYSCALL_FILTER_ENTRY    *Filter;
    Entry = FindHashTableEntry(HashTable, Hash);
    if (Entry == NULL)
        return STATUS_UNSUCCESSFUL;

    Filter = Entry->Entry;
    Filter->ProxyFunction = NULL;
    CLEAR_FLAG(Filter->Flags, SYSCALL_FILTER_FLAG_ENABLE);

    return STATUS_SUCCESS;
}

VOID HookSysEnter_x86();
VOID HookSysEnter_x64();

ASM VOID OldSysEnter()
{
    ASM_DUMMY_AUTO();
}

VOID HookSysCall_x64()
{
    INLINE_ASM
    {
        or      g_SysEnterSize, -1;
        mov     eax, HookSysEnter_x64;
        xchg    fs:[0xC0], eax;
        mov     byte ptr [OldSysEnter], 0x68;       // push cosnt_4
        mov     dword ptr [OldSysEnter + 1], eax;
        mov     dword ptr [OldSysEnter + 5], 0xC3;  // ret
    }
}

VOID UnHookSysCall_x64()
{
    __writefsdword(0xC0, *(PULONG_PTR)((ULONG_PTR)OldSysEnter + 1));
}

NTSTATUS HookSysCall_x86()
{
    NTSTATUS    Status;
    ULONG       OldProtect, SysEnterSize;
    PBYTE       KiFastCallEntry, BaseKiFastCallEntry;

    KiFastCallEntry     = (PBYTE)KiFastSystemCall;
    BaseKiFastCallEntry = KiFastCallEntry;
    g_KiFastSystemCall  = (PVOID)((ULONG_PTR)KiFastCallEntry ^ KI_FAST_SYSTEM_CALL_MASK);
/*
    do
    {
        KiFastCallEntry += GetOpCodeSize(KiFastCallEntry);
    } while (KiFastCallEntry[0] != 0xC3);
*/
    if (
        (
         *(PULONG)&KiFastCallEntry[0] != 0x340FD48B ||  // mov edx, esp     sysenter
         *(PULONG)&KiFastCallEntry[4] != 0x24A48DC3 ||  // ret
         *(PULONG)&KiFastCallEntry[8] != 0              // lea esp, dword ptr [esp]     7 bytes
        ) &&
        (
         *(PULONG)&KiFastCallEntry[0]   != 0x000000BA ||  // mov edx, 000000C3h
         *(PUSHORT)&KiFastCallEntry[4]  != 0xBAC3    ||  // mov edx, const
         *(PUSHORT)&KiFastCallEntry[10] != 0xE2FF        // jmp edx
        )
       )
    {
        DebugBreakPoint();
    }
/*
    ++KiFastCallEntry;
    if (*(PULONG)KiFastCallEntry != 0x0024A48D || *(PULONG)&KiFastCallEntry[3] != 0)
    {
        DebugBreakPoint();
    }

    SysEnterSize = KiFastCallEntry - BaseKiFastCallEntry + 7;
*/
    SysEnterSize = 0xC;
    Status = Nt_ProtectMemory(NtCurrentProcess(), BaseKiFastCallEntry, SysEnterSize, PAGE_EXECUTE_READWRITE, &OldProtect);
    if (!NT_SUCCESS(Status))
        return Status;

    g_SysEnterSize = SysEnterSize;
    CopyMemory(OldSysEnter, BaseKiFastCallEntry, g_SysEnterSize);
    *(PULONG)BaseKiFastCallEntry = 0x000000BA;  // mov     edx, 'C3' 000000

    KiFastCallEntry += 5;
    *KiFastCallEntry = 0xBA;
    *(PULONG_PTR)&KiFastCallEntry[1] = (ULONG_PTR)HookSysEnter_x86;
    *(PUSHORT)&KiFastCallEntry[5] = 0xE2FF;

    if (OldProtect != PAGE_EXECUTE_READWRITE)
    {
        Nt_ProtectMemory(NtCurrentProcess(), BaseKiFastCallEntry, 12, OldProtect, &OldProtect);
    }

    return STATUS_SUCCESS;
}

NTSTATUS UnHookSysCall_x86()
{
    PVOID       BaseAddress, KiFastCallEntry;
    ULONG       OldProtect;
    NTSTATUS    Status;

    KiFastCallEntry = (PVOID)((ULONG_PTR)g_KiFastSystemCall ^ KI_FAST_SYSTEM_CALL_MASK);
    BaseAddress = KiFastCallEntry;
    Status = Nt_ProtectMemory(NtCurrentProcess(), KiFastCallEntry, 12, PAGE_EXECUTE_READWRITE, &OldProtect);
    if (!NT_SUCCESS(Status))
        return Status;

    CopyMemory(KiFastCallEntry, OldSysEnter, g_SysEnterSize);
    if (OldProtect != PAGE_EXECUTE_READWRITE)
    {
        Nt_ProtectMemory(NtCurrentProcess(), KiFastCallEntry, 12, OldProtect, &OldProtect);
    }

    return STATUS_SUCCESS;
}

ASM
NTSTATUS
CDECL
CallSystemCall(
    SYSCALL_FILTER_ENTRY   *FilterInfo,
    PBOOL                   BypassType,
    ...
)
{
    UNREFERENCED_PARAMETER(FilterInfo);
    UNREFERENCED_PARAMETER(BypassType);

    INLINE_ASM jmp g_CallSystemCall;
}

ASM
NTSTATUS
CDECL
CallSystemCall_x86(
    SYSCALL_FILTER_ENTRY   *FilterInfo,
    PBOOL                   BypassType,
    ...
)
{
    UNREFERENCED_PARAMETER(FilterInfo);
    UNREFERENCED_PARAMETER(BypassType);

    INLINE_ASM
    {
        mov     eax, [esp + 4];
        mov     ecx, esp;
        mov     edx, [esp + 8];

        lea     esp, [esp - 0x10];
        mov     [esp + 0x0], esi;
        mov     [esp + 0x4], edi;
        mov     [esp + 0x8], ebx;
        mov     [esp + 0xC], ebp;

        mov     ebx, esp;
        lea     esi, [ecx + 0xC];
        mov     ecx, [eax]SYSCALL_FILTER_ENTRY.ArgumentSize;
        sub     esp, ecx;
        shr     ecx, 2;
        mov     edi, esp;
        rep     movsd;
        mov     eax, [eax]SYSCALL_FILTER_ENTRY.ServiceIndex;
//        mov     eax, [edx + 0x20];
        mov     ecx, [edx + 0x1C];
        push    CALLSYSTEMCALL_X86_RET;
        call    OldSysEnter;

CALLSYSTEMCALL_X86_RET:

        mov     esp, ebx;
        mov     esi, [esp + 0x0];
        mov     edi, [esp + 0x4];
        mov     ebx, [esp + 0x8];
        mov     ebp, [esp + 0xC];
        lea     esp, [esp + 0x10];
        ret;
    }
}

ASM VOID HookSysEnter_x86()
{
    INLINE_ASM
    {
        push OldSysEnter;
        pushfd;
        pushad;

        cmp     eax, MAX_SERVICE_INDEX;
        jae     _PASS_SYSCALL;

        shl     eax, 5;
        add     eax, g_pSysCallFilters;
        mov     ebx, eax;
        xor     eax, eax;
        or      eax, [ebx]SYSCALL_FILTER_ENTRY.ProxyFunction;
        je      _PASS_SYSCALL;
        test    [ebx]SYSCALL_FILTER_ENTRY.Flags, SYSCALL_FILTER_FLAG_ENABLE;
        je      _PASS_SYSCALL;

        lea     edx, [esp + 0x30];
        mov     ecx, [ebx]SYSCALL_FILTER_ENTRY.ArgumentSize;
        mov     ebp, esp;
        lea     ecx, [ecx + 4];
        mov     esi, edx;
        lea     edx, [esp - 4];
        sub     esp, ecx;
        mov     edi, esp;
        shr     ecx, 2;
        dec     ecx;
        rep     movsd;
        mov     dword ptr [edx], ecx;
        mov     edi, edx;
        mov     ecx, ebx;
        call    eax;
        mov     esp, ebp;
        cmp     dword ptr [edi], 0;
        je      _PASS_SYSCALL;

        mov     ecx, ebx;
        mov     edx, esp;
        mov     edi, [edx + 0x00];
        mov     esi, [edx + 0x04];
        mov     ebp, [edx + 0x08];
        mov     esp, [edx + 0x0C];
        mov     ebx, [edx + 0x10];
        popfd;

        lea     esp, [esp + 0x08];
        jmp     [ecx]SYSCALL_FILTER_ENTRY.ReturnOpAddress;
//        mov     edx, [esp + 8];
//        mov     ecx, [ecx]SYSCALL_FILTER_ENTRY.ArgumentSize;
//        lea     esp, [esp + ecx + 0xC];
//        jmp     edx;

//        mov     ecx, [ebx]SYSCALL_FILTER_ENTRY.ArgumentSize;
//        mov     edx, g_BypassSysEnterRetOp;
//        mov     [edx], ecx;
//        mov     dword ptr [esp + 0x24], offset BypassSysEnter;
//        mov     [esp + 0x1C], eax;

_PASS_SYSCALL:
        popad;
        popfd;
        ret;
    }
}

VOID FASTCALL ShowSysCallInfo(ULONG ServiceIndex, ULONG_PTR ReturnAddress)
{
    UnHookSysCall_x64();

    static ULONG Count;

    PrintConsoleW(
        L"%08X: %08X @ %08X: %S\n",
        Count++,
        ServiceIndex,
        ReturnAddress,
        g_pSysCallFilters[ServiceIndex].FunctionName
    );

    HookSysCall_x64();
}

ASM
NTSTATUS
CDECL
CallSystemCall_x64(
    SYSCALL_FILTER_ENTRY   *FilterInfo,
    PBOOL                   BypassType,
    ...
)
{
    UNREFERENCED_PARAMETER(FilterInfo);
    UNREFERENCED_PARAMETER(BypassType);

    INLINE_ASM
    {
        mov     eax, [esp + 4];
        mov     ecx, esp;
        mov     edx, [esp + 8];

        lea     esp, [esp - 0x10];
        mov     [esp + 0x0], esi;
        mov     [esp + 0x4], edi;
        mov     [esp + 0x8], ebx;
        mov     [esp + 0xC], ebp;

        mov     ebx, esp;
        lea     esi, [ecx + 0xC];
        mov     ecx, [eax]SYSCALL_FILTER_ENTRY.ArgumentSize;
        sub     esp, ecx;
        shr     ecx, 2;
        mov     edi, esp;
        rep     movsd;
        mov     eax, [eax]SYSCALL_FILTER_ENTRY.ServiceIndex;
//        mov     eax, [edx + 0x20];
        mov     ecx, [edx + 0x1C];
        mov     edx, esp;
        call    OldSysEnter;

        mov     esp, ebx;
        mov     esi, [esp + 0x0];
        mov     edi, [esp + 0x4];
        mov     ebx, [esp + 0x8];
        mov     ebp, [esp + 0xC];
        lea     esp, [esp + 0x10];
        ret;
    }
}

#if 0

VOID STDCALL PrintSyscall(ULONG Index, PVOID *Parameter)
{
    static BOOL             SpinLock;
    SYSCALL_FILTER_ENTRY   *Entry;
    ULONG                   Length;
    WCHAR                   Buffer[0xFF0 / 2];
    BOOL                    BypassType;
    OBJECT_ATTRIBUTES       ObjectAttributes;
    IO_STATUS_BLOCK         IoStatus;

    static HANDLE                LogFileHandle;
    static SYSCALL_FILTER_ENTRY *CreateFileEntry;
    static SYSCALL_FILTER_ENTRY *WriteFileEntry;

    switch (Index)
    {
        case 0x0002:
        case 0x0004:
        case 0x000F:
        case 0x0082:
        case 0x0040:
        case 0x000C:
        case 0x0045:
        case 0x0014:
        case 0x000D:
        case 0x00F2:
        case 0x002F:
        case 0x0010:
        case 0x0015:
        case 0x001B:
        case 0x004D:
            return;
    }

    while (_InterlockedCompareExchange((PLONG)&SpinLock, TRUE, FALSE));

    if (WriteFileEntry == NULL)
    {
        ULONG BOM;
        UNICODE_STRING FileName;

        CreateFileEntry = FindHashTableEntry(&g_HashTable, SYSCALL_ZwCreateFile)->Entry;
        WriteFileEntry  = FindHashTableEntry(&g_HashTable, SYSCALL_ZwWriteFile)->Entry;

        RTL_CONST_STRING(FileName, L"\\??\\E:\\Desktop\\mix\\packer\\SE\\oLog.txt");

        InitializeObjectAttributes(&ObjectAttributes, &FileName, OBJ_CASE_INSENSITIVE, NULL, NULL);
        CallSystemCall(
            CreateFileEntry,
            &BypassType,
            &LogFileHandle,
            GENERIC_WRITE | SYNCHRONIZE | FILE_READ_ATTRIBUTES,
            &ObjectAttributes,
            &IoStatus,
            NULL,
            FILE_ATTRIBUTE_NORMAL,
            FILE_SHARE_READ,
            FILE_OVERWRITE_IF,
            FILE_SYNCHRONOUS_IO_NONALERT | FILE_OPEN_FOR_BACKUP_INTENT,
            NULL,
            0
        );
/*
        BOM = BOM_UTF16_LE;
        CallSystemCall(
            WriteFileEntry,
            &BypassType,
            LogFileHandle,
            NULL,
            NULL,
            NULL,
            &IoStatus,
            &BOM,
            2,
            NULL,
            NULL
        );
*/
    }

    Entry = &g_pSysCallFilters[Index];

    Length = swprintf(Buffer, L"%08X %S: ", Index, Entry->FunctionName);
    for (ULONG Count = Entry->ArgumentSize / 4; Count; --Count)
        Length += swprintf(Buffer + Length, L" %08X", *Parameter++);

    Length += swprintf(Buffer + Length, L"\n");

    WriteConsoleW(Nt_CurrentPeb()->ProcessParameters->StandardOutput, Buffer, Length, &Length, NULL);
/*
    CallSystemCall(
        WriteFileEntry,
        &BypassType,
        LogFileHandle,
        NULL,
        NULL,
        NULL,
        &IoStatus,
        Buffer,
        Length * 2,
        NULL,
        NULL
    );
*/
    _InterlockedCompareExchange((PLONG)&SpinLock, FALSE, TRUE);
}

#endif

ASM VOID HookSysEnter_x64()
{
    INLINE_ASM
    {
        push OldSysEnter;
        pushfd;
        pushad;

        cmp     eax, MAX_SERVICE_INDEX;
        jae     _PASS_SYSCALL;

/*
        pushad;
        push edx;
        push eax;
        call PrintSyscall;
        popad;
        pushad;
        mov ecx, eax;
        mov edx, [esp + 0x4C];
        call ShowSysCallInfo;
        popad;
*/
        shl     eax, 5;
        add     eax, g_pSysCallFilters;
        mov     ebx, eax;
        xor     eax, eax;
        or      eax, [ebx]SYSCALL_FILTER_ENTRY.ProxyFunction;
        je      _PASS_SYSCALL;
        test    [ebx]SYSCALL_FILTER_ENTRY.Flags, SYSCALL_FILTER_FLAG_ENABLE;
        je      _PASS_SYSCALL;

        mov     ecx, [ebx]SYSCALL_FILTER_ENTRY.ArgumentSize;
        mov     ebp, esp;
        lea     ecx, [ecx + 4];
        mov     esi, edx;
        lea     edx, [esp - 4];
        sub     esp, ecx;
        mov     edi, esp;
        shr     ecx, 2;
        dec     ecx;
        rep     movsd;
        mov     dword ptr [edx], ecx;
        mov     edi, edx;
        mov     ecx, ebx;
        call    eax;
        mov     esp, ebp;
        cmp     dword ptr [edi], 0;
        je      _PASS_SYSCALL;

#if 0
        mov     ecx, dword ptr [edi];
        or      ecx, ecx;
        je      _PASS_SYSCALL;
        dec     ecx;
        je      _BYPASS_SYSCALL;
        dec     ecx;
        jnz     _PASS_SYSCALL;

// CALL_AFTER_RETURN

        mov     ecx, [ebx]SYSCALL_FILTER_ENTRY.ArgumentSize;
        sub     esi, ecx;
        mov     edx, esi;
        mov     eax, ebp;
        mov     ecx, [esp + 0x18];
        mov     edi, esp;
        call    OldSysEnter;
        mov     esp, edi;
        mov     [ebx]SYSCALL_FILTER_ENTRY.Status, eax;
        mov     ecx, [ebx]SYSCALL_FILTER_ENTRY.ArgumentSize;
        mov     eax, [ebx]SYSCALL_FILTER_ENTRY.ProxyFunction;
        push    ebx;
        mov     ebx, esp;
        sub     esp, ecx;
        mov     edi, esp;
        shr     ecx, 2;
        rep     movsd;
        xor     edx, edx;
        mov     ecx, ebp;
        call    eax;
        mov     esp, ebx;
        pop     ebx;

_BYPASS_SYSCALL:

#endif

        mov     ecx, ebx;
        mov     edx, esp;
        mov     edi, [edx + 0x00];
        mov     esi, [edx + 0x04];
        mov     ebp, [edx + 0x08];
        mov     esp, [edx + 0x0C];
        mov     ebx, [edx + 0x10];
        popfd;

        lea     esp, [esp + 0x08];
        jmp     [ecx]SYSCALL_FILTER_ENTRY.ReturnOpAddress;

//        mov     edx, [esp + 8];
//        mov     ecx, [ecx]SYSCALL_FILTER_ENTRY.ArgumentSize;
//        lea     esp, [esp + ecx + 0xC];
//        jmp     edx;

//        mov     ecx, [ebx]SYSCALL_FILTER_ENTRY.ArgumentSize;
//        mov     edx, g_BypassSysEnterRetOp;
//        mov     [edx], ecx;
//        mov     dword ptr [esp + 0x24], offset BypassSysEnter;
//        mov     [esp + 0x1C], eax;

_PASS_SYSCALL:
        popad;
        popfd;
        ret;
    }
}

PUNICODE_STRING GetModuleUnicodePath(PVOID hModule)
{
    PVOID                   pTEB;
    PPEB_LDR_DATA           PebLdr;
    PLDR_DATA_TABLE_ENTRY   LdrModule, FirstLdrModule;

    pTEB = NtCurrentTeb();
    PebLdr = *(PPEB_LDR_DATA *)(*(PULONG_PTR)((ULONG_PTR)pTEB + 0x30) + 0xC);
    LdrModule = (PLDR_DATA_TABLE_ENTRY)PebLdr->InLoadOrderModuleList.Flink;
    FirstLdrModule = LdrModule;

    if (hModule == NULL)
        hModule = *(HMODULE *)(*(PULONG_PTR)((ULONG_PTR)pTEB + 0x30) + 0x8);

    LOOP_FOREVER
    {
        if (LdrModule->DllBase == hModule)
            break;

        LdrModule = (PLDR_DATA_TABLE_ENTRY)LdrModule->InLoadOrderLinks.Flink;
        if (LdrModule == FirstLdrModule)
            return NULL;
    }

    return &LdrModule->FullDllName;
}

NTSTATUS MapNtdll(PVOID *BaseAddress)
{
    NTSTATUS            Status;
    SIZE_T              ViewSize;
    HANDLE              FileHandle, SectionHandle;
    PVOID               NtdllModule;
    OBJECT_ATTRIBUTES   ObjectAttributes;
    UNICODE_STRING     *NtdllPath, NtPath;
    IO_STATUS_BLOCK     IoStatus;

    *BaseAddress = NULL;
    NtdllModule = GetNtdllHandle();
    NtdllPath   = GetModuleUnicodePath(NtdllModule);
    if (NtdllPath == NULL)
        return STATUS_UNSUCCESSFUL;

    RtlDosPathNameToNtPathName_U(NtdllPath->Buffer, &NtPath, NULL, NULL);
    InitializeObjectAttributes(&ObjectAttributes, &NtPath, OBJ_CASE_INSENSITIVE, NULL, NULL);
    Status = NtCreateFile(
                &FileHandle,
                GENERIC_READ | SYNCHRONIZE | FILE_READ_ATTRIBUTES,
                &ObjectAttributes,
                &IoStatus,
                NULL,
                FILE_ATTRIBUTE_NORMAL,
                FILE_SHARE_READ,
                FILE_OPEN,
                FILE_SYNCHRONOUS_IO_ALERT | FILE_OPEN_FOR_BACKUP_INTENT,
                NULL,
                0
             );
    RtlFreeUnicodeString(&NtPath);
    if (!NT_SUCCESS(Status))
        return Status;

    Status = NtCreateSection(
                &SectionHandle,
                GENERIC_READ,
                NULL,
                NULL,
                PAGE_READONLY,
                SEC_IMAGE,
                FileHandle
             );

    NtClose(FileHandle);
    if (!NT_SUCCESS(Status))
        return Status;

    ViewSize = 0;
    Status = NtMapViewOfSection(
                SectionHandle,
                NtCurrentProcess(),
                BaseAddress,
                0,
                0,
                NULL,
                &ViewSize,
                ViewShare,
                0,
                PAGE_READONLY
             );
    NtClose(SectionHandle);

    return Status;
}

NTSTATUS UnmapNtdll(PVOID BaseAddress)
{
    return NtUnmapViewOfSection(NtCurrentProcess(), BaseAddress);
}

NTSTATUS InstallSyscallHook()
{
    BOOL                        IsWow64;
    NTSTATUS                    Status;
    HMODULE                     NtdllModule;
    SIZE_T                      RegionSize, HashTableCount;
    ULONG_PTR                   BaseAddress;
    PBYTE                       Function, Function2;
    LPSTR                       FunctionName;
    PULONG_PTR                  AddressOfNames, AddressOfFunctions;
    PUSHORT                     AddressOfNameOrdinals;
    PIMAGE_DOS_HEADER           DosHeader;
    PIMAGE_NT_HEADERS           NtHeader;
    PIMAGE_EXPORT_DIRECTORY     ExportDirectory;
    SYSCALL_FILTER_ENTRY       *SysCallFilter, *FilterEntry;
    HASH_TABLE_ENTRY           *HashTableEntry;
    LDR_MODULE                 *LdrModule;

    Status = NtQueryInformationProcess(NtCurrentProcess(), ProcessWow64Information, &BaseAddress, sizeof(BaseAddress), NULL);
    if (!NT_SUCCESS(Status))
        return Status;

    IsWow64 = !!BaseAddress;

    RegionSize = MAX_SERVICE_INDEX * sizeof(*g_pSysCallFilters);
    Status = Nt_AllocateMemory(NtCurrentProcess(), (PVOID *)&g_pSysCallFilters, RegionSize, PAGE_READWRITE);
    if (!NT_SUCCESS(Status))
        return Status;

    RegionSize = MAX_SERVICE_INDEX * sizeof(*g_HashTable.Entry);
    Status = Nt_AllocateMemory(NtCurrentProcess(), (PVOID *)&g_HashTable.Entry, RegionSize, PAGE_READWRITE);
    if (!NT_SUCCESS(Status))
        return Status;

    LdrModule = FIELD_BASE(Nt_CurrentPeb()->Ldr->InInitializationOrderModuleList.Flink, LDR_MODULE, InInitializationOrderLinks);
    NtdllModule = (HMODULE)LdrModule->DllBase;
//    Status = MapNtdll((PVOID *)&BaseAddress);
    Status = ReLoadDll(LdrModule->FullDllName.Buffer, (PVOID *)&BaseAddress, NtdllModule);
    if (!NT_SUCCESS(Status))
        return Status;

    DosHeader               = (PIMAGE_DOS_HEADER)BaseAddress;
    NtHeader                = (PIMAGE_NT_HEADERS)((ULONG_PTR)DosHeader + DosHeader->e_lfanew);
    ExportDirectory         = (PIMAGE_EXPORT_DIRECTORY)(NtHeader->OptionalHeader.DataDirectory[IMAGE_DIRECTORY_ENTRY_EXPORT].VirtualAddress + BaseAddress);
    AddressOfNames          = (PULONG_PTR)(ExportDirectory->AddressOfNames + BaseAddress);
    AddressOfFunctions      = (PULONG_PTR)(ExportDirectory->AddressOfFunctions + BaseAddress);
    AddressOfNameOrdinals   = (PUSHORT)(ExportDirectory->AddressOfNameOrdinals + BaseAddress);

    SysCallFilter   = g_pSysCallFilters;
    HashTableEntry  = g_HashTable.Entry;
    for (ULONG Count = ExportDirectory->NumberOfNames; Count; ++AddressOfNames, ++AddressOfNameOrdinals, --Count)
    {
        ULONG ServiceIndex;

        FunctionName = (LPSTR)(*AddressOfNames + BaseAddress);
        if (*(PUSHORT)FunctionName != TAG2('Zw'))
            continue;

        Function = (PBYTE)(AddressOfFunctions[*AddressOfNameOrdinals] + BaseAddress);
        if (Function[0] != 0xB8)  // mov eax, const
        {
            DebugBreakPoint();
            continue;
        }

        Function2       = Function;
        ServiceIndex    = *(PULONG)&Function[1];
        FilterEntry     = &SysCallFilter[ServiceIndex];

        do
        {
            Function += GetOpCodeSize(Function);
        } while (Function[0] != 0xC2 && Function[0] != 0xC3);

        FilterEntry->ReturnOpAddress = (PVOID)(Function - BaseAddress + (ULONG_PTR)NtdllModule);
        if (Function[0] == 0xC2)
            FilterEntry->ArgumentSize = ROUND_UP(*(PUSHORT)&Function[1], 4);

        HashTableEntry->Entry       = FilterEntry;
        HashTableEntry->Hash        = HashAPI(FunctionName);
//        FilterEntry->FilterLock     = &g_FilterCriticalSection;
        FilterEntry->ServiceIndex   = ServiceIndex;
        FilterEntry->FunctionName   = FunctionName - BaseAddress + (ULONG_PTR)NtdllModule;
        ++HashTableEntry;
#if 0
        ULONG len;
        FILE *fp = _wfopen(L"E:\\Desktop\\Source\\Test_Con\\syscallhash.h", L"ab");
        len = fprintf(fp, "#define SYSCALL_%s", FunctionName);
        for (len = 76 - len; len; --len)
            fprintf(fp, " ");
        fprintf(fp, "0x%08X\n", HashTableEntry[-1].Hash);
        fclose(fp);
#endif
    }

//    UnmapNtdll((PVOID)BaseAddress);
    UnLoadDll((PVOID)BaseAddress);

    HashTableCount      = HashTableEntry - g_HashTable.Entry;
    g_HashTable.Count   = HashTableCount;
    HashTableEntry      = g_HashTable.Entry;
    for (ULONG i = HashTableCount; i; --i)
    {
        for (ULONG j = 0; j != i - 1; ++j)
            if (HashTableEntry[j].Hash > HashTableEntry[j + 1].Hash)
                Swap(HashTableEntry[j], HashTableEntry[j + 1]);
    }

//    *(PULONG)BypassSysEnter = 0xC204C483;   // add esp, 4; ret 00
//    g_BypassSysEnterRetOp = (PBYTE)BypassSysEnter + 4;

    if (IsWow64)
    {
        g_CallSystemCall = CallSystemCall_x64;
        HookSysCall_x64();
    }
    else
    {
        g_CallSystemCall = CallSystemCall_x86;
        Status = HookSysCall_x86();
        if (!NT_SUCCESS(Status))
            return Status;
    }

    GetWindowThreadProcessId(GetShellWindow(), &g_ExplorerPID);
//    RtlInitializeCriticalSectionAndSpinCount(&g_FilterCriticalSection, 400);

    return STATUS_SUCCESS;
}

NTSTATUS UnInstallSyscallHook()
{
    if (g_SysEnterSize == -1)
    {
        UnHookSysCall_x64();
    }
    else if (g_SysEnterSize != 0)
    {
        UnHookSysCall_x86();
    }

    if (g_HashTable.Entry != NULL)
    {
        Nt_FreeMemory(NtCurrentProcess(), g_HashTable.Entry);
        g_HashTable.Entry = NULL;
    }

    if (g_pSysCallFilters != NULL)
    {
        Nt_FreeMemory(NtCurrentProcess(), g_pSysCallFilters);
        g_pSysCallFilters = NULL;
    }

//    RtlDeleteCriticalSection(&g_FilterCriticalSection);

    return STATUS_SUCCESS;
}
