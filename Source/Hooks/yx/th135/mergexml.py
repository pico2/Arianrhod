from ml import *

def gettext(line):
    line = line.strip()[4:-5]
    if line.find('<![CDATA[') == 0:
        line = line[9:-3]

    return line

def hasjp(line):
    for x in line:
        if x >= '\x80':
            return True

    return False

def isletter(text):
    for x in text.lower():
        if (x < 'a' or x > 'z') and (x < '0' or x > '9'):
            return False

    return True

def main():

    cache = []
    xml = ['<?xml version="1.0" encoding="utf-8"?>', '<Arianrhod>']

    for x in os.listdir('xml'):
        text = ReadTextToList('xml\\' + x, 'UTF8')

        for i in range(len(text)):
            line = text[i].strip()
            if line[:4] != '<sc>':
                continue

            jp = gettext(text[i - 1])
            sc = gettext(line)

            if jp != sc:
                raise Exception('??')

            if jp.replace('-', '') == '': continue
            if jp.replace('-', '').isdigit(): continue
            if isletter(jp.replace('_', '')): continue
            if jp[-1].isdigit(): continue
            if jp.find('data/') != -1 or jp.find('data\\') != -1: continue
            #if not hasjp(jp): continue

            xml.append('    <Text File = "%s" Line = "%d">' % (x, i))
            xml.append('        <jp><![CDATA[%s]]></jp>' % jp)
            xml.append('        <sc><![CDATA[%s]]></sc>' % sc)
            xml.append('    </Text>')


    xml.append('</Arianrhod>')
    open('th135_jp.xml', 'wb').write('\r\n'.join(xml).encode('UTF8'))

TryInvoke(main)
