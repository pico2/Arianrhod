#include "PyHooker.h"
#include "HandleTable.cpp"

#define POINTER_SIZE sizeof(PVOID)

PyHooker::PyHooker() : MemoryAllocator(RtlCreateHeap(HEAP_CREATE_ENABLE_EXECUTE | HEAP_GROWABLE | HEAP_CREATE_ALIGN_16, nullptr, 0, 0, nullptr, nullptr))
{
    this->VehHandle = nullptr;
    RtlInitializeCriticalSectionAndSpinCount(&this->Lock, 4000);
}

PyHooker::~PyHooker()
{
    PROTECT_SECTION(&this->Lock)
    {
        this->RecordTable.Destroy(
            [](PML_HANDLE_TABLE_ENTRY Entry, ULONG_PTR Count, PVOID Context) -> NTSTATUS
            {
                FOR_EACH(Entry, Entry, Count)
                {
                    if (Entry->Handle == nullptr)
                        continue;
                    ((PyHooker *)Context)->PyUnHookFunction(((PHOOK_RECORD)(Entry->Handle))->Address);
                }

                return STATUS_SUCCESS;
            },
            this
        );

        RtlRemoveVectoredExceptionHandler(this->VehHandle);
    }

    RtlDeleteCriticalSection(&this->Lock);
}

NTSTATUS PyHooker::Initialize()
{
    FAIL_RETURN(this->InitRecordTable());
    FAIL_RETURN(this->InitPython());
    FAIL_RETURN(this->InitDispatcher());

    return STATUS_SUCCESS;
}

NTSTATUS PyHooker::InitPython()
{
    this->python.Initialize();

    LONG_PTR argc;
    PWSTR *argv;

    getargsW(&argc, &argv);
    PySys_SetArgv(argc, argv);
    ReleaseArgv(argv);

    this->python.Register(
        [=](ULONG_PTR Address, PyObject* Callable)
        {
            return this->PyHookFunction((PVOID)Address, Callable);
        },
        L"Hook"
    )
    .Register(
        [=](ULONG_PTR Address)
        {
            return this->PyUnHookFunction((PVOID)Address);
        },
        L"UnHook"
    )
    .Register(
        [=] (ULONG_PTR Address, ULONG_PTR Length) -> ByteArray
        {
            NTSTATUS    Status;
            ByteArray   Buffer;

            if (Length == 0)
                return Buffer;

            Buffer.SetSize(Length);
            Status = Mm::ReadMemory(CurrentProcess, (PVOID)Address, Buffer.GetData(), Length, &Length);
            if (NT_FAILED(Status))
                return Buffer;

            Buffer.UpdateDataCount(Length);

            return Buffer;
        },
        L"ReadMemory"
    )
    .Register(
        [=] (ULONG_PTR Address, ByteArray &Buffer) -> ULONG_PTR
        {
            NTSTATUS    Status;
            ULONG_PTR   Length;

            if (Buffer.GetSize() == 0)
                return 0;

            Status = Mm::WriteMemory(CurrentProcess, (PVOID)Address, Buffer.GetData(), Buffer.GetSize(), &Length);
            if (NT_FAILED(Status))
                return 0;

            return Length;
        },
        L"WriteMemory"
    )
    .Register(
        [=] (ULONG_PTR Address) -> ByteArray
        {
            return ByteArray((PBYTE)Address, StrLengthA((PCSTR)Address));
        },
        L"ReadAnsi"
    )
    .Register(
        [=] (ULONG_PTR Address) -> String
        {
            return String((PCWSTR)Address);
        },
        L"ReadUnicode"
    )
    .Register(
        [=] (PVOID _Context, PVOID Stack, ULONG_PTR StackSize) -> ULONG64
        {
            PCONTEXT Context = (PCONTEXT)_Context;

            extern VOID InvokeNativeFunction(PCONTEXT Context, BOOL TestAlert = FALSE);

            InvokeNativeFunction(Context);

            ULARGE_INTEGER ret;

            ret.LowPart = Context->Eax;
            ret.HighPart = Context->Edx;

            return ret.QuadPart;
        },
        L"Call"
    )
    .AddToModule(L"_pyhooker");

    return STATUS_SUCCESS;
}

NoInline VOID CDECL NativeInvoker(PCONTEXT Context, BOOL TestAlert = FALSE)
{
    *(PVOID *)Context->Esp = _ReturnAddress();
    *(PVOID *)_AddressOfReturnAddress() = NtContinue;
}

