from .SysLib import OrderedDict

def RoundDown(Value, Multiple):
    return type(Value)(type(Value)(Value / Multiple) * Multiple)

def RoundUp(Value, Multiple):
    return RoundDown(Value + Multiple - 1, Multiple)

def rol32(val, shift):
    val &= 0xFFFFFFFF
    return ((val << shift) | (val >> (32 - shift))) & 0xFFFFFFFF

def ror32(val, shift):
    val &= 0xFFFFFFFF
    return ((val >> shift) | (val << (32 - shift))) & 0xFFFFFFFF

def HashAPI(str):
    hash = 0
    for ch in str:
        hash = rol32(hash, 0xD) ^ ord(ch)

    return hash & 0xFFFFFFFF

def _IsBaseObject(obj):
    return isinstance(obj, (int, float, str, type(None)))

def FormatObject(obj, depth = 0, itergen = sorted):
    info = []

    space = '  ' * depth
    if _IsBaseObject(obj):
        info.append('%s%r\n' % ('', obj))
        return info

    if isinstance(obj, (list, tuple)):
        info.extend(FormatList(obj, depth, itergen))
        return info

    if depth != 0:
        info.append('\n')

    if isinstance(obj, dict):
        info.extend(FormatDictionary(obj, depth, itergen))
        return info

    if isinstance(obj, (bytes, bytearray)):
        info.append('%s%r\n' % (space, bytes(obj)))
        return info

    for attr in itergen(dir(obj)):
        if attr.startswith('_'):
            continue

        attrv = getattr(obj, attr)
        if hasattr(attrv, '__call__'):
            continue

        if _IsBaseObject(attrv):
            info.append('%s%r = ' % (space, attr))
        else:
            info.append('%s[%r]' % (space, attr))

        if isinstance(attrv, (list, tuple)):
            info.extend(FormatList(attrv, depth + 1, itergen))
        else:
            info.extend(FormatObject(getattr(obj, attr), depth + 1, itergen))

    return info

def FormatList(obj, depth = 0, itergen = sorted):
    info = []
    space = depth * '  '

    if len(obj) == 0:
        info.append('\n')
        return info

    if depth != 0:
        info.append('\n')

    for i, x in enumerate(obj):
        if isinstance(x, (list, tuple)):
            info.append('%s[%04d] =' % (space, i))
            info.extend(FormatList(x, depth + 1, itergen))
        else:
            info.append('%s[%04d] = ' % (space, i))
            info.extend(FormatObject(x, depth + 1, itergen))

    return info

def FormatDictionary(obj, depth = 0, itergen = sorted):
    info = []
    space = '  ' * depth

    if isinstance(obj, OrderedDict):
        itergen = iter

    for k in itergen(obj):
        try:
            v = obj.getlist(k)
        except AttributeError:
            v = obj.get(k)

        if isinstance(v, dict):
            info.append('%s%r:\n' % (space, k))
            info.extend(FormatDictionary(v, depth + 1, itergen))

        elif isinstance(v, (list, tuple)):
            info.append('%s%r =' % (space, k))
            info.extend(FormatList(v, depth + 1, itergen))

        else:
            info.append('%s%r = ' % (space, k))
            info.extend(FormatObject(v, depth + 1, itergen))

    if depth == 0:
        info.append('\n')

    return info
