from ml import *

def main():
    os.chdir(os.path.dirname(__file__))
    chs = ET.parse('Traffic Manager.chs.xml').getroot()

    textmap = {}
    for text in chs:
        id = text.attrib['Id']
        text = text.find('sc').text
        textmap[id] = text.replace('，', '， ').replace('。', '。 ')

    lines = ReadTextToList('data/text/english.txt')

    chars = {}

    for i in range(len(lines)):
        text = lines[i]
        if len(text) == 0 or text[0] != '[':
            continue

        id, txt = text.split('] ', maxsplit = 1)
        id = id + ']'

        lines[i] = '%s %s' % (id, textmap[id])

        for ch in lines[i]:
            chars[ch] = True

    open('data/text/chinese.txt', 'wb').write('\r\n'.join(lines).encode('936'))

    charset = []
    for ch in sorted(chars):
        charset.append(ch)

    open('chars.txt', 'wb').write(''.join(charset).encode('UTF16'))

TryInvoke(main)
