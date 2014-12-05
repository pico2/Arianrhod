#ifndef _PYHOOKER_H_a831a88f_9272_4882_a723_dfd24cbb9e76_
#define _PYHOOKER_H_a831a88f_9272_4882_a723_dfd24cbb9e76_

#include "ml.h"
#include "mlpython.h"

using ml::String;
using ml::ByteArray;
using ml::StringArray;

class PyHooker
{
protected:
    MlPython python;

public:
    PyHooker();
    ~PyHooker();

public:
    NTSTATUS Initialize();
};

#endif // _PYHOOKER_H_a831a88f_9272_4882_a723_dfd24cbb9e76_
