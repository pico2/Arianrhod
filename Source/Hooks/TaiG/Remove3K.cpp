#include "TaiG2.h"

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

NAKED VOID SetDebEntry()
{
    INLINE_ASM
    {
        mov     byte ptr [esi+0xA02], 0x1;
        mov     eax, dword ptr [ebp-0xDC];
        cmp     eax, 1;
        or      eax, eax;
        je      IS_CYDIA;

        xor     eax, eax;
        mov     byte ptr [esi+0xA02], al;   // Selected

IS_CYDIA:
        ret;
    }
}

BOOL CDECL IsJailbroken2(HANDLE Device)
{
    RtlSetLastWin32Error(0xE8000022);
    return FALSE;
}

PVOID NTAPI TgLoadLibrary(PCSTR Library)
{
    PVOID base = LoadLibraryA(Library);
    using namespace Mp;

    {
        PATCH_MEMORY_DATA p[] =
        {
            FunctionJumpRva(0xF340, IsJailbroken2),
            MemoryPatchRva("com.saurik.Cybia", 16, 0x652FC),
        };

        PatchMemory(p, countof(p), base);
    }

    return base;
}

NTSTATUS Remove3K2_Initialize(PVOID TaiGBase)
{
    using namespace Mp;

    {
        PATCH_MEMORY_DATA p[] =
        {
            //MemoryPatchRva(0x00ull, 4, 0x15EB2),
            //FunctionCallRva(0x1533B, TgLoadLibrary),
            FunctionCallRva(0x15E71, SetDebEntry),
            MemoryPatchRva(0x80, 1, 0x1A423),       // jo
        };

        PatchMemory(p, countof(p), GetExeModuleHandle());
    }

    return STATUS_SUCCESS;
}

