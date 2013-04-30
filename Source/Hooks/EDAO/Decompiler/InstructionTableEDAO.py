from InstructionTable import *

CODE_PAGE = '936'

def SplitText(text):
    return text.split('\x01')

InstructionNames = {}

InstructionNames[0x00]  = 'OP_00'
InstructionNames[0x01]  = 'Return'
InstructionNames[0x02]  = 'If'
InstructionNames[0x03]  = 'Jump'
InstructionNames[0x04]  = 'Switch'
InstructionNames[0x05]  = 'Call'
InstructionNames[0x06]  = 'NewScene'
InstructionNames[0x07]  = 'OP_07'
InstructionNames[0x08]  = 'OP_08'
InstructionNames[0x09]  = 'SetXXXFlags'
InstructionNames[0x0A]  = 'ClearXXXFlags'
InstructionNames[0x0B]  = 'OP_0B'
InstructionNames[0x0C]  = 'OP_0C'
InstructionNames[0x0D]  = 'OP_0D'
InstructionNames[0x0E]  = 'OP_0E'
InstructionNames[0x0F]  = 'Battle'
InstructionNames[0x10]  = 'OP_10'
InstructionNames[0x11]  = 'OP_11'
InstructionNames[0x12]  = 'OP_12'
InstructionNames[0x13]  = 'OP_13'
InstructionNames[0x14]  = 'OP_14'
InstructionNames[0x15]  = 'OP_15'
InstructionNames[0x16]  = 'OP_16'
InstructionNames[0x17]  = 'OP_17'
InstructionNames[0x19]  = 'EventBegin'
InstructionNames[0x1A]  = 'EventEnd'
InstructionNames[0x1B]  = 'OP_1B'
InstructionNames[0x1C]  = 'OP_1C'
InstructionNames[0x1D]  = 'OP_1D'
InstructionNames[0x1E]  = 'PlayBgm'
InstructionNames[0x1F]  = 'OP_1F'
InstructionNames[0x20]  = 'VolumeBgm'
InstructionNames[0x21]  = 'OP_21'
InstructionNames[0x22]  = 'OP_22'
InstructionNames[0x23]  = 'Sound'
InstructionNames[0x24]  = 'OP_24'
InstructionNames[0x25]  = 'OP_25'
InstructionNames[0x26]  = 'SoundDistance'
InstructionNames[0x27]  = 'SoundLoad'
InstructionNames[0x28]  = 'OP_28'
InstructionNames[0x29]  = 'OP_29'
InstructionNames[0x2A]  = 'OP_2A'
InstructionNames[0x2B]  = 'OP_2B'
InstructionNames[0x2C]  = 'OP_2C'
InstructionNames[0x2D]  = 'OP_2D'
InstructionNames[0x2E]  = 'OP_2E'
InstructionNames[0x2F]  = 'OP_2F'
InstructionNames[0x30]  = 'OP_30'
InstructionNames[0x31]  = 'OP_31'
InstructionNames[0x32]  = 'OP_32'
InstructionNames[0x35]  = 'OP_35'
InstructionNames[0x36]  = 'OP_36'
InstructionNames[0x37]  = 'OP_37'
InstructionNames[0x38]  = 'OP_38'
InstructionNames[0x39]  = 'OP_39'
InstructionNames[0x3A]  = 'OP_3A'
InstructionNames[0x3B]  = 'OP_3B'
InstructionNames[0x3C]  = 'OP_3C'
InstructionNames[0x3D]  = 'OP_3D'
InstructionNames[0x3E]  = 'OP_3E'
InstructionNames[0x3F]  = 'OP_3F'
InstructionNames[0x40]  = 'OP_40'
InstructionNames[0x41]  = 'OP_41'
InstructionNames[0x42]  = 'OP_42'
InstructionNames[0x43]  = 'OP_43'
InstructionNames[0x44]  = 'OP_44'
InstructionNames[0x45]  = 'OP_45'
InstructionNames[0x46]  = 'OP_46'
InstructionNames[0x47]  = 'OP_47'
InstructionNames[0x48]  = 'OP_48'
InstructionNames[0x49]  = 'OP_49'
InstructionNames[0x4A]  = 'OP_4A'
InstructionNames[0x4B]  = 'OP_4B'
InstructionNames[0x4C]  = 'OP_4C'
InstructionNames[0x4D]  = 'OP_4D'
InstructionNames[0x4E]  = 'OP_4E'
InstructionNames[0x4F]  = 'OP_4F'
InstructionNames[0x50]  = 'OP_50'
InstructionNames[0x51]  = 'OP_51'
InstructionNames[0x52]  = 'OP_52'
InstructionNames[0x53]  = 'OP_53'
InstructionNames[0x54]  = 'OP_54'
InstructionNames[0x55]  = 'AnonymousTalk'
InstructionNames[0x56]  = 'OP_56'
InstructionNames[0x57]  = 'OP_57'
InstructionNames[0x58]  = 'OP_58'
InstructionNames[0x59]  = 'OP_59'
InstructionNames[0x5A]  = 'OP_5A'
InstructionNames[0x5B]  = 'OP_5B'
InstructionNames[0x5C]  = 'ChrTalk'
InstructionNames[0x5D]  = 'NpcTalk'
InstructionNames[0x5E]  = 'Menu'
InstructionNames[0x5F]  = 'MenuEnd'
InstructionNames[0x60]  = 'OP_60'
InstructionNames[0x61]  = 'OP_61'
InstructionNames[0x62]  = 'OP_62'
InstructionNames[0x63]  = 'OP_63'
InstructionNames[0x64]  = 'OP_64'
InstructionNames[0x65]  = 'OP_65'
InstructionNames[0x66]  = 'OP_66'
InstructionNames[0x67]  = 'OP_67'
InstructionNames[0x68]  = 'OP_68'
InstructionNames[0x69]  = 'OP_69'
InstructionNames[0x6A]  = 'OP_6A'
InstructionNames[0x6B]  = 'OP_6B'
InstructionNames[0x6C]  = 'OP_6C'
InstructionNames[0x6D]  = 'OP_6D'
InstructionNames[0x6E]  = 'OP_6E'
InstructionNames[0x6F]  = 'OP_6F'
InstructionNames[0x70]  = 'OP_70'
InstructionNames[0x71]  = 'OP_71'
InstructionNames[0x72]  = 'OP_72'
InstructionNames[0x73]  = 'OP_73'
InstructionNames[0x74]  = 'OP_74'
InstructionNames[0x75]  = 'OP_75'
InstructionNames[0x76]  = 'OP_76'
InstructionNames[0x77]  = 'OP_77'
InstructionNames[0x78]  = 'OP_78'
InstructionNames[0x79]  = 'OP_79'
InstructionNames[0x7A]  = 'OP_7A'
InstructionNames[0x7B]  = 'OP_7B'
InstructionNames[0x7D]  = 'OP_7D'
InstructionNames[0x82]  = 'OP_82'
InstructionNames[0x83]  = 'OP_83'
InstructionNames[0x84]  = 'OP_84'
InstructionNames[0x85]  = 'LoadEffect'
InstructionNames[0x86]  = 'PlayEffect'
InstructionNames[0x87]  = 'OP_87'
InstructionNames[0x88]  = 'OP_88'
InstructionNames[0x89]  = 'OP_89'
InstructionNames[0x8A]  = 'OP_8A'
InstructionNames[0x8B]  = 'OP_8B'
InstructionNames[0x8C]  = 'OP_8C'
InstructionNames[0x8D]  = 'OP_8D'
InstructionNames[0x8E]  = 'OP_8E'
InstructionNames[0x8F]  = 'OP_8F'
InstructionNames[0x90]  = 'OP_90'
InstructionNames[0x91]  = 'OP_91'
InstructionNames[0x92]  = 'OP_92'
InstructionNames[0x93]  = 'OP_93'
InstructionNames[0x94]  = 'OP_94'
InstructionNames[0x95]  = 'OP_95'
InstructionNames[0x96]  = 'OP_96'
InstructionNames[0x97]  = 'OP_97'
InstructionNames[0x98]  = 'OP_98'
InstructionNames[0x99]  = 'OP_99'
InstructionNames[0x9A]  = 'OP_9A'
InstructionNames[0x9B]  = 'OP_9B'
InstructionNames[0x9C]  = 'OP_9C'
InstructionNames[0x9D]  = 'OP_9D'
InstructionNames[0x9E]  = 'OP_9E'
InstructionNames[0x9F]  = 'OP_9F'
InstructionNames[0xA0]  = 'OP_A0'
InstructionNames[0xA1]  = 'OP_A1'
InstructionNames[0xA2]  = 'OP_A2'
InstructionNames[0xA3]  = 'OP_A3'
InstructionNames[0xA4]  = 'OP_A4'
InstructionNames[0xA5]  = 'OP_A5'
InstructionNames[0xA6]  = 'OP_A6'
InstructionNames[0xA7]  = 'OP_A7'
InstructionNames[0xA8]  = 'OP_A8'
InstructionNames[0xA9]  = 'OP_A9'
InstructionNames[0xAA]  = 'OP_AA'
InstructionNames[0xAB]  = 'OP_AB'
InstructionNames[0xAC]  = 'OP_AC'
InstructionNames[0xAD]  = 'OP_AD'
InstructionNames[0xAE]  = 'OP_AE'
InstructionNames[0xAF]  = 'OP_AF'
InstructionNames[0xB2]  = 'OP_B2'
InstructionNames[0xB3]  = 'OP_B3'
InstructionNames[0xB4]  = 'OP_B4'
InstructionNames[0xB5]  = 'OP_B5'
InstructionNames[0xB6]  = 'OP_B6'
InstructionNames[0xB7]  = 'OP_B7'
InstructionNames[0xB8]  = 'OP_B8'
InstructionNames[0xB9]  = 'OP_B9'
InstructionNames[0xBA]  = 'OP_BA'
InstructionNames[0xBC]  = 'OP_BC'
InstructionNames[0xBD]  = 'OP_BD'
InstructionNames[0xBE]  = 'OP_BE'
InstructionNames[0xBF]  = 'OP_BF'
InstructionNames[0xC0]  = 'OP_C0'
InstructionNames[0xC2]  = 'OP_C2'
InstructionNames[0xC3]  = 'OP_C3'
InstructionNames[0xC4]  = 'OP_C4'
InstructionNames[0xC5]  = 'OP_C5'
InstructionNames[0xC7]  = 'OP_C7'
InstructionNames[0xC9]  = 'OP_C9'
InstructionNames[0xCA]  = 'OP_CA'
InstructionNames[0xCB]  = 'OP_CB'
InstructionNames[0xCC]  = 'OP_CC'
InstructionNames[0xCD]  = 'PlaceName2'
InstructionNames[0xCE]  = 'OP_CE'
InstructionNames[0xCF]  = 'OP_CF'
InstructionNames[0xD0]  = 'MenuCmd'
InstructionNames[0xD1]  = 'OP_D1'
InstructionNames[0xD2]  = 'OP_D2'
InstructionNames[0xD3]  = 'OP_D3'
InstructionNames[0xD4]  = 'OP_D4'
InstructionNames[0xD5]  = 'OP_D5'
InstructionNames[0xD6]  = 'LoadChr'
InstructionNames[0xD7]  = 'OP_D7'
InstructionNames[0xD8]  = 'OP_D8'
InstructionNames[0xD9]  = 'OP_D9'
InstructionNames[0xDA]  = 'OP_DA'
InstructionNames[0xDC]  = 'OP_DC'
InstructionNames[0xDD]  = 'OP_DD'
InstructionNames[0xDE]  = 'OP_DE'
InstructionNames[0xDF]  = 'LoadAnimeChip'
InstructionNames[0xE0]  = 'OP_E0'
InstructionNames[0xE2]  = 'OP_E2'
InstructionNames[0xE3]  = 'OP_E3'
InstructionNames[0xE4]  = 'OP_E4'
InstructionNames[0xE5]  = 'OP_E5'
InstructionNames[0xE6]  = 'OP_E6'
InstructionNames[0xE7]  = 'OP_E7'
InstructionNames[0xE8]  = 'OP_E8'
InstructionNames[0xE9]  = 'OP_E9'
InstructionNames[0xF0]  = 'OP_F0'
InstructionNames[0xF3]  = 'OP_F3'
InstructionNames[0xF4]  = 'OP_F4'
InstructionNames[0xFA]  = 'OP_FA'
InstructionNames[0xFB]  = 'OP_FB'
InstructionNames[0xFC]  = 'OP_FC'
InstructionNames[0xFD]  = 'OP_FD'
InstructionNames[0xFE]  = 'OP_FE'
InstructionNames[0xFF]  = 'OP_FF'

