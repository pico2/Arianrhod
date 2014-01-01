#encoding=utf-8

from th135_base import *
from ctypes import windll

def ConvertTHCSToXml(csvfile):
    csv = open(csvfile, 'rb')

    textblock = []

    rows = struct.unpack('<I', csv.read(4))[0]
    for i in range(rows):
        columes = struct.unpack('<I', csv.read(4))[0]
        textlist = []
        for j in range(columes):
            length = struct.unpack('<I', csv.read(4))[0]
            text = csv.read(length).decode(CODE_PAGE)
            #if text.lower().find('data/') != -1: return
            #if text.lower().find('data\\') != -1: return

            textlist.append(text)

        textblock.append(textlist)

    xml = []
    xml.append('<?xml version="1.0" encoding="utf-8"?>')
    xml.append('<THCsv File="%s">' % os.path.basename(csvfile))

    for block in textblock:
        xml.append('    <Row>')
        for text in block:
            xml.append('        <Text>')
            xml.append('            <jp><![CDATA[%s]]></jp>' % text)
            xml.append('            <sc><![CDATA[%s]]></sc>' % text)
            xml.append('        </Text>')

        xml.append('    </Row>')

    xml.append('</THCsv>')

    open(csvfile + '.xml', 'wb').write('\r\n'.join(xml).encode('UTF8'))

def procfile(file):
    print(file)
    ConvertTHCSToXml(file)

TryInvoke(ForEachFile, sys.argv[1:], procfile, '*.csv')
