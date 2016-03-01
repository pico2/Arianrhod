#include "Hooks.h"
#include <gdiplus.h>

using namespace Gdiplus;

BOOL
NTAPI
CameraBitBlt(
    HDC     hdc,
    int     x,
    int     y,
    int     cx,
    int     cy,
    HDC     desktopDC,
    int     x1,
    int     y1,
    ULONG   rop
)
{
    BOOL        success;
    RECT        workArea;
    BITMAP      desktopBmp;
    HDC         memDC;
    HBITMAP     memBmp;

    GetObjectW(GetCurrentObject(desktopDC, OBJ_BITMAP), sizeof(desktopBmp), &desktopBmp);
    memDC = CreateCompatibleDC(0);
    memBmp = CreateCompatibleBitmap(desktopDC, desktopBmp.bmWidth, desktopBmp.bmHeight);
    SelectObject(memDC, memBmp);

    success = BitBlt(memDC, 0, 0, desktopBmp.bmWidth, desktopBmp.bmHeight, desktopDC, 0, 0, SRCCOPY | CAPTUREBLT);

    if (success)
    {
        Bitmap desktop(memBmp, nullptr);
        Graphics g(hdc);

        g.SetInterpolationMode(InterpolationModeHighQualityBicubic);
        g.ScaleTransform((REAL)cx / desktopBmp.bmWidth, (REAL)cy / desktopBmp.bmHeight, MatrixOrderAppend);
        g.DrawImage(&desktop, 0, 0);
    }

    DeleteObject(memBmp);
    DeleteDC(memDC);

    return success;
}

NTSTATUS HookCamera(PVOID BaseAddress)
{
    GdiplusStartupInput gdiplusStartupInput;
    ULONG_PTR gdiplusToken;

    GdiplusStartup(&gdiplusToken, &gdiplusStartupInput, nullptr);

    Mp::PATCH_MEMORY_DATA Function_Camera[] =
    {
        Mp::MemoryPatchVa((ULONG64)CameraBitBlt, sizeof(PVOID), LookupImportTable(BaseAddress, "GDI32.dll", GDI32_BitBlt)),
    };

    return Mp::PatchMemory(Function_Camera, countof(Function_Camera), BaseAddress);
}
