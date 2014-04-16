#ifndef _GDI32HOOK_H_c6f62ce3_e0ab_44ea_99b1_07a3f245255b_
#define _GDI32HOOK_H_c6f62ce3_e0ab_44ea_99b1_07a3f245255b_

#include "LocaleEmulator.h"

#define FMS_CALL_MAGIC TAG4('FMSC')

struct FMS_CALL_CONTEXT : public TEB_ACTIVE_FRAME
{
    HDC hDC;

    FMS_CALL_CONTEXT()
    {
        this->Context = FMS_CALL_MAGIC;
    }

    static FMS_CALL_CONTEXT* Find()
    {
        return (FMS_CALL_CONTEXT *)FindThreadFrame(FMS_CALL_MAGIC);
    }
};

typedef FMS_CALL_CONTEXT *PFMS_CALL_CONTEXT;

extern ULONG (NTAPI *GdiGetCodePage)(HDC NewDC);

HFONT GetFontFromDC(PLeGlobalData GlobalData, HDC hDC);
HFONT GetFontFromFont(PLeGlobalData GlobalData, HFONT Font);

#endif // _GDI32HOOK_H_c6f62ce3_e0ab_44ea_99b1_07a3f245255b_
