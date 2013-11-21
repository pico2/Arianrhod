from MyPyLibrary.syslib import *
import io

def ReadByte(fs, endian = '<'):
    return struct.unpack(endian + 'B', fs.read(1))[0]

def ReadShort(fs, endian = '<'):
    return struct.unpack(endian + 'h', fs.read(2))[0]

def ReadUShort(fs, endian = '<'):
    return struct.unpack(endian + 'H', fs.read(2))[0]

def ReadLong(fs, endian = '<'):
    return struct.unpack(endian + 'l', fs.read(4))[0]

def ReadULong(fs, endian = '<'):
    return struct.unpack(endian + 'L', fs.read(4))[0]

def ReadLong64(fs, endian = '<'):
    return struct.unpack(endian + 'q', fs.read(8))[0]

def ReadULong64(fs, endian = '<'):
    return struct.unpack(endian + 'Q', fs.read(8))[0]

def ReadFloat(fs, endian = '<'):
    return struct.unpack(endian + 'f', fs.read(4))[0]

def ReadDouble(fs, endian = '<'):
    return struct.unpack(endian + 'd', fs.read(8))[0]

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

def WriteUShort(fs, ushort, endian = '<'):
    return fs.write(struct.pack(endian + 'H', USHORT(ushort).value))

def WriteShort(fs, short, endian = '<'):
    return fs.write(struct.pack(endian + 'h', SHORT(short).value))

def WriteULong(fs, ulong, endian = '<'):
    return fs.write(struct.pack(endian + 'L', ULONG(ulong).value))

def WriteLong(fs, long, endian = '<'):
    return fs.write(struct.pack(endian + 'l', LONG(long).value))

def WriteLong64(fs, l64, endian = '<'):
    return fs.write(struct.pack(endian + 'q', LONG64(l64).value))

def WriteULong64(fs, ul64, endian = '<'):
    return fs.write(struct.pack(endian + 'Q', ULONG64(ul64).value))

def WriteFloat(fs, flt, endian = '<'):
    return fs.write(struct.pack(endian + 'f', FLOAT(flt).value))

def WriteDouble(fs, db, endian = '<'):
    return fs.write(struct.pack(endian + 'd', DOUBLE(db).value))

class BytesStream:
    def __init__(self):
        self.stream = None
        self.endian = '<'
        self.encoding = '936'

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
        if isinstance(file, bytes) or isinstance(file, bytearray):
            return self.openmem(file)

        self.stream = open(file, mode, buffering, encoding, errors, newline, closefd, opener)
        return self

    def openmem(self, buffer = b''):
        self.stream = io.BytesIO(buffer)
        return self

    def setendian(self, endian):
        self.endian = endian

    def setencoding(self, encoding):
        self.encoding = encoding

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

    def flush(self):
        return self.stream.flush()

    def size(self):
        pos = self.tell()
        self.seek(0, io.SEEK_END)
        stmsize = self.tell()
        self.seek(pos)
        return stmsize

    def byte(self):
        return ReadByte(self.stream, self.endian)

    def short(self):
        return ReadShort(self.stream, self.endian)

    def ushort(self):
        return ReadUShort(self.stream, self.endian)

    def long(self):
        return ReadLong(self.stream, self.endian)

    def ulong(self):
        return ReadULong(self.stream, self.endian)

    def long64(self):
        return ReadLong64(self.stream, self.endian)

    def ulong64(self):
        return ReadULong64(self.stream, self.endian)

    def float(self):
        return ReadFloat(self.stream, self.endian)

    def double(self):
        return ReadDouble(self.stream, self.endian)

    def astr(self, cp = None):
        return ReadAString(self.stream, self.encoding if cp is None else cp)

    def wstr(self):
        return ReadWString(self.stream)

    def wchar(self, b):
        return WriteChar(self.stream, b)

    def wbyte(self, b):
        return WriteByte(self.stream, b)

    def wshort(self, short):
        return WriteShort(self.stream, short, self.endian)

    def wushort(self, ushort):
        return WriteUShort(self.stream, ushort, self.endian)

    def wlong(self, l):
        return WriteLong(self.stream, l, self.endian)

    def wulong(self, l):
        return WriteULong(self.stream, l, self.endian)

    def wlong64(self, l64):
        return WriteLong64(self.stream, l, self.endian)

    def wulong64(self, l64):
        return WriteULong64(self.stream, l, self.endian)

    def wfloat(self, flt):
        return WriteFloat(self.stream, flt, self.endian)

    def wdouble(self, db):
        return WriteDouble(self.stream, db, self.endian)

