#ifndef _EDAO_H_5c8a3013_4334_4138_9413_3d0209da878e_
#define _EDAO_H_5c8a3013_4334_4138_9413_3d0209da878e_

#include "MyLibrary.h"

class EDAO
{
public:
    VOID THISCALL Fade(ULONG Param1, ULONG Param2, ULONG Param3, ULONG Param4, ULONG Param5, ULONG Param6);
    BOOL THISCALL CheckItemEquipped(ULONG ItemId, PULONG EquippedIndex);

    static TYPE_OF(&EDAO::Fade)                 StubFade;
    static TYPE_OF(&EDAO::CheckItemEquipped)    StubCheckItemEquipped;
};

DECL_SELECTANY TYPE_OF(EDAO::StubFade) EDAO::StubFade = NULL;
DECL_SELECTANY TYPE_OF(EDAO::StubCheckItemEquipped) EDAO::StubCheckItemEquipped = NULL;

class CBattle
{
public:
    VOID USE_ATTACK_FOR_CHECKING();
    VOID USE_MAGIC_FOR_CHECKING();
    VOID USE_CRAFT_FOR_CHECKING();
    VOID USE_SCRAFT_FOR_CHECKING();
};

class CSSaveData
{
public:
    VOID SaveData2SystemData();
    VOID SystemData2SaveData();
};

#endif // _EDAO_H_5c8a3013_4334_4138_9413_3d0209da878e_