for op, name in InstructionNames.items():
    expr = '%s = 0x%08X' % (name, op)
    exec(expr)

class EDAOInstructionTableEntry(InstructionTableEntry):
    def __init__(self, op, name = '', operand = NO_OPERAND, flags = 0, handler = None):
        super().__init__(op, name, operand, flags, handler)

    def GetOperand(self, opr, fs):
        if opr.lower() != 's':
            return super().GetOperand(opr, fs)

        string = b''
        while True:
            buf = fs.read(1)
            if buf == b'\x07':
                buf += fs.read(1)
            elif buf == b'' or buf == b'\x00':
                break

            string += buf

        return string.decode(self.Container.CodePage)

    def GetOperandSize(self, opr, fs):
        if opr.lower() != 's':
            return super().GetOperandSize(opr, fs)

        pos = fs.tell()
        oprsize = len(self.GetOperand(opr, fs))
        fs.seek(pos)
        return oprsize

def inst(op, operand = NO_OPERAND, flags = 0, handler = None):
    return EDAOInstructionTableEntry(op, InstructionNames[op], operand, flags, handler)

def instopr(opr, size):
    return InstructionOperand(opr, size)

def GetOpCode(fs):
    return fs.byte()

EXPRESSION_PUSH_LONG        = 0x00
EXPRESSION_END              = 0x01
EXPRESSION_EQU              = 0x02
EXPRESSION_NEQ              = 0x03
EXPRESSION_LSS              = 0x04
EXPRESSION_GTR              = 0x05
EXPRESSION_LEQ              = 0x06
EXPRESSION_GE               = 0x07
EXPRESSION_EQUZ             = 0x08
EXPRESSION_NEQUZ_I64        = 0x09
EXPRESSION_AND              = 0x0A
EXPRESSION_OR               = 0x0B
EXPRESSION_ADD              = 0x0C
EXPRESSION_SUB              = 0x0D
EXPRESSION_NEG              = 0x0E
EXPRESSION_XOR              = 0x0F
EXPRESSION_IMUL             = 0x10
EXPRESSION_IDIV             = 0x11
EXPRESSION_IMOD             = 0x12
EXPRESSION_STUB             = 0x13
EXPRESSION_IMUL_SAVE        = 0x14
EXPRESSION_IDIV_SAVE        = 0x15
EXPRESSION_IMOD_SAVE        = 0x16
EXPRESSION_ADD_SAVE         = 0x17
EXPRESSION_SUB_SAVE         = 0x18
EXPRESSION_AND_SAVE         = 0x19
EXPRESSION_XOR_SAVE         = 0x1A
EXPRESSION_OR_SAVE          = 0x1B
EXPRESSION_EXEC_OP          = 0x1C
EXPRESSION_NOT              = 0x1D
EXPRESSION_1E               = 0x1E
EXPRESSION_GET_RESULT       = 0x1F
EXPRESSION_PUSH_VALUE_INDEX = 0x20
EXPRESSION_GET_CHR_WORK     = 0x21
EXPRESSION_RAND             = 0x22
EXPRESSION_23               = 0x23

