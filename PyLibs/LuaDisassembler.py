from ml import *

class LuaString:
    def __init__(self, fs = None):
        if fs is None: return

        self.Length = fs.ulong()
        self.String = '' if self.Length == 0 else fs.read(self.Length)[:-1].decode('UTF8')

    def __str__(self):
        return self.String

class LuaHeader:
    def __init__(self, fs = None):
        if fs is None: return

        self.Signature              = fs.read(4)
        self.Version                = fs.byte()
        self.Official               = fs.byte()
        self.Endianness             = fs.byte()
        self.SizeOfInt              = fs.byte()
        self.SizeOfPtr              = fs.byte()
        self.SizeOfInstruction      = fs.byte()
        self.SizeOfDouble           = fs.byte()
        self.IsDoubleIntegral       = fs.byte()

    def ToStrings(self):
        lines = []

        lines.append('Header = LuaHeader()')
        lines.append('Header.Signature          = %s' % self.Signature)
        lines.append('Header.Version            = 0x%X' % self.Version)
        lines.append('Header.Official           = %s' % self.Official)
        lines.append('Header.Endianness         = %s' % self.Endianness)
        lines.append('Header.SizeOfInt          = %s' % self.SizeOfInt)
        lines.append('Header.SizeOfPtr          = %s' % self.SizeOfPtr)
        lines.append('Header.SizeOfInstruction  = %s' % self.SizeOfInstruction)
        lines.append('Header.SizeOfDouble       = %s' % self.SizeOfDouble)
        lines.append('Header.IsDoubleIntegral   = %s' % self.IsDoubleIntegral)
        lines.append('')

        return lines


class LuaInstruction:
    def __init__(self, fs = None):
        if fs is None: return

        if type(fs) == int:
            self.Value = fs
        else:
            self.Value = fs.ulong()

class LuaCode:
    def __init__(self, fs = None):
        if fs is None: return

        number = fs.ulong()
        self.Instruction = []
        for i in range(number):
            self.Instruction.append(LuaInstruction(fs))

LUA_TNIL        = 0
LUA_TBOOLEAN    = 1
LUA_TNUMBER     = 3
LUA_TSTRING     = 4

def LuaReadNil(fs):
    return None

def LuaReadBoolean(fs):
    return bool(fs.byte())

def LuaReadNumber(fs):
    return fs.double()

def LuaReadString(fs):
    return LuaString(fs).String

luatype = {}
luatype[LUA_TNIL]       = LuaReadNil
luatype[LUA_TBOOLEAN]   = LuaReadBoolean
luatype[LUA_TNUMBER]    = LuaReadNumber
luatype[LUA_TSTRING]    = LuaReadString

PyTypeToLuaType = {}
PyTypeToLuaType[None]   = LUA_TNIL
PyTypeToLuaType[bool]   = LUA_TBOOLEAN
PyTypeToLuaType[float]  = LUA_TNUMBER
PyTypeToLuaType[str]    = LUA_TSTRING


class LuaConstants:
    def __init__(self, fs = None):
        self.Value = []

        if fs is None: return

        number = fs.ulong()
        for i in range(number):
            type = fs.byte()
            self.Value.append(luatype[type](fs))


class LuaLocalVariable:
    def __init__(self, fs = None, StartPC = None, EndPC = None):
        if fs is None: return

        if type(fs) == str:
            self.VarName = fs
            self.StartPC = StartPC
            self.EndPC = EndPC
        else:
            self.VarName    = LuaString(fs)
            self.StartPC    = fs.ulong()
            self.EndPC      = fs.ulong()

    def __str__(self):
        return 'LuaLocalVariable("%s", %d, %d)' % (self.VarName, self.StartPC, self.EndPC)


class LuaDebug:
    def __init__(self, fs = None):
        if fs is None: return

        self.LineInfo       = []
        self.LocalVariable  = []
        self.UpValues       = []

        n = fs.ulong()
        for i in range(n):
            self.LineInfo.append(fs.ulong())

        n = fs.ulong()
        for i in range(n):
            self.LocalVariable.append(LuaLocalVariable(fs))

        n = fs.ulong()
        for i in range(n):
            self.UpValues.append(LuaString(fs))


