from Unpacker import *

DecryptTable = b'\x6e\x87\x75\x5a\x04\x89\x04\xd0\x00\x22\x94\x8d\x2a\xf9\x58\xe8'

def DecryptBuffer(buf, declen = None):
    buf = bytearray(buf)
    if declen == None:
        declen = len(buf)

    for i in range(declen):
        buf[i] ^= DecryptTable[i % len(DecryptTable)]

    return buf

class LunchRushHD(UnpackerBase):

    def Open(self, FileName):
        fs = self.File.open(FileName)
        magic, filenum, zero = struct.unpack('<III', fs.read(0xC))
        if magic != 0x4152:
            raise Exception('magic not match: %X' % magic)

        NewEntry = UnpackerFileEntryBase

        entrylist = self.Entry
        for i in range(filenum):
            entry = NewEntry()
            namelen = fs.ulong()
            entry.SetFileName(DecryptBuffer(fs.read(namelen)).decode('U16'))
            entrylist.append(entry)

        for entry in entrylist:
            offsethigh, offsetlow, size = struct.unpack('<III', fs.read(0xC))
            
            if offsethigh != 0: bp()

            entry.Size = size
            entry.Offset = offsetlow | (offsethigh << 32)

    def GetFileData(self, Entry, Flags = 0):
        File = self.File
        File.seek(Entry.Offset)

        buf = DecryptBuffer(File.read(Entry.Size), 0x14)

        FileInfo = UnpackerFileInfo()
        FileInfo.AddData(UnpackerFileBinaryData(buf))

        return FileInfo

TryInvoke(ForEachFile, sys.argv[1:], lambda file : LunchRushHD().Auto(file))
