#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text /MERGE:.text1=.text /SECTION:.idata,ERW")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")
#pragma comment(lib, "freetype.lib")

#include "ml.cpp"
#include <ft2build.h>
#include <freetype.h>

using ml::String;
using ml::GrowableArray;

FT_Library FTLibrary;

PVOID SearchPatternSafe(PCSTR Pattern, PVOID Begin, LONG_PTR Length)
{
    GrowableArray<SEARCH_PATTERN_DATA> Patterns;

    for (String &p : String::Decode((PVOID)Pattern, StrLengthA(Pattern), CP_ACP).Split(L" "))
    {
        if (!p)
            continue;

        if (p.GetCount() != 2)
            return nullptr;

        if (p == L"??")
        {
            ;
        }
        else
        {
            ULONG Hex = p.ToHex();
        }

        PrintConsole(L"%s\n", p);
    }

    return SearchPatternSafe(Patterns.GetData(), Patterns.GetSize(), Begin, Length);
}

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    LdrDisableThreadCalloutsForDll(BaseAddress);
    ml::MlInitialize();

    AllocConsole();

    if (SearchPatternSafe("81  3D  ?? ??   ?? ?? BC 02 00 00", BaseAddress, 0x2000))
        DebugBreakPoint();

    //
    // 4A12E0
    // check ascii range
    //
    // 4A0DE0
    // check sjis range
    //
    // 4A1300
    // char outline
    //
    // FT_Load_Glyph
    // FT_Get_Glyph
    // FT_Render_Glyph
    // FT_Glyph_To_Bitmap
    //

    Mp::PATCH_MEMORY_DATA p[] =
    {
        Mp::MemoryPatchVa(
            (ULONG64)(API_POINTER(::Sleep))[] (ULONG ms) -> VOID
            {
                Ps::Sleep(ms == 0 ? 1 : ms);
            },
            sizeof(PVOID),
            LookupImportTable(GetExeModuleHandle(), "KERNEL32.dll", KERNEL32_Sleep)
        ),

        Mp::MemoryPatchVa(
            (ULONG64)(API_POINTER(SetWindowPos))[](HWND Wnd, HWND InsertAfter, int X, int Y, int cx, int cy, UINT Flags) -> BOOL
            {
                if (Flags == SWP_NOMOVE)
                {
                    RECT WorkArea;

                    SystemParametersInfoW(SPI_GETWORKAREA, 0, &WorkArea, 0);
                    X = ((WorkArea.right - WorkArea.left) - cx) / 2;
                    Y = ((WorkArea.bottom - WorkArea.top) - cy) / 2;

                    CLEAR_FLAG(Flags, SWP_NOMOVE);
                }

                return SetWindowPos(Wnd, InsertAfter, X, Y, cx, cy, Flags);
            },
            sizeof(PVOID),
            LookupImportTable(GetExeModuleHandle(), "USER32.dll", USER32_SetWindowPos)
        ),
    };

    Mp::PatchMemory(p, countof(p));

    FT_Init_FreeType(&FTLibrary);

    return TRUE;
}

BOOL WINAPI DllMain(PVOID BaseAddress, ULONG Reason, PVOID Reserved)
{
    switch (Reason)
    {
        case DLL_PROCESS_ATTACH:
            return Initialize(BaseAddress) || UnInitialize(BaseAddress);

        case DLL_PROCESS_DETACH:
            UnInitialize(BaseAddress);
            break;
    }

    return TRUE;
}
