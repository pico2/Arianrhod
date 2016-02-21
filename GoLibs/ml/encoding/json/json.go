package json

import (
    . "ml/trace"
    . "ml/dict"

    "os"
    "io/ioutil"
)

func MustMarshal(v interface{}) []byte {
    data, err := Marshal(v)
    RaiseIf(err)
    return data
}

func MustMarshalIndent(v interface{}, prefix, indent string) []byte {
    data, err := MarshalIndent(v, prefix, indent)
    RaiseIf(err)
    return data
}

func LoadFile(file string) JsonDict {
    f, err := os.Open(file)
    if err != nil {
        Raise(NewFileNotFoundError(err.Error()))
    }

    defer f.Close()

    data, err := ioutil.ReadAll(f)
    if err != nil {
        Raise(NewBaseException(err.Error()))
    }

    return LoadData(data)
}

func LoadData(data []byte) JsonDict {
    v := JsonDict{}

    err := Unmarshal(data, &v)
    if err != nil {
        Raise(NewJSONDecodeError(err.Error()))
    }

    return v
}

func LoadString(text string) JsonDict {
    return LoadData([]byte(text))
}
