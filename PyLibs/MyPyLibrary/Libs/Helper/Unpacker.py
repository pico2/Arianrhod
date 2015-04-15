from Libs.IO.FileStream import BytesStream
from Libs.Misc.Console import SetConsoleTitle
import time
import os

class UnpackerFileType:
    UnpackerFileBinary  = 0
    UnpackerFileBitmap  = 1
    UnpackerFilePNG     = 2
    UnpackerFileWave    = 3
    UnpackerFileMax     = 4

class UnpackerFileDataBase:
    def __init__(self, Buffer = b''):
        self.Buffer = Buffer

    def GetData(self):
        return self.Buffer


class UnpackerFileBinaryData(UnpackerFileDataBase):
    def __init__(self, Buffer = b''):
        super().__init__(Buffer)

class UnpackerFileImageData(UnpackerFileDataBase):
    def __init__(self, Buffer = b'', Width = -1, Height = -1, BitsPerPixel = -1):
        super().__init__(Buffer)

        self.Width          = Width
        self.Height         = Height
        self.BitsPerPixel   = BitsPerPixel

class UnpackerFileInfo:
    def __init__(self):
        self.FileType    = UnpackerFileType.UnpackerFileBinary
        self.FileNumber  = 1
        self.ExtraData   = b''
        self.Data        = []    # list of UnpackerFileData

    def GetFileNumber(self):
        return self.FileNumber

    def GetDataList(self):
        return self.Data

    def AddData(self, Data):
        self.Data.append(Data)

    def GetFileType(self):
        return self.FileType

UNPACKER_ENTRY_COMPRESSED   = 0x00000001
UNPACKER_ENTRY_ENCRYPTED    = 0x00000002

UNPACKER_SAVE_RAW_DATA      = 0x00000001


class UnpackerFileEntryFlags:
    def __init__(self, Flags):
        if type(Flags) == int:
            self.Flags = Flags
        elif type(Flags) == UnpackerFileEntryFlags:
            self.Flags = Flags.Flags
        else:
            raise Exception('unknown input type %s' % type(Flags))

        self.Compressed = self.FlagOn(UNPACKER_ENTRY_COMPRESSED)
        self.Encrypted = self.FlagOn(UNPACKER_ENTRY_ENCRYPTED)

    def FlagOn(self, Flags):
        return (self.Flags & Flags) != 0


class UnpackerFileEntryBase:
    def __init__(self):
        self.Flags           = 0
        self.Attributes      = 0
        self.Offset          = 0
        self.CompressedSize  = 0
        self.Size            = 0
        self.FileName        = ''

    def GetFileName(self):
        return self.FileName

    def SetFileName(self, Name):
        self.FileName = Name


class UnpackerBase:
    def __init__(self):
        self.File = BytesStream()
        self.Entry = []

    def DefaultNotImplemented(self):
        raise NotImplementedError

    def GetFileEntries(self):
        return self.Entry

    def GetFileStream(self):
        return self.File

    def Open(self, FileName):
        return self.DefaultNotImplemented()

    def GetFileData(self, Entry, Flags = 0):
        File = self.GetFileStream()
        File.seek(Entry.Offset)

        FileInfo = UnpackerFileInfo()
        FileInfo.AddData(UnpackerFileBinaryData(File.read(Entry.Size)))

        return FileInfo

    def ExtractCallBack(self, Entry, FileInfo, OutputPath, OutputFileName):
        pass

    def ExtractFile(self, Entry, OutputPath = '', Flags = 0):
        return self.ExtractFileBase(Entry, OutputPath, Flags)

    def ExtractFileBase(self, Entry, OutputPath = '', Flags = 0):
        FileInfo = self.GetFileData(Entry, Flags)
        if FileInfo == None:
            raise Exception('')

        OutputFileName = os.path.join(OutputPath, Entry.GetFileName())
        os.makedirs(os.path.dirname(OutputFileName), exist_ok = True)

        Result = self.ExtractCallBack(Entry, FileInfo, OutputPath, OutputFileName)
        if Result != None:
            return Result

        TypeExtension = {
            UnpackerFileType.UnpackerFileBitmap : '.bmp',
            UnpackerFileType.UnpackerFilePNG    : '.png',
            UnpackerFileType.UnpackerFileWave   : '.wav',
        }

        TypeExtension = TypeExtension[FileInfo.GetFileType()] if FileInfo.GetFileType() in TypeExtension else ''

        if FileInfo.GetFileNumber() < 2:

            if TypeExtension != '':
                OutputFileName = os.path.splitext(OutputFileName)[0] + TypeExtension

            File = BytesStream().open(OutputFileName, 'wb')
            data = FileInfo.GetDataList()[0].GetData()
            File.write(data)
            return len(data)

        Size = 0
        FileName = os.path.splitext(OutputFileName)[0]
        for Index in range(FileInfo.GetFileNumber()):

            data = FileInfo.GetDataList()[Index].GetData()
            File = BytesStream().open('%s_%08X%s' % (FileName, Index, TypeExtension, 'wb'))
            File.write(data)

            Size += len(data)

        return Size

    def Pack(self, FileList, InputPath, OutputFile = '', Flags = 0):
        return self.DefaultNotImplemented()

    def Auto(self, Path, AutoFlags = 0):

        if os.path.isdir(Path):
            print('Packing %s ...' % Path)
            FileList = EnumDirectoryFiles(Path)
            ret = self.Pack(FileList, Path)
            time.sleep(1)
            return ret

        self.Open(Path)

        OutputPath = os.path.join(os.path.splitext(Path)[0]) + '\\'

        Entries = self.GetFileEntries()
        Path = os.path.basename(Path)

        for i in range(len(Entries)):
            entry = Entries[i]

            SetConsoleTitle('%d / %d: %s' % (i + 1, len(Entries), Path))

            try:
                print('Extracting "%s" ... ' % entry.GetFileName(), end = '')
            except:
                print('Extracting xxx ... ', end = '')

            try:
                size = self.ExtractFile(entry, OutputPath)
            except:
                size = None

            print('%s' % 'OK' if size != None else 'failed')

        time.sleep(1)
