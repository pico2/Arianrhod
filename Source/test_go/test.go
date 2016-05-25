package main

import (
    "github.com/PuerkitoBio/goquery"
    . "ml/strings"
    . "ml/dict"
    "fmt"
    "os"
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
    doc := html.Parse(String(io2.ReadContent(`D:\Desktop\New Text Document.html`)))
    // paymentName := doc.Find("span.payment-name").Parent()
    // info := paymentName.Parent()
    // action := info.Next()
    // edit := action.Find("a.see-all")

    edit := doc.Find("a.see-all[href]").Eq(2)

    fmt.Println(edit.Attr2("href"), edit.Text())
}
