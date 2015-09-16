package main

import (
    _ "ml"
    . "fmt"
    // "ml/console"
    "ml/net/pop3"
    "net/mail"
    "strings"
    "time"
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

func list(user, pass string) {
    Printf("try %s @ %s...", user, pass)
    start := time.Now()

    defer func () {
        Printf(" take %v  ", time.Now().Sub(start))
    }()

    c, err := pop3.DialTLS("pop.sina.com:995")
    RaiseIf(err)

    err = c.Auth(user, pass)
    RaiseIf(err)

    _, sizes, err := c.ListAll()
    RaiseIf(err)

    for i := 0; i != len(sizes); i++ {
        text, err := c.Retr(i + 1)
        RaiseIf(err)

        m, err := mail.ReadMessage(strings.NewReader(text))
        RaiseIf(err)
        _, err = ioutil.ReadAll(m.Body)
        RaiseIf(err)
    }
}

func main2() {
    for _, acc := range [][]string{
    } {
        exp := Try(func () {
            list(acc[0], acc[1])
        })

        if exp != nil {
            Println(strings.Trim(exp.Message, "\n"), "failed")
        } else {
            Println("success")
        }
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
