package ml

import (
    "runtime"
    "ml/strings"
    // "ml/array"
    // "ml/console"
)

/* ++

  console

-- */

// type _Console struct {
//     Pause func(...string)
// }

// var Console = _Console{Pause : console.Pause}


/* ++

  strings

-- */

func Str(s string) strings.String {
    return strings.String(s)
}


/* ++

  array

-- */

// func Array(values ...interface{}) array.Array {
//     return array.Array(values)
// }


/* ++

  dict

-- */

/* ++

    init

-- */

func init() {
    runtime.GOMAXPROCS(runtime.NumCPU())
}
