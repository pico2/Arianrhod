package main

import (
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
    for i := 0; i != 500; i++ {
        go func() {
            for {
                Try(func() {
                    h := http.NewSession()
                    defer h.Close()
                    h.SetProxy("localhost", 48888)
                    h.Get("http://www.qq.com")
                })
            }
        }()
    }

    time.Sleep(time.Hour)
}
