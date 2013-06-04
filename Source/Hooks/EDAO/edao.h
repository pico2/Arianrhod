#ifndef _EDAO_H_5c8a3013_4334_4138_9413_3d0209da878e_
#define _EDAO_H_5c8a3013_4334_4138_9413_3d0209da878e_

#include "MyLibrary.h"

ML_OVERLOAD_NEW

class EDAO;
class CGlobal;
class CBattle;

#define INIT_STATIC_MEMBER(x) DECL_SELECTANY TYPE_OF(x) x = NULL
#define DECL_STATIC_METHOD_POINTER(cls, method) static TYPE_OF(&cls::method) Stub##method
#define DETOUR_METHOD(cls, method, addr, ...) TYPE_OF(&cls::method) (method); *(PULONG_PTR)&(method) = addr; return (this->*method)(__VA_ARGS__)


#define UCL_COMPRESS_MAGIC TAG4('UCL4')

#define MINIMUM_CUSTOM_CHAR_ID          0xB0
#define MINIMUM_CUSTOM_CRAFT_INDEX      0x3E8
#define MAXIMUM_CHR_NUMBER_IN_BATTLE    0x16

#pragma pack(push, 1)

typedef struct
{
    ULONG Magic;
    ULONG CompressedSize;

} UCL_COMPRESS_HEADER;


ML_NAMESPACE_BEGIN(CraftConditions)

    static const ULONG_PTR Poison              = 0x00000001;
    static const ULONG_PTR Frozen              = 0x00000002;
    static const ULONG_PTR Landification       = 0x00000004;
    static const ULONG_PTR Sleeping            = 0x00000008;
    static const ULONG_PTR BanArts             = 0x00000010;
    static const ULONG_PTR Darkness            = 0x00000020;
    static const ULONG_PTR BanCraft            = 0x00000040;
    static const ULONG_PTR Confusion           = 0x00000080;
    static const ULONG_PTR Stun                = 0x00000100;
    static const ULONG_PTR OnehitKill          = 0x00000200;
    static const ULONG_PTR Burning             = 0x00000400;
    static const ULONG_PTR Rage                = 0x00000800;
    static const ULONG_PTR ArtsGuard           = 0x00001000;
    static const ULONG_PTR CraftGuard          = 0x00002000;

    static const ULONG_PTR MaxGuard            = 0x00004000;
    static const ULONG_PTR Vanish              = 0x00008000;
    static const ULONG_PTR StrUp               = 0x00010000;
    static const ULONG_PTR DefUp               = 0x00020000;
    static const ULONG_PTR AtsUp               = 0x00040000;
    static const ULONG_PTR AdfUp               = 0x00080000;
    static const ULONG_PTR DexUp               = 0x00100000;
    static const ULONG_PTR AglUp               = 0x00200000;
    static const ULONG_PTR MovUp               = 0x00400000;
    static const ULONG_PTR SpdUp               = 0x00800000;
    static const ULONG_PTR HPRecovery          = 0x01000000;
    static const ULONG_PTR CPRecovery          = 0x02000000;

    static const ULONG_PTR Stealth             = 0x04000000;
    static const ULONG_PTR ArtsReflect         = 0x08000000;
    static const ULONG_PTR Reserve_1           = 0x10000000;
    static const ULONG_PTR Reserve_2           = 0x20000000;
    static const ULONG_PTR Reserve_3           = 0x40000000;

    static const ULONG_PTR Dead                = 0x80000000;

ML_NAMESPACE_END


typedef struct  // 0x18
{
    BYTE    Condition;
    BYTE    Probability;
    BYTE    Target;
    BYTE    TargetCondition;
    BYTE    AriaActionIndex;
    BYTE    ActionIndex;
    USHORT  CraftIndex;
    ULONG   Parameter[4];

} CRAFT_AI_INFO, *PCRAFT_AI_INFO;

typedef struct
{
    USHORT  ActionIndex;
    BYTE    Target;
    BYTE    Unknown_3;
    BYTE    Attribute;
    BYTE    RangeType;
    BYTE    State1;
    BYTE    State2;
    BYTE    RNG;
    BYTE    RangeSize;
    BYTE    AriaTime;
    BYTE    SkillTime;
    USHORT  EP_CP;
    USHORT  RangeSize2;
    USHORT  State1Parameter;
    USHORT  State1Time;
    USHORT  State2Parameter;
    USHORT  State2Time;

    DUMMY_STRUCT(4);

} CRAFT_INFO, *PCRAFT_INFO;

typedef struct
{
    CHAR Description[0x100];
    CHAR Name[0x20];

} CRAFT_DESCRIPTION;

enum
{
    ACTION_ATTACK,
    ACTION_MOVE,
    ACTION_MAGIC,
    ACTION_CRAFT,
    ACTION_SCRAFT,
    ACTION_ITEM,
    ACTION_ARIA_MAGIC,
    ACTION_CAST_MAGIC,
    ACTION_ARIA_CRAFT,
    ACTION_CAST_CRAFT,
};

