package console

import (
    "fmt"
)

func SetTitle(text interface{}) {
    setTitle(fmt.Sprintf("%v", text))
}

func Pause(text ...string) {
    if len(text) != 0 {
        print(text[0])
        print("\n")
    }

    pause()
}
