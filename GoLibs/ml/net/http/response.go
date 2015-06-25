package http

import (
    "io/ioutil"
    "net/url"
    . "ml/strings"
    gohttp "net/http"
)

type Response struct {
    Status      String // e.g. "200 OK"
    StatusCode  int    // e.g. 200
    Proto       String // e.g. "HTTP/1.0"
    ProtoMajor  int    // e.g. 1
    ProtoMinor  int    // e.g. 0
    Header      gohttp.Header
    Content     []byte
    Request     *gohttp.Request

    resp        *gohttp.Response
}

func (self *Response) Cookies() []*gohttp.Cookie {
    return self.resp.Cookies()
}

func (self *Response) Location() (*url.URL, error) {
    return self.resp.Location()
}

func NewResponse(resp *gohttp.Response) (*Response, error) {
    defer resp.Body.Close()

    content, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        return nil, err
    }

    return &Response{
        Status      : String(resp.Status),
        StatusCode  : resp.StatusCode,
        Proto       : String(resp.Proto),
        ProtoMajor  : resp.ProtoMajor,
        ProtoMinor  : resp.ProtoMinor,
        Header      : resp.Header,
        Content     : content,
        Request     : resp.Request,

        resp        : resp,

    }, nil
}
