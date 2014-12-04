import os, sys, struct, io

if sys.winver == '2.7':
    import pefile
    import debugger
    import immutils
    from immlib2 import *
    from libhook import *
    from wintypes2 import *
    from immhelper import *

    imm = Debugger2()

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
            return Register(self._reg + int(y))

        def __sub__(self, y):
            return Register(self._reg - int(y))

        def __mul__(self, y):
            return Register(self._reg * int(y))

        def __truediv__(self, y):
            return Register(self._reg / int(y))

        def buf(self, size):
            return imm.readMemory(self._reg, int(size))

        def astr(self):
            return gbk(imm.readString(self._reg))

        def utf8(self):
            return utf8(imm.readString(self._reg))

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

    def utf8(addr):
        addr = int(addr)
        return imm.readString(addr).decode('UTF8')

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

        def __delitem__(self, key):
            return super(CaseInsensitiveDict, self).__delitem__(key.lower())

    def PrintException(e = None):
        excinfo = FormatException(e)
        for line in excinfo:
            imm.log(line)

