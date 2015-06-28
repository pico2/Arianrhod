package http

import (
    gourl "net/url"
    gohttp "net/http"
    "net/http/cookiejar"
    "errors"
    "fmt"
    "bytes"
    "io"
    "time"
    . "ml/strings"
    . "ml/dict"
)

type TimeoutError struct {
    Op  string
    URL string
    Err error
}

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

func dictToValues(d Dict, encoding int) gourl.Values {
    values := gourl.Values{}
    for k, v := range d {

        key := toString(k)
        value := toString(v)

        values.Set(string(key.Encode(encoding)), string(value.Encode(encoding)))
    }

    return values
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
    var bodyReader  io.Reader
    var params      Dict
    var encoding    int
    var queryString string

    switch (len(params_)) {
        case 1:
            params = params_[0]

        case 0:
            params = Dict{}

        default:
            return nil, errors.New("invalid params number")
    }

    switch v := params["encoding"].(type) {
        case int:
            encoding = v

        default:
            encoding = CP_UTF8
    }

    switch body := params["body"].(type) {
        case string:
            b := String(body)
            bodyReader = bytes.NewBuffer(b.Encode(encoding))

        case String:
            bodyReader = bytes.NewBuffer(body.Encode(encoding))

        case []byte:
            bodyReader = bytes.NewBuffer(body)

        case Dict:
            bodyReader = bytes.NewBufferString(dictToValues(body, encoding).Encode())

        default:
            bodyReader = nil
    }

    request, err := gohttp.NewRequest(string(method), string(url), bodyReader)
    if err != nil {
        return nil, err
    }

    switch query := params["params"].(type) {
        case Dict:
            values := dictToValues(query, encoding)
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

    var timer *time.Timer
    timeout := false

    if self.client.Timeout > 0 {
        timer = time.AfterFunc(self.client.Timeout, func() {
            timeout = true
        })
    }

    resp, err := self.client.Do(request)
    if timer != nil {
        timer.Stop()
    }

    if err != nil {
        // uerr := err.(*gourl.Error)
        // timeout := uerr.Err.Error() == "net/http: request canceled while waiting for connection"
        fmt.Println("timeout", timeout)
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
    if len(headers) == 0 {
        self.ClearHeaders()
        return
    }

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

func (self *Session) SetTimeout(second float64) {
    self.client.Timeout = time.Duration(second * 1000) * time.Millisecond
}

func NewSession() (*Session, error) {
    jar, err := cookiejar.New(nil)
    if err != nil {
        return nil, err
    }

    client := &gohttp.Client{
        CheckRedirect   : nil,
        Jar             : jar,
        Timeout         : 30 * time.Second,
    }

    return &Session{
                cookie  : jar,
                client  : client,
                headers : make(gohttp.Header),
            }, nil
}
