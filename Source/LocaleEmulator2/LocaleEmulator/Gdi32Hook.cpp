#include "stdafx.h"

typedef struct
{
    LPARAM          lParam;
    PLeGlobalData   GlobalData;
    PVOID           Callback;

} GDI_ENUM_FONT_PARAM, *PGDI_ENUM_FONT_PARAM;

ULONG (NTAPI *GdiGetCodePage)(HDC NewDC);

HFONT GetFontFromFont(PLeGlobalData GlobalData, HFONT Font)
{
    LOGFONTW LogFont;

    if (GetObjectW(Font, sizeof(LogFont), &LogFont) == 0)
        return NULL;

    LogFont.lfCharSet = GlobalData->GetLeb()->DefaultCharset;
    Font = CreateFontIndirectW(&LogFont);

    return Font;
}

HFONT GetFontFromDC(PLeGlobalData GlobalData, HDC hDC)
{
    HFONT       Font;
    LOGFONTW    LogFont;

    Font = (HFONT)GetCurrentObject(hDC, OBJ_FONT);
    if (Font == NULL)
        return NULL;

    return GetFontFromFont(GlobalData, Font);
}

HGDIOBJ NTAPI LeStubGetStockObject(LONG Object)
{
    HGDIOBJ         StockObject;
    PULONG_PTR      Index;
    PLeGlobalData   GlobalData = LeGetGlobalData();

    StockObject = NULL;

    static ULONG_PTR StockObjectIndex[] =
    {
        ANSI_FIXED_FONT,
        ANSI_VAR_FONT,
        DEVICE_DEFAULT_FONT,
        DEFAULT_GUI_FONT,
        OEM_FIXED_FONT,
        SYSTEM_FONT,
        SYSTEM_FIXED_FONT,
    };

    if (!GlobalData->HookRoutineData.Gdi32.StockObjectInitialized)
    {
        PROTECT_SECTION(&GlobalData->HookRoutineData.Gdi32.GdiLock)
        {
            if (GlobalData->HookRoutineData.Gdi32.StockObjectInitialized)
                break;

            FOR_EACH(Index, StockObjectIndex, countof(StockObjectIndex))
            {
                GlobalData->HookRoutineData.Gdi32.StockObject[*Index] = GetFontFromFont(GlobalData, (HFONT)GlobalData->GetStockObject(*Index));
            }

            GlobalData->HookRoutineData.Gdi32.StockObjectInitialized = TRUE;
        }
    }

    LOOP_ONCE
    {
        if (Object > countof(GlobalData->HookRoutineData.Gdi32.StockObject))
            break;

        StockObject = GlobalData->HookRoutineData.Gdi32.StockObject[Object];

        if (StockObject != NULL)
            return StockObject;
    }

    return GlobalData->GetStockObject(Object);
}

HFONT NTAPI LeCreateFontIndirectExW(PENUMLOGFONTEXDVW penumlfex)
{
    ENUMLOGFONTEXDVW enumlfex;
    PLeGlobalData GlobalData = LeGetGlobalData();

    if (penumlfex != NULL) LOOP_ONCE
    {
        ULONG_PTR Charset;

        Charset = penumlfex->elfEnumLogfontEx.elfLogFont.lfCharSet;

        if (Charset != ANSI_CHARSET && Charset != DEFAULT_CHARSET)
            break;

        enumlfex = *penumlfex;
        enumlfex.elfEnumLogfontEx.elfLogFont.lfCharSet = GlobalData->GetLeb()->DefaultCharset;

        //if (GdiGetCodePage == NULL)
        //CopyStruct(enumlfex.elfEnumLogfontEx.elfLogFont.lfFaceName, GlobalData->GetLeb()->DefaultFaceName, LF_FACESIZE);
        //AllocConsole();
        //PrintConsoleW(L"%s\n", enumlfex.elfEnumLogfontEx.elfLogFont.lfFaceName);

        penumlfex = &enumlfex;
    }

    return GlobalData->CreateFontIndirectExW(penumlfex);
}

HDC NTAPI LeCreateCompatibleDC(HDC hDC)
{
    HDC             NewDC;
    HFONT           Font;
    LOGFONTW        LogFont;
    PLeGlobalData   GlobalData = LeGetGlobalData();

    NewDC = GlobalData->CreateCompatibleDC(hDC);

    if (NewDC == NULL)
        return NewDC;

    Font = (HFONT)GetCurrentObject(NewDC, OBJ_FONT);
    if (Font == NULL)
        return NewDC;

    if (GetObjectW(Font, sizeof(LogFont), &LogFont) == 0)
        return NewDC;

    LogFont.lfCharSet = GlobalData->GetLeb()->DefaultCharset;

    //if (hDC == NULL)
        CopyStruct(&LogFont.lfFaceName, GlobalData->GetLeb()->DefaultFaceName, sizeof(LogFont.lfFaceName));

    Font = CreateFontIndirectW(&LogFont);
    if (Font == NULL)
        return NewDC;

    SelectObject(NewDC, Font);
    DeleteObject(Font);

    return NewDC;
}