enum
{
    BattleStatusRaw,
    BattleStatusFinal,
};


typedef union
{
    DUMMY_STRUCT(0x34);

    struct
    {
        ULONG                   MaximumHP;                  // 0x234
        ULONG                   InitialHP;                  // 0x238
        USHORT                  Level;                      // 0x23C
        USHORT                  MaximumEP;                  // 0x23E
        USHORT                  InitialEP;                  // 0x240
        USHORT                  InitialCP;                  // 0x242
        USHORT                  EXP;                        // 0x244

        DUMMY_STRUCT(2);

        USHORT                  STR;                        // 0x248
        USHORT                  DEF;                        // 0x24A
        USHORT                  ATS;                        // 0x24C
        USHORT                  ADF;                        // 0x24E
        USHORT                  DEX;                        // 0x250
        USHORT                  AGL;                        // 0x252
        USHORT                  MOV;                        // 0x254
        USHORT                  SPD;                        // 0x256
        USHORT                  DEXRate;                    // 0x258
        USHORT                  AGLRate;                    // 0x25A
        USHORT                  MaximumCP;                  // 0x25C

        DUMMY_STRUCT(2);                                    // 0x25E

        USHORT                  RNG;                        // 0x260

        DUMMY_STRUCT(2);

        ULONG                   ConditionFlags;             // 0x264
    };

} CHAR_STATUS, *PCHAR_STATUS;

typedef struct
{
    ULONG               ConditionFlags;
    PVOID               Effect;
    BYTE                Unknown2[2];
    USHORT              ConditionRate;
    ULONG               ATLeft;
    ULONG               Unknown4;

} MS_EFFECT_INFO, *PMS_EFFECT_INFO;

enum
{
    CHR_FLAG_ENEMY  = 0x1000,
    CHR_FLAG_NPC    = 0x2000,
    CHR_FLAG_PLAYER = 0x4000,
    CHR_FLAG_EMPTY  = 0x8000,
};

typedef union MONSTER_STATUS
{
    DUMMY_STRUCT(0x2424);

    BOOL IsChrEnemy()
    {
        return AiType != 0xFF && !FLAG_ON(State, CHR_FLAG_NPC | CHR_FLAG_PLAYER | CHR_FLAG_EMPTY);
    }

    BOOL IsChrCanThinkSCraft(BOOL CheckAiType = FALSE)
    {
        if (!IsChrEnemy())
            return FALSE;

        if (AiType == 0xFF)
            return FALSE;

        if (!CheckAiType)
            return TRUE;

        switch (AiType)
        {
            case 0x00:
            case 0x02:
            case 0x1F:
                return TRUE;
        }

        return FALSE;
    }

    struct
    {

        USHORT                  CharPosition;               // 0x00
        USHORT                  State;                      // 0x02
        USHORT                  State2;                     // 0x04
        DUMMY_STRUCT(4);                                    // 0x06
        USHORT                  CharID;                     // 0x0A
        DUMMY_STRUCT(4);                                    // 0x0C
        ULONG                   SymbolIndex;                // 0x10
        ULONG                   MSFileIndex;                // 0x14

        DUMMY_STRUCT(0x16C - 0x18);

        USHORT                  CurrentActionType;          // 0x16C

        DUMMY_STRUCT(2);

        USHORT                  PreviousActionType;         // 0x170
        USHORT                  SelectedActionType;         // 0x172
        USHORT                  Unknown_174;
        USHORT                  Unknown_176;
        USHORT                  Unknown_178;
        USHORT                  Unknown_17A;
        USHORT                  WhoAttackMe;                // 0x17C
        USHORT                  CurrentCraftIndex;          // 0x17E
        USHORT                  LastActionIndex;            // 0x180
        USHORT                  CurrentAiIndex;             // 0x182

        DUMMY_STRUCT(0x1AA - 0x184);

        USHORT                  Target[0x10];               // 0x1AA
        BYTE                    TargetCount;                // 0x1CA
        BYTE                    SelectedTargetIndex;        // 0x1CB
        COORD                   SelectedTargetPos;          // 0x1CC

        DUMMY_STRUCT(0x234 - 0x1D0);

        CHAR_STATUS ChrStatus[2];                           // 0x234

        USHORT MoveSPD;                                     // 0x29C

        DUMMY_STRUCT(2);

        MS_EFFECT_INFO          EffectInfo[32];             // 0x2A0

        DUMMY_STRUCT(0x538 - (0x2A0 + sizeof(MS_EFFECT_INFO) * 32));

        ULONG                   AT;                         // 0x538
        ULONG                   AT2;                        // 0x53C
        USHORT                  AiType;                     // 0x540
        USHORT                  EXPGet;                     // 0x542
        USHORT                  DropItem[2];                // 0x544
        BYTE                    DropRate[2];                // 0x548

        DUMMY_STRUCT(2);

        USHORT                  Equipment[5];               // 0x54C
        USHORT                  Orbment[7];                 // 0x556
        CRAFT_AI_INFO           Attack;                     // 0x564
        CRAFT_AI_INFO           MagicAiInfo[80];            // 0x57C
        CRAFT_AI_INFO           CraftAiInfo[15];            // 0xCFC
        CRAFT_AI_INFO           SCraftAiInfo[5];            // 0xE64
        CRAFT_AI_INFO           SupportAiInfo[3];           // 0xEDC

        struct
        {
            USHORT                  CraftIndex;             // 0xF24
            BYTE                    AriaActionIndex;        // 0xF26
            BYTE                    ActionIndex;            // 0xF27

        } SelectedCraft;

        DUMMY_STRUCT(4);                                    // 0xF28

        CRAFT_INFO                  CraftInfo[16];          // 0xF2C
        CRAFT_DESCRIPTION           CraftDescription[10];   // 0x10EC

        DUMMY_STRUCT(0x2408 - 0x10EC - sizeof(CRAFT_DESCRIPTION) * 10);

        ULONG                       SummonCount;            // 0x2408

    };

} MONSTER_STATUS, *PMONSTER_STATUS;