class ScpExpression:
    def __init__(self, operation = None, operand = None):
        self.Operation = operation
        self.Operand = operand if operand != None else []

def ParseScpExpression(data):
    expr = []
    fs = data.FileStream

    # stack size == 0xB0 ?

    while True:
        operation = fs.byte()

        scpexpr = ScpExpression(operation)

        if operation == EXPRESSION_PUSH_LONG:

            scpexpr.Operand.append(fs.ulong())

        elif operation == EXPRESSION_END:

            break

        elif operation == EXPRESSION_EQU            or \
             operation == EXPRESSION_NEQ            or \
             operation == EXPRESSION_LSS            or \
             operation == EXPRESSION_GTR            or \
             operation == EXPRESSION_LEQ            or \
             operation == EXPRESSION_GE             or \
             operation == EXPRESSION_EQUZ           or \
             operation == EXPRESSION_NEQUZ_I64      or \
             operation == EXPRESSION_AND            or \
             operation == EXPRESSION_OR             or \
             operation == EXPRESSION_ADD            or \
             operation == EXPRESSION_SUB            or \
             operation == EXPRESSION_NEG            or \
             operation == EXPRESSION_XOR            or \
             operation == EXPRESSION_IMUL           or \
             operation == EXPRESSION_IDIV           or \
             operation == EXPRESSION_IMOD           or \
             operation == EXPRESSION_STUB           or \
             operation == EXPRESSION_IMUL_SAVE      or \
             operation == EXPRESSION_IDIV_SAVE      or \
             operation == EXPRESSION_IMOD_SAVE      or \
             operation == EXPRESSION_ADD_SAVE       or \
             operation == EXPRESSION_SUB_SAVE       or \
             operation == EXPRESSION_AND_SAVE       or \
             operation == EXPRESSION_XOR_SAVE       or \
             operation == EXPRESSION_OR_SAVE        or \
             operation == EXPRESSION_NOT:

            # pop all operand, and push result
            pass

        elif operation == EXPRESSION_EXEC_OP:

            # execute one op code

            execdata = data.CreateBranch()
            execdata.Instruction.OpCode = fs.byte()
            execdata.TableEntry = data.TableEntry.Container[execdata.Instruction.OpCode]
            execinst = execdata.Disasm(execdata)
            scpexpr.Operand.append(execinst)

        elif operation == EXPRESSION_1E or \
             operation == EXPRESSION_GET_RESULT:

            scpexpr.Operand.append(fs.ushort())

        elif operation == EXPRESSION_PUSH_VALUE_INDEX:

            scpexpr.Operand.append(fs.byte())

        elif operation == EXPRESSION_GET_CHR_WORK:

            scpexpr.Operand.append(fs.ushort())
            scpexpr.Operand.append(fs.byte())

        elif operation == EXPRESSION_RAND:

            pass

        elif operation == EXPRESSION_23:

            scpexpr.Operand.append(fs.byte())

        expr.append(scpexpr)

    return expr

