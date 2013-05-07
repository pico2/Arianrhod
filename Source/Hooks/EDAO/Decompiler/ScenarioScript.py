from BaseType import *
from Assembler import *
from EDAOBase import *
import ScenaOpTableEDAO as edao

CODE_PAGE = edao.CODE_PAGE

'''

version = ED_AO

enum CHIP_TYPE
{
    CHIP_TYPE_CHAR      = 7,
    CHIP_TYPE_APL       = 8,
    CHIP_TYPE_MONSTER   = 9,
};

total actor <= 0x80

enum SCN_INFO_INDEX
{
    SCN_INFO_CHIP       = 0,        // ULONG
    SCN_INFO_NPC        = 1,        // SCENARIO_NPC
    SCN_INFO_MONSTER    = 2,        // SCENARIO_MONSTER
    SCN_INFO_EVENT      = 3,        // SCENARIO_EVENT
    SCN_INFO_ACTOR      = 4,        // SCENARIO_ACTOR

    SCN_INFO_MAXIMUM    = 5,
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
/* 0x15 */  UCHAR   InitFunctionIndex;
/* 0x16 */  UCHAR   TalkScenaIndex;
/* 0x17 */  UCHAR   TalkFunctionIndex;
/* 0x18 */  USHORT  Unknown4;
/* 0x1A */  USHORT  Unknown5;

} SCENARIO_NPC;

typedef struct  // 0x20
{
/* 0x00 */    ULONG   X;
/* 0x04 */    ULONG   Y;
/* 0x08 */    ULONG   Z;
/* 0x0C */    ULONG   Unknown_0C;
/* 0x10 */    USHORT  BattleInfoOffset;
/* 0x12 */    USHORT  Unknown_12;
/* 0x14 */    USHORT  ChipIndex;
/* 0x16 */    USHORT  Unknown_16;
/* 0x18 */    ULONG   Unknown_18;
/* 0x1C */    ULONG   Unknown_1C;

} SCENARIO_MONSTER;

typedef struct  // 0x60
{
    UCHAR Dummy[0x60];

} SCENARIO_EVENT;

typedef struct  // 0x24
{
    UCHAR Dummy[0x24];

} SCENARIO_ACTOR;

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
/* 0x3F */  UCHAR EntryFunctionIndex;

} SCENARIO_INFORMATION;

typedef struct
{
    USHORT Offset;
    USHORT Size;

} SCENARIO_ENTRY;

typedef struct
{
/* 0x00 */   CHAR                     MapName[0xA];                         // %s/%s/%s.it3
/* 0x0A */   CHAR                     Location[0xA];
/* 0x14 */   ULONG                    Unknown_14;
/* 0x18 */   ULONG                    Flags;
/* 0x1C */   ULONG                    IncludedScenario[6];
/* 0x34 */   ULONG                    StringTableOffset;                    // multi-sz, max-len = 0x20
/* 0x38 */   USHORT                   ScnInfoOffset[SCN_INFO_MAXIMUM];
/* 0x42 */   SCENARIO_ENTRY           ScenaFunctionTable;
/* 0x46 */   USHORT                   ChipFrameInfoOffset;
/* 0x48 */   USHORT                   PlaceNameOffset;                        // ???
/* 0x4A */   UCHAR                    PlaceNameNumber;
/* 0x4B */   UCHAR                    PreInitFunctionIndex;
/* 0x4C */   CHAR                     ScnInfoNumber[SCN_INFO_MAXIMUM];
/* 0x51 */   UCHAR                    Unknown_51[3];
/* 0x54 */   SCENARIO_INFORMATION     Information;

} SCENARIO_HEADER;

op count: 227

'''


NUMBER_OF_INCLUDE_FILE          = 6

SCN_INFO_CHIP       = 0
SCN_INFO_NPC        = 1
SCN_INFO_MONSTER    = 2
SCN_INFO_EVENT      = 3
SCN_INFO_ACTOR      = 4
SCN_INFO_MAXIMUM    = 5

class ScenarioEntry:
    def __init__(self, offset = 0, size = 0):
        self.Offset = offset
        self.Size = size

