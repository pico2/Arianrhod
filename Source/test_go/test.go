package main

import (
    _ "ml"
    . "fmt"
    . "ml/dict"
    . "ml/array"
    . "ml/strings"
    "ml/console"

    "plistlib"
    "strconv"
    "os"

    "github.com/PuerkitoBio/goquery"
)

func unused() {
    _ = Dict{}
    _ = Array{}
    _ = Printf
    _ = strconv.Atoi
    _ = plistlib.Unmarshal
}

func main() {
    r, _ := os.Open("1.html")
    doc, _ := goquery.NewDocumentFromReader(r)

    success := doc.Find(".email-verification").Length() != 0
    Println(success)

    script := doc.Find("script[id=protocol][type*=text][type*=x-apple-plist]")

    plist := Dict{}
    plistlib.Unmarshal(
        String("<plist version=\"1.0\">\r\n" + script.Text() + "</plist>").Encode(CP_UTF8),
        &plist,
    )

    dsid, _ := strconv.ParseInt(plist["set-current-user"].(map[string]interface{})["dsPersonId"].(string), 10, 64)
    Printf("%d\n", dsid)

    console.Pause("done")
}