int NTAPI LeEnumFontFamiliesExA(HDC hdc, LPLOGFONTA lpLogfont, FONTENUMPROCA lpProc, LPARAM lParam, DWORD dwFlags)
{
    ULONG_PTR           Charset;
    LOGFONTA            lf;
    PLeGlobalData       GlobalData = LeGetGlobalData();
    GDI_ENUM_FONT_PARAM Param;

    LOOP_ONCE
    {
        if (lpLogfont == NULL)
            break;

        Charset = lpLogfont->lfCharSet;
        switch (Charset)
        {
            case ANSI_CHARSET:
                break;

            case DEFAULT_CHARSET:
                Param.Callback      = lpProc;
                Param.GlobalData    = GlobalData;
                Param.lParam        = lParam;

                lParam = (LPARAM)&Param;
                lpProc = [] (CONST LOGFONTA *LogFont, CONST TEXTMETRICA *TextMetric, DWORD FontType, LPARAM Param)
                        {
                            PGDI_ENUM_FONT_PARAM EnumParam;
                            LPENUMLOGFONTEXA elf = (LPENUMLOGFONTEXA)LogFont;

                            EnumParam = (PGDI_ENUM_FONT_PARAM)Param;

                            if (LogFont->lfCharSet == EnumParam->GlobalData->GetLePeb()->OriginalCharset)
                            {
                                *(PBYTE)&LogFont->lfCharSet = EnumParam->GlobalData->GetLeb()->DefaultCharset;
                                CopyStruct(elf->elfScript, EnumParam->GlobalData->GetLePeb()->ScriptNameA, sizeof(elf->elfScript));
                            }

                            return ((FONTENUMPROCA)EnumParam->Callback)(LogFont, TextMetric, FontType, Param);
                        };
                break;
        }
    }

    return GlobalData->EnumFontFamiliesExA(hdc, lpLogfont, lpProc, lParam, dwFlags);
}

int NTAPI LeEnumFontFamiliesExW(HDC hdc, LPLOGFONTW lpLogfont, FONTENUMPROCW lpProc, LPARAM lParam, DWORD dwFlags)
{
    ULONG_PTR           Charset;
    LOGFONTW            lf;
    PLeGlobalData       GlobalData = LeGetGlobalData();
    GDI_ENUM_FONT_PARAM Param;

    LOOP_ONCE
    {
        if (lpLogfont == NULL)
            break;

        Charset = lpLogfont->lfCharSet;
        switch (Charset)
        {
            case ANSI_CHARSET:
                break;

            case DEFAULT_CHARSET:
                Param.Callback      = lpProc;
                Param.GlobalData    = GlobalData;
                Param.lParam        = lParam;

                lParam = (LPARAM)&Param;
                lpProc = [] (CONST LOGFONTW *LogFont, CONST TEXTMETRICW *TextMetric, DWORD FontType, LPARAM Param)
                        {
                            PGDI_ENUM_FONT_PARAM EnumParam;
                            LPENUMLOGFONTEXW elf = (LPENUMLOGFONTEXW)LogFont;

                            EnumParam = (PGDI_ENUM_FONT_PARAM)Param;

                            if (LogFont->lfCharSet == EnumParam->GlobalData->GetLePeb()->OriginalCharset)
                            {
                                *(PBYTE)&LogFont->lfCharSet = EnumParam->GlobalData->GetLeb()->DefaultCharset;
                                CopyStruct(elf->elfScript, EnumParam->GlobalData->GetLePeb()->ScriptNameW, sizeof(elf->elfScript));
                            }

                            return ((FONTENUMPROCW)EnumParam->Callback)(LogFont, TextMetric, FontType, Param);
                        };
                break;
        }
    }

    return GlobalData->EnumFontFamiliesExW(hdc, lpLogfont, lpProc, lParam, dwFlags);
}

int NTAPI LeEnumFontFamiliesA(HDC hdc, PCSTR lpLogfont, FONTENUMPROCA lpProc, LPARAM lParam)
{
    LOGFONTA lf;

    ZeroMemory(&lf, sizeof(lf));

    lf.lfPitchAndFamily = 0;
    lf.lfCharSet = DEFAULT_CHARSET;
    StrCopyA(lf.lfFaceName, lpLogfont);

    return LeEnumFontFamiliesExA(hdc, &lf, lpProc, lParam, 0);
}

int NTAPI LeEnumFontFamiliesW(HDC hdc, PCWSTR lpLogfont, FONTENUMPROCW lpProc, LPARAM lParam)
{
    LOGFONTW lf;

    ZeroMemory(&lf, sizeof(lf));

    lf.lfPitchAndFamily = 0;
    lf.lfCharSet = DEFAULT_CHARSET;
    StrCopyW(lf.lfFaceName, lpLogfont);

    return LeEnumFontFamiliesExW(hdc, &lf, lpProc, lParam, 0);
}

