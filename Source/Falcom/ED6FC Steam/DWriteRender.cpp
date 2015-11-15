#include "DWriteRender.h"

DWriteRender::DWriteRender()
{
    this->renderTarget = nullptr;
    this->renderingParams = nullptr;
}

DWriteRender::~DWriteRender()
{
    SafeReleaseT(this->renderTarget);
    SafeReleaseT(this->renderingParams);
}

NTSTATUS DWriteRender::Initialize(PCWSTR FaceName, ULONG_PTR FontSize)
{
    NTSTATUS hr;
    PBYTE                   fontSize;
    ID2D1Factory*           factory;
    IDWriteFactory*         dwrite;
    IDWriteGdiInterop*      gdiInterop;
    IDWriteRenderingParams* renderingParams;

    factory = nullptr;
    dwrite = nullptr;
    gdiInterop = nullptr;

    hr = S_OK;

    LOOP_ONCE
    {
        //FAIL_BREAK(D2D1CreateFactory(D2D1_FACTORY_TYPE_SINGLE_THREADED, &factory));
        FAIL_BREAK(DWriteCreateFactory(DWRITE_FACTORY_TYPE_SHARED, __uuidof(IDWriteFactory), (IUnknown **)&dwrite));
        FAIL_BREAK(dwrite->GetGdiInterop(&gdiInterop));
        FAIL_BREAK(gdiInterop->CreateBitmapRenderTarget(nullptr, FontSize * 2, FontSize * 2, &this->renderTarget));
        FAIL_BREAK(dwrite->CreateRenderingParams(&renderingParams));

        hr = dwrite->CreateCustomRenderingParams(
                renderingParams->GetGamma(),
                renderingParams->GetEnhancedContrast(),
                renderingParams->GetClearTypeLevel(),
                renderingParams->GetPixelGeometry(),
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
    this->renderTarget->DrawGlyphRun(0, 0, DWRITE_MEASURING_MODE_NATURAL, )
}
