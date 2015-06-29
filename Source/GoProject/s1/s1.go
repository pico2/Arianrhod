package main

import (
    . "fmt"
    . "ml"
    . "ml/dict"
    . "ml/strings"
    "ml/strings"
    "ml/net/http"
    "ml/io2"
    "ml/os2"
    "path/filepath"
    "time"
    "golang.org/x/net/html"
    // "errors"
)

func login(session *http.Session, user, pass String) error {
    resp, err := session.Post(
                    "http://bbs.saraba1st.com/2b/member.php",
                    Dict{
                        "params": Dict{
                            "mod"           : "logging",
                            "action"        : "login",
                            "loginsubmit"   : "yes",
                            "infloat"       : "yes",
                            "lssubmit"      : "yes",
                            "inajax"        : "1",
                        },
                        "body": Dict{
                            "fastloginfield"    : "username",
                            "quickforward"      : "yes",
                            "handlekey"         : "ls",
                            "username"          : user,
                            "password"          : pass,
                        },
                        "encoding": strings.CP_UTF8,
                    },
                )

    if err != nil {
        return err
    }

    if resp.StatusCode != http.StatusOK {
        return Errorf("login status: %s", http.StatusText(resp.StatusCode))
    }

    return nil
}

func openPage(session *http.Session, url String) (doc *html.Node, err error) {
    resp, err := session.Get(url)

    if err != nil {
        return nil, err
    }

    doc, err = html.Parse(strings.Decode(resp.Content, strings.CP_UTF8).NewReader())
    return
}

func openThread(session *http.Session) error {
    doc, err := openPage(session, "http://bbs.saraba1st.com/2b/forum-75-1.html")
    if err != nil {
        return err
    }

    var f func(*html.Node)

    f = func(n *html.Node) {
        Printf("type = %v, data = %v\n", n.Type, n.Data)
        for _, attr := range n.Attr {
            Printf("  %s = %s\n", attr.Key, attr.Val)
        }

        for c := n.FirstChild; c != nil; c = c.NextSibling {
            f(c)
        }
    }

    f(doc)

    return nil
}

func logout(session *http.Session) {

}

func do() error {
    usertxt := String(filepath.Join(filepath.Dir(os2.Executable()), "user.txt"))
    Println(usertxt)
    acc, err := io2.ReadTextToLines(usertxt)
    if err != nil {
        return err
    }

    if len(acc) < 2 {
        panic("corrupt user.txt")
    }

    user, pass := acc[0], acc[1]

    for {
        session, _ := http.NewSession()
        session.SetProxy("localhost", 6789)
        session.SetHeaders(Dict{
            "Accept"            : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Encoding"   : "gzip, deflate",
            "Accept-Language"   : "zh-CN,en-US;q=0.8,en;q=0.5,zh-HK;q=0.3",
            "User-Agent"        : "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:39.0) Gecko/20100101 Firefox/39.0",
            "Content-Type"      : "application/x-www-form-urlencoded",
            "Connection"        : "keep-alive",
        })

        for {
            err = login(session, user, pass)
            if err == nil {
                break
            }

            time.Sleep(time.Second)
        }

        for i := 0; i != 6; i++ {
            err = openThread(session)

            switch err {
                case nil:
                    time.Sleep(10 * time.Minute)

                default:
                    time.Sleep(2 * time.Second)
            }
        }

        logout(session)
    }
}

func main() {
    err := do()
    if err != nil {
        Println(err)
    }

    Console.Pause("done")
}
