#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text /MERGE:.text1=.text /SECTION:.idata,ERW")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")
#pragma comment(linker, "/EXPORT:D3DPERF_SetOptions=d3d9.D3DPERF_SetOptions")

#include "TESV/Patcher.h"
#include "ml.cpp"

ML_OVERLOAD_NEW

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    Rtl::SetExeDirectoryAsCurrent();

    LdrDisableThreadCalloutsForDll(BaseAddress);
    ml::MlInitialize();

    return NT_SUCCESS((new Patcher())->Initialize()) && (Ldr::LoadDll(L"skse_steam_loader.dll"), TRUE);
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
