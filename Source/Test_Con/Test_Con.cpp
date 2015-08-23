#if 1

#define _WIN32_WINNT 0x601

#pragma comment(linker,"/ENTRY:main2")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text /MERGE:.text1=.text /SECTION:.idata,ERW")
#pragma comment(linker, "/SECTION:.Amano,ERW /MERGE:.text=.Amano")
#pragma warning(disable:4995 4273 4005)

#ifndef UNICODE
    #define UNICODE
#endif

#ifndef _UNICODE
    #define _UNICODE
#endif

#define  _DECL_DLLMAIN

#include "ml.cpp"

ML_OVERLOAD_NEW

using ml::String;

#if defined(UNICODE)
    #define __WSTRING(str) L##str
    #define WSTRING(str) __WSTRING(str)
#else
    #define WSTRING(str) (str)
#endif


ULONG GetBitSetCount(ULONG Value)
{
    Value -= ((Value >> 1) & 0x55555555);
    Value  = (((Value >> 2) & 0x33333333) + (Value & 0x33333333));
    Value  = (((Value >> 4) + Value) & 0x0F0F0F0F);
    Value += (Value >> 8);
    Value += (Value>>16);
    Value &= 0x3F;

    return Value;
}

#if ML_X86

BOOL IsRunningInVMWare()
{
    BOOL Result;

    SEH_TRY
    {
        INLINE_ASM
        {
            mov     eax, 'VMXh';
            mov     ecx, 0xA;
            mov     edx, 'VX';
            in      eax, dx;
            sub     ebx, 'VMXh';
            sete    al;
            movzx   eax, al;
            mov     Result, eax;
        }
    }
    SEH_EXCEPT(EXCEPTION_EXECUTE_HANDLER)
    {
        Result = FALSE;
    }

    return Result;
}

#endif

VOID PrintLocaleDefaultAnsiCodePage()
{
    WCHAR Buffer[8];
    GetLocaleInfoW(GetUserDefaultLangID(), LOCALE_IDEFAULTANSICODEPAGE, Buffer, countof(Buffer));
    PrintConsole(L"%s\n", Buffer);
    PauseConsole();

    Ps::ExitProcess(0);
}

#include <vector>
#include <map>

using namespace std;

void quick_sort(int *array, int count)
{
    int *left, *right, base;

    left = array;
    right = &array[count - 1];

    if (left > right)
        return;

    base = *left;

    while (left < right)
    {
        while (*right >= base && left < right)
            --right;

        while (*left <= base && left < right)
            ++left;

        if (left < right)
            Swap(*left, *right);
    }

    Swap(*array, *left);

    quick_sort(array, left - array);

    ++left;
    quick_sort(left, &array[count] - left);
}

#include "iTunes/iTunes.h"

#include <dwrite.h>

#pragma comment(lib, "dwrite.lib")

class GdiTextRenderer : public IDWriteTextRenderer
{
public:
    GdiTextRenderer(
        IDWriteBitmapRenderTarget* bitmapRenderTarget,
        IDWriteRenderingParams* renderingParams
        )
        :
    cRefCount_(0),
        pRenderTarget_(bitmapRenderTarget),
        pRenderingParams_(renderingParams)
    {
        pRenderTarget_->AddRef();
        pRenderingParams_->AddRef();
    }

    GdiTextRenderer::~GdiTextRenderer()
    {
        SafeReleaseT(pRenderTarget_);
        SafeReleaseT(pRenderingParams_);
    }

    IFACEMETHOD(IsPixelSnappingDisabled)(
        __maybenull void* clientDrawingContext,
        __out BOOL* isDisabled
        )
    {
        *isDisabled = FALSE;
        return S_OK;
}

    IFACEMETHOD(GetCurrentTransform)(
        __maybenull void* clientDrawingContext,
        __out DWRITE_MATRIX* transform
        )
    {
        //forward the render target's transform
        pRenderTarget_->GetCurrentTransform(transform);
        return S_OK;
}

    IFACEMETHOD(GetPixelsPerDip)(
        __maybenull void* clientDrawingContext,
        __out FLOAT* pixelsPerDip
        )
    {
        *pixelsPerDip = pRenderTarget_->GetPixelsPerDip();
        return S_OK;
}

    IFACEMETHOD(DrawGlyphRun)(
        __maybenull void* clientDrawingContext,
        FLOAT baselineOriginX,
        FLOAT baselineOriginY,
        DWRITE_MEASURING_MODE measuringMode,
        __in DWRITE_GLYPH_RUN const* glyphRun,
        __in DWRITE_GLYPH_RUN_DESCRIPTION const* glyphRunDescription,
        IUnknown* clientDrawingEffect
        )
    {
        HRESULT hr = S_OK;

        // Pass on the drawing call to the render target to do the real work.
        RECT dirtyRect = {0};

        hr = pRenderTarget_->DrawGlyphRun(
            baselineOriginX,
            baselineOriginY,
            measuringMode,
            glyphRun,
            pRenderingParams_,
            RGB(0,200,255),
            &dirtyRect
            );


        return hr;
}

