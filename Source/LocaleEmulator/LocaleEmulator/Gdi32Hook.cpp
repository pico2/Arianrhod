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

INT FmsEnumFontFamiliesEx(HDC hDC, PLOGFONTW Logfont, FONTENUMPROCW Proc, LPARAM Parameter, ULONG Flags)
{
    ULONG           NumberOfFonts, PropertySize;
    PULONG          FontIdList, FontId;
    INT             ReturnValue;
    NTSTATUS        Status;
    FMS_ENUMERATOR  Enumerator;
    FMS_FILTER_DATA FilterData;

    ReturnValue = 0;

    Status = FmsInitializeEnumerator(&Enumerator);
    if (NT_FAILED(Status))
        return ReturnValue;

    FmsSetFilter(Enumerator, &FilterData, 0);

    if (Logfont->lfFaceName[0] != 0)
    {
        ZeroMemory(&FilterData, sizeof(FilterData));

        FilterData.Unknown1 = 1;
        FilterData.FilterType = FmsFilterType::FaceName;
        CopyMemory(FilterData.FaceName, Logfont->lfFaceName, sizeof(Logfont->lfFaceName));
        FilterData.FaceName[countof(Logfont->lfFaceName)] = 0;

        FmsAddFilter(Enumerator, &FilterData, 1);
    }

    if (Logfont->lfCharSet != DEFAULT_CHARSET)
    {
        ZeroMemory(&FilterData, sizeof(FilterData));

        FilterData.Unknown1 = 1;
        FilterData.FilterType = FmsFilterType::CharSet;
        FilterData.Charset = Logfont->lfCharSet;

        FmsAddFilter(Enumerator, &FilterData, 1);
    }

    NumberOfFonts = 0;
    FontIdList = nullptr;
    Status = FmsGetFilteredFontList(Enumerator, &NumberOfFonts, FontIdList);
    if (NT_FAILED(Status))
    {
        FmsFreeEnumerator(&Enumerator);
        return ReturnValue;
    }

    FontIdList = (PULONG)AllocStack(NumberOfFonts * sizeof(*FontIdList));
    Status = FmsGetFilteredFontList(Enumerator, &NumberOfFonts, FontIdList);
    if (NT_FAILED(Status))
    {
        FmsFreeEnumerator(&Enumerator);
        return ReturnValue;
    }

    for (PULONG FontId = FontIdList; NumberOfFonts; ++FontId, --NumberOfFonts)
    {
        ULONG           FontType;
        TEXTMETRICW     TextMetric[2];
        ENUMLOGFONTEXW  EnumLogFont;
        WCHAR           Style[countof(EnumLogFont.elfStyle)];

        FillMemory(TextMetric, sizeof(TextMetric), -1);

        Status = FmsGetGdiLogicalFont(Enumerator, *FontId, TRUE, &EnumLogFont, TextMetric, nullptr);
        if (NT_FAILED(Status))
            continue;

        PropertySize = sizeof(EnumLogFont.elfLogFont.lfFaceName);
        Status = FmsGetFontProperty(Enumerator, *FontId, FmsPropertyType::FaceNameLocale, &PropertySize, EnumLogFont.elfLogFont.lfFaceName);
        if (NT_FAILED(Status))
            continue;

        PropertySize = sizeof(EnumLogFont.elfFullName);
        Status = FmsGetFontProperty(Enumerator, *FontId, FmsPropertyType::FullNameLocale, &PropertySize, EnumLogFont.elfFullName);
        if (NT_FAILED(Status))
            continue;

        PropertySize = sizeof(Style);
        Status = FmsGetFontProperty(Enumerator, *FontId, FmsPropertyType::FontStyleNameLocale, &PropertySize, Style);
        if (NT_SUCCESS(Status))
        {
            CopyMemory(EnumLogFont.elfStyle, Style, PropertySize);
        }

        PropertySize = sizeof(FontType);
        Status = FmsGetFontProperty(Enumerator, *FontId, FmsPropertyType::FontType, &PropertySize, &FontType);
        if (NT_FAILED(Status))
            FontType = 0;

        ReturnValue = Proc(&EnumLogFont.elfLogFont, TextMetric, FontType, Parameter);
    }

    FmsFreeEnumerator(&Enumerator);

    return ReturnValue;
}

