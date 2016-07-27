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
    "ml/net/http"
    "ml/html"
    "ml/logging/logger"
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

func fn2() {
    go func() {
        e := Try(func() {
            (&goquery.Selection{}).Attr2("attrName")
        })
        fmt.Println(e)
    }()
}

func main() {
    e := Try(func() {
        (&goquery.Selection{}).Attr2("attrName")
    })
    fmt.Println(e)
    fmt.Println()

    fn2()

    time.Sleep(time.Hour)
}
