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
    NTSTATUS DrawRune(WCHAR ch, ULONG_PTR Color, PVOID Buffer, ULONG_PTR OutputStride);

    FLOAT PixelsToDipsX(LONG_PTR x);
    FLOAT PixelsToDipsY(LONG_PTR y);
    LONG_PTR DipsToPixelsX(FLOAT x);
    LONG_PTR DipsToPixelsY(FLOAT y);

protected:
    NTSTATUS DrawRenderTarget(UINT16 glyphIndice, PRECT blackBox);
    VOID SaveToBmpFile();

protected:
    IDWriteBitmapRenderTarget*  renderTarget;
    IDWriteRenderingParams*     renderingParams;
    IDWriteFontFace*            fontFace;
    FLOAT                       fontEmSize;
    FLOAT                       fontHeight;
    FLOAT                       renderTargetSize;
    FLOAT                       dpiX, dpiY;
};

#endif // _DWRITERENDER_H_e14e1038_3d82_475d_96c6_c38253ae4232_
