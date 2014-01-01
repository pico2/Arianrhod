from ml import *

def writestr(fs, str):
    str = str.encode('UTF8')
    fs.wushort(len(str))
    fs.write(str)

def addtext(TextSet, str):
    for ch in str:
        TextSet[ch] = True

def main():
    root = ET.parse('ff4.xml').getroot()

    Locales = []
    TextSet = {}
    TextMap = {}
    Tags = []
    FirstLocales = None

    for node in root:

        Locale = node.attrib['Locale']
        Type = node.attrib['Type']

        try:
            Locales.index(Locale)
        except ValueError:
            Locales.append(Locale)

        if Locale not in TextMap:
            textlist = []
            TextMap[Locale] = ['', textlist]
        else:
            textlist = TextMap[Locale][1]

        if FirstLocales is None:
            FirstLocales = Locale

        if Locale == FirstLocales and 'Tag' in node.attrib:
            Tags.insert(int(node.attrib['Id']), node.attrib['Tag'])

        if Type == 'ChrList':
            TextMap[Locale][0] = node.find('sc').text
        elif Type == 'Text':
            Id = int(node.attrib['Id'])
            textlist.insert(Id, node.find('sc').text)


    fs = BytesStream().open('MTF_1.0.lbin', 'wb')
    fs.setendian('>')

    fs.wulong(len(Locales))
    for locale in Locales:
        writestr(fs, locale)

    fs.wulong(len(Tags))
    for tag in Tags:
        writestr(fs, tag)

    for locale in Locales:
        writestr(fs, locale)

        chrlist, textlist = TextMap[locale]

        if len(textlist) != len(Tags):
            raise Exception('text count (%d) != tags count (%d)' % (len(textlist), len(Tags)))

        fs.wulong(len(Tags))
        for i in range(len(textlist)):
            fs.wulong(i)

            addtext(TextSet, textlist[i])
            writestr(fs, textlist[i])

        addtext(TextSet, chrlist)
        writestr(fs, chrlist)

    open('charset.txt', 'wb').write(''.join(sorted(list(TextSet))).encode('utf_8_sig'))


if __name__ == '__main__':
    TryInvoke(main)
