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
    NTSTATUS RenderRune(WCHAR ch, PVOID Buffer, PULONG_PTR OutputSize);

protected:
    IDWriteBitmapRenderTarget*  renderTarget;
    IDWriteRenderingParams*     renderingParams;
};

#endif // _DWRITERENDER_H_e14e1038_3d82_475d_96c6_c38253ae4232_
