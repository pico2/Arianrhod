#include "PyHooker.h"

PyHooker::PyHooker()
{

}

PyHooker::~PyHooker()
{

}

NTSTATUS PyHooker::Initialize()
{
    this->python.Initialize(MlPython::IgnoreSetPath);

    return STATUS_SUCCESS;
}
