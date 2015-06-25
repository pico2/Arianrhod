package ml

import (
    "runtime"
    "syscall"
    "ml/strings"
    "ml/array"
    "ml/console"
)

/* ++

  console

-- */

type _Console struct {
    Pause func(...string)
}

var Console = _Console{Pause : console.Pause}


/* ++

  strings

-- */

func Str(s string) strings.String {
    return strings.String(s)
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

/* ++

    init

-- */

func fixTimePeriod() {
    syscall.MustLoadDLL("winmm.dll").MustFindProc("timeEndPeriod").Call(uintptr(1))
}

func init() {
    runtime.GOMAXPROCS(runtime.NumCPU())

    if runtime.GOOS == "windows" {
        fixTimePeriod()
    }
}
