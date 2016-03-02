#include "Hooks.h"
#include <gdiplus.h>

using namespace Gdiplus;

struct ScreenShotContext : public TEB_ACTIVE_FRAME
{
    static const ULONG_PTR magic = TAG4('SSCT');

    Bitmap* screenshot;
    BOOL    endCapture;
    REAL    sx;
    REAL    sy;

    static ScreenShotContext* Get()
    {
        return (ScreenShotContext *)FindThreadFrame(magic);
    }

    ScreenShotContext(Bitmap* screenshot, REAL sx, REAL sy) : TEB_ACTIVE_FRAME(magic)
    {
        screenshot->RotateFlip(Rotate180FlipX);

        this->endCapture    = FALSE;
        this->screenshot    = screenshot;
        this->sx            = sx;
        this->sy            = sy;
        this->Push();
    }

    ~ScreenShotContext()
    {
        delete this->screenshot;
        this->Pop();
    }
};

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

    if (desktopBmp.bmWidth == cx && desktopBmp.bmHeight == cy)
        return BitBlt(hdc, x, y, cx, cy, desktopDC, x1, y1, rop);

    memDC = CreateCompatibleDC(0);

    BITMAPINFO bmi;
    LPBYTE pBits = NULL;

    ZeroMemory(&bmi, sizeof(bmi));

    bmi.bmiHeader.biSize = sizeof(bmi.bmiHeader);
    bmi.bmiHeader.biWidth = desktopBmp.bmWidth;
    bmi.bmiHeader.biHeight = desktopBmp.bmHeight;
    bmi.bmiHeader.biPlanes = desktopBmp.bmPlanes;
    bmi.bmiHeader.biBitCount = desktopBmp.bmBitsPixel;
    bmi.bmiHeader.biCompression = BI_RGB;

    memBmp = CreateDIBSection(desktopDC, &bmi, DIB_RGB_COLORS, (LPVOID*)&pBits, NULL, 0);

    SelectObject(memDC, memBmp);

    success = BitBlt(memDC, 0, 0, desktopBmp.bmWidth, desktopBmp.bmHeight, desktopDC, 0, 0, SRCCOPY | CAPTUREBLT);

    if (success)
    {
        Bitmap desktop(memBmp, nullptr);
        Graphics g(hdc);
        REAL sx, sy;

        sx = (REAL)cx / desktopBmp.bmWidth;
        sy = (REAL)cy / desktopBmp.bmHeight;

        g.SetInterpolationMode(InterpolationModeHighQualityBicubic);
        g.ScaleTransform(sx, sy, MatrixOrderAppend);
        g.DrawImage(&desktop, 0, 0);

        sx = (REAL)desktopBmp.bmWidth / cx;
        sy = (REAL)desktopBmp.bmHeight / cy;

        new ScreenShotContext(Bitmap::FromHBITMAP(memBmp, nullptr), sx, sy);
    }

    DeleteObject(memBmp);
    DeleteDC(memDC);

    return success;
}

VOID (FASTCALL *StubCaptureWndController_EndCapture)(PVOID thiz, PVOID, BOOLEAN success, BOOLEAN resetActiveWnd);

VOID FASTCALL CaptureWndController_EndCapture(PVOID thiz, PVOID, BOOLEAN success, BOOLEAN resetActiveWnd)
{
    ScreenShotContext* context = ScreenShotContext::Get();

    if (success && context != nullptr)
    {
        context->endCapture = TRUE;
    }

    StubCaptureWndController_EndCapture(thiz, nullptr, success, resetActiveWnd);

    delete context;
}

#define ODS(...) OutputDebugStringW(ml::String::Format(L"[QQ] " __VA_ARGS__))

HANDLE CDECL CameraCreateTexture(LONG_PTR width, LONG_PTR height)
{
    ScreenShotContext* context = ScreenShotContext::Get();

    if (context != nullptr && context->endCapture)
    {
        width = ceil(context->sx * width);
        height = ceil(context->sy * height);

        ODS(L"textureSize = %d %d", width, height);
    }

    return xGraphic32::CreateTexture(width, height);
}

BOOL CDECL CameraCopyTexture(HANDLE regionTexture, const RECT& regionRect, HANDLE screenTexture, const RECT& screenRect)
{
    ScreenShotContext* context = ScreenShotContext::Get();

    if (context == nullptr || context->endCapture == FALSE)
        return xGraphic32::CopyTexture(regionTexture, regionRect, screenTexture, screenRect);

    BOOL success = FALSE;

    HBITMAP bitmap;

    if (context->screenshot->GetHBITMAP(Color(0, 0, 0, 0), &bitmap) == Gdiplus::Ok)
    {
        RECT scaledRegionRect, scaledScreenRect;

        SIZE textureSize;

        xGraphic32::GetTextureSize(regionTexture, &textureSize);

        scaledRegionRect = regionRect;
        scaledScreenRect = screenRect;

        scaledRegionRect.left     = 0;
        scaledRegionRect.right    = textureSize.cx;
        scaledRegionRect.top      = 0;
        scaledRegionRect.bottom   = textureSize.cy;

        scaledScreenRect.left     *= context->sx;
        scaledScreenRect.right    *= context->sx;
        scaledScreenRect.top      *= context->sy;
        scaledScreenRect.bottom   *= context->sy;

        ODS(L"scaledRegionRect = %d %d %d %d, %d %d", scaledRegionRect, scaledRegionRect.right - scaledRegionRect.left, scaledRegionRect.bottom - scaledRegionRect.top);
        ODS(L"scaledScreenRect = %d %d %d %d, %d %d", scaledScreenRect, scaledScreenRect.right - scaledScreenRect.left, scaledScreenRect.bottom - scaledScreenRect.top);

        screenTexture = Util::Texture::HBitmapToTexture(bitmap);

        success = xGraphic32::CopyTexture(regionTexture, scaledRegionRect, screenTexture, scaledScreenRect);

        DeleteObject(bitmap);
        xGraphic32::ReleaseTexture(screenTexture);
    }

    return success;
}

PVOID SearchCamera_CaptureWndController_EndCapture(PVOID ImageBase)
{
    static WCHAR String[] = L"CaptureWndController::EndCapture";

    return SearchStringAndReverseSearchHeader(ImageBase, String, sizeof(String) - sizeof(String[0]), 0x80);
}

NTSTATUS HookCamera(PVOID BaseAddress)
{
    GdiplusStartupInput gdiplusStartupInput;
    ULONG_PTR gdiplusToken;

    GdiplusStartup(&gdiplusToken, &gdiplusStartupInput, nullptr);

    Mp::PATCH_MEMORY_DATA Function_Camera[] =
    {
        Mp::MemoryPatchVa((ULONG64)CameraBitBlt,        sizeof(PVOID), LookupImportTable(BaseAddress, "GDI32.dll", GDI32_BitBlt)),
        Mp::MemoryPatchVa((ULONG64)CameraCreateTexture, sizeof(PVOID), LookupImportTable(BaseAddress, "xGraphic32.dll", "CreateTexture")),
        Mp::MemoryPatchVa((ULONG64)CameraCopyTexture,   sizeof(PVOID), LookupImportTable(BaseAddress, "xGraphic32.dll", "CopyTexture")),

        Mp::FunctionJumpVa(SearchCamera_CaptureWndController_EndCapture(BaseAddress), CaptureWndController_EndCapture, &StubCaptureWndController_EndCapture),
    };

    return Mp::PatchMemory(Function_Camera, countof(Function_Camera), BaseAddress);
}
