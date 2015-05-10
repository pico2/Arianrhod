package ml

import (
    "runtime"
    _ "ml/console"
)

func init() {
    runtime.GOMAXPROCS(runtime.NumCPU())
}