#pragma pack(pop)


class CActor
{
public:
    PUSHORT GetPartyChipMap()
    {
        return (PUSHORT)PtrAdd(this, 0x6140);
    }

    PUSHORT GetPartyList()
    {
        return (PUSHORT)PtrAdd(this, 0x2CC);
    }

    PUSHORT GetPartyListSaved()
    {
        return (PUSHORT)PtrAdd(this, 0x2DC);
    }

    BOOL IsCustomChar(ULONG_PTR ChrId)
    {
        return GetPartyChipMap()[ChrId] >= MINIMUM_CUSTOM_CHAR_ID;
    }

    PUSHORT GetChrMagicList()
    {
        return (PUSHORT)PtrAdd(this, 0x5D4);
    }
};

typedef union
{
    ULONG Flags;
    struct
    {
        UCHAR   HP              : 1;        // 0x00000001
        UCHAR   Level           : 1;        // 0x00000002
        UCHAR   EXP             : 1;        // 0x00000004
        UCHAR   Information     : 1;
        UCHAR   Resist          : 1;        // 0x00000020
        UCHAR   AttributeRate   : 1;        // 0x00000040

                                            // 0x10000000   orb
    };

    BOOL AllValid()
    {
        ULONG AllFlags = 0x01 | 0x02 | 0x04 | 0x20 | 0x40;
        return (Flags & AllFlags) == AllFlags;
    }

    BOOL IsShowByOrbment()
    {
        return FLAG_ON(Flags, 0x10000000);
    }

} MONSTER_INFO_FLAGS, *PMONSTER_INFO_FLAGS;



enum
{
    COLOR_WHITE     = 0,
    COLOR_ORANGE    = 1,
    COLOR_RED       = 2,
    COLOR_BLUE      = 3,
    COLOR_YELLOW    = 4,
    COLOR_GREEN     = 5,
    COLOR_GRAY      = 6,
    COLOR_PINK      = 7,
    COLOR_GOLD      = 8,
    COLOR_BLACK     = 9,
    COLOR_YELLOWB   = 10,


    COLOR_MAXIMUM   = 21,
};

class CBattleInfoBox
{
public:
    EDAO* GetEDAO()
    {
        return *(EDAO **)PtrAdd(this, 0xC);
    }

    CBattle* GetBattle()
    {
        return (CBattle *)PtrSub(this, 0xF0D24);
    }

    PCOORD GetUpperLeftCoord()
    {
        return (PCOORD)PtrAdd(*(PULONG_PTR)PtrAdd(this, 0x20), 0xF2);
    }

    ULONG_PTR GetBackgroundColor()
    {
        return *(PULONG)PtrAdd(*(PULONG_PTR)PtrAdd(this, 0x20), 0x100);
    }

    VOID SetTargetIsEnemy(BOOL Is)
    {
        *(PULONG)PtrAdd(*(PULONG_PTR)PtrAdd(this, 0x20), 0xEC) = Is ? 0 : 1;
    }

    ULONG_PTR IsTargetEnemy()
    {
        return *(PULONG)PtrAdd(*(PULONG_PTR)PtrAdd(this, 0x20), 0xEC) != 1;
    }

    VOID SetMonsterInfoFlags(ULONG_PTR Flags)
    {
        *(PULONG_PTR)PtrAdd(this, 0x1028) = Flags;
    }

    MONSTER_INFO_FLAGS GetMonsterInfoFlags()
    {
        return *(PMONSTER_INFO_FLAGS)PtrAdd(this, 0x1028);
    }

