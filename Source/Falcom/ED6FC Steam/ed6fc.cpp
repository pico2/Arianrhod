// this file must be compiled under zh-CN locale

#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text /MERGE:.text1=.text /SECTION:.idata,ERW")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")

#include "ed6fc.h"
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

BYTE LetterWidthTable[] =
{
    0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10,
    0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10,
    0x0A, 0x06, 0x08, 0x0C, 0x0B, 0x0F, 0x0D, 0x05, 0x08, 0x07, 0x09, 0x0C, 0x06, 0x08, 0x06, 0x09,
    0x0B, 0x09, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x06, 0x06, 0x0B, 0x0C, 0x0B, 0x0A,
    0x10, 0x0D, 0x0C, 0x0D, 0x0D, 0x0C, 0x0B, 0x0D, 0x0D, 0x07, 0x09, 0x0D, 0x0B, 0x10, 0x0D, 0x0E,
    0x0C, 0x0E, 0x0C, 0x0B, 0x0C, 0x0D, 0x0D, 0x10, 0x0C, 0x0C, 0x0C, 0x08, 0x09, 0x07, 0x0B, 0x0C,
    0x07, 0x0A, 0x0B, 0x0A, 0x0B, 0x0A, 0x09, 0x0B, 0x0B, 0x06, 0x06, 0x0B, 0x06, 0x0F, 0x0B, 0x0B,
    0x0B, 0x0B, 0x09, 0x09, 0x07, 0x0B, 0x0B, 0x0E, 0x0A, 0x0A, 0x09, 0x08, 0x07, 0x08, 0x0C, 0x0A,
};

USHORT FontColorTable[] =
{
    0x0fff, 0x0fc7, 0x0f52, 0x08cf, 0x0fb4, 0x08fa, 0x0888, 0x0fee, 0x0853, 0x0333,
    0x0ca8, 0x0fdb, 0x0ace, 0x0cff, 0x056b, 0x0632, 0x0135, 0x0357, 0x0bbb,
};

DWriteRender *DWriteMBCSRenders[countof(FontSizeTable)];
DWriteRender *DWriteAnsiRenders[countof(FontSizeTable)];

VOID (NTAPI *StubGetGlyphsBitmap2)(PCSTR Text, PVOID Buffer, ULONG Stride, ULONG ColorIndex);

BOOL TranslateChar(PCSTR Text, USHORT& translated)
{
    USHORT ch;

    ch = *(PUSHORT)Text;
    switch (ch)
    {
        case 0xA181:    // 仭
        case 0x9F81:    // 仧   菱形
        case 0xAA84:    // 劒   横杠
        case 0x4081:    // 丂   空格
            translated = ch;
            return TRUE;

        case 0xA1A1:    // 全角空格
            translated = 0x4081;
            return TRUE;

        case 0x5AA9:    // ㈱ 心形
            translated = 0x8A87;    // TAG2('噴');
            return TRUE;

        case 0xD1A1:    // ⊙ 音符
            translated = 0xF481;  // TAG2('侓');
            return TRUE;

        case 0xF6A1:    // ■ 方块
            translated = 0xA181;
            return TRUE;
    }

    if (ch >= 0x80)
        ch = SWAP2(ch);

    return FALSE;
/*
    if (ch >= '０' && ch <= '９')
    {
        ch = ch - '０' + '侽';
    }
    else if (ch >= 'Ａ' && ch <= 'Ｚ')
    {
        ch = ch - 'Ａ' + '俙';
    }
    else if (ch >= 'ａ' && ch <= 'ｚ')
    {
        ch = ch - 'ａ' + '倎';
    }
    else
    {
        return FALSE;
    }

    translated = SWAP2(ch);

    return TRUE;
*/
}

