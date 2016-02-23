package console

import (
    "syscall"
    "unsafe"
)

var (
    getch           *syscall.Proc
    setConsoleTitle *syscall.Proc
)

func pause() {
    getch.Call()
}

func setTitle(text string) {
    setConsoleTitle.Call(uintptr(unsafe.Pointer(syscall.StringToUTF16Ptr(text))))
}

func init() {
    getch = syscall.MustLoadDLL("msvcrt.dll").MustFindProc("_getch")
    setConsoleTitle = syscall.MustLoadDLL("kernel32.dll").MustFindProc("SetConsoleTitleW")
}
