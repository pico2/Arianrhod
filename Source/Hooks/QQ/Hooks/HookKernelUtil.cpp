#include "Hooks.h"

TYPE_OF(Util::Group::CheckMsgImage) StubCheckMsgImage;
TYPE_OF(Util::Contact::IsSuperVip)  StubIsSuperVip;

BOOL CDECL CheckMsgImage(PVOID GroupObject, CTXStringW &Message)
{
    BOOL Success;

    Success = StubCheckMsgImage(GroupObject, Message);

    if (!Success && !Message.IsEmpty())
    {
        if (wcsstr(Message.Buffer, L"·¢ËÍ") != nullptr)
        {
            Success = TRUE;
            Message.Empty();
        }
    }

    return Success;
}

BOOL CDECL IsSuperVip(ULONG_PTR Uin, PULONG_PTR SVipLevel)
{
    if (Uin == Util::Contact::GetSelfUin())
    {
        if (SVipLevel != nullptr)
            *SVipLevel = 7;

        return TRUE;
    }

    return StubIsSuperVip(Uin, SVipLevel);
}

NTSTATUS HookKernelUtil(PVOID BaseAddress)
{
    /************************************************************************
      KernelUtil

        CF_Group_Image_TooManyImage
    ************************************************************************/

    Mp::PATCH_MEMORY_DATA Function_KernelUtil[] =
    {
        Mp::FunctionJumpVa(Util::Group::CheckMsgImage, CheckMsgImage, &StubCheckMsgImage),
        Mp::FunctionJumpVa(Util::Contact::IsSuperVip,  IsSuperVip,    &StubIsSuperVip),
    };

    return Mp::PatchMemory(Function_KernelUtil, countof(Function_KernelUtil), BaseAddress);
}
