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
    "ml/net/http2"
    "ml/html"
    "ml/logging/logger"
)

func main() {
    s := http.NewSession(http.DefaultTimeout(1 * time.Second))
    s.SetHTTPProxy("localhost", 6789)
    ret := s.Get("https://storage.googleapis.com/golang/go1.7.1.windows-amd64.zip")
    fmt.Println(ret.Err())
}