    NoInline VOID DrawSimpleText(LONG X, LONG Y, PCSTR Text, ULONG ColorIndex, LONG Weight = FW_NORMAL, ULONG ZeroU1 = 1, FLOAT ZeroF1 = 1)
    {
        TYPE_OF(&CBattleInfoBox::DrawSimpleText) StubDrawSimpleText;

        *(PVOID *)&StubDrawSimpleText = (PVOID)0x67A101;

        return (this->*StubDrawSimpleText)(X, Y, Text, ColorIndex, Weight, ZeroU1, ZeroF1);
    }

public:
    VOID THISCALL SetMonsterInfoBoxSize(LONG X, LONG Y, LONG Width, LONG Height);
    VOID THISCALL DrawMonsterStatus();

    DECL_STATIC_METHOD_POINTER(CBattleInfoBox, DrawMonsterStatus);
};

INIT_STATIC_MEMBER(CBattleInfoBox::StubDrawMonsterStatus);

typedef union
{
    DUMMY_STRUCT(0x78);
    struct
    {
        DUMMY_STRUCT(0x60);

        PMONSTER_STATUS MSData;     // 0x60

        DUMMY_STRUCT(4);

        ULONG   IconAT;             // 0x68 不含20 空; 含10 AT条移动; 含04 行动、delay后的([20A]0销毁); 含40 当前行动的(1销毁)
        USHORT  Flags;                // 0x6C

        DUMMY_STRUCT(3);
        BYTE    RNo;		        // 0x71

        DUMMY_STRUCT(1);

        BYTE    sequence;	        // 0x73
        BOOLEAN IsSBreaking;

        DUMMY_STRUCT(3);
    };

} AT_BAR_ENTRY, *PAT_BAR_ENTRY;

class CBattleATBar
{
public:
    AT_BAR_ENTRY   Entry[0x3C];
    PAT_BAR_ENTRY  EntryPointer[0x3C];      // 0x1C20

    BOOL IsCurrentChrSBreak()
    {
        return EntryPointer[0]->IsSBreaking;
    }

    // -1 for null
    BYTE THISCALL GetChrAT0()
    {
        TYPE_OF(&CBattleATBar::GetChrAT0) f;
        *(PVOID *)&f = (PVOID)0x00677230;
		return (this->*f)();
    }

    VOID AdvanceChrInATBar(PMONSTER_STATUS MSData, BOOL InsertToFirstPos)
    {
        TYPE_OF(&CBattleATBar::AdvanceChrInATBar) AdvanceChrInATBar;

        *(PVOID *)&AdvanceChrInATBar = (PVOID)0x676D3F;

        return (this->*AdvanceChrInATBar)(MSData, InsertToFirstPos);
    }

    NoInline PAT_BAR_ENTRY FindATBarEntry(PMONSTER_STATUS MSData)
    {
        PAT_BAR_ENTRY *Entry;

        FOR_EACH(Entry, EntryPointer, countof(EntryPointer))
        {
            if (Entry[0]->MSData == MSData)
                return Entry[0];
        }

        return NULL;
    }

    PAT_BAR_ENTRY THISCALL LookupReplaceAtBarEntry(PMONSTER_STATUS MSData, BOOL IsFirst);
};

class CBattle
{
public:
    VOID THISCALL SetSelectedAttack(PMONSTER_STATUS MSData);
    VOID THISCALL SetSelectedMagic(PMONSTER_STATUS MSData, USHORT CraftIndex, USHORT CurrentCraftIndex);
    VOID THISCALL SetSelectedCraft(PMONSTER_STATUS MSData, USHORT CraftIndex, USHORT AiIndex);
    VOID THISCALL SetSelectedSCraft(PMONSTER_STATUS MSData, USHORT CraftIndex, USHORT AiIndex);

    CActor* GetActor()
    {
        return *(CActor **)PtrAdd(this, 0x38D28);
    }

    CBattleInfoBox* GetBattleInfoBox()
    {
        return (CBattleInfoBox *)PtrAdd(this, 0xF0D24);
    }

    BOOL IsCustomChar(ULONG_PTR ChrId)
    {
        return GetActor()->IsCustomChar(ChrId);
    }

    EDAO* GetEDAO()
    {
        return *(EDAO **)PtrAdd(this, 0x38D24);
    }

    CBattleATBar* GetBattleATBar()
    {
        return (CBattleATBar *)PtrAdd(this, 0x103148);
    }

    BOOL IsForceInsertToFirst()
    {
        return *(PBOOL)PtrAdd(this, 0x3A7B0);
    }

    PVOID GetMSFileBuffer()
    {
        return PtrAdd(this, 0x114ED0);
    }

    PMONSTER_STATUS GetMonsterStatus()
    {
        return (PMONSTER_STATUS)PtrAdd(this, 0x4DE4);
    }

    LONG_PTR GetCurrentChrIndex()
    {
        return *(PLONG)PtrAdd(this, 0x113080);
    }

