#include "stdafx.h"

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

BOOL IsGdiHookBypassed()
{
    return FindThreadFrame(GDI_HOOK_BYPASS) != nullptr;
}

HFONT CreateFontIndirectBypassA(CONST LOGFONTA *lplf)
{
    TEB_ACTIVE_FRAME Bypass(GDI_HOOK_BYPASS);
    Bypass.Push();

    return CreateFontIndirectA(lplf);
}

HFONT CreateFontIndirectBypassW(CONST LOGFONTW *lplf)
{
    TEB_ACTIVE_FRAME Bypass(GDI_HOOK_BYPASS);
    Bypass.Push();

    return CreateFontIndirectW(lplf);
}

VOID LeGlobalData::GetTextMetricsAFromLogFont(PTEXTMETRICA TextMetricA, CONST LOGFONTW *LogFont)
{
    HDC     hDC;
    HFONT   Font, OldFont;
    ULONG   GraphicsMode;

    hDC = this->CreateCompatibleDC(nullptr);
    if (hDC == nullptr)
        return;

    GraphicsMode = SetGraphicsMode(hDC, GM_ADVANCED);

    LOOP_ONCE
    {
        Font = CreateFontIndirectBypassW(LogFont);
        if (Font == nullptr)
            break;

        OldFont = (HFONT)SelectObject(hDC, Font);
        if (OldFont != nullptr)
        {
            TextMetricA->tmCharSet = 0x80;
            GetTextMetricsA(hDC, TextMetricA);
        }

        SelectObject(hDC, OldFont);
        DeleteObject(Font);
    }

    DeleteDC(hDC);
}

