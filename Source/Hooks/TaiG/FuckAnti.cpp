#include "TaiG2.h"

VOID (*StubiTunesInitAndStealAFCSendRecv)();
VOID (*StubInitAndStealAMDServiceSendRecv)();

PVOID NTAPI LoadTaiGDll(PCSTR)
{
    return LoadDll(L"TaiG.dll");
}

BOOL CDECL VerifyTaiGExe()
{
    return TRUE;
}

PVOID CDECL TgGetRoutine(PVOID BaseAddress, PVOID OrdinalOrName)
{
}

BOOL CDECL IsiTunesMobileAndAirTrafficHasBreakPoint()
{
    return FALSE;
}

VOID iTunesInitAndStealAFCSendRecv()
{
    StubiTunesInitAndStealAFCSendRecv();

    iTunesApi::Initialize();

    *(PVOID *)PtrAdd(TaiGBase, 0x868A8) = iTunesApi::AFC::AFCReadData;
    *(PVOID *)PtrAdd(TaiGBase, 0x868AC) = iTunesApi::AFC::AFCSendData;
}

VOID InitAndStealAMDServiceSendRecv()
{
    StubInitAndStealAMDServiceSendRecv();

    *(PVOID *)PtrAdd(TaiGBase, 0x868B4) = iTunesApi::AMD::AMDServiceConnectionReceive;
    *(PVOID *)PtrAdd(TaiGBase, 0x868B8) = iTunesApi::AMD::AMDServiceConnectionSend;
}

NTSTATUS FuckAnti_Initialize(PVOID TaiGBase)
{
    using namespace Mp;

    {
        PATCH_MEMORY_DATA p[] =
        {
            FunctionJumpRva(0x149A0, IsiTunesMobileAndAirTrafficHasBreakPoint),
            FunctionJumpRva(0x147D0, iTunesInitAndStealAFCSendRecv, &StubiTunesInitAndStealAFCSendRecv),
            FunctionJumpRva(0x163F0, InitAndStealAMDServiceSendRecv, &StubInitAndStealAMDServiceSendRecv),

            //FunctionJumpRva(0x35870, TgGetRoutine),
            //FunctionJumpRva(0x5CD0, VerifyTaiGExe),
        };

        PatchMemory(p, countof(p), TaiGBase);
    }

    {
        PATCH_MEMORY_DATA p[] =
        {
            FunctionCallRva(0x1500B, LoadTaiGDll),
        };

        PatchMemory(p, countof(p), GetExeModuleHandle());
    }

    return STATUS_SUCCESS;
}
