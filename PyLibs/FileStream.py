import struct, io

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

    def openmem(self, buffer):
        self.stream = io.BytesIO(buffer)
        return self

    def seek(self, offset, method = io.SEEK_SET):
        return self.stream.seek(offset, method)

    def forward(self, length):
        return self.stream.seek(length, io.SEEK_CUR)

    def read(self, n = -1):
        return self.stream.read(n)

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

