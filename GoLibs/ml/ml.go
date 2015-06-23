package ml

import (
    "runtime"
    "ml/str"
    "ml/array"
    "ml/console"
)

/* ++

  syscall

-- */

/* ++

  console

-- */

type _Console struct {
    Pause func(...string)
}

var Console = _Console{Pause : console.Pause}


/* ++

  str

-- */

func Str(s string) str.String {
    return str.String(s)
}


/* ++

  array

-- */

func Array(values ...interface{}) array.Array {
    return array.Array(values)
}


/* ++

  dict

-- */

func init() {
    runtime.GOMAXPROCS(runtime.NumCPU())
}
