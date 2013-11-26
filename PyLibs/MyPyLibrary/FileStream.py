from MyPyLibrary.syslib import *
import io

_DEFAULT_ENDIAN = '<'

def _ReadChar(fs, endian = _DEFAULT_ENDIAN):
    return struct.unpack(endian + 'b', fs.read(1))[0]

def _ReadUChar(fs, endian = _DEFAULT_ENDIAN):
    return struct.unpack(endian + 'B', fs.read(1))[0]

def _ReadShort(fs, endian = _DEFAULT_ENDIAN):
    return struct.unpack(endian + 'h', fs.read(2))[0]

def _ReadUShort(fs, endian = _DEFAULT_ENDIAN):
    return struct.unpack(endian + 'H', fs.read(2))[0]

def _ReadLong(fs, endian = _DEFAULT_ENDIAN):
    return struct.unpack(endian + 'l', fs.read(4))[0]

def _ReadULong(fs, endian = _DEFAULT_ENDIAN):
    return struct.unpack(endian + 'L', fs.read(4))[0]

def _ReadLong64(fs, endian = _DEFAULT_ENDIAN):
    return struct.unpack(endian + 'q', fs.read(8))[0]

def _ReadULong64(fs, endian = _DEFAULT_ENDIAN):
    return struct.unpack(endian + 'Q', fs.read(8))[0]

def _ReadFloat(fs, endian = _DEFAULT_ENDIAN):
    return struct.unpack(endian + 'f', fs.read(4))[0]

def _ReadDouble(fs, endian = _DEFAULT_ENDIAN):
    return struct.unpack(endian + 'd', fs.read(8))[0]

def _ReadAString(fs, cp = '936'):
    string = b''
    while True:
        buf = fs.read(1)
        if buf == b'' or buf == b'\x00':
            break

        string += buf

    return string.decode(cp)

def _ReadWString(fs):
    string = b''
    while True:
        buf = fs.read(2)
        if buf == b'' or buf == b'\x00\x00':
            break

        string += buf

    return string.decode('U16')

def _WriteByte(fs, b):
    return fs.write(struct.pack('<B', BYTE(b & 0xFF).value))

def _WriteChar(fs, b):
    return fs.write(CHAR(b & 0xFF).value)

def _WriteUShort(fs, ushort, endian = _DEFAULT_ENDIAN):
    return fs.write(struct.pack(endian + 'H', USHORT(ushort).value))

def _WriteShort(fs, short, endian = _DEFAULT_ENDIAN):
    return fs.write(struct.pack(endian + 'h', SHORT(short).value))

def _WriteULong(fs, ulong, endian = _DEFAULT_ENDIAN):
    return fs.write(struct.pack(endian + 'L', ULONG(ulong).value))

def _WriteLong(fs, long, endian = _DEFAULT_ENDIAN):
    return fs.write(struct.pack(endian + 'l', LONG(long).value))

def _WriteLong64(fs, l64, endian = _DEFAULT_ENDIAN):
    return fs.write(struct.pack(endian + 'q', LONG64(l64).value))

def _WriteULong64(fs, ul64, endian = _DEFAULT_ENDIAN):
    return fs.write(struct.pack(endian + 'Q', ULONG64(ul64).value))

def _WriteFloat(fs, flt, endian = _DEFAULT_ENDIAN):
    return fs.write(struct.pack(endian + 'f', FLOAT(flt).value))

def _WriteDouble(fs, db, endian = _DEFAULT_ENDIAN):
    return fs.write(struct.pack(endian + 'd', DOUBLE(db).value))

class BytesStream:
    def __init__(self):
        self.stream = None
        self.endian = _DEFAULT_ENDIAN
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

    def getendian(self):
        return self.endian

    def setencoding(self, encoding):
        self.encoding = encoding

    def truncate(self, size):
        return self.stream.truncate(size)

    def seek(self, offset, method = io.SEEK_SET):
        return self.stream.seek(offset, method)

    def rewind(self):
        return self.stream.seek(0)

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

    def eof(self):
        return self.tell() >= self.size()

    def boolean(self):
        return bool(self.uchar())

    def char(self):
        return _ReadChar(self.stream, self.endian)

    def uchar(self):
        return _ReadUChar(self.stream, self.endian)

    def byte(self):
        return _ReadUChar(self.stream, self.endian)

    def short(self):
        return _ReadShort(self.stream, self.endian)

    def ushort(self):
        return _ReadUShort(self.stream, self.endian)

    def long(self):
        return _ReadLong(self.stream, self.endian)

    def ulong(self):
        return _ReadULong(self.stream, self.endian)

    def long64(self):
        return _ReadLong64(self.stream, self.endian)

    def ulong64(self):
        return _ReadULong64(self.stream, self.endian)

    def float(self):
        return _ReadFloat(self.stream, self.endian)

    def double(self):
        return _ReadDouble(self.stream, self.endian)

    def astr(self, cp = None):
        return _ReadAString(self.stream, self.encoding if cp is None else cp)

    def wstr(self):
        return _ReadWString(self.stream)

    def wchar(self, b):
        return _WriteChar(self.stream, b)

    def wbyte(self, b):
        return _WriteByte(self.stream, b)

    def wshort(self, short):
        return _WriteShort(self.stream, short, self.endian)

    def wushort(self, ushort):
        return _WriteUShort(self.stream, ushort, self.endian)

    def wlong(self, l):
        return _WriteLong(self.stream, l, self.endian)

    def wulong(self, l):
        return _WriteULong(self.stream, l, self.endian)

    def wlong64(self, l64):
        return _WriteLong64(self.stream, l, self.endian)

    def wulong64(self, l64):
        return _WriteULong64(self.stream, l, self.endian)

    def wfloat(self, flt):
        return _WriteFloat(self.stream, flt, self.endian)

    def wdouble(self, db):
        return _WriteDouble(self.stream, db, self.endian)

