#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text /MERGE:.text1=.text /SECTION:.idata,ERW")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")

#include "ml.cpp"
#include "DWriteRender.h"

#pragma comment(lib, "dwrite.lib")
#pragma comment(lib, "d2d1.lib")

ML_OVERLOAD_NEW

using ml::String;
using ml::GrowableArray;

ULONG       SleepFix;
PVOID       GameFontRender;

BYTE FontSizeTable[] =
{
    0x08, 0x0c, 0x10, 0x14,
    0x18, 0x20, 0x12, 0x1a,
    0x1e, 0x24, 0x28, 0x2c,
    0x30, 0x32, 0x36, 0x3c,
    0x40, 0x48, 0x50, 0x60,
    0x80, 0x90, 0xa0, 0xc0,
};

USHORT FontColorTable[] =
{
    0x0fff, 0x0fc7, 0x0f52, 0x08cf, 0x0fb4, 0x08fa, 0x0888, 0x0fee, 0x0853, 0x0333,
    0x0ca8, 0x0fdb, 0x0ace, 0x0cff, 0x056b, 0x0632, 0x0135, 0x0357, 0x0bbb,
};

DWriteRender *DWriteRenders[countof(FontSizeTable)];

NTSTATUS GetGlyphBitmap(LONG_PTR FontSize, WCHAR Chr, PVOID& Buffer, ULONG ColorIndex, ULONG Stride)
{
    PBYTE           Outline, Source;
    ULONG_PTR       Color;

#if 0

    Color = FontColorTable[ColorIndex];

    bitmap = (FT_BitmapGlyph)glyph;
    Source = (PBYTE)bitmap->bitmap.buffer;

    if (Source != nullptr)
    {
        BYTE LocalOutline[0x2000];
        ZeroMemory(LocalOutline, FontSize * FontSize);

        Outline = LocalOutline + bitmap->left + (FontSize - ML_MIN(FontSize, bitmap->top + 3)) * FontSize;

        for (ULONG_PTR Height = bitmap->bitmap.rows; Height; --Height)
        {
            PBYTE out = Outline;

            for (ULONG_PTR Width = bitmap->bitmap.width; Width; --Width)
            {
                *out++ = FontLumaTable[*Source++];
            }

            Outline += FontSize;
        }

        PBYTE Surface = (PBYTE)Buffer;

        Source = LocalOutline;

        for (ULONG_PTR Height = FontSize; Height; --Height)
        {
            PUSHORT out = (PUSHORT)Surface;

            for (ULONG_PTR Width = FontSize; Width; --Width)
            {
                *out++ = *Source != 0 ? ((*Source << 0xC) | Color) : 0;
                ++Source;
            }

            Surface += Stride;
        }

        //Buffer = PtrAdd(Buffer, (bitmap->left + bitmap->bitmap.pitch + bitmap->left) * sizeof(USHORT));
        Buffer = PtrAdd(Buffer, (Chr >= 0x80 ? FontSize : FontSize / 2) * sizeof(USHORT));
    }
    else
    {
        //Buffer = PtrAdd(Buffer, Face->glyph->metrics.horiAdvance * 2);
        Buffer = PtrAdd(Buffer, Chr == ' ' ? FontSize : FontSize * 2);
    }

#endif

    return STATUS_SUCCESS;
}

VOID (NTAPI *StubGetGlyphsBitmap2)(PCSTR Text, PVOID Buffer, ULONG ColorIndex, ULONG Stride);

VOID NTAPI GetGlyphsBitmap2(PCSTR Text, PVOID Buffer, ULONG Stride, ULONG ColorIndex)
{
    DWriteRender*   DWRender;
    ULONG_PTR       FontSize, FontIndex, Color;

//    return StubGetGlyphsBitmap2(Text, Buffer, Stride, ColorIndex);

    FontIndex = *(PULONG_PTR)PtrAdd(GameFontRender, 0x24);
    FontSize = FontSizeTable[FontIndex];
    DWRender = DWriteRenders[FontIndex];
    Color = FontColorTable[ColorIndex];

    for (auto &chr : String::Decode(Text, StrLengthA(Text), CP_SHIFTJIS))
    {
        if (NT_FAILED(DWRender->DrawRune(chr, Color, Buffer, Stride)))
        {
            ;
        }

        //Buffer = PtrAdd(Buffer, Stride * FontSize);
    }

    //StubGetGlyphsBitmap2(Text, Buffer, ColorIndex, Stride);
}

