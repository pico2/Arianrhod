#define DIRECTINPUT_VERSION 0x800

#include "Patcher.h"
#include <dinput.h>

using namespace Mp;

Patcher::Patcher()
{
    this->TESVBase = GetExeModuleHandle();
}

NTSTATUS Patcher::Initialize()
{
    FAIL_RETURN(this->window.Initialize(this->TESVBase));

    PATCH_MEMORY_DATA p[] =
    {
        // patch ShowCursor display count check
        MemoryPatchRva(0ull, 1, 0x661DF1),
        MemoryPatchRva(0ull, 1, 0x661E15),
        //MemoryPatchRva(0ull, 1, 0x661781),
        //MemoryPatchRva(0ull, 1, 0x6618B7),

        // CDIDev::SetCooperativeLevel flags
        // enable win key
        // 00A6B0AC    .  6A 15               push    0x15
        // 00A6B0AE    .  FF15 DCB20601       call    dword ptr [<&USER32.GetActiveWindow>]             ; [GetActiveWindow
        // 00A6B0B4    .  8B56 28             mov     edx, dword ptr [esi+0x28]
        // 00A6B0B7    .  50                  push    eax
        // 00A6B0B8    .  8B47 34             mov     eax, dword ptr [edi+0x34]
        // 00A6B0BB    .  52                  push    edx
        // 00A6B0BC    .  FFD0                call    eax                                               ;  dinput8.CDIDev_SetCooperativeLevel
        MemoryPatchRva(DISCL_NONEXCLUSIVE | DISCL_FOREGROUND, 1, 0x66B0AD),
    };

    return PatchMemory(p, countof(p), this->TESVBase);
}
