#include "Hooks.h"

VOID CDECL ReportScanResult()
{
    ODS(L"%S", __FUNCTION__);
    DebugBreakPoint();
    //return TRUE;
}

BOOL CDECL PluginSecurityCheck()
{
    ODS(L"%S", __FUNCTION__);
    return TRUE;
}

NTSTATUS CDECL CheckPluginList()
{
    ODS(L"%S", __FUNCTION__);
    return STATUS_SUCCESS;
}

PVOID SearchAppUtil_CheckImportantModule(PVOID ImageBase)
{
    static WCHAR String[] = L"PerfStand.CheckImportantModule.Begin";

    return SearchStringAndReverseSearchHeader(ImageBase, String, sizeof(String), 0x30);
}

NTSTATUS HookAppUtil(PVOID BaseAddress)
{

    /************************************************************************
      AppUtil

        L"PerfStand.CheckImportantModule.Begin"
        L"DllCheck"
        L"Dll Check Fail"

        check:
            QQExternal.exe
            TXPlatform.exe
            ...
    ************************************************************************/

    AppUtilBase = BaseAddress;

    Mp::PATCH_MEMORY_DATA Function_AppUtil[] =
    {
        Mp::FunctionJumpVa(LookupExportTable(BaseAddress, "?ReportScanResult@Misc@Util@@YAHKVCTXStringW@@0@Z"), ReportScanResult),
        Mp::FunctionJumpVa(LookupExportTable(BaseAddress, "?PluginSecurityCheck@Misc@Util@@YAHXZ"),             PluginSecurityCheck),
        Mp::FunctionJumpVa(SearchAppUtil_CheckImportantModule(BaseAddress),                                     CheckPluginList),
    };

    return Mp::PatchMemory(Function_AppUtil, countof(Function_AppUtil), BaseAddress);
}
