package main

import (
    . "ml"
    . "fmt"
    . "ml/dict"
    . "ml/array"
    "ml/console"
    "ml/logging"
    "ml/strings"
    "ml/preference"
    "ml/net/http"
    "unicode/utf8"
    "net/url"
    "os"
    "strconv"
    "bytes"
    "io"
)

import "database/sql"
import _ "github.com/go-sql-driver/mysql"

func testString() (r int) {
    s := Str("fuck")

    s = `中文`
    s += `fuck`

    u16le := s.Encode(strings.CP_UTF16_LE)
    for _, ch := range u16le {
        Printf("%02X ", ch)
    }
    Println()

    u16be := s.Encode(strings.CP_UTF16_BE)
    for _, ch := range u16be {
        Printf("%02X ", ch)
    }
    Println()

    Printf("%+v\n", s)
    Println((&s).Replace("f", "fuck you f"))
    Println(s.Index("k"))
    Println(s.StartsWith("fuck"))
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
    arr := Array{1, 2, 3, 4}

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
    Println("fuck mm", mm, len(mm))

    testDict2(PARAMS{"1": 2})

    Println(x)
    Println(x["fuck"])
    // Println(x.Get)
    _ = x
}

func testLogger() {
    var w io.WriteCloser

    w = os.Stdout

    Println("w == os.Stdout", w == os.Stdout)

    Println("ModeDir = ", os.ModeDir)
    Println("ModeAppend = ", os.ModeAppend)
    Println("ModeExclusive = ", os.ModeExclusive)
    Println("ModeTemporary = ", os.ModeTemporary)
    Println("ModeSymlink = ", os.ModeSymlink)
    Println("ModeDevice = ", os.ModeDevice)
    Println("ModeNamedPipe = ", os.ModeNamedPipe)
    Println("ModeSocket = ", os.ModeSocket)
    Println("ModeSetuid = ", os.ModeSetuid)
    Println("ModeSetgid = ", os.ModeSetgid)
    Println("ModeCharDevice = ", os.ModeCharDevice)
    Println("ModeSticky = ", os.ModeSticky)

    logger := logging.NewLogger("fuck")
    logger.LogToFile()

    // _ = logger
    // logger.SetLevel(20)

    logger.Debug("fuck中文")
}

func testMisc(a interface{}) {
    switch 1 {
        case 1:
            defer Println("defer scope")
    }

    xx := uintptr(a.(int))
    Println(xx)

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

    conv := func (r io.Reader) {
        // rc, ok := r.(io.ReadCloser)
        Println("io.Reader", r)
        if r != nil {
            Println("r is not nil", r)
        }
    }

    var b *bytes.Buffer
    var r io.Reader
    b = nil
    r = b

    _ = b

    conv(r)
}

func testNet() {
    session, _ := http.NewSession()

    session.SetProxy("localhost", 6789)

    session.SetHeaders(Dict{
        "Accept"            : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding"   : "gzip, deflate",
        "Accept-Language"   : "zh-CN,en-US;q=0.8,en;q=0.5,zh-HK;q=0.3",
        "User-Agent"        : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:42.0) Gecko/20100101 Firefox/42.0",
        // "Content-Type"      : "application/x-www-form-urlencoded",
        "Connection"        : "keep-alive",
    })

    resp, err := session.Get("http://www.taobao.com/")

    if err != nil {
        Println(err)
        return
    }

    Println(resp.Encoding)
    Println(resp.Header.Get("Content-Type"))

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

type Preferences struct {
    MaxAsyncTask    int         `json:"maxAsyncTask,omitempty"`
    MaxWorkers      int         `json:"maxWorkers,omitempty"`

    Proxy struct {
        Port        int         `json:"Port,omitempty"`
        User        string      `json:"User,omitempty"`
        Password    string      `json:"Password,omitempty"`
    }

    ProxyServer struct {
        Host        string      `json:"Host,omitempty"`
        Port        int         `json:"Port,omitempty"`
        Port2       int         `json:"Port2,omitempty"`
    }

    Database struct {
        Host        string      `json:"Host,omitempty"`
        User        string      `json:"User,omitempty"`
        Password    string      `json:"Password,omitempty"`
        Db          string      `json:"db,omitempty"`
    }
}

func testSql() {
    pref := &Preferences{}

    err := preference.LoadFile(`D:\Desktop\xx\AppleIdRegister\Preferences.json`, pref)
    if err != nil {
        Println(err)
        return
    }

    dsn := Sprintf(
                "%s:%s@tcp(%s:3306)/%s",
                pref.Database.User,
                pref.Database.Password,
                pref.Database.Host,
                pref.Database.Db,
            )

    Println(dsn)

    db, err := sql.Open("mysql", dsn)

    if err != nil {
        Println(err)
        return
    }

    err = db.Ping()
    Println("ping =", err)
    if err != nil {
        return
    }

    rows, err := db.Query("SELECT COUNT(id) from appstore_buydata_appleid WHERE `status` = 4")
    Println("exec =", err)
    if err != nil {
        return
    }

    defer rows.Close()

    for rows.Next() {
        var name string
        if err := rows.Scan(&name); err != nil {
            Println(err)
        }
        Printf("%s\n", name)
    }

    if err := rows.Err(); err != nil {
        Println(err)
    }
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

    testSql()
    Println()

    console.Pause("done")
}
