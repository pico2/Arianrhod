#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")

#include "MyLibrary.cpp"

TYPE_OF(::CreateProcessW)*  Shell32CreateProcessWPtr;
TYPE_OF(::CreateProcessW)** Shell32CreateProcessWIAT;

UNICODE_STRING  ProbeApplicationName, ProbeCommandLine;
PVOID           InvokeReturnAddress;

BOOL TryIsProbeProcess(PCWSTR ApplicationName, PWSTR CommandLine)
{
    UNICODE_STRING  AppName, CmdLine;

    RtlInitUnicodeString(&AppName, ApplicationName);
    RtlInitUnicodeString(&CmdLine, CommandLine);

    SEH_TRY
    {
        if (CmdLine.Length < ProbeCommandLine.Length)
            return FALSE;

        CmdLine.Buffer = PtrAdd(CmdLine.Buffer, CmdLine.Length - ProbeCommandLine.Length);
        CmdLine.Length = ProbeCommandLine.Length;

        if (!RtlEqualUnicodeString(&CmdLine, &ProbeCommandLine, TRUE))
            return FALSE;

        if (!RtlEqualUnicodeString(&AppName, &ProbeApplicationName, TRUE))
            return FALSE;

        return TRUE;
    }
    SEH_EXCEPT(EXCEPTION_EXECUTE_HANDLER)
    {
        return FALSE;
    }
}

BOOL
NTAPI
ProbeInvokeCreateProcessW(
    PCWSTR                  ApplicationName,
    PWSTR                   CommandLine,
    PSECURITY_ATTRIBUTES    ProcessAttributes,
    PSECURITY_ATTRIBUTES    ThreadAttributes,
    BOOL                    InheritHandles,
    ULONG                   CreationFlags,
    PVOID                   Environment,
    PCWSTR                  CurrentDirectory,
    LPSTARTUPINFOW          StartupInfo,
    PPROCESS_INFORMATION    ProcessInformation
)
{
    if (TryIsProbeProcess(ApplicationName, CommandLine))
    {
        InvokeReturnAddress = _ReturnAddress();
        RtlSetLastWin32Error(NO_ERROR);

        return FALSE;
    }

    return Shell32CreateProcessWPtr(ApplicationName, CommandLine, ProcessAttributes, ThreadAttributes, InheritHandles, CreationFlags, Environment, CurrentDirectory, StartupInfo, ProcessInformation);
}

BOOL
NTAPI
SpeedUpCreateProcessW(
    PCWSTR                  ApplicationName,
    PWSTR                   CommandLine,
    PSECURITY_ATTRIBUTES    ProcessAttributes,
    PSECURITY_ATTRIBUTES    ThreadAttributes,
    BOOL                    InheritHandles,
    ULONG                   CreationFlags,
    PVOID                   Environment,
    PCWSTR                  CurrentDirectory,
    LPSTARTUPINFOW          StartupInfo,
    PPROCESS_INFORMATION    ProcessInformation
)
{
    LOOP_ONCE
    {
        AllocConsole();
        PrintConsoleW(
            L"Application: %s\n"
            L"Commandline: %s\n\n",
            ApplicationName, CommandLine
        );
    }

    return (*Shell32CreateProcessWIAT)(ApplicationName, CommandLine, ProcessAttributes, ThreadAttributes, InheritHandles, CreationFlags, Environment, CurrentDirectory, StartupInfo, ProcessInformation);
}

