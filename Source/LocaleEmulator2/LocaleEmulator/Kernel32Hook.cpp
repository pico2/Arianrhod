#include "stdafx.h"

NTSTATUS LeGlobalData::HackUserDefaultLCID(PVOID Kernel32)
{
    LCID        Lcid;
    PVOID       gNlsProcessLocalCache;
    PLDR_MODULE Kernel;
    API_POINTER(GetUserDefaultLCID) GetUserDefaultLCID;

    *(PVOID *)&GetUserDefaultLCID = EATLookupRoutineByHashPNoFix(Kernel32, KERNEL32_GetUserDefaultLCID);
    Lcid = GetUserDefaultLCID();

    Kernel = FindLdrModuleByName(&USTR(L"KERNELBASE.dll"));
    if (Kernel == nullptr)
        Kernel = FindLdrModuleByHandle(Kernel32);

    gNlsProcessLocalCache = nullptr;

    WalkRelocTableT(Kernel->DllBase,
        WalkRelocCallbackM(ImageBase, RelocationEntry, Offset, Context)
        {
            SEH_TRY
            {
                PULONG_PTR Memory = *(PULONG_PTR *)PtrAdd(ImageBase, RelocationEntry->VirtualAddress + Offset->Offset);
                if (*(PLCID)Memory[2] == Lcid)
                {
                    gNlsProcessLocalCache = Memory;
                    return STATUS_UNSUCCESSFUL;
                }
            }
            SEH_EXCEPT(EXCEPTION_EXECUTE_HANDLER)
            {
            }
            return STATUS_SUCCESS;
        }
    );

    if (gNlsProcessLocalCache != nullptr)
        *(PLCID)(((PULONG_PTR)gNlsProcessLocalCache)[2]) = GetLeb()->LocaleID;

    return STATUS_SUCCESS;
}

NTSTATUS LeGlobalData::HookKernel32Routines(PVOID Kernel32)
{
    PVOID GetCurrentNlsCache;

    WriteLog(L"hook k32");

    this->SetUnhandledExceptionFilter();

    return this->HackUserDefaultLCID(Kernel32);

    //GetCurrentNlsCache = FindGetCurrentNlsCache(Kernel32);
    //if (GetCurrentNlsCache == nullptr)
    //    return STATUS_NOT_FOUND;

    //MEMORY_FUNCTION_PATCH f[] =
    //{
    //    LE_INLINE_JUMP(GetCurrentNlsCache),
    //};

    //return Nt_PatchMemory(nullptr, 0, f, countof(f));
}

NTSTATUS LeGlobalData::UnHookKernel32Routines()
{
    return 0;
}
