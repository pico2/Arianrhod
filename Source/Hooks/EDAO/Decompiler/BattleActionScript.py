from Assembler2 import *
from EDAOBase import *
import ActionOpTableEDAO as edao

INVALID_ACTION_OFFSET = 0xFFFF
EMPTY_ACTION    = INVALID_ACTION_OFFSET

class CharacterPositionFactor:

    def __init__(self, fs):
        if fs == None:
            return

        self.X = fs.byte()
        self.Y = fs.byte()

class BattleActionScriptInfo:

    def __init__(self):
        self.ActionListOffset       = 0
        self.ChrPosFactorOffset     = 0
        self.Reserve                = 0
        self.PreloadChipList        = []
        self.ActionList             = []

        self.ChrPosFactor = []
        self.CraftActions = []

    def open(self, buf):
        if type(buf) == str:
            buf = open(buf, 'rb').read()

        fs = BytesStream()
        fs.openmem(buf)

        self.ActionListOffset   = fs.ushort()
        self.ChrPosFactorOffset = fs.ushort()
        self.Reserve            = fs.ushort()

        while True:
            index = fs.ulong()
            if index == 0xFFFFFFFF:
                break

            self.PreloadChipList.append(ChipFileIndex(index))

        fs.seek(self.ChrPosFactorOffset)
        for i in range(8):
            self.ChrPosFactor.append(CharacterPositionFactor(fs))

        fs.seek(self.ActionListOffset)
        while True:
            offset = fs.ushort()
            if offset == 0:
                break

            self.ActionList.append(offset)

        if len(self.ActionList) == 0:
            raise Exception('action number == 0')

        self.CraftActions = self.DisassembleCraftActions(fs)

        return

        for i in range(self.ActionListOffset + len(self.ActionList) * 2, fs.size()):
            if i not in offsetlist:
                print('%X' % i)
                input()

        input()

    def DiasmInstructionCallback(self, inst, fs):
        return

    def DisassembleCraftActions(self, fs):

        BuiltinCraftNames = \
        [
            'SysCraft_MagicEffect',
            'SysCraft_Stand',
            'SysCraft_Move',
            'SysCraft_UnderAttack',
            'SysCraft_Dead',
            'SysCraft_NormalAttack',
            'SysCraft_MagicChant',
            'SysCraft_MagicCast',
            'SysCraft_Win',
            'SysCraft_EnterBattle',
            'SysCraft_UseItem',
            'SysCraft_Stun',
            'SysCraft_Unknown2',
            'SysCraft_Reserve1',
            'SysCraft_Reserve2',
            'SysCraft_Counter',
        ]

        disasm = Disassembler(edao.edao_as_op_table, self.DiasmInstructionCallback)

        index = 0
        codeblocks = []
        blockoffsetmap = {}
        for func in self.ActionList:
            if func == INVALID_ACTION_OFFSET:
                codeblocks.append(CodeBlock(INVALID_ACTION_OFFSET))
                continue

            if func in blockoffsetmap:
                codeblocks.append(blockoffsetmap[func])
                continue

            fs.seek(func)
            block = disasm.DisasmBlock(fs)
            block.Name = ('Craft_%X' % block.Offset) if index >= len(BuiltinCraftNames) else BuiltinCraftNames[index]
            codeblocks.append(block)

            blockoffsetmap[func] = block

            index += 1

        return codeblocks

    def FormatCodeBlocks(self):
        disasm = Disassembler(edao.edao_as_op_table)

        blocks = []
        blockoffsetmap = {}
        for block in self.CraftActions:
            if block.Offset == INVALID_ACTION_OFFSET:
                continue

            if block.Offset in blockoffsetmap:
                continue

            blockoffsetmap[block.Offset] = True
            blocks.append(disasm.FormatCodeBlock(block))

        #for x in disasmtbl: print('%08X' % x)
        #input()

        return blocks

    def SaveToFile(self, filename):
        lines = []

        lines.append('from %s import *' % os.path.splitext(os.path.basename(__file__))[0])
        lines.append('')

        tmp = []
        for pos in self.ChrPosFactor:
            tmp.append('(%d, %d)' % (pos.X, pos.Y))

        lines.append('CreateBattleAction("%s", (%s))' % (os.path.splitext(os.path.basename(filename))[0] + '.dat', ', '.join(tmp)))
        lines.append('')
        lines.append('AddPreloadChip(')

        index = 0
        for chip in self.PreloadChipList:
            x = ('    "%s",' % chip.Name()).ljust(30)
            x += ' # %02X %d' % (index, index)
            lines.append(x)
            index += 1

        lines.append(')')
        lines.append('')

        index = 0
        for craft in self.CraftActions:
            name = ('"%s"'% craft.Name) if craft.Offset != INVALID_ACTION_OFFSET else 'EMPTY_ACTION'
            lines.append(('CraftAction(%s)' % name).ljust(40) + ('# %02X %d' % (index, index)))
            index += 1

        lines.append('')

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

def main():
    for f in sys.argv[1:]:
        asdat = BattleActionScriptInfo()
        asdat.open(f)
        asdat.SaveToFile(os.path.splitext(f)[0] + '.py')

TryInvoke(main)
