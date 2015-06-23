package http

import (
    gohttp "net/http"
)

type Response struct {
    Status      str.String // e.g. "200 OK"
    StatusCode  int    // e.g. 200
    Proto       str.String // e.g. "HTTP/1.0"
    ProtoMajor  int    // e.g. 1
    ProtoMinor  int    // e.g. 0
    Header      gohttp.Header
}
