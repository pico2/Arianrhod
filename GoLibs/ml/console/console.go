package console

import (
    "syscall"
    "runtime"
)

var getch *syscall.Proc

func Pause(text ...string) {
    if len(text) != 0 {
        print(text[0])
        print("\n")
    }

    getch.Call()
}

func initWindows() {
    getch = syscall.MustLoadDLL("msvcrt.dll").MustFindProc("_getch")
}

func init() {
    if runtime.GOOS == "windows" {
        initWindows()
    }
}
