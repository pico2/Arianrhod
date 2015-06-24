package encoding

import (
    // "io/ioutil"
    // "compress/zlib"
    // "bytes"
)

const (
    MAXIMUM_LEADBYTES   = 12
    SIZE_OF_WCHAR       = 2
    UnicodeNull         = 0
)

const (
    MB_TBL_SIZE         = 256             /* size of MB tables */
    GLYPH_TBL_SIZE      = MB_TBL_SIZE     /* size of GLYPH tables */
    DBCS_TBL_SIZE       = 256             /* size of DBCS tables */
    GLYPH_HEADER        = 1               /* size of GLYPH table header */
    DBCS_HEADER         = 1               /* size of DBCS table header */
    LANG_HEADER         = 1               /* size of LANGUAGE file header */
    UP_HEADER           = 1               /* size of UPPERCASE table header */
    LO_HEADER           = 1               /* size of LOWERCASE table header */
)

type codePageTableInfo struct {
    data []byte
    initialized bool

    CodePage                uint                           // code page number
    MaximumCharacterSize    uint                           // max length (bytes) of a char
    DefaultChar             uint                           // default character (MB)
    UniDefaultChar          uint                           // default character (Unicode)
    TransDefaultChar        uint                           // translation of default char (Unicode)
    TransUniDefaultChar     uint                           // translation of Unic default char (MB)
    DBCSCodePage            bool                            // Non 0 for DBCS code pages
    LeadByte                [MAXIMUM_LEADBYTES]byte         // lead byte ranges
    MultiByteTable          []uint16                        // pointer to MB translation table
    WideCharTable           []uint16                        // pointer to WC translation table
    DBCSRanges              uint                            // pointer to DBCS ranges
    TranslateTable          []uint16                        // pointer to DBCS offsets

    // MultiByteTableAddress   uintptr
    // WideCharTableAddress    uintptr
    // DBCSRangesAddress       uintptr
    // DBCSOffsetsAddress      uintptr
}

func (self *codePageTableInfo) initialize() {
    if self.initialized {
        return
    }

    // b := bytes.NewReader(self.data)
    // r, err := zlib.NewReader(b)
    // if err != nil {
    //     panic(err)
    // }

    // self.data, err = ioutil.ReadAll(r)
    // r.Close()

    // if err != nil {
    //     panic(err)
    // }

    // self.initCodePageTable()

    self.initialized = true
}
