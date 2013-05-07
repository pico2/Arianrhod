from InstructionTable import *
from EDAOBase import *

def GetOpCode(fs):
    return fs.byte()

def WriteOpCode(fs, op):
    return fs.wbyte(op)

edao_as_op_table = InstructionTable(GetOpCode, WriteOpCode, DefaultGetLabelName, CODE_PAGE)

InstructionNames = {}

InstructionNames[0x00] = 'Return'
InstructionNames[0x01] = 'Jump'
InstructionNames[0x02] = 'SetChrSubChip'
InstructionNames[0x03] = 'AS_03'
InstructionNames[0x04] = 'AS_04'
InstructionNames[0x05] = 'AS_05'
InstructionNames[0x06] = 'Sleep'
InstructionNames[0x07] = 'AS_07'
InstructionNames[0x08] = 'AS_08'
InstructionNames[0x09] = 'AS_09'
InstructionNames[0x0A] = 'AS_0A'
InstructionNames[0x0B] = 'AS_0B'
InstructionNames[0x0C] = 'AS_0C'
InstructionNames[0x0D] = 'AS_0D'
InstructionNames[0x0E] = 'AS_0E'
InstructionNames[0x0F] = 'AS_0F'
InstructionNames[0x10] = 'AS_10'
InstructionNames[0x11] = 'AS_11'
InstructionNames[0x12] = 'LoadEffect'
InstructionNames[0x13] = 'AS_13'
InstructionNames[0x14] = 'AS_14'
InstructionNames[0x15] = 'WaitEffect'
InstructionNames[0x16] = 'AS_16'
InstructionNames[0x17] = 'AS_17'
InstructionNames[0x18] = 'PlayEffect'
InstructionNames[0x19] = 'AS_19'
InstructionNames[0x1A] = 'AS_1A'
InstructionNames[0x1B] = 'SetChrChip'
InstructionNames[0x1C] = 'DamageCue'
InstructionNames[0x1D] = 'DamageAnime'
InstructionNames[0x1E] = 'AS_1E'
InstructionNames[0x1F] = 'AS_1F'
InstructionNames[0x20] = 'AS_20'
InstructionNames[0x21] = 'AS_21'
InstructionNames[0x22] = 'BeginChrThread'
InstructionNames[0x23] = 'AS_23'
InstructionNames[0x24] = 'AS_24'
InstructionNames[0x25] = 'AS_25'
InstructionNames[0x26] = 'AS_26'
InstructionNames[0x27] = 'AS_27'
InstructionNames[0x28] = 'Say'
InstructionNames[0x29] = 'AS_29'
InstructionNames[0x2A] = 'ShowInfoText'
InstructionNames[0x2B] = 'AS_2B'
InstructionNames[0x2C] = 'ShowChrTrails'
InstructionNames[0x2D] = 'HideChrTrails'
InstructionNames[0x2E] = 'AS_2E'
InstructionNames[0x2F] = 'AS_2F'
InstructionNames[0x31] = 'AS_31'
InstructionNames[0x32] = 'AS_32'
InstructionNames[0x33] = 'AS_33'
InstructionNames[0x34] = 'AS_34'
InstructionNames[0x35] = 'AS_35'
InstructionNames[0x36] = 'AS_36'
InstructionNames[0x39] = 'AS_39'
InstructionNames[0x3A] = 'AS_3A'
InstructionNames[0x3B] = 'AS_3B'
InstructionNames[0x3C] = 'AS_3C'
InstructionNames[0x3D] = 'AS_3D'
InstructionNames[0x3E] = 'AS_3E'
InstructionNames[0x3F] = 'AS_3F'
InstructionNames[0x40] = 'AS_40'
InstructionNames[0x43] = 'AS_43'
InstructionNames[0x44] = 'AS_44'
InstructionNames[0x45] = 'AS_45'
InstructionNames[0x46] = 'AS_46'
InstructionNames[0x47] = 'AS_47'
InstructionNames[0x48] = 'AS_48'
InstructionNames[0x49] = 'SetControl'
InstructionNames[0x4A] = 'AS_4A'
InstructionNames[0x4B] = 'Jc'
InstructionNames[0x4C] = 'ForeachTarget'
InstructionNames[0x4D] = 'InitForeachTarget'
InstructionNames[0x4E] = 'NextTarget'
InstructionNames[0x4F] = 'AS_4F'
InstructionNames[0x50] = 'Call'
InstructionNames[0x51] = 'CallReturn'
InstructionNames[0x52] = 'AS_52'
InstructionNames[0x53] = 'AS_53'
InstructionNames[0x54] = 'SendMessage'
InstructionNames[0x55] = 'MagicUsing'
InstructionNames[0x56] = 'MagicEnd'
InstructionNames[0x57] = 'AS_57'
InstructionNames[0x58] = 'Knockback'
InstructionNames[0x59] = 'AS_59'
InstructionNames[0x5A] = 'AS_5A'
InstructionNames[0x5B] = 'AS_5B'
InstructionNames[0x5C] = 'ShowChr'
InstructionNames[0x5D] = 'HideChr'
InstructionNames[0x5E] = 'AS_5E'
InstructionNames[0x5F] = 'AS_5F'
InstructionNames[0x60] = 'AS_60'
InstructionNames[0x61] = 'SetBattleSpeed'
InstructionNames[0x62] = 'Voice'
InstructionNames[0x64] = 'Sound'
InstructionNames[0x65] = 'SoundEx'
InstructionNames[0x66] = 'AS_66'
InstructionNames[0x67] = 'AS_67'
InstructionNames[0x68] = 'AS_68'
InstructionNames[0x6A] = 'LoadChrChip'
InstructionNames[0x6B] = 'AS_6B'
InstructionNames[0x6C] = 'AS_6C'
InstructionNames[0x6D] = 'AS_6D'
InstructionNames[0x6E] = 'AS_6E'
InstructionNames[0x6F] = 'AS_6F'
InstructionNames[0x70] = 'AS_70'
InstructionNames[0x71] = 'AS_71'
InstructionNames[0x72] = 'AS_72'
InstructionNames[0x73] = 'AS_73'
InstructionNames[0x74] = 'AS_74'
InstructionNames[0x77] = 'AS_77'
InstructionNames[0x78] = 'AS_78'
InstructionNames[0x79] = 'AS_79'
InstructionNames[0x7A] = 'AS_7A'
InstructionNames[0x7B] = 'AS_7B'
InstructionNames[0x7C] = 'AS_7C'
InstructionNames[0x7D] = 'AS_7D'
InstructionNames[0x7E] = 'AS_7E'
InstructionNames[0x7F] = 'AS_7F'
InstructionNames[0x80] = 'AS_80'
InstructionNames[0x82] = 'AS_82'
InstructionNames[0x83] = 'AS_83'
InstructionNames[0x84] = 'AS_84'
InstructionNames[0x85] = 'AS_85'
InstructionNames[0x87] = 'AS_87'
InstructionNames[0x89] = 'AS_89'
InstructionNames[0x8A] = 'AS_8A'
InstructionNames[0x8B] = 'UseItemBegin'
InstructionNames[0x8C] = 'UseItemEnd'
InstructionNames[0x8D] = 'AS_8D'
InstructionNames[0x8E] = 'AS_8E'
InstructionNames[0x8F] = 'AS_8F'
InstructionNames[0x91] = 'AS_91'
InstructionNames[0x92] = 'AS_92'
InstructionNames[0x93] = 'AS_93'
InstructionNames[0x94] = 'AS_94'
InstructionNames[0x95] = 'AS_95'
InstructionNames[0x96] = 'AS_96'
InstructionNames[0x97] = 'AS_97'
InstructionNames[0x98] = 'AS_98'
InstructionNames[0x99] = 'AS_99'
InstructionNames[0x9A] = 'AS_9A'
InstructionNames[0x9B] = 'AS_9B'
InstructionNames[0x9C] = 'AS_9C'
InstructionNames[0x9E] = 'AS_9E'
InstructionNames[0x9F] = 'AS_9F'
InstructionNames[0xA0] = 'AS_A0'
InstructionNames[0xA1] = 'AS_A1'
InstructionNames[0xA6] = 'AS_A6'
InstructionNames[0xA7] = 'AS_A7'
InstructionNames[0xA8] = 'AS_A8'
InstructionNames[0xA9] = 'AS_A9'
InstructionNames[0xAC] = 'AS_AC'
InstructionNames[0xAD] = 'AS_AD'
InstructionNames[0xAE] = 'AS_AE'
InstructionNames[0xAF] = 'AS_AF'
InstructionNames[0xB0] = 'AS_B0'
InstructionNames[0xB1] = 'AS_B1'
InstructionNames[0xB2] = 'AS_B2'
InstructionNames[0xB3] = 'AS_B3'
InstructionNames[0xB4] = 'AS_B4'
InstructionNames[0xB5] = 'AS_B5'
InstructionNames[0xB6] = 'AS_B6'
InstructionNames[0xB7] = 'AS_B7'
InstructionNames[0xB8] = 'AS_B8'