    IFACEMETHOD(DrawUnderline)(
        __maybenull void* clientDrawingContext,
        FLOAT baselineOriginX,
        FLOAT baselineOriginY,
        __in DWRITE_UNDERLINE const* underline,
        IUnknown* clientDrawingEffect
        )
    {
        // Not implemented
        return E_NOTIMPL;
}

    IFACEMETHOD(DrawStrikethrough)(
        __maybenull void* clientDrawingContext,
        FLOAT baselineOriginX,
        FLOAT baselineOriginY,
        __in DWRITE_STRIKETHROUGH const* strikethrough,
        IUnknown* clientDrawingEffect
        )
    {
        // Not implemented
        return E_NOTIMPL;
}

    IFACEMETHOD(DrawInlineObject)(
        __maybenull void* clientDrawingContext,
        FLOAT originX,
        FLOAT originY,
        IDWriteInlineObject* inlineObject,
        BOOL isSideways,
        BOOL isRightToLeft,
        IUnknown* clientDrawingEffect
        )
    {
        // Not implemented
        return E_NOTIMPL;
}

public:
    IFACEMETHOD_(unsigned long, AddRef) ()
    {
        return InterlockedIncrement(&cRefCount_);
}

    IFACEMETHOD_(unsigned long, Release) ()
    {
        long newCount = InterlockedDecrement(&cRefCount_);

        if (newCount == 0)
        {
            delete this;
            return 0;
        }
        return newCount;
}
    IFACEMETHOD(QueryInterface)(
        IID const& riid,
        void** ppvObject

        )
    {
        if (__uuidof(IDWriteTextRenderer) == riid)
        {
            *ppvObject = this;
        }
        else if (__uuidof(IDWritePixelSnapping) == riid)
        {
            *ppvObject = this;
        }
        else if (__uuidof(IUnknown) == riid)
        {
            *ppvObject = this;
        }
        else
        {
            *ppvObject = NULL;
            return E_FAIL;
        }

        return S_OK;
}

private:
    unsigned long cRefCount_;
    IDWriteBitmapRenderTarget* pRenderTarget_;
    IDWriteRenderingParams* pRenderingParams_;
};

IDWriteFactory* g_pDWriteFactory = NULL;
IDWriteTextFormat* g_pTextFormat = NULL;
IDWriteGdiInterop* g_pGdiInterop = NULL;
IDWriteTextLayout* g_pTextLayout = NULL;
IDWriteBitmapRenderTarget* g_pBitmapRenderTarget = NULL;
IDWriteRenderingParams* g_pRenderingParams = NULL;

// For our custom renderer class.
IDWriteTextRenderer* g_pGdiTextRenderer = NULL;

HRESULT DWriteCreateResources(HDC hdc, wchar_t *text, HFONT hfont)
{
    HRESULT hr = S_OK;

    // If the DirectWrite factory doesn't exist, create the resources,
    // only create these resources once.
    if (!g_pDWriteFactory)
    {
        HWND hwnd;
        RECT r;

        // DirectWrite variables.
        IDWriteFontFamily* pFontFamily = NULL;
        IDWriteFont* pFont = NULL;
        IDWriteLocalizedStrings* pFamilyNames = NULL;

        // Logical (GDI) font.
        LOGFONT lf = {};

        UINT32 length = 0;
        UINT32 index = 0;
        float fontSize = 0;

        // length of the string
        UINT32 textLength = 0;

        wchar_t *name = NULL;

        // Get a handle to the DC and the window rect.
        hwnd = WindowFromDC(hdc);
        GetClientRect(hwnd, &r);

        // Calculate the string length.
        textLength = UINT32(wcslen(text));

        // Create the DirectWrite factory.
        hr = DWriteCreateFactory(
            DWRITE_FACTORY_TYPE_SHARED,
            __uuidof(IDWriteFactory),
            reinterpret_cast<IUnknown**>(&g_pDWriteFactory)
            );

        // Create a GDI interop interface.
        if (SUCCEEDED(hr))
        {
            hr = g_pDWriteFactory->GetGdiInterop(&g_pGdiInterop);
        }

        if (SUCCEEDED(hr))
        {
            // Get a logical font from the font handle.
            GetObject(hfont, sizeof(LOGFONT), &lf);
        }

        // Convert to a DirectWrite font.
        if (SUCCEEDED(hr))
        {
            hr = g_pGdiInterop->CreateFontFromLOGFONT(&lf, &pFont);
        }

        // Get the font family.
        if (SUCCEEDED(hr))
        {
            hr = pFont->GetFontFamily(&pFontFamily);
        }

        // Get a list of localized family names.
        if (SUCCEEDED(hr))
        {
            hr = pFontFamily->GetFamilyNames(&pFamilyNames);
        }

        // Select the first locale.  This is OK, because we are not displaying the family name.
        index = 0;

        // Get the length of the family name.
        if (SUCCEEDED(hr))
        {
            hr = pFamilyNames->GetStringLength(index, &length);
        }

        if (SUCCEEDED(hr))
        {
            // Allocate a new string.
            name = new (std::nothrow) wchar_t[length+1];
		    if (name == NULL)
            {
			    hr = E_OUTOFMEMORY;
            }
        }

        // Get the actual family name.
        if (SUCCEEDED(hr))
        {
            hr = pFamilyNames->GetString(index, name, length+1);
        }

        if (SUCCEEDED(hr))
        {
            // Calculate the font size.
            fontSize = (float) -MulDiv(lf.lfHeight, 96, GetDeviceCaps(hdc, LOGPIXELSY));
        }

        // Create a text format using the converted font information.
        if (SUCCEEDED(hr))
        {
            hr = g_pDWriteFactory->CreateTextFormat(
                name,                // Font family name.
                NULL,
                pFont->GetWeight(),
                pFont->GetStyle(),
                pFont->GetStretch(),
                fontSize,
                L"en-us",
                &g_pTextFormat
                );
        }

        // Create a text layout.
        if (SUCCEEDED(hr))
        {
            hr = g_pDWriteFactory->CreateTextLayout(
                text,
                textLength,
                g_pTextFormat,
                1024.0f,
                480.0f,
                &g_pTextLayout
                );
        }

        // Underline and strikethrough are part of a LOGFONT structure, but are not
        // part of a DWrite font object so we must set them using the text layout.
        if(lf.lfUnderline)
        {
            DWRITE_TEXT_RANGE textRange = {0, textLength};
            g_pTextLayout->SetUnderline(true, textRange);
        }

        if(lf.lfStrikeOut)
        {
            DWRITE_TEXT_RANGE textRange = {0, textLength};
            g_pTextLayout->SetStrikethrough(true, textRange);
        }

        // Create a bitmap render target for our custom renderer.
        if (SUCCEEDED(hr))
        {
            hr = g_pGdiInterop->CreateBitmapRenderTarget(hdc, r.right, r.bottom, &g_pBitmapRenderTarget);
        }

        // Create default rendering params for our custom renderer.
        if (SUCCEEDED(hr))
        {
            hr = g_pDWriteFactory->CreateRenderingParams(&g_pRenderingParams);
        }

        if (SUCCEEDED(hr))
        {
            // Initialize the custom renderer class.
		    g_pGdiTextRenderer = new (std::nothrow) GdiTextRenderer(g_pBitmapRenderTarget, g_pRenderingParams);
        }

        // Clean up local interfaces.
        SafeReleaseT(pFontFamily);
        SafeReleaseT(pFont);
        SafeReleaseT(pFamilyNames);
    }

    return hr;
}

