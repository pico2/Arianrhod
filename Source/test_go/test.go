package main

import (
    _ "ml"
    "ml/console"
    "path/filepath"
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
    Println(filepath.Join(`D:\Desktop\Source\Project\Private\bettor\common\match`, `../site`))
    Println(`../site`[0] == '.')
    return

    if err := qml.Run(run); err != nil {
        Printf("error: %v\n", err)
        console.Pause("done")
    }
}
