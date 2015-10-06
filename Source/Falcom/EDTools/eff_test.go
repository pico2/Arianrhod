package test

import (
    . "fmt"
    . "ml/strings"

    "testing"
    "path/filepath"
    "os"
    "bytes"
    "ml/io2/filestream"
    "./eff/eff"
)

func TestEff(t *testing.T) {
    filepath.Walk(`D:\Game\Falcom\ED_AO\data\effect\`, func(path string, info os.FileInfo, err error) error {
        if err != nil {
            t.Fatal(err)
            return err
        }

        if info.IsDir() {
            return nil
        }

        if String(path).EndsWith(".eff") == false {
            return nil
        }

        e := eff.NewEDAOEffect(path)

        return nil
    })
}
