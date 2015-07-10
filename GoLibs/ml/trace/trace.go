package trace

import (
    . "fmt"
    "runtime"
    "path/filepath"
)

const (
    depth = 10
)

func getCaller(skip int) (name, file string, line int) {
    pc, file, line, _ := runtime.Caller(skip)

    // file = filepath.Base(file)
    name = filepath.Base(runtime.FuncForPC(pc).Name())
    return
}

func raiseimpl(v interface{}) {
    var exp *Exception

    name, _, line := getCaller(3)

    switch e := v.(type) {
        case *Exception:
            exp = e

        default:
            exp = &Exception{
                        Message : Sprintf("(traceback)\n%s\n[%s:%d] %v\n", stack(3, depth), name, line, v),
                        Value   : v,
                    }
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
            const skip = 2
            name, _, line := getCaller(skip)
            return &Exception{
                        Message : Sprintf("%s\n[%s:%d] %v\n", stack(skip, depth), name, line, e),
                        Value   : e,
                    }
    }
}