for op, name in InstructionNames.items():
    expr = '%s = 0x%08X' % (name, op)
    exec(expr)

class EDAOASOpTableEntry(InstructionTableEntry):
    def __init__(self, op, name = '', operand = NO_OPERAND, flags = 0, handler = None):
        super().__init__(op, name, operand, flags, handler)

def inst(op, operand = NO_OPERAND, flags = 0, handler = None):
    return EDAOASOpTableEntry(op, InstructionNames[op], operand, flags, handler)


class ActionTarget:
    Self        = 0xFF
    Target      = 0xFE


def as_0c(data):
    def getopr(target):
        operand = 'WWB'
        if target == 0xFC:
            operand = 'WWW' + operand
        return operand

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        inst = data.Instruction
        entry = data.TableEntry

        target, opr2 = entry.GetAllOperand('BB', fs)

        inst.Operand = [target, opr2]

        operand = getopr(target)
        inst.Operand += entry.GetAllOperand(operand, fs)

        return inst

def as_8e(data):

    def getopr(opr1, opr2):
        operand = ''

        if opr1 == 1:
            operand = 'S'
        else:
            operand = 'LLLL'
            if opr2 == 0xD:
                operand += 'L'

        return operand

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        inst = data.Instruction
        entry = data.TableEntry

        opr1, opr2 = entry.GetAllOperand('BB', fs)
        inst.Operand = [opr1, opr2]
        operand = getopr(opr1, opr2)
        inst.Operand += entry.GetAllOperand(operand, fs)

        return inst

