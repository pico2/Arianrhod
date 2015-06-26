package main

import (
    . "ml"
    . "fmt"
    . "ml/dict"
    "ml/logging"
    "ml/syscall"
    "ml/strings"
    "ml/net/http"
    "unicode/utf8"
    "net/url"
    "os"
    "strconv"
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

    var emptyString string

    Println(emptyString, len(emptyString))

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

type PARAMS map[string]interface{}

func testDict2(params PARAMS) {
    v := 2
    switch 1 {
        case 1:
            Println("is 1")
            fallthrough
        case 2:
            Println("is ", v)
    }

    Println(params)
}

func testDict() {
    x := Dict{1 : 2, "fuck" : 3.33}
    x[2] = 3

    mm := map[int][]int{}

    Println("fuck mm", mm[1])
    mm[1] = append(mm[1], 1)
    Println("fuck mm", mm)

    testDict2(PARAMS{"1": 2})

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

    var i64 uint64
    var i interface{}

    i64 = 12345678901234567890
    i = i64
    switch t := i.(type) {
        case int32:
            Println(Sprintf("%v", t))
    }

    Println(Ucs16String)
    Println(strconv.FormatUint(i64, 10))
}

func testNet() {
    session, _ := http.NewSession()

    resp, err := session.Get(
                    "https://www.baidu.com/fuck",
                    Dict{
                        "params": Dict{
                            "a1": "中文",
                            "a2": "测试",
                        },
                        // "encoding": strings.CP_GBK,
                    },
                )

    Println(err)

    _ = resp
}

func testEncoding() {
    ss := Str("身喰らう蛇")

    Println("orig", ss)

    text := ss.Encode(strings.CP_UTF8)
    for _, ch := range text {
        Printf("%02X ", ch)
    }

    Println()
    Println(strings.Decode(text, strings.CP_UTF8))
    Println()

    text = ss.Encode(strings.CP_SHIFT_JIS)
    for _, ch := range text {
        Printf("%02X ", ch)
    }

    s := string(text)

    Println()

    v := url.Values{}

    v.Set("fuck", s)

    for i := 0; i != len(s); i++ {
        Printf("%02X ", s[i])
    }

    Println()
    Println(v.Encode())
    Println()

    gg := strings.Decode(text, strings.CP_GBK)
    Println(gg)

    gg = strings.Decode(text, strings.CP_SHIFT_JIS)
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
