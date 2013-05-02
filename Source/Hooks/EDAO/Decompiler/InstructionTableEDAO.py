from InstructionTable import *

CODE_PAGE = '936'

def GetOpCode(fs):
    return fs.byte()

def WriteOpCode(op):
    return struct.pack('<B', op)

edao_op_table = InstructionTable(GetOpCode, WriteOpCode, DefaultGetLabelName, CODE_PAGE)

InstructionNames = {}

InstructionNames[0x00]  = 'OP_00'
InstructionNames[0x01]  = 'Return'
InstructionNames[0x02]  = 'Jc'
InstructionNames[0x03]  = 'Jump'
InstructionNames[0x04]  = 'Switch'
InstructionNames[0x05]  = 'Call'
InstructionNames[0x06]  = 'NewScene'
InstructionNames[0x07]  = 'OP_07'
InstructionNames[0x08]  = 'Sleep'
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
InstructionNames[0x59]  = 'CloseMessageWindow'
InstructionNames[0x5A]  = 'OP_5A'
InstructionNames[0x5B]  = 'OP_5B'
InstructionNames[0x5C]  = 'ChrTalk'
InstructionNames[0x5D]  = 'NpcTalk'
InstructionNames[0x5E]  = 'Menu'
InstructionNames[0x5F]  = 'MenuEnd'
InstructionNames[0x60]  = 'OP_60'
InstructionNames[0x61]  = 'SetChrName'
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
InstructionNames[0xCA]  = 'CreatePortrait'
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

SCPSTR_CODE_STRING      = -1
SCPSTR_CODE_ITEM        = 0x1F
SCPSTR_CODE_LINE_FEED   = 0x01
SCPSTR_CODE_ENTER       = 0x02
SCPSTR_CODE_CLEAR       = 0x03
SCPSTR_CODE_07          = 0x07

class ScpString:
    def __init__(self, CtrlCode, Value = None):
        self.CtrlCode   = CtrlCode
        self.Value      = Value

    def binary(self):
        pass

    def __str__(self):
        if self.CtrlCode == SCPSTR_CODE_STRING:
            return '"%s"' % self.Value

        if self.Value == None:
            return 'scpstr(0x%X)' % (self.CtrlCode)

        return 'scpstr(0x%X, 0x%X)' % (self.CtrlCode, self.Value)

def BuildStringListFromObjectList(strlist):
    s = []
    laststrindex = None
    for x in strlist:
        if  x.CtrlCode == SCPSTR_CODE_LINE_FEED or \
            x.CtrlCode == SCPSTR_CODE_ENTER     or \
            x.CtrlCode == SCPSTR_CODE_CLEAR     or \
            x.CtrlCode == SCPSTR_CODE_07:

            if len(s) != laststrindex:

                s.append(str(x))

            else:

                if x.CtrlCode == SCPSTR_CODE_07:
                    tmp = '\\x%02X\\x%02X' % (x.CtrlCode, x.Value)
                else:
                    tmp = '\\x%02X' % x.CtrlCode
                s[-1] = '"%s%s"' % (s[-1][1:-1], tmp)

        elif x.CtrlCode == SCPSTR_CODE_STRING:

            s.append(str(x))
            laststrindex = len(s)

        else:

            s.append(str(x))

    return s

def FormatFuncString(data, oprfmt):

    entry = data.TableEntry
    ins = data.Instruction

    txt = [ '', '%s(' % entry.OpName ]

    for i in range(len(oprfmt)):
        opr = oprfmt[i].lower()
        if opr != 's':
            txt.append('    0x%X,' % ins.Operand[i])
        else:
            strlist = BuildStringListFromObjectList(ins.Operand[i])

            if len(strlist) == 1:
                s = '    %s' % strlist[0]

                if i != len(oprfmt):
                    s += ','

                txt.append(s)
                continue

            txt.append('    (')
            for s in strlist:
                txt.append('        %s,' % s)
            txt.append('    )')

    txt.append(')')
    txt.append('')

    return '\r\n'.join(txt)