/******************************************************************
*                                                                 *
*  GdiOnPaint                                                     *
*                                                                 *
*  Draw the text using GDI and the TextOut function.              *
*                                                                 *
*                                                                 *
******************************************************************/

void GdiOnPaint(HDC hdc, wchar_t *text, HFONT hfont)
{
    HFONT hf;
    UINT32 textLength;

    textLength = UINT32(wcslen(text));

    hf = (HFONT) SelectObject(hdc, hfont);

    SetTextColor(hdc, RGB(0, 200, 255));

    TextOut(hdc, 0, 0, text, textLength);

    SelectObject(hdc, hf);
}

/******************************************************************
*                                                                 *
*  DWriteOnPaint                                                  *
*                                                                 *
*  Clears the memory DC of the bitmap render target, renders to   *
*  it using a custom text renderer, and then copies it to the     *
*  window device context using the BitBlt function.               *
*                                                                 *
******************************************************************/

HRESULT DWriteOnPaint(HDC hdc, wchar_t *text, HFONT hfont)
{
    HRESULT hr = S_OK;

    // Draw the text below the GDI text
    if (SUCCEEDED(hr))
    {
        hr = g_pTextLayout->Draw(NULL, g_pGdiTextRenderer, 0, 150);
    }

    return hr;
}

void OnPaint(HDC hdc)
{
    HRESULT hr = S_OK;

    HFONT hfont = NULL;
    long height = 0;
    HDC memoryHdc = NULL;
    SIZE size = {};

    // Set the height, equivalent to 50 em for DirectWrite.
    height = -MulDiv(200, GetDeviceCaps(hdc, LOGPIXELSY), 96);

    hfont = CreateFontW(height, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, L"Consolas");

    wchar_t dwriteText[ ] = L"Sample text using DirectWrite.";
    wchar_t gdiText[ ] = L"Sample text using GDI TextOut.";

    // The DirectWrite objects need only be created once and can be reused each time the window paints
    hr = DWriteCreateResources(hdc, dwriteText, hfont);

    // Get the memory device context, the drawing is done offscreen.
    if (SUCCEEDED(hr))
    {
        memoryHdc = g_pBitmapRenderTarget->GetMemoryDC();
        SetBoundsRect(memoryHdc, NULL, DCB_ENABLE|DCB_RESET);
    }

    // Get the size of the target.
    if (SUCCEEDED(hr))
    {
        hr = g_pBitmapRenderTarget->GetSize(&size);
    }

    // Clear the background
    if (SUCCEEDED(hr))
    {
        SetDCBrushColor(memoryHdc, 0xFFFFFF);
        SelectObject(memoryHdc, GetStockObject(NULL_PEN));
        SelectObject(memoryHdc, GetStockObject(DC_BRUSH));
        Rectangle(memoryHdc, 0, 0, size.cx + 1, size.cy + 1);
    }

    // Draw the string to the memory HDC using GDI.
    if (SUCCEEDED(hr))
    {
        GdiOnPaint(memoryHdc, gdiText, hfont);
    }

    // Draw the same string below the first to the memory HDC using DirectWrite.
    if (SUCCEEDED(hr))
    {
        hr = DWriteOnPaint(memoryHdc, dwriteText, hfont);
    }

    // Transfer from DWrite's rendering target to the window.
    BitBlt(
        hdc,
        0, 0,
        size.cx + 1, size.cy + 1,
        memoryHdc,
        0, 0,
        SRCCOPY
        );

    // If the DirectWrite drawing failed, exit and display an error.
    if (FAILED(hr))
    {
        wchar_t error[255];

        swprintf(error, L"HRESULT = %x", hr);

        MessageBox(0, error, L"Error, exiting.", 0);

        exit(1);
    }
}


