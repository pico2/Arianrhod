#include "edao.h"

NAKED VOID CBattle::NakedCopyMagicAndCraftData()
{
    INLINE_ASM
    {
        mov     ecx, [ebp - 08h];
        mov     edx, [ebp + 08h];
        and     dword ptr [ebp - 20h], 0;
        jmp     CBattle::CopyMagicAndCraftData
    }
}

VOID FASTCALL CBattle::CopyMagicAndCraftData(PMONSTER_STATUS MSData)
{
    PUSHORT         MagicList;
    ULONG_PTR       MaxMagicNumber;
    PCRAFT_AI_INFO  Magic;

    if (!IsCustomChar(MSData->CharID))
        return;

    MaxMagicNumber  = countof(MSData->MagicAiInfo);
    Magic           = MSData->MagicAiInfo;
    MagicList       = GetActor()->GetChrMagicList() + MSData->CharID * MaxMagicNumber;

    for (ULONG_PTR Count = countof(MSData->MagicAiInfo); Count; --Count)
    {
        if (Magic->CraftIndex == 0)
            break;

        --MaxMagicNumber;
        ++Magic;
    }

    for (; MaxMagicNumber; ++Magic, ++MagicList, --MaxMagicNumber)
    {
        Magic->CraftIndex       = *MagicList;
        Magic->AriaActionIndex  = 6;
        Magic->ActionIndex      = 7;
        Magic->Condition        = 0;
    }

    *(PVOID *)_AddressOfReturnAddress() = (PVOID)0x9A37F4;
}

NAKED VOID CBattle::NakedOverWriteBattleStatusWithChrStatus()
{
    INLINE_ASM
    {
        mov     ecx, [ebp - 08h];
        mov     edx, edi;
        push    eax;
        call    CBattle::OverWriteBattleStatusWithChrStatus
        ret;
    }
}

PMONSTER_STATUS FASTCALL CBattle::OverWriteBattleStatusWithChrStatus(PMONSTER_STATUS MSData, PCHAR_STATUS ChrStatus)
{
    MSData = PtrSub(MSData, FIELD_OFFSET(MONSTER_STATUS, ChrStatus[BattleStatusFinal].MaximumHP));

    PCHAR_STATUS Raw = &MSData->ChrStatus[BattleStatusRaw];
    PCHAR_STATUS Final = &MSData->ChrStatus[BattleStatusFinal];

    *Final = *ChrStatus;

    if (!IsCustomChar(MSData->CharID))
        return MSData;

    Final->MaximumHP    += Raw->MaximumHP   / 2;
    Final->InitialHP    += Raw->InitialHP   / 2;
    Final->MaximumEP    += Raw->MaximumEP   / 2;
    Final->InitialEP    += Raw->InitialEP   / 2;
    Final->STR          += Raw->STR         * 2 / 3;
    Final->DEF          += Raw->DEF         * 2 / 3;
    Final->ATS          += Raw->ATS         * 2 / 3;
    Final->ADF          += Raw->ADF         * 2 / 3;
    Final->DEX          += Raw->DEX         * 2 / 3;
    Final->AGL          += Raw->AGL         * 2 / 3;
    Final->MOV          += Raw->MOV         * 2 / 3;
    Final->SPD          += Raw->SPD         * 2 / 3;

    return MSData;
}

NAKED VOID CBattle::NakedIsChrStatusNeedRefresh()
{
    INLINE_ASM
    {
        mov     ecx, [ebp - 0Ch];
        mov     edx, dword ptr [ebp - 8Ch];
        push    dword ptr [ebp - 25E8h];
        push    eax;
        call    CBattle::IsChrStatusNeedRefresh
        neg     eax;
        ret;
    }
}

BOOL FASTCALL CBattle::IsChrStatusNeedRefresh(ULONG_PTR ChrPosition, PCHAR_STATUS CurrentStatus, ULONG_PTR PrevLevel)
{
    PMONSTER_STATUS MSData;

    MSData = GetMonsterStatus() + ChrPosition;

    if (!IsCustomChar(MSData->CharID))
    {
        return CurrentStatus->Level != PrevLevel;
    }

    return TRUE;
}

