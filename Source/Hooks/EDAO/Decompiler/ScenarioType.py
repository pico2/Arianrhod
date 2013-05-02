from BaseType import *
from Assembler import *
import InstructionTableEDAO as edao

CODE_PAGE = edao.CODE_PAGE

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
/* 0x00 */   CHAR                     MapName[0xA];                         // %s/%s/%s.it3
/* 0x0A */   CHAR                     Location[0xA];
/* 0x14 */   ULONG                    Unknown_14;
/* 0x18 */   ULONG                    Flags;
/* 0x1C */   ULONG                    IncludedScenarioFileIndex[6];
/* 0x34 */   ULONG                    NpcNameOffset;                    // multi-sz, max-len = 0x20
/* 0x38 */   USHORT                   ScnInfoOffset[SCN_INFO_MAXIMUM];
/* 0x42 */   SCENARIO_ENTRY           ScenaFunctionTable;
/* 0x46 */   SCENARIO_ENTRY           UnknownEntry_46;                        // ???
/* 0x4A */   UCHAR                    Unknown_4A;
/* 0x4B */   UCHAR                    PreInitSectionIndex;
/* 0x4C */   CHAR                     ScnInfoNumber[SCN_INFO_MAXIMUM];
/* 0x51 */   UCHAR                    Unknown_51[3];
/* 0x54 */   SCENARIO_INFORMATION     Information;

} SCENARIO_HEADER;

op count: 227

