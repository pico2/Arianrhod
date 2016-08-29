package main

import (
    "github.com/garyburd/redigo/redis"
    "gopkg.in/redsync.v1"
    "github.com/PuerkitoBio/goquery"
    . "ml/strings"
    . "ml/trace"
    . "ml/dict"
    "fmt"
    "os"
    "time"
    "context"
    "ml/io2"
    "net/http"
    // "ml/net/http2"
    "ml/html"
    "ml/logging/logger"
)

func main() {
    req, _ := http.NewRequest("GET", "http://fuck.norn7.com/", nil)

    parent := context.Background()
    ctx, cancel := context.WithTimeout(parent, time.Microsecond * 2000)
    req = req.WithContext(ctx)

    t := time.Now()
    resp, err := http.DefaultClient.Do(req)
    fmt.Println(time.Now().Sub(t))

    fmt.Println(err, resp)
    // fmt.Println(<-ctx.Done(), "done")
    fmt.Println(ctx.Err())
    cancel()
    fmt.Println(ctx.Err() == context.DeadlineExceeded)
    fmt.Println(ctx.Err() == context.Canceled)

    fmt.Println(time.ParseDuration("1000s"))

    _ = cancel
}
