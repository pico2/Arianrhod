#ifndef _QQ2011_H_
#define _QQ2011_H_

#include "MyLibrary.h"

typedef struct
{
    PCWSTR                  DllName;
    PMEMORY_PATCH           Patch;
    ULONG_PTR               PatchCount;
    PMEMORY_FUNCTION_PATCH  FunctionPatch;
    ULONG_PTR               FunctionCount;

} PATCH_ARRAY, *PPATCH_ARRAY;

// contracts.dll 61948343 age

#endif /* _QQ2011_H_ */