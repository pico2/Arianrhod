package socket

import (
    . "ml/trace"
)

type SocketError struct {
    Message string
}

func RaiseSocketError(err error) {
    if err == nil {
        return
    }

    Raise(NewSocketError(err.Error()))
}

func NewSocketError(msg string) *SocketError {
    return &SocketError{msg}
}

func (self *SocketError) String() string {
    return self.Message
}
