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

func getCaller() (name, file string, line int) {
    pc, file, line, _ := runtime.Caller(2)

    // file = filepath.Base(file)
    name = filepath.Base(runtime.FuncForPC(pc).Name())
    return
}

func RaiseError(e error) {
    if e != nil {
        Raise(e)
    }
}

func Raise(v interface{}) {
    name, _, line := getCaller()
    exp := &Exception{
                Message : Sprintf("%s\n[%s:%d] %v\n", stack(2), name, line, v),
                Value   : v,
            }

    panic(exp)
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
