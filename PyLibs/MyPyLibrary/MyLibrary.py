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

def ForEachFile(filelist, callback, filter = '*.*'):
    if type(filelist) == str:
        filelist = [filelist]

    for f in filelist:
        if os.path.isdir(f):
            for x in EnumDirectoryFiles(f, filter):
                callback(x)
        else:
            callback(f)

def TryForEachFile(filelist, callback, filter = '*.*'):
    TryInvoke(ForEachFile, filelist, callback, filter)

def TryForEachFileMP(filelist, callback, filter = '*.*'):
    TryInvoke(ForEachFileMP, filelist, callback, filter)


def ForEachFileMPInvoker(cb, flist):
    for f in flist:
        cb(f)

def ForEachFileMP(filelist, callback, filter = '*.*'):
    if type(filelist) == str:
        filelist = [filelist]

    allfile = []
    for f in filelist:
        if os.path.isdir(f):
            allfile += EnumDirectoryFiles(f, filter)
        else:
            allfile.append(f)

    if len(allfile) == 0:
        return

    import multiprocessing

    core = multiprocessing.cpu_count()
    if core == 1:
        return ForEachFileMPInvoker(callback, allfile)

    files = []
    step = int(len(allfile) / core + 1)
    n = 0
    for i in range(core):
        files.append(allfile[n:n + step])
        n += step

    process = []
    for f in range(len(files) - 1):
        f = files[f]
        t = multiprocessing.Process(target = ForEachFileMPInvoker, args = [callback, f])
        t.start()
        process.append(t)

    ForEachFileMPInvoker(callback, files[-1])

    for t in process:
        t.join()


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
