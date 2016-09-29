package main

import (
    . "ml/strings"

    "fmt"
    urllib "net/url"

    "ml/os2"
    "ml/trace"
    "ml/console"

    "downloader"
    "path/filepath"
)

func getDownloaderFromUrl(url String) downloader.Downloader {
    if url.ToLower().StartsWith("http") == false {
        url = "http://" + url
    }

    u, err := urllib.Parse(url.String())
    if err != nil {
        trace.Raise(trace.NewWrapper(err, "parse url '%v' failed:", url))
    }

    fmt.Println(u.Host)

    switch String(u.Host).ToLower() {
        case "v.ku6.com", "baidu.ku6.com":
            return downloader.NewKu6(url)

        case "v.youku.com":
            return downloader.NewYouku(url)

        case "open.163.com":
            return downloader.NewNetEase(url)

        default:
            trace.Raise(trace.NewNotImplementedError("%v unimplemented", url))
            return nil
    }
}

func run() {
    var url String

    fmt.Printf("url = ")
    fmt.Scanf("%s\n", &url)

    if url.IsEmpty() {
        url = "http://open.163.com/movie/2011/9/E/4/M8DOH67K8_M8DQVB8E4.html"
    }

    d := getDownloaderFromUrl(url)
    defer d.Close()

    path := String(filepath.Join(os2.ExecutablePath(), "downloaded"))

    switch d.Analysis() {
        case downloader.AnalysisSuccess:
            d.Download(path)
    }
}

func main() {
    if e := trace.Try(run); e != nil {
        fmt.Println(e)
    }

    console.Pause("done")
}
