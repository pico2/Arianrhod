def AddRelativePath(path):
    import sys, os
    path = os.path.abspath(os.path.dirname(__file__) + '\\' + path)
    sys.path.append(path)

AddRelativePath('.')

del AddRelativePath

from syslib import *
from misc import *
from PyImage import *
from FileIo import *

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
    open(filename, 'wb').write('\r\n'.join(xml).encode('UTF8'))

def ForEachFile(filelist, callback, filter = '*.*'):
    for f in filelist:
        if os.path.isdir(f):
            for x in EnumDirectoryFiles(f, filter):
                callback(x)
        else:
            callback(f)

def TryForEachFile(filelist, callback, filter = '*.*'):
    TryInvoke(ForEachFile, filelist, callback, filter)

def TryInvoke(method, *values):
    try:
        return method(*values) if len(values) != 0 else method()
    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        input()

    return None

def ReadTextToList(filename, cp = '936'):
    stm = open(filename,'rb').read()
    if stm[0:2] == b'\xff\xfe':
        stm = stm.decode('U16')
    elif stm[0:3] == b'\xef\xbb\xbf':
        stm = stm.decode('utf-8-sig')
    else:
        stm = stm.decode(cp)

    return stm.replace('\r\n','\n').replace('\r','\n').split('\n')