class LuaFunction_51:
    def __init__(self, fs = None):

        self.Code       = LuaCode()
        self.Constants  = LuaConstants()
        self.Functions  = []
        self.Parent     = None

        if fs is None: return

        self.Name = 'Func_%X' % fs.tell()

        self.Source             = LuaString(fs)
        self.LineDefined        = fs.ulong()
        self.LastLineDefined    = fs.ulong()
        self.NumberOfUpvalues   = fs.byte()
        self.NumberOfParam      = fs.byte()
        self.IsVararg           = fs.byte()
        self.MaxStackSize       = fs.byte()
        self.Code               = LuaCode(fs)
        self.Constants          = LuaConstants(fs)

        self.NumberOfFunction   = fs.ulong()

        for i in range(self.NumberOfFunction):
            self.Functions.append(LuaFunction_51(fs))
            self.Functions[-1].Parent = self.Name

        self.Debug = LuaDebug(fs)

    def ToStrings(self):
        lines = []

        for f in self.Functions:
            lines += f.ToStrings()

        leftjust = 0

        lines.append('%s                    = LuaFunction_51()' % self.Name)
        lines.append('%s.Source             = r"%s"' % (self.Name, self.Source))
        lines.append('%s.LineDefined        = %s' % (self.Name, self.LineDefined))
        lines.append('%s.LastLineDefined    = %s' % (self.Name, self.LastLineDefined))
        lines.append('%s.NumberOfUpvalues   = %s' % (self.Name, self.NumberOfUpvalues))
        lines.append('%s.NumberOfParam      = %s' % (self.Name, self.NumberOfParam))
        lines.append('%s.IsVararg           = %s' % (self.Name, self.IsVararg))
        lines.append('%s.MaxStackSize       = %s' % (self.Name, self.MaxStackSize))

        lines.append('')

        if len(self.Code.Instruction) != 0:
            lines.append('%s.Code.Instruction = list((' % self.Name)
            for inst in self.Code.Instruction:
                lines.append('    LuaInstruction(0x%08X),' % inst.Value)
            lines.append('))')
            lines.append('')

        if len(self.Constants.Value) == 0:
            lines.append('%s.Constants = LuaConstants()' % self.Name)
        else:
            lines.append('%s.Constants.Value = list((' % self.Name)
            for v in self.Constants.Value:
                if type(v) == str:
                    v = '"%s"' % v.replace('\n', '\\n').replace('\r', '\\r')
                lines.append('    %s,' % v)
            lines.append('))')

        lines.append('')

        if len(self.Functions) != 0:
            for f in self.Functions:
                lines.append('%s.Functions.append(%s)' % (self.Name, f.Name))

            lines.append('')

        lines.append('%s.Debug = LuaDebug()' % self.Name)
        lines.append('%s.Debug.LineInfo = %s' % (self.Name, self.Debug.LineInfo))

        localvars = []
        for local in self.Debug.LocalVariable:
            localvars.append('%s' % local)

        lines.append('%s.Debug.LocalVariable = [%s]' % (self.Name, ', '.join(localvars)))

        lines.append('%s.Debug.UpValues = %s' % (self.Name, self.Debug.UpValues))

        lines.append('')

        return lines


class LuaDisassembler:
    def __init__(self):
        pass

    def LoadFunction_51(self, fs):
        self.Function = LuaFunction_51(fs)

    def LoadFunction_52(self, fs):
        raise Exception('not implemented')

    def open(self, file):
        fs = BytesStream().open(file)

        self.FileName = os.path.basename(file)

        self.Header = LuaHeader(fs)

        loadfunc = {}
        loadfunc[0x51] = self.LoadFunction_51
        loadfunc[0x52] = self.LoadFunction_52

        loadfunc[self.Header.Version](fs)

        return self

    def CompileTo(self, file):
        pass

    def ToStrings(self):
        lines = []

        lines += self.Header.ToStrings()
        lines += self.Function.ToStrings()

        lines.append('luac = LuaDisassembler()')
        lines.append('luac.Header = Header')
        lines.append('luac.Function = %s' % self.Function.Name)
        lines.append('luac.Function = %s' % self.Function.Name)
        lines.append('')
        lines.append('luac.CompileTo("%s")' % self.FileName)
        lines.append('')

        return lines

    def save(self, file):
        hdr = []

        hdr.append('from ml import *')
        hdr.append('from %s import *' % os.path.splitext(os.path.basename(__file__))[0])
        hdr.append('')
        hdr.append('def main():')

        lines = self.ToStrings()

        for i in range(len(lines)):
            lines[i] = '    ' + lines[i] if lines[i] != '' else lines[i]

        hdr += lines
        hdr.append('TryInvoke(main)')
        hdr.append('')

        open(file, 'wb').write('\r\n'.join(hdr).encode('UTF8'))

def main(file):
    print('disasm %s' % file)
    lua = LuaDisassembler().open(file).save(file + '.py')

if __name__ == '__main__':
    TryForEachFile(sys.argv[1:], main) #, 'menu-main-init.lb'
