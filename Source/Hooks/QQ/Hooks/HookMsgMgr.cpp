#include "Hooks.h"

NTSTATUS NTAPI MsgMgr_RevokeMessageAgent(PVOID, PVOID, PVOID, PVOID)
{
    return STATUS_SUCCESS;
}

PVOID SearchMsgMgr_RemoveRevokedMsg(PVOID ImageBase)
{
    static WCHAR String[] = L"Failed to BatchGetRecordByTime, time[%lu], rand[%lu].";

    return SearchStringAndReverseSearchHeader(ImageBase, String, sizeof(String) - sizeof(String[0]), 0x1C0);
}

NTSTATUS HookMsgMgr(PVOID BaseAddress)
{
    Mp::PATCH_MEMORY_DATA Function_MsgMgr[] =
    {
        Mp::FunctionJumpVa(SearchMsgMgr_RemoveRevokedMsg(BaseAddress), MsgMgr_RevokeMessageAgent),
    };

    return Mp::PatchMemory(Function_MsgMgr, countof(Function_MsgMgr), BaseAddress);
}
