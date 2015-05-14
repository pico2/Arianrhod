#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text /MERGE:.text1=.text /SECTION:.idata,ERW")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")
#pragma comment(linker, "/EXPORT:SHRegGetValueW=SHLWAPI.SHRegGetValueW")

#pragma comment(lib, "od2.lib")

#include "gikdbg.h"
#include "ml.cpp"

using ml::String;

VOID (FASTCALL *SetAppPathAndArguments)(PWSTR Path, PWSTR Name, PWSTR CommandLine);

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

INT_PTR
NTAPI
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

    SetAppPathAndArguments(app.SubString(0, index), app.SubString(index + 1), buf);

    return 0;
}

BOOL Initialize(PVOID BaseAddress)
{
    LdrDisableThreadCalloutsForDll(BaseAddress);
    ml::MlInitialize();

    BaseAddress = FindLdrModuleByName(&USTR(L"iosdbg.dll"))->DllBase;

    Mp::PATCH_MEMORY_DATA p[] =
    {
        Mp::FunctionCallRva(0x1094F, GikDialogBoxParamW),
    };

    Mp::PatchMemory(p, countof(p), BaseAddress);

    *(PVOID *)&SetAppPathAndArguments = PtrAdd(BaseAddress, 0xD400);

    return TRUE;
}

BOOL WINAPI DllMain(PVOID BaseAddress, ULONG Reason, PVOID Reserved)
{
    switch (Reason)
    {
        case DLL_PROCESS_ATTACH:
            return Initialize(BaseAddress) || UnInitialize(BaseAddress);

        case DLL_PROCESS_DETACH:
            UnInitialize(BaseAddress);
            break;
    }

    return TRUE;
}
