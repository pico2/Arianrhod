from Libs.Misc import *
from Libs.IO.FileIo import *

def encodeVarint(value):
    varint = b''

    bits = value & 0x7f
    value >>= 7

    while value:
        varint += int.to_bytes(0x80 | bits, 1, 'little')
        bits = value & 0x7f
        value >>= 7

    varint += int.to_bytes(bits, 1, 'little')

    return varint

def decodeVarint(buffer, mask = (1 << 64) - 1):
    pos    = 0
    result = 0
    shift  = 0

    while True:
        b = buffer[pos]
        result |= ((b & 0x7f) << shift)
        pos += 1
        if not (b & 0x80):
            buffer
            result &= mask
            return (result, pos)

        shift += 7
        if shift >= 64:
            raise Exception('Too many bytes when decoding varint.')

def base64Encode(data, *, encoding = 'UTF8', multiline = False):
    import base64

    if isinstance(data, str):
        data = data.encode(encoding)

    data = base64.encodebytes(data)

    if not multiline:
        data = data.replace(b'\r', b'').replace(b'\n', b'')

    return data.decode('ASCII')

def base64Decode(data, *, encoding = None):
    import base64

    if isinstance(data, str):
        data = data.encode('ASCII')

    data = base64.decodebytes(data)

    if encoding:
        data = data.decode(encoding)

    return data

def HashBytes(bytes, method = 'md5'):
    import hashlib

    h = getattr(hashlib, method.lower())()
    h.update(bytes)
    return h.hexdigest()

def every(iter, n):
    for i in range(0, len(iter), n):
        yield iter[i : i + n]

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
        #traceback.print_exception(type(e), e, e.__traceback__)
        #exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(*sys.exc_info())
        PauseConsole()

    return None

def TryInvokeDbg(method, *values):
    try:
        return method(*values) if len(values) != 0 else method()
    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        bp()

    return None

def ReadTextToList(filename, cp = '936'):
    buf = open(filename,'rb').read()

    if buf[0:2] == b'\xff\xfe':
        buf = buf.decode('U16')
    elif buf[0:3] == b'\xef\xbb\xbf':
        buf = buf.decode('utf-8-sig')
    else:
        try:
            buf = buf.decode('UTF8')
        except UnicodeDecodeError:
            buf = buf.decode(cp)

    return buf.splitlines()

    return buf.replace('\r\n','\n').replace('\r','\n').split('\n')
