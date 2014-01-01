from ml import *

def writedw(fs, dw):
    fs.write(struct.pack('<I', dw))

def main():
    for xmlfile in sys.argv[1:]:
        tree = ET.parse(xmlfile)
        rtr = tree.getroot()
        if rtr.tag != 'RTR':
            continue

        xmlbin = os.path.splitext(xmlfile)[0] + '.bin'
        fs = open(xmlbin, 'wb')
        writedw(fs, HashAPI(os.path.splitext(rtr.attrib['FullPath'])[0]))
        writedw(fs, len(rtr))
        for text in rtr:
            writedw(fs, int(text.attrib['Offset'], 16))
            text = text.find('sc').text.encode('UTF8') + b'\x00'
            textlen = len(text)
            writedw(fs, textlen)
            fs.write(text)
            if textlen % 4 != 0:
                fs.write(b'\x00' * (4 - textlen % 4))

TryInvoke(main)
