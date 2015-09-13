package ml

import (
    "runtime"
)

func init() {
    println(runtime.GOMAXPROCS(0))
    runtime.GOMAXPROCS(runtime.NumCPU())
}