int NTAPI LeEnumFontFamiliesExW(HDC hdc, LPLOGFONTW lpLogfont, FONTENUMPROCW lpProc, LPARAM lParam, DWORD dwFlags)
{

#if 0

    FMS_CALL_CONTEXT    Context;
    PFMS_CALL_CONTEXT   PrevContext;
    PLeGlobalData       GlobalData = LeGetGlobalData();

    PrevContext = Context.Find();
    if (PrevContext != nullptr)
    {
        return GlobalData->EnumFontFamiliesExW(PrevContext->hDC, lpLogfont, lpProc, lParam, dwFlags);
    }

    Context.hDC = hdc;
    Context.Push();

    return FmsEnumFontFamiliesEx(hdc, lpLogfont, lpProc, lParam, dwFlags);

#else

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
#endif
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

int NTAPI LeEnumFontsA(HDC hDC, PCSTR lpFaceName, FONTENUMPROCA lpProc, LPARAM lParam)
{
    GDI_ENUM_FONT_PARAM Param;

    Param.lParam = lParam;
    Param.Callback = lpProc;
    Param.GlobalData = LeGetGlobalData();

    return Param.GlobalData->EnumFontsA(hDC, lpFaceName,
                [] (const LOGFONTA *lplf, const TEXTMETRICA *lptm, DWORD dwType, LPARAM lpData) -> int
                {
                    PGDI_ENUM_FONT_PARAM Param = (PGDI_ENUM_FONT_PARAM)lpData;

                    ((PLOGFONTW)lplf)->lfCharSet = Param->GlobalData->GetLeb()->DefaultCharset;
                    return ((FONTENUMPROCA)Param->Callback)(lplf, lptm, dwType, Param->lParam);
                },
                (LPARAM)&Param
            );
}

int NTAPI LeEnumFontsW(HDC hDC, PCWSTR lpFaceName, FONTENUMPROCW lpProc, LPARAM lParam)
{
    GDI_ENUM_FONT_PARAM Param;

    Param.lParam = lParam;
    Param.Callback = lpProc;
    Param.GlobalData = LeGetGlobalData();

    return Param.GlobalData->EnumFontsW(hDC, lpFaceName,
                [] (const LOGFONTW *lplf, const TEXTMETRICW *lptm, DWORD dwType, LPARAM lpData) -> int
                {
                    PGDI_ENUM_FONT_PARAM Param = (PGDI_ENUM_FONT_PARAM)lpData;

                    ((PLOGFONTW)lplf)->lfCharSet = Param->GlobalData->GetLeb()->DefaultCharset;
                    return ((FONTENUMPROCW)Param->Callback)(lplf, lptm, dwType, Param->lParam);
                },
                (LPARAM)&Param
            );
}

API_POINTER(SelectObject)  StubSelectObject;

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

    CreateFontIndirectExW = LookupExportTable(Gdi32, GDI32_CreateFontIndirectExW);

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

    Mp::PATCH_MEMORY_DATA p[] =
    {
        LeHookFromEAT(Gdi32, GDI32, GetStockObject),
        //LeHookFromEAT(Gdi32, GDI32, CreateFontIndirectExW),
        LeHookFromEAT(Gdi32, GDI32, CreateCompatibleDC),
        LeHookFromEAT(Gdi32, GDI32, EnumFontFamiliesExA),
        LeHookFromEAT(Gdi32, GDI32, EnumFontFamiliesExW),
        LeHookFromEAT(Gdi32, GDI32, EnumFontsW),
        LeHookFromEAT(Gdi32, GDI32, EnumFontsA),

        LeHookFromEAT2(Gdi32, GDI32, EnumFontFamiliesA),
        LeHookFromEAT2(Gdi32, GDI32, EnumFontFamiliesW),

        LeFunctionJump(NtGdiHfontCreate),

        //Mp::FunctionJumpVa(LookupExportTable(Gdi32, GDI32_SelectObject), LeSelectObject, &StubSelectObject),
    };

    return Mp::PatchMemory(p, countof(p));
}

NTSTATUS LeGlobalData::UnHookGdi32Routines()
{
    Mp::RestoreMemory(HookStub.StubGetStockObject);
    Mp::RestoreMemory(HookStub.StubCreateCompatibleDC);
    Mp::RestoreMemory(HookStub.StubEnumFontFamiliesExA);
    Mp::RestoreMemory(HookStub.StubEnumFontFamiliesExW);
    Mp::RestoreMemory(HookStub.StubEnumFontsA);
    Mp::RestoreMemory(HookStub.StubEnumFontsW);
    Mp::RestoreMemory(HookStub.StubNtGdiHfontCreate);

    return 0;
}
