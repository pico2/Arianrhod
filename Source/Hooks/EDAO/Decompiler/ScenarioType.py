
'''

version = ED_AO

enum OFFSET_TABLE_INDEX
{
    OffsetCharName,
    OffsetUnknown1,
};

7B8 - sn buf

3A  -   7C0
3C  -   7C4
3E  -   7C8
40  -   7CC


/* 0x00000000 */   CHAR    Location[0xA];
/* 0x0000000A */   CHAR    ModuleName[0xA];
/* 0x00000014 */   ULONG   Unknown1;
/* 0x00000018 */   ULONG   Flags;
/* 0x0000001C */   ULONG   IncludedScenarioFileIndex[6];
/* 0x00000034 */   USHORT  OffsetTable[8]; // OFFSET_TABLE_INDEX

'''


class ScenarioInfo:
    def __init__(self):
        pass

    def open(self, buf):
        pass

