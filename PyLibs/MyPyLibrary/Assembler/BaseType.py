from ml import *

CODE_PAGE = '936'

def SetGlobalCodePage(cp):
    global CODE_PAGE
    CODE_PAGE = cp



INVALID_OFFSET = 0xFFFFABCD
INVALID_OFFSET2 = (~0xFFFF | 0xABCD)

INSTRUCTION_END_BLOCK       = 1 << 0
INSTRUCTION_START_BLOCK     = 1 << 1
INSTRUCTION_CALL            = (1 << 2) | INSTRUCTION_START_BLOCK
INSTRUCTION_JUMP            = (1 << 3) | INSTRUCTION_END_BLOCK
INSTRUCTION_SWITCH          = 0

INSTRUCTION_FORMAT_ARG_NEW_LINE         = 1 << 4
INSTRUCTION_FORMAT_EMPTY_LINE           = 1 << 5

class InstructionFlags:
    def __init__(self, flags):
        self.Flags      = flags
        self.EndBlock   = bool(flags & INSTRUCTION_END_BLOCK)
        self.StartBlock = bool(flags & INSTRUCTION_START_BLOCK)
        self.Call       = bool(flags & INSTRUCTION_CALL & ~INSTRUCTION_START_BLOCK)
        self.Jump       = bool(flags & INSTRUCTION_JUMP & ~INSTRUCTION_END_BLOCK)
        self.ArgNewLine = bool(flags & INSTRUCTION_FORMAT_ARG_NEW_LINE)

class InstructionOperand:
    def __init__(self, operand, size):
        self.Operand = operand
        self.Size = size



Global_StringTypeMap = {}
Global_TypeStringMap = {}

def LookupOperandType(TypeOrString):
    global Global_StringTypeMap, Global_TypeStringMap

    if type(TypeOrString) == str:

        if TypeOrString not in Global_StringTypeMap:
            return None

        Type    = Global_StringTypeMap[TypeOrString]
        String  = TypeOrString

    elif isinstance(TypeOrString, OperandTypeBase):

        if TypeOrString not in Global_TypeStringMap:
            return None

        String  = Global_TypeStringMap[TypeOrString]
        Type    = TypeOrString

    else:

        return None

    return Type, String

def RegisterOperandType(OperandType, TypeString, OverWrite = False):
    global Global_StringTypeMap, Global_TypeStringMap

    if not OverWrite:
        OprInfo = LookupOperandType(TypeString)
        if not OprInfo is None:
            ExistType, ExistString = OprInfo
            expinfo = []
            expinfo.append('opr type conflict:')
            expinfo.append('    New:   %s <--> \'%s\'' % (OperandType, TypeString))
            expinfo.append('    Exist: %s <--> \'%s\'' % OprInfo)
            raise Exception('\r\n'.join(expinfo))

    Global_StringTypeMap[TypeString]  = OperandType
    Global_TypeStringMap[OperandType]       = TypeString

def UnRegisterOperandType(TypeOrString):
    global Global_StringTypeMap, Global_TypeStringMap

    OprInfo = LookupOperandType(TypeOrString)
    if OprInfo is None:
        raise Exception('unknown opr type: %s' % TypeOrString)

    Type, String = OprInfo

    del Global_StringTypeMap[String]
    del Global_TypeStringMap[Type]



class OperandTypeParameter:
    def __init__(self, fs, length = None):

        if isinstance(fs, BytesStream):
            self.FileStream = fs
            self.Value = None
        else:
            self.FileStream = None
            self.Value = fs

        self.Length = length

class OperandTypeBase:
    def __init__(self, oprtyparam):
        self.param  = oprtyparam
        self.fs     = oprtyparam.FileStream
        self.Length = oprtyparam.Length
        self.Value  = oprtyparam.Value

        if not self.OperandSize is None and not self.fs is None:
            self.Value = struct.unpack(self.UnpackFormat, fs.read(self.OperandSize))[0]

        return self

    def GetSize(self):
        return self.OperandSize

    def GetValue(self):
        return self.Value

    def WriteValue(self):
        return self.fs.write(struct.pack(self.UnpackFormat, self.Value))

    def FormatValue(self, Format = None):
        if Format is None:
            Format = self.FormatFormat
        return Format % self.Value



class OperandTypeBytes(OperandTypeBase):
    UnpackFormat    = None
    FormatFormat    = '%s'
    OperandSize     = None

    def __init__(self, oprtyparam):
        r = super().__init__(oprtyparam)
        self.Value = self.fs.read(self.Length)
        return r