class ScenarioNpcInfo:
    def __init__(self, fs = None):
        if fs == None:
            return

        # size = 0x1C

        self.X                  = fs.ulong()
        self.Z                  = fs.ulong()
        self.Y                  = fs.ulong()
        self.Direction          = fs.ushort()   # 0 90 270 360
        self.Unknown2           = fs.ushort()

        self.ChipIndex          = fs.byte()
        self.Unknown_11         = fs.byte()
        self.NpcIndex           = fs.byte()
        self.Unknown_14         = fs.byte()

        self.InitScenaIndex     = fs.byte()
        self.InitFunctionIndex  = fs.byte()
        self.TalkScenaIndex     = fs.byte()
        self.TalkFunctionIndex  = fs.byte()

        self.Unknown4           = fs.ushort()
        self.Unknown5           = fs.ushort()

    def __str__(self):
        return str(self.binary())

    def param(self):
        return '%d, %d, %d, %d, %d, 0x%X, %d, %d, %d, %d, %d, %d, %d, %d, %d' % (
                    LONG(self.X).value,
                    LONG(self.Z).value,
                    LONG(self.Y).value,
                    LONG(self.Direction).value,
                    LONG(self.Unknown2).value,
                    ULONG(self.ChipIndex).value,
                    LONG(self.Unknown_11).value,
                    LONG(self.NpcIndex).value,
                    LONG(self.Unknown_14).value,
                    LONG(self.InitScenaIndex).value,
                    LONG(self.InitFunctionIndex).value,
                    LONG(self.TalkScenaIndex).value,
                    LONG(self.TalkFunctionIndex).value,
                    LONG(self.Unknown4).value,
                    LONG(self.Unknown5).value
                )

    def binary(self):
        return struct.pack('<LLLHHBBBBBBBBHH',
                    ULONG(self.X).value,
                    ULONG(self.Z).value,
                    ULONG(self.Y).value,
                    ULONG(self.Direction).value,
                    ULONG(self.Unknown2).value,
                    ULONG(self.ChipIndex).value,
                    ULONG(self.Unknown_11).value,
                    ULONG(self.NpcIndex).value,
                    ULONG(self.Unknown_14).value,
                    ULONG(self.InitScenaIndex).value,
                    ULONG(self.InitFunctionIndex).value,
                    ULONG(self.TalkScenaIndex).value,
                    ULONG(self.TalkFunctionIndex).value,
                    ULONG(self.Unknown4).value,
                    ULONG(self.Unknown5).value
                )

class BattleSepith:

    # size = 7

    def __init__(self, fs = None):
        self.Value = []

        if fs == None:
            for i in range(7):
                self.Value.append(0)
            return

        self.Offset = fs.tell()

        for i in range(7):
            self.Value.append(fs.byte())

    def param(self):
        p = []
        for v in self.Value:
            p.append('%d' % v)

        return ', '.join(p)

    def binary(self):
        return struct.pack('<' + 'B' * len(self.Value), *self.Value)

class BattleATBonus:

    # size = 0x10

    def __init__(self, fs = None):
        if fs == None:
            return

        self.Offset     = fs.tell()

        self.Nothing    = fs.byte()
        self.HP_HEAL_10 = fs.byte()
        self.HP_HEAL_50 = fs.byte()
        self.EP_HEAL_10 = fs.byte()
        self.EP_HEAL_50 = fs.byte()
        self.CP_HEAL_10 = fs.byte()
        self.CP_HEAL_50 = fs.byte()
        self.SEPITH     = fs.byte()
        self.CRITICAL   = fs.byte()
        self.VANISH     = fs.byte()
        self.DEATH      = fs.byte()
        self.GUARD      = fs.byte()
        self.RUSH       = fs.byte()
        self.ARTS_GUARD = fs.byte()
        self.TEAMRUSH   = fs.byte()
        self.Unknown    = fs.byte()

    def param(self):
        return '"ATBonus_%X", %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d' % (
                    self.Offset,
                    self.Nothing,
                    self.HP_HEAL_10,
                    self.HP_HEAL_50,
                    self.EP_HEAL_10,
                    self.EP_HEAL_50,
                    self.CP_HEAL_10,
                    self.CP_HEAL_50,
                    self.SEPITH,
                    self.CRITICAL,
                    self.VANISH,
                    self.DEATH,
                    self.GUARD,
                    self.RUSH,
                    self.ARTS_GUARD,
                    self.TEAMRUSH,
                    self.Unknown
                )

    def __str__(self):
        return str(self.binary())

    def binary(self):
        return struct.pack(
                    '<' + 'B' * 0x10,
                    self.Nothing,
                    self.HP_HEAL_10,
                    self.HP_HEAL_50,
                    self.EP_HEAL_10,
                    self.EP_HEAL_50,
                    self.CP_HEAL_10,
                    self.CP_HEAL_50,
                    self.SEPITH,
                    self.CRITICAL,
                    self.VANISH,
                    self.DEATH,
                    self.GUARD,
                    self.RUSH,
                    self.ARTS_GUARD,
                    self.TEAMRUSH,
                    self.Unknown
                )

