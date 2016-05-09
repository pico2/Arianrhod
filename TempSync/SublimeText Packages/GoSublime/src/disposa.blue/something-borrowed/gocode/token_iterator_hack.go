package gocode

import (
    "go/token"
)

func (ti *token_iterator) extract_struct_type2() string {
    if !ti.skip_to_left_curly() {
        return ""
    }
    if !ti.go_back() {
        return ""
    }

    if ti.token().tok != token.IDENT {
        return ""
    }
    b := ti.token().literal()
    if !ti.go_back() {
        return b
    }

    if ti.token().tok != token.PERIOD {
        return b
    }
    if !ti.go_back() {
        return b
    }

    if ti.token().tok != token.IDENT {
        return b
    }

    r := ti.token().literal() + "." + b

    var lastToken token.Token

    for ti.go_back() && ti.token().tok != token.SEMICOLON {
        lastToken = ti.token().tok
    }

    if lastToken == token.FUNC {
        return ""
    }

    return r
}
