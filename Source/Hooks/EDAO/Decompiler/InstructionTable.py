from BaseType import *

HANDLER_REASON_READ     = 0
HANDLER_REASON_WRITE    = 1
HANDLER_REASON_FORMAT   = 1

class HandlerData:
    def __init__(self, reason, data = None):
        self.Reason = reason

        if type(data) == BytesStream:
            self.FileStream = data
        elif type(data) == Instruction:
            self.Instruction = data

        # list of OffsetFixupEntry
        self.Labels = []

        self.TableEntry = None

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



NO_OPERAND = ''

class InstructionTableEntry:
    def __init__(self, op, name = '', operand = NO_OPERAND, flags = 0, handler = None):
        self.OpCode     = op
        self.OpName     = name
        self.Operand    = operand
        self.Flags      = InstructionFlags(flags)
        self.Handler    = handler

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

            return string

        oprtype = \
        {
            'b' : lambda : struct.unpack('<b', fs.read(1))[0],
            'B' : lambda : struct.unpack('<B', fs.read(1))[0],

            'w' : lambda : struct.unpack('<h', fs.read(2))[0],
            'W' : lambda : struct.unpack('<H', fs.read(2))[0],

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
            'b' : lambda : 1,
            'B' : lambda : 1,

            'w' : lambda : 2,
            'W' : lambda : 2,

            'l' : lambda : 4,
            'L' : lambda : 4,

            'q' : lambda : 8,
            'Q' : lambda : 8,

            'f' : lambda : 4,
            'F' : lambda : 4,

            'd' : lambda : 8,
            'D' : lambda : 8,

            's' : lambda : len(self.GetOperand(opr, fs)),
            'S' : lambda : len(self.GetOperand(opr, fs)),

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
