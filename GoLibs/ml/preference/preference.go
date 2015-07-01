package preference

import (
    "encoding/json"
    "os"
    "io/ioutil"
)

func LoadFile(fileName string, v interface{}) error {
    file, err := os.Open(fileName)
    if err != nil {
        return err
    }

    defer file.Close()

    buf, err := ioutil.ReadAll(file)
    if err != nil {
        return err
    }

    return json.Unmarshal(buf, v)
}
