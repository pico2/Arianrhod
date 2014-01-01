from Unpacker import *

class RoyalGems(UnpackerBase):

    def Open(self, FileName):
        file = self.GetFileStream()
        file.open(FileName)
        length = file.ulong()
        magic = file.read(length)
        if magic != b'gepack':
            raise Exception('not gepack')

        entries = self.GetFileEntries()

        filenum = file.ulong()
        for i in range(filenum):

            length = file.ulong()

            entry = UnpackerFileEntryBase()
            entry.SetFileName(file.read(length * 2).decode('U16'))
            entry.Size = file.ulong()
            entry.Offset = file.ulong()

            file.byte()
            file.ulong()

            entries.append(entry)

    def Pack(self, FileList, InputPath, OutputFile = '', Flags = 0):
        InputPath = InputPath if InputPath[-1] != '\\' and InputPath[-1] != '/' else InputPath[:-1]
        if OutputFile == '':
            OutputFile = InputPath + '.chs'

        Path = InputPath.replace('\\', '/') + '/'

        magic = b'gepack'

        MagicSize = 4 + len(magic) + 4
        HeaderSize = MagicSize

        Entries = []
        for file in sorted(FileList):
            file = file.replace('\\', '/').replace(Path, '')
            entry = UnpackerFileEntryBase()
            entry.SetFileName(file)
            Entries.append(entry)

            HeaderSize += 4 + len(file) * 2 + 4 + 4 + 1 + 4

        file = self.GetFileStream().open(OutputFile, 'wb+')
        file.seek(HeaderSize)

        Offset = HeaderSize
        for entry in Entries:
            buf = open(Path + entry.GetFileName(), 'rb').read()
            entry.Offset = Offset
            entry.Size = len(buf)
            file.write(buf)

            Offset += entry.Size

        file.seek(0)
        file.wulong(len(magic))
        file.write(magic)
        file.wulong(len(Entries))
        for entry in Entries:
            file.wulong(len(entry.GetFileName()))
            file.write(entry.GetFileName().encode('UTF-16LE'))
            file.wulong(entry.Size)
            file.wulong(entry.Offset)
            file.wbyte(0)
            file.wulong(0)

        return len(Entries)

def main(file):
    rg = RoyalGems()
    rg.Auto(file)

for i in sys.argv[1:]:
    TryInvoke(main, i)
