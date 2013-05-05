from BaseType import *

HANDLER_REASON_READ         = 0
HANDLER_REASON_WRITE        = 1
HANDLER_REASON_FORMAT       = 2
HANDLER_REASON_FUNCTION     = 3
HANDLER_REASON_GENERATE     = 4

class HandlerData:
    def __init__(self, reason):
        self.Reason         = reason
        self.FileStream     = None
        self.Instruction    = None
        self.Arguments      = None

        # list of LabelEntry
        self.Labels = []

        self.TableEntry = None

        self.Disasm     = None
        self.Format     = None
        self.Assemble   = None

    def CreateBranch(self):
        data = HandlerData(self.Reason)

        data.Reason             = self.Reason
        data.FileStream         = self.FileStream
        data.Instruction        = Instruction()
        data.Labels             = []
        data.TableEntry         = None
        data.Disasm             = self.Disasm

        return data

#
#   def inst_handler(data):
#
#       if data.Reason == HANDLER_REASON_READ:
#
#           data.fs = BytesStream
#           return Instruction object
#
#       elif data.Reason == HANDLER_REASON_WRITE:
#
#           data.inst = Instruction object
#           data.inst.labels.append(LabelEntry('label name', label_offset_in_bytes))
#           return Instruction object
#
#       elif data.Reason == HANDLER_REASON_FORMAT:
#
#           return 'formatted instruction'
#
#       return None
#

def DefaultGetLabelName(offset):
    return 'loc_%X' % offset

class InstructionTable(dict):
    def __init__(self, GetOpCode, WriteOpCode, GetLabelName = DefaultGetLabelName, CodePage = '936'):
        self.GetOpCode      = GetOpCode
        self.WriteOpCode    = WriteOpCode
        self.GetLabelName   = GetLabelName
        self.CodePage       = CodePage

NO_OPERAND = ''

