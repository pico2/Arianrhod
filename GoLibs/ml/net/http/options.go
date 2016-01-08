package http

import (
    . "ml/array"
)

type RequestOptions struct {
    DontReadResponseBody    bool
    IgnoreEncodeKeys        Array
    OverwriteHeaders        bool
}
