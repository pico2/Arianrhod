#include "PyHooker.h"
#include "HandleTable.cpp"

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
                    if (Entry->Handle != nullptr)
                    {
                        ((PyHooker *)Context)->PyUnHookFunction(((PHOOK_RECORD)(Entry->Handle))->Address);
                        //((PHOOK_RECORD)(Entry->Handle))->~HOOK_RECORD();
                        //((PyHooker *)Context)->Free(Entry->Handle);
                        //Entry->Handle = nullptr;
                    }
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

    this->python.Register(
        [=](PVOID Address, PyObject* Callable)
        {
            return this->PyHookFunction(Address, Callable);
        },
        L"Hook"
    )
    .Register(
        [=](PVOID Address)
        {
            return this->PyUnHookFunction(Address);
        },
        L"UnHook"
    )
    .AddToModule(L"pyhooker");

    return STATUS_SUCCESS;
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

LONG NTAPI PyHooker::StaticExceptionHandler(PEXCEPTION_POINTERS ExceptionPointers)
{
    return PyHooker::instance->ExceptionHandler(ExceptionPointers);
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

    PML_HANDLE_TABLE_ENTRY  Entry;
    PHOOK_RECORD            Record;
    PCONTEXT                Context;
    PEXCEPTION_RECORD       ExceptionRecord;

    Context         = ExceptionPointers->ContextRecord;
    ExceptionRecord = ExceptionPointers->ExceptionRecord;

    PROTECT_SECTION(&this->Lock)
    {
        if (IsBreakPoint(ExceptionRecord->ExceptionAddress) == FALSE)
            return EXCEPTION_CONTINUE_SEARCH;

        LOOP_ONCE
        {
            Entry = this->RecordTable.Lookup(ExceptionRecord->ExceptionAddress);
            if (Entry == nullptr || Entry->Handle == nullptr)
                continue;

            Record = (PHOOK_RECORD)Entry->Handle;
            if (Record == nullptr)
                break;

            Record->AddRef();
            Context->Eip = (ULONG_PTR)Record->Instruction;

            return EXCEPTION_CONTINUE_EXECUTION;
        }

        if (IsBreakPoint(ExceptionRecord->ExceptionAddress) == FALSE)
            return EXCEPTION_CONTINUE_EXECUTION;
    }

    return EXCEPTION_CONTINUE_SEARCH;
}

NTSTATUS PyHooker::PyHookFunction(PVOID Address, PyObject* Callable)
{
    PHOOK_RECORD Record;

    //if (PyCallable_Check(Callable) == FALSE)
    //    return STATUS_OBJECT_TYPE_MISMATCH;

    PROTECT_SECTION(&this->Lock)
    {
        if (this->RecordTable.Lookup(Address) != nullptr)
            return STATUS_ADDRESS_ALREADY_EXISTS;

        Record = this->CreateHookRecord(Address, Callable);
        if (Record == nullptr)
            return STATUS_NO_MEMORY;

        this->RecordTable.Insert(Address)->Handle = Record;
    }

    return STATUS_SUCCESS;
}

NTSTATUS PyHooker::PyUnHookFunction(PVOID Address)
{
    PROTECT_SECTION(&this->Lock)
    {
        PML_HANDLE_TABLE_ENTRY  Entry;
        PHOOK_RECORD            Record;

        Entry = this->RecordTable.Lookup(Address);
        if (Entry == nullptr || Entry->Handle == nullptr)
            return STATUS_ADDRESS_NOT_ASSOCIATED;

        Record = (PHOOK_RECORD)Entry->Handle;
        if (Record == nullptr)
            break;

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

    if (Record == nullptr)
        return STATUS_SUCCESS;

    Status = Mm::ProtectVirtualMemory(Record->Address, 1, PAGE_EXECUTE_READWRITE, &Protect);
    FAIL_RETURN(Status);

    *(PBYTE)Record->Address = Record->Instruction[0];

    Mm::ProtectVirtualMemory(Record->Address, 1, Protect, &Protect);

    Record->~HOOK_RECORD();
    Free(Record);

    return STATUS_SUCCESS;
}
