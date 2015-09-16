package main

import (
    _ "ml"
    . "fmt"
    // "ml/console"
    "ml/net/pop3"
    "net/mail"
    "strings"
    "io/ioutil"
    . "ml/trace"
)

// func run() error {
//     engine := qml.NewEngine()
//     component, err := engine.LoadFile(`D:\Dev\Library\Qt\Examples\Qt-5.5\quick\controls\gallery\qml\InputPage.qml`)
//     if err != nil {
//         return err
//     }

//     window := component.CreateWindow(nil)
//     window.Show()
//     window.Wait()
//     return nil
// }

func main2() {
    c, err := pop3.DialTLS("pop3.sohu.com:995")
    RaiseIf(err)

    Println(c.Auth("", ""))
    _, sizes, err := c.ListAll()
    RaiseIf(err)

    for i := 0; i != len(sizes); i++ {
        text, err := c.Retr(i + 1)
        RaiseIf(err)

        m, err := mail.ReadMessage(strings.NewReader(text))
        RaiseIf(err)
        Println(m.Header)
        body, err := ioutil.ReadAll(m.Body)
        RaiseIf(err)
        Println("body\n", string(body))
    }
}

func main() {
    // defer console.Pause("done")
    main2()
    return

    // if err := qml.Run(run); err != nil {
    //     Printf("error: %v\n", err)
    //     console.Pause("done")
    // }
}
