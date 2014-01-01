from ml import *

def readstr(fs):
    return fs.read(fs.ushort()).decode('UTF8')

def main():
    fs = BytesStream().open('MTF_1.0.lbin')
    fs.setendian('>')

    locale_num = fs.ulong()

    sorted_locale = []
    locales = []
    stringtag = []
    localevalues = {}

    for i in range(locale_num):
        locales.append(readstr(fs))

    stringtagnum = fs.ulong()

    for i in range(stringtagnum):
        stringtag.append(readstr(fs))

    for i in range(locale_num):
        current_locale = readstr(fs)

        #if current_locale != 'English': continue

        values = []
        localevalues[current_locale] = values

        valuenum = fs.ulong()

        if valuenum != stringtagnum:
            raise Exception('error number: %d %d' % (valuenum, stringtagnum))

        for j in range(valuenum):
            id = fs.ulong()
            val = readstr(fs)
            values.append((id, val))

        values.append(readstr(fs))


    xml = XMLCreate()

    for locale in locales:
        values = localevalues[locale]
        for text in range(len(values) - 1):
            id, text = values[text]

            attr = 'Type="Text" Tag="%s" Id="%d" Locale="%s"' % (stringtag[id], id, locale)
            XMLAppendText(xml, text, attr)

        XMLAppendText(xml, values[-1], 'Type="ChrList" Locale="%s"' % locale)

    XMLSaveTo(xml, "ff4.xml")


TryInvoke(main)
