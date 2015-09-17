package http

import (
    gohttp "net/http"
)

type Transport struct {
    *gohttp.Transport
    canceledRequests map[*gohttp.Request]bool
}

func newTransport(transport *gohttp.Transport) *Transport {
    return &Transport{
        Transport           : transport,
        canceledRequests    : map[*gohttp.Request]bool{},
    }
}

func (self *Transport) CancelRequest(req *gohttp.Request) {
    self.Transport.CancelRequest(req)
    self.canceledRequests[req] = true
}
