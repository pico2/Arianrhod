from ml import *

ALIGNMENT = 4

def getGoType(obj):
    return {
        int:    'int',
        str:    'string',
        float:  'float64',
    }[type(obj)]

def getMaxLength(obj, indent = 0):
    l = 0

    for k, v in obj.items():
        if isinstance(v, dict):
            l = max(l, getMaxLength(v, indent + ALIGNMENT))
        else:
            l = max(l, len(k))

    return l + indent

def parseObject(obj, adjust, depth = 0):
    lines = []
    pad = ' ' * depth

    for k, v in obj.items():
        if isinstance(v, dict):
            if lines:
                lines.append('')

            s = parseObject(v, adjust - ALIGNMENT, depth + ALIGNMENT)

            o = [
                '%s struct {' % k,
            ]

            o.extend(s)
            o.append('}')

            for l in o:
                lines.append((pad + l).rstrip())

        elif isinstance(v, (list, tuple)):
            raise NotADirectoryError

        else:
            l = '{pad}{field}{type}{tag}'.format(
                    pad     = pad,
                    field   = (k[:1].upper() + k[1:]).ljust(adjust),
                    type    = getGoType(v).ljust(12),
                    tag     = '`json:"%s,omitempty"`' % k,
                )

            lines.append(l)

    return lines

def convert(jsonfile):
    obj = Preferences.LoadPreferences(jsonfile)
    if not obj:
        return

    structName = os.path.splitext(os.path.basename(jsonfile))[0]

    l = getMaxLength(obj)
    l = (l + 1 + ALIGNMENT) & ~3

    s = parseObject(obj, l)

    s = [(' ' * ALIGNMENT + l).rstrip() for l in s]

    s.insert(0, 'type %s struct {' % structName)
    s.append('}')

    print('\n'.join(s))

    return s

def main():
    if len(sys.argv) == 1:
        sys.argv.extend([r'D:\Desktop\xx\AppleIdRegister\Preferences.json'])

    for f in sys.argv[1:]:
        convert(f)
        print()

    PauseConsole()

if __name__ == '__main__':
    TryInvoke(main)