NTSTATUS GetGlyphsBitmap(PVOID Render, PCSTR Text, PVOID Buffer, ULONG ColorIndex, ULONG Stride, PVOID OriginalRoutine)
{
    LONG_PTR FontSize = FontSizeTable[*(PULONG_PTR)PtrAdd(Render, 0x24)];
    ULONG_PTR Encoding = CP_GB2312;

    SleepFix = 1;

    // FT_Set_Pixel_Sizes(Face, FontSize, FontSize);

    for (auto &chr : String::Decode(Text, StrLengthA(Text), Encoding))
    {
        if (NT_FAILED(GetGlyphBitmap(FontSize, chr, Buffer, ColorIndex, Stride)))
        {
            WCHAR wcs[] = { chr, 0 };
            auto mbcs = String(wcs).Encode(Encoding);
            Buffer = PtrAdd(Buffer, FontSize * 2);
        }
    }

    return 0;
}

/************************************************************************
  init
************************************************************************/

PVOID FindFontRender(PVOID BaseAddress)
{
    PVOID p;

     p = SearchPatternSafe(L"81 3D ?? ?? ?? ?? BC 02 00 00", BaseAddress, ImageNtHeaders(BaseAddress)->OptionalHeader.SizeOfImage);
     if (p == nullptr)
         return IMAGE_INVALID_VA;

     GameFontRender = PtrSub(*(PVOID *)PtrAdd(p, 2), 0x28);

     return GameFontRender;
}

template<typename... ARGS>
PVOID FindAndAdvance(ULONG_PTR Advance, ARGS... args)
{
    PVOID p = SearchPatternSafe(args...);
    return p == nullptr ? IMAGE_INVALID_VA : PtrAdd(p, Advance);
}

NTSTATUS InitializeDWrite()
{
    NTSTATUS hr;
    ID2D1Factory*       factory;
    IDWriteFactory*     dwrite;
    IDWriteGdiInterop*  gdiInterop;

    factory = nullptr;
    dwrite = nullptr;

    hr = S_OK;

    LOOP_ONCE
    {
        PBYTE           fontSize;
        DWriteRender**  render = DWriteRenders;

        FOR_EACH_ARRAY(fontSize, FontSizeTable)
        {
            *render = new DWriteRender();
            if (*render == nullptr)
            {
                hr = STATUS_NO_MEMORY;
                break;
            }

            hr = (*render)->Initialize(L"Microsoft YaHei UI", *fontSize);
            FAIL_BREAK(hr);
            ++render;
        }
    }

    SafeReleaseT(factory);
    SafeReleaseT(dwrite);

    return hr;
}

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    BOOL        Success;
    ULONG_PTR   SizeOfImage;
    PVOID       FaceBuffer;

    LdrDisableThreadCalloutsForDll(BaseAddress);
    ml::MlInitialize();
    InitializeDWrite();

    BaseAddress = GetExeModuleHandle();

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

    Rtl::SetExeDirectoryAsCurrent();

    Success = FindFontRender(BaseAddress) != IMAGE_INVALID_VA;

    using namespace Mp;

    PATCH_MEMORY_DATA p[] =
    {
        MemoryPatchVa(
            (ULONG64)(API_POINTER(::Sleep))[] (ULONG ms) -> VOID
            {
                Ps::Sleep(ms == 0 ? SleepFix : ms);
            },
            sizeof(PVOID),
            LookupImportTable(GetExeModuleHandle(), nullptr, KERNEL32_Sleep)
        ),

        MemoryPatchVa(
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
            LookupImportTable(GetExeModuleHandle(), nullptr, USER32_SetWindowPos)
        ),

        FunctionJumpVa(Success ? (PVOID)0x4B7C30 : IMAGE_INVALID_VA, GetGlyphsBitmap2, &StubGetGlyphsBitmap2),
    };

    PatchMemory(p, countof(p), BaseAddress);

    //DWriteRenders[9]->DrawRune(L"ά"[0], FontColorTable[0], 0, 0), Ps::ExitProcess(0);

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