'''

NUMBER_OF_INCLUDE_FILE          = 6

SCN_INFO_CHIP                   = 0
SCN_INFO_NPC_POSITION           = 1
SCN_INFO_MONSTER_POSITION       = 2
SCN_INFO_SCP_INFO               = 3
SCN_INFO_UNKNOWN1               = 4
SCN_INFO_MAXIMUM                = 5

class ScenarioEntry:
    def __init__(self, offset = 0, size = 0):
        self.Offset = offset
        self.Size = size

class ScenarioChipInfo:
    # ULONG chipindex
    def __init__(self, fs = None):
        if fs == None:
            return

        self.ChipIndex = fs.ulong()

    def __str__(self):
        return '0x%08X' % self.ChipIndex

    def binary(self):
        return struct.pack('<L', self.ChipIndex)

    def param(self):
        return self.__str__()

class ScenarioCharInformation:
    def __init__(self, fs = None):
        if fs == None:
            return

        # size = 0x1C

        self.X                  = fs.ulong()
        self.Y                  = fs.ulong()
        self.Z                  = fs.ulong()
        self.Unknown1           = fs.ushort()
        self.Unknown2           = fs.ushort()
        self.Unknown            = fs.ulong()
        self.InitScenaIndex     = fs.byte()
        self.InitSectionIndex   = fs.byte()
        self.TalkScenaIndex     = fs.byte()
        self.TalkSectionIndex   = fs.byte()
        self.Unknown4           = fs.ushort()
        self.Unknown5           = fs.ushort()

    def __str__(self):
        return str(self.binary())

    def param(self):
        return '%d, %d, %d, %d, %d, 0x%X, %d, %d, %d, %d, %d, %d' % (
                    LONG(self.X).value,
                    LONG(self.Y).value,
                    LONG(self.Z).value,
                    LONG(self.Unknown1).value,
                    LONG(self.Unknown2).value,
                    ULONG(self.Unknown).value,
                    LONG(self.InitScenaIndex).value,
                    LONG(self.InitSectionIndex).value,
                    LONG(self.TalkScenaIndex).value,
                    LONG(self.TalkSectionIndex).value,
                    LONG(self.Unknown4).value,
                    LONG(self.Unknown5).value
                )

    def binary(self):
        return struct.pack('<LLLHHLBBBBHH', self.X, self.Y, self.Z, self.Unknown1, self.Unknown2, self.Unknown, self.InitScenaIndex, self.InitSectionIndex, self.TalkScenaIndex, self.TalkSectionIndex, self.Unknown4, self.Unknown5)

class ScenarioScpInfo:
    # 0x60 bytes
    def __init__(self, fs = None):
        if fs == None:
            return

        self.buf = fs.read(0x60)

    def __str__(self):
        return str(self.buf)

    def param(self):
        return self.__str__()

    def binary(self):
        return self.buf

class ScenarioInfoUnknown1:
    def __init__(self, fs = None):
        if fs == None:
            return

        self.buf = fs.read(0x24)

    def __str__(self):
        return str(self.buf)

    def param(self):
        return self.__str__()

    def binary(self):
        return self.buf

class ScenarioInfo:
    def __init__(self):
        # file header

        self.MapName                    = ''
        self.Location                   = ''
        self.Unknown_14                 = 0
        self.Flags                      = 0
        self.IncludedScenario           = []
        self.NpcNameOffset              = 0
        self.ScnInfoOffset              = []
        self.ScenaFunctionTable         = ScenarioEntry()
        self.UnknownEntry_46            = ScenarioEntry()
        self.Unknown_4A                 = 0
        self.PreInitSectionIndex        = 0
        self.ScnInfoNumber              = []
        self.Unknown_51                 = b''
        self.Information                = b''

        # file header end

        self.ScenaFunctions     = []
        self.NpcName            = []
        self.ScnInfo            = []
        self.CodeBlocks         = []

        for i in range(SCN_INFO_MAXIMUM):
            self.ScnInfo.append([])
            self.ScnInfoOffset.append([])

    def open(self, buf):
        if type(buf) is str:
            buf = open(buf, 'rb').read()

        fs = BytesStream()
        fs.openmem(buf)

        # file header

        self.MapName                = fs.read(0xA).decode(CODE_PAGE).split('\x00', 1)[0]
        self.Location               = fs.read(0xA).decode(CODE_PAGE).split('\x00', 1)[0]
        self.Unknown_14             = fs.ulong()
        self.Flags                  = fs.ulong()
        self.IncludedScenario       = list(struct.unpack('<' + 'I' * NUMBER_OF_INCLUDE_FILE, fs.read(NUMBER_OF_INCLUDE_FILE * 4)))
        self.NpcNameOffset          = fs.ulong()
        self.ScnInfoOffset          = list(struct.unpack('<' + 'H' * SCN_INFO_MAXIMUM, fs.read(SCN_INFO_MAXIMUM * 2)))
        self.ScenaFunctionTable     = ScenarioEntry(fs.ushort(), fs.ushort())
        self.UnknownEntry_46        = ScenarioEntry(fs.ushort(), fs.ushort())
        self.Unknown_4A             = fs.byte()
        self.PreInitSectionIndex    = fs.byte()
        self.ScnInfoNumber          = list(struct.unpack('<' + 'B' * SCN_INFO_MAXIMUM, fs.read(SCN_INFO_MAXIMUM * 1)))
        self.Unknown_51             = fs.read(3)
        self.Information            = fs.read(0x40)

        # file header end

        self.InitScenaInfo(fs)
        self.InitOtherInfo(fs)

        self.CodeBlocks = self.DisassembleBlocks(fs)

    def InitScenaInfo(self, fs):
        ScnInfoTypes = \
        [
            ScenarioChipInfo,
            ScenarioCharInformation,
            ScenarioCharInformation,
            ScenarioScpInfo,
            ScenarioInfoUnknown1,
        ]

        for i in range(len(self.ScnInfoOffset)):
            fs.seek(self.ScnInfoOffset[i])
            ScnInfoType = ScnInfoTypes[i]
            for n in range(self.ScnInfoNumber[i]):
                self.ScnInfo[i].append(ScnInfoType(fs))

    def InitOtherInfo(self, fs):
        fs.seek(self.ScenaFunctionTable.Offset)
        self.ScenaFunctions = list(struct.unpack('<' + 'I' * int(self.ScenaFunctionTable.Size / 4), fs.read(self.ScenaFunctionTable.Size)))

        fs.seek(self.UnknownEntry_46.Offset)
        self.UnknownEntry_46_Data = fs.read(self.UnknownEntry_46.Size)

        fs.seek(self.NpcNameOffset)

        buf = fs.read()
        endmz = buf.find(b'\x00\x00')
        if endmz != -1:
            buf = buf[:endmz - 1]

        self.NpcName = fs.read().decode(CODE_PAGE).rstrip('\x00').split('\x00')

    def DisassembleBlocks(self, fs):
        disasm = Disassembler(edao.edao_op_table)

        codeblocks = []
        for func in self.ScenaFunctions:
            fs.seek(func)
            block = disasm.DisasmBlock(fs)
            block.Name = 'Function_%X' % block.Offset
            codeblocks.append(block)

        return codeblocks

    def FormatCodeBlocks(self):
        disasm = Disassembler(edao.edao_op_table)

        blocks = []
        for block in self.CodeBlocks:
            blocks.append(disasm.FormatCodeBlock(block))

        #for x in disasmtbl: print('%08X' % x)
        #input()

        return blocks


    def stub(self):

        hdrstub = '''\
