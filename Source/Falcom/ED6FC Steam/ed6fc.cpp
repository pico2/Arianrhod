// this file must be compiled under zh-CN locale

#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text /MERGE:.text1=.text /SECTION:.idata,ERW")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")
#pragma comment(linker, "/EXPORT:DirectInput8Create=DINPUT8.DirectInput8Create")

#include "ed6fc.h"
#include "ml.cpp"
#include "DWriteRender.h"

#pragma comment(lib, "dwrite.lib")
#pragma comment(lib, "d2d1.lib")

ML_OVERLOAD_NEW

BOOL SleepFix;
PED6_FC_FONT_RENDER GameFontRender;

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

DWriteRender *DWriteMBCSRenders[countof(FontSizeTable)];
DWriteRender *DWriteAnsiRenders[countof(FontSizeTable)];

VOID (NTAPI *StubGetGlyphsBitmap)(PCSTR Text, PVOID Buffer, ULONG Stride, ULONG ColorIndex);

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
        case 0x5C81:    // 乗   横杠
        case 0x9A81:    // 仛   ★
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

        case 0xADA1:    // … 中文省略号
            translated = 0x6381;
            return TRUE;
    }

    return FALSE;
}

PVOID NTAPI GetGlyphsBitmap(PCSTR Text, PVOID Buffer, ULONG Stride, ULONG ColorIndex)
{
    DWriteRender    *mbcsRender, *ansiRender;
    ULONG_PTR       fontSize, fontIndex, color, width;

    fontIndex   = GameFontRender->FontSizeIndex;
    fontSize    = FontSizeTable[fontIndex];
    mbcsRender  = DWriteMBCSRenders[fontIndex];
    ansiRender  = DWriteAnsiRenders[fontIndex];
    color       = FontColorTable[ColorIndex];

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

            StubGetGlyphsBitmap(tmp, Buffer, Stride, ColorIndex);
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

        Buffer = PtrAdd(Buffer, (LONG_PTR)width * 2);
    }

    return Buffer;
}

PVOID FASTCALL DrawTalkText(PVOID thiz, PVOID, PVOID Buffer, ULONG Stride, PCSTR Text, ULONG ColorIndex)
{
    CHAR tmp[3] = { Text[0], Text[0] < 0 ? Text[1] : 0 };
    return GetGlyphsBitmap(tmp, Buffer, Stride * 2, ColorIndex);
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
        call    GetGlyphsBitmap;
        pop     ebx;
        ret     8;
    }
}

NAKED VOID NakedCalcBookTextWidth()
{
    INLINE_ASM
    {
        movzx   edx, [eax];
        mov     ecx, GameFontRender;
        mov     ecx, [ecx]ED6_FC_FONT_RENDER.FontSizeIndex;
        movzx   ecx, FontSizeTable[ecx];
        mov     eax, ecx;
        shr     eax, 1;
        cmp     edx, 80h;
        cmovae  eax, ecx;
        push    eax;
        fild    dword ptr [esp];
        pop     eax;
        ret;
    }
}

/************************************************************************
  load file
************************************************************************/

BOOL NTAPI LoadFileFromDat(PVOID buffer, ULONG datIndex, ULONG datOffset, ULONG fileSize)
{
    PED6_DIR_ENTRY entry;

    entry = DirCacheTable[datIndex];
    if (entry == nullptr)
        return FALSE;

    LOOP_FOREVER
    {
        if (entry->Offset == datOffset && entry->Size == fileSize)
            break;

        ++entry;
    }

    String path;
    NtFileDisk dat;

    GetModuleDirectory(path, nullptr);

    if (NT_SUCCESS(dat.Open(path + String::Format(L"DAT\\ED6_DT%02X\\%.*S", datIndex, sizeof(entry->FileName), entry->FileName))))
    {
        //PrintConsoleW(L"%S\n", entry->FileName);

        *(PULONG)PtrAdd(buffer, 0) = fileSize;
        *(PULONG)PtrAdd(buffer, 4) = RAW_FILE_MAGIC;
        *(PULONG)PtrAdd(buffer, 8) = dat.GetSize32();
        return NT_SUCCESS(dat.Read(PtrAdd(buffer, 12)));
    }

    if (NT_FAILED(dat.Open(path + String::Format(L"ED6_DT%02X.dat", datIndex))))
        return FALSE;

    dat.Seek(datOffset);
    return NT_SUCCESS(dat.Read(buffer, fileSize));
}

ULONG_PTR NTAPI DecompressData(PBYTE& compressed, PBYTE& uncompressed)
{
    if (*(PULONG)&compressed[4] != RAW_FILE_MAGIC)
        return ~0u;

    ULONG size = *(PULONG)(compressed + 8);
    CopyMemory(uncompressed, compressed + 12, size);

    compressed += size + 12;
    uncompressed += size;

    return size;
}

NAKED VOID CDECL NakedLoadFileFromDat()
{
    INLINE_ASM
    {
        push    [esp + 0Ch];
        push    [esp + 0Ch];
        push    [esp + 0Ch];
        push    edi;
        call    LoadFileFromDat;
        ret;
    }
}

