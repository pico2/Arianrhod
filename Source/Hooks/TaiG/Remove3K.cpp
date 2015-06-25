#include "TaiG2.h"
#include <DbgHelp.h>

VOID (FASTCALL *StubPushDebList)(PVOID vec, PVOID, PVOID v1, PVOID v2, DEB_ENTRY*& Entry);
LONG (CDECL *StubFormatCheckboxXml)(PVOID str, PWSTR format, ULONG index);

VOID FASTCALL PushDebList(PVOID vec, PVOID, PVOID v1, PVOID v2, DEB_ENTRY*& Entry)
{
    if (StrCompareA(Entry->FileName.GetBuffer(), "Cydia") != 0)
    {
        //Entry->Selectable    = FALSE;
        Entry->SelectPrompt  = FALSE;
        Entry->Selected      = FALSE;
    }

    return StubPushDebList(vec, 0, v1, v2, Entry);
}

LONG CDECL FormatCheckboxXml(PVOID str, PWSTR format, ULONG index)
{
    if (index != 0)
    {
        return StubFormatCheckboxXml(str, ml::String(format).Replace(LR"(selected="true")", LR"(selected="false" enabled="false")"), index);
    }

    return StubFormatCheckboxXml(str, format, index);
}

NTSTATUS Remove3K_Initialize(PVOID TaiGBase)
{
    using namespace Mp;

    {
        PATCH_MEMORY_DATA p[] =
        {
            MemoryPatchRva(0x00ull, 1, 0x9301),     // DebEntry->Selected = FALSE

            //FunctionCallRva(0x09357, PushDebList, &StubPushDebList),
        };

        PatchMemory(p, countof(p), TaiGBase);
    }

    {
        PATCH_MEMORY_DATA p[] =
        {
            MemoryPatchRva(0x80, 1, 0x18D9B),       // jo
            //FunctionCallRva(0x18BBC, FormatCheckboxXml, &StubFormatCheckboxXml),
        };

        PatchMemory(p, countof(p), GetExeModuleHandle());
    }

    return STATUS_SUCCESS;
}
