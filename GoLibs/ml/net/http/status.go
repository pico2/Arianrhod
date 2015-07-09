package http

import (
    gohttp "net/http"
)

const (
    StatusContinue                      = gohttp.StatusContinue
    StatusSwitchingProtocols            = gohttp.StatusSwitchingProtocols

    StatusOK                            = gohttp.StatusOK
    StatusCreated                       = gohttp.StatusCreated
    StatusAccepted                      = gohttp.StatusAccepted
    StatusNonAuthoritativeInfo          = gohttp.StatusNonAuthoritativeInfo
    StatusNoContent                     = gohttp.StatusNoContent
    StatusResetContent                  = gohttp.StatusResetContent
    StatusPartialContent                = gohttp.StatusPartialContent

    StatusMultipleChoices               = gohttp.StatusMultipleChoices
    StatusMovedPermanently              = gohttp.StatusMovedPermanently
    StatusFound                         = gohttp.StatusFound
    StatusSeeOther                      = gohttp.StatusSeeOther
    StatusNotModified                   = gohttp.StatusNotModified
    StatusUseProxy                      = gohttp.StatusUseProxy
    StatusTemporaryRedirect             = gohttp.StatusTemporaryRedirect

    StatusBadRequest                    = gohttp.StatusBadRequest
    StatusUnauthorized                  = gohttp.StatusUnauthorized
    StatusPaymentRequired               = gohttp.StatusPaymentRequired
    StatusForbidden                     = gohttp.StatusForbidden
    StatusNotFound                      = gohttp.StatusNotFound
    StatusMethodNotAllowed              = gohttp.StatusMethodNotAllowed
    StatusNotAcceptable                 = gohttp.StatusNotAcceptable
    StatusProxyAuthRequired             = gohttp.StatusProxyAuthRequired
    StatusRequestTimeout                = gohttp.StatusRequestTimeout
    StatusConflict                      = gohttp.StatusConflict
    StatusGone                          = gohttp.StatusGone
    StatusLengthRequired                = gohttp.StatusLengthRequired
    StatusPreconditionFailed            = gohttp.StatusPreconditionFailed
    StatusRequestEntityTooLarge         = gohttp.StatusRequestEntityTooLarge
    StatusRequestURITooLong             = gohttp.StatusRequestURITooLong
    StatusUnsupportedMediaType          = gohttp.StatusUnsupportedMediaType
    StatusRequestedRangeNotSatisfiable  = gohttp.StatusRequestedRangeNotSatisfiable
    StatusExpectationFailed             = gohttp.StatusExpectationFailed
    StatusTeapot                        = gohttp.StatusTeapot

    StatusInternalServerError           = gohttp.StatusInternalServerError
    StatusNotImplemented                = gohttp.StatusNotImplemented
    StatusBadGateway                    = gohttp.StatusBadGateway
    StatusServiceUnavailable            = gohttp.StatusServiceUnavailable
    StatusGatewayTimeout                = gohttp.StatusGatewayTimeout
    StatusHTTPVersionNotSupported       = gohttp.StatusHTTPVersionNotSupported
)

func StatusText(code int) string {
    return gohttp.StatusText(code)
}
