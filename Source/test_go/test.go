package main

import (
    _ "ml"
    . "fmt"
    "goqml"
)

func run() error {
    engine := qml.NewEngine()
    component, err := engine.LoadFile("resource/fuck.qml")
    if err != nil {
        return err
    }

    window := component.CreateWindow(nil)
    window.Show()
    window.Wait()
    return nil
}

func main() {
    switch ("fuck") {
        case "1", "fuck":
            Println("case fuck")
    }

    if err := qml.Run(run); err != nil {
        Printf("error: %v\n", err)
    }
}
