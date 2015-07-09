package socket

import (
    "net"
    "time"
)

type Socket interface {
    Connect(host string, port int, timeout time.Duration) error
    Read(n int) (buf []byte, err error)
    Write(buf []byte) (n int, err error)
    Close() error

    LocalAddr() net.Addr
    RemoteAddr() net.Addr

    SetTimeout(t time.Duration)
    SetReadTimeout(t time.Duration)
    SetWriteTimeout(t time.Duration)

    SetDeadline(t time.Time) error
    SetReadDeadline(t time.Time) error
    SetWriteDeadline(t time.Time) error
}
