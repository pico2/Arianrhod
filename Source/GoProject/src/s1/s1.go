package main

import (
    . "ml/dict"
    . "ml/strings"
    . "ml/trace"

    "fmt"
    "os"
    "time"
    "sync"
    "path/filepath"

    "ml/console"
    "ml/strings"
    "ml/net/http"
    "ml/io2"
    "ml/os2"
    "ml/random"
    "ml/encoding/json"
    "ml/signal"

    "github.com/PuerkitoBio/goquery"
)

const (
    BASE_URL    = "http://bbs.saraba1st.com/2b/"
    FORUM_URL   = "http://bbs.saraba1st.com/2b/forum-75-1.html"
)

type Account struct {
    UserName    String              `json:"username,omitempty"`
    Password    String              `json:"password,omitempty"`
    Cookie      String              `json:"cookie,omitempty"`
}

var exiting bool = false

func login(session *http.Session, user, pass String) {
    resp := session.Post(
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

    if resp.StatusCode != http.StatusOK {
        Raisef("login status: %v", resp.StatusCode)
    }
}

func openPage(session *http.Session, url String) (doc *goquery.Document) {
    resp := session.Get(url)

    doc, err := goquery.NewDocumentFromReader(strings.Decode(resp.Content, resp.Encoding).NewReader())
    RaiseIf(err)

    return
}

func openThread(session *http.Session, user String) {
    doc := openPage(session, FORUM_URL)

    threads := []*goquery.Selection{}

    doc.Find("tbody").Each(func(i int, s *goquery.Selection) {
        id_, exist := s.Attr("id")
        id := String(id_)
        if exist && id.StartsWith("normalthread_") {
            threads = append(threads, s)
        }
    })

    if len(threads) == 0 {
        Raise("empty thread")
    }

    index := random.IntRange(0, len(threads))
    t := threads[index].Find("a.s.xst")
    href, ok := t.Attr("href")

    if ok == false {
        Raise("can't find thread addr")
    }

    credit := String(doc.Find("#extcreditmenu").Text())
    console.SetTitle(credit.Split(":", 1)[1])

    fmt.Printf("[%s][%s] %s @ %s\n", time.Now().Format("2006-01-02 15:04:05"), user, credit, t.Text())

    session.Get(BASE_URL + href)
}

func logout(session *http.Session) {
    doc := openPage(session, FORUM_URL)

    doc.Find("a").Each(func(i int, s *goquery.Selection){
        href_, exist := s.Attr("href")
        href := String(href_)
        if exist && href.Contains("action=logout") {
            session.Get(BASE_URL + href)
        }
    })
}

func do(user Account) {
    // user, pass := acc[0], acc[1]

    if user.Cookie.IsEmpty() {
        fmt.Printf("[%v] cookie required\n", user.UserName)
        return
    }

    session := http.NewSession()
    // session.SetProxy("localhost", 6789)
    session.SetHeaders(Dict{
        "Accept"            : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding"   : "gzip, deflate",
        "Accept-Language"   : "zh-CN,en-US;q=0.8,en;q=0.5,zh-HK;q=0.3",
        "User-Agent"        : "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:39.0) Gecko/20100101 Firefox/39.0",
        "Content-Type"      : "application/x-www-form-urlencoded",
        "Connection"        : "keep-alive",
        "Cookie"            : user.Cookie,
    })

    for exiting == false {
        // for exiting == false {
        //     exp := Try(func() {
        //         login(session, user, pass)
        //     })

        //     if exp == nil {
        //         break
        //     }

        //     fmt.Println(exp)
        //     time.Sleep(time.Second)
        // }

        for i := 0; i != 6 && exiting == false; i++ {
            exp := Try(func() {
                        openThread(session, user.UserName)
                    })

            switch exp {
                case nil:
                    for i := 0; i != 600 && exiting == false; i++ {
                        time.Sleep(time.Second)
                    }

                default:
                    fmt.Println(exp)
                    time.Sleep(2 * time.Second)
            }
        }

        // Try(func() {
        //     fmt.Println("logout")
        //     logout(session)
        // })
    }
}

func readuser() (accounts []Account) {
    json.MustUnmarshal(io2.ReadContent(filepath.Join(filepath.Dir(os2.Executable()), "users.json")), &accounts)
    return
}

func main() {
    var exp *Exception

    defer func() {
        fmt.Println(exp)
        console.Pause("done")
    }()

    exp = Try(func() {
        users := readuser()

        signal.Notify(
            func() {
                exiting = true
            },
            os.Interrupt,
        )

        wg := sync.WaitGroup{}

        for _, u := range users {
            wg.Add(1)
            go func(u Account) {
                do(u)
                wg.Done()
            }(u)
        }

        wg.Wait()
    })
}