class BattleMonsterPostion:

    # size = 4

    def __init__(self, fs = None):
        if fs == None:
            return

        self.Offset = fs.tell()

        self.X      = fs.byte()
        self.Y      = fs.byte()
        self.Degree = fs.ushort()

    def __str__(self):
        return str(self.binary())

    def binary(self):
        return struct.pack('<BBH', self.X, self.Y, self.Degree)

    def param(self):
        return '"MonsterBattlePostion_%X", %d, %d, %d' % (self.Offset, self.X, self.Y, self.Degree)

class BattleMonsterInfo:

    # size = 0x2C

    def __init__(self, fs = None):
        if fs == None:
            self.MsFileIndex = [BattleScriptFileIndex()] * 8
            return

        self.Offset = fs.tell()

        self.MsFileIndex = []
        for i in range(8):
            self.MsFileIndex.append(BattleScriptFileIndex(fs.ulong()))

        self.PositionNormalOffset           = fs.ushort()
        self.PositionEnemyAdvantageOffset   = fs.ushort()
        self.BgmNormal                      = fs.ushort()
        self.BgmDanger                      = fs.ushort()
        self.ATBonusOffset                  = fs.ulong()

        pos = fs.tell()

        self.PositionNormal = []
        fs.seek(self.PositionNormalOffset)
        for i in range(len(self.MsFileIndex)):
            self.PositionNormal.append(BattleMonsterPostion(fs))

        self.PositionEnemyAdvantage = []
        fs.seek(self.PositionEnemyAdvantageOffset)
        for i in range(len(self.MsFileIndex)):
            self.PositionEnemyAdvantage.append(BattleMonsterPostion(fs))

        fs.seek(self.ATBonusOffset)
        self.ATBonus = BattleATBonus(fs)

        fs.seek(pos)

    def param(self):
        p = ''
        for ms in self.MsFileIndex:
            name = '0' if ms.IsZero() else ('"%s"' % ms.Name())
            p += '%s, ' % name

        return p + '"MonsterBattlePostion_%X", "MonsterBattlePostion_%X", "ed7%d.ogg", "ed7%d.ogg", "ATBonus_%X"' % (
                    self.PositionNormalOffset,
                    self.PositionEnemyAdvantageOffset,
                    self.BgmNormal,
                    self.BgmDanger,
                    self.ATBonusOffset
                )

    def binary(self):
        if len(self.MsFileIndex) != 8:
            raise Exception('incorrect ms file count')

        buf = b''
        for i in self.MsFileIndex:
            buf += struct.pack('<L', i.Index())

        return buf + struct.pack('<HHHHL', self.PositionNormalOffset, self.PositionEnemyAdvantageOffset, self.BgmNormal, self.BgmDanger, self.ATBonusOffset)

class ScenarioBattleInfo:

    # size = 0x18

    def binary(self):
        return struct.pack(
                    '<HHBBBBHHLLBBBB',
                    self.Flags,
                    self.Level,
                    self.Unknown_04,
                    self.Vision,
                    self.MoveRange,
                    self.CanMove,
                    self.MoveSpeed,
                    self.Unknown_0A,
                    self.BattleMapOffset,
                    self.SepithOffset,
                    self.Probability[0],
                    self.Probability[1],
                    self.Probability[2],
                    self.Probability[3]
                )

    def __init__(self, fs = None):
        if fs == None:
            return

        self.Offset             = fs.tell()

        self.Flags              = fs.ushort()
        self.Level              = fs.ushort()
        self.Unknown_04         = fs.byte()
        self.Vision             = fs.byte()
        self.MoveRange          = fs.byte()
        self.CanMove            = fs.byte()
        self.MoveSpeed          = fs.ushort()
        self.Unknown_0A         = fs.ushort()
        self.BattleMapOffset    = fs.ulong()
        self.SepithOffset       = fs.ulong()
        self.Probability        = [ fs.byte(), fs.byte(), fs.byte(), fs.byte() ]

        pos = fs.tell()

        fs.seek(self.BattleMapOffset)
        self.BattleMap = fs.astr()

        self.Sepith = None
        if self.SepithOffset != 0:
            fs.seek(self.SepithOffset)
            self.Sepith = BattleSepith(fs)

        fs.seek(pos)

        self.MonsterBattleInfo = []
        for p in self.Probability:
            if p == 0:
                self.MonsterBattleInfo.append(BattleMonsterInfo())
                continue

            self.MonsterBattleInfo.append(BattleMonsterInfo(fs))

        fs.seek(pos)

    def param(self):
        sepithfmt = '"Sepith_%X"' if self.Sepith != None else '0x%08X'
        return ('"BattleInfo_%X", 0x%04X, %d, %d, %d, %d, %d, %d, %d, "%s", ' + sepithfmt + ', %d, %d, %d, %d') % (
                    ULONG(self.Offset).value,
                    LONG(self.Flags).value,
                    LONG(self.Level).value,
                    LONG(self.Unknown_04).value,
                    LONG(self.Vision).value,
                    LONG(self.MoveRange).value,
                    LONG(self.CanMove).value,
                    LONG(self.MoveSpeed).value,
                    LONG(self.Unknown_0A).value,
                    self.BattleMap,
                    ULONG(self.SepithOffset).value,
                    LONG(self.Probability[0]).value,
                    LONG(self.Probability[1]).value,
                    LONG(self.Probability[2]).value,
                    LONG(self.Probability[3]).value
                )

