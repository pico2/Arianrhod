package trace

import (
    . "fmt"
    "runtime"
    "path/filepath"
)

type Exception struct {
    Message string
    Value   interface{}
}

func (self *Exception) String() string {
    return self.Message
}

func getCaller(skip int) (name, file string, line int) {
    pc, file, line, _ := runtime.Caller(skip)

    // file = filepath.Base(file)
    name = filepath.Base(runtime.FuncForPC(pc).Name())
    return
}

func raiseimpl(v interface{}) {
    name, _, line := getCaller(3)
    exp := &Exception{
                Message : Sprintf("%s\n[%s:%d] %v\n", stack(3), name, line, v),
                Value   : v,
            }

    panic(exp)
}

func RaiseIf(err error) {
    if err != nil {
        raiseimpl(err)
    }
}

func Raise(v interface{}) {
    raiseimpl(v)
}

func Catch(exp interface{}) *Exception {
    switch e := exp.(type) {
        case *Exception:
            return e

        case nil:
            return nil

        default:
            return &Exception{
                        Message : Sprintf("%v", e),
                        Value   : e,
                    }
    }
}
