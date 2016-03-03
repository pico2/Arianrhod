package main

import (
    . "fmt"
    . "ml/strings"
    . "ml/trace"
    . "ml/dict"
    "./pinyin"
    "ml/random"
    "os"
    "time"
    "syscall"
    "sync"
    "io/ioutil"
    "github.com/PuerkitoBio/goquery"
    "ml/uuid"
    "ml/encoding/binary"
    "ml/encoding/json"
    "ml/net/socket"
    "ml/net/http"
    "ml/pprof"
)

func genacc() {
    py := [][]string{}
    json.Unmarshal([]byte(pinyin.Json), &py)

    f, _ := os.Open("domains.txt")
    bytes, _ := ioutil.ReadAll(f)
    f.Close()

    domains := String(bytes).SplitLines()

    // names := []string{}
    nameset := map[string]bool{}

    target  := 1000000
    perline := 30000
    index   := 0

    names := []String{}

    for i := 0; i != target; i++ {
        name := ""
        for n := random.IntRange(1, 5); n > 0; {
            p := py[random.ChoiceIndex(py)][1]
            if len(p) > 2 {
                continue
            }

            name += p
            n--
        }

        name += Sprintf("%d@%s", random.IntRange(1000, 100000), random.Choice(domains).(String))
        if nameset[name] {
            i--
            continue
        }

        nameset[name] = true
        names = append(names, String(name))

        switch {
            case i + 1 == target,
                 i != 0 && i % perline == 0:
                 f, _ = os.Create(Sprintf("names%d.txt", index))
                 f.WriteString("INSERT IGNORE INTO appstore_buydata_appleid (username) VALUES (\"")
                 f.WriteString(string(String("\"),(\"").Join(names)))
                 f.WriteString("\");\n")

                 f.Close()

                 index++
                 names = []String{}
        }
    }
}

func main() {
    // pprof.Start()

    // wg := sync.WaitGroup{}

    // for i := 0; i < 1000; i++ {
    //     wg.Add(1)
    //     go func() {
    //         h := http.NewSession()
    //         h.DefaultOptions.AutoRetry = true
    //         // h.SetProxy("localhost", 6789)
    //         // h.SetTimeout(time.Second)
    //         defer wg.Done()
    //         defer h.Close()
    //         // Try(func() {
    //             h.Get("https://init.itunes.apple.com/bag.xml?ix=5&ign-bsn=1")
    //         // })

    //         // time.Sleep(time.Second * 10)

    //     }()
    // }

    // wg.Wait()

    // time.Sleep(time.Second * 15)

    // pprof.Stop()

    // // pprof.Lookup("goroutine").WriteTo(os.Stdout, 0)

    // syscall.Syscall(0, 0, 0, 0, 0)

    tcp := socket.NewTcpSocket()
    tcp.SetSocks5Proxy("localhost", 8000, nil)
    tcp.Connect("ip.taobao.com", 80, time.Second)

    Println("Connect done")

    raw := `POST http://ip.taobao.com/service/getIpInfo2.php HTTP/1.1
Host: ip.taobao.com
Connection: keep-alive
Content-Length: 7
Cache-Control: max-age=0
Accept: */*
Origin: http://ip.taobao.com
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Referer: http://ip.taobao.com/
Accept-Encoding: text
Accept-Language: en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4
Cookie: thw=cn; l=AuHh397aQko-bp/6FWKb3JWYcbf6k1WG; uc3=sg2=BqQh7DSZz7N7ZPPvcbOqCgJW2buIOxHCpMGEJ0S1qTs%3D&nk2=qjBd6OnyVBZVZhqvfGQ%3D&id2=WvEDJwaVEqaa&vt3=F8dASch8AdG9T6MXoBs%3D&lg2=UtASsssmOIJ0bQ%3D%3D; uss=VFCvO2FtLewdzwPIR3Jz%2BC1UvkhR23ZCJGfJJnhJFzUdmhB9MrQl6Pc1fg%3D%3D; lgc=%5Cu86C7%5Cu4E4B%5Cu4F7F%5Cu5F92%5Cu7B2C%5Cu96F6%5Cu67F1; tracknick=%5Cu86C7%5Cu4E4B%5Cu4F7F%5Cu5F92%5Cu7B2C%5Cu96F6%5Cu67F1; _cc_=V32FPkk%2Fhw%3D%3D; tg=0; mt=ci=5_1&cyk=1_1; t=47968250fcc0773919460fb997a693b9; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; PHPSESSID=05qqi1vevk9mtsusup23g9q1s0

ip=myip`

    tcp.SetTimeout(time.Second * 5)
    tcp.Write([]byte(raw))
    // return
    resp := tcp.Read(10000)

    tcp.Close()

    Printf("%s", resp)
}