\
CreateScena(
    %s,                                     # MapName
    %s,                                     # Location
    0x%08X,                                 # Unknown_14
    0x%08X,                                 # Flags
    ('%s', '%s', '%s', '%s', '%s', '%s'),   # IncludedScenarioFileIndex
                                            # NpcNameOffset (update later)
                                            # ScnInfoOffset[SCN_INFO_MAXIMUM] (update later)
                                            # ScenaFunctionTable (update later)
                                            # UnknownEntry_46 (update later)
    0x%02X,                                 # Unknown_4A
    0x%02X,                                 # PreInitSectionIndex
                                            # ScnInfoNumber[SCN_INFO_MAXIMUM] (update later)
    %s,                                     # Unknown_51 (3 bytes)
    %s,                                     # Information (0x40 bytes)
)

'''

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
            include += '0x%08X, ' % scp

        hdr.append('    (%s),   # include' % include[:-2])
        hdr.append('    0x%02X,                       # Unknown_4A' % self.Unknown_4A)
        hdr.append('    0x%02X,                       # PreInitSectionIndex' % self.PreInitSectionIndex)
        hdr.append('    %s,            # Unknown_51' % self.Unknown_51)
        hdr.append('')
        hdr.append('    # Information')
        hdr.append('    %s,' % self.Information)

        hdr.append(')')
        hdr.append('')

        if len(self.ScnInfo[SCN_INFO_CHIP]) != 0:
            hdr.append('AddCharChip(')

            for chip in self.ScnInfo[SCN_INFO_CHIP]:
                hdr.append('    %s,' % chip.param())

            hdr.append(')')
            hdr.append('')

        def AppendScpInfo(info, func):
            if len(info) == 0:
                return

            for i in info:
                hdr.append('%s(%s)' % (func, i.param()))

            hdr.append('')

        AppendScpInfo(self.ScnInfo[SCN_INFO_NPC_POSITION],      'Npc')
        AppendScpInfo(self.ScnInfo[SCN_INFO_MONSTER_POSITION],  'Monster')
        AppendScpInfo(self.ScnInfo[SCN_INFO_SCP_INFO],          'ScpInfo')
        AppendScpInfo(self.ScnInfo[SCN_INFO_UNKNOWN1],          'ScpInfoUnknwon1')

        for block in self.CodeBlocks:
            hdr.append('ScpFunction("%s")' % block.Name)

        hdr.append('')

        return hdr

    def SaveToFile(self, filename):
        lines = []

        lines += self.GenerateHeader()

        blocks = self.FormatCodeBlocks()

        for block in blocks:
            lines += block

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

        info.append('NpcNameOffset          = %08X' % (self.NpcNameOffset))

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

        info.append('ScenaFunctionTable     = %04X, %04X' % (self.ScenaFunctionTable.Offset, self.ScenaFunctionTable.Size))
        info.append('UnknownEntry_46        = %04X, %04X' % (self.UnknownEntry_46.Offset, self.UnknownEntry_46.Size))
        info.append('Unknown_4A             = %02X' % (self.Unknown_4A))
        info.append('PreInitSectionIndex    = %02X' % (self.PreInitSectionIndex))
        info.append('Unknown_51             = %s' % self.Unknown_51)

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

