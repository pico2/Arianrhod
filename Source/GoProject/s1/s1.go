package main

import (
    . "fmt"
    . "ml"
    "ml/net/http"
    // "net/url"
)

func do() {

}

func main() {
    ss := Str("fuck your mother")

    for _, s := range ss.RSplit(" ") {
        Println(s)
    }

    Println(ss.EndsWith("fuck"))

    session, _ := http.NewSession()
    session.SetProxy("localhost", 6789)
    session.SetTimeout(1)

    resp, err2 := session.Get("https://www.google.com/")

    if err, ok := err2.(*http.HttpError); ok {
        Println("timeout", err.Timeout, err)
    }

    Println("resp", len(resp.Content))

    Console.Pause("fuck")
}
