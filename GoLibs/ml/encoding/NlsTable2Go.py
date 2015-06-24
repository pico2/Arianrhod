from ml import *
import zlib

MAXIMUM_LEADBYTES   = 12
MB_TBL_SIZE         = 256
GLYPH_TBL_SIZE      = MB_TBL_SIZE
DBCS_TBL_SIZE       = 256
GLYPH_HEADER        = 1
DBCS_HEADER         = 1
LANG_HEADER         = 1
UP_HEADER           = 1
LO_HEADER           = 1

class CPTABLEINFO(Structure):
    _fields_ = [
        ('CodePage',                USHORT),
        ('MaximumCharacterSize',    USHORT),
        ('DefaultChar',             USHORT),
        ('UniDefaultChar',          USHORT),
        ('TransDefaultChar',        USHORT),
        ('TransUniDefaultChar',     USHORT),
        ('DBCSCodePage',            USHORT),
        ('LeadByte',                BYTE * MAXIMUM_LEADBYTES),
        ('MultiByteTable',          ULONG_PTR),
        ('WideCharTable',           ULONG_PTR),
        ('DBCSRanges',              ULONG_PTR),
        ('DBCSOffsets',             ULONG_PTR),
    ]

PCPTABLEINFO = ctypes.POINTER(CPTABLEINFO)

def RtlInitCodePageTable(table):
    info = CPTABLEINFO()
    buf = (BYTE * len(table)).from_buffer(table)

    windll.ntdll.RtlInitCodePageTable(byref(buf), PCPTABLEINFO(info))

    return info

def main():
    if len(sys.argv) == 1:
        sys.argv.append(r"D:\Dev\go\pkgs\src\ml\encoding\C_932.NLS")

    for f in sys.argv[1:]:
        table = bytearray(open(f, 'rb').read())

        info = RtlInitCodePageTable(table)

        print('CodePage             = %s' % info.CodePage)
        print('MaximumCharacterSize = %X' % info.MaximumCharacterSize)
        print('DefaultChar          = %X' % info.DefaultChar)
        print('UniDefaultChar       = %X' % info.UniDefaultChar)
        print('TransDefaultChar     = %X' % info.TransDefaultChar)
        print('TransUniDefaultChar  = %X' % info.TransUniDefaultChar)
        print('DBCSCodePage         = %s' % info.DBCSCodePage)
        print('LeadByte             = %s' % bytes(info.LeadByte))
        print('MultiByteTable       = %s' % (info.MultiByteTable))
        print('WideCharTable        = %s' % (info.WideCharTable))
        print('DBCSRanges           = %s' % (info.DBCSRanges))
        print('DBCSOffsets          = %s' % (info.DBCSOffsets))

        cp = info.CodePage

        src = [
            'package encoding',
            '',
            'func init() {',
            '    cptable[%d] = codePageTableInfo{' % cp,
            '                        CodePage                : %d,' % cp,
            '                        MaximumCharacterSize    : 0x%X,' % info.MaximumCharacterSize,
            '                        DefaultChar             : 0x%X,' % info.DefaultChar,
            '                        UniDefaultChar          : 0x%X,' % info.UniDefaultChar,
            '                        TransDefaultChar        : 0x%X,' % info.TransDefaultChar,
            '                        TransUniDefaultChar     : 0x%X,' % info.TransUniDefaultChar,
            '                        DBCSCodePage            : %s,' % (info.DBCSCodePage and 'true' or 'false'),
        ]

        padding = '                        '

        LeadByte = '[]byte[]{%s},' % ','.join(['0x%X' % ch for ch in bytes(info.LeadByte)])
        src.append(padding + LeadByte)

        MultiByteTable = bytes((BYTE * MB_TBL_SIZE).from_address(int(info.MultiByteTable)))
        ibp()

        src.extend([
            '                    }',
            '}',
        ])

        f = os.path.dirname(f) + '\\%d.go' % cp
        print(f)
        open(f, 'wb').write('\n'.join(src).encode('UTF8'))

if __name__ == '__main__':
    TryInvoke(main)
