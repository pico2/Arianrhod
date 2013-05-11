#include "edao.h"

NAKED VOID CBattle::NakedGetPredefinedMagicNumber()
{
    INLINE_ASM
    {
        mov     ecx, [ebp - 08h];
        mov     edx, [ebp + 08h];
        call    CBattle::GetPredefinedMagicNumber
        mov     [ebp - 20h], eax;
        ret;
    }
}

ULONG FASTCALL CBattle::GetPredefinedMagicNumber(PMONSTER_STATUS MSData)
{
    ULONG_PTR MagicDefined;
    PCRAFT_AI_INFO Magic;

    MagicDefined = 0;
    Magic = MSData->MagicAiInfo;

    for (ULONG_PTR Count = countof(MSData->MagicAiInfo); Count; ++Magic, --Count)
    {
        if (Magic->CraftIndex == 0)
            break;

        ++MagicDefined;
    }

    return MagicDefined;
}

NAKED VOID CBattle::OverWriteBattleStatusWithChrStatus()
{
    INLINE_ASM
    {
        mov     dword ptr [ebp - 20h], 0x0;
        mov     ecx, [ebp - 08h];
        call    CBattle::GetActorInfo
        mov     ecx, eax;
        call    CActor::GetPartyChipMap
        mov     edx, dword ptr [ebp - 14h];
        movzx   eax, word ptr [eax + edx * 2];
        mov     ecx, [esp];
        cmp     eax, MINIMUM_CUSTOM_CHAR_ID
        mov     edx, 0x9A37F4;
        cmovae  ecx, edx;
        mov     [esp], ecx;
        ret;
    }
}

NAKED ULONG CBattle::GetChrIdForSCraft()
{
    INLINE_ASM
    {
        mov     ecx, [ebp - 08h];
        call    CBattle::GetActorInfo
        mov     ecx, eax;
        call    CActor::GetPartyChipMap
        mov     ecx, dword ptr [ebp - 14h];
        movzx   ecx, [ecx]MONSTER_STATUS.CharID;
        movzx   eax, [eax + ecx * 2];
        cmp     eax, MINIMUM_CUSTOM_CHAR_ID
        cmovae  ecx, eax;
        ret;
    }
}

NAKED VOID CBattle::NakedGetTurnVoiceChrId()
{
    INLINE_ASM
    {
        mov     ecx, [ebp - 0Ch];
        mov     edx, [ebp + 08h];
        call    CBattle::GetTurnVoiceChrId;
        mov     ecx, eax;
        ret;
    }
}

ULONG FASTCALL CBattle::GetTurnVoiceChrId(PMONSTER_STATUS MSData)
{
    ULONG ChrId, PartyId;

    ChrId = MSData->CharID;
    PartyId = GetActorInfo()->GetPartyChipMap()[ChrId];

    return PartyId < MINIMUM_CUSTOM_CHAR_ID ? ChrId : PartyId;
}

NAKED VOID CBattle::NakedGetSBreakVoiceChrId()
{
    INLINE_ASM
    {
        jmp CBattle::NakedGetTurnVoiceChrId;
    }
}

/************************************************************************
  EDAO
************************************************************************/

NAKED VOID EDAO::NakedGetChrSBreak()
{
    INLINE_ASM
    {
        mov     ecx, eax;
        jmp     EDAO::GetChrSBreak;
    }
}

VOID FASTCALL EDAO::GetChrSBreak(PMONSTER_STATUS MSData)
{
    ULONG           ChrId;
    PCRAFT_AI_INFO  Craft;

    ChrId = GetBattle()->GetActorInfo()->GetPartyChipMap()[MSData->CharID];
    if (ChrId < MINIMUM_CUSTOM_CHAR_ID)
    {
        MSData->CurrentActionIndex = GetSBreakList()[MSData->CharID];
        return;
    }

    Craft = MSData->SCraftAiInfo;
    for (ULONG_PTR Count = countof(MSData->SCraftAiInfo); Count; ++Craft, --Count)
    {
        if (Craft->CraftIndex == 0)
            break;
    }

    //Craft = Craft == MSData->SCraftAiInfo ? Craft : (Craft - 1);
    Craft = PtrSub(Craft, ((Craft == MSData->SCraftAiInfo) - 1) & sizeof(*Craft));

    MSData->SelectedCraft.MagicAriaActionIndex  = Craft->MagicAriaActionIndex;
    MSData->SelectedCraft.ActionIndex           = Craft->ActionIndex;
    MSData->CurrentActionIndex                  = Craft->CraftIndex;
}

/************************************************************************
  CGlobal
************************************************************************/

PCSTR CGlobal::GetMagicDescription(USHORT MagicId)
{
    if (MagicId < MINIMUM_CUSTOM_CRAFT_INDEX)
        return (this->*StubGetMagicDescription)(MagicId);

    CBattle*        Battle;
    PMONSTER_STATUS MSData;

    Battle = GetEDAO()->GetBattle();

    MSData = &Battle->GetMonsterStatus()[Battle->GetCurrentChrIndex()];

    return MSData->CraftDescription[MagicId - MINIMUM_CUSTOM_CRAFT_INDEX].Description;
}

PBYTE CGlobal::GetMagicQueryTable(USHORT MagicId)
{
    if (MagicId < MINIMUM_CUSTOM_CRAFT_INDEX)
        return (this->*StubGetMagicQueryTable)(MagicId);

    static BYTE StaticMagicQueryTable[] = { 233, 233, 233, 233, 233, 233, 233, 233 };

    return StaticMagicQueryTable;
}
