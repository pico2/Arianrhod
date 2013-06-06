from syslib import *
from misc import *
from PyImage import *
from FileIo import *

def ForEachFile(filelist, callback, filter = '*.*'):
    for f in sys.argv[1:]:
        if os.path.isdir(f):
            for x in EnumDirectoryFiles(f, filter):
                callback(x)
        else:
            callback(f)

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