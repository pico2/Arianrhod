package test

import (
    . "fmt"
    . "ml/strings"

    "testing"
    "path/filepath"
    "os"
    "encoding/json"
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

        p := String(path)

        if p.EndsWith(".eff") == false {
            return nil
        }

        if p.EndsWith("sysatk07.eff") == false {
            // return nil
        }

        e := eff.NewEDAOEffect(path)

        Println(e)
        Println()

        b, err := json.MarshalIndent(e, "", "  ")
        Println(err)

        e = eff.EDAOEffectFromJson(b)
        b, err = json.MarshalIndent(e, "", "  ")

        f, _ := os.Create(`D:\Desktop\Source\Falcom\EDTools\fuck.json`)
        f.Write(b)
        f.Close()

        return Errorf("break")

        return nil
    })
}
