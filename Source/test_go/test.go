package main

import (
    _ "ml"
    . "fmt"
    "goqml"
)

func run() error {
    q := `
        import QtQuick 2.0

        Rectangle {
            id: page
            width: 320; height: 480
            color: "lightgray"

            Text {
                id: helloText
                text: "Hello world!"
                y: 30
                anchors.horizontalCenter: page.horizontalCenter
                font.pointSize: 24; font.bold: true
            }
        }
    `

    engine := qml.NewEngine()
    component, err := engine.LoadString("fuck.qml", q)
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