class EDAOInstructionTableEntry(InstructionTableEntry):
    def __init__(self, op, name = '', operand = NO_OPERAND, flags = 0, handler = None):
        super().__init__(op, name, operand, flags, handler)

    def FormatOperand(self, opr, value, flags):
        def formatstr(strlist):
            s = BuildStringListFromObjectList(strlist)

            if not flags.ArgNewLine:
                if len(s) == 1:
                    return s[0]

                return '(' + ', '.join(s) + ')'

            tmp = []
            tmp.append('(')
            for arg in s:
                tmp.append('    %s,' % arg)
            tmp.append(')')

            return tmp

        oprtype = \
        {
            'e' : lambda : FormatExpressionList(value),
            'E' : lambda : FormatExpressionList(value),

            's' : lambda : formatstr(value),
            'S' : lambda : formatstr(value),
        }

        return oprtype[opr]() if opr in oprtype else super().FormatOperand(opr, value, flags)

    def GetOperand(self, opr, fs):
        if opr.lower() != 's':
            return super().GetOperand(opr, fs)

        def readstr():
            string = []
            tmpstr = ''

            while True:
                buf = fs.read(1)

                if buf < b' ':
                    if tmpstr != '':
                        string.append(ScpString(SCPSTR_CODE_STRING, tmpstr))
                        tmpstr = ''

                    code = struct.unpack('<B', buf)[0]

                    if code == 0:
                        break

                    strobj = ScpString(code)

                    if code == SCPSTR_CODE_07:

                        # dummy byte ?
                        strobj.Value = fs.byte()

                    elif code == SCPSTR_CODE_LINE_FEED or code == 0x0A:

                        # line feed
                        pass

                    elif code == SCPSTR_CODE_ENTER:

                        # need press enter
                        pass

                    elif code == SCPSTR_CODE_CLEAR or code == 0x04:

                        # unknown
                        pass

                    elif code == 0x06:

                        # unknown
                        pass

                    elif code == SCPSTR_CODE_ITEM:

                        # item id
                        strobj.Value = fs.ushort()

                    string.append(strobj)

                    continue

                elif buf >= b'\x80':

                    buf += fs.read(1)

                tmpstr += buf.decode(self.Container.CodePage)

            return string

        return readstr()

    def GetOperandSize(self, opr, fs):
        if opr.lower() != 's':
            return super().GetOperandSize(opr, fs)

        pos = fs.tell()
        self.GetOperand(opr, fs)
        oprsize = fs.tell() - pos
        fs.seek(pos)
        return oprsize

def inst(op, operand = NO_OPERAND, flags = 0, handler = None):
    return EDAOInstructionTableEntry(op, InstructionNames[op], operand, flags, handler)

def instopr(opr, size):
    return InstructionOperand(opr, size)

ExpressionOperantions = {}

ExpressionOperantions[0x00] = 'EXPR_PUSH_LONG'
ExpressionOperantions[0x01] = 'EXPR_END'
ExpressionOperantions[0x02] = 'EXPR_EQU'
ExpressionOperantions[0x03] = 'EXPR_NEQ'
ExpressionOperantions[0x04] = 'EXPR_LSS'
ExpressionOperantions[0x05] = 'EXPR_GTR'
ExpressionOperantions[0x06] = 'EXPR_LEQ'
ExpressionOperantions[0x07] = 'EXPR_GE'
ExpressionOperantions[0x08] = 'EXPR_EQUZ'
ExpressionOperantions[0x09] = 'EXPR_NEQUZ_I64'
ExpressionOperantions[0x0A] = 'EXPR_AND'
ExpressionOperantions[0x0B] = 'EXPR_OR'
ExpressionOperantions[0x0C] = 'EXPR_ADD'
ExpressionOperantions[0x0D] = 'EXPR_SUB'
ExpressionOperantions[0x0E] = 'EXPR_NEG'
ExpressionOperantions[0x0F] = 'EXPR_XOR'
ExpressionOperantions[0x10] = 'EXPR_IMUL'
ExpressionOperantions[0x11] = 'EXPR_IDIV'
ExpressionOperantions[0x12] = 'EXPR_IMOD'
ExpressionOperantions[0x13] = 'EXPR_STUB'
ExpressionOperantions[0x14] = 'EXPR_IMUL_SAVE'
ExpressionOperantions[0x15] = 'EXPR_IDIV_SAVE'
ExpressionOperantions[0x16] = 'EXPR_IMOD_SAVE'
ExpressionOperantions[0x17] = 'EXPR_ADD_SAVE'
ExpressionOperantions[0x18] = 'EXPR_SUB_SAVE'
ExpressionOperantions[0x19] = 'EXPR_AND_SAVE'
ExpressionOperantions[0x1A] = 'EXPR_XOR_SAVE'
ExpressionOperantions[0x1B] = 'EXPR_OR_SAVE'
ExpressionOperantions[0x1C] = 'EXPR_EXEC_OP'
ExpressionOperantions[0x1D] = 'EXPR_NOT'
ExpressionOperantions[0x1E] = 'EXPR_1E'
ExpressionOperantions[0x1F] = 'EXPR_GET_RESULT'
ExpressionOperantions[0x20] = 'EXPR_PUSH_VALUE_INDEX'
ExpressionOperantions[0x21] = 'EXPR_GET_CHR_WORK'
ExpressionOperantions[0x22] = 'EXPR_RAND'
ExpressionOperantions[0x23] = 'EXPR_23'

