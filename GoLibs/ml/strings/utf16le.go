package strings

import (
    "unicode/utf8"
)

func utf16LeEncode(table *codePageTableInfo, str String) (bytes []byte) {
    utf8String := string(str)

    for len(utf8String) > 0 {
        r, size := utf8.DecodeRuneInString(utf8String)
        utf8String = utf8String[size:]
        bytes = append(bytes, byte(r))
        bytes = append(bytes, byte(r >> 8))
    }

    return
}

func utf16LeDecode(table *codePageTableInfo, bytes []byte) String {
    runes := []rune{}
    for _, r := range bytesToUInt16Array(bytes) {
        runes = append(runes, rune(r))
    }

    return String(string(runes))
}

func init() {
    cptable[CP_UTF16_LE] = codePageTableInfo{
                        CodePage    : CP_UTF16_LE,
                        initialized : true,
                        encode      : utf16LeEncode,
                        decode      : utf16LeDecode,
                    }
}
