#ifndef _MENU_H_daaa024e_01c9_486e_b37c_4c190abe81ad_
#define _MENU_H_daaa024e_01c9_486e_b37c_4c190abe81ad_

#include "ml.h"

class GikDbg;

class GikMenu
{
protected:
    GikDbg* gikdbg;

public:
    GikMenu(GikDbg *gikdbg);

    NTSTATUS Initialize();

    static
    INT_PTR
    NTAPI
    StaticGikDialogBoxParamW(
        HINSTANCE   Instance,
        PCWSTR      TemplateName,
        HWND        WndParent,
        DLGPROC     DialogFunc,
        LPARAM      InitParam
    );

    INT_PTR
    GikDialogBoxParamW(
        HINSTANCE   Instance,
        PCWSTR      TemplateName,
        HWND        WndParent,
        DLGPROC     DialogFunc,
        LPARAM      InitParam
    );
};

#endif // _MENU_H_daaa024e_01c9_486e_b37c_4c190abe81ad_