NoInline VOID InvokeNativeFunction(PCONTEXT Context, BOOL TestAlert = FALSE)
{
    auto X = [] (PEXCEPTION_POINTERS p, PCONTEXT Context)
    {
        *Context = *p->ContextRecord;
        return EXCEPTION_EXECUTE_HANDLER;
    };

    SEH_TRY
    {
        VOID (NTAPI *_NativeInvoker)(PCONTEXT Context, BOOL TestAlert);

        *(PVOID *)&_NativeInvoker = NativeInvoker;
        _NativeInvoker(Context, TestAlert);
        DebugBreakPoint();
    }
    SEH_EXCEPT(*Context = *(((PEXCEPTION_POINTERS)GetExceptionInformation())->ContextRecord), EXCEPTION_EXECUTE_HANDLER)
    {
    }

    CLEAR_FLAG(Context->ContextFlags, CONTEXT_XSTATE ^ CONTEXT_i386);
}

NTSTATUS PyHooker::InitDispatcher()
{
    this->VehHandle = RtlAddVectoredExceptionHandler(TRUE, PyHooker::StaticExceptionHandler);
    return this->VehHandle != nullptr ? STATUS_SUCCESS : STATUS_INVALID_EXCEPTION_HANDLER;
}

NTSTATUS PyHooker::InitRecordTable()
{
    return this->RecordTable.Create() == nullptr ? STATUS_NO_MEMORY : STATUS_SUCCESS;
}

NTSTATUS PyHooker::LoadPyFile()
{
    this->python.Invoke<VOID>(L"pyhooker", L"main");
    return STATUS_SUCCESS;
}

PHOOK_RECORD PyHooker::LookupAndReferenceRecord(PVOID Address)
{
    PHOOK_RECORD            Record;
    PML_HANDLE_TABLE_ENTRY  Entry;

    auto IsBreakPoint = [=](PVOID Address)
    {
        BOOL        IsBreakPoint;
        ULONG       Protect;
        NTSTATUS    Status;

        Status = Mm::ProtectVirtualMemory(Address, 1, PAGE_EXECUTE_READWRITE, &Protect);
        if (NT_FAILED(Status))
            return FALSE;

        IsBreakPoint = *(PBYTE)Address == this->BreakOpCode;
        Mm::ProtectVirtualMemory(Address, 1, Protect, &Protect);

        return IsBreakPoint;
    };

    PROTECT_SECTION(&this->Lock)
    {
        if (IsBreakPoint(Address) == FALSE)
            break;

        Entry = this->RecordTable.Lookup(Address);
        if (Entry == nullptr || Entry->Handle == nullptr)
            break;

        Record = (PHOOK_RECORD)Entry->Handle;
        if (Record == nullptr)
            break;

        Record->AddRef();
        return Record;
    }

    return nullptr;
}

LONG NTAPI PyHooker::StaticExceptionHandler(PEXCEPTION_POINTERS ExceptionPointers)
{
    return PyHooker::instance->ExceptionHandler(ExceptionPointers);
}

VOID FASTCALL PyHooker::StaticPyDispatcher(PHOOK_RECORD Record, PDISPATCHER_CONTEXT Context)
{
    return Context->hooker->PyDispatcher(Record, &Context->Context);
}

VOID PyHooker::PyDispatcher(PHOOK_RECORD Record, PCONTEXT Context)
{
    CONTEXT LocalContext;
    TEB_ACTIVE_FRAME trap = PY_CALLBACK_IN_PROGRESS;

    trap.Data = (ULONG_PTR)Record;
    trap.Push();

    LocalContext = *Context;

    Context = &LocalContext;
    Context->Eip = (ULONG_PTR)Record->Instruction;

    PROTECT_SECTION(&this->Lock)
    {
        this->python.Invoke<VOID>(Record->Callback, (ULONG_PTR)Record->Address, (ULONG_PTR)Context);
    }

    Record->Release();

    NtContinue(Context, FALSE);
}

LONG PyHooker::ExceptionHandler(PEXCEPTION_POINTERS ExceptionPointers)
{
    switch (ExceptionPointers->ExceptionRecord->ExceptionCode)
    {
        case EXCEPTION_PRIV_INSTRUCTION:
            break;

        //case EXCEPTION_BREAKPOINT:
        //    break;

        default:
            return EXCEPTION_CONTINUE_SEARCH;
    }

    PULONG_PTR              Esp, StackLimit;
    PHOOK_RECORD            Record;
    PCONTEXT                Context;
    PEXCEPTION_RECORD       ExceptionRecord;
    PDISPATCHER_CONTEXT     DispatcherContext;

    Context         = ExceptionPointers->ContextRecord;
    ExceptionRecord = ExceptionPointers->ExceptionRecord;

    Record = LookupAndReferenceRecord(ExceptionRecord->ExceptionAddress);
    if (Record == nullptr)
        return EXCEPTION_CONTINUE_SEARCH;

    if (FindThreadFrameEx(PY_CALLBACK_IN_PROGRESS, (ULONG_PTR)Record) != nullptr)
    {
        Record->Release();
        Context->Eip = (ULONG_PTR)Record->Instruction;
        return EXCEPTION_CONTINUE_EXECUTION;
    }

    StackLimit = (PULONG_PTR)CurrentTeb()->NtTib.StackLimit;
    Esp = (PULONG_PTR)Context->Esp;

    while (PtrOffset(Esp, StackLimit) <= 0x5000)
    {
        _InterlockedOr((PLONG)PtrSub(StackLimit, 0x10), 0);
        StackLimit = (PULONG_PTR)CurrentTeb()->NtTib.StackLimit;
    }

    DispatcherContext = (PDISPATCHER_CONTEXT)StackLimit;
    DispatcherContext->Context = *Context;

    CLEAR_FLAG(DispatcherContext->Context.ContextFlags, CONTEXT_XSTATE ^ CONTEXT_i386);
    DispatcherContext->hooker = this;

    Context->Ecx = (ULONG_PTR)Record;
    Context->Edx = (ULONG_PTR)StackLimit;
    Context->Eip = (ULONG_PTR)StaticPyDispatcher;

    return EXCEPTION_CONTINUE_EXECUTION;
}