NAKED ULONG CBattle::NakedGetChrIdForSCraft()
{
    INLINE_ASM
    {
        mov     ecx, [ebp - 08h];
        call    CBattle::GetActor
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

ULONG FASTCALL CBattle::GetVoiceChrIdWorker(PMONSTER_STATUS MSData)
{
    ULONG ChrId, PartyId;

    ChrId = MSData->CharID;
    PartyId = GetActor()->GetPartyChipMap()[ChrId];

    return IsCustomChar(ChrId) ? PartyId : ChrId;
}

/*++

  mov     word ptr [ebp-const], r16
  mov     r32, const
  mov     word ptr [ebp-const], r16
  mov     r32, const
  mov     word ptr [ebp-const], r16
  mov     r32, [ebp+8]
  movzx   r32, [r32+0A]

--*/

NAKED VOID CBattle::NakedGetTurnVoiceChrId()
{
    INLINE_ASM
    {
        mov     ecx, [ebp - 0Ch];
        mov     edx, [ebp + 08h];
        call    CBattle::GetVoiceChrIdWorker;
        mov     ecx, eax;
        ret;
    }
}

NAKED VOID CBattle::NakedGetReplySupportVoiceChrId()
{
    INLINE_ASM
    {
        jmp CBattle::NakedGetTurnVoiceChrId;
    }
}

NAKED VOID CBattle::NakedGetRunawayVoiceChrId()
{
    INLINE_ASM
    {
        jmp CBattle::NakedGetTurnVoiceChrId;
    }
}

NAKED VOID CBattle::NakedGetTeamRushVoiceChrId()
{
    INLINE_ASM
    {
        jmp CBattle::NakedGetTurnVoiceChrId;
    }
}

NAKED VOID CBattle::NakedGetSBreakVoiceChrId()
{
    INLINE_ASM
    {
        jmp CBattle::NakedGetTurnVoiceChrId;
    }
}

NAKED VOID CBattle::NakedGetBattleState()
{
    static ULONG PreviousState;

    INLINE_ASM
    {
        mov     dword ptr [ebp-0x294], ecx;
        mov     ecx, dword ptr [eax+0x113078];
        cmp     ecx, 2;
        je      INIT_STATE;

        cmp     PreviousState, -1;
        je      RETURN;

        cmp     PreviousState, 1Eh;
        je      THINK_FIRST_SBREAK;

        mov     PreviousState, ecx;

        jmp     RETURN;

THINK_FIRST_SBREAK:

        mov     dword ptr [eax+0x113078], 03Ch;
        or      PreviousState, -1;
        jmp     RETURN;

INIT_STATE:

        and     PreviousState, 0;

RETURN:

        ret;
    }
}

BOOL CBattle::ThinkSCraft(PMONSTER_STATUS MSData)
{
    PAT_BAR_ENTRY Entry;

    Entry = GetBattleATBar()->EntryPointer[0];

    if (!MSData->IsChrEnemy() ||
        Entry == NULL ||
        Entry->MSData != MSData ||
        !Entry->IsSBreaking)
    {
        return (this->*StubThinkSCraft)(MSData);
    }

    SetCurrentActionChr(0xA, MSData);

    return TRUE;
}

BOOL CBattle::ThinkRunaway(PMONSTER_STATUS MSData)
{
    return GetBattleATBar()->FindATBarEntry(MSData)->IsSBreaking ? FALSE : (this->*StubThinkRunaway)(MSData);
}

BOOL CBattle::ThinkSBreak(PMONSTER_STATUS MSData)
{
    BOOL            Success;
    PAT_BAR_ENTRY   SelfEntry, *Entry;

    //TYPE_OF(&CBattle::ThinkSBreak) ThinkMagicEveryChrAction;
    //*(PULONG_PTR)&ThinkMagicEveryChrAction = 0x9926E0;

    TYPE_OF(&CBattle::ThinkSBreak) ThinkSCraft;
    *(PULONG_PTR)&ThinkSCraft = 0x98E730;

    if ((this->*StubThinkSBreak)(MSData))
        return TRUE;

    if (!MSData->IsChrCanThinkSCraft())
        return FALSE;

    SelfEntry = GetBattleATBar()->FindATBarEntry(MSData);
/*
    FOR_EACH(Entry, GetBattleATBar()->EntryPointer, countof(GetBattleATBar()->EntryPointer))
    {
        if (Entry[0] == SelfEntry && Entry != GetBattleATBar()->EntryPointer)
            break;

        if (Entry[0]->IsSBreaking)
            return FALSE;
    }
*/
    if (SelfEntry == NULL || SelfEntry->IsSBreaking)
        return FALSE;

    ULONG_PTR Conditions =  CraftConditions::Frozen         |
                            CraftConditions::Landification  |
                            CraftConditions::Sleeping       |
                            CraftConditions::Stun           |
                            CraftConditions::BanCraft       |
                            CraftConditions::Confusion      |
                            CraftConditions::OnehitKill     |
                            CraftConditions::Vanish         |
                            CraftConditions::Reserve_3      |
                            CraftConditions::Dead;

    if (FindEffectInfoByCondition(MSData, Conditions) != NULL)
        return FALSE;

    struct
    {
        PMONSTER_STATUS MSData;
        ULONG_PTR       Type;
        ULONG_PTR       Unknown_119AEE;
        ULONG_PTR       Unknown_11A4D9;

    } SavedData;

    SavedData.MSData            = *(PMONSTER_STATUS *)PtrAdd(this, 0x119AE8);
    SavedData.Type              = *(PUSHORT)PtrAdd(this, 0x119AEC);
    SavedData.Unknown_119AEE    = *(PUSHORT)PtrAdd(this, 0x119AEE);
    SavedData.Unknown_11A4D9    = *(PUSHORT)PtrAdd(this, 0x11A4D9);

    Success = (this->*ThinkSCraft)(MSData);

    *(PMONSTER_STATUS *)PtrAdd(this, 0x119AE8)  = SavedData.MSData;
    *(PUSHORT)PtrAdd(this, 0x119AEC)            = SavedData.Type;
    *(PUSHORT)PtrAdd(this, 0x119AEE)            = SavedData.Unknown_119AEE;
    *(PUSHORT)PtrAdd(this, 0x11A4D9)            = SavedData.Unknown_11A4D9;

    if (!Success)
        return FALSE;

    GetEDAO()->GetSound()->PlaySound(506);
    GetBattleATBar()->AdvanceChrInATBar(MSData, IsForceInsertToFirst());

    MSData->AT = 0;

    return FALSE;
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
    PCRAFT_AI_INFO Craft;

    if (!IsCustomChar(MSData->CharID))
    {
        MSData->CurrentCraftIndex = GetSBreakList()[MSData->CharID];
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

    MSData->SelectedCraft.AriaActionIndex   = Craft->AriaActionIndex;
    MSData->SelectedCraft.ActionIndex       = Craft->ActionIndex;
    MSData->CurrentCraftIndex               = Craft->CraftIndex;
}

/************************************************************************
  CGlobal
************************************************************************/

PCREATE_INFO CGlobal::GetMagicData(USHORT MagicId)
{
    if (MagicId < MINIMUM_CUSTOM_CRAFT_INDEX)
        return (this->*StubGetMagicData)(MagicId);

    CBattle*        Battle;
    PMONSTER_STATUS MSData;

    Battle = GetEDAO()->GetBattle();

    MSData = &Battle->GetMonsterStatus()[Battle->GetCurrentChrIndex()];

    return &MSData->CraftInfo[MagicId - MINIMUM_CUSTOM_CRAFT_INDEX];
}

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

    static BYTE StaticMagicQueryTable[7] = { /* 233, 233, 233, 233, 233, 233, 233, 233 */ };

    return StaticMagicQueryTable;
}



/************************************************************************
  info box
************************************************************************/

VOID THISCALL CBattleInfoBox::SetMonsterInfoBoxSize(LONG X, LONG Y, LONG Width, LONG Height)
{
    TYPE_OF(&CBattleInfoBox::SetMonsterInfoBoxSize) StubSetBoxSize;

    *(PVOID *)&StubSetBoxSize = (PVOID)0x67302C;

    return (this->*StubSetBoxSize)(X, Y, 120, Height);
}

VOID THISCALL CBattleInfoBox::DrawMonsterStatus()
{
    if (GetBattle()->GetCurrentTargetIndex() > MAXIMUM_CHR_NUMBER_IN_BATTLE)
        return;

    BOOL                ShowInfo, ShowByOrbment;
    ULONG_PTR           BackgroundColor;
    MONSTER_INFO_FLAGS  Flags;
    PCOORD              UpperLeft;
    RECT                Rect;
    PMONSTER_STATUS     MSData;

    if (!IsTargetEnemy())
    {
        SetTargetIsEnemy(TRUE);
        SetMonsterInfoFlags(~0u);
    }

    (this->*StubDrawMonsterStatus)();

    Flags = GetMonsterInfoFlags();
    ShowInfo = Flags.AllValid();
    ShowByOrbment = !ShowInfo && Flags.IsShowByOrbment();
    ShowInfo = ShowInfo || ShowByOrbment;

    UpperLeft = GetUpperLeftCoord();

    RECT debug = { 284, 12, 128, 100 };

    Rect.left   = UpperLeft->X + debug.left;
    Rect.top    = UpperLeft->Y + debug.top;
    Rect.right  = Rect.left + debug.right;
    Rect.bottom = Rect.top + debug.bottom;

    BackgroundColor = (GetBackgroundColor() & 0xA0000000) | 0x00101020;

    GetEDAO()->DrawRectangle(Rect.left, Rect.top, Rect.right, Rect.bottom, BackgroundColor, BackgroundColor);

    MSData = GetBattle()->GetMonsterStatus() + GetBattle()->GetCurrentTargetIndex();

    typedef struct
    {
        PCSTR Text;
        ULONG Value;

        ULONG_PTR (*Format)(PMONSTER_STATUS MSData, PSTR Buffer);

    } STATUS_ENTRY;

    STATUS_ENTRY *Entry, Status[] =
    {
        { "EP:", 0, [](PMONSTER_STATUS MSData, PSTR Buffer) -> ULONG_PTR { return sprintf(Buffer, "%d/%d", MSData->ChrStatus[BattleStatusFinal].InitialEP, MSData->ChrStatus[BattleStatusFinal].MaximumEP); }  },
        { "CP:", 0, [](PMONSTER_STATUS MSData, PSTR Buffer) -> ULONG_PTR { return sprintf(Buffer, "%d/%d", MSData->ChrStatus[BattleStatusFinal].InitialCP, MSData->ChrStatus[BattleStatusFinal].MaximumCP); }  },

        { "STR:", MSData->ChrStatus[BattleStatusFinal].STR },
        { "DEF:", MSData->ChrStatus[BattleStatusFinal].DEF },
        { "ATS:", MSData->ChrStatus[BattleStatusFinal].ATS },
        { "ADF:", MSData->ChrStatus[BattleStatusFinal].ADF },
        { "DEX:", MSData->ChrStatus[BattleStatusFinal].DEX },
        { "AGL:", MSData->ChrStatus[BattleStatusFinal].AGL },
        { "MOV:", MSData->ChrStatus[BattleStatusFinal].MOV },
        { "SPD:", MSData->ChrStatus[BattleStatusFinal].SPD },
        { "RNG:", MSData->ChrStatus[BattleStatusFinal].RNG },
    };

    CHAR        Buffer[0x200];
    LONG_PTR    X, Y, ValueX, ValueY, BoxWidth;
    ULONG_PTR   ValueColor;
    EDAO*       edao;

    POINT debug2 = { -11, -14 };

    edao = GetEDAO();

    BoxWidth = Rect.right - Rect.left;

    X = Rect.left - UpperLeft->X + debug2.x;
    Y = Rect.top - UpperLeft->Y + debug2.y;

    ValueY = Rect.top - UpperLeft->Y + 24;
    ValueColor = (ShowByOrbment ? 0xFF8020 : 0xFFFFFF) | (GetBackgroundColor() & 0xFF000000);

    FOR_EACH(Entry, Status, countof(Status))
    {
        DrawSimpleText(X, Y, Entry->Text, COLOR_GOLD);

        if (ShowInfo)
        {
            Entry->Format == NULL ? sprintf(Buffer, "%d", Entry->Value) : Entry->Format(MSData, Buffer);
            edao->DrawNumber(X + 69, ValueY, Buffer, ValueColor);
        }
        else
        {
            DrawSimpleText(X + 26, Y, "?", COLOR_WHITE);
        }

        Y += 14;
        ValueY += 14;
    }
}

/************************************************************************
  battle tweak
************************************************************************/

LONG CDECL CBattle::FormatBattleChrAT(PSTR Buffer, PCSTR Format, LONG Index, LONG No, LONG IcoAT, LONG ObjAT, LONG Pri)
{
    return sprintf(Buffer, "%d", IcoAT);
}

LONG CDECL CBattle::ShowSkipCraftAnimeButton(...)
{
    AllocStack(16);

    CBattle *Battle;

    Battle = *(CBattle **)(*(PULONG_PTR)PtrSub(_AddressOfReturnAddress(), sizeof(PVOID)) - 0xC);
    Battle->ShowSkipAnimeButton();

    return 0;
}
