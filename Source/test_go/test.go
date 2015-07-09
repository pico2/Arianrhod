package main

import (
    . "fmt"
    "ml/console"
    "os"
    "github.com/PuerkitoBio/goquery"
)

func unused() {
}

var count int = 1

func rand() int {
    if count < 5 {
        count++
    }
    println("count =", count)
    return count
}

func main() {
    f, _ := os.Open("D:/desktop/111.html")

    doc, _ := goquery.NewDocumentFromReader(f)
    g := doc.Find(".page-error").Find(".generic-error")

    Println(g.Length(), g.Text())

    console.Pause("done")
}
