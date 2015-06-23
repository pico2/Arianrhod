package http

import (
    "io/ioutil"
    "net/url"
    "ml/str"
    gohttp "net/http"
)

type Response struct {
    Status      str.String // e.g. "200 OK"
    StatusCode  int    // e.g. 200
    Proto       str.String // e.g. "HTTP/1.0"
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
        Status      : str.String(resp.Status),
        StatusCode  : resp.StatusCode,
        Proto       : str.String(resp.Proto),
        ProtoMajor  : resp.ProtoMajor,
        ProtoMinor  : resp.ProtoMinor,
        Header      : resp.Header,
        Content     : content,
        Request     : resp.Request,

        resp        : resp,

    }, nil
}
