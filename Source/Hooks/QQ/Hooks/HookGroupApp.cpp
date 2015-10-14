#include "Hooks.h"

ULONG_PTR BanSpeechObjectOffset;
VOID (FASTCALL *StubGetBanSpeechTimeStamp)(PVOID This, PVOID Edx, PULONG* TimeStampData, PULONG* What);

VOID FASTCALL GetBanSpeechTimeStamp(PVOID This, PVOID Edx, PULONG* TimeStampData, PULONG* What)
{
    StubGetBanSpeechTimeStamp(This, Edx, TimeStampData, What);

    ULONG& TimeStamp = (*TimeStampData)[4];

    if (*TimeStampData == *(PULONG*)PtrAdd(PtrSub(This, BanSpeechObjectOffset), BanSpeechObjectOffset + 4))
        return;

    if (GetKeyState(VK_CONTROL) < 0)
    {
        TimeStamp = INT32_MAX;
    }
}

BOOL SearchGroupApp_AtAllGroupMember(PVOID GroupApp, PVOID *GetAdminFlag, PVOID *GetUseTimes)
{
    static WCHAR String[] = L"AtAllGroupMember_MsgBox_Title";

    PVOID Found;
    PBYTE Buffer;
    PLDR_MODULE Module;

    Module = FindLdrModuleByHandle(GroupApp);

    Found = SearchStringReference(Module, String, sizeof(String));
    if (Found == nullptr)
        return FALSE;

    Buffer = (PBYTE)Found - 1;

    if (Buffer[0] != PUSH ||
        Buffer[-2] != 0x6A ||
        Buffer[-4] != 0x75)
    {
        return FALSE;
    }

    *GetAdminFlag = &Buffer[-4];

    Found = SearchStringReference(Module, String, sizeof(String), PtrOffset(Buffer + 5, Module->DllBase));
    if (Found == nullptr)
        return FALSE;

    Buffer = (PBYTE)Found - 1;

    if (Buffer[0] != PUSH ||
        Buffer[-2] != 0x6A ||
        Buffer[-4] != 0x75 ||
        Buffer[-0xB] != CALL)
    {
        return FALSE;
    }

    *GetUseTimes = GetCallDestination(&Buffer[-0xB]);

    return TRUE;
}

BOOL SearchGroupApp_AtAllGroupMemberMax(PVOID GroupApp, PVOID *ConditionJump)
{
    PVOID Found, Buffer;
    PLDR_MODULE Module;

    /************************************************************************
    360C9908    .  E8 93F0FFFF         call    0x360C89A0
    360C990D    .  83BD 74FFFFFF 14    cmp     dword ptr [ebp-0x8C], 0x14
    360C9914    .  59                  pop     ecx
    360C9915    .  59                  pop     ecx
    360C9916    .  7C 12               jl      short 0x360C992A
    ************************************************************************/

    Module = FindLdrModuleByHandle(GroupApp);
    Buffer = SearchPatternSafe(L"E8 ?? ?? ?? ?? 83 BD ?? ?? ?? ?? 14", Module->DllBase, Module->SizeOfImage);
    if (Buffer == nullptr)
        return FALSE;

    Found = IMAGE_INVALID_VA;

    WalkOpCodeT(Buffer, 0x20,
        WalkOpCodeM(Buffer, OpLength, Ret)
        {
            switch (Buffer[0])
            {
                case 0x7C:  // jl short
                    Found = Buffer;
                    return STATUS_SUCCESS;
            }

            return STATUS_NOT_FOUND;
        }
    );

    *ConditionJump = Buffer;

    return Found != IMAGE_INVALID_VA;
}

PVOID SearchGroupApp_GroupBanSpeech(PVOID ImageBase)
{
    PVOID Function, CallGetBanSpeechTimeStamp;

    static WCHAR String[] = LR"({"groupuin":%lu;"currenttime":%lu;"banspeechtime":%lu;"useruin":%lu})";

    Function = SearchStringAndReverseSearchHeader(ImageBase, String, sizeof(String) - sizeof(String[0]), 0x320);
    if (Function == IMAGE_INVALID_VA)
        return IMAGE_INVALID_VA;

    CallGetBanSpeechTimeStamp = IMAGE_INVALID_VA;

    WalkOpCodeT(Function, 0x270,
        WalkOpCodeM(Buffer, OpLength, Ret)
        {
            if (
                OpLength == 3 &&
                Buffer[0] == 0x83 && Buffer[1] == 0xC1 && // Buffer[2] == 0x58 &&       // add ecx, const
                Buffer[3] == 0xE8                                                       // call const
               )
            {
                BanSpeechObjectOffset = (ULONG_PTR)Buffer[2];
                CallGetBanSpeechTimeStamp = Buffer + 3;
                return STATUS_SUCCESS;
            }

            return STATUS_NOT_FOUND;
        }
    );

    return CallGetBanSpeechTimeStamp;
}

NTSTATUS HookGroupApp(PVOID BaseAddress)
{
    // BOOL AtAllGroupMemberFound, AtGroupMemberMaxFound;
    // PVOID GetAdminFlag, GetUseTimes, AtGroupMemberMax;

    // AtAllGroupMemberFound = SearchGroupApp_AtAllGroupMember(BaseAddress, &GetAdminFlag, &GetUseTimes);
    // AtGroupMemberMaxFound = SearchGroupApp_AtAllGroupMemberMax(BaseAddress, &AtGroupMemberMax);

    Mp::PATCH_MEMORY_DATA Function_GroupApp[] =
    {
        //Mp::FunctionJumpVa(AtAllGroupMemberFound ? GetUseTimes : IMAGE_INVALID_VA, GetAtAllGroupMemberUseTimes),
        //Mp::FunctionCallVa(AtGroupMemberMaxFound ? AtGroupMemberMax : IMAGE_INVALID_VA, GetCurrentAtNumber),
        Mp::FunctionCallVa(SearchGroupApp_GroupBanSpeech(BaseAddress), GetBanSpeechTimeStamp, &StubGetBanSpeechTimeStamp),
    };

    return Mp::PatchMemory(Function_GroupApp, countof(Function_GroupApp), BaseAddress);
}