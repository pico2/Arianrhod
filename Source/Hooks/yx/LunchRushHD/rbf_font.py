from ml import *

def main(file):
    fs = BytesStream().open(file)
    magic = fs.read(4)
    if magic != b'TFBR':
        raise Exception('magic %s' % magic)

    width, height = 126, 119
    width, height = 960, 688

    xml = XMLCreate()

    glyphnum = fs.ushort()

    xml.append('    <chars count="%d">' % glyphnum)

    for i in range(glyphnum):
        id, l, t, r, b, w = struct.unpack('<Hfffff', fs.read(0x16))

        l *= width
        t *= height
        r *= width
        b *= height
        w *= width

        xml.append('        <char id="%c" left="%d" top="%d" right="%d" bottom="%d" width="%d" />' % (id, l, t, r, b, w))

    xml.append('    </chars>')

    block2 = fs.read(8)
    if block2 != b'':
        xml.append('    <kerneling>')
        for i in range(glyphnum):
            id, x, y = struct.unpack('<Hff', fs.read(0xA))
            x *= width
            y *= height
            xml.append('        <char id="%c" x="%f" y="%f" />' % (id, x, y))
        xml.append('    </kerneling>')

    XMLSaveTo(xml, file + '.xml')

for f in sys.argv[1:]:
    TryInvoke(main, f)