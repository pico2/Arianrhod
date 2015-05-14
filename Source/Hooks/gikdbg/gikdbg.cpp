#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text /MERGE:.text1=.text /SECTION:.idata,ERW")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")
#pragma comment(linker, "/EXPORT:SHRegGetValueW=SHLWAPI.SHRegGetValueW")
#pragma comment(lib, "od2.lib")

#include "gikdbg.h"
#include "ml.cpp"

ML_OVERLOAD_NEW

GikDbg* gikdbg;

GikDbg::GikDbg() : menu(this)
{
}

NTSTATUS GikDbg::Initialize()
{
    PVOID BaseAddress;

    BaseAddress = FindLdrModuleByName(&USTR(L"iosdbg.dll"))->DllBase;

    *(PVOID *)&SetAppPathAndArguments = PtrAdd(BaseAddress, 0xD400);

    this->menu.Initialize();

    return STATUS_SUCCESS;
}

ForceInline VOID SetDebugger(GikDbg* dbg)
{
    gikdbg = dbg;
}

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    LdrDisableThreadCalloutsForDll(BaseAddress);
    ml::MlInitialize();

    SetDebugger(new GikDbg());
    GetDebugger()->Initialize();

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
