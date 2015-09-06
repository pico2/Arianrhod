package main

import (
    . "fmt"
    "internal/syscall/windows/registry"
)

func getCmdDefaultPosition() (uint64, error) {
    key, err := registry.OpenKey(registry.CURRENT_USER, `Console\%SystemRoot%_system32_cmd.exe`, registry.QUERY_VALUE)
    if err != nil {
        return 0, err
    }

    defer key.Close()
    v, _, err := key.GetIntegerValue("WindowPosition")

    return v, err
}

func setConsoleDefaultPosition(pos uint64) error {
    key, err := registry.OpenKey(registry.CURRENT_USER, "Console", registry.SET_VALUE)
    if err != nil {
        return err
    }

    defer key.Close()
    return key.SetDWordValue("WindowPosition", uint32(pos))
}

func main() {
    pos, err := getCmdDefaultPosition()
    if err != nil {
        Println(err)
        return
    }

    err = setConsoleDefaultPosition(pos)
    if err != nil {
        Println(err)
        return
    }

    Println("done")
}
