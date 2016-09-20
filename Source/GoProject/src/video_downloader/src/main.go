package main

import (
    . "ml/strings"

    "fmt"
    urllib "net/url"

    "ml/os2"
    "ml/trace"

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

        default:
            trace.Raise(trace.NewNotImplementedError("unimplemented for %v", url))
            return nil
    }
}

func main() {
    var url String = "http://baidu.ku6.com/watch/9161687529597316875.html?page=videoMultiNeed"
    //url = "http://v.ku6.com/show/voWYIqc6BWBfzK_gzdLRXw...html"
    d := getDownloaderFromUrl(url)
    defer d.Close()

    path := String(filepath.Join(os2.ExecutablePath(), "downloaded"))

    switch d.Analysis() {
        case downloader.AnalysisSuccess:
            d.Download(path)
    }
}
