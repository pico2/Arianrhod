package main

import (
    . "fmt"
    . "ml/strings"
    . "ml/trace"
    . "ml/dict"
    "./pinyin"
    "ml/random"
    "ml/console"
    "os"
    "time"
    "syscall"
    "sync"
    "io/ioutil"
    "github.com/PuerkitoBio/goquery"
    "ml/uuid"
    "ml/encoding/binary"
    "ml/encoding/json"
    "ml/net/socket"
    "ml/net/http"
    "ml/pprof"
    "ml/sync2"
)

func genacc() {
    py := [][]string{}
    json.Unmarshal([]byte(pinyin.Json), &py)

    f, _ := os.Open("domains.txt")
    bytes, _ := ioutil.ReadAll(f)
    f.Close()

    domains := String(bytes).SplitLines()

    // names := []string{}
    nameset := map[string]bool{}

    target  := 1000000
    perline := 30000
    index   := 0

    names := []String{}

    for i := 0; i != target; i++ {
        name := ""
        for n := random.IntRange(1, 5); n > 0; {
            p := py[random.ChoiceIndex(py)][1]
            if len(p) > 2 {
                continue
            }

            name += p
            n--
        }

        name += Sprintf("%d@%s", random.IntRange(1000, 100000), random.Choice(domains).(String))
        if nameset[name] {
            i--
            continue
        }

        nameset[name] = true
        names = append(names, String(name))

        switch {
            case i + 1 == target,
                 i != 0 && i % perline == 0:
                 f, _ = os.Create(Sprintf("names%d.txt", index))
                 f.WriteString("INSERT IGNORE INTO appstore_buydata_appleid (username) VALUES (\"")
                 f.WriteString(string(String("\"),(\"").Join(names)))
                 f.WriteString("\");\n")

                 f.Close()

                 index++
                 names = []String{}
        }
    }
}

func main() {
    defer console.Pause("done")
    tcp := socket.NewTcpSocket()
    tcp.Connect("40.83.120.76", 443, 10 * time.Second)
    Println("connected")
}
