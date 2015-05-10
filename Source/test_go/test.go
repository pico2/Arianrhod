package main

import (
    _ "ml"
    "ml/console"
    "log"
    "os"
)

type Job struct {
    Command string
    *log.Logger
}

func main() {
    jog := &Job{"command", log.New(os.Stderr, "[fucker] ", log.LstdFlags)}

    jog.Print("fucking")

    console.Pause("FUCK")
}