NTSTATUS PyHooker::PyHookFunction(PVOID Address, PyObject* Callable)
{
    PHOOK_RECORD Record;
    MlPyObject _(Callable);

    if (PyCallable_Check(Callable) == FALSE)
        return STATUS_OBJECT_TYPE_MISMATCH;

    Record = LookupAndReferenceRecord(Address);
    if (Record != nullptr)
    {
        Record->Release();
        return STATUS_ADDRESS_ALREADY_EXISTS;
    }

    PROTECT_SECTION(&this->Lock)
    {
        Record = this->CreateHookRecord(Address, Callable);
        if (Record == nullptr)
            return STATUS_NO_MEMORY;

        this->RecordTable.Insert(Address)->Handle = Record;
    }

    return STATUS_SUCCESS;
}

NTSTATUS PyHooker::PyUnHookFunction(PVOID Address)
{
    PHOOK_RECORD Record;

    Record = LookupAndReferenceRecord(Address);
    if (Record == nullptr)
        return STATUS_ADDRESS_NOT_ASSOCIATED;

    Record->Release();

    PROTECT_SECTION(&this->Lock)
    {
        this->RecordTable.Remove(Record->Address);
        DestroyHookRecord(Record);
    }

    return STATUS_SUCCESS;
}

PHOOK_RECORD PyHooker::CreateHookRecord(PVOID Address, PyObject* Callable)
{
    NTSTATUS        Status;
    PHOOK_RECORD    Record;
    ULONG           Protect;
    ULONG_PTR       TargetOpLength, SourceOpLength;

    Record = (PHOOK_RECORD)Alloc(sizeof(*Record));
    if (Record == nullptr)
        return Record;

    new (Record) HOOK_RECORD();

    Record->Address     = Address;
    Record->Callback    = Callable;

    PyAddRef(Callable);

    LOOP_ONCE
    {
        Status = Mm::ProtectVirtualMemory(Address, 1, PAGE_EXECUTE_READWRITE, &Protect);
        FAIL_CONTINUE(Status);

        Status = CopyOneOpCode(Record->Instruction, Address, &TargetOpLength, &SourceOpLength, 0, 0);

        PBYTE Buffer = Record->Instruction + TargetOpLength;
        PVOID Target = PtrAdd(Address, SourceOpLength);

#if ML_X86

        //
        // push imm
        // ret
        //
        *Buffer++ = 0x68;
        *(PULONG)Buffer = (ULONG)Target;
        Buffer += sizeof(PVOID);
        *Buffer = 0xC3;

#elif ML_AMD64
        //
        // push imm.low
        // mov dword ptr [rsp + 4], imm.high
        // ret
        //
        *Buffer++ = 0x68;
        *(PULONG)Buffer = (ULONG)((ULONG_PTR)Target >> 32);
        Buffer += sizeof(PVOID);

        *Buffer++ = 0xC7;
        *Buffer++ = 0x04;
        *Buffer++ = 0x24;
        *(PULONG)Buffer = (ULONG)Target;

        *Buffer = 0xC3;

#else

        #error

#endif

        *(PBYTE)Address = this->BreakOpCode;

        Status = Mm::ProtectVirtualMemory(Address, 1, Protect, &Protect);

        return Record;
    }

    Record->~HOOK_RECORD();
    Free(Record);

    return nullptr;
}

NTSTATUS PyHooker::DestroyHookRecord(PHOOK_RECORD Record)
{
    NTSTATUS    Status;
    ULONG       Protect;

    Status = Mm::ProtectVirtualMemory(Record->Address, 1, PAGE_EXECUTE_READWRITE, &Protect);
    FAIL_RETURN(Status);

    *(PBYTE)Record->Address = Record->Instruction[0];

    Mm::ProtectVirtualMemory(Record->Address, 1, Protect, &Protect);

    Record->Release();

    return STATUS_SUCCESS;
}
