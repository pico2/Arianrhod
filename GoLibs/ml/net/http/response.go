package http

import (
    . "ml/trace"
    . "ml/strings"
    "io"
    "io/ioutil"
    "compress/gzip"
    "compress/zlib"
    "net/url"
    "mime"
    "plistlib"
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
    Encoding    int

    resp        *gohttp.Response
}

func NewResponse(resp *gohttp.Response) (response *Response) {
    var content []byte

    if resp.Body != nil {
        defer resp.Body.Close()
        content = readBody(resp)
    }

    response = &Response{
        Status      : String(resp.Status),
        StatusCode  : resp.StatusCode,
        Proto       : String(resp.Proto),
        ProtoMajor  : resp.ProtoMajor,
        ProtoMinor  : resp.ProtoMinor,
        Header      : resp.Header,
        Content     : content,
        Request     : resp.Request,
        Encoding    : getEncoding(resp, content),

        resp        : resp,
    }

    return
}

func (self *Response) Text(encoding ...int) String {
    var enc int
    switch len(encoding) {
        case 0:
            enc = self.Encoding

        default:
            enc = encoding[0]
    }

    return Decode(self.Content, enc)
}

func (self *Response) Plist(v interface{}) {
    RaiseHttpError(plistlib.Unmarshal(self.Content, v))
}

func (self *Response) Cookies() []*gohttp.Cookie {
    return self.resp.Cookies()
}

func (self *Response) Location() (*url.URL) {
    u, err := self.resp.Location()
    RaiseHttpError(err)
    return u
}

func raise(resp *gohttp.Response, err error) {
    if err == nil {
        return
    }

    msg := String(err.Error())
    switch {
        case msg.Contains("No connection could be made because the target machine actively refused it"):
            Raise(NewHttpError(
                HTTP_ERROR_CANNOT_CONNECT,
                String(resp.Request.Method),
                String(resp.Request.URL.String()),
                msg,
            ))

        case msg.Contains("Client.Timeout exceeded"):
            Raise(NewHttpError(
                HTTP_ERROR_TIMEOUT,
                String(resp.Request.Method),
                String(resp.Request.URL.String()),
                msg,
            ))

        default:
            Raise(NewHttpError(
                HTTP_ERROR_RESPONSE_ERROR,
                String(resp.Request.Method),
                String(resp.Request.URL.String()),
                String(err.Error()),
            ))
            // RaiseHttpError(err)
    }
}

func readBody(resp *gohttp.Response) (body []byte) {
    var reader io.ReadCloser
    var err error

    switch String(resp.Header.Get("Content-Encoding")).ToLower() {
        case "gzip":
            reader, err = gzip.NewReader(resp.Body)
            raise(resp, err)
            defer reader.Close()

        case "deflate":
            reader, err = zlib.NewReader(resp.Body)
            raise(resp, err)
            defer reader.Close()

        default:
            reader = resp.Body
    }

    body, err = ioutil.ReadAll(reader)
    raise(resp, err)

    return
}

func getEncoding(resp *gohttp.Response, body []byte) int {
    charsetTable := map[string]int{
        "gb18030"   : CP_GBK,
        "gb2312"    : CP_GBK,
        "hz"        : CP_GBK,
        "big5"      : CP_BIG5,
        "shift_jis" : CP_SHIFT_JIS,
        "euc-jp"    : CP_SHIFT_JIS,
        "utf-8"     : CP_UTF8,
    }

    ctype := resp.Header.Get("Content-Type")
    if len(ctype) == 0 {
        return CP_UTF8
    }

    _, params, err := mime.ParseMediaType(ctype)
    if err != nil {
        return CP_UTF8
    }

    charset, ok := params["charset"]
    if ok == false {
        return CP_UTF8
    }

    encoding, ok := charsetTable[string(String(charset).ToLower())]
    if ok == false {
        encoding = CP_UTF8
    }

    return encoding
}
