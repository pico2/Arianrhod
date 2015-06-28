package main

import (
    . "ml"
    "ml/net/http"
    "fmt"
    "net/url"
)

func do() {

}

func main() {
    session, _ := http.NewSession()
    session.SetProxy("localhost", 6789)
    session.SetTimeout(0.1)

    resp, err2 := session.Get("https://www.google.com/")
    err := err2.(*url.Error)

    fmt.Println("resp", resp)
    fmt.Println("err", err.Op)

    Console.Pause("fuck")
}
