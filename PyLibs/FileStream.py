from syslib import *
import io

def ReadByte(fs):
    return struct.unpack('<B', fs.read(1))[0]

def ReadShort(fs):
    return struct.unpack('<h', fs.read(2))[0]

def ReadUShort(fs):
    return struct.unpack('<H', fs.read(2))[0]

def ReadLong(fs):
    return struct.unpack('<l', fs.read(4))[0]

def ReadULong(fs):
    return struct.unpack('<L', fs.read(4))[0]

def ReadLong64(fs):
    return struct.unpack('<q', fs.read(8))[0]

def ReadULong64(fs):
    return struct.unpack('<Q', fs.read(8))[0]

def ReadFloat(fs):
    return struct.unpack('<f', fs.read(4))[0]

def ReadDouble(fs):
    return struct.unpack('<d', fs.read(8))[0]

def ReadAString(fs, cp = '936'):
    string = b''
    while True:
        buf = fs.read(1)
        if buf == b'' or buf == b'\x00':
            break

        string += buf

    return string.decode(cp)

def ReadWString(fs):
    string = b''
    while True:
        buf = fs.read(2)
        if buf == b'' or buf == b'\x00\x00':
            break

        string += buf

    return string.decode('U16')

def WriteByte(fs, b):
    return fs.write(struct.pack('<B', BYTE(b & 0xFF).value))

def WriteChar(fs, b):
    return fs.write(CHAR(b & 0xFF).value)

def WriteUShort(fs, ushort):
    return fs.write(struct.pack('<H', USHORT(ushort).value))

def WriteShort(fs, short):
    return fs.write(struct.pack('<h', SHORT(short).value))

def WriteULong(fs, ulong):
    return fs.write(struct.pack('<L', ULONG(ulong).value))

def WriteLong(fs, long):
    return fs.write(struct.pack('<l', LONG(long).value))

def WriteLong64(fs, l64):
    return fs.write(struct.pack('<q', LONG64(l64).value))

def WriteULong64(fs, ul64):
    return fs.write(struct.pack('<Q', ULONG64(ul64).value))

def WriteFloat(fs, flt):
    return fs.write(struct.pack('<f', FLOAT(flt).value))

def WriteDouble(fs, db):
    return fs.write(struct.pack('<d', DOUBLE(db).value))

class BytesStream:
    stream = None

    def open(
            self,
            file,
            mode        = 'rb',
            buffering   = -1,
            encoding    = None,
            errors      = None,
            newline     = None,
            closefd     = True,
            opener      = None
        ):
        self.stream = open(file, mode, buffering, encoding, errors, newline, closefd, opener)
        return self

    def openmem(self, buffer = b''):
        self.stream = io.BytesIO(buffer)
        return self

    def seek(self, offset, method = io.SEEK_SET):
        return self.stream.seek(offset, method)

    def forward(self, length):
        return self.stream.seek(length, io.SEEK_CUR)

    def read(self, n = -1):
        return self.stream.read(n)

    def write(self, buf):
        return self.stream.write(buf)

    def tell(self):
        return self.stream.tell()

    def size(self):
        pos = self.tell()
        self.seek(0, io.SEEK_END)
        stmsize = self.tell()
        self.seek(pos)
        return stmsize

    def byte(self):
        return ReadByte(self.stream)

    def short(self):
        return ReadShort(self.stream)

    def ushort(self):
        return ReadUShort(self.stream)

    def long(self):
        return ReadLong(self.stream)

    def ulong(self):
        return ReadULong(self.stream)

    def long64(self):
        return ReadLong64(self.stream)

    def ulong64(self):
        return ReadULong64(self.stream)

    def float(self):
        return ReadFloat(self.stream)

    def double(self):
        return ReadDouble(self.stream)

    def astr(self):
        return ReadAString(self.stream)

    def wstr(self):
        return ReadWString(self.stream)

    def wchar(self, b):
        return WriteChar(self.stream, b)

    def wbyte(self, b):
        return WriteByte(self.stream, b)

    def wshort(self, short):
        return WriteShort(self.stream, short)

    def wushort(self, ushort):
        return WriteUShort(self.stream, ushort)

    def wlong(self, l):
        return WriteLong(self.stream, l)

    def wulong(self, l):
        return WriteULong(self.stream, l)

    def wlong64(self, l64):
        return WriteLong64(self.stream, l)

    def wulong64(self, l64):
        return WriteULong64(self.stream, l)

    def wfloat(self, flt):
        return WriteFloat(self.stream, flt)

    def wdouble(self, db):
        return WriteDouble(self.stream, db)

