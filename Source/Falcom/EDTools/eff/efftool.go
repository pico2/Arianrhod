package main

import (
    . "ml"
    . "fmt"
    . "ml/trace"

    "os"
    "time"
    "path/filepath"
    "ml/console"
    "ml/io2/filestream"

    "./eff"
)

func usage() {
    Println("usage:")
    Printf("  %s eff_file.eff  ==> eff_file.json\n", filepath.Base(os.Args[0]))
    Printf("  %s eff_file.json ==> eff_file.eff\n", filepath.Base(os.Args[0]))
    Println()
}

func handleJsonFile(input string) {
    success := false

    Printf("convert %s to .eff ... ", input)
    defer func () {
        Println(If(success, "success", "failed").(string))
    }()

    e := eff.LoadEDAOEffect(input)
    f, err := os.Create(filepath.Join(filepath.Dir(input), e.FileName().String()))
    RaiseIf(err)

    defer f.Close()
    f.Write(e.ToBinary())

    success = true
}

func handleEffFile(input string) {
    success := false

    Printf("convert %s to .json ... ", input)
    defer func () {
        Println(If(success, "success", "failed").(string))
    }()

    e := eff.NewEDAOEffect(input)
    e.Serialize()

    ext := filepath.Ext(input)

    f, err := os.Create(input[0:len(input) - len(ext)] + ".json")
    RaiseIf(err)

    f.Write(e.Serialize())

    success = true
}

func dofile(input string) {
    f := filestream.Open(input)
    defer f.Close()

    if string(f.Read(4)) == "EF20" {
        f.Close()
        handleEffFile(input)
    } else {
        f.Close()
        handleJsonFile(input)
    }
}

func main() {
    if len(os.Args) == 1 {
        usage()
        console.Pause("press any key to continue...")
        return
    }

    defer time.Sleep(time.Second * 3)

    for _, f := range os.Args[1:] {
        exp := Try(func () {
            dofile(f)
        })

        if exp != nil {
            Println(exp.Message)
        }
    }
}
