#encoding=utf-8

from th135_base import *
from ctypes import windll

if len(sys.argv) < 2:
    sys.exit(0)

def ConvertXmlToTHCsv(xmlfile):
    tree = ET.parse(xmlfile)
    THCsv = tree.getroot()

    if THCsv.tag != 'THCsv':
        return

    blockcount = len(THCsv)
    rows = []

    for row in THCsv:
        textlist = []

        for text in row:
            jp = text.find('jp').text
            sc = text.find('sc').text
            if sc == None:
                sc = ''
            elif jp == sc:
                #if xmlfile.lower().find('reimu') != -1: print(sc)
                sub = ['_', 'data/']

                for x in sub:
                    if sc.find(x) == -1:
                        continue
                    sc = jp.encode(CODE_PAGE).decode('936')
                    break

                pass

            #if sc.lower().find('data/') != -1 or sc.lower().find('data\\') != -1:
            #    sc = jp.encode('932').decode('936')

            textlist.append(sc)

        rows.append(textlist)

    csv = open(os.path.splitext(xmlfile)[0], 'wb')
    csv.write(struct.pack('<I', len(rows)))
    for row in rows:
        csv.write(struct.pack('<I', len(row)))
        for text in row:

            text = text.replace('♪', '').replace('・', '·')

            text = text.encode('936')
            csv.write(struct.pack('<I', len(text)))
            csv.write(text)

def procfile(file):
    print(file)
    ConvertXmlToTHCsv(file)

TryInvoke(ForEachFile, sys.argv[1:], procfile, '*.csv.xml')
