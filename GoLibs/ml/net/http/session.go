package http

import (
    // "fmt"
    "errors"
    gourl "net/url"
    "net/http/cookiejar"
    "ml/str"
    . "ml/dict"
    gohttp "net/http"
)

type Header struct {
    *gohttp.Header
}

type Session struct {
    cookie  *cookiejar.Jar
    client  *gohttp.Client
    header  gohttp.Header
}

func (self *Session) Request(method, url str.String, params_ ...Dict) (*Response, error) {
    request, err := gohttp.NewRequest(string(method), string(url), nil)
    if err != nil {
        return nil, err
    }

    params := Dict{}
    switch (len(params_)) {
        case 1:
            params = params_[0]

        case 0:
            break

        default:
            return nil, errors.New("invalid params number")
    }

    data := params["data"]
    query := params["params"]

    switch (method.ToUpper()) {
        case "GET":
            if query == nil {
                break
            }

            values := gourl.Values{}
            for k, v := range query.(Dict) {
                values.Set(k.(string), v.(string))
            }

        case "POST":
            if data == nil {
                break
            }
    }

    resp, err := self.client.Do(request)
    if err != nil {
        return nil, err
    }

    return NewResponse(resp)
}

func (self *Session) Get(url str.String, params ...Dict) (resp *Response, err error) {
    return self.Request("GET", url, params...)
}

func (self *Session) Post(url str.String, params ...Dict) (resp *Response, err error) {
    return self.Request("POST", url, params...)
}

func (self *Session) SetHeaders(headers *Header) {

}

func NewSession() (*Session, error) {
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
                header: make(gohttp.Header),
            }, nil
}
