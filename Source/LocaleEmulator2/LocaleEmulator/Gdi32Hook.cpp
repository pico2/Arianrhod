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
        return nullptr;

    LogFont.lfCharSet = GlobalData->GetLeb()->DefaultCharset;
    Font = CreateFontIndirectW(&LogFont);

    return Font;
}

HFONT GetFontFromDC(PLeGlobalData GlobalData, HDC hDC)
{
    HFONT       Font;
    LOGFONTW    LogFont;

    Font = (HFONT)GetCurrentObject(hDC, OBJ_FONT);
    if (Font == nullptr)
        return nullptr;

    return GetFontFromFont(GlobalData, Font);
}

HGDIOBJ NTAPI LeGetStockObject(LONG Object)
{
    HGDIOBJ         StockObject;
    PULONG_PTR      Index;
    PLeGlobalData   GlobalData = LeGetGlobalData();

    StockObject = nullptr;

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

        if (StockObject != nullptr)
            return StockObject;
    }

    return GlobalData->GetStockObject(Object);
}

HFONT NTAPI LeCreateFontIndirectExW(PENUMLOGFONTEXDVW penumlfex)
{
    ENUMLOGFONTEXDVW enumlfex;
    PLeGlobalData GlobalData = LeGetGlobalData();

    if (penumlfex != nullptr) LOOP_ONCE
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

    if (NewDC == nullptr)
        return NewDC;

    Font = (HFONT)GetCurrentObject(NewDC, OBJ_FONT);
    if (Font == nullptr)
        return NewDC;

    if (GetObjectW(Font, sizeof(LogFont), &LogFont) == 0)
        return NewDC;

    LogFont.lfCharSet = GlobalData->GetLeb()->DefaultCharset;

    //if (hDC == NULL)
        CopyStruct(&LogFont.lfFaceName, GlobalData->GetLeb()->DefaultFaceName, sizeof(LogFont.lfFaceName));

    Font = CreateFontIndirectW(&LogFont);
    if (Font == nullptr)
        return NewDC;

    SelectObject(NewDC, Font);
    DeleteObject(Font);

    return NewDC;
}

template
<
    typename ElfLogFontType,
    typename TextMetricType,
    typename CallbackType
>
BOOL
NTAPI
EnumFontFamiliesCallback(
    ElfLogFontType*         ElfLogFont,
    TextMetricType*         TextMetric,
    ULONG                   FontType,
    PGDI_ENUM_FONT_PARAM    EnumParam
)
{
    if (ElfLogFont->elfLogFont.lfCharSet == EnumParam->GlobalData->GetLePeb()->OriginalCharset)
    {
        ElfLogFont->elfLogFont.lfCharSet = EnumParam->GlobalData->GetLeb()->DefaultCharset;

        switch (sizeof(ElfLogFont->elfScript[0]))
        {
            case sizeof(CHAR):
                CopyStruct(ElfLogFont->elfScript, EnumParam->GlobalData->GetLePeb()->ScriptNameA, sizeof(ElfLogFont->elfScript));
                break;

            case sizeof(WCHAR):
                CopyStruct(ElfLogFont->elfScript, EnumParam->GlobalData->GetLePeb()->ScriptNameW, sizeof(ElfLogFont->elfScript));
                break;
        }
    }

    return ((CallbackType)EnumParam->Callback)(&ElfLogFont->elfLogFont, TextMetric, FontType, EnumParam->lParam);
}

int NTAPI LeEnumFontFamiliesExA(HDC hdc, LPLOGFONTA lpLogfont, FONTENUMPROCA lpProc, LPARAM lParam, DWORD dwFlags)
{
    ULONG_PTR           Charset;
    LOGFONTA            lf;
    PLeGlobalData       GlobalData = LeGetGlobalData();
    GDI_ENUM_FONT_PARAM Param;

    LOOP_ONCE
    {
        if (lpLogfont == nullptr)
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
                lpProc = (FONTENUMPROCA)EnumFontFamiliesCallback<ENUMLOGFONTEXA, TEXTMETRICA, FONTENUMPROCA>;
                break;
        }
    }

    return GlobalData->EnumFontFamiliesExA(hdc, lpLogfont, lpProc, lParam, dwFlags);
}

