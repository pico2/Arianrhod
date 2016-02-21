package filestream

import (
    . "ml/trace"
)

func raiseGenericError(err error) {
    if err == nil {
        return
    }

    Raise(NewFileGenericError(err.Error()))
}
