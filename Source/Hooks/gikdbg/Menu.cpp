#include "gikdbg.h"

GikMenu::GikMenu(GikDbg *gikdbg)
{
    this->gikdbg = gikdbg;
}

NTSTATUS GikMenu::Initialize()
{
    PVOID BaseAddress;

    BaseAddress = FindLdrModuleByName(&USTR(L"iosdbg.dll"))->DllBase;

    Mp::PATCH_MEMORY_DATA p[] =
    {
        Mp::FunctionCallRva(0x1094F, StaticGikDialogBoxParamW),
    };

    return Mp::PatchMemory(p, countof(p), BaseAddress);
}

INT_PTR
NTAPI
GikMenu::
StaticGikDialogBoxParamW(
    HINSTANCE   Instance,
    PCWSTR      TemplateName,
    HWND        WndParent,
    DLGPROC     DialogFunc,
    LPARAM      InitParam
)
{
    return GetDebugger()->menu.GikDialogBoxParamW(Instance, TemplateName, WndParent, DialogFunc, InitParam);
}

INT_PTR
GikMenu::
GikDialogBoxParamW(
    HINSTANCE   Instance,
    PCWSTR      TemplateName,
    HWND        WndParent,
    DLGPROC     DialogFunc,
    LPARAM      InitParam
)
{
    if (GetKeyState(VK_SHIFT) >= 0)
        return DialogBoxParamW(Instance, TemplateName, WndParent, DialogFunc, InitParam);

    RECT rc;
    LONG ret, x, y;
    WCHAR buf[MAX_NTPATH *2];

    GetWindowRect(WndParent, &rc);

    x = rc.left + (rc.right - rc.left) / 2 - 250;
    y = rc.top + (rc.bottom - rc.top) / 2;
    buf[0] = 0;
    ret = Getstring(WndParent, L"Input full path of app", buf, countof(buf), 0, 0, x, y, 0, 0);
    if (ret == -1)
    {
        Info(L"canceled");
        return 0;
    }

    ULONG64 index;
    String app = buf;

    app = app.Replace(L"\\", L"/");

    index = app.LastIndexOf(L"/");
    if (index == app.kInvalidIndex)
    {
        Info(L"invalid app path");
        return 0;
    }

    buf[0] = 0;
    ret = Getstring(WndParent, L"Command line", buf, countof(buf), 0, 0, x, y, 0, 0);
    if (ret == -1)
    {
        Info(L"canceled");
        return 0;
    }

    gikdbg->SetAppPathAndArguments(app.SubString(0, index), app.SubString(index + 1), buf);

    return 0;
}
