#include "WindowManager.h"
#include <dwmapi.h>

using namespace Mp;

#define TESV_WINDOW_PROP L"TESV_WINDOW_DATA"

API_POINTER(CreateWindowExA) StubCreateWindowExA;
HWND MainWindow, RendererWindow;

WindowManager::WindowManager()
{
    this->borderless = FALSE;
    this->aeroShadow = FALSE;
}

NTSTATUS WindowManager::Initialize(PVOID TESVBase)
{
    FAIL_RETURN(NtAddAtom(TESV_WINDOW_PROP, CONST_STRLEN(TESV_WINDOW_PROP) * sizeof(TESV_WINDOW_PROP[0]), &this->windowProp));

    return CenterSkyrimWindow(TESVBase);
}

NTSTATUS WindowManager::CenterSkyrimWindow(PVOID TESVBase)
{
    PATCH_MEMORY_DATA p[] =
    {
        MemoryPatchVa((ULONG64)TESVCreateWindowExA, sizeof(PVOID), LookupImportTable(TESVBase, "USER32.dll", USER32_CreateWindowExA)),

        FunctionCallRva(0x86DD66, TESVSetWindowPos),
    };

    FAIL_RETURN(PatchMemory(p, countof(p), TESVBase));

    *(PVOID *)&StubCreateWindowExA = (PVOID)p[0].Memory.Backup;

    PTEB_ACTIVE_FRAME thiz = new TEB_ACTIVE_FRAME(TAG4('TESV'));
    thiz->Data = (ULONG_PTR)this;
    thiz->Push();

    return STATUS_SUCCESS;
}

HWND NTAPI WindowManager::TESVCreateWindowExA(DWORD dwExStyle, LPCSTR lpClassName, LPCSTR lpWindowName, DWORD dwStyle, int X, int Y, int nWidth, int nHeight, HWND hWndParent, HMENU hMenu, HINSTANCE hInstance, LPVOID lpParam)
{
    HWND    hWnd;
    RECT    workArea;
    HWND*   which;

    if (FLAG_OFF(dwStyle, WS_CHILD))
    {
        SystemParametersInfoW(SPI_GETWORKAREA, 0, &workArea, 0);
        X = ((workArea.right - workArea.left) - nWidth) / 2;
        Y = ((workArea.bottom - workArea.top) - nHeight)  / 2;

        which = &MainWindow;
    }
    else
    {
        which = &RendererWindow;
    }

    hWnd = StubCreateWindowExA(dwExStyle, lpClassName, lpWindowName, dwStyle, X, Y, nWidth, nHeight, hWndParent, hMenu, hInstance, lpParam);
    *which = hWnd;

    return hWnd;
}

BOOL NTAPI WindowManager::TESVSetWindowPos(HWND hWnd, HWND hWndInsertAfter, int X, int Y, int cx, int cy, UINT uFlags)
{
    RECT workArea;
    PTEB_ACTIVE_FRAME thiz;

    SystemParametersInfoW(SPI_GETWORKAREA, 0, &workArea, 0);

    X = ((workArea.right - workArea.left) - cx) / 2;
    Y = ((workArea.bottom - workArea.top) - cy)  / 2;

    if ((workArea.right - workArea.left) <= cx)
        X = 0;

    if (((workArea.bottom - workArea.top) <= cy))
        Y = 0;

    if (X == 0 && Y == 0)
    {
        hWndInsertAfter = HWND_TOPMOST;
    }

    thiz = FindThreadFrame(TAG4('TESV'));
    if (thiz != nullptr)
    {
        WindowManager *self;

        self = (WindowManager *)thiz->Data;
        delete thiz;

        SetPropW(hWnd, TESV_WINDOW_PROP, (HANDLE)self);

        self->mainWindowProc = (WNDPROC)SetWindowLongPtrA(hWnd, GWLP_WNDPROC,
            (LONG_PTR)(WNDPROC)[] (HWND hWnd, UINT Message, WPARAM wParam, LPARAM lParam) -> LRESULT
            {
                return ((WindowManager *)GetPropW(hWnd, TESV_WINDOW_PROP))->TESVMainWindowProc(hWnd, Message, wParam, lParam);
            }
        );

        self->ToggleBorderless(hWnd);
    }

    return SetWindowPos(hWnd, hWndInsertAfter, X, Y, cx, cy, uFlags);
}

LRESULT WindowManager::TESVMainWindowProc(HWND hWnd, UINT Message, WPARAM wParam, LPARAM lParam)
{
    switch (Message)
    {
        case WM_NCCALCSIZE:
            if (this->borderless)
                return 0;

            break;

        case WM_NCHITTEST:
            break;

        case WM_ACTIVATE:
            if (this->borderless == FALSE)
                break;

            SetWindowPos(hWnd, wParam == WA_INACTIVE ? HWND_NOTOPMOST : HWND_TOPMOST, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE);

            if (wParam == WA_INACTIVE)
            {
                while (ShowCursor(TRUE) <= 16);
            }
            break;

        case WM_KEYDOWN:
        case WM_SYSKEYDOWN:
        {
            switch (wParam)
            {
                case VK_F12:
                    //ToggleBorderless(hWnd);
                    break;
            }
            break;
        }
    }

    return this->mainWindowProc(hWnd, Message, wParam, lParam);
}

VOID WindowManager::ToggleBorderless(HWND hwnd)
{
    Style newStyle = (borderless) ? Style::windowed : Style::aeroBorderless;
    SetWindowLongPtrA(hwnd, GWL_STYLE, (LONG_PTR)newStyle);

    borderless = !borderless;

    if (newStyle == Style::aeroBorderless)
    {
        // ToggleShadow(hwnd);
    }

    //redraw frame
    SetWindowPos(hwnd, 0, 0, 0, 0, 0, SWP_FRAMECHANGED | SWP_NOMOVE | SWP_NOSIZE);
}

VOID WindowManager::ToggleShadow(HWND hwnd)
{
    if (borderless)
    {
        aeroShadow = !aeroShadow;
        aeroShadow = FALSE;
        const MARGINS shadow_on = { 1, 1, 1, 1 };
        const MARGINS shadow_off = { 0, 0, 0, 0 };
        DwmExtendFrameIntoClientArea(hwnd, aeroShadow ? &shadow_on : &shadow_off);
    }
}