for opr, expr in ExpressionOperantions.items():
    exec('%s = 0x%X' % (expr, opr))

class ScpExpression:
    def __init__(self, operation = None, operand = None):
        self.Operation = operation
        self.Operand = operand if operand != None else []

    def binary(self):
        return b''

    def __str__(self):
        if self.Operation != EXPR_EXEC_OP:
            txt = 'scpexpr(%s' % ExpressionOperantions[self.Operation]
            for opr in self.Operand:
                txt += ', 0x%X' % opr

            txt += ')'
            return txt

        import Assembler

        asm = Assembler.Disassembler(edao_op_table)

        txt = 'scpexpr(%s' % ExpressionOperantions[self.Operation]
        for inst in self.Operand:
            data = HandlerData(HANDLER_REASON_FORMAT)
            data.Instruction    = inst
            data.TableEntry     = edao_op_table[inst.OpCode]
            txt += ', %s' % asm.FormatInstruction(data)

        txt += ')'
        return txt

def FormatExpressionList(exprlist):
    exprtxt = '%s' % exprlist[0]
    for expr in exprlist[1:]:
        exprtxt += ', %s' % expr

    return '(%s)' % exprtxt

def ParseScpExpression(data):
    expr = []
    fs = data.FileStream

    # stack size == 0xB0 ?

    while True:
        operation = fs.byte()

        scpexpr = ScpExpression(operation)

        if operation == EXPR_PUSH_LONG:

            scpexpr.Operand.append(fs.ulong())

        elif operation == EXPR_END:

            break

        elif operation == EXPR_EQU            or \
             operation == EXPR_NEQ            or \
             operation == EXPR_LSS            or \
             operation == EXPR_GTR            or \
             operation == EXPR_LEQ            or \
             operation == EXPR_GE             or \
             operation == EXPR_EQUZ           or \
             operation == EXPR_NEQUZ_I64      or \
             operation == EXPR_AND            or \
             operation == EXPR_OR             or \
             operation == EXPR_ADD            or \
             operation == EXPR_SUB            or \
             operation == EXPR_NEG            or \
             operation == EXPR_XOR            or \
             operation == EXPR_IMUL           or \
             operation == EXPR_IDIV           or \
             operation == EXPR_IMOD           or \
             operation == EXPR_STUB           or \
             operation == EXPR_IMUL_SAVE      or \
             operation == EXPR_IDIV_SAVE      or \
             operation == EXPR_IMOD_SAVE      or \
             operation == EXPR_ADD_SAVE       or \
             operation == EXPR_SUB_SAVE       or \
             operation == EXPR_AND_SAVE       or \
             operation == EXPR_XOR_SAVE       or \
             operation == EXPR_OR_SAVE        or \
             operation == EXPR_NOT:

            # pop all operand, and push result
            pass

        elif operation == EXPR_EXEC_OP:

            # execute one op code

            execdata = data.CreateBranch()
            execdata.Instruction.OpCode = data.TableEntry.Container.GetOpCode(fs)
            execdata.TableEntry = data.TableEntry.Container[execdata.Instruction.OpCode]
            execinst = execdata.Disasm(execdata)
            scpexpr.Operand.append(execinst)

        elif operation == EXPR_1E or \
             operation == EXPR_GET_RESULT:

            scpexpr.Operand.append(fs.ushort())

        elif operation == EXPR_PUSH_VALUE_INDEX:

            scpexpr.Operand.append(fs.byte())

        elif operation == EXPR_GET_CHR_WORK:

            scpexpr.Operand.append(fs.ushort())
            scpexpr.Operand.append(fs.byte())

        elif operation == EXPR_RAND:

            pass

        elif operation == EXPR_23:

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

        ins.OperandFormat = 'EO'

        return ins

    elif data.Reason == HANDLER_REASON_FORMAT:
        # Jc(expression, 'label')
        #entry = data.TableEntry
        #ins = data.Instruction
        #return '%s(%s, "%s")' % (entry.OpName, FormatExpressionList(ins.Operand[0]), entry.Container.GetLabelName(ins.Operand[1]))
        pass

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

    elif data.Reason == HANDLER_REASON_FORMAT:
        #   switch(
        #       Expression,
        #       (CaseID, CaseLabel),
        #       (CaseID, CaseLabel),
        #       (CaseID, CaseLabel),
        #       (-1,    DefaultLabel)
        #   )

        ins = data.Instruction
        entry = data.TableEntry

        txt = []
        txt.append('%s(' % entry.OpName)
        txt.append('    %s,' % FormatExpressionList(ins.Operand[0]))

        GetLabelName = entry.Container.GetLabelName

        for case in ins.Operand[1]:
            txt.append('    (%d, "%s"),' % (case[0], GetLabelName(case[1])))

        txt.append('    (-1, "%s"),' % GetLabelName(ins.Operand[-1]))
        txt.append(')')
        txt.append('')

        return '\r\n'.join(txt)

