package binary

import (
    . "ml/trace"
    "encoding/binary"
    "bytes"
)

func IntToBytes(data interface{}, length int, byteOrder binary.ByteOrder) []byte {
    w := bytes.NewBuffer(nil)
    err := binary.Write(w, byteOrder, data)
    RaiseIf(err)

    b := w.Bytes()
    if len(b) >= length {
        return b
    }

    buf := make([]byte, length)
    copy(buf, b)

    return buf
}
