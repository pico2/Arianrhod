package main

import (
    _ "ml"
    "ml/console"
    . "fmt"
    "goqml"
    _ "./resource"
)

func run() error {
    engine := qml.NewEngine()
    component, err := engine.LoadFile("qrc:///resource/main.qml")
    if err != nil {
        return err
    }

    window := component.CreateWindow(nil)
    window.Show()
    window.Wait()
    return nil
}

func main() {
    if err := qml.Run(run); err != nil {
        Printf("error: %v\n", err)
        console.Pause("done")
    }
}