int NTAPI LeEnumFontsA(HDC hDC, PCSTR lpLogfont, FONTENUMPROCA lpProc, LPARAM lParam)
{
    GDI_ENUM_FONT_PARAM Param;

    Param.lParam = lParam;
    Param.Callback = lpProc;
    Param.GlobalData = LeGetGlobalData();

    return Param.GlobalData->EnumFontsA(hDC, lpLogfont,
                [] (const LOGFONTA *lplf, const TEXTMETRICA *lptm, DWORD dwType, LPARAM lpData) -> int
                {
                    PGDI_ENUM_FONT_PARAM Param = (PGDI_ENUM_FONT_PARAM)lpData;

                    ((PLOGFONTW)lplf)->lfCharSet = Param->GlobalData->GetLeb()->DefaultCharset;
                    return ((FONTENUMPROCA)Param->Callback)(lplf, lptm, dwType, Param->lParam);
                },
                (LPARAM)&Param
            );
}

int NTAPI LeEnumFontsW(HDC hDC, PCWSTR lpLogfont, FONTENUMPROCW lpProc, LPARAM lParam)
{
    GDI_ENUM_FONT_PARAM Param;

    Param.lParam = lParam;
    Param.Callback = lpProc;
    Param.GlobalData = LeGetGlobalData();

    return Param.GlobalData->EnumFontsW(hDC, lpLogfont,
                [] (const LOGFONTW *lplf, const TEXTMETRICW *lptm, DWORD dwType, LPARAM lpData) -> int
                {
                    PGDI_ENUM_FONT_PARAM Param = (PGDI_ENUM_FONT_PARAM)lpData;

                    ((PLOGFONTW)lplf)->lfCharSet = Param->GlobalData->GetLeb()->DefaultCharset;
                    return ((FONTENUMPROCW)Param->Callback)(lplf, lptm, dwType, Param->lParam);
                },
                (LPARAM)&Param
            );
}

TYPE_OF(SelectObject)*  StubSelectObject;

HGDIOBJ NTAPI LeSelectObject(HDC hdc, HGDIOBJ h)
{
    HGDIOBJ obj;

    obj = StubSelectObject(hdc, h);

    if (GdiGetCodePage(hdc) == 0x3A4)
    {
        ULONG objtype = GetObjectType(h);

        union
        {
            LOGFONTW lf;
        };

        switch (objtype)
        {
            case OBJ_FONT:
                GetObjectW(h, sizeof(lf), &lf);
                break;

            default:
                return obj;
        }
    }

    return obj;
}

NTSTATUS LeGlobalData::HookGdi32Routines(PVOID Gdi32)
{
    // *(PVOID *)&GdiGetCodePage = GetRoutineAddress(Gdi32, "GdiGetCodePage");

    RtlInitializeCriticalSectionAndSpinCount(&HookRoutineData.Gdi32.GdiLock, 4000);

    if (HookStub.StubNtUserCreateWindowEx != NULL)
    {
        InitFontCharsetInfo();
    }

    MEMORY_FUNCTION_PATCH f[] =
    {
        EAT_HOOK_JUMP_HASH(Gdi32, GDI32_GetStockObject,         LeStubGetStockObject,       HookStub.StubGetStockObject),
        EAT_HOOK_JUMP_HASH(Gdi32, GDI32_CreateFontIndirectExW,  LeCreateFontIndirectExW,    HookStub.StubCreateFontIndirectExW),
        EAT_HOOK_JUMP_HASH(Gdi32, GDI32_CreateCompatibleDC,     LeCreateCompatibleDC,       HookStub.StubCreateCompatibleDC),
        EAT_HOOK_JUMP_HASH(Gdi32, GDI32_EnumFontFamiliesExA,    LeEnumFontFamiliesExA,      HookStub.StubEnumFontFamiliesExA),
        EAT_HOOK_JUMP_HASH(Gdi32, GDI32_EnumFontFamiliesExW,    LeEnumFontFamiliesExW,      HookStub.StubEnumFontFamiliesExW),
        EAT_HOOK_JUMP_HASH(Gdi32, GDI32_EnumFontsW,             LeEnumFontsW,               HookStub.StubEnumFontsW),
        EAT_HOOK_JUMP_HASH(Gdi32, GDI32_EnumFontsA,             LeEnumFontsA,               HookStub.StubEnumFontsA),

        // EAT_HOOK_JUMP_HASH(Gdi32, GDI32_SelectObject,    LeSelectObject,      StubSelectObject),

        EAT_HOOK_JUMP_HASH_NULL(Gdi32, GDI32_EnumFontFamiliesA, LeEnumFontFamiliesA),
        EAT_HOOK_JUMP_HASH_NULL(Gdi32, GDI32_EnumFontFamiliesW, LeEnumFontFamiliesW),
    };

    return Nt_PatchMemory(NULL, 0, f, countof(f), Gdi32);
}

NTSTATUS LeGlobalData::UnHookGdi32Routines()
{
    Nt_RestoreMemory(&HookStub.StubCreateFontIndirectExW);
    Nt_RestoreMemory(&HookStub.StubCreateCompatibleDC);
    Nt_RestoreMemory(&HookStub.StubEnumFontFamiliesExA);
    Nt_RestoreMemory(&HookStub.StubEnumFontFamiliesExW);

    return 0;
}
