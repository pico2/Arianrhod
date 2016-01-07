package ituneslib

import (
    "unsafe"
)

func toBytes(buf *byte, size int) []byte {
    data := make([]byte, size)

    if buf != nil {
        p := (*[^uint32(0) >> 1]byte)(unsafe.Pointer(buf))
        copy(data, p[:size])
    }

    return data
}

func toString(buf *byte) string {
    p := (*[^uint32(0) >> 1]byte)(unsafe.Pointer(buf))
    length := 0

    for p[length] != 0 {
        length++
    }

    return string(p[:length])
}

func getStatus(status uintptr) int {
    return int(int32(status))
}