PVOID ProbeInvokeCreateProcessAddress()
{
    PVOID               Shell32, Shell32CreateProcessW, CreateProcessW;
    PLDR_MODULE         Shell32Module, MainModule;
    SHELLEXECUTEINFOW   ExecuteInfo;
    PIMAGE_NT_HEADERS   NtHeaders;

    Shell32 = Ldr::LoadDll(L"Shell32.dll");

    Shell32CreateProcessW = PtrAdd(Shell32, IATLookupRoutineRVAByHashNoFix(Shell32, KERNEL32_CreateProcessW));

    MainModule = FindLdrModuleByHandle(NULL);

    RtlDuplicateUnicodeString(RTL_DUPSTR_ADD_NULL, &MainModule->FullDllName, &ProbeApplicationName);
    RtlInitUnicodeString(&ProbeCommandLine, L"ML_PROBE_APPLICATION_COMMAMD_LINE");

    ZeroMemory(&ExecuteInfo, sizeof(ExecuteInfo));

    ExecuteInfo.cbSize          = sizeof(ExecuteInfo);
    ExecuteInfo.fMask           = SEE_MASK_NOASYNC | SEE_MASK_FLAG_NO_UI;
    ExecuteInfo.lpVerb          = L"open";
    ExecuteInfo.lpFile          = ProbeApplicationName.Buffer;
    ExecuteInfo.lpParameters    = ProbeCommandLine.Buffer;
    ExecuteInfo.nShow           = SW_SHOW;

    *(PVOID *)&Shell32CreateProcessWIAT = Shell32CreateProcessW;
    *(PVOID *)&Shell32CreateProcessWPtr = *(PVOID *)Shell32CreateProcessWIAT;

    CreateProcessW = ProbeInvokeCreateProcessW;
    WriteProtectMemory(CurrentProcess, Shell32CreateProcessW, &CreateProcessW, sizeof(CreateProcessW));
    ShellExecuteExW(&ExecuteInfo);
    WriteProtectMemory(CurrentProcess, Shell32CreateProcessW, &Shell32CreateProcessWPtr, sizeof(Shell32CreateProcessWPtr));

    RtlFreeUnicodeString(&ProbeApplicationName);

    NtHeaders = RtlImageNtHeader(Shell32);

    if (InvokeReturnAddress < Shell32 || InvokeReturnAddress > PtrAdd(Shell32, NtHeaders->OptionalHeader.SizeOfImage))
        return NULL;

    return InvokeReturnAddress;
}

BOOL HookCallCreateProcessFast(PVOID InvokeReturnAddress)
{
    PBYTE               InvokeBuffer;
    PVOID               *JumpAddressBegin, *JumpAddressEnd, HookRoutine;
    PIMAGE_NT_HEADERS   NtHeaders;
    PLDR_MODULE         Shell32;

    InvokeBuffer = (PBYTE)InvokeReturnAddress;
    LOOP_ONCE
    {
        PrintConsoleW(L"phase 0\n");

        if (*(PUSHORT)&InvokeBuffer[-6] != 0x15FF)
            continue;

#if ML_X86

        if (*(PULONG)&InvokeBuffer[-4] != (ULONG)Shell32CreateProcessWIAT)
            break;

#elif ML_AMD64

        if ((PVOID)PtrAdd(InvokeBuffer, *(PULONG)&InvokeBuffer[-4]) != Shell32CreateProcessWIAT)
            break;

#endif // arch

        Shell32 = FindLdrModuleByName(&WCS2US(L"SHELL32.dll"));
        NtHeaders = RtlImageNtHeader(Shell32->DllBase);
        if (NtHeaders == NULL)
            break;

        JumpAddressEnd = (PVOID *)PtrAdd(Shell32->DllBase, ROUND_UP(NtHeaders->OptionalHeader.SizeOfHeaders, NtHeaders->OptionalHeader.SectionAlignment));
        JumpAddressBegin = (PVOID *)(IMAGE_FIRST_SECTION(NtHeaders) + NtHeaders->FileHeader.NumberOfSections);

        while (JumpAddressBegin < JumpAddressEnd)
        {
            if (*JumpAddressBegin == NULL)
                break;

            ++JumpAddressBegin;
        }

        if (JumpAddressBegin >= JumpAddressEnd)
            break;

        HookRoutine = SpeedUpCreateProcessW;
        WriteProtectMemory(CurrentProcess, JumpAddressBegin, &HookRoutine, sizeof(HookRoutine));

#if ML_X86

        WriteProtectMemory(CurrentProcess, &InvokeBuffer[-4], &JumpAddressBegin, sizeof(JumpAddressBegin));

#elif ML_AMD64

        LONG64 RelateOffset;

        RelateOffset = (TYPE_OF(RelateOffset))PtrSub(JumpAddressBegin, InvokeBuffer);

        WriteProtectMemory(CurrentProcess, &InvokeBuffer[-4], &RelateOffset, sizeof(LONG));

#endif

        return TRUE;
    }

    return FALSE;
}

