from ml import *
from Unpacker import *
import lzma

# 게임종료

def DecryptBuffer(buf):
    mask = [0xDF, 0x97, 0x6F, 0x03]

    buf = bytearray(buf)
    index = 0
    for i in range(len(buf)):
        buf[i] ^= mask[index]
        index += 1
        if index == len(mask):
            index = 0

    return buf


class KritikaFileEntry(UnpackerFileEntryBase):
    def __init__(self):
        super().__init__()

        self.UnknownShort1 = 0
        self.UnknownShort2 = 0
        self.UnknownULong1 = 0
        self.UnknownULong2 = 0

        self.Properties = b''


class Kritika(UnpackerBase):

    def Open(self, FileName):

        file = self.GetFileStream().open(FileName)
        magic = file.read(4)
        if magic != b'GKPA':
            raise Exception('magic not match: %s' % magic)

        version = file.ushort()
        if version < 0 or version > 2:
            raise Exception('unknown version %d' % version)

        indexoffset = file.ulong64()

        type1 = file.byte()
        type2 = file.byte()
        type3 = file.byte()

        if type1 != 1:
            raise Exception('unknown alp type %s' % FileName)

        file.seek(indexoffset)

        # read Root directory first

        self.ReadDirectory(self.GetFileEntries(), '')
        #for x in self.GetFileEntries():
        #    print(x.GetFileName())
        #    input()

    def ReadEntry(self, fs):
        length = fs.ulong()
        return BytesStream().open(DecryptBuffer(fs.read(length)))

    def ReadDirectory(self, EntryList, FullPath):

        fs = self.GetFileStream()

        pos = fs.tell()

        entry = self.ReadEntry(fs)

        magic = entry.read(4)
        if magic != b'DGKP':
            raise Exception('unknown entry magic %s @ %X' % (magic, pos))

        version = entry.ushort()
        if version != 1:
            raise Exception('unknown format %X @ %X' % (version, pos))

        dirnum = entry.ulong()
        filenum = entry.ulong()

        namelen = entry.ushort()
        name = ''
        if namelen != 0:
            name = entry.read(namelen * 2).decode('U16') + '\\'

        FullPath += name

        for i in range(dirnum):
            self.ReadDirectory(EntryList, FullPath)

        for i in range(filenum):
            pos = fs.tell()

            entry = self.ReadEntry(fs)

            magic = entry.read(4)
            if magic != b'FGKP':
                raise Exception('unknown file entry magic %s @ %X' (magic, pos))

            version = entry.ushort()
            if version != 1:
                raise Exception('unknown file entry format %X @ %X' % (version, pos))

            prop = entry.read(5)

            offset      = entry.ulong()
            size        = entry.ulong()
            compressed  = entry.ulong()

            short1 = entry.ushort()
            short2 = entry.ushort()
            ulong1 = entry.ulong()

            # if version >= 1
            ulong2 = entry.ulong()

            namelen = entry.ushort()
            name = ''
            if namelen != 0:
                name = entry.read(namelen * 2).decode('U16')
            else:
                raise Exception('file without file name ?? @ %X' % pos)

            alpentry = KritikaFileEntry()

            alpentry.SetFileName(FullPath + name)

            alpentry.Offset         = offset
            alpentry.Size           = size
            alpentry.CompressedSize = compressed
            alpentry.UnknownShort1  = short1
            alpentry.UnknownShort2  = short2
            alpentry.UnknownULong1  = ulong1
            alpentry.UnknownULong2  = ulong2
            alpentry.Properties     = prop

            EntryList.append(alpentry)

    def GetFileData(self, Entry, Flags = 0):

        fs = self.GetFileStream()
        fs.seek(Entry.Offset)

        buf = DecryptBuffer(fs.read(Entry.CompressedSize))

        #
        # The .lzma File Format
        #
        # +------------+----+----+----+----+--+--+--+--+--+--+--+--+==========================+
        # | Properties |  Dictionary Size  |   Uncompressed Size   |   LZMA Compressed Data   |
        # +------------+----+----+----+----+--+--+--+--+--+--+--+--+==========================+
        #

        buf = self.LZMADecompress(Entry.Properties + struct.pack('<ii', -1, -1) + buf)

        fileinfo = UnpackerFileInfo()
        fileinfo.AddData(UnpackerFileBinaryData(buf))

        return fileinfo

    def LZMADecompress(self, data):
        results = []
        while True:
            decomp = lzma.LZMADecompressor(lzma.FORMAT_ALONE, None, None)
            results.append(decomp.decompress(data))

            if not decomp.unused_data:
                return b"".join(results)
            # There is unused data left over. Proceed to next stream.
            data = decomp.unused_data



def main(alpfile):
    alp = Kritika()
    alp.Auto(alpfile)


TryForEachFile(sys.argv[1:], main)
