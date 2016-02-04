package trace

import (
    . "fmt"
    "runtime"
    "bytes"
    "strings"
    "io/ioutil"
)

var (
    dunno           = []byte("???")
    centerDot       = []byte("·")
    dot             = []byte(".")
    slash           = []byte("/")
    mainFuncName    = []byte("main")
)

func source(lines [][]byte, n int) []byte {
    if n < 0 || n >= len(lines) {
        return dunno
    }
    return bytes.Trim(lines[n], " \t")
}

func function(n string) []byte {
    name := []byte(n)

    if lastslash := bytes.LastIndex(name, slash); lastslash >= 0 {
        name = name[lastslash+1:]
    }

    if period := bytes.Index(name, dot); period >= 0 {
        name = name[period+1:]
    }

    return bytes.Replace(name, centerDot, dot, -1)
}

func stack(skip, depth int) []byte {
    buf := new(bytes.Buffer)

    var lines [][]byte
    var traceback []string
    var lastFile string

    if false {
        callers := make([]uintptr, depth)
        n := runtime.Callers(skip, callers)

        callers = callers[:n]

        for _, pc := range callers {
            f := runtime.FuncForPC(pc)
            file, line := f.FileLine(pc)
            funcName := function(f.Name())

            Fprintf(buf, "%s:%d (0x%x)\n", file, line, pc)

            if Config.ReadSource {
                if file != lastFile {
                    data, err := ioutil.ReadFile(file)
                    if err != nil {
                        continue
                    }
                    lines = bytes.Split(data, []byte{'\n'})
                    lastFile = file
                }

                Fprintf(buf, "\t%s: %s\n", funcName, source(lines, line - 1))
            } else {
                Fprintf(buf, "\t%s\n", funcName)
            }

            if bytes.Equal(funcName, mainFuncName) {
                break
            }
        }

    } else {
        depth += skip
        for i := skip; i < depth; i++ {
            pc, file, line, ok := runtime.Caller(i)
            if !ok {
                break
            }

            funcName := function(runtime.FuncForPC(pc).Name())

            text := Sprintf("%s:%d (0x%x)\n", file, line, pc)

            // Fprintf(buf, "%s:%d (0x%x)\n", file, line, pc)

            if Config.ReadSource {
                if file != lastFile {
                    data, err := ioutil.ReadFile(file)
                    if err != nil {
                        continue
                    }
                    lines = bytes.Split(data, []byte{'\n'})
                    lastFile = file
                }

                text += Sprintf("\t%s: %s", funcName, source(lines, line - 1))

                // Fprintf(buf, "\t%s: %s\n", funcName, source(lines, line - 1))

            } else {
                text += Sprintf("\t%s", funcName)
                // Fprintf(buf, "\t%s\n", funcName)
            }

            traceback = append(traceback, text)

            if bytes.Equal(funcName, mainFuncName) {
                break
            }
        }
    }

    length := len(traceback)
    for i := 0; i != length / 2; i++ {
        traceback[i], traceback[length - i - 1] = traceback[length - i - 1], traceback[i]
    }

    traceback = append(traceback, "")

    return []byte(strings.Join(traceback, "\n"))
    // return buf.Bytes()
}