    LONG_PTR GetCurrentTargetIndex()
    {
        return *(PLONG)PtrAdd(this, 0x113090);
    }

    VOID ShowConditionText(PMONSTER_STATUS MSData, PCSTR Text, ULONG Color = RGBA(255, 136, 0, 255), ULONG Unknown = 0)
    {
        TYPE_OF(&CBattle::ShowConditionText) ShowConditionText;
        *(PULONG_PTR)&ShowConditionText = 0xA17420;
        return (this->*ShowConditionText)(MSData, Text, Color, Unknown);
    }

    PMS_EFFECT_INFO THISCALL FindEffectInfoByCondition(PMONSTER_STATUS MSData, ULONG_PTR Condition, ULONG_PTR TimeLeft = 0)
    {
        TYPE_OF(&CBattle::FindEffectInfoByCondition) FindEffectInfoByCondition;

        *(PULONG_PTR)&FindEffectInfoByCondition = 0x9E34A0;

        return (this->*FindEffectInfoByCondition)(MSData, Condition, TimeLeft);
    }

    VOID THISCALL ShowSkipAnimeButton()
    {
        DETOUR_METHOD(CBattle, ShowSkipAnimeButton, 0x673513);
    }

    VOID THISCALL CancelAria(PMONSTER_STATUS MSData, BOOL Reset)
    {
        DETOUR_METHOD(CBattle, CancelAria, 0x99DDC0, MSData, Reset);
    }

    VOID THISCALL UpdateHP(PMONSTER_STATUS MSData, LONG Increment, LONG Initial, BOOL What = TRUE)
    {
        TYPE_OF(&CBattle::UpdateHP) UpdateHP;
        *(PULONG_PTR)&UpdateHP = 0x9ED1F0;
        return (this->*UpdateHP)(MSData, Increment, Initial, What);
    }

    /************************************************************************
      bug fix
    ************************************************************************/
    VOID
    THISCALL
    ExecuteActionScript(
        PMONSTER_STATUS MSData,
        PBYTE           ActionScript,
        BYTE            ChrThreadId,
        USHORT          ScriptOffset,
        ULONG           Unknown1,
        ULONG           Unknown2,
        ULONG           Unknown3
    );

    /************************************************************************
      tweak
    ************************************************************************/

    VOID NakedNoResistConditionUp();

    static LONG CDECL FormatBattleChrAT(PSTR Buffer, PCSTR Format, LONG Index, LONG No, LONG IcoAT, LONG ObjAT, LONG Pri);
    static LONG CDECL ShowSkipCraftAnimeButton(...);

    /************************************************************************
      hack for use enemy
    ************************************************************************/

    PMONSTER_STATUS FASTCALL OverWriteBattleStatusWithChrStatus(PMONSTER_STATUS MSData, PCHAR_STATUS ChrStatus);
    VOID NakedOverWriteBattleStatusWithChrStatus();

    VOID NakedIsChrStatusNeedRefresh();
    BOOL FASTCALL IsChrStatusNeedRefresh(ULONG_PTR ChrPosition, PCHAR_STATUS CurrentStatus, ULONG_PTR PrevLevel);

    ULONG NakedGetChrIdForSCraft();

    VOID NakedGetTurnVoiceChrId();
    VOID NakedGetReplySupportVoiceChrId();
    VOID NakedGetRunawayVoiceChrId();
    VOID NakedGetTeamRushVoiceChrId();
    VOID NakedGetUnderAttackVoiceChrId();
    VOID NakedGetUnderAttackVoiceChrId2();
    VOID NakedGetSBreakVoiceChrId();

    ULONG FASTCALL GetVoiceChrIdWorker(PMONSTER_STATUS MSData);

    VOID NakedCopyMagicAndCraftData();
    VOID FASTCALL CopyMagicAndCraftData(PMONSTER_STATUS MSData);



    typedef struct
    {
        BYTE    OpCode;
        BYTE    Function;

        union
        {
            ULONG Param[4];

        };

    } AS_8D_PARAM, *PAS_8D_PARAM;

    enum
    {
        AS_8D_FUNCTION_MINIMUM  = 0x70,

        AS_8D_FUNCTION_REI_JI_MAI_GO    =   AS_8D_FUNCTION_MINIMUM,
    };

    VOID NakedAS8DDispatcher();
    VOID FASTCALL AS8DDispatcher(PMONSTER_STATUS MSData, PAS_8D_PARAM ASBuffer);


    /************************************************************************
      enemy sbreak
    ************************************************************************/

#define THINK_SBREAK_FILTER TAG4('THSB')

    VOID NakedGetBattleState();
    VOID FASTCALL HandleBattleState(ULONG_PTR CurrentState);
    VOID THISCALL SetCurrentActionChrInfo(USHORT Type, PMONSTER_STATUS MSData);

    LONG NakedEnemyThinkAction();
    BOOL FASTCALL EnemyThinkAction(PMONSTER_STATUS MSData);

