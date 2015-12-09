package ituneslib

import (
    "syscall"
    "reflect"
    "path/filepath"
    "ml/os2"
)

func Initialize() {
    itunes.Initialize.Call()
}

func init() {
    base := syscall.MustLoadDLL(filepath.Join(os2.ExecutablePath(), "iTunesHelper.dll"))

    t := reflect.TypeOf(itunes)
    v := reflect.ValueOf(&itunes).Elem()
    for i, n := 0, t.NumField(); i != n; i++ {
        name := t.Field(i).Name
        v.Field(i).Set(reflect.ValueOf(base.MustFindProc(name)))
    }
}
