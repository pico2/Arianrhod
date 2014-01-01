from ml import *

'''

ulong ver
ulong strtblsize
byte strtbl[strtblsize]
ulong unknown1size
byte unknown1[unknown1size]
ulong doublecount1
double double1[doublecount1]
ulong doublecount2
double double2[doublecount2]
ulong opcount
ulong paramcount

opcodes

str ref table

'''

def readb(fs):
    return struct.unpack('<B', fs.read(1))[0]

def readdw(fs):
    return struct.unpack('<I', fs.read(4))[0]

def InitStringTable(fs):
    strtbl = {}

    strtblsize = readdw(fs)
    if strtblsize == 0:
        return None

    strbuf = fs.read(strtblsize)
    offset = 0
    while offset < len(strbuf):
        strpos = strbuf.find(b'\x00', offset)
        if strpos == -1:
            break

        text = strbuf[offset:].split(b'\x00', 2)[0].decode('UTF8')
        #if text != '':
        strtbl[offset] = text

        offset = strpos + 1

    return strtbl

def InitOpCodes(fs):
    opcount = readdw(fs)
    paramcount = readdw(fs)
    oplist = []

    for i in range(opcount):
        op = readb(fs)
        if op == 0xFF:
            op = readdw(fs)

        oplist.append(op)

    for i in range(paramcount * 2):
        oplist.append(readdw(fs))

    return oplist

def InitStringRefTable(fs):
    refcount = readdw(fs)
    strref = {}
    for i in range(refcount):
        offset = readdw(fs)
        count = readdw(fs)
        refindex = []
        for j in range(count):
            refindex.append(readdw(fs))

        #if len(refindex) != 0:
        strref[offset] = refindex

    return strref

def main():
    dirname = os.path.dirname(__file__) + '/'

    for dsofile in sys.argv[1:]:
        fs = open(dsofile, 'rb')
        if readdw(fs) != 0x29:
            continue

        strtbl = InitStringTable(fs)

        unksize = readdw(fs)
        fs.seek(unksize, SEEK_CUR)
        doublecount = readdw(fs)
        fs.seek(doublecount * 8, SEEK_CUR)
        doublecount = readdw(fs)
        fs.seek(doublecount * 8, SEEK_CUR)

        oplist = InitOpCodes(fs)
        strref = InitStringRefTable(fs)
        textlist = []

        for offset, refindex in strref.items():
            #if offset not in strtbl: continue

            #text = strtbl[offset]
            del strtbl[offset]

            #for index in refindex:
            #    line = '%08X, %08X, %08X, %08X, %08X: %s' % (oplist[index - 4], oplist[index - 3], oplist[index - 2], oplist[index - 1], oplist[index - 0], text)
            #    textlist.append(line)

        relativepath = os.path.abspath(dsofile)[len(dirname):].lower().replace('\\', '/')

        xml = []
        xml.append('<?xml version="1.0" encoding="utf-8"?>')
        xml.append('<%s FullPath = "%s">' % ('RTR', relativepath))

        textlist = []
        for offset in sorted(strtbl.keys()):
            text = strtbl[offset]
            if text.replace(' ', '').isdigit():
                continue

            xml.append('    <Text Offset = "%08X">' % offset)
            xml.append('        <jp><![CDATA[%s]]></jp>' % text)
            xml.append('        <sc><![CDATA[%s]]></sc>' % text)
            xml.append('    </Text>')

        xml.append('</%s>' % 'RTR')

        open(os.path.splitext(dsofile)[0] + '.xml', 'wb').write('\r\n'.join(xml).encode('utf_8_sig'))

TryInvoke(main)
#input()