    BOOL THISCALL ThinkRunaway(PMONSTER_STATUS MSData);
    BOOL THISCALL ThinkSCraft(PMONSTER_STATUS MSData);

    BOOL ThinkSBreak(PMONSTER_STATUS MSData, PAT_BAR_ENTRY Entry);


    /************************************************************************
      acgn beg
    ************************************************************************/

    VOID THISCALL LoadMSFile(PMONSTER_STATUS MSData, ULONG MSFileIndex);
    VOID THISCALL LoadMonsterIt3(ULONG CharPosition, ULONG par2, PSTR it3Path);
    VOID NakedAS_8D_5F();
	VOID THISCALL AS_8D_5F(PMONSTER_STATUS);

    VOID THISCALL UnsetCondition(PMONSTER_STATUS MSData, ULONG condition)
    {
        TYPE_OF(&CBattle::UnsetCondition) f;
        *(PVOID *)&f = (PVOID)0x672AE1;
        return (this->*f)(MSData, condition);
    }

    VOID THISCALL SetCondition(PMONSTER_STATUS MSData, ULONG par2, ULONG condition, ULONG par4, ULONG par5)
    {
        TYPE_OF(&CBattle::SetCondition) f;
        *(PVOID *)&f = (PVOID)0x676EA2;
        return (this->*f)(MSData, par2, condition, par4, par5);
	}

    BOOL CheckCondition(PMONSTER_STATUS MSData, ULONG condition, ULONG par3=0)
    {
        return FindEffectInfoByCondition(MSData, condition, par3) != NULL;
    }


    DECL_STATIC_METHOD_POINTER(CBattle, LoadMSFile);

    /************************************************************************
      acgn end
    ************************************************************************/


    DECL_STATIC_METHOD_POINTER(CBattle, SetCurrentActionChrInfo);
    DECL_STATIC_METHOD_POINTER(CBattle, ThinkRunaway);
    DECL_STATIC_METHOD_POINTER(CBattle, ThinkSCraft);
    DECL_STATIC_METHOD_POINTER(CBattle, ExecuteActionScript);
};

INIT_STATIC_MEMBER(CBattle::StubSetCurrentActionChrInfo);
INIT_STATIC_MEMBER(CBattle::StubThinkRunaway);
INIT_STATIC_MEMBER(CBattle::StubThinkSCraft);
INIT_STATIC_MEMBER(CBattle::StubLoadMSFile);
INIT_STATIC_MEMBER(CBattle::StubExecuteActionScript);

class CSound
{
public:

    VOID THISCALL PlaySound(ULONG SeIndex, ULONG v1 = 1, ULONG v2 = 0, ULONG v3 = 100, ULONG v4 = 0, ULONG v5 = 35, ULONG v6 = 0)
    {
        TYPE_OF(&CSound::PlaySound) PlaySound;

        *(PVOID *)&PlaySound = (PVOID)0x677271;

        return (this->*PlaySound)(SeIndex, v1, v2, v3, v4, v5, v6);
    }
};

typedef struct
{
    USHORT  State;
    BYTE    ScenaIndex;

    DUMMY_STRUCT(1);

    ULONG   FunctionOffset;
    ULONG   CurrentOffset;

} *PSCENA_ENV_BLOCK;

class CScript
{
public:
    EDAO* GetEDAO()
    {
        return (EDAO *)PtrSub(this, 0x384EC);
    }

    CActor* GetActor()
    {
        return *(CActor **)this;
    }

    PBYTE* GetScenaTable()
    {
        return (PBYTE *)PtrAdd(this, 0x7D4);
    }


    BOOL THISCALL ScpSaveRestoreParty(PSCENA_ENV_BLOCK Block);

    VOID FASTCALL InheritSaveData(PBYTE ScenarioFlags);
    VOID NakedInheritSaveData();

    DECL_STATIC_METHOD_POINTER(CScript, InheritSaveData);
    DECL_STATIC_METHOD_POINTER(CScript, ScpSaveRestoreParty);
};

INIT_STATIC_MEMBER(CScript::StubInheritSaveData);
INIT_STATIC_MEMBER(CScript::StubScpSaveRestoreParty);

class EDAO
{
    // battle

public:

    static EDAO* GlobalGetEDAO()
    {
        return *(EDAO **)0xC29988;
    }

    CGlobal* GetGlobal()
    {
        return (CGlobal *)PtrAdd(this, 0x4D3E8);
    }

    CBattle* GetBattle()
    {
        return *(CBattle **)PtrAdd(this, 0x82BA4);
    }

    CSound* GetSound()
    {
        return (CSound *)PtrAdd(this, 0x3A628);
    }

    CScript* GetScript()
    {
        return (CScript *)PtrAdd(this, 0x384EC);
    }

    CActor* GetActor()
    {
        return GetScript()->GetActor();
    }

