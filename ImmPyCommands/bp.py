from immdbg import *

class Register:
    def __init__(self, reg):
        self._reg = int(reg)

    def reg(self):
        return self._reg

    def __int__(self):
        return self._reg

    def __float__(self):
        return float(self._reg)

    def __hex__(self):
        return '%X' % self._reg

    def __eq__(self, y):
        if type(y) == str:
            return self.astr() == gbk(y)
        elif type(y) == unicode:
            return self.wstr() == y

        return self._reg == y

    def __add__(self, y):
        return Register(self._reg + y)

    def __sub__(self, y):
        return Register(self._reg - y)

    def __mul__(self, y):
        return Register(self._reg * y)

    def __truediv__(self, y):
        return Register(self._reg / y)

    def buf(self, size):
        return imm.readMemory(self._reg, int(size))

    def astr(self):
        return gbk(imm.readString(self._reg))

    def wstr(self):
        return imm.readWString(self._reg).decode('U16')

    def u64(self):
        return Register(struct.unpack('<Q', self.buf(8))[0])

    def u32(self):
        return Register(struct.unpack('<I', self.buf(4))[0])

    def u16(self):
        return Register(struct.unpack('<H', self.buf(2))[0])

    def u8(self):
        return Register(struct.unpack('<B', self.buf(1))[0])

    def s64(self):
        return Register(struct.unpack('<q', self.buf(8))[0])

    def s32(self):
        return Register(struct.unpack('<i', self.buf(4))[0])

    def s16(self):
        return Register(struct.unpack('<h', self.buf(2))[0])

    def s8(self):
        return Register(struct.unpack('<b', self.buf(1))[0])

def buf(addr, size):
    return imm.readMemory(int(addr), int(size))

def astr(addr):
    addr = int(addr)
    return gbk(imm.readString(addr))

def wstr(addr):
    addr = int(addr)
    return imm.readWString(addr).decode('U16')

def u64(addr):
    return Register(addr).u64()

def u32(addr):
    return Register(addr).u32()

def u16(addr):
    return Register(addr).u16()

def u8(addr):
    return Register(addr).u8()

class CaseInsensitiveDict(dict):
    def __setitem__(self, key, value):
        super(CaseInsensitiveDict, self).__setitem__(key.lower(), value)

    def __getitem__(self, key):
        return super(CaseInsensitiveDict, self).__getitem__(key.lower())

class BpCondition(LogBpHook):
    def __init__(self, addr, args):
        LogBpHook.__init__(self)
        self.addr = addr

        if args[0][0] == '#':
            self.run        = self.run_pyfile
            self.modname    = args[0][1:]
            self.entry      = 'main' if len(args) == 1 else args[1]
            self.mod        = loadmod(self.modname)
        else:
            self.run = self.run_expression
            self.cond   = gbk(args[0])
            self.condvm = compile(self.cond, '', 'eval')

    def run_expression(self, regs):
        eax = Register(regs['EAX'])
        ecx = Register(regs['ECX'])
        edx = Register(regs['EDX'])
        ebx = Register(regs['EBX'])
        esp = Register(regs['ESP'])
        ebp = Register(regs['EBP'])
        esi = Register(regs['ESI'])
        edi = Register(regs['EDI'])
        eip = Register(regs['EIP'])

        try:
            imm.clearState()
            result = eval(self.condvm)
        except Exception as e:
            result = False
            PrintException()

        imm.log('%s: %s' % (self.cond, result))

        if result != True:
            return

        #imm.log('%08X, %08X' % (self.addr, eip.reg()))
        imm.setTemporaryBreakpoint(self.addr)

    def run_pyfile(self, regs):
        try:
            #if not hasattr(self, 'mod'): self.mod = loadmod(self.modname)
            self.mod = reloadmod(self.mod)

            _regs = CaseInsensitiveDict()
            _regs['EAX'] = Register(regs['EAX'])
            _regs['ECX'] = Register(regs['ECX'])
            _regs['EDX'] = Register(regs['EDX'])
            _regs['EBX'] = Register(regs['EBX'])
            _regs['ESP'] = Register(regs['ESP'])
            _regs['EBP'] = Register(regs['EBP'])
            _regs['ESI'] = Register(regs['ESI'])
            _regs['EDI'] = Register(regs['EDI'])
            _regs['EIP'] = Register(regs['EIP'])

            entry = getattr(self.mod, self.entry)
            result = entry(_regs)
        except Exception as e:
            result = False
            #if hasattr(self, 'mod'): del self.mod
            PrintException()

        if result != True:
            return

        imm.setTemporaryBreakpoint(self.addr)

    def run_stub(self, regs):
        pass

import re

def ResolveAddress(expr):
    expr = gbk(expr)
    modulelist = re.findall(u'!\w+', expr, flags=re.DOTALL)
    if len(modulelist) == 0:
        return expr

    for module in modulelist:
        mod = imm.QueryModuleByName(module[1:])
        if mod == None:
            continue

        expr = expr.replace(module, u'%08X' % mod.getBaseAddress())

    return mbcs(expr)

def main(args):
    #debugger.pyresetall()

    if len(args) == 0:
        return 'usage: bp addr "py expr"'

    addr = imm.getAddress(ResolveAddress(args[0]))

    if addr == -3:
        return 'invalid address: %s' % args[0]
    elif addr == -1:
        return 'invalid symbol name: %s' % args[0]

    if len(args) == 1:
        imm.setBreakpoint(addr)
        return ''

    bpc = BpCondition(addr, args[1:])
    imm.log('addr = %08X, cond = %s' % (addr, args[1]))
    bpc.add2('condition bp at %08X' % addr, addr, replace = True)

    return ''