LRESULT CALLBACK WndProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam)
{
    int wmId, wmEvent;
    PAINTSTRUCT ps;
    HDC hdc;

    switch (message)
    {
    case WM_COMMAND:
        wmId    = LOWORD(wParam);
        wmEvent = HIWORD(wParam);
        // Parse the menu selections:
        switch (wmId)
        {
        default:
            return DefWindowProc(hWnd, message, wParam, lParam);
        }
        break;
    case WM_PAINT:
        hdc = BeginPaint(hWnd, &ps);
        OnPaint(hdc);
        EndPaint(hWnd, &ps);
        break;
    case WM_SIZE:
        if (g_pBitmapRenderTarget)
        {
            int width = LOWORD(lParam);
            int height = HIWORD(lParam);
            g_pBitmapRenderTarget->Resize(width, height);
        }
        break;
    case WM_DESTROY:
        // The window is closing, release the DirectWrite variables we created for drawing.
        SafeReleaseT(g_pDWriteFactory);
        SafeReleaseT(g_pTextFormat);
        SafeReleaseT(g_pGdiInterop);
        SafeReleaseT(g_pTextLayout);
        SafeReleaseT(g_pBitmapRenderTarget);
        SafeReleaseT(g_pRenderingParams);
        SafeReleaseT(g_pGdiTextRenderer);

        PostQuitMessage(0);
        break;
    default:
        return DefWindowProc(hWnd, message, wParam, lParam);
    }
    return 0;
}