class ScenarioChipFrameInfo:

    # size = 0xC

    def __init__(self, fs = None):
        if fs == None:
            return

        self.Offset = fs.tell()

        self.Speed          = fs.ushort()
        self.Reserve        = fs.byte()
        self.SubChipCount   = fs.byte()
        self.SubChipIndex   = struct.unpack('<' + 'B' * self.SubChipCount, fs.read(self.SubChipCount))

        if self.SubChipCount != 8:
            fs.seek(8 - self.SubChipCount, io.SEEK_CUR)

    def param(self):
        s = ''
        if len(self.SubChipIndex) != 0:
            s = ', ('
            for idx in self.SubChipIndex:
                s += '%d, ' % idx

            s = s[:-2] + ')'

        return ('%d, %d' % (self.Speed, self.Reserve)) + s

    def binary(self):
        buf = struct.pack('<HBB' + 'B' * len(self.SubChipIndex), self.Speed, self.Reserve, len(self.SubChipIndex), *self.SubChipIndex)

        if len(buf) < 0xC:
            buf += b'\x00' * (0xC - len(buf))
        elif len(buf) > 0xC:
            raise Exception('too long')

        return buf

class ScenarioMonsterInfo:
    def __init__(self, fs = None):
        if fs == None:
            return

        # size = 0x20

        self.X                      = fs.ulong()
        self.Z                      = fs.ulong()
        self.Y                      = fs.ulong()
        self.Unknown_0C             = fs.ulong()
        self.BattleInfoOffset       = fs.ushort()
        self.Unknown_12             = fs.ushort()
        self.ChipIndex              = fs.ushort()
        self.Unknown_16             = fs.ushort()
        self.StandFrameInfoIndex    = fs.ulong()
        self.MoveFrameInfoIndex     = fs.ulong()

        pos = fs.tell()
        fs.seek(self.BattleInfoOffset)
        self.BattleInfo = ScenarioBattleInfo(fs)
        fs.seek(pos)

    def __str__(self):
        return str(self.binary())

    def param(self):
        return '%d, %d, %d, 0x%X, "BattleInfo_%X", %d, %d, %d, %d, %d' % (
                    LONG(self.X).value,
                    LONG(self.Y).value,
                    LONG(self.Z).value,
                    ULONG(self.Unknown_0C).value,
                    ULONG(self.BattleInfoOffset).value,
                    LONG(self.Unknown_12).value,
                    LONG(self.ChipIndex).value,
                    LONG(self.Unknown_16).value,
                    LONG(self.StandFrameInfoIndex).value,
                    LONG(self.MoveFrameInfoIndex).value
                )

    def binary(self):
        return struct.pack('<LLLLHHHHLL', 
                    ULONG(self.X).value,
                    ULONG(self.Y).value,
                    ULONG(self.Z).value,
                    ULONG(self.Unknown_0C).value,
                    ULONG(self.BattleInfoOffset).value,
                    ULONG(self.Unknown_12).value,
                    ULONG(self.ChipIndex).value,
                    ULONG(self.Unknown_16).value,
                    ULONG(self.StandFrameInfoIndex).value,
                    ULONG(self.MoveFrameInfoIndex).value
                )

class ScenarioEventInfo:
    # 0x60 bytes
    def __init__(self, fs = None):
        if fs == None:
            return

        self.Binary = fs.read(0x60)

    def __str__(self):
        return str(self.Binary)

    def param(self):
        return self.__str__()

    def binary(self):
        return self.Binary

class ScenarioActorInfo:
    def __init__(self, fs = None):
        if fs == None:
            return

        self.Binary = fs.read(0x24)

    def __str__(self):
        return str(self.Binary)

    def param(self):
        return self.__str__()

    def binary(self):
        return self.Binary

