#include "Hooks.h"

NTSTATUS NTAPI IM_RevokeMessageAgent(PVOID, PVOID, PVOID, PVOID)
{
    return STATUS_SUCCESS;
}

PVOID SearchIM_RemoveRevokedMsg(PVOID ImageBase)
{
    static CHAR String[] = "tencent.im.msgrevoke.UinTypeUserDef";

    PLDR_MODULE Module;
    PVOID Found;

    SEARCH_PATTERN_DATA Str[] =
    {
        ADD_PATTERN_(String, sizeof(String)),
    };

    Module = FindLdrModuleByHandle(ImageBase);

    Found = SearchPattern(Str, countof(Str), Module->DllBase, Module->SizeOfImage);

    return Found == nullptr ? IMAGE_INVALID_VA : Found;
}

PVOID SearchIM_RemoveRevokedGroupMsg(PVOID ImageBase)
{
    static CHAR String[] = "tencent.im.msgrevoke.MsgInfoUserDef";

    PLDR_MODULE Module;
    PVOID Found;

    SEARCH_PATTERN_DATA Str[] =
    {
        ADD_PATTERN_(String, sizeof(String)),
    };

    Module = FindLdrModuleByHandle(ImageBase);

    Found = SearchPattern(Str, countof(Str), Module->DllBase, Module->SizeOfImage);

    return Found == nullptr ? IMAGE_INVALID_VA : Found;
}

NTSTATUS HookIM(PVOID BaseAddress)
{
    Mp::PATCH_MEMORY_DATA Function_IM[] =
    {
        Mp::MemoryPatchVa(0ull, 1, SearchIM_RemoveRevokedMsg(BaseAddress)),
        Mp::MemoryPatchVa(0ull, 1, SearchIM_RemoveRevokedGroupMsg(BaseAddress)),
    };

    return Mp::PatchMemory(Function_IM, countof(Function_IM), BaseAddress);
}
