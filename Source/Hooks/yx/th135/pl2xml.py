from th135_base import *

def main(file):
    lines = ReadTextToList(file, CODE_PAGE)

    xml = []
    xml.append('<?xml version="1.0" encoding="utf-8"?>')
    xml.append('<THPL File="%s">' % os.path.basename(file))

    for i in range(len(lines)):
        line = lines[i]
        text = line.strip()
        if text == '': continue
        if text[0] < '\x80': continue
        #if text[0] in ['#', ',', ':']: continue

        text = text.split('\,', maxsplit = 1)
        if len(text) == 1:
            text = text[0].split(',', maxsplit = 1)

        text = text[0]
        if text[-1] == '\\':
            text = text[:-1]

        xml.append('    <Text Line = "%d" Begin = "%d" End = "%d">' % (i, 0, len(text)))
        xml.append('        <jp><![CDATA[%s]]></jp>' % text)
        xml.append('        <sc><![CDATA[%s]]></sc>' % text)
        xml.append('    </Text>')

    xml.append('</THPL>')

    open(file + '.xml', 'wb').write('\r\n'.join(xml).encode('UTF8'))

#for i in sys.argv[1:]:
#    TryInvoke(main, i)
#    #main(i)

def procfile(file):
    print(file)
    main(file)

TryInvoke(ForEachFile, sys.argv[1:], procfile, '*.pl')
