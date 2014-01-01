from ml import *

def matchline(xmlline, text):
    return xmlline.strip() == '<jp><![CDATA[%s]]></jp>' % text.strip()

def makesc(text):
    return '<sc><![CDATA[%s]]></sc>' % text

def main(chs, xmlpath):

    if xmlpath[-1] != '\\':
        xmlpath += '\\'

    print(chs)
    chs = ET.parse(chs).getroot()

    chsmap = {}

    for text in chs:
        file = text.attrib['File']
        if file not in chsmap:
            chsmap[file] = []

        chsmap[file].append(text)

    for file in sorted(chsmap):
        print('updating %s' % file)

        textlist = chsmap[file]
        xml = ReadTextToList(xmlpath + file, 'UTF8')

        for text in textlist:
            line = int(text.attrib['Line'])
            jp = text.find('jp').text
            sc = text.find('sc').text

            if not matchline(xml[line - 1], jp):
                raise Exception('does not match at line %d of %s' % (line, file))

            xml[line] = xml[line].replace(makesc(jp), makesc(sc)).replace('\\\\n', '\\n')

        open(xmlpath + file, 'wb').write('\r\n'.join(xml).encode('UTF8'))

TryInvoke(main, 'th135_jp.v02.chs.xml', 'xmlcn')
