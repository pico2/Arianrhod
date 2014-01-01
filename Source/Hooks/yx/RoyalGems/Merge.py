from ml import *
import Peek

def main():
    lang = ReadTextToList('en_lang.xml', 'UTF8')
    chs = ET.parse('2013-06-20 1416 royalgems.v01.chs.xml').getroot()

    charset = {}
    for ch in Peek.char:
        charset[chr(ch)] = True

    for x in chs:
        id = 'id="%s"' % x.attrib['Id']
        jp = x.find('jp').text
        sc = x.find('sc').text

        for ch in sc:
            charset[ch] = True

        for i in range(len(lang)):
            line = lang[i]
            if line.find(id) == -1:
                continue

            #lang[i] = line.replace(jp, sc)
            lang[i] = '        <T id="%s"><![CDATA[%s]]></T>' % (x.attrib['Id'], sc)
            break

    open('cn_lang.xml', 'wb').write('\r\n'.join(lang).encode('utf-8-sig'))
    open('charset.txt', 'wb').write(''.join(list(sorted(charset))).encode('U16'))

TryInvoke(main)
