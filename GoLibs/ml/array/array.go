package array

type Array []interface{}

func (self *Array) Index(value interface{}) (index int, found bool) {
    index = 0
    found = false

    for i, v := range *self {
        if v == value {
            index = i
            found = true
            break
        }
    }

    return
}

func (self *Array) Append(values ...interface{}) {
    *self = append(*self, values...)
}

func (self *Array) Remove(value interface{}) bool {
    index, ok := self.Index(value)

    if ok {
        self.Pop(index)
    }

    return ok
}

func (self *Array) Pop(index int) (interface{}, bool) {
    if index >= len(*self) {
        return nil, false
    }

    value := (*self)[index]
    *self = append((*self)[:index], (*self)[index + 1:]...)

    return value, true
}

func NewArray(values ...interface{}) Array {
    return Array{values}
}
