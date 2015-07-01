package trace

import (
    . "fmt"
    "runtime"
    "bytes"
    "io/ioutil"
)

var (
    dunno     = []byte("???")
    centerDot = []byte("·")
    dot       = []byte(".")
    slash     = []byte("/")
)

func source(lines [][]byte, n int) []byte {
    if n < 0 || n >= len(lines) {
        return dunno
    }
    return bytes.Trim(lines[n], " \t")
}

func function(pc uintptr) []byte {
    fn := runtime.FuncForPC(pc)
    if fn == nil {
        return dunno
    }
    name := []byte(fn.Name())

    if lastslash := bytes.LastIndex(name, slash); lastslash >= 0 {
        name = name[lastslash+1:]
    }

    if period := bytes.Index(name, dot); period >= 0 {
        name = name[period+1:]
    }

    return bytes.Replace(name, centerDot, dot, -1)
}

func stack(skip int) []byte {
    buf := new(bytes.Buffer)

    var lines [][]byte
    var lastFile string

    for i := skip; ; i++ {
        pc, file, line, ok := runtime.Caller(i)
        if !ok {
            break
        }

        Fprintf(buf, "%s:%d (0x%x)\n", file, line, pc)
        if file != lastFile {
            data, err := ioutil.ReadFile(file)
            if err != nil {
                continue
            }
            lines = bytes.Split(data, []byte{'\n'})
            lastFile = file
        }

        funcName := function(pc)
        Fprintf(buf, "\t%s: %s\n", funcName, source(lines, line - 1))

        if bytes.Equal(funcName, []byte("main")) {
            break
        }
    }

    return buf.Bytes()
}