PVOID NTAPI GetGlyphsBitmap2(PCSTR Text, PVOID Buffer, ULONG Stride, ULONG ColorIndex)
{
    DWriteRender    *mbcsRender, *ansiRender;
    ULONG_PTR       fontSize, fontIndex, color;
    DOUBLE          delta, width;

    //return StubGetGlyphsBitmap2(Text, Buffer, Stride, ColorIndex), 0;

    fontIndex   = *(PULONG_PTR)PtrAdd(GameFontRender, 0x24);
    fontSize    = FontSizeTable[fontIndex];
    mbcsRender  = DWriteMBCSRenders[fontIndex];
    ansiRender  = DWriteAnsiRenders[fontIndex];
    color       = FontColorTable[ColorIndex];
    delta       = 0;

    for (auto &chr : String::Decode(Text, StrLengthA(Text), CP_GBK))
    {
        USHORT translated;
        CHAR ansi = Text[0];

        if (ansi == ' ')
        {
            width = fontSize / 2;
            ++Text;
        }
        else if (ansi > 0)
        {
            ULONG_PTR runeWidth;
            ansiRender->DrawRune(chr, color, Buffer, Stride, &runeWidth);
            width = fontSize / 2;
            ++Text;
        }
        else if (TranslateChar(Text, translated))
        {
            CHAR tmp[3] = { translated & 0xFF, translated >> 8 };

            StubGetGlyphsBitmap2(tmp, Buffer, Stride, ColorIndex);
            width = fontSize;
            Text += 2;
        }
        else
        {
            ULONG_PTR runeWidth;
            mbcsRender->DrawRune(chr, color, Buffer, Stride, &runeWidth);
            width = fontSize;
            Text += 2;
        }

        width += delta;
        Buffer = PtrAdd(Buffer, (LONG_PTR)width * 2);
        delta = width - (LONG_PTR)width;
    }

    return Buffer;
}

PVOID FASTCALL DrawTalkText(PVOID thiz, PVOID, PVOID Buffer, ULONG Stride, PCSTR Text, ULONG ColorIndex)
{
    CHAR tmp[3] = { Text[0], Text[0] < 0 ? Text[1] : 0 };
    return GetGlyphsBitmap2(tmp, Buffer, Stride * 2, ColorIndex);
}

NAKED PVOID NakedDrawDialogText(PVOID thiz, PVOID, PVOID Buffer, ULONG Stride, PCSTR Text, ULONG ColorIndex)
{
    INLINE_ASM
    {
        movzx   ebx, bl;
        push    ebx;
        lea     ebx, [esp];
        push    edx;                    // colorIndex
        mov     edx, [esp+10h];
        lea     edx, [edx*2];
        push    edx;                    // stride
        push    eax;                    // buffer
        push    ebx;                    // text
        call    GetGlyphsBitmap2;
        pop     ebx;
        ret     8;
    }
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
        DWriteRender**  mbcsRender = DWriteMBCSRenders;
        DWriteRender**  ansiRender = DWriteAnsiRenders;

        FOR_EACH_ARRAY(fontSize, FontSizeTable)
        {
            *mbcsRender = new DWriteRender();
            if (*mbcsRender == nullptr)
            {
                hr = STATUS_NO_MEMORY;
                break;
            }

            hr = (*mbcsRender)->Initialize(L"font.ttf", nullptr, *fontSize);
            FAIL_BREAK(hr);
            ++mbcsRender;

            *ansiRender = new DWriteRender();
            if (*ansiRender == nullptr)
            {
                hr = STATUS_NO_MEMORY;
                break;
            }

            hr = (*ansiRender)->Initialize(nullptr, L"SIMHEI", *fontSize);
            FAIL_BREAK(hr);
            ++ansiRender;
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

    //AllocConsole();
    Success = NT_SUCCESS(InitializeDWrite());
    InitializeTextPatcher(BaseAddress);

    //DWriteRenders[9]->DrawRune(L'P', FontColorTable[0], 0, 0, 0), Ps::ExitProcess(0);

    Success = Success && FindFontRender(BaseAddress) != IMAGE_INVALID_VA;

    using namespace Mp;

    auto sleep = [] (ULONG ms) -> VOID
    {
        Ps::Sleep(1);
    };

    PATCH_MEMORY_DATA p[] =
    {
        FunctionCallVa((PVOID)0x4BE533, (ULONG64)(API_POINTER(::Sleep))sleep),
        FunctionCallVa((PVOID)0x47CF77, (ULONG64)(API_POINTER(::Sleep))sleep),

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

        MemoryPatchVa(0xEBull, 1, 0x485041),
        MemoryPatchVa(0x0404ull, 2, 0x4850FE),
        FunctionJumpVa(Success ? (PVOID)0x4B7C30 : IMAGE_INVALID_VA, GetGlyphsBitmap2, &StubGetGlyphsBitmap2),
        FunctionJumpVa(Success ? (PVOID)0x484A40 : IMAGE_INVALID_VA, DrawTalkText),
        FunctionJumpVa(Success ? (PVOID)0x484A90 : IMAGE_INVALID_VA, NakedDrawDialogText),
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
