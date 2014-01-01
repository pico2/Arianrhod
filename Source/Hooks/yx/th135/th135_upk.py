from th135_base import *
import zlib, shutil

th135_path = 'E:\\Desktop\\yx\\th135\\'

def HashFileNamePartial(name, partial):
    local = ''
    for ch in name:
        if ord(ch) in range(ord('A'), ord('Z') + 1):
            ch = ch.lower()
        local += ch

    name = local
    name = name.replace('/', '\\').encode(CODE_PAGE)
    for ch in name:
        if ch >= 0x80:
            ch |= 0xFFFFFF00

        partial = partial * 0x1000193
        partial ^= ch
        partial = partial & 0xFFFFFFFF

    return partial


def unpackTFCS(buf):
    buf = buf[1:]
    compsize = struct.unpack('<I', buf[:4])[0]
    uncompsize = buf[4:8]

    uncomp = zlib.decompress(buf[8:])
    return uncomp

def unpackTFBM(buf):
    unknown, bpp, width, height, scanlines, length = struct.unpack('<BBIIII', buf[:0x12])

    unp = zlib.decompress(buf[0x12:])

    hdr = BuildBmpHeader(width, height, bpp)

    pitch = width * int(bpp / 8)
    stride = (width * int(bpp / 8) + 3) & ~3

    offset = height * pitch
    while offset >= 0:
        offset = offset - pitch
        hdr += unp[offset:offset + stride]

    return hdr


def unpackTFPA(buf):
    unknown, compsize = struct.unpack('<BI', buf[:5])
    return zlib.decompress(buf[5:5 + compsize])

def unpackTFWA(buf):
    pass


class FileEntry:
    def __init__(self):
        self.FileName   = ''
        self.Hash       = 0
        self.Offset     = 0
        self.Size       = 0
        self.DecryptKey = b'\x00' * 0x10


def main(pakfile):
    os.chdir(os.path.dirname(sys.argv[0]))

    pakname = os.path.splitext(os.path.basename(pakfile))[0]

    namelist = ReadTextToList(pakname + '.name', CODE_PAGE)

    pakdir = BytesStream()
    pakdir.open(pakname + '.dir')

    dirlist = []

    filecount = 0

    index = 0
    for i in range(int(pakdir.size() / 8)):
        dirhash, filenum = pakdir.ulong(), pakdir.ulong()
        dirlist.append((dirhash, namelist[index:index + filenum]))
        index += filenum

    pakfiles = BytesStream()
    pakfiles.open(pakname + '.file')

    filemap = {}
    for i in range(int(pakfiles.size() / 0x28)):
        key, pakindex, hash, crc, offset, size = struct.unpack('<IIIIII', pakfiles.read(0x18))
        deckey = pakfiles.read(0x10)

        entry = FileEntry()

        entry.Hash       = hash
        entry.Offset     = offset
        entry.Size       = size
        entry.DecryptKey = deckey

        filemap[hash] = entry

    output = pakfile + '.out\\'
    shutil.rmtree(output, ignore_errors = True)
    os.makedirs(output, exist_ok = True)

    include = ['.png', '.dds', '.act', '.csv']
    include = ['.act', '.csv']

    unpackFunc = {}
    unpackFunc[b'TFCS'] = unpackTFCS
    unpackFunc[b'TFBM'] = unpackTFBM
    unpackFunc[b'TFPA'] = unpackTFPA

    pak = BytesStream()
    pak.open(th135_path + pakfile)

    fileindex = -1

    for dirinfo in dirlist:
        dirhash, dirfiles = dirinfo

        for file in dirfiles:
            fileindex += 1

            fullpath = output + '%08X_%s' % (dirhash, file)
            filehash = HashFileNamePartial(file, dirhash)
            if not filehash in filemap:
                print("can't find %s in %08X" % (file, dirhash))
                continue

            #if not os.path.splitext(fullpath)[1] in include: continue

            entry = filemap[filehash]

            pak.seek(entry.Offset)
            buf = bytearray(pak.read(entry.Size))

            index = 0
            for i in range(len(buf)):
                buf[i] ^= entry.DecryptKey[index]
                index = (index + 1) & 0xF

            magic = bytes(buf[:4])

            if magic in unpackFunc:
                buf = unpackFunc[magic](buf[4:])

            open(fullpath, 'wb').write(buf)
            print('(%05d / %05d) %s' % (fileindex, len(namelist), fullpath))


for pak in ['th135c.pak', 'th135b.pak']:
    TryInvoke(main, pak)
    exit(0)
