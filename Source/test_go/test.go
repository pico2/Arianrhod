package main

import (
    "github.com/garyburd/redigo/redis"
    "gopkg.in/redsync.v1"
    "github.com/PuerkitoBio/goquery"
    . "ml/strings"
    . "ml/trace"
    . "ml/dict"
    "fmt"
    "os"
    "time"
    "ml/io2"
    "ml/net/http2"
    "ml/html"
    "ml/logging/logger"
)

func fn2() {
    go func() {
        e := Try(func() {
            (&goquery.Selection{}).Attr2("attrName")
        })
        fmt.Println(e)
    }()
}

func main() {
    s := http.NewSession(
        http.Timeout(time.Second * 30),
        http.TLSHandshakeTimeout(10 * time.Second),
    )

    fmt.Println(s.Get("http://www.qq.com?test=fuck&haha=hehe"))
}
