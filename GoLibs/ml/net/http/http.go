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

func (self *Session) Request(method str.String, url str.String) (resp *Response, err error) {
    return nil, nil
}

func (self *Session) Get(url str.String) (resp *Response, err error) {
    return self.Request("GET", url)
}

func (self *Session) Post(url str.String) (resp *Response, err error) {
    return self.Request("Post", url)
}

func New() (*Session, error) {
    jar, err := cookiejar.New(nil)
    if err != nil {
        return nil, err
    }

    client := &gohttp.Client{
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
