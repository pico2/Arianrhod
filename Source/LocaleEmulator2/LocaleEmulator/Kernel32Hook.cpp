#include "stdafx.h"

PVOID LeGetCurrentNlsCache()
{
    PULONG          CurrentNlsNode;
    PULONG_PTR      NlsCache;
    PLeGlobalData   GlobalData = LeGetGlobalData();

    NlsCache = (PULONG_PTR)GlobalData->GetCurrentNlsCache();

    CurrentNlsNode = (PULONG)NlsCache[2];
    if (CurrentNlsNode == NULL)
        return NlsCache;

    *CurrentNlsNode = GlobalData->GetLeb()->LocaleID;

    return NlsCache;
}

PVOID FindGetCurrentNlsCache(PVOID Kernel32)
{
    PVOID KernelBase, GetUserDefaultLCID, GetCurrentNlsCache;

    KernelBase = FindLdrModuleByName(&USTR(L"KERNELBASE.dll"))->DllBase;

    GetUserDefaultLCID = EATLookupRoutineByHashPNoFix(KernelBase, KERNEL32_GetUserDefaultLCID);
    if (GetUserDefaultLCID == NULL)
        return NULL;

    GetCurrentNlsCache = NULL;

    WalkOpCodeT(GetUserDefaultLCID, 0x30,
        WalkOpCodeM(Buffer, OpLength, Ret)
        {
            switch (Buffer[0])
            {
                case CALL:
                    GetCurrentNlsCache = GetCallDestination(Buffer);
                    return STATUS_SUCCESS;
            }

            return STATUS_NOT_FOUND;
        }
    );

    return GetCurrentNlsCache;
}

NTSTATUS LeGlobalData::HookKernel32Routines(PVOID Kernel32)
{
    PVOID GetCurrentNlsCache;

    WriteLog(L"hook k32");

    GetCurrentNlsCache = FindGetCurrentNlsCache(Kernel32);
    if (GetCurrentNlsCache == NULL)
        return STATUS_NOT_FOUND;

    MEMORY_FUNCTION_PATCH f[] =
    {
        LE_INLINE_JUMP(GetCurrentNlsCache),
    };

    return Nt_PatchMemory(NULL, 0, f, countof(f));
}

NTSTATUS LeGlobalData::UnHookKernel32Routines()
{
    return 0;
}