class ScenarioPlaceNameInfo:

    # size = 0x14

    def __init__(self, fs = None):
        if fs == None:
            return

        self.X          = fs.float()
        self.Z          = fs.float()
        self.Y          = fs.float()
        self.Flags1     = fs.ushort()
        self.Flags2     = fs.ushort()
        self.NameOffset = fs.ulong()

        pos = fs.tell()
        fs.seek(self.NameOffset)

        self.Name = fs.astr()

        fs.seek(pos)

    def param(self):
        return '%s, %s, %s, 0x%04X, 0x%04X, "%s"' % (self.X, self.Z, self.Y, self.Flags1, self.Flags2, self.Name)

    def binary(self):
        return struct.pack('<fffHHL', self.X, self.Z, self.Y, self.Flags1, self.Flags2, self.NameOffset)

class ScenarioInfo:
    def __init__(self):
        # file header

        self.MapName                    = ''
        self.Location                   = ''
        self.Unknown_14                 = 0
        self.Flags                      = 0
        self.IncludedScenario           = []
        self.StringTableOffset          = 0
        self.ScnInfoOffset              = []
        self.ScenaFunctionTable         = ScenarioEntry()
        self.ChipFrameInfoOffset        = 0
        self.PlaceNameOffset            = 0
        self.PlaceNameNumber            = 0
        self.PreInitFunctionIndex       = 0
        self.ScnInfoNumber              = []
        self.Unknown_51                 = b''
        self.Information                = b''

        # file header end

        self.ScenaFunctions     = []
        self.PlaceName          = []
        self.ChipFrameInfo      = []
        self.StringTable        = []
        self.ScnInfo            = []
        self.CodeBlocks         = []
        self.BattleInfoRefs     = []

        for i in range(SCN_INFO_MAXIMUM):
            self.ScnInfo.append([])
            self.ScnInfoOffset.append(0)
            self.ScnInfoNumber.append(0)

    def binary(self):
        MapName = self.MapName.encode(CODE_PAGE)
        if len(MapName) < 0xA:
            MapName += b'\x00' * (0xA - len(MapName))

        Location = self.Location.encode(CODE_PAGE)
        if len(Location) < 0xA:
            Location += b'\x00' * (0xA - len(Location))

        Unknown_14 = struct.pack('<L', self.Unknown_14)
        Flags = struct.pack('<L', self.Flags)

        IncludedScenario = b''
        for inc in self.IncludedScenario:
            IncludedScenario += struct.pack('<L', inc)

        StringTableOffset = struct.pack('<L', self.StringTableOffset)

        ScnInfoOffset = b''
        ScnInfoNumber = b''
        for i in range(len(self.ScnInfoNumber)):
            ScnInfoOffset += struct.pack('<H', self.ScnInfoOffset[i])
            ScnInfoNumber += struct.pack('<B', self.ScnInfoNumber[i])

        ScenaFunctionTable = struct.pack('<HH', self.ScenaFunctionTable.Offset, self.ScenaFunctionTable.Size)

        ChipFrameInfoOffset = struct.pack('<H', self.ChipFrameInfoOffset)

        PlaceNameOffset = struct.pack('<H', self.PlaceNameOffset)
        PlaceNameNumber = struct.pack('<B', self.PlaceNameNumber)

        PreInitFunctionIndex = struct.pack('<B', self.PreInitFunctionIndex)
        Unknown_51 = struct.pack('<BBB', self.Unknown_51[0], self.Unknown_51[1], self.Unknown_51[2])

        Information = self.Information

        return MapName + \
                Location + \
                Unknown_14 + \
                Flags + \
                IncludedScenario + \
                StringTableOffset + \
                ScnInfoOffset + \
                ScenaFunctionTable + \
                ChipFrameInfoOffset + \
                PlaceNameOffset + \
                PlaceNameNumber + \
                PreInitFunctionIndex + \
                ScnInfoNumber + \
                Unknown_51 + \
                Information

    def open(self, buf):
        if type(buf) is str:
            buf = open(buf, 'rb').read()

        fs = BytesStream()
        fs.openmem(buf)

        # file header

        self.MapName                    = fs.read(0xA).decode(CODE_PAGE).split('\x00', 1)[0]
        self.Location                   = fs.read(0xA).decode(CODE_PAGE).split('\x00', 1)[0]
        self.Unknown_14                 = fs.ulong()
        self.Flags                      = fs.ulong()
        self.IncludedScenario           = list(struct.unpack('<' + 'I' * NUMBER_OF_INCLUDE_FILE, fs.read(NUMBER_OF_INCLUDE_FILE * 4)))
        self.StringTableOffset          = fs.ulong()
        self.ScnInfoOffset              = list(struct.unpack('<' + 'H' * SCN_INFO_MAXIMUM, fs.read(SCN_INFO_MAXIMUM * 2)))
        self.ScenaFunctionTable         = ScenarioEntry(fs.ushort(), fs.ushort())
        self.ChipFrameInfoOffset        = fs.ushort()
        self.PlaceNameOffset            = fs.ushort()
        self.PlaceNameNumber            = fs.byte()
        self.PreInitFunctionIndex       = fs.byte()
        self.ScnInfoNumber              = list(struct.unpack('<' + 'B' * SCN_INFO_MAXIMUM, fs.read(SCN_INFO_MAXIMUM * 1)))
        self.Unknown_51                 = fs.read(3)
        self.Information                = fs.read(0x40)

        # file header end

        #if self.PlaceNameOffset != 0: raise Exception('not implemented')

        self.InitScenaInfo(fs)
        self.InitOtherInfo(fs)

        self.CodeBlocks = self.DisassembleBlocks(fs)

    def InitScenaInfo(self, fs):
        ScnInfoTypes = \
        [
            ScenarioChipInfo,
            ScenarioNpcInfo,
            ScenarioMonsterInfo,
            ScenarioEventInfo,
            ScenarioActorInfo,
        ]

        for i in range(len(self.ScnInfoOffset)):
            fs.seek(self.ScnInfoOffset[i])
            ScnInfoType = ScnInfoTypes[i]
            for n in range(self.ScnInfoNumber[i]):
                self.ScnInfo[i].append(ScnInfoType(fs))

    def InitOtherInfo(self, fs):

        fs.seek(self.PlaceNameOffset)
        for i in range(self.PlaceNameNumber):
            self.PlaceName.append(ScenarioPlaceNameInfo(fs))

        fs.seek(self.ScenaFunctionTable.Offset)
        self.ScenaFunctions = list(struct.unpack('<' + 'I' * int(self.ScenaFunctionTable.Size / 4), fs.read(self.ScenaFunctionTable.Size)))

        fs.seek(self.ChipFrameInfoOffset)
        self.ChipFrameInfo = []
        for i in range(self.ScnInfoNumber[SCN_INFO_MONSTER]):
            self.ChipFrameInfo.append(ScenarioChipFrameInfo(fs))

        fs.seek(self.StringTableOffset)

        buf = fs.read()
        endmz = buf.find(b'\x00\x00')
        if endmz != -1:
            buf = buf[:endmz]

        stringtable = buf.decode(CODE_PAGE).rstrip('\x00').split('\x00')
        for string in stringtable:
            #if string in self.StringTable: continue
            self.StringTable.append(string)

    def DiasmInstructionCallback(self, inst, fs):
        if inst.OpCode != edao.Battle:
            return

        BattleInfoOffset = inst.Operand[0]
        if BattleInfoOffset == 0xFFFFFFFF:
            return

        pos = fs.tell()
        fs.seek(BattleInfoOffset)
        self.BattleInfoRefs.append(ScenarioBattleInfo(fs))
        fs.seek(pos)

    def DisassembleBlocks(self, fs):
        disasm = Disassembler(edao.edao_op_table, self.DiasmInstructionCallback)

        codeblocks = []
        blockoffsetmap = {}
        for func in self.ScenaFunctions:
            if func in blockoffsetmap:
                codeblocks.append(blockoffsetmap[func])
                continue

            fs.seek(func)
            block = disasm.DisasmBlock(fs)
            block.Name = 'Function_%X' % block.Offset
            codeblocks.append(block)

            blockoffsetmap[func] = block

        return codeblocks

    def FormatCodeBlocks(self):
        disasm = Disassembler(edao.edao_op_table)

        blocks = []
        blockoffsetmap = {}
        for block in self.CodeBlocks:
            if block.Offset in blockoffsetmap:
                continue

            blockoffsetmap[block.Offset] = True
            blocks.append(disasm.FormatCodeBlock(block))

        #for x in disasmtbl: print('%08X' % x)
        #input()

        return blocks

    def GenerateSingleBattleInfo(self, btinfo, offsetmap):
        battleinfolines = []
        sepithlines     = []
        monposlines     = []
        atbonuslines    = []

        if btinfo.Offset in offsetmap:
            return (battleinfolines, sepithlines, monposlines, atbonuslines)

        offsetmap[btinfo.Offset] = True

        if btinfo.Sepith != None and btinfo.Sepith.Offset not in offsetmap:
            offsetmap[btinfo.Sepith.Offset] = True
            sepithlines.append('Sepith("Sepith_%X", %s)' % (btinfo.Sepith.Offset, btinfo.Sepith.param()))

        monbtinfolines = []
        monbtinfolines.append('    (')

        for i in range(len(btinfo.Probability)):
            if btinfo.Probability[i] == 0:
                monbtinfolines.append('        (),')
                continue

            monbtinfo = btinfo.MonsterBattleInfo[i]

            for posinfo in monbtinfo.PositionNormal:
                if posinfo.Offset in offsetmap:
                    continue

                offsetmap[posinfo.Offset] = True
                monposlines.append('MonsterBattlePostion(%s)' % posinfo.param())

            for posinfo in monbtinfo.PositionEnemyAdvantage:
                if posinfo.Offset in offsetmap:
                    continue

                offsetmap[posinfo.Offset] = True
                monposlines.append('MonsterBattlePostion(%s)' % posinfo.param())

            if monbtinfo.ATBonus.Offset not in offsetmap:
                offsetmap[monbtinfo.ATBonus.Offset] = True
                atbonuslines.append('ATBonus(%s)' % monbtinfo.ATBonus.param())

            monbtinfolines.append('        (%s),' % monbtinfo.param())

        monbtinfolines.append('    )')

        battleinfolines.append('BattleInfo(')
        battleinfolines.append('    %s,' % btinfo.param())
        battleinfolines += monbtinfolines
        battleinfolines.append(')')
        battleinfolines.append('')

        return (battleinfolines, sepithlines, monposlines, atbonuslines)

    def GenerateBattleInfo(self):
        battleinfolines = []
        sepithlines     = []
        monposlines     = []
        atbonuslines    = []

        btcount = 0

        offsetmap = {}

        for monster in self.ScnInfo[SCN_INFO_MONSTER]:
            btcount += 1
            btinfo = monster.BattleInfo

            r = self.GenerateSingleBattleInfo(btinfo, offsetmap)

            battleinfolines += r[0]
            sepithlines     += r[1]
            monposlines     += r[2]
            atbonuslines    += r[3]

        if len(self.BattleInfoRefs) != 0:
            battleinfolines.append('# event battle count: %d' % len(self.BattleInfoRefs))
            battleinfolines.append('')

            for btinfo in self.BattleInfoRefs:
                r = self.GenerateSingleBattleInfo(btinfo, offsetmap)
                battleinfolines += r[0]
                sepithlines     += r[1]
                monposlines     += r[2]
                atbonuslines    += r[3]

        if len(atbonuslines) != 0:
            atbonuslines += ['']

        if len(sepithlines) != 0:
            sepithlines += ['']

        if len(monposlines) != 0:
            monposlines += ['']

        if len(battleinfolines) != 0:
            battleinfolines.insert(0, '# monster count: %d' % btcount)
            battleinfolines.insert(1, '')

        return atbonuslines + sepithlines + monposlines + battleinfolines

    def GenerateStringList(self):

        lines = []

        if len(self.StringTable) == 0:
            return lines

        index = 0
        lines.append('BuildStringList((')
        for string in self.StringTable:
            x = ljust_cn('    "%s",' % string, 30)
            lines.append(x + '# %d' % index)
            index += 1

        lines.append('))')
        lines.append('')

        return lines

    def GenerateHeader(self):
        hdr = []
        hdr.append('from EDAOScenaFile import *')
        hdr.append('')
        hdr.append('CreateScenaFile(')
        hdr.append('    "%s",                    # MapName' % self.MapName)
        hdr.append('    "%s",                    # Location' % self.Location)
        hdr.append('    0x%08X,                 # Unknown_14' % self.Unknown_14)
        hdr.append('    0x%08X,                 # Flags' % self.Flags)

        include = ''
        for scp in self.IncludedScenario:
            include += '"%s", ' % ScenarioFileIndex(scp).Name()

        hdr.append('    (%s),   # include' % include[:-2])
        hdr.append('    0x%02X,                       # PlaceNameNumber' % self.PlaceNameNumber)
        hdr.append('    0x%02X,                       # PreInitFunctionIndex' % self.PreInitFunctionIndex)
        hdr.append('    %s,            # Unknown_51' % self.Unknown_51)
        hdr.append('')
        hdr.append('    # Information')
        hdr.append('    %s,' % self.Information)

        hdr.append(')')
        hdr.append('')

        hdr += self.GenerateStringList()
        hdr += self.GenerateBattleInfo()

        if len(self.ScnInfo[SCN_INFO_CHIP]) != 0:
            hdr.append('AddCharChip(')

            index = 0
            for chip in self.ScnInfo[SCN_INFO_CHIP]:
                x = ('    %s,' % chip.param()).ljust(40)
                x += ' # %02X' % index
                hdr.append(x)
                index += 1

            hdr.append(')')
            hdr.append('')

        def AppendScpInfo(info, func):
            if len(info) == 0:
                return

            for i in info:
                hdr.append('%s(%s)' % (func, i.param()))

            hdr.append('')

        AppendScpInfo(self.ScnInfo[SCN_INFO_NPC],       'Npc')
        AppendScpInfo(self.ScnInfo[SCN_INFO_MONSTER],   'Monster')
        AppendScpInfo(self.ScnInfo[SCN_INFO_EVENT],     'Event')
        AppendScpInfo(self.ScnInfo[SCN_INFO_ACTOR],     'Actor')

        index = 0
        for block in self.CodeBlocks:
            s = ('ScpFunction("%s")' % block.Name).ljust(30)
            hdr.append('%s # %d' % (s, index))
            index += 1

        hdr.append('')

        for place in self.PlaceName:
            s = 'PlaceName(%s)' % place.param()
            hdr.append(s)

        hdr.append('')

        index = 0
        for frame in self.ChipFrameInfo:
            s = ('ChipFrameInfo(%s)' % frame.param()).ljust(50)
            hdr.append('%s # %d' % (s, index))
            index += 1

        hdr.append('')

        return hdr

    def SaveToFile(self, filename):
        lines = []

        lines += self.GenerateHeader()

        blocks = self.FormatCodeBlocks()

        for block in blocks:
            lines += block

        lines.append('SaveToFile()')
        lines.append('')

        txt = '\r\n'.join(lines)

        lines = txt.replace('\r\n', '\n').replace('\r', '\n').split('\n')

        for i in range(2, len(lines)):
            if lines[i] != '':
                lines[i] = '    %s' % lines[i]

        lines.insert(2, 'def main():')
        lines.append('TryInvoke(main)')
        lines.append('')

        fs = open(filename, 'wb')
        fs.write(''.encode('utf_8_sig'))
        fs.write('\r\n'.join(lines).encode('UTF8'))

    def __str__(self):
        info = []
        info.append('MapName                = %s' % (self.MapName))
        info.append('Location               = %s' % (self.Location))
        info.append('Unknown_14             = %08X' % (self.Unknown_14))
        info.append('Flags                  = %08X' % (self.Flags))

        buf = 'IncludedScenario       = '
        for include in self.IncludedScenario:
            buf += '%08X ' % include

        info.append(buf)

        info.append('StringTableOffset          = %08X' % (self.StringTableOffset))

        info.append('')
        info.append('ScnInfoOffset    ScnInfoNumber')
        for i in range(len(self.ScnInfoOffset)):
            info.append('  %08X          %08X' % (self.ScnInfoOffset[i], self.ScnInfoNumber[i]))
        info.append('')

        ScnInfoNames = \
        [
            'ChipInfo',
            'NpcInformation',
            'MonsterInformation',
            'ScpInfo',
            'InfoUnknown1',
        ]

        info.append('ScnInfo:')
        for i in range(len(self.ScnInfo)):
            info.append('  %s:' % ScnInfoNames[i])
            for scninfo in self.ScnInfo[i]:
                info.append('    %s' % scninfo)

            info.append('')

        info.append('')

        info.append('ScenaFunctionTable         = %04X, %04X' % (self.ScenaFunctionTable.Offset, self.ScenaFunctionTable.Size))
        info.append('ChipFrameInfoOffset        = %04X' % self.ChipFrameInfoOffset)
        info.append('PlaceNameOffset            = %04X' % self.PlaceNameOffset)
        info.append('PlaceNameNumber            = %02X' % (self.PlaceNameNumber))
        info.append('PreInitFunctionIndex       = %02X' % (self.PreInitFunctionIndex))
        info.append('Unknown_51                 = %s' % self.Unknown_51)

        info.append('')
        info.append('Information:')
        info.append('%s' % (self.Information))
        info.append('')

        info.append('ScenaFunctions:')
        for sec in self.ScenaFunctions:
            info.append('  %08X' % sec)
        info.append('')

        info.append('NpcName:')
        for i in range(len(self.NpcName)):
            info.append('  %2d.%s' % (i + 1, self.NpcName[i]))
        info.append('')

        return '\r\n'.join(info)

