#ifndef _GIKDBG_H_dc65053a_93f0_4543_b313_fc6bad438b13_
#define _GIKDBG_H_dc65053a_93f0_4543_b313_fc6bad438b13_

#include "ml.h"
#include "od2.h"
#include "Menu.h"

using ml::String;

class GikDbg
{
public:
    GikMenu menu;

    struct
    {
        VOID (FASTCALL *SetAppPathAndArguments)(PWSTR Path, PWSTR Name, PWSTR CommandLine);
    };

    NTSTATUS Initialize();

public:
    GikDbg();
};

ForceInline GikDbg* GetDebugger()
{
    extern GikDbg* gikdbg;
    return gikdbg;
}

#endif // _GIKDBG_H_dc65053a_93f0_4543_b313_fc6bad438b13_
