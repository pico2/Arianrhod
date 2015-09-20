#ifndef _WINDOWMANAGER_H_fb148139_26d6_45aa_968c_a47b113fde66_
#define _WINDOWMANAGER_H_fb148139_26d6_45aa_968c_a47b113fde66_

#include "Base.h"

class WindowManager
{
    enum class Style : ULONG
    {
        windowed = (WS_OVERLAPPEDWINDOW | WS_CAPTION | WS_SYSMENU | WS_MINIMIZEBOX | WS_MAXIMIZEBOX | WS_THICKFRAME),
        aeroBorderless = ( WS_POPUP | WS_CAPTION | WS_THICKFRAME | WS_MAXIMIZEBOX | WS_MINIMIZEBOX)
    };

public:
    WindowManager();
    NTSTATUS Initialize(PVOID TESVBase);

protected:
    static HWND NTAPI TESVCreateWindowExA(DWORD dwExStyle, LPCSTR lpClassName, LPCSTR lpWindowName, DWORD dwStyle, int X, int Y, int nWidth, int nHeight, HWND hWndParent, HMENU hMenu, HINSTANCE hInstance, LPVOID lpParam);
    static BOOL NTAPI TESVSetWindowPos(HWND hWnd, HWND hWndInsertAfter, int X, int Y, int cx, int cy, UINT uFlags);

    NTSTATUS CenterSkyrimWindow(PVOID TESVBase);
    LRESULT TESVMainWindowProc(HWND hWnd, UINT Message, WPARAM wParam, LPARAM lParam);
    VOID ToggleBorderless(HWND hwnd);
    VOID ToggleShadow(HWND hwnd);

protected:
    ATOM windowProp;
    WNDPROC mainWindowProc;
    BOOL borderless;
    BOOL aeroShadow;
};

#endif // _WINDOWMANAGER_H_fb148139_26d6_45aa_968c_a47b113fde66_