package socket

import (
    . "fmt"
    "net"
    "time"
)

var (
    AlreadyConnectedError   = Errorf("already connected to server")
)

type TcpSocket struct {
    conn            net.Conn
    ReadTimeout     time.Duration
    WriteTimeout    time.Duration
}

func NewTcpSocket() Socket {
    tcp := &TcpSocket{}
    return tcp
}

func (self *TcpSocket) Connect(host string, port int, timeout time.Duration) (err error) {
    if self.conn != nil {
        return AlreadyConnectedError
    }

    switch {
        case timeout <= 0:
            self.conn, err = net.Dial("tcp", Sprintf("%s:%d", host, port))

        default:
            self.conn, err = net.DialTimeout("tcp", Sprintf("%s:%d", host, port), timeout)
    }

    if err != nil {
        return err
    }

    return nil
}

func (self *TcpSocket) Read(n int) (buf []byte, err error) {
    buf = make([]byte, n)

    if self.ReadTimeout > 0 {
        self.conn.SetReadDeadline(time.Now().Add(self.ReadTimeout))
    }

    n, err = self.conn.Read(buf)
    return buf[:n], err
}

func (self *TcpSocket) Write(buf []byte) (n int, err error) {
    if self.WriteTimeout > 0 {
        self.conn.SetWriteDeadline(time.Now().Add(self.WriteTimeout))
    }

    return self.conn.Write(buf)
}

func (self *TcpSocket) Close() (err error) {
    if self.conn != nil {
        err = self.conn.Close()
        self.conn = nil
    }

    return
}

func (self *TcpSocket) LocalAddr() net.Addr {
    return self.conn.LocalAddr()
}

func (self *TcpSocket) RemoteAddr() net.Addr {
    return self.conn.RemoteAddr()
}

func (self *TcpSocket) SetTimeout(t time.Duration) {
    self.SetReadTimeout(t)
    self.SetWriteTimeout(t)
}

func (self *TcpSocket) SetReadTimeout(t time.Duration) {
    self.ReadTimeout = t
}

func (self *TcpSocket) SetWriteTimeout(t time.Duration) {
    self.WriteTimeout = t
}

func (self *TcpSocket) SetDeadline(t time.Time) error {
    return self.conn.SetDeadline(t)
}

func (self *TcpSocket) SetReadDeadline(t time.Time) error {
    self.SetTimeout(0)
    return self.conn.SetReadDeadline(t)
}

func (self *TcpSocket) SetWriteDeadline(t time.Time) error {
    self.SetTimeout(0)
    return self.conn.SetWriteDeadline(t)
}
