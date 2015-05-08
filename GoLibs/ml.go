package ml

import (
    "syscall"
)

func PauseConsole(text ...string) {
    var (
        msvcrt, _ = syscall.LoadLibrary("msvcrt.dll")
        getch, _ = syscall.GetProcAddress(msvcrt, "_getch")
    )

    if len(text) != 0 {
        print(text[0])
    }

    syscall.Syscall(uintptr(getch), uintptr(0), 0, 0, 0)
}

func Init() {
    print("Init")
}
