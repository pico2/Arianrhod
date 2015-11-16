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

//
// Conversions between pixels and DIPs.
//
FLOAT DWriteRender::PixelsToDipsX(LONG_PTR x)
{
    return x * 96.0f / this->dpiX;
}

FLOAT DWriteRender::PixelsToDipsY(LONG_PTR y)
{
    return y * 96.0f / this->dpiY;
}

LONG_PTR DWriteRender::DipsToPixelsX(FLOAT x)
{
    FLOAT pixels = x * this->dpiX * (1 / 96.0f);
    return (LONG_PTR)((pixels + 0.5f));
}

LONG_PTR DWriteRender::DipsToPixelsY(FLOAT y)
{
    FLOAT pixels = y * this->dpiY * (1 / 96.0f);
    return (LONG_PTR)((pixels + 0.5f));
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

NTSTATUS DWriteRender::Initialize(PCWSTR FaceName, ULONG_PTR FontSize)
{
    NTSTATUS                hr;
    ID2D1Factory*           factory;
    IDWriteFactory*         dwrite;
    IDWriteTextFormat*      textFormat;
    IDWriteGdiInterop*      gdiInterop;
    IDWriteRenderingParams* renderingParams;
    IDWriteFont*            font;
    DWRITE_FONT_METRICS     fontMetric;

    factory = nullptr;
    dwrite = nullptr;
    gdiInterop = nullptr;
    textFormat = nullptr;

    hr = S_OK;

    LOOP_ONCE
    {
        hr = D2D1CreateFactory(D2D1_FACTORY_TYPE_SINGLE_THREADED, &factory);
        FAIL_BREAK(hr);

        factory->GetDesktopDpi(&this->dpiX, &this->dpiY);

        hr = DWriteCreateFactory(DWRITE_FACTORY_TYPE_SHARED, __uuidof(IDWriteFactory), (IUnknown **)&dwrite);
        FAIL_BREAK(hr);

        hr = dwrite->CreateTextFormat(
                FaceName,
                nullptr,
                DWRITE_FONT_WEIGHT_NORMAL,
                DWRITE_FONT_STYLE_NORMAL,
                DWRITE_FONT_STRETCH_NORMAL,
                PixelsToDipsY(FontSize),
                L"",
                &textFormat
            );
        FAIL_BREAK(hr);

        this->renderTargetSize = textFormat->GetFontSize();
        this->fontEmSize = this->renderTargetSize;
        this->fontHeight = FontSize;

        hr = dwrite->GetGdiInterop(&gdiInterop);
        FAIL_BREAK(hr);

        LOGFONTW lf =
        {
            0,
            0,
            0,
            0,
            FW_NORMAL,
            FALSE,
            FALSE,
            FALSE,
            GB2312_CHARSET,
            OUT_DEFAULT_PRECIS,
            CLIP_DEFAULT_PRECIS,
            CLEARTYPE_NATURAL_QUALITY,
            FIXED_PITCH,
        };

        CopyMemory(&lf.lfFaceName, FaceName, sizeof(lf.lfFaceName));

        hr = gdiInterop->CreateFontFromLOGFONT(&lf, &font);
        FAIL_BREAK(hr);

        font->GetMetrics(&fontMetric);

        FLOAT ratio = textFormat->GetFontSize() / fontMetric.designUnitsPerEm;
        this->renderTargetSize = (fontMetric.ascent + fontMetric.descent + fontMetric.lineGap) * ratio;

        hr = font->CreateFontFace(&this->fontFace);
        SafeReleaseT(font);
        FAIL_BREAK(hr);

        FontSize = DipsToPixelsY(this->renderTargetSize);
        hr = gdiInterop->CreateBitmapRenderTarget(nullptr, FontSize, FontSize, &this->renderTarget);
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
    SafeReleaseT(textFormat);

    return hr;
}

NTSTATUS DWriteRender::DrawRenderTarget(UINT16 glyphIndice, PRECT blackBox)
{
    DWRITE_GLYPH_RUN run;

    run.fontFace        = this->fontFace;
    run.fontEmSize      = this->fontEmSize;
    run.glyphCount      = 1;
    run.glyphIndices    = &glyphIndice;
    run.glyphAdvances   = nullptr;
    run.glyphOffsets    = nullptr;
    run.isSideways      = FALSE;
    run.bidiLevel       = 0;

    FAIL_RETURN(this->renderTarget->DrawGlyphRun(
        (this->renderTargetSize - this->fontEmSize) / 2,
        this->fontEmSize,
        DWRITE_MEASURING_MODE_NATURAL,
        &run,
        this->renderingParams,
        RGB(255, 255, 255),
        blackBox
    ));

    //MessageBoxW(nullptr, ml::String::Format(L"%d %d %d %d", *blackBox), 0, 64);

    return STATUS_SUCCESS;
}

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

NTSTATUS DWriteRender::DrawRune(WCHAR ch, ULONG_PTR Color, PVOID Buffer, ULONG_PTR OutputStride)
{
    UINT32      codePoint;
    UINT16      glyphIndice;
    RECT        blackBox;
    LONG_PTR    stride, height, x, y, size;
    PBYTE       outline, out, pixels;
    HDC         dc;
    HBITMAP     bitmap;
    BITMAP      bmp;
    BITMAPINFO  bmi;
    IMAGE_BITMAP_HEADER header;

    codePoint = ch;
    FAIL_RETURN(this->fontFace->GetGlyphIndices(&codePoint, 1, &glyphIndice));
    FAIL_RETURN(this->DrawRenderTarget(glyphIndice, &blackBox));

    //SaveToBmpFile();

    dc = this->renderTarget->GetMemoryDC();

    bitmap = (HBITMAP)(HBITMAP)GetCurrentObject(dc, OBJ_BITMAP);
    GetObjectW(bitmap, sizeof(bmp), &bmp);
    InitBitmapHeader(&header, bmp.bmWidth, bmp.bmHeight, bmp.bmBitsPixel, &stride);

    pixels = (PBYTE)AllocStack(header.FileSize);

    bmi.bmiHeader.biSize = sizeof(bmi.bmiHeader);
    bmi.bmiHeader.biWidth = bmp.bmWidth;
    bmi.bmiHeader.biHeight = bmp.bmHeight;
    bmi.bmiHeader.biPlanes = bmp.bmPlanes;
    bmi.bmiHeader.biBitCount = bmp.bmBitsPixel;
    bmi.bmiHeader.biClrUsed = 0;
    bmi.bmiHeader.biCompression = BI_RGB;
    bmi.bmiHeader.biSizeImage = header.FileSize;
    bmi.bmiHeader.biClrImportant = 0;

    GetDIBits(dc, bitmap, 0, bmp.bmHeight, pixels, &bmi, DIB_RGB_COLORS);

    height = blackBox.bottom - blackBox.top;

    //size = DipsToPixelsY(this->renderTargetSize);
    size = this->fontHeight;

    if (height > size || blackBox.right - blackBox.left > size)
        DebugBreakPoint();

    outline = (PBYTE)AllocStack(size * size);
    ZeroMemory(outline, size * size);

    y = blackBox.top - 2;
    out = outline + y * size + blackBox.left;
    pixels += y * stride;

    for (LONG_PTR h = height; h != 0; --h)
    {
        COLORREF* i = (COLORREF *)pixels + blackBox.left;
        PBYTE o = out;

        for (LONG_PTR w = size; w != 0; --w)
        {
            *o++ = FontLumaTable[RGBA_GetRValue(*i++)];
        }

        pixels += stride;
        out += size;
    }

    out = (PBYTE)Buffer;
    for (LONG_PTR h = size; h != 0; --h)
    {
        PUSHORT o = (PUSHORT)out;
        for (LONG_PTR w = size; w != 0; --w)
        {
            ULONG c = *outline++;

            if (c == 0)
                continue;

            *o++ = (c << 12) | Color;
        }

        out += OutputStride;
    }

    return STATUS_SUCCESS;
}
