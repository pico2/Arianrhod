package http

import (
    "errors"
    gourl "net/url"
    "net/http/cookiejar"
    . "ml/strings"
    . "ml/dict"
    gohttp "net/http"
    "fmt"
)

type Header struct {
    *gohttp.Header
}

type Session struct {
    cookie  *cookiejar.Jar
    client  *gohttp.Client
    headers gohttp.Header
}

func toString(value interface{}) String {
    switch v := value.(type) {
        case string:
            return String(v)

        case String:
            return v

        case int:
            return String(fmt.Sprintf("%v", v))

        default:
            return String(v.(string))
    }
}

func (self *Session) Request(method, url String, params_ ...Dict) (*Response, error) {
    request, err := gohttp.NewRequest(string(method), string(url), nil)
    if err != nil {
        return nil, err
    }

    var params Dict
    switch (len(params_)) {
        case 1:
            params = params_[0]

        case 0:
            params = Dict{}

        default:
            return nil, errors.New("invalid params number")
    }

    var encoding int
    var queryString string

    switch v := params["encoding"].(type) {
        case int:
            encoding = v
            if encoding == CP_UTF8 {
                encoding = 0
            }

        default:
            encoding = 0
    }

    switch query := params["params"].(type) {
        case Dict:
            if method.ToUpper() != "GET" {
                break
            }

            values := gourl.Values{}
            for k, v := range query {

                key := toString(k)
                value := toString(v)

                if encoding != 0 {
                    key = String(string(key.Encode(encoding)))
                    value = String(string(value.Encode(encoding)))
                }

                values.Set(string(key), string(value))
            }

            queryString = values.Encode()
    }

    for k, vs := range self.headers {
        for _, v := range vs {
            request.Header.Add(k, v)
        }
    }

    switch headers := params["headers"].(type) {
        case Dict:
            for k, v := range headers {
                request.Header.Set(fmt.Sprintf("%v", k), fmt.Sprintf("%v", v))
            }
    }

    if len(queryString) != 0 {
        request.URL.RawQuery = queryString
    }

    fmt.Printf("query string = %v\n", queryString)
    fmt.Printf("uri = %v\n", request.URL.String())

    resp, err := self.client.Do(request)
    if err != nil {
        return nil, err
    }

    return NewResponse(resp)
}

func (self *Session) Get(url String, params ...Dict) (resp *Response, err error) {
    return self.Request("GET", url, params...)
}

func (self *Session) Post(url String, params ...Dict) (resp *Response, err error) {
    return self.Request("POST", url, params...)
}

func (self *Session) SetHeaders(headers Dict) {
    self.headers = gohttp.Header{}
    for k, v := range headers {
        self.headers.Set(fmt.Sprintf("%v", k), fmt.Sprintf("%v", v))
    }
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
                cookie  : jar,
                client  : client,
                headers : make(gohttp.Header),
            }, nil
}
