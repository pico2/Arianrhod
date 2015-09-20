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
        MemoryPatchRva(0ull, 1, 0x6616B1),
        MemoryPatchRva(0ull, 1, 0x6616D5),
        //MemoryPatchRva(0ull, 1, 0x661781),
        //MemoryPatchRva(0ull, 1, 0x6618B7),

        // SetCooperativeLevel flags
        // enable win key
        MemoryPatchRva(DISCL_NONEXCLUSIVE | DISCL_FOREGROUND, 1, 0x66A6ED),
    };

    return PatchMemory(p, countof(p), this->TESVBase);
}
