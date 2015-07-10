package main

import (
    . "fmt"
    . "ml/trace"
    "ml/trace"
    "ml/console"
    "time"
    // "os"
    // "github.com/PuerkitoBio/goquery"
)

func unused() {
    _ = Raise
}

func main() {
    trace.Config.ReadSource = false

    now := time.Now()
    for i := 0; i != 100000; i++ {
        Println(Try(func() {
            Raise("fuck")
        }))
    }

    Println(time.Now().Sub(now))
    console.SetTitle("done")

    console.Pause("done")
}
