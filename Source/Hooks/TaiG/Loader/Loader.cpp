//#pragma comment(linker, "/ENTRY:main")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")
//#pragma comment(lib, "../LoaderDll/LoaderDll.lib")

#include "ml.cpp"

#if 1
    #define DBG(...)
#else
    #define DBG(...) (PrintConsole(__VA_ARGS__), PrintConsole(L"\n"))
#endif

using ml::String;

PVOID MainThreadEntry;
WCHAR DllFullPath[MAX_NTPATH];

VOID FASTCALL LoadLibraryWorder()
{
    PVOID ModuleBase;
    UNICODE_STRING DllPath;

    API_POINTER(LdrLoadDll) LdrLoadDll;

    DllPath.Length          = (USHORT)StrLengthW(DllFullPath) * sizeof(DllFullPath[0]);
    DllPath.MaximumLength   = DllPath.Length;
    DllPath.Buffer          = DllFullPath;

    *(PVOID *)&LdrLoadDll = LookupExportTable(GetNtdllHandle(), NTDLL_LdrLoadDll);

    LdrLoadDll(nullptr, nullptr, &DllPath, &ModuleBase);
}

VOID
NTAPI
LoadLibraryApc(
    PVOID NormalContext,
    PVOID SystemArgument1,
    PVOID SystemArgument2
)
{
    return LoadLibraryWorder();
}