'''

typedef struct
{
    
}

'''

def scp_battle(data):

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        ins = data.Instruction

        BattleInfoOffset = fs.ulong()
        opr2 = fs.ulong()

        ins.Operand.append(BattleInfoOffset)
        ins.Operand.append(opr2)

        if BattleInfoOffset != 0xFFFFFFFF:
            # size = 0x18 + 0x2C
            # sizeof(BattleInfo + [0x28]) =  0x10
            # sizeof(BattleInfo + [0x20]) =  0x20

            ins.Operand.append(fs.byte())
            ins.Operand.append(fs.ushort())
            ins.Operand.append(fs.ushort())
            ins.Operand.append(fs.ushort())

            ins.BranchTargets.append(BattleInfoOffset)

            ins.OperandFormat = 'OLBWWW'

            return ins

        name = data.TableEntry.GetOperand('s', fs)
        ins.Operand.append(name)

        for i in range(4):
            ins.Operand.append(fs.ulong())

        for i in range(8):
            ins.Operand.append(fs.ulong())

        ins.Operand.append(fs.ushort())
        ins.Operand.append(fs.ushort())

        ins.OperandFormat = 'LL' + ('L' * 4) + ('L' * 8) + 'LL'

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

        ins.OperandFormat = 'BB' + operand

        return ins

def scp_play_bgm(data):

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        ins = data.Instruction

        bgm, volume = data.TableEntry.GetAllOperand('HC', fs)
        ins.Operand.append([ScpString(SCPSTR_CODE_STRING, 'ed7%d' % bgm)])
        ins.Operand.append(volume)

        ins.OperandFormat = 'SC'

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

        ins.OperandFormat = 'WB' + operand

        return ins

def scp_2a(data):

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        ins = data.Instruction

        opr1, opr2 = data.TableEntry.GetAllOperand('WB', fs)

        ins.Operand.append(opr1)
        ins.Operand.append(opr2)

        operand = 'W' if opr2 == 1 else 'B'

        ins.Operand += data.TableEntry.GetAllOperand(operand, fs)

        ins.OperandFormat = 'WB' + operand

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

        ins.OperandFormat = 'W' * len(ins.Operand)

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

        ins.OperandFormat = 'BB' + operand

        return ins

