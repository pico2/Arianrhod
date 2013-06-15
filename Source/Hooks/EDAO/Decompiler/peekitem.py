from ml import *
from BaseType import *

def getname(name):
    filter = \
    [
        (' ', ''),
        ('-', ''),
        ('_', ''),
        ('　', ''),
        ('·', ''),
        ('＋', '_Plus'),
        ('％', ''),
        ('⑿', '12'),
        ('『', '_'),
        ('』', ''),
        ('「', '_'),
        ('」', ''),
        ('！', ''),

        ('①', '1'),
        ('②', '2'),
        ('③', '3'),
        ('④', '4'),
        ('⑤', '5'),
        ('⑥', '6'),
        ('⑦', '7'),
        ('⑧', '8'),
        ('⑨', '9'),
        ('⑩', '10'),
        ('⑾', '11'),
    ]
    for f in filter:
        name = name.replace(f[0], f[1])

    return name

def peek(file):
    fs = BytesStream()
    fs.open(file)

    fs.seek(fs.ushort())

    offsetlist = []
    minoffset = 0xFFFFFFFF
    while True:
        if fs.tell() >= minoffset:
            break

        offset = fs.ushort()
        minoffset = min(minoffset, offset)
        offsetlist.append(offset)

    offsetmap = {}
    itemmap = {}
    itemidmap = {}

    for offset in offsetlist:
        if offset in offsetmap:
            continue

        offsetmap[offset] = True

        fs.seek(offset)
        id = fs.ulong()

        if id in itemidmap:
            continue

        itemidmap[id] = True

        nameoffset = fs.ushort()
        fs.seek(nameoffset)
        name = getname(fs.astr())

        if name not in itemmap:
            itemmap[name] = []

        itemmap[name].append(id)

    items = []
    for name in sorted(itemmap):
        idlist = itemmap[name]
        if len(idlist) == 1:
            items.append((id, name))
            continue

        for id in idlist:
            items.append((id, '%s_%X' % (name, id)))

    return items


def main():
    items = peek('J:\\Falcom\\ED_AO\\data\\text\\t_ittxt._dt')
    items += peek('J:\\Falcom\\ED_AO\\data\\text\\t_ittxt2._dt')

    lines = ['#encoding=utf8', '']
    for x in items:
        name = x[1]
        name = getname(name)
        if name == '':
            name = 'Item_%X' % x[0]
        else:
            name = 'Item_%s' % name

        lines.append('%s = 0x%X' % (ljust_cn(name, 30), x[0]))
    open('ItemIdEDAO.py', 'wb').write('\r\n'.join(lines).encode('UTF8'))

TryInvoke(main)
