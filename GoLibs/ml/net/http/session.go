package http

import (
    . "ml/strings"
    . "ml/dict"
    . "ml/trace"

    gourl "net/url"
    gohttp "net/http"
    gonet "net"

    "net/http/cookiejar"
    "fmt"
    "bytes"
    "io"
    "time"
)

type Session struct {
    cookie             *cookiejar.Jar
    client             *gohttp.Client
    headers             gohttp.Header
    defaultTransport   *Transport
}

func NewSession() *Session {
    jar, err := cookiejar.New(nil)
    if err != nil {
        RaiseHttpError(err)
    }

    defaultTransport := newTransport(&gohttp.Transport{
        Proxy               : nil,
        // DisableKeepAlives   : true,
        Dial                : (&gonet.Dialer{
                                    Timeout     : 30 * time.Second,
                                    KeepAlive   : 30 * time.Second,
                                }).Dial,

        TLSHandshakeTimeout : 10 * time.Second,
    })

    client := &gohttp.Client{
        CheckRedirect   : nil,
        Jar             : jar,
        Timeout         : 30 * time.Second,
        Transport       : defaultTransport,
    }

    return &Session{
                cookie              : jar,
                client              : client,
                headers             : make(gohttp.Header),
                defaultTransport    : defaultTransport,
            }
}

func (self *Session) Close() {
    self.defaultTransport.CloseIdleConnections()
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
            fmt.Printf("%v\n", value)
            return String(v.(string))
    }
}

func dictToValues(d Dict, encoding Encoding) gourl.Values {
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
        request.Header.Set(fmt.Sprintf("%v", k), fmt.Sprintf("%v", v))
    }
}

func (self *Session) Request(methodi, urli interface{}, params_ ...Dict) (*Response) {
    var bodyReader  io.Reader
    var params      Dict
    var encoding    Encoding
    var queryString string
    var err         error

    method := toString(methodi)
    url := toString(urli)

    switch (len(params_)) {
        case 1:
            params = params_[0]

        case 0:
            params = Dict{}

        default:
            Raise(NewHttpError(HTTP_ERROR_GENERIC, method, url, String(fmt.Sprintf("invalid params number: %d", len(params_)))))
    }

    switch v := params["encoding"].(type) {
        case int, Encoding:
            encoding = v.(Encoding)

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
    RaiseHttpError(err)

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

    // fmt.Printf("query string = %v\n", queryString)
    // fmt.Printf("uri = %v\n", request.URL.String())

    self.client.CheckRedirect = func(request *gohttp.Request, via []*gohttp.Request) error {
        if len(via) >= 10 {
            Raise(NewHttpError(HTTP_ERROR_TOO_MANY_REDIRECT, method, url, "stopped after 10 redirects"))
        }

        applyHeadersToRequest(request, &self.headers, extraHeaders)
        return nil
    }

    // request.Close = true
    resp, err := self.client.Do(request)

    timeout := self.defaultTransport.canceledRequests[request]
    delete(self.defaultTransport.canceledRequests, request)

    self.client.CheckRedirect = nil

    if err != nil {
        self.defaultTransport.CancelRequest(request)

        uerr := err.(*gourl.Error)
        herr := &HttpError{
                    Op      : uerr.Op,
                    URL     : uerr.URL,
                    Err     : uerr.Err,
                }

        msg := String(herr.Err.Error())

        switch {
            case timeout,
                 msg.Contains("TLS handshake timeout"),
                 msg.Contains("Client.Timeout exceeded"):
                herr.Type = HTTP_ERROR_TIMEOUT

            case msg.Contains("error connecting to proxy"):
                herr.Type = HTTP_ERROR_CONNECT_PROXY

            case msg.Contains("unexpected EOF"):
                herr.Type = HTTP_ERROR_INVALID_RESPONSE

            case msg.Contains("wsarecv"):
                herr.Type = HTTP_ERROR_READ_ERROR

            case msg.Contains("Bad Gateway"):
                herr.Type = HTTP_ERROR_BAD_GATE_WAY

            default:
                herr.Type = HTTP_ERROR_GENERIC
        }

        Raise(herr)

        return nil
    }

    // fix net/http/client/shouldRedirectPost does not follow StatusTemporaryRedirect

    switch resp.StatusCode {
        case StatusTemporaryRedirect:
            if location := resp.Header.Get("Location"); location != "" {
                return self.Request(method, location, params_...)
            }
    }

    return NewResponse(resp)
}

func (self *Session) Get(url interface{}, params ...Dict) (resp *Response) {
    return self.Request("GET", url, params...)
}

func (self *Session) Post(url interface{}, params ...Dict) (resp *Response) {
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

func (self *Session) SetProxy(host String, port int, userAndPassword ...String) (err error) {
    if host.IsEmpty() {
        self.defaultTransport.Proxy = nil

    } else {
        var proxyUrl *gourl.URL
        var user, pass String

        switch len(userAndPassword) {
            case 2:
                user, pass = userAndPassword[0], userAndPassword[1]
                if user.IsEmpty() == false && pass.IsEmpty() == false {
                    proxyUrl, err = gourl.Parse(fmt.Sprintf("http://%s:%s@%s:%d", user, pass, host, port))
                    break
                }

                fallthrough

            case 1:
                user = userAndPassword[0]
                if user.IsEmpty() == false {
                    proxyUrl, err = gourl.Parse(fmt.Sprintf("http://%s@%s:%d", user, host, port))
                    break
                }

                fallthrough

            default:
                proxyUrl, err = gourl.Parse(fmt.Sprintf("http://%s:%d", host, port))
        }

        if err != nil {
            return
        }

        self.defaultTransport.Proxy = gohttp.ProxyURL(proxyUrl)
    }

    return
}

func (self *Session) SetTimeout(second float64) {
    self.client.Timeout = time.Duration(second * 1000) * time.Millisecond
}
