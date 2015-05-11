package ml

import (
    "runtime"
    "ml/str"
    "ml/array"
)

func Str(s string) str.String {
    return str.String(s)
}

func Array(values ...interface{}) array.Array {
    return array.Array(values)
}

func init() {
    runtime.GOMAXPROCS(runtime.NumCPU())
}
