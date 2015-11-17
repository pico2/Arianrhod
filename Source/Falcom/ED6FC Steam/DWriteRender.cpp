#include "DWriteRender.h"

static BYTE FontLumaTable[] =
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

VOID DWriteRender::SaveToBmpFile()
{
    HDC dc = this->renderTarget->GetMemoryDC();

    PBYTE buffer;
    HBITMAP bitmap = (HBITMAP)(HBITMAP)GetCurrentObject(dc, OBJ_BITMAP);
    BITMAP bmp;
    IMAGE_BITMAP_HEADER header;
    BITMAPINFO bmi;

    GetObjectW(bitmap, sizeof(bmp), &bmp);
    InitBitmapHeader(&header, bmp.bmWidth, bmp.bmHeight, bmp.bmBitsPixel);

    bmi.bmiHeader.biSize = sizeof(bmi.bmiHeader);
    bmi.bmiHeader.biWidth = bmp.bmWidth;
    bmi.bmiHeader.biHeight = bmp.bmHeight;
    bmi.bmiHeader.biPlanes = bmp.bmPlanes;
    bmi.bmiHeader.biBitCount = bmp.bmBitsPixel;
    bmi.bmiHeader.biClrUsed = 0;
    bmi.bmiHeader.biCompression = BI_RGB;
    bmi.bmiHeader.biSizeImage = header.FileSize;
    bmi.bmiHeader.biClrImportant = 0;

    buffer = (PBYTE)AllocStack(header.FileSize);

    GetDIBits(dc, bitmap, 0, bmp.bmHeight, buffer, &bmi, DIB_RGB_COLORS);

    NtFileDisk bin;
    bin.Create(L"d:\\desktop\\picture.bmp");
    bin.Write(&header, sizeof(header));
    bin.Write(buffer, header.FileSize);
    bin.Seek(header.FileSize);
    bin.SetEndOfFile();
}

DWriteRender::DWriteRender()
{
    this->renderTarget = nullptr;
    this->renderingParams = nullptr;
    this->fontFace = nullptr;
}

DWriteRender::~DWriteRender()
{
    SafeReleaseT(this->renderTarget);
    SafeReleaseT(this->renderingParams);
    SafeReleaseT(this->fontFace);
}

NTSTATUS DWriteRender::Initialize(PCWSTR FontPath, ULONG_PTR FontSize)
{
    NTSTATUS                hr;
    ID2D1Factory*           factory;
    IDWriteFactory*         dwrite;
    IDWriteGdiInterop*      gdiInterop;
    IDWriteRenderingParams* renderingParams;
    IDWriteFontFile*        fontFile;
    DWRITE_FONT_METRICS     fontMetric;

    factory         = nullptr;
    dwrite          = nullptr;
    gdiInterop      = nullptr;
    fontFile        = nullptr;

    hr = S_OK;

    LOOP_ONCE
    {
        hr = D2D1CreateFactory(D2D1_FACTORY_TYPE_SINGLE_THREADED, &factory);
        FAIL_BREAK(hr);

        factory->GetDesktopDpi(&this->dpiX, &this->dpiY);

        hr = DWriteCreateFactory(DWRITE_FACTORY_TYPE_SHARED, __uuidof(IDWriteFactory), (IUnknown **)&dwrite);
        FAIL_BREAK(hr);

        hr = dwrite->CreateFontFileReference(FontPath, nullptr, &fontFile);
        FAIL_BREAK(hr);

        hr = dwrite->CreateFontFace(DWRITE_FONT_FACE_TYPE_TRUETYPE, 1, &fontFile, 0, DWRITE_FONT_SIMULATIONS_NONE, &fontFace);
        if (hr == DWRITE_E_FILEFORMAT)
        {
            hr = dwrite->CreateFontFace(DWRITE_FONT_FACE_TYPE_TRUETYPE_COLLECTION, 1, &fontFile, 0, DWRITE_FONT_SIMULATIONS_NONE, &fontFace);
        }
        FAIL_BREAK(hr);

        this->fontEmSize = PixelsToDipsY(FontSize);
        this->fontHeight = FontSize;
        hr = dwrite->GetGdiInterop(&gdiInterop);
        FAIL_BREAK(hr);

        fontFace->GetMetrics(&fontMetric);

        FLOAT ratio = this->fontEmSize / fontMetric.designUnitsPerEm;
        this->maxFontEmSize = (fontMetric.ascent + fontMetric.descent + fontMetric.lineGap) * ratio;
        this->renderTargetSize = this->maxFontEmSize;
        this->baselineY = fontMetric.ascent * ratio;

        hr = gdiInterop->CreateBitmapRenderTarget(nullptr, this->maxFontEmSize, this->maxFontEmSize, &this->renderTarget);
        FAIL_BREAK(hr);

        hr = dwrite->CreateRenderingParams(&renderingParams);
        FAIL_BREAK(hr);

        hr = dwrite->CreateCustomRenderingParams(
                renderingParams->GetGamma(),
                renderingParams->GetEnhancedContrast(),
                renderingParams->GetClearTypeLevel(),
                DWRITE_PIXEL_GEOMETRY_FLAT,
                DWRITE_RENDERING_MODE_NATURAL_SYMMETRIC,
                &this->renderingParams
            );

        SafeReleaseT(renderingParams);
    }

    SafeReleaseT(factory);
    SafeReleaseT(dwrite);
    SafeReleaseT(gdiInterop);

    return hr;
}