NAKED VOID LoadLibraryByModifyEip()
{
    INLINE_ASM
    {
        //__emit 0xEB;
        //__emit 0xFE;
        push MainThreadEntry;
        pushad;
        call LoadLibraryWorder;
        popad;
        ret;
    }
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

NTSTATUS ClearBeingDebugged(HANDLE Process, HANDLE Thread)
{
    NTSTATUS                Status;
    BOOLEAN                 BeingDebugged;
    PPEB_BASE               Peb;
    PVOID                   FsBase;
    CONTEXT                 Context;
    DESCRIPTOR_TABLE_ENTRY  Descriptor;

    Context.ContextFlags = CONTEXT_SEGMENTS;
    Status = NtGetContextThread(Thread, &Context);
    FAIL_RETURN(Status);

    Descriptor.Selector = Context.SegFs;
    Status = NtQueryInformationThread(Thread, ThreadDescriptorTableEntry, &Descriptor, sizeof(Descriptor), NULL);
    FAIL_RETURN(Status);

    FsBase = (PVOID)((Descriptor.Descriptor.HighWord.Bits.BaseHi << 24)  |
                (Descriptor.Descriptor.HighWord.Bits.BaseMid << 16) |
                (Descriptor.Descriptor.BaseLow));

    if (FsBase == NULL)
        return STATUS_NOT_FOUND;

    Peb = (PPEB_BASE)PtrAdd(FsBase, PEB_OFFSET);

    Status = ReadMemory(Process, Peb, &Peb, sizeof(Peb));
    FAIL_RETURN(Status);

    //Status = ReadMemory(Process, &Peb->BeingDebugged, &BeingDebugged, sizeof(BeingDebugged));
    //FAIL_RETURN(Status);

    BeingDebugged = FALSE;
    Status = WriteMemory(Process, &Peb->BeingDebugged, &BeingDebugged, sizeof(BeingDebugged));
    FAIL_RETURN(Status);

    return Status;
}

NTSTATUS InjectByModifyContext(HANDLE Process, HANDLE Thread, PVOID RemoteBase)
{
    NTSTATUS    Status;
    CONTEXT     Context, InitialContext;
    ULONG_PTR   Offset, StackSize;
    //BYTE        StackBuffer[0x1000];
    PBYTE       StackBuffer;
    PULONG_PTR  Probe, ProbeEnd;
    PVOID       ContextAddress, StackTop;
    DBGUI_WAIT_STATE_CHANGE DbgState;

    auto DbgX = [&] () -> NTSTATUS
    {
        NTSTATUS Status;

        Status = DbgUiContinue(&DbgState.AppClientId, DBG_CONTINUE);
        FAIL_RETURN(Status);

        Status = DbgUiWaitStateChange(&DbgState, nullptr);
        return Status;
    };

    BOOL        ProcessCreated = FALSE;
    BYTE        LdrInitializeThunkFirstByte;
    PVOID       RemoteLdrInitializeThunk = nullptr;
    ULONG_PTR   DllLoadCount = 0;
    MEMORY_BASIC_INFORMATION mbi;

    DBG(L"Get1");

    InitialContext.ContextFlags = CONTEXT_INTEGER | CONTEXT_CONTROL;
    Status = NtGetContextThread(Thread, &InitialContext);
    FAIL_RETURN(Status);

    DBG(L"wait");

    Status = DbgUiWaitStateChange(&DbgState, nullptr);
    for (; NT_SUCCESS(Status); Status = DbgX())
    {
        DBG(L"NewState: %p", DbgState.NewState);
        CONTEXT ctx;

        ctx.ContextFlags = CONTEXT_CONTROL;
        NtGetContextThread(Thread, &ctx);
        DBG(L"eip = %p", ctx.Eip);
        DBG(L"esp = %p", ctx.Esp);
        DBG(L"");

        switch (DbgState.NewState)
        {
            case DbgCreateProcessStateChange:
                if (DbgState.StateInfo.CreateProcessInfo.HandleToProcess != nullptr)
                    NtClose(DbgState.StateInfo.CreateProcessInfo.HandleToProcess);

                if (DbgState.StateInfo.CreateProcessInfo.HandleToThread != nullptr)
                    NtClose(DbgState.StateInfo.CreateProcessInfo.HandleToThread);

                if (DbgState.StateInfo.CreateProcessInfo.NewProcess.FileHandle != nullptr)
                    NtClose(DbgState.StateInfo.CreateProcessInfo.NewProcess.FileHandle);

                ProcessCreated = TRUE;
                continue;

            case DbgCreateThreadStateChange:
                if (DbgState.StateInfo.CreateThread.HandleToThread != nullptr)
                    NtClose(DbgState.StateInfo.CreateThread.HandleToThread);

                continue;

            case DbgLoadDllStateChange:
            {
                if (DbgState.StateInfo.LoadDll.FileHandle != nullptr)
                    NtClose(DbgState.StateInfo.LoadDll.FileHandle);

                if (ProcessCreated == FALSE)
                    continue;

                switch (++DllLoadCount)
                {
                    case 1: // ntdll
                    {
                        //DBG(L"read byte");
                        //RemoteLdrInitializeThunk = PtrAdd(DbgState.StateInfo.LoadDll.BaseOfDll, PtrOffset(LdrInitializeThunk, GetNtdllHandle()));
                        //Status = Mm::ReadMemory(Process, RemoteLdrInitializeThunk, &LdrInitializeThunkFirstByte, sizeof(LdrInitializeThunkFirstByte));
                        //if (NT_FAILED(Status))
                        //    break;

                        //Status = ClearBeingDebugged(Process, Thread);
                        //FAIL_BREAK(Status);

                        //DBG(L"write f4");
                        //BYTE CC = 0xF4; // hlt
                        //Status = Mm::WriteProtectMemory(Process, RemoteLdrInitializeThunk, &CC, sizeof(CC));
                        //if (NT_FAILED(Status))
                        //    break;

                        break;
                    }

                    case 2: // kernel32
                        break;
                }

                if (DllLoadCount > 1 || NT_FAILED(Status))
                    break;

                continue;
            }

            // case DbgExceptionStateChange:
            //     if (RemoteLdrInitializeThunk == nullptr ||
            //         DbgState.StateInfo.Exception.ExceptionRecord.ExceptionAddress != RemoteLdrInitializeThunk ||
            //         DbgState.StateInfo.Exception.ExceptionRecord.ExceptionCode != EXCEPTION_PRIV_INSTRUCTION)
            //     {
            //         continue;
            //     }

            //     DBG(L"restore");

            //     Status = Mm::WriteProtectMemory(Process, RemoteLdrInitializeThunk, &LdrInitializeThunkFirstByte, sizeof(LdrInitializeThunkFirstByte));
            //     break;

            default:
                continue;
        }

        break;
    }

    FAIL_RETURN(Status);

    DBG(L"get 2");

    Context.ContextFlags = CONTEXT_INTEGER | CONTEXT_CONTROL;
    Status = NtGetContextThread(Thread, &Context);
    FAIL_RETURN(Status);

    DBG(L"read stack");

    StackTop = (PVOID)(ULONG_PTR)Context.Esp;

    Status = NtQueryVirtualMemory(Process, StackTop, MemoryBasicInformation, &mbi, sizeof(mbi), nullptr);
    FAIL_RETURN(Status);

    StackSize = mbi.RegionSize - PtrOffset(StackTop, mbi.BaseAddress);
    StackBuffer = (PBYTE)AllocStack(StackSize);
    Status = Mm::ReadMemory(Process, StackTop, StackBuffer, StackSize, &StackSize);
    FAIL_RETURN(Status);

    Probe = (PULONG_PTR)StackBuffer;
    ProbeEnd = PtrAdd(Probe, StackSize);
    ContextAddress = nullptr;

    for (; Probe < ProbeEnd; ++Probe)
    {
        PCONTEXT ContextPtr;

        ContextPtr = (PCONTEXT)Probe;
        if (ContextPtr->Eax == InitialContext.Eax &&
            ContextPtr->Ecx == InitialContext.Ecx &&
            ContextPtr->Edx == InitialContext.Edx &&
            ContextPtr->Ebx == InitialContext.Ebx &&
            ContextPtr->Esp == InitialContext.Esp &&
            ContextPtr->Ebp == InitialContext.Ebp &&
            ContextPtr->Esi == InitialContext.Esi &&
            ContextPtr->Edi == InitialContext.Edi &&
            ContextPtr->Eip == InitialContext.Eip)
        {
            ContextAddress = PtrAdd(StackTop, PtrOffset(Probe, StackBuffer));
            //break;
        }
    }

    if (ContextAddress == nullptr)
        return STATUS_NOT_FOUND;

    DBG(L"read context");

    Status = Mm::ReadMemory(Process, ContextAddress, &Context, sizeof(Context));
    FAIL_RETURN(Status);

    DBG(L"eax = %p", Context.Eax);

    //Context.Esp -= sizeof(PVOID);
    //Status = Mm::WriteMemory(Process, (PVOID)Context.Esp, &Context.Eip, sizeof(Context.Eip));
    //FAIL_RETURN(Status);

    DBG(L"write ep");

    Status = Mm::WriteMemory(Process, PtrAdd(RemoteBase, PtrOffset(&MainThreadEntry, &__ImageBase)), &Context.Eip, sizeof(Context.Eip));
    FAIL_RETURN(Status);

    DBG(L"write context");

    Context.Eip = PtrAdd(PtrOffset(LoadLibraryByModifyEip, &__ImageBase), RemoteBase);
    Status = Mm::WriteMemory(Process, ContextAddress, &Context, sizeof(Context));

    DBG(L"continue");

    Status = DbgUiContinue(&DbgState.AppClientId, DBG_CONTINUE);
    FAIL_RETURN(Status);

    DBG(L"stop");

    Status = DbgUiStopDebugging(Process);
    FAIL_RETURN(Status);

    return Status;
}

ForceInline NTSTATUS main2(Long_Ptr argc, WChar **argv)
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
        dll += L"TaiGJBreak_2120.exe";

        WCHAR NoDebugHeap[] = { '_', 'N', 'O', '_', 'D', 'E', 'B', 'U', 'G', '_', 'H', 'E', 'A', 'P'};
        WCHAR Yes[] = { '1' };

        UNICODE_STRING Name, Value;

        Name.Length = sizeof(NoDebugHeap);
        Name.MaximumLength = Name.Length;
        Name.Buffer = NoDebugHeap;

        Value.Length = sizeof(Yes);
        Value.MaximumLength = Name.Length;
        Value.Buffer = Yes;

        RtlSetEnvironmentVariable(nullptr, &Name, &Value);

        Status = Ps::CreateProcess(dll, nullptr, nullptr, DEBUG_PROCESS | DEBUG_ONLY_THIS_PROCESS, nullptr, &pi);
        FAIL_RETURN(Status);

        Rtl::GetModuleDirectory(dll, nullptr);
        dll += L"TaiG3.dll";

        CopyMemory(DllFullPath, (PWSTR)dll, dll.GetSize());

        //pi.hProcess = CurrentProcess;
        //pi.hThread = CurrentThread;

        DBG(L"CopySelfToTarget");
        Status = CopySelfToTarget(pi.hProcess, &BaseAddress);
        FAIL_BREAK(Status);

        DBG(L"NtGetContextThread");
        Status = InjectByModifyContext(pi.hProcess, pi.hThread, BaseAddress);
        FAIL_BREAK(Status);

        //DBG(L"QueueApc\n");

        //Status = NtQueueApcThread(
        //                pi.hThread,
        //                (PKNORMAL_ROUTINE)PtrAdd(PtrOffset(LoadLibraryApc, &__ImageBase), BaseAddress),
        //                0,
        //                0,
        //                0
        //            );

    }

    DBG(L"%p", Status);

    if (NT_SUCCESS(Status))
    {
        NtResumeProcess(pi.hProcess);
    }
    else
    {
        NtTerminateProcess(pi.hProcess, 0);
    }

    NtClose(pi.hProcess);
    NtClose(pi.hThread);

    //PauseConsole();

    return Status;
}

int __cdecl main(Long_Ptr argc, wchar_t **argv)
{
    //getargsW(&argc, &argv);
    NTSTATUS st = main2(argc, argv);
    //ReleaseArgv(argv);
    Ps::ExitProcess(st);
}
