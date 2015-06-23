package http

import (
    "net/http/cookiejar"
    "ml/str"
    gohttp "net/http"
)

type Session struct {
    cookie  *cookiejar.Jar
    client  *gohttp.Client
}

func (self *Session) Get(url str.String) (resp *) {

}

func New() (*Session, error) {
    jar, err := cookiejar.New(nil)
    if err != nil {
        return nil, err
    }

    client := &http.Client{
        CheckRedirect: nil,
        Jar:           jar,
    }

    return &Session{
                cookie: jar,
                client: client,
            }, nil
}

func init() {
    // _ = gohttp
}
