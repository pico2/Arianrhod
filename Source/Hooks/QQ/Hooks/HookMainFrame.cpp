#include "Hooks.h"

BOOL NTAPI PopupSecurityFrame(PVOID, PVOID)
{
    ODS(L"%S", __FUNCTION__);
    return TRUE;
}

PVOID SearchMainFrame_SecurityFrame(PVOID ImageBase)
{
    static WCHAR String[] = L"Misc\\SecurityFrame.xml|SecurityWnd";

    return SearchStringAndReverseSearchHeader(ImageBase, String, sizeof(String), 0xB0);
}

NTSTATUS HookMainFrame(PVOID BaseAddress)
{
    Mp::PATCH_MEMORY_DATA Function_MainFrame[] =
    {
        Mp::FunctionJumpVa(SearchMainFrame_SecurityFrame(BaseAddress),  PopupSecurityFrame),
    };

    return Mp::PatchMemory(Function_MainFrame, countof(Function_MainFrame), BaseAddress);
}