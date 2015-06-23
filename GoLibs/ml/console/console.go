package console

import (
    "syscall"
    syscall2 "ml/syscall"
)

var getch = uintptr(0)

func Pause(text ...string) {
    if len(text) != 0 {
        print(text[0])
    }

    syscall2.Call(uintptr(getch), uintptr(0), 0, 0, 0)
}

func init() {
    msvcrt, _ := syscall.LoadLibrary("msvcrt.dll")
    getch1, _ := syscall.GetProcAddress(msvcrt, "_getch")

    getch = getch1
}
