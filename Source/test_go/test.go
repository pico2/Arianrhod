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
    "ml/io2"
    "ml/net/http"
    "ml/html"
)

func checkDuplicate() {
    for _, arg_ := range os.Args[1:] {
        arg := String(arg_)

        exists := map[String]bool{}
        accounts := []String{}
        for _, line := range io2.ReadLines(arg) {
            if line.Count("----") != 1 {
                continue
            }

            u := line.Split("----", 1)
            if exists[u[0]] {
                continue
            }

            exists[u[0]] = true

            accounts = append(accounts, line)
        }

        io2.WriteContent(arg.RSplit(".", 1)[0].String() + ".unique.txt", []byte(String("\r\n").Join(accounts)))
    }
}

func main() {
    pool := redis.NewPool(
                func() (redis.Conn, error) {
                    return redis.DialTimeout(
                                "tcp",
                                "192.168.1.2:6379",
                                time.Second * 10,
                                time.Second * 60,
                                time.Second * 60,
                            )
                },
                3,
            )
    defer pool.Close()

    sync := redsync.New([]redsync.Pool{pool})

    m := sync.NewMutex(
            "get_account",
            redsync.SetExpiry(time.Minute * 10),
            redsync.SetDriftFactor(1),
        )

    for m.Lock() == redsync.ErrFailed {
    }

    for i := 0; i != 100; i++ {
        fmt.Println(i)
        time.Sleep(time.Second)
    }

    m.Unlock()
}
