#pragma comment(linker, "/ENTRY:main")
//#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
//#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")
//#pragma comment(lib, "../LoaderDll/LoaderDll.lib")

#include "ml.cpp"

using ml::String;

WCHAR DllFullPath[MAX_NTPATH];

VOID
NTAPI
LoadLibraryApc(
    PVOID NormalContext,
    PVOID SystemArgument1,
    PVOID SystemArgument2
)
{
    PVOID ModuleBase;
    UNICODE_STRING DllPath;

    API_POINTER(LdrLoadDll) LdrLoadDll;

    DllPath.Length          = (USHORT)NormalContext;
    DllPath.MaximumLength   = (USHORT)NormalContext;
    DllPath.Buffer          = DllFullPath;

    *(PVOID *)&LdrLoadDll = LookupExportTable(GetNtdllHandle(), NTDLL_LdrLoadDll);

    LdrLoadDll(nullptr, nullptr, &DllPath, &ModuleBase);
}

NTSTATUS CopySelfToTarget(HANDLE Process, PVOID *BaseAddress)
{
    NTSTATUS    status;
    PLDR_MODULE self;
    PVOID       buffer, remote;

    self = FindLdrModuleByHandle(nullptr);

    remote = nullptr;
    status = Mm::AllocVirtualMemoryEx(Process, &remote, self->SizeOfImage, PAGE_EXECUTE_READWRITE);
    FAIL_RETURN(status);

    buffer = AllocateMemoryP(self->SizeOfImage);
    if (buffer == nullptr)
    {
        Mm::FreeVirtualMemory(remote, Process);
        return STATUS_NO_MEMORY;
    }

    CopyMemory(buffer, &__ImageBase, self->SizeOfImage);
    RelocPeImage(buffer, &__ImageBase, nullptr, remote);

    status = Mm::WriteMemory(Process, remote, buffer, self->SizeOfImage);
    if (NT_FAILED(status))
    {
        FreeMemoryP(buffer);
        Mm::FreeVirtualMemory(remote, Process);
        return status;
    }

    *BaseAddress = remote;

    return STATUS_SUCCESS;
}

ForceInline Void main2(Long_Ptr argc, WChar **argv)
{
    NTSTATUS            Status;
    PVOID               BaseAddress;
    ULONG_PTR           DllPathLength;
    PROCESS_INFORMATION pi;

    ml::MlInitialize();
    SetExeDirectoryAsCurrent();

    String dll;

    LOOP_ONCE
    {
        Rtl::GetModuleDirectory(dll, nullptr);
        dll += L"TaiGJBreak2.1.0.0.exe";

        Status = Ps::CreateProcess(dll, nullptr, nullptr, CREATE_SUSPENDED, nullptr, &pi);
        if (NT_FAILED(Status))
            return;

        Rtl::GetModuleDirectory(dll, nullptr);
        dll += L"TaiG3.dll";

        CopyMemory(DllFullPath, (PWSTR)dll, dll.GetSize());

        //pi.hProcess = CurrentProcess;
        //pi.hThread = CurrentThread;

        Status = CopySelfToTarget(pi.hProcess, &BaseAddress);
        FAIL_BREAK(Status);

        Status = NtQueueApcThread(
                        pi.hThread,
                        (PKNORMAL_ROUTINE)PtrAdd(PtrOffset(LoadLibraryApc, &__ImageBase), BaseAddress),
                        (PVOID)(ULONG)dll.GetSize(),
                        0,
                        0
                    );
    }

    NtResumeProcess(pi.hProcess);
    NtClose(pi.hProcess);
    NtClose(pi.hThread);
}

int __cdecl main(Long_Ptr argc, wchar_t **argv)
{
    getargsW(&argc, &argv);
    main2(argc, argv);
    ReleaseArgv(argv);
    Ps::ExitProcess(0);
}
