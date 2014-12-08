#ifndef _PYHOOKER_H_a831a88f_9272_4882_a723_dfd24cbb9e76_
#define _PYHOOKER_H_a831a88f_9272_4882_a723_dfd24cbb9e76_

#include "ml.h"
#include "mlpython.h"
#include "HandleTable.h"
#include "SectionProtector.h"

using ml::String;
using ml::ByteArray;
using ml::StringArray;

#define PY_CALLBACK_IN_PROGRESS TAG4('PCIP')

typedef struct HOOK_RECORD
{
    ULONG_PTR   RefCount;
    PVOID       Address;
    PyObject*   Callback;

#if ML_X86

    BYTE Instruction[0x20];

#elif ML_AMD64

    BYTE Instruction[0x40];

#endif

    HOOK_RECORD()
    {
        ZeroMemory(this, sizeof(*this));
        this->RefCount = 1;
    }

    ULONG_PTR AddRef()
    {
        return _InterlockedIncrementPtr(&this->RefCount);
    }

    ULONG_PTR Release();

    ~HOOK_RECORD()
    {
        PyRelease(Callback);
    }

} HOOK_RECORD, *PHOOK_RECORD;

class PyHooker : public MemoryAllocator
{
protected:
    MlPython                python;
    PVOID                   VehHandle;
    MlHandleTable           RecordTable;
    RTL_CRITICAL_SECTION    Lock;

    static PyHooker *instance;
    static const ULONG_PTR BreakOpCode = 0xF4;  // hlt

    typedef struct
    {
        CONTEXT     Context;
        PyHooker*   hooker;

    } DISPATCHER_CONTEXT, *PDISPATCHER_CONTEXT;

protected:
    PyHooker();
    ~PyHooker();

public:
    NoInline static PyHooker* GetInstance()
    {
        if (instance != nullptr)
            return instance;

        instance = new PyHooker();
        return instance;
    }

    VOID Release()
    {
        delete this;
        instance = nullptr;
    }

public:
    NTSTATUS Initialize();
    NTSTATUS LoadPyFile();

    NTSTATUS PyHookFunction(PVOID Address, PyObject* Callable);
    NTSTATUS PyUnHookFunction(PVOID Address);

protected:
    NTSTATUS InitDispatcher();
    NTSTATUS InitPython();
    NTSTATUS InitRecordTable();

    PHOOK_RECORD LookupAndReferenceRecord(PVOID Address);

    static LONG NTAPI StaticExceptionHandler(PEXCEPTION_POINTERS ExceptionPointers);
    static VOID FASTCALL StaticPyDispatcher(PHOOK_RECORD Record, PDISPATCHER_CONTEXT Context);
    LONG ExceptionHandler(PEXCEPTION_POINTERS ExceptionPointers);
    VOID PyDispatcher(PHOOK_RECORD Record, PCONTEXT Context);

    /************************************************************************
      hook methods
    ************************************************************************/
    PHOOK_RECORD CreateHookRecord(PVOID Address, PyObject* Callable);
    NTSTATUS DestroyHookRecord(PHOOK_RECORD Record);
};

DECL_SELECTANY PyHooker* PyHooker::instance = nullptr;

ULONG_PTR HOOK_RECORD::Release()
{
    ULONG_PTR Ref = _InterlockedDecrementPtr(&this->RefCount);

    if (Ref == 0)
    {
        this->~HOOK_RECORD();
        PyHooker::GetInstance()->Free(this);
    }

    return Ref;
}

#endif // _PYHOOKER_H_a831a88f_9272_4882_a723_dfd24cbb9e76_
