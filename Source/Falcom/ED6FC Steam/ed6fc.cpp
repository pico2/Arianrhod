#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text /MERGE:.text1=.text /SECTION:.idata,ERW")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")
#pragma comment(lib, "freetype.lib")

#include "ml.cpp"
#include <ft2build.h>
#include <freetype.h>
#include <ftglyph.h>
#include <ftimage.h>
#include <ftbitmap.h>
#include <ftsynth.h>

#define FT_INT(_int, _float) ((_int << 6) | (_float))

ML_OVERLOAD_NEW

using ml::String;
using ml::GrowableArray;

FT_Library  FTLibrary;
FT_Face     Face;
ULONG       SleepFix;
PVOID       FontRender;

USHORT FontColorTable[] =
{
    0x0fff, 0x0fc7, 0x0f52, 0x08cf, 0x0fb4, 0x08fa, 0x0888, 0x0fee, 0x0853, 0x0333,
    0x0ca8, 0x0fdb, 0x0ace, 0x0cff, 0x056b, 0x0632, 0x0135, 0x0357, 0x0bbb,
};

BYTE FontSizeTable[] =
{
    0x08, 0x0c, 0x10, 0x14,
    0x18, 0x20, 0x12, 0x1a,
    0x1e, 0x24, 0x28, 0x2c,
    0x30, 0x32, 0x36, 0x3c,
    0x40, 0x48, 0x50, 0x60,
};

BYTE FontLumaTable[] =
{
    0x00, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01,
    0x01, 0x01, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02,
    0x02, 0x02, 0x02, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03,
    0x03, 0x03, 0x03, 0x03, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04,
    0x04, 0x04, 0x04, 0x04, 0x04, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05,
    0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06,
    0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07,
    0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08,
    0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x09, 0x09, 0x09, 0x09, 0x09, 0x09, 0x09,
    0x09, 0x09, 0x09, 0x09, 0x09, 0x09, 0x09, 0x09, 0x09, 0x09, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A,
    0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B,
    0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0C, 0x0C, 0x0C, 0x0C,
    0x0C, 0x0C, 0x0C, 0x0C, 0x0C, 0x0C, 0x0C, 0x0C, 0x0C, 0x0C, 0x0C, 0x0C, 0x0C, 0x0D, 0x0D, 0x0D,
    0x0D, 0x0D, 0x0D, 0x0D, 0x0D, 0x0D, 0x0D, 0x0D, 0x0D, 0x0D, 0x0D, 0x0D, 0x0D, 0x0D, 0x0E, 0x0E,
    0x0E, 0x0E, 0x0E, 0x0E, 0x0E, 0x0E, 0x0E, 0x0E, 0x0E, 0x0E, 0x0E, 0x0E, 0x0E, 0x0E, 0x0E, 0x0F,
    0x0F, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F,
};

NTSTATUS GetGlyphBitmap(LONG_PTR FontSize, WCHAR Chr, PVOID& Buffer, ULONG ColorIndex, ULONG Stride)
{
    PBYTE           Outline, Source;
    ULONG_PTR       Color;
    FT_Glyph        glyph;
    FT_BitmapGlyph  bitmap;

    ULONG strenth = FT_INT(1, 0);

    Color = FontColorTable[ColorIndex];

    FT_Load_Glyph(Face, FT_Get_Char_Index(Face, Chr), FT_LOAD_DEFAULT | FT_LOAD_NO_BITMAP | FT_LOAD_FORCE_AUTOHINT | FT_LOAD_RENDER);
    //FT_Bitmap_Embolden(FTLibrary, &Face->glyph->bitmap, 0, strenth);
    FT_Render_Glyph(Face->glyph, FT_RENDER_MODE_NORMAL);
    FT_Get_Glyph(Face->glyph, &glyph);
    FT_Glyph_To_Bitmap(&glyph, FT_RENDER_MODE_NORMAL, nullptr, TRUE);

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

    FT_Done_Glyph(glyph);

    return STATUS_SUCCESS;

    //return Source != nullptr ? STATUS_SUCCESS : STATUS_UNSUCCESSFUL;
}

NAKED VOID CDECL InvokeOriginalGetGlyphsBitmap(PCSTR Text, PVOID Buffer, ULONG ColorIndex, ULONG Stride, PVOID OriginalRoutine)
{
    INLINE_ASM
    {
        mov     eax, [esp + 0Ch];   // ColorIndex
        mov     ecx, [esp + 10h];   // Stride
        push    [esp + 08h];        // Buffer
        push    [esp + 08h];        // Text;
        call    [esp + 1Ch];
        ret;
    }
}