def scp_4e(data):

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        ins = data.Instruction
        ins.Operand = data.TableEntry.GetAllOperand('W', fs)
        ins.Operand.append(ParseScpExpression(data))

        ins.OperandFormat = 'WE'

        return ins

def scp_50(data):

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        ins = data.Instruction
        ins.Operand.append(fs.byte())
        ins.Operand.append(ParseScpExpression(data))

        ins.OperandFormat = 'BE'

        return ins

def scp_52(data):

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        ins = data.Instruction

        ins.Operand = data.TableEntry.GetAllOperand('WB', fs)
        ins.Operand.append(ParseScpExpression(data))

        ins.OperandFormat = 'WBE'

        return ins

def scp_anonymous_talk(data):

    if data.Reason == HANDLER_REASON_READ:
        fs = data.FileStream
        ins = data.Instruction

        target, text = data.TableEntry.GetAllOperand('WS', fs)

        ins.Operand.append(target)
        ins.Operand.append(text)

        ins.OperandFormat = 'WS'

        return ins

    elif data.Reason == HANDLER_REASON_FORMAT:

        return FormatFuncString(data, data.Instruction.OperandFormat)

def scp_create_chr_talk(data):

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        ins = data.Instruction
        ins.Operand = data.TableEntry.GetAllOperand('WS', fs)

        ins.OperandFormat = 'WS'

        return ins

    elif data.Reason == HANDLER_REASON_FORMAT:

        return FormatFuncString(data, data.Instruction.OperandFormat)

def scp_create_npc_talk(data):

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        ins = data.Instruction

        target, name, text = data.TableEntry.GetAllOperand('WSS', fs)

        ins.Operand.append(target)
        ins.Operand.append(name)
        ins.Operand.append(text)

        ins.OperandFormat = 'WSS'

        return ins

    elif data.Reason == HANDLER_REASON_FORMAT:

        return FormatFuncString(data, data.Instruction.OperandFormat)

def scp_create_menu(data):

    # max 10 line ?

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        ins = data.Instruction

        ins.Operand = data.TableEntry.GetAllOperand('WWWB', fs)
        menuitems = data.TableEntry.GetOperand('S', fs)
        ins.Operand.append(menuitems)

        ins.OperandFormat = 'WWWBS'

        return ins

    elif data.Reason == HANDLER_REASON_FORMAT:

        return FormatFuncString(data, data.Instruction.OperandFormat)

def scp_76(data):

    def getopr(opr3):
        operand = ''
        if opr3 == 0 or \
           opr3 == 1 or \
           opr3 == 3:

            operand = 'L'

        elif opr3 == 2:

            operand = 'S'

        return operand

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        ins = data.Instruction

        ins.Operand = data.TableEntry.GetAllOperand('BSB', fs)

        opr3 = ins.Operand[2]

        operand = getopr(opr3)
        ins.Operand += data.TableEntry.GetAllOperand(operand, fs)

        ins.OperandFormat = 'BSB' + operand

        return ins

def scp_9f(data):

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        ins = data.Instruction

        ins.Operand = data.TableEntry.GetAllOperand('B', fs)

        opr = ins.Operand[0]

        if opr == 0:
            operand = 'W'
        elif opr == 1:
            operand = 'LLL'
        else:
            operand = 'WLB'

        ins.Operand += data.TableEntry.GetAllOperand(operand, fs)

        ins.OperandFormat = 'B' + operand

        return ins

def scp_a1(data):

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        ins = data.Instruction

        ins.Operand = data.TableEntry.GetAllOperand('WWB', fs)

        operand = 'B' * ins.Operand[-1]
        ins.Operand += data.TableEntry.GetAllOperand(operand, fs)

        ins.OperandFormat = 'WWB' + operand

        return ins

def scp_cf(data):

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        ins = data.Instruction

        operand = 'BB'
        ins.Operand = data.TableEntry.GetAllOperand(operand, fs)

        if ins.Operand[0] != 0:
            ins.Operand += data.TableEntry.GetAllOperand('B', fs)
            operand += 'B'

        ins.OperandFormat = operand

        return ins

