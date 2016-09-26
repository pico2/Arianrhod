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
    "ml/encoding/json"
    "net"
)

func create(session String) *http.Session {
    ips, _ := net.LookupHost("zproxy.luminati.io")
    s := http.NewSession(http.DefaultTimeout(5 * time.Second))

    var user String = "lum-customer-weichuan-zone-gen"

    if session.IsEmpty() == false {
        user += "-session-" + session
    }

    s.SetHTTPProxy(String(ips[0]), 22225, user, "bf1cc03e5ded")

    return s
}

func main() {
    var sum time.Duration

    for i := 0; i != 100; i++ {
        s := create(String(fmt.Sprint(i)))

        start := time.Now()

        s.Get("http://lumtest.com/myip.json").Map(func (value interface{}) (interface{}, error) {
            var r JsonDict

            resp := value.(*http.Response)

            resp.Json(&r)

            elapsed := time.Now().Sub(start)
            sum += elapsed
            fmt.Printf("%04d %s %v\n", i, r.Str("ip"), elapsed)

            return nil, nil

        }).MapErr(func (err error) error {
            // panic(err)
            return err
        })

        s.Close()
    }

    fmt.Println(sum / 100)
}
