package base64

import (
    . "ml/trace"
)

type Base64Error struct {
    Message string
}

func raiseBase64Error(err error) {
    if err == nil {
        return
    }

    Raise(NewBase64Error(err.Error()))
}

func NewBase64Error(msg string) *Base64Error {
    return &Base64Error{msg}
}