class OperandTypeString(OperandTypeBase):
    UnpackFormat    = None
    FormatFormat    = '%s'
    OperandSize     = None

    def __init__(self, oprtyparam, cp = CODE_PAGE):
        self.cp = cp
        r = super().__init__(oprtyparam)
        if not self.fs is None:
            self.Value = self.fs.astr(self.cp)
        return r

    def WriteValue(self):
        return self.fs.write(struct.pack(self.UnpackFormat, self.Value))

class OperandTypeUnicode(OperandTypeBase):
    UnpackFormat    = None
    FormatFormat    = '%s'
    OperandSize     = None

    def __init__(self, oprtyparam):
        r = super().__init__(oprtyparam)
        if not self.fs is None:
            self.Value = self.fs.wstr()
        return r

    def WriteValue(self):
        return self.fs.write(self.Value.encode('UTF-16LE'))


def GenerateRegisterOperandTypeStub(typename, unpack, format, oprsize):

    decl_oprtype_stub = \
    '''\
class %s(OperandTypeBase):
    UnpackFormat    = '<%s'
    FormatFormat    = '%s'
    OperandSize     = %d

    def __init__(self, oprtyparam):
        r = super().__init__(oprtyparam)

RegisterOperandType(%s, '%s')

'''

    typename = 'OperandType_%s' % typename
    stub = decl_oprtype_stub % (typename, unpack, format, oprsize, typename, unpack)
    print(stub)
    return stub

exec(GenerateRegisterOperandTypeStub('Signed_Byte_Dec',         'c',        '%d',           1))
exec(GenerateRegisterOperandTypeStub('Unsigned_Byte_Dec',       'C',        '%d',           1))
exec(GenerateRegisterOperandTypeStub('Unsigned_Byte_Hex',       'B',        '0x%X',         1))
exec(GenerateRegisterOperandTypeStub('Signed_Word_Dec',         'w',        '%d',           2))
exec(GenerateRegisterOperandTypeStub('Unsigned_Word_Dec',       'W',        '%d',           2))
exec(GenerateRegisterOperandTypeStub('Unsigned_Word_Hex',       'H',        '0x%X',         2))
exec(GenerateRegisterOperandTypeStub('Signed_DWord_Dec',        'i',        '%d',           4))
exec(GenerateRegisterOperandTypeStub('Unsigned_DWord_Dec',      'I',        '%d',           4))
exec(GenerateRegisterOperandTypeStub('Unsigned_DWord_Hex',      'L',        '0x%X',         4))
exec(GenerateRegisterOperandTypeStub('Signed_QWord_Dec',        'L64',      '%d',           8))
exec(GenerateRegisterOperandTypeStub('Unsigned_QWord_Dec',      'UL64',     '%d',           8))
exec(GenerateRegisterOperandTypeStub('Unsigned_QWord_Hex',      'Q',        '0x%X',         8))
exec(GenerateRegisterOperandTypeStub('Float',                   'f',        '%s',           4))
exec(GenerateRegisterOperandTypeStub('Double',                  'd',        '%s',           8))


RegisterOperandType(OperandTypeString,      'S')
RegisterOperandType(OperandTypeUnicode,     'U')

del GenerateRegisterOperandTypeStub


class LabelEntry:
    def __init__(self, label, offset):
        self.Label = label          # label name
        self.Offset = offset        # label offset in instruction

class Instruction:
    def __init__(self, op = None, operand = None, flags = 0):
        self.OpCode             = op
        self.Operand            = [] if operand is None else operand
        self.OperandFormat      = None
        self.Size               = 0
        self.Offset             = INVALID_OFFSET
        self.BranchTargets      = []
        self.Flags              = InstructionFlags(flags)
        self.RefCount           = 0

class CodeBlock:
    def __init__(self, Offset = INVALID_OFFSET):
        self.Offset         = Offset
        self.Instructions   = []
        self.Blocks         = []
        self.Name           = None

    def AddBlock(self, block):
        self.Blocks.append(block)

    def AddInstruction(self, instruction):
        self.Instructions.append(instruction)


def IsTupleOrList(val):
    return type(val) == tuple or type(val) == list

def strlen(string):
    n = 0
    for ch in string:
        if ch > '\x80':
            n += 1

    return n + len(string)

def ljust_cn(string, n):
    cncount = 0
    for ch in string:
        if ch > '\x80':
            cncount += 1

    return string.ljust(n - cncount)

def rjust_cn(string, n):
    cncount = 0
    for ch in string:
        if ch > '\x80':
            cncount += 1

    return string.rjust(n - cncount)

def AdjustParam(param, spacelist, sep = ', '):
    param = param.split(sep)
    for i in range(len(param) - 1):
        param[i] = ljust_cn(param[i] + sep, int(spacelist[i]))

    return ''.join(param)

def CombineMultiline(text):
    if len(text) == 1:
        return text[0]

    text2 = []
    for line in text:
        text2.append(line.strip())

    text2 = ' '.join(text2)
    return text2