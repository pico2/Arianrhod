package utility

import (
    . "ml/strings"
    "bytes"
)

func BytesToString(buf []byte) String {
    null := bytes.Index(buf, []byte{0})
    if null >= 0 {
        buf = buf[:null]
    }

    return Decode(buf, ENCODING)
}
