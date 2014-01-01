from ml import *

def main():
    ft = ET.parse('SimHei46.xml').getroot().find('FontTable')
    font = BytesStream().open('font.rbf', 'wb')
    font.write(b'TFBR')
    font.wushort(len(ft))
    for ch in ft:
        id      = ord(ch.attrib['code'])
        left    = int(ch.attrib['sx1']) / 512
        top     = int(ch.attrib['sy1']) / 512
        right   = int(ch.attrib['sx2']) / 512
        bottom  = int(ch.attrib['sy2']) / 512
        width   = (right - left)

        font.write(struct.pack('<Hfffff', id, left, top, right, bottom, width))


TryInvoke(main)