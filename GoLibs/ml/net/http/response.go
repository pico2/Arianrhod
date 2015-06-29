package http

import (
    "io"
    "io/ioutil"
    "compress/gzip"
    "compress/zlib"
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

func readBody(resp *gohttp.Response) ([]byte, error) {
    var reader io.ReadCloser
    var err error

    switch String(resp.Header.Get("Content-Encoding")).ToLower() {
        case "gzip":
            reader, err = gzip.NewReader(resp.Body)
            if err != nil {
                return nil, err
            }

        case "deflate":
            reader, err = zlib.NewReader(resp.Body)
            if err != nil {
                return nil, err
            }

        default:
            reader = resp.Body
    }

    defer func() {
        if reader != resp.Body{
            reader.Close()
        }
    }()

    return ioutil.ReadAll(reader)
}

func NewResponse(resp *gohttp.Response) (*Response, error) {
    defer resp.Body.Close()

    content, err := readBody(resp)
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
