package main

import (
    . "fmt"
    . "ml"
    "ml/net/http"
    "ml/strings"
)

func main() {
    ss := Str("fuck your mother")

    le := ss.Encode(strings.CP_UTF16_LE)
    for _, ch := range le {
        Printf("%02X ", ch)
    }
    Println()
    Println(strings.Decode(le, strings.CP_UTF16_LE))

    be := ss.Encode(strings.CP_UTF16_BE)
    for _, ch := range be {
        Printf("%02X ", ch)
    }
    Println()
    Println(strings.Decode(be, strings.CP_UTF16_BE))

    session, _ := http.NewSession()
    session.SetProxy("localhost", 6789)
    session.SetTimeout(0.1)

    resp, err2 := session.Get("https://www.google.com/")

    if err, ok := err2.(*http.HttpError); ok {
        Println("timeout", err.Timeout, err)
    }

    if resp != nil {
        Println("resp", len(resp.Content))
    }

    Console.Pause("fuck")
}