HFONT
NTAPI
LeNtGdiHfontCreate(
    PENUMLOGFONTEXDVW   EnumLogFont,
    ULONG               SizeOfEnumLogFont,
    LONG                LogFontType,
    LONG                Unknown,
    PVOID               FreeListLocalFont
)
{
    PENUMLOGFONTEXDVW   enumlfex;
    PLeGlobalData       GlobalData = LeGetGlobalData();

    if (EnumLogFont != nullptr) LOOP_ONCE
    {
        ULONG_PTR Charset;

        Charset = EnumLogFont->elfEnumLogfontEx.elfLogFont.lfCharSet;

        if (Charset != ANSI_CHARSET && Charset != DEFAULT_CHARSET)
            break;

        enumlfex = (PENUMLOGFONTEXDVW)AllocStack(SizeOfEnumLogFont);

        CopyMemory(enumlfex, EnumLogFont, SizeOfEnumLogFont);

        enumlfex->elfEnumLogfontEx.elfLogFont.lfCharSet = GlobalData->GetLeb()->DefaultCharset;

        //if (GdiGetCodePage == NULL)
        //CopyStruct(enumlfex.elfEnumLogfontEx.elfLogFont.lfFaceName, GlobalData->GetLeb()->DefaultFaceName, LF_FACESIZE);
        //AllocConsole();
        //PrintConsoleW(L"%s\n", enumlfex.elfEnumLogfontEx.elfLogFont.lfFaceName);

        EnumLogFont = enumlfex;
    }

    return GlobalData->HookStub.StubNtGdiHfontCreate(EnumLogFont, SizeOfEnumLogFont, LogFontType, Unknown, FreeListLocalFont);
}

int NTAPI LeEnumFontFamiliesExW(HDC hdc, LPLOGFONTW lpLogfont, FONTENUMPROCW lpProc, LPARAM lParam, DWORD dwFlags)
{
    ULONG_PTR           Charset;
    LOGFONTW            lf;
    PLeGlobalData       GlobalData = LeGetGlobalData();
    GDI_ENUM_FONT_PARAM Param;

    LOOP_ONCE
    {
        if (lpLogfont == nullptr)
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
                lpProc = (FONTENUMPROCW)EnumFontFamiliesCallback<ENUMLOGFONTEXW, TEXTMETRICW, FONTENUMPROCW>;
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

    switch (GdiGetCodePage(hdc))
    {
        //case 0x3A4:
        case 0x3A8:
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
                    ExceptionBox(lf.lfFaceName, L"FUCK FACE");
                    break;

                default:
                    return obj;
            }

            break;
        }
    }

    return obj;
}

/************************************************************************
  init
************************************************************************/

PVOID FindNtGdiHfontCreate(PVOID Gdi32)
{
    PVOID CreateFontIndirectExW, NtGdiHfontCreate;

    CreateFontIndirectExW = EATLookupRoutineByHashPNoFix(Gdi32, GDI32_CreateFontIndirectExW);

    NtGdiHfontCreate = WalkOpCodeT(CreateFontIndirectExW, 0x100,
                            WalkOpCodeM(Buffer, OpLength, Ret)
                            {
                                switch (Buffer[0])
                                {
                                    case CALL:
                                        Buffer = GetCallDestination(Buffer);
                                        if (IsSystemCall(Buffer) == FALSE)
                                            break;

                                        Ret = Buffer;
                                        break;
                                }

                                return STATUS_NOT_FOUND;
                            }
                        );

    return NtGdiHfontCreate;
}


/************************************************************************
  init end
************************************************************************/

NTSTATUS LeGlobalData::HookGdi32Routines(PVOID Gdi32)
{
    PVOID NtGdiHfontCreate;

    *(PVOID *)&GdiGetCodePage = GetRoutineAddress(Gdi32, "GdiGetCodePage");

    NtGdiHfontCreate = FindNtGdiHfontCreate(Gdi32);
    if (NtGdiHfontCreate == nullptr)
        return STATUS_NOT_FOUND;

    RtlInitializeCriticalSectionAndSpinCount(&HookRoutineData.Gdi32.GdiLock, 4000);

    if (HookStub.StubNtUserCreateWindowEx != nullptr)
    {
        InitFontCharsetInfo();
    }

    MEMORY_FUNCTION_PATCH f[] =
    {
        LE_EAT_HOOK(Gdi32, GDI32, GetStockObject),
        //LE_EAT_HOOK(Gdi32, GDI32, CreateFontIndirectExW),
        LE_EAT_HOOK(Gdi32, GDI32, CreateCompatibleDC),
        LE_EAT_HOOK(Gdi32, GDI32, EnumFontFamiliesExA),
        LE_EAT_HOOK(Gdi32, GDI32, EnumFontFamiliesExW),
        LE_EAT_HOOK(Gdi32, GDI32, EnumFontsW),
        LE_EAT_HOOK(Gdi32, GDI32, EnumFontsA),

        LE_EAT_HOOK_NULL(Gdi32, GDI32, EnumFontFamiliesA),
        LE_EAT_HOOK_NULL(Gdi32, GDI32, EnumFontFamiliesW),

        LE_INLINE_JUMP(NtGdiHfontCreate),

        //EAT_HOOK_JUMP_HASH(Gdi32, GDI32_SelectObject,    LeSelectObject,      StubSelectObject),

    };

    return Nt_PatchMemory(nullptr, 0, f, countof(f), Gdi32);
}

NTSTATUS LeGlobalData::UnHookGdi32Routines()
{
    Nt_RestoreMemory(&HookStub.StubCreateFontIndirectExW);
    Nt_RestoreMemory(&HookStub.StubCreateCompatibleDC);
    Nt_RestoreMemory(&HookStub.StubEnumFontFamiliesExA);
    Nt_RestoreMemory(&HookStub.StubEnumFontFamiliesExW);

    return 0;
}
