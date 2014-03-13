#ifndef _GDI32HOOK_H_c6f62ce3_e0ab_44ea_99b1_07a3f245255b_
#define _GDI32HOOK_H_c6f62ce3_e0ab_44ea_99b1_07a3f245255b_

#include "LocaleEmulator.h"

extern ULONG (NTAPI *GdiGetCodePage)(HDC NewDC);

HFONT GetFontFromDC(PLeGlobalData GlobalData, HDC hDC);
HFONT GetFontFromFont(PLeGlobalData GlobalData, HFONT Font);

#endif // _GDI32HOOK_H_c6f62ce3_e0ab_44ea_99b1_07a3f245255b_
