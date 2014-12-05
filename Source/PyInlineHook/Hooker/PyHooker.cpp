#include "PyHooker.h"
#include "HandleTable.cpp"

PyHooker::PyHooker()
{

}

PyHooker::~PyHooker()
{

}

NTSTATUS PyHooker::InitPython()
{
    this->python.Initialize();
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

NTSTATUS PyHooker::Initialize()
{
    FAIL_RETURN(this->InitPython());
    FAIL_RETURN(this->InitDispatcher());
    FAIL_RETURN(this->InitRecordTable());

    return STATUS_SUCCESS;
}

LONG NTAPI PyHooker::StaticExceptionHandler(PEXCEPTION_POINTERS ExceptionPointers)
{
    return PyHooker::instance->ExceptionHandler(ExceptionPointers);
}

LONG PyHooker::ExceptionHandler(PEXCEPTION_POINTERS ExceptionPointers)
{
    return EXCEPTION_CONTINUE_SEARCH;
}
