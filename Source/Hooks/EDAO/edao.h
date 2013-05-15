#ifndef _EDAO_H_5c8a3013_4334_4138_9413_3d0209da878e_
#define _EDAO_H_5c8a3013_4334_4138_9413_3d0209da878e_

#include "MyLibrary.h"

class EDAO;
class CGlobal;
class CBattle;

#define INIT_STATIC_MEMBER(x) DECL_SELECTANY TYPE_OF(x) x = NULL

#define DECL_STATIC_METHOD_POINTER(cls, method) static TYPE_OF(&cls::method) Stub##method

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

} CREATE_INFO, *PCREATE_INFO;

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

        DUMMY_STRUCT(4);

        USHORT                  MaximumCP;                  // 0x25C

        DUMMY_STRUCT(2);                                    // 0x25E

        USHORT                  RNG;                        // 0x260

        DUMMY_STRUCT(2);
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

} MS_EFFECT_INFO;

typedef union
{
    DUMMY_STRUCT(0x2424);

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

        DUMMY_STRUCT(0x172 - 0x18);

        USHORT                  ActionType;                 // 0x172

        DUMMY_STRUCT(0x8);

        USHORT                  WhoAttackMe;                // 0x17C
        USHORT                  CurrentCraftIndex;          // 0x17E
        USHORT                  LastActionIndex;            // 0x180
        USHORT                  CurrentAiIndex;             // 0x182

        DUMMY_STRUCT(0x234 - 0x184);

        CHAR_STATUS ChrStatus[2];                           // 0x234

        USHORT MoveSPD;                                     // 0x29C

        DUMMY_STRUCT(2);

        MS_EFFECT_INFO          EffectInfo[0x14];           // 0x2A0

        DUMMY_STRUCT(0x54C - 0x430);

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

        CREATE_INFO                 CraftInfo[16];          // 0xF2C
        CRAFT_DESCRIPTION           CraftDescription[10];   // 0x10EC

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

    PMONSTER_STATUS FASTCALL OverWriteBattleStatusWithChrStatus(PMONSTER_STATUS MSData, PCHAR_STATUS ChrStatus);
    VOID NakedOverWriteBattleStatusWithChrStatus();

    VOID NakedIsChrStatusNeedRefresh();
    BOOL FASTCALL IsChrStatusNeedRefresh(ULONG_PTR ChrPosition, PCHAR_STATUS CurrentStatus, ULONG_PTR PrevLevel);

    ULONG NakedGetChrIdForSCraft();

    VOID NakedGetTurnVoiceChrId();
    VOID NakedGetReplySupportVoiceChrId();
    VOID NakedGetRunawayVoiceChrId();
    VOID NakedGetTeamRushVoiceChrId();
    VOID NakedGetSBreakVoiceChrId();

    ULONG FASTCALL GetVoiceChrIdWorker(PMONSTER_STATUS MSData);

    VOID NakedCopyMagicAndCraftData();
    VOID FASTCALL CopyMagicAndCraftData(PMONSTER_STATUS MSData);

    BOOL ThinkSBreak(PMONSTER_STATUS MSData);
};

class EDAO
{
    // battle

public:
    CGlobal* GetGlobal()
    {
        return (CGlobal *)PtrAdd(this, 0x4D3E8);
    }

    CBattle* GetBattle()
    {
        return *(CBattle **)PtrAdd(this, 0x82BA4);
    }

    CActor* GetActor()
    {
        return *(CActor **)PtrAdd(this, 0x384EC);
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

    // hook
public:
    VOID THISCALL Fade(ULONG Param1, ULONG Param2, ULONG Param3, ULONG Param4, ULONG Param5, ULONG Param6);
    BOOL THISCALL CheckItemEquipped(ULONG ItemId, PULONG EquippedIndex);

    static TYPE_OF(&EDAO::Fade)                 StubFade;
    static TYPE_OF(&EDAO::CheckItemEquipped)    StubCheckItemEquipped;
};

DECL_SELECTANY TYPE_OF(EDAO::StubFade) EDAO::StubFade = NULL;
DECL_SELECTANY TYPE_OF(EDAO::StubCheckItemEquipped) EDAO::StubCheckItemEquipped = NULL;


class CGlobal
{
public:
    PCREATE_INFO    THISCALL GetMagicData(USHORT MagicId);
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



LONG CDECL FormatBattleChrAT(PSTR Buffer, PCSTR Format, LONG Index, LONG No, LONG IcoAT, LONG ObjAT, LONG Pri);


#endif // _EDAO_H_5c8a3013_4334_4138_9413_3d0209da878e_