BOOL HookCallCreateProcess()
{
    PVOID InvokeReturnAddress;

    SEH_TRY
    {
        InvokeReturnAddress = ProbeInvokeCreateProcessAddress();
        if (InvokeReturnAddress == NULL)
            return FALSE;

        return HookCallCreateProcessFast(InvokeReturnAddress);
    }
    SEH_EXCEPT(EXCEPTION_EXECUTE_HANDLER)
    {
        return FALSE;
    }
}

NTSTATUS CheckIsExplorer()
{
    NTSTATUS                    Status;
    PLDR_MODULE                 Module;
    PWSTR                       FullPath, BackSlash;
    ULONG                       ReturnLength;
    ULONG_PTR                   Length;
    MEMORY_BASIC_INFORMATION    MemoryBasic;

    PPROCESS_IMAGE_FILE_NAME            ExeFileName;
    PMEMORY_MAPPED_FILENAME_INFORMATION NtdllFileName;

    static WCHAR ExplorerName[] = L"explorer.exe";

    Status = NtQueryVirtualMemory(CurrentProcess, NtClose, MemoryMappedFilenameInformation, NULL, 0, &Length);
    if (Status != STATUS_INFO_LENGTH_MISMATCH)
        return Status;

    NtdllFileName = (PMEMORY_MAPPED_FILENAME_INFORMATION)AllocStack(Length);
    Status = NtQueryVirtualMemory(CurrentProcess, NtClose, MemoryMappedFilenameInformation, NtdllFileName, Length, &Length);
    FAIL_RETURN(Status);

    Status = NtQueryInformationProcess(CurrentProcess, ProcessImageFileName, NULL, 0, &ReturnLength);
    if (Status != STATUS_INFO_LENGTH_MISMATCH)
        return Status;

    ExeFileName = (PPROCESS_IMAGE_FILE_NAME)AllocStack(ReturnLength);
    Status = NtQueryInformationProcess(CurrentProcess, ProcessImageFileName, ExeFileName, ReturnLength, &ReturnLength);
    FAIL_RETURN(Status);

    BackSlash = NULL;
    Length = NtdllFileName->Name.Length / sizeof(WCHAR) - 1;
    for (; Length != 0; --Length)
    {
        if (NtdllFileName->Name.Buffer[Length] != '\\')
            continue;

        if (BackSlash != NULL)
        {
            BackSlash = &NtdllFileName->Name.Buffer[Length];
            break;
        }

        BackSlash = &NtdllFileName->Name.Buffer[Length];
    }

    if (BackSlash == NULL)
        return STATUS_NO_MATCH;

    ++BackSlash;

    CopyStruct(BackSlash, ExplorerName, sizeof(ExplorerName));

    NtdllFileName->Name.Length = PtrOffset(BackSlash + CONST_STRLEN(ExplorerName), NtdllFileName->Name.Buffer);

    Status = RtlEqualUnicodeString(&NtdllFileName->Name, &ExeFileName->ImageFileName, TRUE) ? STATUS_SUCCESS : STATUS_NO_MATCH;

    return Status;
}

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    if (NT_FAILED(CheckIsExplorer()))
        return FALSE;

    {
        NtFileDisk  f;
        WCHAR       buf[0x100];
        SYSTEMTIME  st;

        GetLocalTime(&st);
        f.Create(L"C:\\test.txt");
        f.Write(buf, swprintf(buf, L"\xFEFF%08X, %02d:%02d:%02d", BaseAddress, st.wHour, st.wMinute, st.wSecond) * sizeof(WCHAR));
    }

    if (!HookCallCreateProcess())
        return FALSE;

    LdrDisableThreadCalloutsForDll(BaseAddress);
    LdrAddRefDll(LDR_ADDREF_DLL_PIN, BaseAddress);

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
