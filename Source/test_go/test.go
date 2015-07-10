package main

import (
    . "fmt"
    . "ml/trace"
    "ml/trace"
    "ml/console"
    "time"
    "runtime/pprof"
    "runtime"
    "os"
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
    runtime.SetCPUProfileRate(1000000)
    f, _ := os.Create("test.prof")
    pprof.StartCPUProfile(f)
    defer pprof.StopCPUProfile()

    trace.Config.ReadSource = false

    for i := 0; i != 100000; i++ {
        f2()
    }

    console.SetTitle("done")

    console.Pause("done")
}
