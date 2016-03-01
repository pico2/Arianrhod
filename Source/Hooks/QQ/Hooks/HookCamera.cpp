#include "Hooks.h"
#include <gdiplus.h>

using namespace Gdiplus;

struct ScreenShotContext : public TEB_ACTIVE_FRAME
{
    static const ULONG_PTR magic = TAG4('SSCT');

    Bitmap* screenshot;
    HBITMAP memBmp;
    BOOL    endCapture;
    REAL    sx;
    REAL    sy;

    static ScreenShotContext* Get()
    {
        return (ScreenShotContext *)FindThreadFrame(magic);
    }

    ScreenShotContext(Bitmap* screenshot, HBITMAP memBmp, REAL sx, REAL sy) : TEB_ACTIVE_FRAME(magic)
    {
        this->endCapture    = FALSE;
        this->memBmp        = memBmp;
        this->screenshot    = screenshot;
        this->sx            = sx;
        this->sy            = sy;
        this->Push();
    }

    ~ScreenShotContext()
    {
        DeleteObject(this->memBmp);
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

        if (new ScreenShotContext(Bitmap::FromHBITMAP(memBmp, nullptr), memBmp, sx, sy) != nullptr)
            memBmp = nullptr;
    }

    if (memBmp != nullptr)
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

HANDLE CDECL CameraCreateTexture(LONG_PTR width, LONG_PTR height)
{
    ScreenShotContext* context = ScreenShotContext::Get();

    if (context != nullptr && context->endCapture)
    {
        width *= context->sx;
        height *= context->sy;
    }

    return xGraphic32::CreateTexture(width, height);
}

BOOL CDECL CameraCopyTexture(HANDLE dest, const RECT& dstrc, HANDLE src, const RECT& srcrc)
{
    ScreenShotContext* context = ScreenShotContext::Get();

    if (context == nullptr || context->endCapture == FALSE)
        return xGraphic32::CopyTexture(dest, dstrc, src, srcrc);

    BOOL success;
    RECT dstrc1, srcrc1;

    SIZE textureSize;
    REAL screenWidth = context->screenshot->GetWidth();
    REAL screenHeight = context->screenshot->GetHeight();

    xGraphic32::GetTextureSize(src, &textureSize);

    dstrc1.left     = screenWidth * dstrc.left / textureSize.cx;
    dstrc1.right    = screenWidth * dstrc.right / textureSize.cx;
    dstrc1.top      = screenHeight * dstrc.top / textureSize.cy;
    dstrc1.bottom   = screenHeight * dstrc.bottom / textureSize.cy;

    srcrc1.left     = screenWidth * srcrc.left / textureSize.cx;
    srcrc1.right    = screenWidth * srcrc.right / textureSize.cx;
    srcrc1.top      = screenHeight * srcrc.top / textureSize.cy;
    srcrc1.bottom   = screenHeight * srcrc.bottom / textureSize.cy;

    src = Util::Texture::HBitmapToTexture(context->memBmp);
    HANDLE rotated = xGraphic32::RotateTexture(src, 1);

    success = xGraphic32::CopyTexture(dest, dstrc1, rotated, srcrc1);

    xGraphic32::ReleaseTexture(src);
    xGraphic32::ReleaseTexture(rotated);

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
