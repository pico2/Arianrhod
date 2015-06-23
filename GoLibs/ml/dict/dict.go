package dict

import (
    "fmt"
)

type Dict map[interface{}]interface{};

func (self Dict) toString(depth int) string {

    space := ""

    for ; depth > 0; depth-- {
        space += "  "
    }

    s := "{\n"
    for k, v := range self {
        var key, value string

        switch t := k.(type) {
            case string:
                key = fmt.Sprintf("'%v'", t)

            default:
                key = fmt.Sprintf("%v", t)
        }

        switch v.(type) {
            case Dict:
                value = v.(Dict).toString(depth + 1)

            case string:
                value = fmt.Sprintf("'%v'", v)

            default:
                value = fmt.Sprintf("%+v", v)
        }

        s += fmt.Sprintf("%v  %+v: %+v,\n", space, key, value)
    }

    s += space + "}"

    return s

}

func (self Dict) String() string {
    return self.toString(0)

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
