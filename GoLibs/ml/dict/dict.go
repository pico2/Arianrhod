package dict

import (
    "fmt"
)

type Dict map[interface{}]interface{};

func (self Dict) String() string {
    s := "{\n"
    for k, v := range self {
        var key string

        switch t := k.(type) {
            case string:
                key = fmt.Sprintf("'%v'", t)

            default:
                key = fmt.Sprintf("%v", t)
        }

        s += fmt.Sprintf("  %+v: %+v\n", key, v)
    }

    s += "}"

    return s
}

func init() {

}
