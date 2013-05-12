#ifndef _EDAO_H_5c8a3013_4334_4138_9413_3d0209da878e_
#define _EDAO_H_5c8a3013_4334_4138_9413_3d0209da878e_

#include "MyLibrary.h"

class EDAO;

#define UCL_COMPRESS_MAGIC TAG4('UCL4')

#define MINIMUM_CUSTOM_CHAR_ID      0xB0
#define MINIMUM_CUSTOM_CRAFT_INDEX  0x3E8

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
    BYTE    MagicAriaActionIndex;
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

        DUMMY_STRUCT(0x17C - 0x18);

        USHORT                  WhoAttackMe;                // 0x17C
        USHORT                  CurrentActionIndex;         // 0x17E
        USHORT                  LastActionIndex;            // 0x180
        USHORT                  CurrentCraftIndex;          // 0x182

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
            BYTE                    MagicAriaActionIndex;   // 0xF26
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
};

class CBattle
{
public:
    VOID USE_ATTACK_FOR_CHECKING();
    VOID USE_MAGIC_FOR_CHECKING();
    VOID USE_CRAFT_FOR_CHECKING();
    VOID USE_SCRAFT_FOR_CHECKING();

    CActor* GetActor()
    {
        return *(CActor **)PtrAdd(this, 0x38D28);
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

    ULONG_PTR GetCurrentChrIndex()
    {
        return *(PULONG)PtrAdd(this, 0x113080);
    }

    VOID OverWriteCraftWithChrCraft();
    PMONSTER_STATUS FASTCALL OverWriteBattleStatusWithChrStatus(PMONSTER_STATUS MSData, PCHAR_STATUS ChrStatus);
    VOID NakedOverWriteBattleStatusWithChrStatus();

    VOID NakedIsChrStatusNeedRefresh();
    BOOL FASTCALL IsChrStatusNeedRefresh(ULONG_PTR ChrPosition, PCHAR_STATUS CurrentStatus, ULONG_PTR PrevLevel);

    ULONG GetChrIdForSCraft();

    VOID NakedGetTurnVoiceChrId();
    VOID NakedGetReplySupportVoiceChrId();
    VOID NakedGetRunawayVoiceChrId();
    VOID NakedGetTeamRushVoiceChrId();
    VOID NakedGetSBreakVoiceChrId();

    ULONG FASTCALL GetVoiceChrIdWorker(PMONSTER_STATUS MSData);

    VOID NakedGetPredefinedMagicNumber();
    ULONG FASTCALL GetPredefinedMagicNumber(PMONSTER_STATUS MSData);
};

class CGlobal
{
public:
    PCREATE_INFO    GetMagicData(USHORT MagicId);
    PCSTR           GetMagicDescription(USHORT MagicId);
    PBYTE           GetMagicQueryTable(USHORT MagicId);

    EDAO* GetEDAO()
    {
        return (EDAO *)PtrSub(this, 0x4D3E8);
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
        return (CActor *)PtrAdd(this, 0x384EC);
    }

    PUSHORT GetSBreakList()
    {
        return (PUSHORT)PtrAdd(this, 0x7EE10);
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