def as_91(data):

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        inst = data.Instruction
        entry = data.TableEntry

        opr = entry.GetOperand('B', fs)
        inst.Operand = [opr]

        if opr == 0:
            for i in range(0xA):
                inst.Operand.append(fs.byte())
                if inst[-1] == 0xFF:
                    break

        return inst

edao_as_op_list = \
[
    inst(Return,            NO_OPERAND,         INSTRUCTION_END_BLOCK),
    inst(Jump,              'o',                INSTRUCTION_END_BLOCK),
    inst(SetChrSubChip,     'BB'),
    inst(AS_03,             'BW'),
    inst(AS_04,             'BBW'),
    inst(AS_05,             'BBL'),
    inst(Sleep,             'W'),
    inst(AS_07,             NO_OPERAND),
    inst(AS_08,             'BBLLL'),
    inst(AS_09,             'B'),
    inst(AS_0A,             'BBBL'),
    inst(AS_0B,             'WW'),
    inst(AS_0C,             NO_OPERAND,         0,                              as_0c),
    inst(AS_0D,             'BBLLLWW'),
    inst(AS_0E,             'B'),
    inst(AS_0F,             'WW'),
    inst(AS_10,             'WW'),
    inst(AS_11,             'BBLLLLB'),
    inst(LoadEffect,        'BS'),
    inst(AS_13,             'B'),
    inst(AS_14,             'B'),
    inst(WaitEffect,        'BB'),
    inst(AS_16,             'BB'),
    inst(AS_17,             'BB'),
    inst(PlayEffect,        'BBBBiiiHHHHHHB'),
    inst(AS_19,             'BBSBBiiiHHHHHHB'),
    inst(AS_1A,             'BBW'),
    inst(SetChrChip,        'BB'),
    inst(DamageCue,         'B'),
    inst(DamageAnime,       'BBB'),
    inst(AS_1E,             'L'),
    inst(AS_1F,             'WWB'),
    inst(AS_20,             'BBBLL'),
    inst(AS_21,             'BBLL'),
    inst(BeginChrThread,    'BBoB'),
    inst(AS_23,             'BB'),
    inst(AS_24,             'BBW'),
    inst(AS_25,             'BBW'),
    inst(AS_26,             'BBW'),
    inst(AS_27,             'BBW'),
    inst(Say,               'BSL'),
    inst(AS_29,             'B'),
    inst(ShowInfoText,      'SL'),
    inst(AS_2B,             NO_OPERAND),
    inst(ShowChrTrails,     'BWW'),
    inst(HideChrTrails,     'B'),
    inst(AS_2E,             'BLLL'),
    inst(AS_2F,             'BB'),
    inst(AS_31,             'BW'),
    inst(AS_32,             'BB'),
    inst(AS_33,             'BB'),
    inst(AS_34,             NO_OPERAND),
    inst(AS_35,             'BLLLW'),
    inst(AS_36,             'B'),
    inst(AS_39,             'WWWW'),
    inst(AS_3A,             'WW'),
    inst(AS_3B,             'LW'),
    inst(AS_3C,             'WW'),
    inst(AS_3D,             'WWWW'),
    inst(AS_3E,             'WW'),
    inst(AS_3F,             'B'),
    inst(AS_40,             'B'),
    inst(AS_43,             'BWL'),
    inst(AS_44,             'BWL'),
    inst(AS_45,             'BL'),
    inst(AS_46,             'BLL'),
    inst(AS_47,             'B'),
    inst(AS_48,             'BL'),
    inst(SetControl,        'BW'),
    inst(AS_4A,             'B'),
    inst(Jc,                'BBLo',             INSTRUCTION_START_BLOCK),
    inst(ForeachTarget,     'o',                INSTRUCTION_START_BLOCK),
    inst(InitForeachTarget, NO_OPERAND),
    inst(NextTarget,        'Bo',               INSTRUCTION_END_BLOCK), # combine next instruction: Jump(offset ForeachTarget)
    inst(AS_4F,             NO_OPERAND),
    inst(Call,              'o',                INSTRUCTION_START_BLOCK),   # ret stack size == 4
    inst(CallReturn,        NO_OPERAND),
    inst(AS_52,             'B'),
    inst(AS_53,             'B'),
    inst(SendMessage,       'B'),
    inst(MagicUsing,        'W'),
    inst(MagicEnd,          NO_OPERAND),
    inst(AS_57,             'BB'),
    inst(Knockback,         'B'),
    inst(AS_59,             'BW'),
    inst(AS_5A,             'BBW'),
    inst(AS_5B,             'W'),
    inst(ShowChr,           'BW'),
    inst(HideChr,           'BW'),
    inst(AS_5E,             'B'),
    inst(AS_5F,             'BB'),
    inst(AS_60,             'B'),
    inst(SetBattleSpeed,    'L'),
    inst(Voice,             'BIWWWB'),
    inst(Sound,             'H'),
    inst(SoundEx,           'HB'),
    inst(AS_66,             'W'),
    inst(AS_67,             'WBB'),
    inst(AS_68,             'BBL'),
    inst(LoadChrChip,       'BLB'),
    inst(AS_6B,             NO_OPERAND),
    inst(AS_6C,             NO_OPERAND),
    inst(AS_6D,             'L'),
    inst(AS_6E,             'L'),
    inst(AS_6F,             'BB'),
    inst(AS_70,             'BBWWWW'),
    inst(AS_71,             'B'),
    inst(AS_72,             NO_OPERAND),
    inst(AS_73,             'B'),
    inst(AS_74,             'BW'),
    inst(AS_77,             'B'),
    inst(AS_78,             'B'),
    inst(AS_79,             'B'),
    inst(AS_7A,             'B'),
    inst(AS_7B,             'W'),
    inst(AS_7C,             'BB'),
    inst(AS_7D,             'BL'),
    inst(AS_7E,             'L'),
    inst(AS_7F,             'WLBBB'),
    inst(AS_80,             'L'),
    inst(AS_82,             NO_OPERAND),
    inst(AS_83,             'B'),
    inst(AS_84,             'BWWWLB'),
    inst(AS_85,             'BBL'),
    inst(AS_87,             'WB'),
    inst(AS_89,             'B'),
    inst(AS_8A,             'BB'),
    inst(UseItemBegin,      NO_OPERAND),
    inst(UseItemEnd,        NO_OPERAND),
    inst(AS_8D,             'BLLLL'),
    inst(AS_8E,             NO_OPERAND,         0,                              as_8e),
    inst(AS_8F,             'B'),
    inst(AS_91,             NO_OPERAND,         0,                              as_91),
    inst(AS_92,             'BBLLLWL'),
    inst(AS_93,             'BBS'),
    inst(AS_94,             'BSL'),
    inst(AS_95,             NO_OPERAND),
    inst(AS_96,             'BSB'),
    inst(AS_97,             'WBB'),
    inst(AS_98,             'B'),
    inst(AS_99,             'B'),
    inst(AS_9A,             'L'),
    inst(AS_9B,             'B'),
    inst(AS_9C,             'B'),
    inst(AS_9E,             'BS'),
    inst(AS_9F,             'BB'),
    inst(AS_A0,             'BL'),
    inst(AS_A1,             'BLWS'),
    inst(AS_A6,             'BBLLB'),
    inst(AS_A7,             'BBBWWWWWWW'),
    inst(AS_A8,             'BB'),
    inst(AS_A9,             'BBL'),
    inst(AS_AC,             'LL'),
    inst(AS_AD,             'B'),
    inst(AS_AE,             ''),
    inst(AS_AF,             ''),
    inst(AS_B0,             ''),
    inst(AS_B1,             ''),
    inst(AS_B2,             ''),
    inst(AS_B3,             ''),
    inst(AS_B4,             ''),
    inst(AS_B5,             ''),
    inst(AS_B6,             ''),
    inst(AS_B7,             ''),
    inst(AS_B8,             ''),
]

del inst

for op in edao_as_op_list:
    edao_as_op_table[op.OpCode] = op
    op.Container = edao_as_op_table

enable_stat = 10

if enable_stat != 0:
    valid = 0
    for inst in edao_as_op_list:
        if inst.OpName[:3] != 'AS_':
            valid += 1
    print('known: %d (%d%%)' % (valid, valid / len(edao_as_op_list) * 100))
    print('total: %d' % len(edao_as_op_list))
    input()
