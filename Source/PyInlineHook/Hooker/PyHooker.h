#ifndef _PYHOOKER_H_a831a88f_9272_4882_a723_dfd24cbb9e76_
#define _PYHOOKER_H_a831a88f_9272_4882_a723_dfd24cbb9e76_

#include "ml.h"
#include "mlpython.h"
#include "HandleTable.h"

using ml::String;
using ml::ByteArray;
using ml::StringArray;

typedef struct
{
    ULONG_PTR Address;

} HOOK_RECORD, *PHOOK_RECORD;

class PyHooker
{
protected:
    MlPython        python;
    PVOID           VehHandle;
    MlHandleTable   RecordTable;

    static PyHooker *instance;

protected:
    PyHooker();
    ~PyHooker();

public:
    static PyHooker* GetInstance()
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

protected:
    NTSTATUS InitDispatcher();
    NTSTATUS InitPython();
    NTSTATUS InitRecordTable();

    static LONG NTAPI StaticExceptionHandler(PEXCEPTION_POINTERS ExceptionPointers);
    LONG ExceptionHandler(PEXCEPTION_POINTERS ExceptionPointers);
};

DECL_SELECTANY PyHooker* PyHooker::instance = nullptr;

#endif // _PYHOOKER_H_a831a88f_9272_4882_a723_dfd24cbb9e76_
