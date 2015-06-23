package main

import (
    . "ml"
    . "fmt"
    . "ml/dict"
    "os"
    "ml/logging"
    "ml/syscall"
)

func testString() (r int) {
    s := Str("fuck")

    s = `ffa fuck2 `
    s += `fuck`

    Printf("%+v\n", s)
    Println((&s).Replace("f", "fuck you f"))
    Println(s.Index("k"))
    Println(s.HasPrefix("fuck"))
    Println(s.ToUpper())
    Println(s.ToLower())
    Println(s == "Fuck2")
    Printf("%c\n", s[0])
    Printf("'%+v'\n", s.Trim("f"))

    r = 123

    return
}

func testArray() {
    arr := Array(1, 2, 3, 4)

    arr.Append(1, 5, 432, "fuck", 1.555, 73.88)
    arr.Remove("fuck")

    for _, v := range arr {
        switch t := v.(type) {
            case string:
                Printf("v:%v\n", t)

            default:
                Println(v)
        }
    }
}

func testNamedReturn() (i int, s string) {
    i, s = 1, "2"
    return
    return 0, "1"
}

func testDict() {
    x := Dict{1 : 2, "fuck" : 3.33}
    Println(x)
    _ = x
}

func testLogger() {
    logger := logging.New("fuck")

    // _ = logger
    // logger.SetLevel(20)

    logger.Debug("fuck中文")
}

func testMisc(a interface{}) {
    xx := uintptr(a.(int))
    print(xx)

    _ = syscall.Call
    // syscall.Call(uintptr(0), 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
}

func main() {
    testString()
    Println()

    testArray()
    Println()

    testNamedReturn()
    Println()

    testDict()
    Println()

    testLogger()
    Println()

    for _, v := range os.Args {
        Println(v)
    }
    Println()

    testMisc(1)
    Println()

    Console.Pause()
}
