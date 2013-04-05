from immdbg import *

class Register:
    def __init__(self, reg):
        self._reg = reg

    def reg(self):
        return self._reg

    def __int__(self):
        return self._reg

    def __eq__(self, y):
        return y == self._reg

    def astr(self):
        return imm.readString(self._reg)

    def wstr(self):
        return imm.readWString(self._reg)

    def u64(self):
        _u64 = imm.readMemory(self._reg, 8)
        if len(_u64) == 8:
            try:
                return immutils.str2int64_swapped(_u64) 
            except ValueError:
                raise Exception, "failed to gather a _u64 at 0x%08x" % self._reg
        else:
            raise Exception, "failed to gather a _u64 at 0x%08x" % self._reg

    def u32(self):
        return imm.readLong(self._reg)

    def u16(self):
        return imm.readShort(self._reg)

    def u8(self):
        byte = imm.readMemory(self._reg, 1)
        return ord(byte)


def astr(addr):
    addr = int(addr)
    return Register(imm.readString(addr))

def wstr(addr):
    addr = int(addr)
    return Register(imm.readWString(addr))

def u64(addr):
    addr = int(addr)
    _u64 = imm.readMemory(addr, 8)
    if len(_u64) == 8:
        try:
            return Register(immutils.str2int64_swapped(_u64))
        except ValueError:
            raise Exception, "failed to gather a u64 at 0x%08x" % addr
    else:
        raise Exception, "failed to gather a u64 at 0x%08x" % addr

def u32(addr):
    addr = int(addr)
    return Register(imm.readLong(addr))

def u16(addr):
    addr = int(addr)
    return Register(imm.readShort(addr))

def u8(addr):
    addr = int(addr)
    byte = imm.readMemory(addr, 1)
    return Register(ord(byte))

class BpCondition(LogBpHook):
    def __init__(self, addr, cond):
        LogBpHook.__init__(self)
        self.cond   = cond
        self.condvm = compile(cond, '', 'eval')
        self.addr   = addr

    def run(self, regs):
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
            result = eval(self.condvm)
        except:
            result = False

        imm.log('%s: result = %s' % (self.cond, result))
        imm.log('%X' % eax.u32())

        if result == False:
            return

        imm.log('%08X, %08X' % (self.addr, eip.reg()))
        imm.setTemporaryBreakpoint(self.addr)

def main(args):
    #debugger.pyresetall()

    if len(args) == 0:
        return 'usage: bp addr "py exp"'

    addr = imm.getAddress(args[0])
    if addr == -3:
        return 'invalid address: %s' % args[0]
    elif addr == -1:
        return 'invalid symbol name: %s' % args[0]

    if len(args) == 1:
        imm.setBreakpoint(addr)
        return ''

    bpc = BpCondition(addr, args[1])
    imm.log('addr = %08X, cond = %s' % (addr, args[1]))
    bpc.add2('condition bp at %08X' % addr, addr)

    return ''