ForceInline VOID main2(LONG_PTR argc, PWSTR *argv)
{
    NTSTATUS Status;

    MSG msg;

    WNDCLASSEXW wcex;

    ZeroMemory(&wcex, sizeof(wcex));
    wcex.cbSize = sizeof(wcex);

    wcex.style            = CS_HREDRAW | CS_VREDRAW;
    wcex.lpfnWndProc    = WndProc;
    wcex.cbClsExtra        = 0;
    wcex.cbWndExtra        = 0;
    wcex.hInstance        = (HINSTANCE)&__ImageBase;
    wcex.hCursor        = LoadCursor(NULL, IDC_ARROW);
    wcex.hbrBackground    = NULL;
    wcex.lpszClassName    = L"FUCK";

    RegisterClassExW(&wcex);

    auto InitInstance = [](HINSTANCE hInstance, int nCmdShow)
    {
        HWND hWnd;

        hInstance; // Store instance handle in our global variable

        hWnd = CreateWindow(L"FUCK", L"FUCK", WS_OVERLAPPEDWINDOW,
            CW_USEDEFAULT, 0, CW_USEDEFAULT, 0, NULL, NULL, hInstance, NULL);

        if (!hWnd)
        {
            return FALSE;
        }

        ShowWindow(hWnd, nCmdShow);
        UpdateWindow(hWnd);

        return TRUE;
    };

    // Perform application initialization:
    if (!InitInstance ((HINSTANCE)&__ImageBase, SW_SHOWNORMAL))
    {
        return;
    }

    // Main message loop:
    while (GetMessage(&msg, NULL, 0, 0))
    {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    Ps::ExitProcess(0);

    return;

    ml::MlInitialize();

#if ML_X86

    SendMessageA((HWND)0x4A0592, WM_SETTEXT, 0, (LPARAM)"431670");

    return;

#else

    RtlAddVectoredExceptionHandler(TRUE,
        [](PEXCEPTION_POINTERS Exception) -> LONG
        {
            if (Exception->ExceptionRecord->ExceptionCode == EXCEPTION_PRIV_INSTRUCTION)
            {
                Exception->ContextRecord->Rip++;
                return EXCEPTION_CONTINUE_EXECUTION;
            }

            return EXCEPTION_CONTINUE_SEARCH;
        }
    );

    ULONG64 beg, end;

    beg = NtGetTickCount();

    for (int i = 1000000; i; --i)
    {
        __halt();
        YieldProcessor();
    }

    end = NtGetTickCount();

    PrintConsole(L"%d\n", end - beg);
    PauseConsole();

#endif

    return;

#if 0

    SC_HANDLE       ScManager, Service, Themes;
    SERVICE_STATUS  ServiceStatus;
    WCHAR           DriverPath[MAX_NTPATH];

    ScManager   = NULL;
    Service     = NULL;

    RtlWow64EnableFsRedirection(FALSE);
    ScManager = OpenSCManagerW(NULL, NULL, SC_MANAGER_CREATE_SERVICE);
    if (ScManager == NULL)
        return;

    PrintConsoleW(L"open scmgr\n");
    Status = STATUS_UNSUCCESSFUL;

    SCOPE_EXIT
    {
        if (Service != NULL)
        {
            if (!NT_SUCCESS(Status))
            {
                ControlService(Service, SERVICE_CONTROL_STOP, &ServiceStatus);
                DeleteService(Service);
            }
            CloseServiceHandle(Service);
        }

        if (ScManager != NULL)
            CloseServiceHandle(ScManager);

        PauseConsole();
        Nt_ExitProcess(0);
    }
    SCOPE_EXIT_END;

    Service = OpenServiceW(ScManager, BYPASS_UAC_SERVICE_NAME, SERVICE_ALL_ACCESS);

    PrintConsoleW(L"open svr\n");
    if (Service == NULL)
    {
        static WCHAR drv[] = BYPASS_UAC_DRIVER_NAME;
        CopyStruct(DriverPath + Nt_GetExeDirectory(DriverPath, countof(DriverPath)), drv, sizeof(drv));

        Service = CreateServiceW(
                        ScManager,
                        BYPASS_UAC_SERVICE_NAME,
                        BYPASS_UAC_SERVICE_NAME,
                        SERVICE_ALL_ACCESS,
                        SERVICE_KERNEL_DRIVER,
                        SERVICE_BOOT_START,
                        SERVICE_ERROR_IGNORE,
                        DriverPath,
                        NULL,
                        NULL,
                        NULL,
                        NULL,
                        NULL
                  );

        PrintConsoleW(L"create svr\n");
        if (Service == NULL)
            return;
    }

    if (!StartServiceW(Service, 0, NULL) && RtlGetLastWin32Error() != ERROR_SERVICE_ALREADY_RUNNING)
    {
        PrintConsoleW(L"lasterr %d\n", RtlGetLastWin32Error());
        return;
    }

    PrintConsoleW(L"start svr\n");
    Status = 0;

    return;

    NtFileDisk Device;

    Status = Device.OpenDevice(SHADOW_SYSCALL_DEVICE_SYMBOLIC);
    if (!NT_SUCCESS(Status))
        return;

    SS_PROBE_DEBUG_PORT Pdp;
    CONTEXT Context;
    ULONG_PTR CC;
    ULONG_PTR RemoteBase;
    HANDLE Thread;

    PROCESS_INFORMATION pi;

    if (!NT_SUCCESS(Nt_CreateProcess(NULL, Nt_CurrentPeb()->ProcessParameters->ImagePathName.Buffer, NULL, NULL, CREATE_SUSPENDED, NULL, &pi)))
        return;

    Context.ContextFlags = CONTEXT_ALL;
    NtGetContextThread(pi.hThread, &Context);

    RemoteBase = PtrSub(Context.Eax, PtrOffset(main2, &__ImageBase));

//    Nt_CreateThread((PVOID)(RemoteBase + PtrOffset(StubThread, &__ImageBase)), NULL, TRUE, pi.hProcess, &Thread);
//    Nt_WriteMemory(pi.hProcess, (PVOID)(Context.Esp + sizeof(PVOID)), &Thread, sizeof(Thread));
    Context.Eax = RemoteBase + PtrOffset(UnMapSectionThread, &__ImageBase);
    NtSetContextThread(pi.hThread, &Context);

    Pdp.DebugProcessId  = pi.dwProcessId;
    Pdp.DebugThreadId   = pi.dwThreadId;
    Pdp.UserContext     = &Context;

    Status = Device.DeviceIoControl(IOCTL_PROBE_DEBUG_PORT_ADDRESS, &Pdp, sizeof(Pdp), NULL, 0);
    PrintConsoleW(L"IOCTL_PROBE_DEBUG_PORT_ADDRESS: %08X\n", Status);

    NtTerminateProcess(pi.hProcess, 0);
    NtClose(pi.hProcess);
    NtClose(pi.hThread);

    PauseConsole();

    return;

#endif

#if 0
    INT   Height;
    HDC   hDC;
    HFONT hFont;
    BYTE  Buffer[0x5000];
    GLYPHMETRICS gm;
    MAT2 mat = { { 0, 1 }, { 0, 0 }, { 0, 0 }, { 0, 1 } };

    _wsetlocale(LC_CTYPE, L"");
    Height = 50;

#if 0
    ULONG BitsPerRow = 0x3E;
    PBYTE p = BitMap + sizeof(BitMap) - ROUND_UP(BitsPerRow / 8, 4);
    for (ULONG i = Height; i; --i)
    {
        PBYTE bak = p;
        for (ULONG j = BitsPerRow / 8; j; --j)
        {
            BYTE b = *p++;
            TEST_BIT(b, 7) ? printf("@") : printf(" ");
            TEST_BIT(b, 6) ? printf("@") : printf(" ");
            TEST_BIT(b, 5) ? printf("@") : printf(" ");
            TEST_BIT(b, 4) ? printf("@") : printf(" ");
            TEST_BIT(b, 3) ? printf("@") : printf(" ");
            TEST_BIT(b, 2) ? printf("@") : printf(" ");
            TEST_BIT(b, 1) ? printf("@") : printf(" ");
            TEST_BIT(b, 0) ? printf("@") : printf(" ");
        }
        p = bak - ROUND_UP(BitsPerRow / 8, 4);
        printf("#\n");
    }

//    return;

#endif

    hDC = CreateCompatibleDC(NULL);
    hFont = CreateFontW(
                Height,
                0,
                0,
                0,
                FW_NORMAL,
                0,
                0,
                0,
                GB2312_CHARSET,
                0,
                0,
                ANTIALIASED_QUALITY,
                FIXED_PITCH,
                L"ºÚÌå");
    SelectObject(hDC, hFont);
    WCHAR c = L'´ô';
    GetGlyphOutlineW(hDC, c, GGO_GRAY8_BITMAP, &gm, sizeof(Buffer), Buffer, &mat);

    INT nBytesPerLine;
    PBYTE pbBuffer = Buffer;

    printf(
        "Height             = %08X\n"
        "gmBlackBoxX        = %08X\n"
        "gmBlackBoxY        = %08X\n"
        "gmptGlyphOrigin.x  = %08X\n"
        "gmptGlyphOrigin.y  = %08X\n"
        "gmCellIncX         = %08X\n"
        "gmCellIncY         = %08X\n"
        "=========================\n",
        Height, gm.gmBlackBoxX, gm.gmBlackBoxY, gm.gmptGlyphOrigin.x, gm.gmptGlyphOrigin.y,
        gm.gmCellIncX, gm.gmCellIncY);

    nBytesPerLine = ROUND_UP(gm.gmBlackBoxX, sizeof(DWORD));

#if 0
    int nByteCount = ((gm.gmBlackBoxX +31) >> 5) << 2;
//    nByteCount = ROUND_UP(gm.gmBlackBoxX / 8, 8);
//    printf("%08X\n", nByteCount);

    PBYTE p1 = Buffer + (gm.gmBlackBoxY - 1) * nByteCount;
    p1 = Buffer;

    for (int i = ROUND_UP(gm.gmptGlyphOrigin.y, 32) / 8; i; --i)
        printf("\n");

    for ( int i = 0; i < gm.gmBlackBoxY; i++)
    {
        for (int j = gm.gmptGlyphOrigin.x; j; --j)
            printf(" ");

        PBYTE bak = p1;
        for (int j = 0; j < nByteCount; j++)
        {
            BYTE b;
            b = *p1++;
            TEST_BIT(b, 7) ? printf("@") : printf(" ");
            TEST_BIT(b, 6) ? printf("@") : printf(" ");
            TEST_BIT(b, 5) ? printf("@") : printf(" ");
            TEST_BIT(b, 4) ? printf("@") : printf(" ");
            TEST_BIT(b, 3) ? printf("@") : printf(" ");
            TEST_BIT(b, 2) ? printf("@") : printf(" ");
            TEST_BIT(b, 1) ? printf("@") : printf(" ");
            TEST_BIT(b, 0) ? printf("@") : printf(" ");
        }
//        p1 = bak - nByteCount;
        printf("#\n");
    }

    for (int i = (Height - gm.gmBlackBoxY) / 8; i; --i)
        printf("\n");

#else

    for (int j = 0; j != gm.gmBlackBoxY; ++j)
    {
        for (int i = 0; i != nBytesPerLine; ++i)
        {
            char c = *pbBuffer++;
            if (c > 31 && i < Height)
                printf("@");
            else
                printf(" ");
        }

        printf("#\n");
    }
#endif
#endif
    return;

/*
    HANDLE hFile, hMap;
    PBYTE  pbImage;
    PULONG_PTR pRVA;
    hFile = CreateFileW(
                name,
                GENERIC_READ|GENERIC_WRITE,
                FILE_SHARE_READ,
                NULL,
                OPEN_EXISTING,
                FILE_ATTRIBUTE_NORMAL,
                NULL);
    if (hFile == INVALID_HANDLE_VALUE)
        return;

    hMap = CreateFileMappingW(hFile, NULL, PAGE_READWRITE, 0, 0, NULL);
    CloseHandle(hFile);
    if (hMap == NULL)
        return;

    pbImage = (PBYTE)MapViewOfFile(hMap, FILE_MAP_READ|FILE_MAP_WRITE, 0, 0, 0);
    CloseHandle(hMap);
    if (pbImage == NULL)
        return;

    pRVA = (PULONG_PTR)(pbImage + 0x21440C);
    for (DWORD i = 266; i; --i)
    {
        if (*pRVA)
            *pRVA = *pRVA - 0x214400 + 0x21D000;
        else
            break;
        pRVA += 5;
    }

    UnmapViewOfFile(pbImage);
*/
}

int CDECL main(Long_Ptr argc, TChar **argv)
{
//    MyLib_Initialize();
//    my_initterm(&__xi_a, &__xi_z);
//    my_initterm(&__xc_a, &__xc_z);
    getargs(&argc, &argv);
    main2(argc, argv);

//    MyLib_UnInitialize();

    Ps::ExitProcess(0);
}

#if 0
Void FASTCALL ExtractSubtitles(Int argc, PWChar *argv)
{
    UInt32 cur;
    WChar path[MAX_PATH];
    HANDLE hPipeRead, hPipeWrite;
    STARTUPINFOW si;
    PROCESS_INFORMATION pi;
    SECURITY_ATTRIBUTES sa;

    if (argc < 2)
        return;
/*
    cur = GetModuleFileNameW(0, path, countof(path));
    while (path[--cur] != '\\');
    path[++cur] = 0;
*/

    _wsetlocale(LC_CTYPE, L"");

    sa.nLength = sizeof(sa);
    sa.lpSecurityDescriptor = NULL;
    sa.bInheritHandle = True;

    ZeroMemory(&si, sizeof(si));
    si.cb = sizeof(si);

    wcscpy(path, L"G:\\x\\mkvtoolnix\\mkvinfo.exe");
    cur = wcslen(path);
    for (Int i = 1; i != argc; ++i)
    {
        if (CreatePipe(&hPipeRead, &hPipeWrite, &sa, 0x2000) == False)
        {
            PrintError(GetLastError());
            continue;
        }

        si.dwFlags = STARTF_USESTDHANDLES;
        si.hStdOutput = hPipeWrite;
        swprintf(path + cur, L" \"%s\"", *++argv);
        if (CreateProcessW(NULL, path, NULL, NULL, True, 0, NULL, NULL, &si, &pi) == False)
        {
            PrintError(GetLastError());
            CloseHandle(hPipeWrite);
            CloseHandle(hPipeRead);
            continue;
        }

        WaitForSingleObjectEx(pi.hProcess, INFINITE, False);
        CloseHandle(pi.hProcess);
        CloseHandle(pi.hThread);
        CloseHandle(hPipeWrite);

        PChar pBuf, p1;
        DWORD dwRead, dwAvail;

        if (PeekNamedPipe(hPipeRead, 0, 0, NULL, &dwAvail, NULL))
        {
            pBuf = (PChar)malloc(dwAvail + 4);
            p1 = pBuf;
            ReadFile(hPipeRead, pBuf, dwAvail, &dwRead, NULL);
            *(PUInt32)&pBuf[dwRead] = 0;

            UInt32 count, n;
            PChar psubid, p;
            WChar cmd[MAX_PATH * 3];

            n = 0;
            count = swprintf(cmd, L"%s\"%s\" ", L"G:\\x\\mkvtoolnix\\mkvextract.exe tracks ", *argv);
            rmextw(*argv);
            while (psubid = strstr(pBuf, "Track type: subtitles"))
            {
                p = pBuf;
                pBuf = psubid + 1;
                psubid = StrRStrIA(p, psubid, "Track number:");
                if (psubid == NULL)
                    continue;

                if (sscanf(psubid, "Track number: %u", &dwRead) != 1)
                    continue;

                PCWChar fmt, param;
                static WChar *lang[] = { L"sc", L"tc", L"jp" };

                count += swprintf(cmd + count, L"%u:\"%s.", dwRead, *argv);

                if (n >= 0 && n < countof(lang))
                {
                    fmt = L"%s.ass\" ";
                    param = lang[n];
                }
                else
                {
                    fmt = L"%u.ass\" ";
                    param = (PCWChar)n;
                }

                count += swprintf(cmd + count, fmt, param);
                ++n;
            }

            si.dwFlags = 0;
            if (n && CreateProcessW(NULL, cmd, 0, 0, 0, 0, 0, 0, &si, &pi))
            {
                WaitForSingleObjectEx(pi.hProcess, INFINITE, False);
                CloseHandle(pi.hThread);
                CloseHandle(pi.hProcess);
            }

            free(p1);
        }

        CloseHandle(hPipeRead);
    }
}

#endif





#if 0



// #include "JsonParser.h"

HANDLE g_hHeap;

typedef struct
{
    TYPE_OF(NtWaitForSingleObject)  *NtWaitForSingleObject;
    TYPE_OF(DeleteFileW)            *DeleteFileW;
    TYPE_OF(NtTerminateProcess)     *NtTerminateProcess;
    TYPE_OF(NtClose)                *NtClose;

    HANDLE ProcessHandle;
    WCHAR  FullPath[1];

} DELETE_SELF_INFO, *PDELETE_SELF_INFO;

#if !ML_AMD64

VOID FASTCALL DeleteSelfImpl(PDELETE_SELF_INFO dsi)
{
    INLINE_ASM
    {
        call SELF_LOCATE;
SELF_LOCATE:
        pop eax;
        and eax, not (MEMORY_PAGE_SIZE - 1);
        mov dsi, eax;
    }

    dsi->NtWaitForSingleObject(dsi->ProcessHandle, FALSE, NULL);
    dsi->NtClose(dsi->ProcessHandle);
    dsi->DeleteFileW(dsi->FullPath);
    dsi->NtTerminateProcess(NtCurrentProcess(), 0);
}

ASM VOID DeleteSelfImplEnd() {}

VOID DeleteSelf()
{
    NTSTATUS            Status;
    ULONG               Length;
    WCHAR               path[MAX_PATH];
    STARTUPINFOW        si;
    PROCESS_INFORMATION pi;
    DELETE_SELF_INFO    dsi, *pdsi;
    CONTEXT             Context;
    PVOID               FuncAddress;

    CopyStruct(path + Nt_GetSystemDirectory(path, countof(path)), L"\\cmd.exe", sizeof(L"\\cmd.exe"));
    ZeroMemory(&si, sizeof(si));
    si.cb = sizeof(si);

//    pi.hProcess = NtCurrentProcess();
//    pi.hThread = NtCurrentThread();
    Status = Nt_CreateProcess(NULL, path, NULL, CREATE_SUSPENDED, NULL, &pi);
    if (!NT_SUCCESS(Status))
        return;

    pdsi = NULL;
    Status = Nt_AllocateMemory(pi.hProcess, (PVOID *)&pdsi, 0x1000);

    NtDuplicateObject(
        NtCurrentProcess(),
        NtCurrentProcess(),
        pi.hProcess,
        &dsi.ProcessHandle,
        0,
        FALSE,
        DUPLICATE_SAME_ACCESS
    );

    dsi.NtWaitForSingleObject   = NtWaitForSingleObject;
    dsi.DeleteFileW             = DeleteFileW;
    dsi.NtTerminateProcess      = NtTerminateProcess;
    dsi.NtClose                 = NtClose;

    Nt_WriteMemory(pi.hProcess, pdsi, &dsi, sizeof(dsi), (PSIZE_T)&Length);
    Length = Nt_GetModuleFileName(NULL, path, countof(path));
    Nt_WriteMemory(pi.hProcess, pdsi->FullPath, path, (Length + 1) * sizeof(WCHAR), (PSIZE_T)&Length);

    FuncAddress = (PBYTE)&pdsi->FullPath + Length;
    Nt_WriteMemory(
        pi.hProcess,
        FuncAddress,
        DeleteSelfImpl,
        (ULONG_PTR)DeleteSelfImplEnd - (ULONG_PTR)DeleteSelfImpl,
        (PSIZE_T)&Length
    );

    Context.ContextFlags = CONTEXT_CONTROL;
    NtGetContextThread(pi.hThread, &Context);
    Context.Eip = (ULONG_PTR)FuncAddress;
    Context.Ecx = (ULONG_PTR)pdsi;
    NtSetContextThread(pi.hThread, &Context);

    NtResumeThread(pi.hThread, NULL);
    NtClose(pi.hProcess);
    NtClose(pi.hThread);
}

#endif // x86

#endif



















/*

void CPUUsage()
{
    SYSTEM_PERFORMANCE_INFORMATION SysPerfInfo;
    SYSTEM_TIME_INFORMATION SysTimeInfo;
    SYSTEM_BASIC_INFORMATION SysBaseInfo;
    DOUBLE dbIdleTime;
    LONG64 dbSystemTime;
    LONG status;
    LARGE_INTEGER liOldIdleTime = {0,0};
    LARGE_INTEGER liOldSystemTime = {0,0};

    // get number of processors in the system
    status = NtQuerySystemInformation(SystemBasicInformation,
        &SysBaseInfo, sizeof(SysBaseInfo), NULL);

    printf("CPU Usage\n");
    while(!_kbhit())
    {
        // get new system time
        NtQuerySystemInformation(SystemTimeInformation, &SysTimeInfo, sizeof(SysTimeInfo), 0);
        // get new CPU'sname idle time
        NtQuerySystemInformation(SystemPerformanceInformation,
            &SysPerfInfo, sizeof(SysPerfInfo), NULL);

        // if it'sname a first call-skip it
        if (liOldIdleTime.QuadPart != 0)
        {
            // CurrentValue = NewValue - OldValue
            dbIdleTime   = (DOUBLE)SysPerfInfo.liIdleTime.QuadPart - liOldIdleTime.QuadPart;
            dbSystemTime = SysTimeInfo.liKeSystemTime.QuadPart - liOldSystemTime.QuadPart;

            // CurrentCpuIdle = IdleTime / SystemTime
            dbIdleTime = dbIdleTime / dbSystemTime;

            // CurrentCpuUsage% = 100 - (CurrentCpuIdle * 100) / NumberOfProcessors
            dbIdleTime = 100.0 - dbIdleTime * 100.0 / SysBaseInfo.bKeNumberProcessors + 0.5;

            printf("%d%%             \r",(UINT)dbIdleTime);
        }

        // store new CPU'sname idle and system time
        liOldIdleTime = SysPerfInfo.liIdleTime;
        liOldSystemTime = SysTimeInfo.liKeSystemTime;

        // wait one second
        Sleep(1000);
    }
    printf("\n");
}
*/
// & > ^ > |


#else // global

#pragma comment(linker, "/ENTRY:main")

#include <Windows.h>
#include <functional>

NTSTATUS NTAPI NtClose2(HANDLE Handle);

NTSTATUS __cdecl main(HANDLE)
{
    std::function<decltype(NtClose2)> fuck = main;
}

#endif