PVOID StubNakedDecompressData;

NAKED VOID NakedDecompressData()
{
    INLINE_ASM
    {
        push    ebx;
        push    edi;
        call    DecompressData;
        inc     eax;
        jnz     UNCOMPRESSED;
        jmp     [StubNakedDecompressData];

UNCOMPRESSED:
        dec     eax;
        ret;
    }
}

/************************************************************************
  cpu usage
************************************************************************/

WNDPROC OrigGameWindowProc;

LRESULT NTAPI GameWindowProc(HWND hwnd, UINT message, WPARAM wParam, LPARAM lParam)
{
    switch (message)
    {
        case WM_ACTIVATEAPP:
            SleepFix = wParam == FALSE;
            break;
    }

    return OrigGameWindowProc(hwnd, message, wParam, lParam);
}

/************************************************************************
  init
************************************************************************/

PED6_FC_FONT_RENDER FindFontRender(PVOID BaseAddress)
{
    PVOID p;

     p = SearchPatternSafe(L"81 3D ?? ?? ?? ?? BC 02 00 00", BaseAddress, ImageNtHeaders(BaseAddress)->OptionalHeader.SizeOfImage);
     if (p == nullptr)
         return nullptr;

     return FIELD_BASE(*(PVOID *)PtrAdd(p, 2), ED6_FC_FONT_RENDER, FontWeight);
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

    //AllocConsole();

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

    Success = NT_SUCCESS(InitializeDWrite());
    InitializeTextPatcher(BaseAddress);

    //DWriteRenders[9]->DrawRune(L'P', FontColorTable[0], 0, 0, 0), Ps::ExitProcess(0);

    if (Success)
    {
        GameFontRender = FindFontRender(BaseAddress);
        Success = GameFontRender != nullptr;
    }

    using namespace Mp;

    auto sleep = [] (ULONG ms) -> VOID
    {
        Ps::Sleep(SleepFix ? 1 : ms);
    };

    PATCH_MEMORY_DATA p[] =
    {
        MemoryPatchVa(
            (ULONG64)(API_POINTER(::Sleep))[] (ULONG ms) -> VOID
            {
                Ps::Sleep(SleepFix ? ms == 0 ? 1 : ms : ms);
            },
            sizeof(PVOID), LookupImportTable(BaseAddress, nullptr, KERNEL32_Sleep)
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

                    OrigGameWindowProc = (WNDPROC)SetWindowLongPtrW(Wnd, GWLP_WNDPROC, (LONG_PTR)GameWindowProc);
                }

                return SetWindowPos(Wnd, InsertAfter, X, Y, cx, cy, Flags);
            },
            sizeof(PVOID),
            LookupImportTable(GetExeModuleHandle(), nullptr, USER32_SetWindowPos)
        ),

        // cmp r8, 80
        MemoryPatchVa(0xEBull, 1, 0x485041),
        MemoryPatchVa(0xEBull, 1, 0x469C52),
        MemoryPatchVa(0xEBull, 1, 0x4794B7),
        MemoryPatchVa(0xEBull, 1, 0x47B131),
        MemoryPatchVa(0xEBull, 1, 0x484B0B),
        MemoryPatchVa(0xEBull, 1, 0x488015),
        MemoryPatchVa(0x00ull, 1, 0x48819D),
        MemoryPatchVa(0xEBull, 1, 0x488567),
        MemoryPatchVa(0xEBull, 1, 0x4B78D1),
        MemoryPatchVa(0xEBull, 1, 0x4B7934),
        MemoryPatchVa(0xEBull, 1, 0x4B79B5),
        MemoryPatchVa(0xEBull, 1, 0x4B7A4D),
        MemoryPatchVa(0xEBull, 1, 0x4B7BFC),
        MemoryPatchVa(0xEBull, 1, 0x4B7C6C),
        MemoryPatchVa(0xEBull, 1, 0x4B7D1B),
        MemoryPatchVa(0xEBull, 1, 0x4D9F4D),

        // ctrl code
        MemoryPatchVa(0x0404ull, 2, 0x4850FE),

        FunctionJumpVa(Success ? GET_GLYPHS_BITMAP_VA       : IMAGE_INVALID_VA, GetGlyphsBitmap, &StubGetGlyphsBitmap),
        FunctionJumpVa(Success ? DRAW_TALK_TEXT_VA          : IMAGE_INVALID_VA, DrawTalkText),
        FunctionJumpVa(Success ? DRAW_DIALOG_TEXT_VA        : IMAGE_INVALID_VA, NakedDrawDialogText),
        FunctionJumpVa(Success ? CACL_BOOK_TEXT_WIDTH_VA    : IMAGE_INVALID_VA, NakedCalcBookTextWidth),

        FunctionJumpVa(LOAD_FILE_FROM_DAT_VA,   NakedLoadFileFromDat),
        FunctionJumpVa(DECOMPRESS_DATA_VA,      NakedDecompressData, &StubNakedDecompressData),
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
