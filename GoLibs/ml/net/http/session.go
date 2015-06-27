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

func applyHeadersToRequest(request *gohttp.Request, defaultHeaders *gohttp.Header, extraHeaders Dict) {
    for k, vs := range *defaultHeaders {
        for _, v := range vs {
            request.Header.Add(k, v)
        }
    }

    for k, v := range extraHeaders {
        request.Header.Add(fmt.Sprintf("%v", k), fmt.Sprintf("%v", v))
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

    extraHeaders := Dict{}

    switch headers := params["headers"].(type) {
        case Dict:
            extraHeaders = headers
    }

    applyHeadersToRequest(request, &self.headers, extraHeaders)

    if len(queryString) != 0 {
        request.URL.RawQuery = queryString
    }

    fmt.Printf("query string = %v\n", queryString)
    fmt.Printf("uri = %v\n", request.URL.String())

    self.client.CheckRedirect = func(request *gohttp.Request, via []*gohttp.Request) error {
        if len(via) >= 10 {
            return errors.New("stopped after 10 redirects")
        }

        applyHeadersToRequest(request, &self.headers, extraHeaders)
        return nil
    }

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

func (self *Session) ClearHeaders() {
    self.headers = gohttp.Header{}
}

func (self *Session) SetHeaders(headers Dict) {
    for k, v := range headers {
        self.headers.Add(fmt.Sprintf("%v", k), fmt.Sprintf("%v", v))
    }
}

func (self *Session) SetProxy(host String, port int) {
    if len(host) == 0 {
        self.client.Transport = nil
    } else {
        proxyUrl, err := gourl.Parse(fmt.Sprintf("http://%s:%d", host, port))
        if err != nil {
            return
        }

        self.client.Transport = &gohttp.Transport{Proxy: gohttp.ProxyURL(proxyUrl)}
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
