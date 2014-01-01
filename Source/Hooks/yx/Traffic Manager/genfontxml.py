from ml import *

def main(filename):
    font = ET.parse(filename).getroot()
    chars = font.find('chars')

    xml = []
    xml.append('<font width="19" height="18">')

    for char in chars:
        attrib = char.attrib
        id = int(attrib['id'])
        x = int(attrib['x'])
        y = int(attrib['y'])
        w = int(attrib['width'])
        h = int(attrib['height'])
        xo = int(attrib['xoffset'])
        yo = int(attrib['yoffset'])
        xa = int(attrib['xadvance'])

        if id == '"':
            id = '&quot;'

        if id == ' ':
            continue

        buf = chr(id).encode('936')
        if len(buf) == 2:
            id = struct.unpack('<H', buf)[0]

        xml.append(' <item ascii="%d" top="%d" x="%d" y="%d" width="%d" height="%d" leading="%d" trailing="%d" />' %
            (id, yo, x, y, w, h, xo, 1)
        )

    xml.append('</font>')
    open('font.xml', 'wb').write('\r\n'.join(xml).encode('UTF8'))


TryInvoke(main, 'xxx.xml')
