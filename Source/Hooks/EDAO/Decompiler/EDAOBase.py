from ml import *

CODE_PAGE = '936'

SEPITH_CHI  = 0
SEPITH_MIZU = 1
SEPITH_HONO = 3
SEPITH_KAZE = 2
SEPITH_TOKI = 4
SEPITH_SORA = 5
SEPITH_GEN  = 6

def IsTupleOrList(val):
    return type(val) == tuple or type(val) == list

def ljust_cn(string, n):
    cncount = 0
    for ch in string:
        if ch > '\x80':
            cncount += 1

    return string.ljust(n - cncount)

CHIP_TYPE_CHAR      = 7
CHIP_TYPE_APL       = 8
CHIP_TYPE_MONSTER   = 9

class ScenarioChipInfo:
    # ULONG chipindex
    def __init__(self, fs = None):

        if fs == None:
            return
        elif type(fs) == str:
            name = fs

            monster ='monster/'
            apl ='apl/'
            chr ='chr/'

            if name[:len(monster)].lower() == monster:
                chiptype = CHIP_TYPE_MONSTER
                name = name[len(monster):]
            elif name[:len(apl)].lower() == apl:
                chiptype = CHIP_TYPE_APL
                name = name[len(apl):]
            elif name[:len(chr)].lower() == chr:
                chiptype = CHIP_TYPE_CHAR
                name = name[len(chr):]
            else:
                raise Exception('unknown chip type')

            chipindex = int(os.path.splitext(name[2:])[0], 16)

            self.ChipIndex = (chiptype << 20) | chipindex

        elif type(fs) == int:

            self.ChipIndex = fs

        else:
            self.ChipIndex = fs.ulong()

    def __str__(self):
        chiptype = self.ChipIndex >> 20
        chipindex = self.ChipIndex & 0xFFFFF

        chipdir = 'monster' if chiptype == CHIP_TYPE_MONSTER else 'apl' if chiptype == CHIP_TYPE_APL else 'chr'

        return '%s/ch%05X.itc' % (chipdir, chipindex)

    def fileindex(self):
        return self.ChipIndex

    def binary(self):
        return struct.pack('<L', self.ChipIndex)

    def param(self):
        return '"%s"' % self.__str__()

class FileIndexBase:
    def __init__(self, param):
        self.Value = param

class ScenarioFileIndex:

    # c1000_2

    def __init__(self, param):

        self.FilePrefix = '0atcrmeb'
        #self.IsIndexZero = bool(param == 0)

        if type(param) == int:

            if param == 0xFFFFFFFF:
                self.FileIndex = param
                self.FileName = ''
                return

            ftype       = (param >> 0x14) & 0xF
            findex      = (param >> 4) & 0xFFFF
            fsubindex   = param & 0xF

            if fsubindex == 0:
                name = '%s%04X' % (self.FilePrefix[ftype], findex)
            else:
                name = '%s%04X_%X' % (self.FilePrefix[ftype], findex, fsubindex)

            self.FileName = name
            self.FileIndex = param

        elif type(param) == str:

            if param == '':
                self.FileIndex = 0xFFFFFFFF
                self.FileName = param
                return

            name = os.path.splitext(param)[0]

            ftype = self.FilePrefix.find(name[0])
            if ftype == -1:
                raise Exception('invalid scena file name')

            name = name[1:].split('_', 1)
            findex = int(name[0], 16)

            fsubindex = 0 if len(name) == 1 else int(name[1], 16)

            self.FileName = param
            self.FileIndex = 0x21000000 | (ftype << 0x14) | (findex << 4) | fsubindex

        else:

            raise Exception('unsupported input type')

    def Name(self):
        return self.FileName

    def Index(self):
        return self.FileIndex


class ChipFileIndex:

    def __init__(self, param):

        self.Value = param

        try:
            self.IsIndexZero = bool(int(param) == 0 or (int(param) == 0xFFFFFFFF))
        except:
            self.IsIndexZero = False

        monster ='monster/'
        apl ='apl/'
        chr ='chr/'

        if type(param) == int:

            chiptype = param >> 20
            chipindex = param & 0xFFFFF

            chipdir = monster if chiptype == CHIP_TYPE_MONSTER else apl if chiptype == CHIP_TYPE_APL else chr

            self.ChipName = '%sch%05X.itc' % (chipdir, chipindex)
            self.ChipIndex = param

        elif type(param) == str:

            if self.IsIndexZero:
                return

            name = param

            if name[:len(monster)].lower() == monster:

                chiptype = CHIP_TYPE_MONSTER
                name = name[len(monster):]

            elif name[:len(apl)].lower() == apl:

                chiptype = CHIP_TYPE_APL
                name = name[len(apl):]

            elif name[:len(chr)].lower() == chr:

                chiptype = CHIP_TYPE_CHAR
                name = name[len(chr):]

            else:

                raise Exception('unknown chip type')

            chipindex = int(os.path.splitext(name[2:])[0], 16)

            self.ChipIndex = (chiptype << 20) | chipindex
            self.ChipName = param

        else:

            raise Exception('unsupported input type')

    def IsZero(self):
        return self.IsIndexZero

    def Name(self):
        return self.ChipName if not self.IsIndexZero else self.Value

    def Index(self):
        return self.ChipIndex if not self.IsIndexZero else self.Value


class SymbolFileIndex:

    def __init__(self, param):

        try:
            self.IsIndexZero = bool(int(param) == 0)
        except:
            self.IsIndexZero = False

        if type(param) == int:

            self.SymbolIndex = param
            self.SymbolName = 'sy%05x.itp' % (param & 0xFFFFFF)

        elif type(param) == str:

            if self.IsIndexZero:
                return

            self.SymbolIndex = int(os.path.splitext(os.path.basename(param))[0][2:], 16) | 0x31000000
            self.SymbolName = param

        else:

            raise Exception('unsupported input type')

    def IsZero(self):
        return self.IsIndexZero

    def Name(self):
        return self.SymbolName if not self.IsIndexZero else 0

    def Index(self):
        return self.SymbolIndex if not self.IsIndexZero else 0

class BattleScriptFileIndex:

    def __init__(self, param = None):

        if param == None:
            param = 0

        try:
            self.IsIndexZero = bool(int(param) == 0)
        except:
            self.IsIndexZero = False

        if self.IsIndexZero:
            return

        prefix = [ 'ms', 'as', 'bs' ]
        datindex = 0x30000000

        if type(param) == int:

            ftype = (param >> 0x14) & 0xF
            findex = param & 0xFFFFF

            if ftype > len(prefix):
                raise Exception('unknown file type')

            self.FileIndex = param
            self.FileName = '%s%05x.dat' % (prefix[ftype], param & 0xFFFFF)

        elif type(param) == str:

            name = os.path.splitext(os.path.basename(param))[0]

            ftype = prefix.index(name[:2])

            self.FileIndex = int(name[2:], 16) | datindex | (ftype << 0x14)
            self.FileName = param

        else:

            raise Exception('unsupported input type')

    def IsZero(self):
        return self.IsIndexZero

    def Name(self):
        return self.FileName if not self.IsIndexZero else 0

    def Index(self):
        return self.FileIndex if not self.IsIndexZero else 0
