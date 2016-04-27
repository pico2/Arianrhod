package main

import (
    . "ml/strings"
    . "ml/dict"
    "fmt"
    "os"
    "ml/io2"
    "ml/net/http"
)

func checkDuplicate() {
    for _, arg_ := range os.Args[1:] {
        arg := String(arg_)

        exists := map[String]bool{}
        accounts := []String{}
        for _, line := range io2.ReadLines(arg) {
            if line.Count("----") != 1 {
                continue
            }

            u := line.Split("----", 1)
            if exists[u[0]] {
                continue
            }

            exists[u[0]] = true

            accounts = append(accounts, line)
        }

        io2.WriteContent(arg.RSplit(".", 1)[0].String() + ".unique.txt", []byte(String("\r\n").Join(accounts)))
    }
}

func main() {
    s := http.NewSession()
    s.SetSocks5Proxy("inke.norn7.com", 47777, nil)
    // s.SetProxy("localhost", 6789)

    s.SetHeaders(Dict{
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
        "Upgrade-Insecure-Requests": "1",
    })

    // resp := s.Post("http://ip.taobao.com/service/getIpInfo2.php", Dict{"body": []byte("ip=myip")})
    resp := s.Get("https://www.baidu.com/s?ie=UTF-8&wd=ip")
    fmt.Printf("%s\n", resp.Content)
}
