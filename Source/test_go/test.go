package main

import (
    _ "ml"
    "ml/console"
    . "fmt"
    "goqml"
    // _ "./resource"
)

func run() error {
    engine := qml.NewEngine()
    component, err := engine.LoadFile(`D:\Dev\Library\Qt\Examples\Qt-5.5\quick\controls\gallery\qml\InputPage.qml`)
    if err != nil {
        return err
    }

    window := component.CreateWindow(nil)
    window.Show()
    window.Wait()
    return nil
}

type String2 struct {
    string
}

func funcTakeString(str string) {
    Println(str)
}

func main() {
    // f := "normal string"
    // var x String2 = f

    // Printf("%T\n", x)
    // funcTakeString(x)

    // return

    if err := qml.Run(run); err != nil {
        Printf("error: %v\n", err)
        console.Pause("done")
    }
}
