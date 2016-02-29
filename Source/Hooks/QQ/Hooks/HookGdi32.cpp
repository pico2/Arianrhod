#include "Hooks.h"

using namespace Mp;

API_POINTER(GetDeviceCaps)  StubGetDeviceCaps;

LONG NTAPI QqGetDeviceCaps(HDC hdc, LONG index)
{
    switch (index)
    {
        case LOGPIXELSY:
        case LOGPIXELSX:
            return 96;
    }

    return StubGetDeviceCaps(hdc, index);
}

NTSTATUS HookGdi32(PVOID BaseAddress)
{
    PATCH_MEMORY_DATA Function_gdi32[] =
    {
        FunctionJumpVa(LookupExportTable(BaseAddress, GDI32_GetDeviceCaps), QqGetDeviceCaps, &StubGetDeviceCaps),
    };

    return PatchMemory(Function_gdi32, countof(Function_gdi32), BaseAddress);
}
