package main

import (
    . "ml/trace"
    "ml/net/http"
    "ml/console"
    "time"
)

func unused() {
    _ = Raise
}

func f2() {
    console.Pause("get")

    sesstion := http.NewSession()
    // sesstion.SetProxy("localhost", 6789)

    for i := 0; i < 10; i++ {
        sesstion.Get("http://www.baidu.com")
        time.Sleep(time.Second)
    }

    console.Pause("got")
    sesstion.Close()
    console.Pause("closed")
}

func main() {
    f2()
    console.Pause("done")
}
