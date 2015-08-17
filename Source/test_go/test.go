package main

import (
    // . "ml"
    // . "ml/trace"
    // "ml/net/http"
    // "ml/console"
    // "time"
    "github.com/andlabs/ui"
)

func main() {
    var window ui.Window

    go ui.Do(func() {
        name := ui.NewTextField()
        button := ui.NewButton("Greet")
        greeting := ui.NewLabel("")
        stack := ui.NewVerticalStack(
            ui.NewLabel("Enter your name:"),
            name,
            button,
            greeting)
        window = ui.NewWindow("Hello", 200, 100, stack)
        button.OnClicked(func() {
            greeting.SetText("Hello, " + name.Text() + "!")
        })
        window.OnClosing(func() bool {
            ui.Stop()
            return true
        })
        window.Show()
    })
    err := ui.Go()
    if err != nil {
        panic(err)
    }
}