NTSTATUS GetGlyphsBitmap(PVOID Render, PCSTR Text, PVOID Buffer, ULONG ColorIndex, ULONG Stride, PVOID OriginalRoutine)
{
    LONG_PTR FontSize = FontSizeTable[*(PULONG_PTR)PtrAdd(Render, 0x24)];
    ULONG_PTR Encoding = CP_GB2312;

    SleepFix = 1;

    FT_Set_Pixel_Sizes(Face, FontSize, FontSize);

    for (auto &chr : String::Decode(Text, StrLengthA(Text), Encoding))
    {
        if (NT_FAILED(GetGlyphBitmap(FontSize, chr, Buffer, ColorIndex, Stride)))
        {
            WCHAR wcs[] = { chr, 0 };
            auto mbcs = String(wcs).Encode(Encoding);
            InvokeOriginalGetGlyphsBitmap((PCSTR)mbcs.GetData(), Buffer, ColorIndex, Stride, OriginalRoutine);
            Buffer = PtrAdd(Buffer, FontSize * 2);
        }
    }

    return 0;
}

VOID MP_CALL NakedGetGlyphBitmap(Mp::PTRAMPOLINE_NAKED_CONTEXT Context)
{
    ULONG ColorIndex, Stride;
    PVOID Render, Buffer, Original;
    PCSTR Text;

    ColorIndex  = (ULONG)Context->Rax;
    Stride      = (ULONG)Context->Rcx;
    Text        = (PCSTR)Context->GetArgument(1);
    Buffer      = (PVOID)Context->GetArgument(2);
    Original    = (PVOID)Context->ReturnAddress;
    Render      = FontRender;

    if (NT_SUCCESS(GetGlyphsBitmap(Render, Text, Buffer, ColorIndex, Stride, Original)))
    {
        Context->SetArgument(2, Context->GetArgument(0));
        Context->Rsp += sizeof(PVOID) * 3;
    }
}

/************************************************************************
  init
************************************************************************/

PVOID FindGetGlyphsBitmap(PVOID BaseAddress)
{
    PVOID p;

     p = SearchPatternSafe(L"81 3D ?? ?? ?? ?? BC 02 00 00", BaseAddress, ImageNtHeaders(BaseAddress)->OptionalHeader.SizeOfImage);
     if (p == nullptr)
         return IMAGE_INVALID_VA;

     FontRender = PtrSub(*(PVOID *)PtrAdd(p, 2), 0x28);

     p = ReverseSearchFunctionHeader(p, 0x60);
     return p == nullptr ? IMAGE_INVALID_VA : p;
}

template<typename... ARGS>
PVOID FindAndAdvance(ULONG_PTR Advance, ARGS... args)
{
    PVOID p = SearchPatternSafe(args...);
    return p == nullptr ? IMAGE_INVALID_VA : PtrAdd(p, Advance);
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

    Success = FALSE;
    FaceBuffer = nullptr;

    LOOP_ONCE
    {
        NtFileMemory file;

        if (FT_Init_FreeType(&FTLibrary) != FT_Err_Ok)
            break;

        if (NT_FAILED(file.Open(L"user.ttf")))
            break;

        FaceBuffer = AllocateMemoryP(file.GetSize32());
        if (FaceBuffer == nullptr)
            break;

        CopyMemory(FaceBuffer, file.GetBuffer(), file.GetSize32());

        if (FT_New_Memory_Face(FTLibrary, (PBYTE)FaceBuffer, file.GetSize32(), 0, &Face) != FT_Err_Ok)
            break;

        FT_Select_Charmap(Face, FT_ENCODING_GB2312);

        Success = TRUE;
    }

    if (Success == FALSE)
    {
        FreeMemoryP(FaceBuffer);
        // return TRUE;
    }

    SizeOfImage = ImageNtHeaders(BaseAddress)->OptionalHeader.SizeOfImage;

    using namespace Mp;

    PATCH_MEMORY_DATA p[] =
    {
        MemoryPatchVa((ULONG64)0x00, 1, FindAndAdvance(0xA, L"3C 80 73 03 32 C0 C3 3C A0 73 03", BaseAddress, SizeOfImage)),
        MemoryPatchVa((ULONG64)0x00, 1, FindAndAdvance(0xA, L"3C 80 73 03 33 C0 C3 3C A0 73 06", BaseAddress, SizeOfImage)),

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

        FunctionJumpVa(Success ? FindGetGlyphsBitmap(BaseAddress) : IMAGE_INVALID_VA, NakedGetGlyphBitmap, nullptr, NakedTrampoline),
    };

    PatchMemory(p, countof(p), BaseAddress);

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
