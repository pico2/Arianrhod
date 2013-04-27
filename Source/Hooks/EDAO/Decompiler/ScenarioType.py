
'''

version = ED_AO

enum CHIP_TYPE
{
    CHIP_TYPE_CHAR      = 7,
    CHIP_TYPE_APL       = 8,
    CHIP_TYPE_MONSTER   = 9,
};

enum SCN_INFO_INDEX
{
    SCN_INFO_CHIP                   = 0,        // ULONG, num <= 0x80
    SCN_INFO_NPC_POSITION           = 1,        // SCENARIO_CHAR_INFORMATION, num <= 0x80
    SCN_INFO_MONSTER_POSITION       = 2,        // SCENARIO_CHAR_INFORMATION, num <= 0x80
    SCN_INFO_SCP_INFO               = 3,        // ??, size = 0x60
    SCN_INFO_UNKNOWN1               = 4,        // size = 0x24

    SCN_INFO_MAXIMUM                = 5,
};

typedef struct  // 0x1C
{
/* 0x00 */  ULONG   X;
/* 0x04 */  ULONG   Y;
/* 0x08 */  ULONG   Z;
/* 0x0C */  USHORT  Unknown1;
/* 0x0E */  USHORT  Unknown2;
/* 0x10 */  UCHAR   Unknown[4];

/* 0x14 */  UCHAR   InitScenaIndex;
/* 0x15 */  UCHAR   InitSectionIndex;
/* 0x16 */  UCHAR   TalkScenaIndex;
/* 0x17 */  UCHAR   TalkSectionIndex;
/* 0x18 */  USHORT  Unknown4;
/* 0x1A */  USHORT  Unknown5;

} SCENARIO_CHAR_INFORMATION;

7B8 - sn buf

3A  -   7C0
3C  -   7C4
3E  -   7C8
40  -   7CC

#define INVALID_SCN_INFO_NUMBER        -1
#define MINIMUM_CHAR_NUMBER             8

typedef struct  // 0x40
{
/* 0x00 */  UCHAR Dummy[0x3E];
/* 0x3E */  UCHAR EntryScenaIndex;
/* 0x3F */  UCHAR EntrySectionIndex;

} SCENARIO_INFORMATION;

typedef struct
{
    USHORT Offset;
    USHORT Size;

} SCENARIO_ENTRY;

typedef struct
{
/* 0x00 */   CHAR                     MapName[0xA];                       // %s/%s/%s.it3
/* 0x0A */   CHAR                     Location[0xA];
/* 0x14 */   ULONG                    Unknown1;
/* 0x18 */   ULONG                    Flags;
/* 0x1C */   ULONG                    IncludedScenarioFileIndex[6];
/* 0x34 */   ULONG                    CharNameOffset;
/* 0x38 */   USHORT                   ScnInfoOffset[SCN_INFO_MAXIMUM];
/* 0x42 */   SCENARIO_ENTRY           ScenaSectionTable;
/* 0x46 */   SCENARIO_ENTRY           UnknownEntry1;                      // ???
/* 0x4A */   UCHAR                    Unknown2;
/* 0x4B */   UCHAR                    PreInitSectionIndex;
/* 0x4C */   CHAR                     ScnInfoNumber[SCN_INFO_MAXIMUM];
/* 0x54 */   SCENARIO_INFORMATION     Information;

} SCENARIO_HEADER;

op count: 227

'''


class ScenarioInfo:
    def __init__(self):
        pass

    def open(self, buf):
        pass

