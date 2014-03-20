def XMLCreate(RootTag = 'Arianrhod', attrib = ''):
    if attrib != '':
        attrib = ' ' + attrib
    return ['<?xml version="1.0" encoding="utf-8"?>', '<%s%s>' % (RootTag, attrib)]

def XMLAppendText(xml, text, attrib = ''):

    if attrib != '':
        attrib = ' ' + attrib

    xml.append('    <Text%s>' % attrib)
    xml.append('        <jp><![CDATA[%s]]></jp>' % text)
    xml.append('        <sc><![CDATA[%s]]></sc>' % text)
    xml.append('    </Text>')

    return xml

def XMLSaveTo(xml, filename, RootTag = 'Arianrhod'):
    xml.append('</%s>' % RootTag)
    xml.append('')
    open(filename, 'wb').write('\r\n'.join(xml).encode('UTF8'))
