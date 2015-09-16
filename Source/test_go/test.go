package main

import (
    _ "ml"
    . "fmt"
    // "ml/console"
    "ml/net/pop3"
    "net/mail"
    "strings"
    "io/ioutil"
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
    Println(err)

    Println(c.Auth("", ""))
    _, sizes, err := c.ListAll()
    Println(err)

    for i := 0; i != len(sizes); i++ {
        text, err := c.Retr(i + 1)
        Println(err)

        m, err := mail.ReadMessage(strings.NewReader(text))
        Println(err)
        Println(m.Header)
        body, err := ioutil.ReadAll(m.Body)
        Println(err)
        Println(string(body))
    }
}

func main() {
    main2()
    return

    // if err := qml.Run(run); err != nil {
    //     Printf("error: %v\n", err)
    //     console.Pause("done")
    // }
}
