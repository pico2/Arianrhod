package main

import (
    . "fmt"
    "encoding/json"
    "./pinyin"
    "ml/random"
    "os"
    "time"
)

func main() {
    Println(time.Unix(0, int64(1442485578335) * int64(time.Millisecond)))
    return

    py := [][]string{}
    json.Unmarshal([]byte(pinyin.Json), &py)

    domains := []string{
    }

    // names := []string{}
    nameset := map[string]bool{}

    f, _ := os.Create("names.txt")
    defer f.Close()

    // f.WriteString("INSERT IGNORE INTO appstore_buydata_appleid (username) VALUES\n")

    for i := 0; i != 3000000; i++ {
        n := random.IntRange(1, 5)
        name := ""
        for n > 0 {
            p := py[random.ChoiceIndex(py)][1]
            if len(p) > 4 {
                continue
            }

            name += p
            n--
        }

        name += Sprintf("%d%s", random.IntRange(1000, 100000), random.Choice(domains).(string))
        if nameset[name] {
            continue
        }

        nameset[name] = true

        f.WriteString("INSERT IGNORE INTO appstore_buydata_appleid (username) VALUES ")
        f.WriteString(Sprintf("('%s');\n", name))
    }
}
