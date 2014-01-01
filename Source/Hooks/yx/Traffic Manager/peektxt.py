from ml import *

def main():
    os.chdir(os.path.dirname(__file__))
    lines = ReadTextToList('data/text/english.txt')

    xml = []
    xml.append('<?xml version="1.0" encoding="utf-8"?>')
    xml.append('<TM>')

    chars = {}

    for text in lines:
        if len(text) == 0 or text[0] != '[':
            continue

        id, txt = text.split('] ', maxsplit = 1)
        id = id + ']'

        xml.append('    <Text Id = "%s">' % id)
        xml.append('        <jp><![CDATA[%s]]></jp>' % txt)
        xml.append('        <sc><![CDATA[%s]]></sc>' % txt)
        xml.append('    </Text>')

        for ch in txt:
            chars[ch] = True

    xml.append('</TM>')

    open('tm.xml', 'wb').write('\r\n'.join(xml).encode('UTF8'))

    charset = []
    for ch in sorted(chars):
        charset.append(ch)

    open('chars.txt', 'wb').write(''.join(charset).encode('UTF16'))

TryInvoke(main)
