package main

import (
    . "ml"
    . "fmt"
    . "ml/dict"
    "os"
    "ml/logging"
    "ml/syscall"
    // "ml/net/http"
    "ml/encoding"
    "unicode/utf8"
)

func testString() (r int) {
    s := Str("fuck")

    s = `中文`
    s += `fuck`

    Printf("%+v\n", s)
    Println((&s).Replace("f", "fuck you f"))
    Println(s.Index("k"))
    Println(s.HasPrefix("fuck"))
    Println(s.ToUpper())
    Println(s.ToLower())
    Println(s == "Fuck2")

    str := s
    Println(str, "bytes =", len(str))
    Println(str, "runes =", str.Length())

    for c := range str {
        Println(c)
    }

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
    x[2] = 3

    Println(x)
    Println(x["fuck"])
    // Println(x.Get)
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
    Println(xx)

    _ = syscall.Call
    // syscall.Call(uintptr(0), 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

    Ucs16String := []uint16{}
    UnicodeString := "中文"

    for len(UnicodeString) > 0 {
        r, size := utf8.DecodeRuneInString(UnicodeString)
        UnicodeString = UnicodeString[size:]

        Ucs16String = append(Ucs16String, uint16(r))
    }

    Println(Ucs16String)
}

func testNet() {
    // session, _ := http.NewSession()

    // resp, err := session.Get(
    //                 "https://www.baidu.com/",
    //                 Dict{
    //                     "params": Dict{
    //                         "中": "文",
    //                     },
    //                 },
    //             )

    // Println(err, resp)

    // _ = session
}

func testEncoding() {
    gbk := encoding.GetEncoder(encoding.CP_SHIFT_JIS)

    text := gbk.Encode("身喰らう蛇")
    for _, ch := range text {
        Printf("%02X ", ch)
    }

    Println()

    gbk = encoding.GetEncoder(encoding.CP_GBK)

    gg := gbk.Decode(text)
    Println(gg)
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

    testNet()
    Println()

    testEncoding()
    Println()

    Console.Pause()
}