NTSTATUS DWriteRender::DrawRenderTarget(UINT16 glyphIndice, PRECT blackBox)
{
    DWRITE_GLYPH_RUN run;
    HDC dc;
    SIZE size;

    run.fontFace        = this->fontFace;
    run.fontEmSize      = this->fontEmSize - PixelsToDipsY(1);
    run.glyphCount      = 1;
    run.glyphIndices    = &glyphIndice;
    run.glyphAdvances   = nullptr;
    run.glyphOffsets    = nullptr;
    run.isSideways      = FALSE;
    run.bidiLevel       = 0;

    dc = this->renderTarget->GetMemoryDC();
    this->renderTarget->GetSize(&size);

    SetDCBrushColor(dc, RGB(0, 0, 0));
    SelectObject(dc, GetStockObject(BLACK_PEN));
    SelectObject(dc, GetStockObject(DC_BRUSH));
    Rectangle(dc, 0, 0, size.cx + 1, size.cy + 1);

    FAIL_RETURN(this->renderTarget->DrawGlyphRun(
        (this->renderTargetSize - this->fontEmSize) / 2,
        this->baselineY,
        DWRITE_MEASURING_MODE_NATURAL,
        &run,
        this->renderingParams,
        RGB(255, 255, 255),
        blackBox
    ));

    return STATUS_SUCCESS;
}

NTSTATUS DWriteRender::DrawRune(WCHAR ch, ULONG_PTR Color, PVOID Output, ULONG_PTR OutputStride, PULONG_PTR runeWidth)
{
    UINT32      codePoint;
    UINT16      glyphIndice;
    RECT        blackBox;
    LONG_PTR    stride, width, height, x, y, fontSize;
    PBYTE       outline, out, pixels;
    HDC         dc;
    HBITMAP     bitmap;
    BITMAP      bmp;
    IMAGE_BITMAP_HEADER header;

    BOOL show = FALSE;
    if (ch == L'½Ç')
    {
        //show = TRUE;
    }

    codePoint = ch;
    FAIL_RETURN(this->fontFace->GetGlyphIndices(&codePoint, 1, &glyphIndice));
    FAIL_RETURN(this->DrawRenderTarget(glyphIndice, &blackBox));

    if (show)
    {
        PrintConsole(L"rawrc = {%d %d %d %d}\n", blackBox);
    }

    dc = this->renderTarget->GetMemoryDC();

    bitmap = (HBITMAP)(HBITMAP)GetCurrentObject(dc, OBJ_BITMAP);
    GetObjectW(bitmap, sizeof(bmp), &bmp);
    InitBitmapHeader(&header, bmp.bmWidth, bmp.bmHeight, bmp.bmBitsPixel, &stride);

    pixels = (PBYTE)AllocStack(header.FileSize);

    GetDIBits(dc, bitmap, 0, bmp.bmHeight, pixels, (PBITMAPINFO)&header.Info, DIB_RGB_COLORS);

    blackBox.top = ML_MAX(0, blackBox.top);
    blackBox.left = ML_MAX(0, blackBox.left);
    blackBox.right = ML_MIN(blackBox.right, header.Info.Width);
    blackBox.bottom = ML_MIN(blackBox.bottom, header.Info.Height);

    width = blackBox.right - blackBox.left;
    height = blackBox.bottom - blackBox.top;

    *runeWidth = blackBox.right + blackBox.left;

    fontSize = this->fontHeight;

    if (width > fontSize)
    {
        ExceptionBox(L"width strange");
        blackBox.left += width - fontSize;
        width = blackBox.right - blackBox.left;
    }

    if (height > fontSize)
    {
        ExceptionBox(L"height strange");
        blackBox.top += height - fontSize;
        height = blackBox.bottom - blackBox.top;
    }

    if (show)
    {
        SaveToBmpFile();
        PrintConsole(L"rc = {%d %d %d %d} stride = %d w = %d h = %d fs = %d\n", blackBox, stride, width, height, fontSize);
    }

    outline = (PBYTE)AllocStack(fontSize * fontSize * 2);
    ZeroMemory(outline, fontSize * fontSize);

    auto opixels = pixels;

    pixels += (bmp.bmHeight - blackBox.top - 1) * stride + blackBox.left * sizeof(COLORREF);
    out = outline + blackBox.left;

    if (blackBox.top + height <= fontSize)
        out += blackBox.top * fontSize;

    for (LONG_PTR h = height; h != 0; --h)
    {
        COLORREF* i = (COLORREF *)pixels;
        PBYTE o = out;

        for (LONG_PTR w = width; w != 0; --w)
        {
            *o++ = FontLumaTable[RGBA_GetRValue(*i++)];
        }

        pixels -= stride;
        out += fontSize;

        if (o > out)
        {
            ExceptionBox(L"out of range");
            Ps::ExitProcess(0);
        }
    }

    out = (PBYTE)Output;
    for (LONG_PTR h = fontSize; h != 0; --h)
    {
        PUSHORT o = (PUSHORT)out - 1;
        for (LONG_PTR w = fontSize; w != 0; --w)
        {
            ULONG c = *outline++;

            ++o;
            if (c == 0)
                continue;

            *o = (c << 12) | Color;
        }

        out += OutputStride;
        if ((PBYTE)o > out)
        {
            ExceptionBox(L"out of range 2");
            Ps::ExitProcess(0);
        }
    }

    return STATUS_SUCCESS;
}
