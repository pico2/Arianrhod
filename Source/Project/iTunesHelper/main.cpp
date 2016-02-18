#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text /MERGE:.text1=.text /SECTION:.idata,ERW")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")

#include "stdafx.h"
#include "ml.cpp"

ML_OVERLOAD_NEW

API_POINTER(LdrLoadDll) StubLdrLoadDll;

NTSTATUS
NTAPI
iLdrLoadDll(
    IN  PWSTR               PathToFile OPTIONAL,
    IN  PULONG              DllCharacteristics OPTIONAL,
    IN  PCUNICODE_STRING    ModuleFileName,
    OUT PVOID*              DllHandle
)
{
    auto st = StubLdrLoadDll(PathToFile, DllCharacteristics, ModuleFileName, DllHandle);
    DebugLog(L"load %wZ %p", ModuleFileName, st);
    return st;
}

BOOL UnInitialize(PVOID BaseAddress)
{
    DebugLog(L"%S", __FUNCTION__);
    PauseConsole(L"hit");
    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    LdrDisableThreadCalloutsForDll(BaseAddress);
    ml::MlInitialize();

    using namespace Mp;

    PATCH_MEMORY_DATA p[] =
    {
        FunctionJumpVa(LdrLoadDll, iLdrLoadDll, &StubLdrLoadDll),
    };

    //PatchMemory(p, countof(p), BaseAddress);

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