class InstructionTableEntry:
    def __init__(self, op, name = '', operand = NO_OPERAND, flags = 0, handler = None):
        self.OpCode     = op
        self.OpName     = name
        self.Operand    = operand
        self.Flags      = InstructionFlags(flags)
        self.Handler    = handler
        self.Container  = None

    def WriteOperand(self, data, opr, value):

        fs = data.FileStream
        labels = data.Instruction.Labels

        def wlabel():
            labels.append(LabelEntry(value, fs.tell()))
            fs.wulong(INVALID_OFFSET)

        oprtype = \
        {
            'c' : lambda : fs.wchar(value),
            'C' : lambda : fs.wbyte(value),

            'b' : lambda : fs.wchar(value),
            'B' : lambda : fs.wbyte(value),

            'w' : lambda : fs.wshort(value),
            'W' : lambda : fs.wushort(value),

            'h' : lambda : fs.wshort(value),
            'H' : lambda : fs.wushort(value),

            'l' : lambda : fs.wlong(value),
            'L' : lambda : fs.wulong(value),

            'i' : lambda : fs.wlong(value),
            'I' : lambda : fs.wulong(value),

            'q' : lambda : fs.wlong64(value),
            'Q' : lambda : fs.wulong64(value),

            'f' : lambda : fs.wfloat(value),
            'F' : lambda : fs.wdouble(value),

            'd' : lambda : fs.wfloat(value),
            'D' : lambda : fs.wdouble(value),

            's' : lambda : fs.write(value.encode(data.TableEntry.Container.CodePage)),
            'S' : lambda : fs.write(value.encode(data.TableEntry.Container.CodePage)),

            'o' : wlabel,
            'O' : wlabel,
        }

        return oprtype[opr]()

    def FormatAllOperand(self, oprs, values, flags):
        if len(oprs) != len(values):
            raise Exception('operand: does not match values')

        if len(oprs) == 0:
            return ''

        oprtext = self.FormatOperand(oprs[0], values[0], flags)

        if not flags.ArgNewLine:
            for i in range(1, len(oprs)):
                tmp = ', ' + self.FormatOperand(oprs[i], values[i], flags)
                oprtext += tmp
        else:
            raise Exception('not implemented')

        return oprtext

    def FormatOperand(self, opr, value, flags):
        oprtype = \
        {
            'c' : lambda : '%d' % value,
            'C' : lambda : '%d' % value,

            'b' : lambda : '0x%X' % value,
            'B' : lambda : '0x%X' % value,

            'w' : lambda : '0x%X' % value,
            'W' : lambda : '0x%X' % value,

            'h' : lambda : '%d' % value,
            'H' : lambda : '%d' % value,

            'l' : lambda : '0x%X' % value,
            'L' : lambda : '0x%X' % value,

            'i' : lambda : '%d' % value,
            'I' : lambda : '%d' % value,

            'q' : lambda : '0x%X' % value,
            'Q' : lambda : '0x%X' % value,

            'f' : lambda : '%f' % value,
            'F' : lambda : '%f' % value,

            'd' : lambda : '%f' % value,
            'D' : lambda : '%f' % value,

            's' : lambda : '"%s"' % value,
            'S' : lambda : '"%s"' % value,

            'o' : lambda : '"%s"' % DefaultGetLabelName(value),
            'O' : lambda : '"%s"' % DefaultGetLabelName(value),
        }

        opr = oprtype[opr]
        return opr()

    def GetAllOperand(self, oprs, fs):
        operand = []
        for opr in oprs:
            operand.append(self.GetOperand(opr, fs))

        return operand

    def GetOperand(self, opr, fs):
        def readstr():
            string = b''
            while True:
                buf = fs.read(1)
                if buf == b'' or buf == b'\x00':
                    break

                string += buf

            return string.decode(self.Container.CodePage)

        oprtype = \
        {
            'c' : lambda : struct.unpack('<b', fs.read(1))[0],
            'C' : lambda : struct.unpack('<B', fs.read(1))[0],
            'b' : lambda : struct.unpack('<b', fs.read(1))[0],
            'B' : lambda : struct.unpack('<B', fs.read(1))[0],

            'h' : lambda : struct.unpack('<h', fs.read(2))[0],
            'H' : lambda : struct.unpack('<H', fs.read(2))[0],
            'w' : lambda : struct.unpack('<h', fs.read(2))[0],
            'W' : lambda : struct.unpack('<H', fs.read(2))[0],

            'i' : lambda : struct.unpack('<l', fs.read(4))[0],
            'I' : lambda : struct.unpack('<L', fs.read(4))[0],
            'l' : lambda : struct.unpack('<l', fs.read(4))[0],
            'L' : lambda : struct.unpack('<L', fs.read(4))[0],

            'q' : lambda : struct.unpack('<q', fs.read(8))[0],
            'Q' : lambda : struct.unpack('<Q', fs.read(8))[0],

            'f' : lambda : struct.unpack('<f', fs.read(4))[0],
            'F' : lambda : struct.unpack('<f', fs.read(4))[0],

            'd' : lambda : struct.unpack('<d', fs.read(8))[0],
            'D' : lambda : struct.unpack('<d', fs.read(8))[0],

            's' : readstr,
            'S' : readstr,

            'o' : lambda : struct.unpack('<L', fs.read(4))[0],
            'O' : lambda : struct.unpack('<L', fs.read(4))[0],
        }

        opr = oprtype[opr]
        return opr()

    def GetOperandSize(self, opr, fs):
        oprsize = \
        {
            'c' : lambda : 1,
            'C' : lambda : 1,
            'b' : lambda : 1,
            'B' : lambda : 1,

            'h' : lambda : 2,
            'H' : lambda : 2,
            'w' : lambda : 2,
            'W' : lambda : 2,

            'i' : lambda : 4,
            'I' : lambda : 4,
            'l' : lambda : 4,
            'L' : lambda : 4,

            'q' : lambda : 8,
            'Q' : lambda : 8,

            'f' : lambda : 4,
            'F' : lambda : 4,

            'd' : lambda : 8,
            'D' : lambda : 8,

            's' : lambda : self.GetOperand(opr, fs),
            'S' : lambda : self.GetOperand(opr, fs),

            'o' : lambda : 4,   # offset
            'O' : lambda : 4,   # offset
        }

        pos = fs.tell()
        oprsize = oprsize[opr]()
        fs.seek(pos)
        return oprsize

    def __str__(self):
        s = []
        s.append('op        = %08X' % self.OpCode)
        s.append('name      = %s'   % self.OpName)
        s.append('operand   = %s' % (self.Operand if self.Operand != NO_OPERAND else 'NO_OPERAND'))
        s.append('flags     = %08X' % self.Flags.Flags)
        s.append('handler   = %s'   % self.Handler)

        return '\r\n'.join(s)
