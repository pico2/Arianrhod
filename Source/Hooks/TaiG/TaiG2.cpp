#pragma comment(linker, "/ENTRY:DllMain")
//#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text /MERGE:.text1=.text /SECTION:.idata,ERW")
//#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")
#pragma comment(linker, "/EXPORT:GetFileVersionInfoW=VERSION.GetFileVersionInfoW")
#pragma comment(linker, "/EXPORT:GetFileVersionInfoSizeW=VERSION.GetFileVersionInfoSizeW")
#pragma comment(linker, "/EXPORT:VerQueryValueW=VERSION.VerQueryValueW")

#include "TaiG2.h"
#include "ml.cpp"

PVOID TaiGBase;

BOOL CDECL IsJailbroken(HANDLE Device)
{
    RtlSetLastWin32Error(STATUS_UNSUCCESSFUL);
    return FALSE;
}

BOOL CDECL IsDeviceUnActivated(HANDLE Device)
{
    return FALSE;
}

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

NTSTATUS FuckAnti_Initialize(PVOID TaiGBase);
NTSTATUS Remove3K_Initialize(PVOID TaiGBase);
NTSTATUS Remove3K2_Initialize(PVOID TaiGBase);
NTSTATUS Record_Initialize(PVOID TaiGBase);

BOOL Initialize(PVOID BaseAddress)
{
    using namespace Mp;

    LdrDisableThreadCalloutsForDll(BaseAddress);
    ml::MlInitialize();

    //BaseAddress = LoadDll(L"TaiG.dll");
    //TaiGBase = BaseAddress;

    Remove3K2_Initialize(BaseAddress);
    //Remove3K_Initialize(BaseAddress);
    //FuckAnti_Initialize(BaseAddress);
    //Record_Initialize(BaseAddress);

    PATCH_MEMORY_DATA p[] =
    {
        FunctionJumpRva(0x11360, IsJailbroken),
        FunctionJumpRva(0x145B0, IsDeviceUnActivated),
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
