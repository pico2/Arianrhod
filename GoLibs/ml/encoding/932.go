package encoding

func init() {
    cptable[932] = codePageTableInfo{
                        CodePage                : 932,
                        MaximumCharacterSize    : 0x2,
                        DefaultChar             : 0x3F,
                        UniDefaultChar          : 0x30FB,
                        TransDefaultChar        : 0x3F,
                        TransUniDefaultChar     : 0x8145,
                        DBCSCodePage            : true,
                        []byte[]{0x81,0x9F,0xE0,0xFC,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0},
                    }
}