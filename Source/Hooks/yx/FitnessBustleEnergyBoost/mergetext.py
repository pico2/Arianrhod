from ml import *

def main():
    default = ET.parse('default.xml').getroot()
    chs = ET.parse('fbeb.chs.xml').getroot()

    charset = {}
    textmap = {}

    ch = 0x41
    for i in range(26):
        charset[chr(ch)] = True
        ch += 1

    ch = 0x61
    for i in range(26):
        charset[chr(ch)] = True
        ch += 1

    for text in chs:
        id = text.attrib['Id']
        sc = text.find('sc').text
        textmap[id] = sc

    xml = ['<Properties>']

    for text in default:
        if text.text == None:
            text.text = ''
        elif text.text != '':
            text.text = textmap[text.attrib['id']]

        text.text = text.text.replace(':', '：')

        for ch in text.text:
            if ch in ['\n', '\r']:
                continue
            charset[ch] = True

        xml.append('    <String id="%s">%s</String>' % (text.attrib['id'], text.text))

        cmt = '''\
    <String id="IDS_STR_LIST">©! #$%&'()*+,-./0123456789:;=?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\\\]^_`abcdefghijklmnopqrstuvwxyz{|}~àÿÀß</String>\
'''

    xml.append(cmt)
    xml.append('</Properties>')
    open('default2.xml', 'wb').write('\r\n'.join(xml).encode('U16'))
    open('charset.txt', 'wb').write(''.join(list(sorted(charset))).encode('U16'))

TryInvoke(main)