def scp_if(data):
    # if (expression)
    #   goto offset

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        ins = data.Instruction
        expr = ParseScpExpression(data)
        ins.Operand.append(expr)

        offset = fs.ulong()
        ins.Operand.append(offset)
        ins.BranchTargets.append(offset)

        return ins

def scp_switch(data):

    # switch (expression)
    #     case option_id:
    #         goto option_offset;
    #     default:
    #         goto default_offset

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        ins = data.Instruction

        expr = ParseScpExpression(data)
        optioncount = fs.byte()
        options = []

        for i in range(optioncount):
            optionid, optionoffset = struct.unpack('<HL', fs.read(6))
            options.append((optionid, optionoffset))
            ins.BranchTargets.append(optionoffset)

        defaultoffset = fs.ulong()

        ins.BranchTargets.append(defaultoffset)

        ins.Operand.append(expr)
        ins.Operand.append(options)
        ins.Operand.append(defaultoffset)

        return ins

def scp_battle(data):

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        ins = data.Instruction

        opr1 = fs.ulong()
        opr2 = fs.ulong()

        ins.Operand.append(opr1)
        ins.Operand.append(opr2)

        if opr1 != 0xFFFFFFFF:
            ins.Operand.append(fs.byte())
            ins.Operand.append(fs.ushort())
            ins.Operand.append(fs.ushort())
            ins.Operand.append(fs.ushort())

            return ins

        name = data.TableEntry.GetOperand('s', fs)
        ins.Operand.append(name)

        for i in range(4):
            ins.Operand.append(fs.ulong())

        for i in range(8):
            ins.Operand.append(fs.ulong())

        ins.Operand.append(fs.ushort())
        ins.Operand.append(fs.ushort())

        return ins

