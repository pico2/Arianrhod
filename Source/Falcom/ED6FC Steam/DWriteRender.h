#ifndef _DWRITERENDER_H_e14e1038_3d82_475d_96c6_c38253ae4232_
#define _DWRITERENDER_H_e14e1038_3d82_475d_96c6_c38253ae4232_

#include "ml.h"
#include <d2d1.h>
#include <dwrite.h>

class DWriteRender
{
public:
    DWriteRender();
    ~DWriteRender();

public:
    NTSTATUS Initialize(PCWSTR FaceName, ULONG_PTR FontSize);
    NTSTATUS DrawRune(WCHAR ch, ULONG_PTR Color, PVOID Buffer, ULONG_PTR OutputStride, PULONG_PTR runeWidth);

    template <typename T>
    FLOAT PixelsToDipsX(T x)
    {
        return x * 96.0f / this->dpiX;
    }

    template <typename T>
    FLOAT PixelsToDipsY(T y)
    {
        return y * 96.0f / this->dpiY;
    }

    LONG_PTR DipsToPixelsX(FLOAT x)
    {
        FLOAT pixels = x * this->dpiX * (1 / 96.0f);
        return (LONG_PTR)((pixels + 0.5f));
    }

    LONG_PTR DipsToPixelsY(FLOAT y)
    {
        FLOAT pixels = y * this->dpiY * (1 / 96.0f);
        return (LONG_PTR)((pixels + 0.5f));
    }

protected:
    NTSTATUS DrawRenderTarget(UINT16 glyphIndice, PRECT blackBox);
    VOID SaveToBmpFile();

protected:
    IDWriteBitmapRenderTarget*  renderTarget;
    IDWriteRenderingParams*     renderingParams;
    IDWriteFontFace*            fontFace;
    LONG_PTR                    fontHeight;
    FLOAT                       baselineY;
    FLOAT                       fontEmSize;
    FLOAT                       maxFontEmSize;
    FLOAT                       renderTargetSize;
    FLOAT                       dpiX, dpiY;
};

#endif // _DWRITERENDER_H_e14e1038_3d82_475d_96c6_c38253ae4232_