    BOOL IsCustomChar(ULONG_PTR ChrId)
    {
        return GetActor()->IsCustomChar(ChrId);
    }

    PUSHORT GetSBreakList()
    {
        return (PUSHORT)PtrAdd(this, 0x7EE10);
    }

    ULONG_PTR GetLayer()
    {
        return *(PUSHORT)PtrAdd(this, 0xA6FA8);
    }

    VOID LoadFieldAttackData(ULONG_PTR Dummy = 0)
    {
        TYPE_OF(&EDAO::LoadFieldAttackData) LoadFieldAttackData;
        *(PULONG_PTR)&LoadFieldAttackData = 0x6F8D30;
        return (this->*LoadFieldAttackData)(Dummy);
    }

    LONG THISCALL AoMessageBox(PCSTR Text, BOOL CanUseCancelButton = TRUE)
    {
        typedef struct
        {
            PVOID Callbacks[4];

        } MSGBOX_CALLBACK;

        LONG (FASTCALL *AoMessageBoxWorker)(EDAO*, PVOID, BOOL CanUseCancelButton, PCSTR Text, MSGBOX_CALLBACK, ULONG, ULONG, ULONG);

        MSGBOX_CALLBACK cb = { (PVOID)0x676056, NULL, NULL, NULL };

        *(PULONG_PTR)&AoMessageBoxWorker = 0x67A4D5;
        return AoMessageBoxWorker(this, 0, CanUseCancelButton, Text, cb, 0, 0, -1);
    }

    VOID StubDrawNumber(LONG X, LONG Y, PCSTR Text, ULONG OneU1, ULONG Color, ULONG ZeroU1);

    NoInline VOID DrawNumber(LONG X, LONG Y, PCSTR Text, ULONG_PTR Color, ULONG OneU1 = 1, ULONG ZeroU1 = 0)
    {
        TYPE_OF(&EDAO::StubDrawNumber) StubDrawNumber;

        *(PVOID *)&StubDrawNumber = (PVOID)0x6778E3;

        return (this->*StubDrawNumber)(X, Y, Text, OneU1, Color, ZeroU1);
    }

    VOID THISCALL StubDrawRectangle(USHORT Layer, LONG Left, LONG Top, LONG Right, LONG Bottom, FLOAT ZeroF1, FLOAT ZeroF2, FLOAT ZeroF3, FLOAT ZeroF4, ULONG UpperLeftColor, ULONG UpperRightColor, ULONG ZeroU1,ULONG ZeroU2,ULONG ZeroU3,ULONG ZeroU4,ULONG ZeroU5,ULONG ZeroU6,FLOAT ZeroF5);

    NoInline
    VOID
    THISCALL
    DrawRectangle(
        /* USHORT Layer */
        LONG    Left,
        LONG    Top,
        LONG    Right,
        LONG    Bottom,

        ULONG   UpperLeftColor,
        ULONG   UpperRightColor,

        FLOAT   ZeroF1 = 0,
        FLOAT   ZeroF2 = 0,
        FLOAT   ZeroF3 = 0,
        FLOAT   ZeroF4 = 0,

        ULONG   ZeroU1 = 0,
        ULONG   ZeroU2 = 0,
        ULONG   ZeroU3 = 0,
        ULONG   ZeroU4 = 0,
        ULONG   ZeroU5 = 0,
        ULONG   ZeroU6 = 0,

        FLOAT   ZeroF5 = 0
    )
    {
        TYPE_OF(&EDAO::StubDrawRectangle) StubDrawRectangle;
        *(PVOID *)&StubDrawRectangle = (PVOID)0x6726EA;

        return (PtrAdd(this, 0x254)->*StubDrawRectangle)(
                    GetLayer(),
                    Left,
                    Top,
                    Right,
                    Bottom,

                    ZeroF1,
                    ZeroF2,
                    ZeroF3,
                    ZeroF4,

                    UpperLeftColor,
                    UpperRightColor,

                    ZeroU1,
                    ZeroU2,
                    ZeroU3,
                    ZeroU4,
                    ZeroU5,
                    ZeroU6,

                    ZeroF5
                );
    }

    VOID CalcChrRawStatusFromLevel(ULONG ChrId, ULONG Level, ULONG Unknown = 0)
    {
        TYPE_OF(&EDAO::CalcChrRawStatusFromLevel) f;

        *(PVOID *)&f = (PVOID)0x675FF7;

        return (this->*f)(ChrId, Level, Unknown);
    }

    VOID NakedGetChrSBreak();
    VOID FASTCALL GetChrSBreak(PMONSTER_STATUS MSData);


    /************************************************************************
      tweak
    ************************************************************************/

    static VOID NakedLoadSaveDataThumb();
    static VOID NakedSetSaveDataScrollStep();

    // hook
public:
    VOID THISCALL Fade(ULONG Param1, ULONG Param2, ULONG Param3, ULONG Param4, ULONG Param5, ULONG Param6);
    BOOL THISCALL CheckItemEquipped(ULONG ItemId, PULONG EquippedIndex);