def scp_1d(data):

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        ins = data.Instruction

        opr1 = fs.byte()
        opr2 = fs.byte()

        ins.Operand.append(opr1)
        ins.Operand.append(opr2)

        operand = ''

        if opr1 == 0:
            operand = 'BBLLLLLL'
        elif opr1 == 2 or opr1 == 3:
            operand = 'B'

        ins.Operand += data.TableEntry.GetAllOperand(operand, fs)
        return ins

def scp_29(data):

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        ins = data.Instruction

        opr1 = fs.ushort()
        opr2 = fs.byte()

        ins.Operand.append(opr1)
        ins.Operand.append(opr2)

        operand = ''

        if opr2 == 1 or opr2 == 2:
            operand = 'W'
        elif opr2 == 3 or opr2 == 4:
            operand = 'B'

        ins.Operand += data.TableEntry.GetAllOperand(operand, fs)
        return ins

def scp_2a(data):

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        ins = data.Instruction

        opr1 = fs.ushort()
        opr2 = fs.byte()

        ins.Operand.append(opr1)
        ins.Operand.append(opr2)

        operand = ''

        if opr2 == 1:
            operand = 'W'
        else:
            operand = 'B'

        ins.Operand += data.TableEntry.GetAllOperand(operand, fs)
        return ins

def scp_2b(data):

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        ins = data.Instruction

        for i in range(0xC):
            opr = fs.ushort()
            ins.Operand.append(opr)
            if opr == 0xFFFF:
                break

        return ins

def scp_38(data):

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        ins = data.Instruction

        opr1 = fs.byte()
        opr2 = fs.byte()

        ins.Operand.append(opr1)
        ins.Operand.append(opr2)

        operand = ''

        if opr2 == 0x7F:
            operand = 'B'
        elif opr2 >= 0x80 and opr2 <= 0x87:
            operand = 'B'

        ins.Operand += data.TableEntry.GetAllOperand(operand, fs)
        return ins

def scp_4e(data):

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        ins = data.Instruction
        ins.Operand.append(fs.ushort())
        ins.Operand.append(ParseScpExpression(data))

        return ins

def scp_50(data):

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        ins = data.Instruction
        ins.Operand.append(fs.byte())
        ins.Operand.append(ParseScpExpression(data))

        return ins

def scp_52(data):

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        ins = data.Instruction

        ins.Operand = data.TableEntry.GetAllOperand('WB', fs)
        ins.Operand.append(ParseScpExpression(data))

        return ins

def scp_anonymous_talk(data):

    if data.Reason == HANDLER_REASON_READ:
        fs = data.FileStream
        ins = data.Instruction

        if fs.tell() == 0x71B1:
            bp()

        target = fs.ushort()
        text = data.TableEntry.GetOperand('S', fs)
        text = SplitText(text)

        ins.Operand.append(target)
        ins.Operand.append(text)

        return ins

def scp_create_chr_talk(data):

    if data.Reason == HANDLER_REASON_READ:

        # #FACE_INDEX
        # split by 0x00 0x01 0x03 0x04 0x06 0x07 0x0A 0x1F

        fs = data.FileStream
        ins = data.Instruction
        ins.Operand = data.TableEntry.GetAllOperand('W', fs)
        text = SplitText(data.TableEntry.GetOperand('S', fs))
        ins.Operand.append(text)

        return ins

