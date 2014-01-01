from th135_base import *

def filterstr(text):
    return text.replace('・', '·').replace('ﾇ', '').replace('♪', '')

def main(xml):
    plfile = os.path.splitext(xml)[0]
    pl = ReadTextToList(plfile, '936')
    plcn = ReadTextToList(plfile, CODE_PAGE)

    xml = ET.parse(xml).getroot()

    for text in xml:
        line = int(text.attrib['Line'])
        beg = int(text.attrib['Begin'])
        end = int(text.attrib['End'])
        jp = text.find('jp').text
        sc = text.find('sc').text
        if jp == sc:
            continue

        new = plcn[line][0:beg] + text.find('sc').text + plcn[line][end:]
        pl[line] = new

    open(plfile, 'wb').write(filterstr('\r\n'.join(pl)).encode('936'))

def procfile(file):
    print(file)
    main(file)

TryInvoke(ForEachFile, sys.argv[1:], procfile, '*.pl.xml')
