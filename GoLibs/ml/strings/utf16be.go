package strings

import (
    "unicode/utf8"
)

func utf16BeEncode(table *codePageTableInfo, str String) (bytes []byte) {
    utf8String := string(str)

    for len(utf8String) > 0 {
        r, size := utf8.DecodeRuneInString(utf8String)
        utf8String = utf8String[size:]
        bytes = append(bytes, byte(r >> 8))
        bytes = append(bytes, byte(r))
    }

    return
}

func utf16BeDecode(table *codePageTableInfo, bytes []byte) String {
    runes := []rune{}
    for _, r := range bytesToUInt16Array(bytes) {
        runes = append(runes, rune((r >> 8) | (r << 8)))
    }

    return String(string(runes))
}

func init() {
    cptable[CP_UTF16_BE] = codePageTableInfo{
                        CodePage    : CP_UTF16_BE,
                        initialized : true,
                        encode      : utf16BeEncode,
                        decode      : utf16BeDecode,
                    }
}
