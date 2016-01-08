package json

import (
    . "ml/trace"
)

func MustMarshal(v interface{}) []byte {
    data, err := Marshal(v)
    RaiseIf(err)
    return data
}
