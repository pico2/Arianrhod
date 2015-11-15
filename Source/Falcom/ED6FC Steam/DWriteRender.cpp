#include "DWriteRender.h"

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
    IDWriteGdiInterop*      gdiInterop;
    IDWriteRenderingParams* renderingParams;
    IDWriteFont*            font;
    FLOAT                   dpiX, dpiY;

    factory = nullptr;
    dwrite = nullptr;
    gdiInterop = nullptr;

    hr = S_OK;

    LOOP_ONCE
    {
        hr = D2D1CreateFactory(D2D1_FACTORY_TYPE_SINGLE_THREADED, &factory);
        FAIL_BREAK(hr);

        factory->GetDesktopDpi(&dpiX, &dpiY);

        hr = DWriteCreateFactory(DWRITE_FACTORY_TYPE_SHARED, __uuidof(IDWriteFactory), (IUnknown **)&dwrite);
        FAIL_BREAK(hr);

        hr = dwrite->GetGdiInterop(&gdiInterop);
        FAIL_BREAK(hr);

        this->fontEmSize = FontSize / (dpiY / 96);

        LOGFONTW lf =
        {
            (LONG)FontSize,
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
            L"ºÚÌå"
        };

        hr = gdiInterop->CreateFontFromLOGFONT(&lf, &font);
        FAIL_BREAK(hr);

        hr = font->CreateFontFace(&this->fontFace);
        SafeReleaseT(font);
        FAIL_BREAK(hr);

        hr = gdiInterop->CreateBitmapRenderTarget(nullptr, FontSize * 2, FontSize * 2, &this->renderTarget);
        FAIL_BREAK(hr);

        hr = dwrite->CreateRenderingParams(&renderingParams);
        FAIL_BREAK(hr);

        hr = dwrite->CreateCustomRenderingParams(
                renderingParams->GetGamma(),
                renderingParams->GetEnhancedContrast(),
                renderingParams->GetClearTypeLevel(),
                DWRITE_PIXEL_GEOMETRY_FLAT,
                DWRITE_RENDERING_MODE_NATURAL,
                &this->renderingParams
            );

        SafeReleaseT(renderingParams);
    }

    SafeReleaseT(factory);
    SafeReleaseT(dwrite);
    SafeReleaseT(gdiInterop);

    return hr;
}

NTSTATUS DWriteRender::RenderRune(WCHAR ch, PVOID Buffer, PULONG_PTR OutputSize)
{
    DWRITE_GLYPH_RUN run;

    run.fontFace = this->fontFace;
    run.fontEmSize = this->fontEmSize;
    run.glyphCount = 1;
    run.glyphIndices = (PUSHORT)&ch;
    run.glyphAdvances = nullptr;
    run.glyphOffsets = nullptr;
    run.isSideways = FALSE;
    run.bidiLevel = 0;

    this->renderTarget->DrawGlyphRun(0, 0, DWRITE_MEASURING_MODE_NATURAL, &run, this->renderingParams, RGB(255, 255, 255), nullptr);

    HDC dc = this->renderTarget->GetMemoryDC();

    BYTE buffer[0x10000];

    GetBitmapBits((HBITMAP)GetCurrentObject(dc, OBJ_BITMAP), sizeof(buffer), buffer);

    return STATUS_SUCCESS;
}
