#include "edao.h"

/************************************************************************
  EDAO
************************************************************************/

BOOL EDAO::CheckItemEquipped(ULONG ItemId, PULONG EquippedIndex)
{
    switch (ItemId)
    {
        case 0xB7:  // ú—Ä¿
        case 0xB8:  // ÌìÑÛ
        case 0xBB:  // Ì½Öª
            if (EquippedIndex != NULL)
                *EquippedIndex = 0;
        
            return TRUE;
    }
    
    return (this->*StubCheckItemEquipped)(ItemId, EquippedIndex);
}


/************************************************************************
  CScript
************************************************************************/

NAKED VOID CScript::NakedInheritSaveData()
{
    INLINE_ASM
    {
        mov     dword ptr [eax + 82BB4h], 0;
        lea     edx, dword ptr [ebp - 0x26454 + 0x1B008];
        mov     ecx, [ebp - 0Ch];
        jmp     CScript::InheritSaveData
    }
}

VOID FASTCALL CScript::InheritSaveData(PBYTE ScenarioFlags)
{
    ULONG_PTR CustomOffset[] =
    {
        0x212,
    };

    PULONG_PTR Offset;

    FOR_EACH(Offset, CustomOffset, countof(CustomOffset))
    {
        *(PBYTE)PtrAdd(this, 0x9C + *Offset) = ScenarioFlags[*Offset];
    }
}

BOOL THISCALL CScript::ScpSaveRestoreParty(PSCENA_ENV_BLOCK Block)
{
    BOOL   Result, NeedRefreshFA;
    USHORT Chr[8];

    enum { Save = 1, Restore = 2 };

    NeedRefreshFA = GetScenaTable()[Block->ScenaIndex][Block->CurrentOffset + 1] == Restore &&
                    RtlCompareMemory(GetActor()->GetPartyListSaved(), GetActor()->GetPartyList(), sizeof(Chr)) != sizeof(Chr);

    Result = (this->*StubScpSaveRestoreParty)(Block);

    if (NeedRefreshFA)
        GetEDAO()->LoadFieldAttackData();

    return Result;
}
