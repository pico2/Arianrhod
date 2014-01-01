from ml import *

def main():
    en = ET.parse('lang.cs.en.xml').getroot()
    sc = ET.parse('lang.cs.cn.xml').getroot()

    if en.tag != 'RTR' or sc.tag != 'RTR':
        return

    if len(en) != len(sc):
        print('len not match')
        return

    xml = []
    xml.append('<?xml version="1.0" encoding="utf-8"?>')
    xml.append('<%s FullPath = "%s">' % ('RTR', en.attrib['FullPath']))

    filters = ['rocks', 'flowers']

    for i in range(len(sc)):
        texten = en[i]
        textsc = sc[i]

        entxt = texten.find('jp').text
        sctxt = textsc.find('sc').text

        if entxt not in filters and entxt[0] >= 'a' and entxt[0] <= 'z' and entxt.find(' ') == -1:
            print(entxt)
            continue

        if entxt == sctxt:
            continue

        xml.append('    <Text Offset = "%s">' % texten.attrib['Offset'])
        xml.append('        <jp><![CDATA[%s]]></jp>' % texten.find('sc').text)
        xml.append('        <sc><![CDATA[%s]]></sc>' % textsc.find('sc').text)
        xml.append('    </Text>')

    xml.append('</%s>' % 'RTR')

    open('lang.cs.xml', 'wb').write('\r\n'.join(xml).encode('utf_8_sig'))

TryInvoke(main)
input()