VOID LeGlobalData::GetTextMetricsWFromLogFont(PTEXTMETRICW TextMetricW, CONST LOGFONTW *LogFont)
{
    HDC     hDC;
    HFONT   Font, OldFont;
    ULONG   GraphicsMode;

    hDC = this->CreateCompatibleDC(nullptr);
    if (hDC == nullptr)
        return;

    GraphicsMode = SetGraphicsMode(hDC, GM_ADVANCED);

    LOOP_ONCE
    {
        Font = CreateFontIndirectBypassW(LogFont);
        if (Font == nullptr)
            break;

        OldFont = (HFONT)SelectObject(hDC, Font);
        if (OldFont != nullptr)
            GetTextMetricsW(hDC, TextMetricW);

        SelectObject(hDC, OldFont);
        DeleteObject(Font);
    }

    DeleteDC(hDC);
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

BOOL NTAPI LeDeleteObject(HGDIOBJ GdiObject)
{
    HGDIOBJ*        StockObject;
    PLeGlobalData   GlobalData = LeGetGlobalData();

    if (GdiObject == nullptr || GlobalData->HookRoutineData.Gdi32.StockObjectInitialized == FALSE)
        return TRUE;

    FOR_EACH_ARRAY(StockObject, GlobalData->HookRoutineData.Gdi32.StockObject)
    {
        if (GdiObject == *StockObject)
            return TRUE;
    }

    return GlobalData->DeleteObject(GdiObject);
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

    SelectObject(NewDC, GetStockObject(SYSTEM_FONT));

    return NewDC;
}

NTSTATUS
LeGlobalData::
GetNameRecordFromNameTable(
    PVOID           TableBuffer,
    ULONG_PTR       TableSize,
    ULONG_PTR       NameID,
    PUNICODE_STRING Name
)
{
    using namespace Gdi;

    USHORT                  LanguageID;
    ULONG_PTR               StorageOffset, NameRecordCount;
    PTT_NAME_TABLE_HEADER   NameHeader;
    PTT_NAME_RECORD         NameRecord, NameRecordUser, NameRecordEn;

    NameHeader = (PTT_NAME_TABLE_HEADER)TableBuffer;

    NameRecordCount = Bswap(NameHeader->NameRecordCount);
    StorageOffset = Bswap(NameHeader->StorageOffset);

    if (StorageOffset >= TableSize)
        return STATUS_NOT_SUPPORTED;

    if (StorageOffset < NameRecordCount * sizeof(*NameRecord))
        return STATUS_NOT_SUPPORTED;

    LanguageID      = Bswap((USHORT)this->GetLeb()->LocaleID);
    NameRecordUser  = nullptr;
    NameRecordEn    = nullptr;
    NameRecord      = (PTT_NAME_RECORD)(NameHeader + 1);

    FOR_EACH(NameRecord, NameRecord, NameRecordCount)
    {
        if (NameRecord->PlatformID != TT_PLATFORM_ID_WINDOWS)
            continue;

        if (NameRecord->EncodingID != TT_ENCODEING_ID_UTF16_BE)
            continue;

        if (NameRecord->NameID != NameID)
            continue;

        if (NameRecord->LanguageID == Bswap((USHORT)0x0409))
            NameRecordEn = NameRecord;

        if (NameRecord->LanguageID != LanguageID)
            continue;

        NameRecordUser = NameRecord;
        break;
    }

    NameRecordUser = NameRecordUser == nullptr ? NameRecordEn : NameRecordUser;

    if (NameRecordUser != nullptr)
    {
        PWSTR     FaceName, Buffer;
        ULONG_PTR Offset, Length;

        Offset = StorageOffset + Bswap(NameRecordUser->StringOffset);
        Length = Bswap(NameRecordUser->StringLength);
        FaceName = (PWSTR)PtrAdd(TableBuffer, Offset);

        Buffer = Name->Buffer;
        Length = (USHORT)ML_MIN(Length, Name->MaximumLength);
        Name->Length = Length;

        for (ULONG_PTR Index = 0; Index != Length / sizeof(WCHAR); ++Index)
        {
            Buffer[Index] = Bswap(FaceName[Index]);
        }

        if (Length < Name->MaximumLength)
            *PtrAdd(Buffer, Length) = 0;

        return STATUS_SUCCESS;
    }

    return STATUS_NOT_FOUND;
}

NTSTATUS LeGlobalData::AdjustFaceNameInternal(PADJUST_FACE_NAME_DATA AdjustData)
{
    NTSTATUS        Status;
    PVOID           Table;
    ULONG_PTR       TableSize, TableName;
    WCHAR           FaceNameBuffer[LF_FACESIZE];
    WCHAR           FullNameBuffer[LF_FULLFACESIZE];
    UNICODE_STRING  FaceName, FullName;

    TableName = Gdi::TT_TABLE_TAG_NAME;
    TableSize = GetFontData(AdjustData->DC, TableName, 0, 0, 0);
    if (TableSize == GDI_ERROR)
        return STATUS_OBJECT_NAME_NOT_FOUND;

    Table = AllocStack(TableSize);
    TableSize = GetFontData(AdjustData->DC, TableName, 0, Table, TableSize);
    if (TableSize == GDI_ERROR)
        return STATUS_OBJECT_NAME_NOT_FOUND;

    RtlInitEmptyString(&FaceName, FaceNameBuffer, sizeof(FaceNameBuffer));
    RtlInitEmptyString(&FullName, FullNameBuffer, sizeof(FullNameBuffer));

    Status = this->GetNameRecordFromNameTable(Table, TableSize, Gdi::TT_NAME_ID_FACENAME, &FaceName);
    Status = NT_SUCCESS(Status) ? this->GetNameRecordFromNameTable(Table, TableSize, Gdi::TT_NAME_ID_FULLNAME, &FullName) : Status;

    if (NT_SUCCESS(Status))
    {
        BOOL        Vertical;
        PWSTR       Buffer;
        ULONG_PTR   Length;

        Vertical = AdjustData->EnumLogFontEx->elfLogFont.lfFaceName[0] == '@';

        Buffer = AdjustData->EnumLogFontEx->elfLogFont.lfFaceName + Vertical;
        Length = ML_MIN(sizeof(AdjustData->EnumLogFontEx->elfLogFont.lfFaceName) - Vertical, FaceName.Length);
        CopyMemory(Buffer, FaceName.Buffer, Length);
        *PtrAdd(Buffer, Length) = 0;

        Buffer = AdjustData->EnumLogFontEx->elfFullName + Vertical;
        Length = ML_MIN(sizeof(AdjustData->EnumLogFontEx->elfFullName) - Vertical, FullName.Length);
        CopyMemory(Buffer, FullName.Buffer, Length);
        *PtrAdd(Buffer, Length) = 0;
    }

    return Status;
}

NTSTATUS LeGlobalData::AdjustFaceName(LPENUMLOGFONTEXW EnumLogFontEx, PTEXT_METRIC_INTERNAL TextMetric, ULONG_PTR FontType)
{
    NTSTATUS Status;
    ADJUST_FACE_NAME_DATA AdjustData;

    if (FLAG_ON(FontType, RASTER_FONTTYPE))
        return STATUS_NOT_SUPPORTED;

    ZeroMemory(&AdjustData, sizeof(AdjustData));
    AdjustData.EnumLogFontEx = EnumLogFontEx;

    Status = STATUS_UNSUCCESSFUL;

    LOOP_ONCE
    {
        AdjustData.Font = CreateFontIndirectBypassW(&EnumLogFontEx->elfLogFont);
        if (AdjustData.Font == nullptr)
            break;

        AdjustData.DC = this->CreateCompatibleDC(nullptr);
        if (AdjustData.DC == nullptr)
            break;

        AdjustData.OldFont = (HFONT)SelectObject(AdjustData.DC, AdjustData.Font);
        if (AdjustData.OldFont == nullptr)
            break;

        Status = AdjustFaceNameInternal(&AdjustData);
        //FAIL_BREAK(Status);

        if (TextMetric != nullptr)
        {
            if (GetTextMetricsA(AdjustData.DC, &TextMetric->TextMetricA) && 
                GetTextMetricsW(AdjustData.DC, &TextMetric->TextMetricW))
            {
                TextMetric->Filled = TRUE;
            }
        }
    }

    if (AdjustData.OldFont != nullptr)
        SelectObject(AdjustData.DC, AdjustData.OldFont);

    if (AdjustData.DC != nullptr)
        DeleteDC(AdjustData.DC);

    if (AdjustData.Font != nullptr)
        this->DeleteObject(AdjustData.Font);

    return Status;
}

int NTAPI LeEnumFontFamiliesExW(HDC hdc, LPLOGFONTW lpLogfont, FONTENUMPROCW lpProc, LPARAM lParam, DWORD dwFlags)
{
    PLeGlobalData       GlobalData = LeGetGlobalData();
    GDI_ENUM_FONT_PARAM Param;
    LOGFONTW            LocalLogFont;

    Param.Callback      = lpProc;
    Param.GlobalData    = GlobalData;
    Param.lParam        = lParam;
    Param.Charset       = lpLogfont->lfCharSet;

    LocalLogFont = *lpLogfont;

    return GlobalData->EnumFontFamiliesExW(hdc, &LocalLogFont,
            [](CONST LOGFONTW *lf, CONST TEXTMETRICW *TextMetricW, DWORD FontType, LPARAM param) -> INT
            {
                NTSTATUS                Status;
                PGDI_ENUM_FONT_PARAM    EnumParam;
                TEXT_METRIC_INTERNAL    TextMetric;

                EnumParam = (PGDI_ENUM_FONT_PARAM)param;
                if (EnumParam->Charset == DEFAULT_CHARSET && lf->lfCharSet == EnumParam->GlobalData->GetLePeb()->OriginalCharset)
                {
                    ((LPLOGFONTW)lf)->lfCharSet = EnumParam->GlobalData->GetLeb()->DefaultCharset;
                }

                Status = EnumParam->GlobalData->AdjustFaceName((LPENUMLOGFONTEXW)lf, &TextMetric, FontType);
                if (Status == STATUS_OBJECT_NAME_NOT_FOUND)
                    return TRUE;

                if (TextMetric.Filled == FALSE)
                {
                    TextMetric.TextMetricW = *TextMetricW;
                    TextMetric.Magic = 0;
                }

                TextMetricW = &TextMetric.TextMetricW;

                return ((FONTENUMPROCW)(EnumParam->Callback))(lf, TextMetricW, FontType, EnumParam->lParam);
            },
            (LPARAM)&Param,
            dwFlags
        );
}

VOID ConvertAnsiLogfontToUnicode(PLOGFONTW LogFontW, PLOGFONTA LogFontA)
{
    CopyMemory(LogFontW, LogFontA, PtrOffset(&LogFontA->lfFaceName, LogFontA));
    RtlMultiByteToUnicodeN(LogFontW->lfFaceName, sizeof(LogFontW->lfFaceName), nullptr, LogFontA->lfFaceName, StrLengthA(LogFontA->lfFaceName) + 1);
}

VOID ConvertUnicodeLogfontToAnsi(PLOGFONTA LogFontA, PLOGFONTW LogFontW)
{
    CopyMemory(LogFontA, LogFontW, PtrOffset(&LogFontW->lfFaceName, LogFontW));
    RtlUnicodeToMultiByteN(LogFontA->lfFaceName, sizeof(LogFontA->lfFaceName), nullptr, LogFontW->lfFaceName, (StrLengthW(LogFontW->lfFaceName) + 1) * sizeof(WCHAR));
}

VOID ConvertUnicodeTextMetricToAnsi(PTEXTMETRICA TextMetricA, CONST TEXTMETRICW *TextMetricW)
{
    TextMetricA->tmHeight           = TextMetricW->tmHeight;
    TextMetricA->tmAscent           = TextMetricW->tmAscent;
    TextMetricA->tmDescent          = TextMetricW->tmDescent;
    TextMetricA->tmInternalLeading  = TextMetricW->tmInternalLeading;
    TextMetricA->tmExternalLeading  = TextMetricW->tmExternalLeading;
    TextMetricA->tmAveCharWidth     = TextMetricW->tmAveCharWidth;
    TextMetricA->tmMaxCharWidth     = TextMetricW->tmMaxCharWidth;
    TextMetricA->tmWeight           = TextMetricW->tmWeight;
    TextMetricA->tmOverhang         = TextMetricW->tmOverhang;
    TextMetricA->tmDigitizedAspectX = TextMetricW->tmDigitizedAspectX;
    TextMetricA->tmDigitizedAspectY = TextMetricW->tmDigitizedAspectY;

    TextMetricA->tmFirstChar        = TextMetricW->tmStruckOut;
    TextMetricA->tmLastChar         = ML_MIN(0xFF, TextMetricW->tmLastChar);
    TextMetricA->tmDefaultChar      = TextMetricW->tmDefaultChar;
    TextMetricA->tmBreakChar        = TextMetricW->tmBreakChar;

    TextMetricA->tmItalic           = TextMetricW->tmItalic;
    TextMetricA->tmUnderlined       = TextMetricW->tmUnderlined;
    TextMetricA->tmStruckOut        = TextMetricW->tmStruckOut;
    TextMetricA->tmPitchAndFamily   = TextMetricW->tmPitchAndFamily;
    TextMetricA->tmCharSet          = TextMetricW->tmCharSet;
}

int NTAPI LeEnumFontFamiliesExA(HDC hdc, LPLOGFONTA lpLogfont, FONTENUMPROCA lpProc, LPARAM lParam, DWORD dwFlags)
{
    ULONG_PTR           Charset;
    LOGFONTW            lf;
    PLeGlobalData       GlobalData = LeGetGlobalData();
    GDI_ENUM_FONT_PARAM Param;

    Param.Callback      = lpProc;
    Param.GlobalData    = GlobalData;
    Param.lParam        = lParam;

    ConvertAnsiLogfontToUnicode(&lf, lpLogfont);

    return LeEnumFontFamiliesExW(hdc, &lf,
                [](CONST LOGFONTW *lf, CONST TEXTMETRICW *TextMetricW, DWORD FontType, LPARAM param) -> INT
                {
                    ENUMLOGFONTEXA          EnumLogFontA;
                    LPENUMLOGFONTEXW        EnumLogFontW;
                    PGDI_ENUM_FONT_PARAM    EnumParam;
                    PTEXT_METRIC_INTERNAL   TextMetric;
                    TEXTMETRICA             TextMetricA;
                    PTEXTMETRICA            tma;

                    TextMetric = FIELD_BASE(TextMetricW, TEXT_METRIC_INTERNAL, TextMetricW);
                    EnumParam = (PGDI_ENUM_FONT_PARAM)param;

                    EnumLogFontW = (LPENUMLOGFONTEXW)lf;
                    ConvertUnicodeLogfontToAnsi(&EnumLogFontA.elfLogFont, &EnumLogFontW->elfLogFont);

                    RtlUnicodeToMultiByteN((PSTR)EnumLogFontA.elfFullName, sizeof(EnumLogFontA.elfFullName), nullptr, EnumLogFontW->elfFullName, (StrLengthW(EnumLogFontW->elfFullName) + 1) * sizeof(WCHAR));
                    RtlUnicodeToMultiByteN((PSTR)EnumLogFontA.elfScript, sizeof(EnumLogFontA.elfScript), nullptr, EnumLogFontW->elfScript, (StrLengthW(EnumLogFontW->elfScript) + 1) * sizeof(WCHAR));
                    RtlUnicodeToMultiByteN((PSTR)EnumLogFontA.elfStyle, sizeof(EnumLogFontA.elfStyle), nullptr, EnumLogFontW->elfStyle, (StrLengthW(EnumLogFontW->elfStyle) + 1) * sizeof(WCHAR));

                    //EnumParam->GlobalData->GetTextMetricsAFromLogFont(&TextMetricA, lf);

                    if (TextMetric->VerifyMagic() == FALSE)
                    {
                        ConvertUnicodeTextMetricToAnsi(&TextMetricA, TextMetricW);
                        tma = &TextMetricA;
                    }
                    else
                    {
                        tma = &TextMetric->TextMetricA;
                    }

                    return ((FONTENUMPROCA)(EnumParam->Callback))(&EnumLogFontA.elfLogFont, tma, FontType, EnumParam->lParam);
                },
                (LPARAM)&Param,
                dwFlags
            );
}

int NTAPI LeEnumFontFamiliesA(HDC hdc, PCSTR lpszFamily, FONTENUMPROCA lpProc, LPARAM lParam)
{
    LOGFONTA lf;

    ZeroMemory(&lf, sizeof(lf));

    lf.lfCharSet = DEFAULT_CHARSET;
    StrCopyA(lf.lfFaceName, lpszFamily);

    return LeEnumFontFamiliesExA(hdc, &lf, lpProc, lParam, 0);
}

int NTAPI LeEnumFontFamiliesW(HDC hdc, PCWSTR lpszFamily, FONTENUMPROCW lpProc, LPARAM lParam)
{
    LOGFONTW lf;

    ZeroMemory(&lf, sizeof(lf));

    lf.lfCharSet = DEFAULT_CHARSET;
    StrCopyW(lf.lfFaceName, lpszFamily);

    return LeEnumFontFamiliesExW(hdc, &lf, lpProc, lParam, 0);
}

int NTAPI LeEnumFontsA(HDC hDC, PCSTR lpFaceName, FONTENUMPROCA lpProc, LPARAM lParam)
{
    LOGFONTA LogFont;

    ZeroMemory(&LogFont, sizeof(LogFont));
    LogFont.lfCharSet = DEFAULT_CHARSET;

    LogFont.lfFaceName[0] = 0;
    StrCopyA(LogFont.lfFaceName, lpFaceName);

    return LeEnumFontFamiliesExA(hDC, &LogFont, lpProc, lParam, 0);
}

int NTAPI LeEnumFontsW(HDC hDC, PCWSTR lpFaceName, FONTENUMPROCW lpProc, LPARAM lParam)
{
    LOGFONTW LogFont;

    ZeroMemory(&LogFont, sizeof(LogFont));
    LogFont.lfCharSet = DEFAULT_CHARSET;

    LogFont.lfFaceName[0] = 0;
    StrCopyW(LogFont.lfFaceName, lpFaceName);

    return LeEnumFontFamiliesExW(hDC, &LogFont, lpProc, lParam, 0);
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

    if (EnumLogFont != nullptr && IsGdiHookBypassed() == FALSE) LOOP_ONCE
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
    PVOID NtGdiHfontCreate, Fms;

    *(PVOID *)&GdiGetCodePage = GetRoutineAddress(Gdi32, "GdiGetCodePage");

    NtGdiHfontCreate = FindNtGdiHfontCreate(Gdi32);
    if (NtGdiHfontCreate == nullptr)
        return STATUS_NOT_FOUND;

    RtlInitializeCriticalSectionAndSpinCount(&HookRoutineData.Gdi32.GdiLock, 4000);

    if (HookStub.StubNtUserCreateWindowEx != nullptr)
    {
        InitFontCharsetInfo();
    }

    //Fms = Ldr::LoadDll(L"fms.dll");
    //if (Fms == nullptr)
    //{
    //    return STATUS_DLL_NOT_FOUND;
    //}
    //LdrAddRefDll(LDR_ADDREF_DLL_PIN, Fms);

    Mp::PATCH_MEMORY_DATA p[] =
    {
        LeHookFromEAT(Gdi32, GDI32, GetStockObject),
        LeHookFromEAT(Gdi32, GDI32, DeleteObject),
        //LeHookFromEAT(Gdi32, GDI32, CreateFontIndirectExW),
        LeHookFromEAT(Gdi32, GDI32, CreateCompatibleDC),
        LeHookFromEAT(Gdi32, GDI32, EnumFontFamiliesExA),
        LeHookFromEAT(Gdi32, GDI32, EnumFontFamiliesExW),
        LeHookFromEAT(Gdi32, GDI32, EnumFontsW),
        LeHookFromEAT(Gdi32, GDI32, EnumFontsA),

        LeHookFromEAT2(Gdi32, GDI32, EnumFontFamiliesA),
        LeHookFromEAT2(Gdi32, GDI32, EnumFontFamiliesW),

        LeFunctionJump(NtGdiHfontCreate),

        //Mp::MemoryPatchVa((ULONG_PTR)LeFmsEnumFontFamiliesExW, sizeof(ULONG_PTR), LookupImportTable(Fms, "GDI32.dll", GDI32_EnumFontFamiliesExW)),

        //Mp::FunctionJumpVa(LookupExportTable(Gdi32, GDI32_SelectObject), LeSelectObject, &StubSelectObject),
    };

    return Mp::PatchMemory(p, countof(p));
}

NTSTATUS LeGlobalData::UnHookGdi32Routines()
{
    Mp::RestoreMemory(HookStub.StubGetStockObject);
    Mp::RestoreMemory(HookStub.StubDeleteObject);
    Mp::RestoreMemory(HookStub.StubCreateCompatibleDC);
    Mp::RestoreMemory(HookStub.StubEnumFontFamiliesExA);
    Mp::RestoreMemory(HookStub.StubEnumFontFamiliesExW);
    Mp::RestoreMemory(HookStub.StubEnumFontsA);
    Mp::RestoreMemory(HookStub.StubEnumFontsW);
    Mp::RestoreMemory(HookStub.StubNtGdiHfontCreate);

    return 0;
}
