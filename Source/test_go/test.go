package main

import (
    . "fmt"
    . "ml/trace"
    // "ml/trace"
    "ml/console"
    "time"
    // "os"
    // "github.com/PuerkitoBio/goquery"
)

func unused() {
    _ = Raise
}

func f2() {
    now := time.Now()
    Println("fuck")
    Println(Try(func() {
        Raise("can't find attribute")
    }).Message)

    Println(time.Now().Sub(now))
}

func main() {
    f2()
    console.Pause("done")
}
