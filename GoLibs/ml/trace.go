package ml

import (
    . "fmt"
    "runtime"
    "path/filepath"
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
    // The name includes the path name to the package, which is unnecessary
    // since the file name is already included.  Plus, it has center dots.
    // That is, we see
    //  runtime/debug.*T路ptrmethod
    // and want
    //  *T.ptrmethod
    // Since the package path might contains dots (e.g. code.google.com/...),
    // we first remove the path prefix if there is one.
    if lastslash := bytes.LastIndex(name, slash); lastslash >= 0 {
        name = name[lastslash+1:]
    }
    if period := bytes.Index(name, dot); period >= 0 {
        name = name[period+1:]
    }
    name = bytes.Replace(name, centerDot, dot, -1)
    return name
}
// stack implements Stack, skipping 2 frames
func stack(skip int) []byte {
    buf := new(bytes.Buffer) // the returned data
    // As we loop, we open files and read them. These variables record the currently
    // loaded file.
    var lines [][]byte
    var lastFile string
    for i := skip; ; i++ { // Caller we care about is the user, 2 frames up
        pc, file, line, ok := runtime.Caller(i)
        if !ok {
            break
        }
        // Print this much at least.  If we can't find the source, it won't show.
        Fprintf(buf, "%s:%d (0x%x)\n", file, line, pc)
        if file != lastFile {
            data, err := ioutil.ReadFile(file)
            if err != nil {
                continue
            }
            lines = bytes.Split(data, []byte{'\n'})
            lastFile = file
        }
        line-- // in stack trace, lines are 1-indexed but our array is 0-indexed
        Fprintf(buf, "\t%s: %s\n", function(pc), source(lines, line))
    }
    return buf.Bytes()
}

func getCaller() (name, file string, line int) {
    pc, file, line, _ := runtime.Caller(2)

    // file = filepath.Base(file)
    name = filepath.Base(runtime.FuncForPC(pc).Name())
    return
}

func Panic(x string) {
    name, file, line := getCaller()

    x = Sprintf("%s\n[%s][%s:%d] %s\n", stack(2), file, name, line, x)
    panic(x)
}
