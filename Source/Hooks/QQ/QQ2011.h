#ifndef _QQ2011_H_
#define _QQ2011_H_

#include "ml.h"
#include "QQMethod.h"

#define ODS(...) OutputDebugStringW(ml::String::Format(L"[QQ] " __VA_ARGS__))

using ml::String;

typedef struct
{
    PCWSTR                  DllName;
    Mp::PPATCH_MEMORY_DATA  PatchData;
    ULONG_PTR               PatchCount;

} PATCH_ARRAY, *PPATCH_ARRAY;

#define CALL 0xE8
#define JUMP 0xE9
#define PUSH 0x68


extern PVOID AppUtilBase;
extern TXReloginMgr* ReloginMgr;

PVOID
SearchStringAndReverseSearchHeader(
    PVOID       ImageBase,
    PVOID       BytesSequence,
    ULONG_PTR   SizeInBytes,
    ULONG_PTR   SearchRange
);

// contracts.dll 61948343 age

#endif /* _QQ2011_H_ */