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
    // Println(Try(func() {
    //     Raise("fuck")
    // }))

    Println(time.Now().Sub(now))
}

func main() {
    Println(time.Now().UnixNano() / int64(time.Millisecond))
    console.Pause("done")
}