    DECL_STATIC_METHOD_POINTER(EDAO, CheckItemEquipped);
};

DECL_SELECTANY TYPE_OF(EDAO::StubCheckItemEquipped) EDAO::StubCheckItemEquipped = NULL;


class CGlobal
{
public:
    PCRAFT_INFO    THISCALL GetMagicData(USHORT MagicId);
    PCSTR           THISCALL GetMagicDescription(USHORT MagicId);
    PBYTE           THISCALL GetMagicQueryTable(USHORT MagicId);

    EDAO* GetEDAO()
    {
        return (EDAO *)PtrSub(this, 0x4D3E8);
    }

    BOOL IsCustomChar(ULONG_PTR ChrId)
    {
        return GetEDAO()->GetActor()->IsCustomChar(ChrId);
    }

    PCHAR_STATUS GetChrStatus(ULONG_PTR ChrId)
    {
        return &((PCHAR_STATUS)PtrAdd(this, 0x2BBBC))[ChrId];
    }

    VOID CalcChrFinalStatus(ULONG ChrId, PCHAR_STATUS FinalStatus, PCHAR_STATUS RawStatus)
    {
        TYPE_OF(&CGlobal::CalcChrFinalStatus) f;

        *(PVOID *)&f = (PVOID)0x677B36;

        return (this->*f)(ChrId, FinalStatus, RawStatus);
    }

    static TYPE_OF(&CGlobal::GetMagicData)          StubGetMagicData;
    static TYPE_OF(&CGlobal::GetMagicDescription)   StubGetMagicDescription;
    static TYPE_OF(&CGlobal::GetMagicQueryTable)    StubGetMagicQueryTable;
};

DECL_SELECTANY TYPE_OF(CGlobal::StubGetMagicData)           CGlobal::StubGetMagicData = NULL;
DECL_SELECTANY TYPE_OF(CGlobal::StubGetMagicDescription)    CGlobal::StubGetMagicDescription = NULL;
DECL_SELECTANY TYPE_OF(CGlobal::StubGetMagicQueryTable)     CGlobal::StubGetMagicQueryTable = NULL;



class CSSaveData
{
public:
    VOID SaveData2SystemData();
    VOID SystemData2SaveData();
};

class EDAOFileStream
{
public:
    ULONG THISCALL Read(PVOID Buffer, ULONG Size, ULONG Count = 1, ULONG Unknown = 0, ULONG Unknown2 = 0)
    {
        TYPE_OF(&EDAOFileStream::Read) StubRead;

        *(PVOID *)&StubRead = (PVOID)0x6725AA;

        return (this->*StubRead)(Buffer, Size, Count, Unknown, Unknown2);
    }

    BOOL THISCALL Seek(LONG Offset, ULONG SeekMethod)
    {
        TYPE_OF(&EDAOFileStream::Seek) StubSeek;

        *(PVOID *)&StubSeek = (PVOID)0x675787;
        return (this->*StubSeek)(Offset, SeekMethod);
    }

    ULONG THISCALL Uncompress(PVOID Output, ULONG BlockSize, ULONG BlockCount)
    {
        LONG_PTR            BytesRead;
        PVOID               Buffer;
        UCL_COMPRESS_HEADER Header;

        static PVOID        StaticBuffer;
        static ULONG_PTR    StaticBufferSize;

        ULONG pos = m_Position;

        BytesRead = Read(&Header, sizeof(Header));
        if (BytesRead != sizeof(Header) || Header.Magic != UCL_COMPRESS_MAGIC)
        {
            Seek(-BytesRead, SEEK_CUR);
            m_Position = pos;

            return (this->*StubUncompress)(Output, BlockSize, BlockCount);
        }

        Buffer = StaticBuffer;
        if (Header.CompressedSize > StaticBufferSize)
        {
            StaticBufferSize = Header.CompressedSize;
            Buffer = ReAllocateMemoryP(Buffer, StaticBufferSize);
            StaticBuffer = Buffer;
        }

        if (Buffer == NULL)
            return 0;

        Read(Buffer, Header.CompressedSize);

        UCL_NRV2E_Decompress(Buffer, Header.CompressedSize, Output, &BlockSize);

        return BlockSize;
    }

    static TYPE_OF(&EDAOFileStream::Uncompress) StubUncompress;

    CHAR    m_FileName[0x24];   // 0x00
    ULONG   m_Position;         // 0x24
    ULONG   m_Size;             // 0x28
    DUMMY_STRUCT(0x54);         // 0x2C
    BYTE    m_BufferIndex;
    BYTE    m_BufferFlags;
};

DECL_SELECTANY TYPE_OF(EDAOFileStream::StubUncompress) EDAOFileStream::StubUncompress = NULL;



#endif // _EDAO_H_5c8a3013_4334_4138_9413_3d0209da878e_