def scp_create_npc_talk(data):

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        ins = data.Instruction

        target = fs.ushort()
        name = data.TableEntry.GetOperand('S', fs)
        text = data.TableEntry.GetOperand('S', fs)
        text = SplitText(text)

        ins.Operand.append(target)
        ins.Operand.append(name)
        ins.Operand.append(text)

        return ins

def scp_create_menu(data):

    # max 10 line

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        ins = data.Instruction
        ins.Operand = data.TableEntry.GetAllOperand('WWWB', fs)
        menutext = data.TableEntry.GetOperand('S', fs)

        menuitems = SplitText(menutext)
        ins.Operand.append(menuitems)

        return ins

def scp_76(data):

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        ins = data.Instruction

        ins.Operand = data.TableEntry.GetAllOperand('BSB', fs)

        opr3 = ins.Operand[2]

        operand = ''
        if opr3 == 0 or \
           opr3 == 1 or \
           opr3 == 3:

            operand = 'L'

        elif opr3 == 2:

            operand = 'S'

        ins.Operand += data.TableEntry.GetAllOperand(operand, fs)

        return ins

def scp_9f(data):

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        ins = data.Instruction

        ins.Operand = data.TableEntry.GetAllOperand('B', fs)

        opr = ins.Operand[0]

        operand = ''
        if opr == 0:
            operand = 'W'
        elif opr == 1:
            operand = 'LLL'
        else:
            operand = 'WLB'

        ins.Operand += data.TableEntry.GetAllOperand(operand, fs)

        return ins

def scp_cf(data):

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        ins = data.Instruction

        ins.Operand = data.TableEntry.GetAllOperand('BB', fs)

        if ins.Operand[0] != 0:
            ins.Operand += data.TableEntry.GetAllOperand('B', fs)

        return ins

def scp_menu_cmd(data):

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream

        ins = Instruction()
        ins = data.Instruction

        menutype = fs.byte()
        menu_xxx = fs.byte()

        ins.Operand.append(menutype)
        ins.Operand.append(menu_xxx)

        operand = ''

        if menutype == 0:
            pass
        elif menutype == 1:
            operand = 'S'
        elif menutype == 2:
            operand = 'WWB'
        elif menutype == 3:
            operand = 'B'
        elif menutype == 4:
            operand = 'B'
        elif menutype == 5:
            operand = 'B'
        elif menutype == 6:
            pass

        ins.Operand += data.TableEntry.GetAllOperand(operand, fs)

        return ins

def scp_d2(data):

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        ins = data.Instruction
        ins.Operand.append(fs.byte())
        ins.Operand.append(ParseScpExpression(data))

        return ins

def scp_e4(data):

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        ins = data.Instruction

        opr = fs.byte()
        ins.Operand.append(opr)

        operand = ''
        if opr == 0:
            operand = 'BB'
        elif opr == 1:
            operand = 'B'
        elif opr == 2:
            operand = 'B'
        elif opr == 3:
            pass

        ins.Operand += data.TableEntry.GetAllOperand(operand, fs)

        return ins