def scp_menu_cmd(data):

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream

        ins = Instruction()
        ins = data.Instruction

        menutype, menu_xxx = data.TableEntry.GetAllOperand('BB', fs)

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

        ins.OperandFormat = 'BB' + operand

        return ins

def scp_d2(data):

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        ins = data.Instruction
        ins.Operand.append(fs.byte())
        ins.Operand.append(ParseScpExpression(data))

        ins.OperandFormat = 'BE'

        return ins

def scp_e4(data):

    if data.Reason == HANDLER_REASON_READ:

        fs = data.FileStream
        ins = data.Instruction

        opr = data.TableEntry.GetOperand('B', fs)
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

        ins.OperandFormat = 'B' + operand

        return ins

edao_op_list = \
[
    inst(OP_00),
    inst(Return,            NO_OPERAND,         INSTRUCTION_END_BLOCK),
    inst(Jc,                NO_OPERAND,         INSTRUCTION_START_BLOCK,        scp_if),
    inst(Jump,              'O',                INSTRUCTION_END_BLOCK),
    inst(Switch,            NO_OPERAND,         INSTRUCTION_START_BLOCK,        scp_switch),
    inst(Call,              'BB'),          # included_scp index, func index
    inst(NewScene,          'LBB'),
    inst(OP_07,             NO_OPERAND),
    inst(Sleep,             'H'),
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
    inst(PlayBgm,           'HC',               0,                              scp_play_bgm),
    inst(OP_1F),
    inst(VolumeBgm,         'BL'),
    inst(OP_21,             'L'),
    inst(OP_22),
    inst(Sound,             'HCCC'),
    inst(OP_24,             'W'),
    inst(OP_25,             'WB'),
    inst(SoundDistance,     'WLLLLLBL'),
    inst(SoundLoad,         'H'),
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
    inst(OP_4E,             'WE',               0,                              scp_4e),
    inst(OP_4F),
    inst(OP_50,             'BE',               0,                              scp_50),
    inst(OP_51),
    inst(OP_52,             'WBE',              0,                              scp_52),
    inst(OP_53,             'W'),
    inst(OP_54,             'W'),
    inst(AnonymousTalk,     NO_OPERAND,         0,                              scp_anonymous_talk),
    inst(OP_56),
    inst(OP_57,             'B'),
    inst(OP_58,             'WWWS'),
    inst(CloseMessageWindow),
    inst(OP_5A),
    inst(OP_5B,             'WWWW'),
    inst(ChrTalk,           NO_OPERAND,         0,                              scp_create_chr_talk),
    inst(NpcTalk,           NO_OPERAND,         0,                              scp_create_npc_talk),
    inst(Menu,              NO_OPERAND,         0,                              scp_create_menu),
    inst(MenuEnd,           'W'),
    inst(OP_60,             'W'),
    inst(SetChrName,        'S'),
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
    inst(OP_76,             NO_OPERAND,         0,                              scp_76),
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
    inst(PlayEffect,        'BBWWIIIHHHIIIWIIII'),
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
    inst(OP_A0,             'WHBB'),
    inst(OP_A1,             NO_OPERAND,             0,                          scp_a1),
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
    inst(CreatePortrait,    'CHHHHHHHHHHHHLBS'),
    inst(OP_CB,             'BBLLLL'),
    inst(OP_CC,             'BBB'),
    inst(PlaceName2,        'WWSBW'),
    inst(OP_CE,             'B'),
    inst(OP_CF,             NO_OPERAND,             0,                          scp_cf),
    inst(MenuCmd,           NO_OPERAND,             0,                          scp_menu_cmd),
    inst(OP_D1,             'W'),
    inst(OP_D2,             'BE',                   0,                          scp_d2),
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

for op in edao_op_list:
    edao_op_table[op.OpCode] = op
    op.Container = edao_op_table

#valid = 0
#for inst in edao_op_list:
#    if inst.OpName[:3] != 'OP_':
#        valid += 1
#print('known: %d' % valid)
#print('total: %d' % len(edao_op_list))
#input()