edao_op_list = \
[
    inst(OP_00),
    inst(Return,            NO_OPERAND,         INSTRUCTION_END_BLOCK),
    inst(If,                NO_OPERAND,         INSTRUCTION_START_BLOCK,        scp_if),
    inst(Jump,              'O',                INSTRUCTION_END_BLOCK),
    inst(Switch,            NO_OPERAND,         INSTRUCTION_START_BLOCK,        scp_switch),
    inst(Call,              'BB'),          # included_scp index, func index
    inst(NewScene,          'LBB'),
    inst(OP_07,             NO_OPERAND),
    inst(OP_08,             'W'),
    inst(SetXXXFlags,       'L'),
    inst(ClearXXXFlags,     'L'),
    inst(OP_0B,             'LLB'),
    inst(OP_0C,             'LL'),
    inst(OP_0D),
    inst(OP_0E,             'L'),
    inst(Battle,            NO_OPERAND,         0,                              scp_battle),
    inst(OP_10,             'BB'),
    inst(OP_11,             'BBBLLL'),
    inst(OP_12,             'WWB'),
    inst(OP_13,             'W'),   # poswnd
    inst(OP_14,             'WLWBW'),
    inst(OP_15,             'L'),
    inst(OP_16,             'B'),
    inst(OP_17),
    inst(EventBegin,        'B'),
    inst(EventEnd,          'B'),
    inst(OP_1B,             'BBW'),
    inst(OP_1C,             'BBBBBBWW'),
    inst(OP_1D,             NO_OPERAND,         0,                              scp_1d),
    inst(PlayBgm,           'WB'),
    inst(OP_1F),
    inst(VolumeBgm,         'BL'),
    inst(OP_21,             'L'),
    inst(OP_22),
    inst(Sound,             'WBBB'),
    inst(OP_24,             'W'),
    inst(OP_25,             'WB'),
    inst(SoundDistance,     'WLLLLLBL'),
    inst(SoundLoad,         'W'),
    inst(OP_28),
    inst(OP_29,             NO_OPERAND,         0,                              scp_29),
    inst(OP_2A,             NO_OPERAND,         0,                              scp_2a),
    inst(OP_2B,             NO_OPERAND,         0,                              scp_2b),
    inst(OP_2C,             'WW'),
    inst(OP_2D,             'WW'),
    inst(OP_2E,             'BBB'),
    inst(OP_2F,             'BB'),
    inst(OP_30),
    inst(OP_31,             'B'),
    inst(OP_32,             'BBW'),
    inst(OP_35,             'BW'),
    inst(OP_36,             'BW'),
    inst(OP_37),
    inst(OP_38,             NO_OPERAND,         0,                              scp_38),
    inst(OP_39,             'BW'),
    inst(OP_3A,             'BW'),
    inst(OP_3B,             'W'),
    inst(OP_3C,             'W'),
    inst(OP_3D,             'W'),
    inst(OP_3E,             'W'),
    inst(OP_3F,             'WW'),
    inst(OP_40,             'WW'),
    inst(OP_41,             'WB'),
    inst(OP_42,             'BWB'),
    inst(OP_43,             'B'),
    inst(OP_44,             'WBBB'),
    inst(OP_45,             'WB'),
    inst(OP_46,             'WBB'),
    inst(OP_47,             'WBB'),
    inst(OP_48,             'WB'),
    inst(OP_49),
    inst(OP_4A,             'BB'),
    inst(OP_4B,             'WB'),
    inst(OP_4C,             'WB'),
    inst(OP_4D),
    inst(OP_4E,             NO_OPERAND,         0,                              scp_4e),
    inst(OP_4F),
    inst(OP_50,             NO_OPERAND,         0,                              scp_50),
    inst(OP_51),
    inst(OP_52,             NO_OPERAND,         0,                              scp_52),
    inst(OP_53,             'W'),
    inst(OP_54,             'W'),
    inst(AnonymousTalk,     NO_OPERAND,         0,                              scp_anonymous_talk),
    inst(OP_56),
    inst(OP_57,             'B'),
    inst(OP_58,             'WWWS'),
    inst(OP_59),
    inst(OP_5A),
    inst(OP_5B,             'WWWW'),
    inst(ChrTalk,           NO_OPERAND,         0,                              scp_create_chr_talk),
    inst(NpcTalk,           NO_OPERAND,         0,                              scp_create_npc_talk),
    inst(Menu,              NO_OPERAND,         0,                              scp_create_menu),
    inst(MenuEnd,           'W'),
    inst(OP_60,             'W'),
    inst(OP_61,             'S'),
    inst(OP_62,             'W'),
    inst(OP_63,             'WLLBBLB'),
    inst(OP_64,             'W'),
    inst(OP_65,             'BW'),
    inst(OP_66,             'BW'),
    inst(OP_67,             'W'),
    inst(OP_68,             'LLLL'),
    inst(OP_69,             'BW'),
    inst(OP_6A,             'WL'),
    inst(OP_6B,             'W'),
    inst(OP_6C,             'LL'),
    inst(OP_6D,             'WWWL'),
    inst(OP_6E,             'LL'),
    inst(OP_6F,             'B'),
    inst(OP_70,             'BW'),
    inst(OP_71,             'BWWWL'),
    inst(OP_72,             'BL'),
    inst(OP_73,             'BL'),
    inst(OP_74,             'WB'),
    inst(OP_75,             'BBL'),
    inst(OP_76,             'BSB',              0,                              scp_76),
    inst(OP_77,             'BW'),
    inst(OP_78,             'BW'),
    inst(OP_79,             'W'),
    inst(OP_7A,             'BL'),
    inst(OP_7B,             'B'),
    inst(OP_7D,             'BBBBL'),
    inst(OP_82,             'LLLL'),
    inst(OP_83,             'BWWW'),
    inst(OP_84,             'BB'),
    inst(LoadEffect,        'BS'),
    inst(PlayEffect,        'BBWWLLLWWWLLLWLLLL'),
    inst(OP_87,             'BBBSWLLLWWWLLLL'),
    inst(OP_88,             'BB'),
    inst(OP_89,             'BB'),
    inst(OP_8A,             'B'),
    inst(OP_8B,             'W'),
    inst(OP_8C,             'WB'),
    inst(OP_8D,             'WB'),
    inst(OP_8E,             'WS'),
    inst(OP_8F,             'WLLLW'),
    inst(OP_90,             'WLLLW'),
    inst(OP_91,             'WWW'),
    inst(OP_92,             'WLLW'),
    inst(OP_93,             'WWW'),
    inst(OP_94,             'WLLLLL'),
    inst(OP_95,             'WLLLLB'),
    inst(OP_96,             'WLLLLB'),
    inst(OP_97,             'WLLLLB'),
    inst(OP_98,             'WLLLLB'),
    inst(OP_99,             'WWLLB'),
    inst(OP_9A,             'WWLLB'),
    inst(OP_9B,             'BWWLLB'),
    inst(OP_9C,             'WLLLLL'),
    inst(OP_9D,             'WLLLLL'),
    inst(OP_9E,             'WLLLLW'),
    inst(OP_9F,             NO_OPERAND,             0,                          scp_9f),
    inst(OP_A0,             'WWBB'),
    inst(OP_A1,             'WWB'),
    inst(OP_A2,             'WW'),
    inst(OP_A3,             'WW'),
    inst(OP_A4,             'WW'),
    inst(OP_A5,             'WW'),
    inst(OP_A6,             'WLLLL'),
    inst(OP_A7,             'WBBBBL'),
    inst(OP_A8,             'WBBBL'),
    inst(OP_A9,             'W'),
    inst(OP_AA,             'W'),
    inst(OP_AB,             'W'),
    inst(OP_AC,             'W'),
    inst(OP_AD,             'W'),
    inst(OP_AE,             'WW'),
    inst(OP_AF,             'B'),
    inst(OP_B2,             'W'),
    inst(OP_B3,             'B'),
    inst(OP_B4,             'B'),
    inst(OP_B5,             'BW'),
    inst(OP_B6),
    inst(OP_B7,             'BBW'),
    inst(OP_B8,             'BSWW'),
    inst(OP_B9,             'B'),
    inst(OP_BA,             'WW'),
    inst(OP_BC,             'B'),
    inst(OP_BD,             'WW'),
    inst(OP_BE,             'BW'),
    inst(OP_BF,             'BB'),
    inst(OP_C0,             'BBL'),
    inst(OP_C2),
    inst(OP_C3,             'BBWWWBLLLLLL'),
    inst(OP_C4,             'BBWW'),
    inst(OP_C5,             'BLLLLLLLL'),
    inst(OP_C7,             'BB'),
    inst(OP_C9,             'BL'),
    inst(OP_CA,             'BWWWWWWWWWWWWLBS'),
    inst(OP_CB,             'BBLLLL'),
    inst(OP_CC,             'BBB'),
    inst(PlaceName2,        'WWSBW'),
    inst(OP_CE,             'B'),
    inst(OP_CF,             NO_OPERAND,             0,                          scp_cf),
    inst(MenuCmd,           NO_OPERAND,             0,                          scp_menu_cmd),
    inst(OP_D1,             'W'),
    inst(OP_D2,             NO_OPERAND,             0,                          scp_d2),
    inst(OP_D3,             'WBS'),
    inst(OP_D4,             'LL'),
    inst(OP_D5,             'WLLLL'),
    inst(LoadChr,           'LB'),
    inst(OP_D7,             'B'),
    inst(OP_D8,             'BB'),
    inst(OP_D9,             'BB'),
    inst(OP_DA,             'B'),
    inst(OP_DC,             'B'),
    inst(OP_DD),
    inst(OP_DE,             'S'),
    inst(LoadAnimeChip,     'WBB'),
    inst(OP_E0,             'BB'),
    inst(OP_E2,             'B'),
    inst(OP_E3,             'LLL'),
    inst(OP_E4,             NO_OPERAND,             0,                          scp_e4),
    inst(OP_E5,             'B'),
    inst(OP_E6,             'BBBBBBL'),
    inst(OP_E7),
    inst(OP_E8),
    inst(OP_E9),
    inst(OP_F0,             'BW'),
    inst(OP_F3,             'L'),
    inst(OP_F4,             'B'),
    inst(OP_FA,             'W'),
    inst(OP_FB,             'WB'),
    inst(OP_FC,             'W'),
    inst(OP_FD,             'WW'),
    inst(OP_FE,             'B'),
    inst(OP_FF,             'BLLL'),
]

del inst

edao_op_table = InstructionTable(GetOpCode, CODE_PAGE)

for op in edao_op_list:
    edao_op_table[op.OpCode] = op
    op.Container = edao_op_table

#valid = 0
#for inst in edao_op_list:
#    if inst.Handler != None:
#        valid += 1

#print('handler: %d' % valid)
#print('%d / %d / 227' % (len(edao_op_list), 227 - len(edao_op_list)))

#input()
