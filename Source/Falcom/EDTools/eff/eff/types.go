package eff

import (
    . "fmt"
    "math"
    "strconv"
    "bytes"
    "ml/strings"
    "../../utility"
)

type effFloat float32
type textByteArray [16]byte
type magicByteArray [4]byte

func (self textByteArray) MarshalJSON() (data []byte, err error) {
    data = []byte(Sprintf(`"%v"`, utility.BytesToString(self[:])))
    return
}

func (self magicByteArray) MarshalJSON() (data []byte, err error) {
    data = []byte(Sprintf(`"%v"`, utility.BytesToString(self[:])))
    return
}

func (self *textByteArray) UnmarshalJSON(data []byte) (err error) {
    str := strings.Decode(data, strings.CP_UTF8).Encode(utility.ENCODING)
    str = str[1:len(str) - 1]
    if len(str) > len(self) {
        str = str[:len(self)]
    }
    copy(self[:], str[:])
    return
}

func (self *magicByteArray) UnmarshalJSON(data []byte) (err error) {
    str := strings.Decode(data, strings.CP_UTF8)
    str = str[1:len(str) - 1]
    if len(str) > len(self) {
        str = str[:len(self)]
    }
    copy(self[:], str[:])
    return
}

func (self effFloat) MarshalJSON() (data []byte, err error) {
    if math.IsNaN(self.Float64()) {
        data = []byte(`"NaN"`)
        return
        self = -1.0
    }

    data = []byte(Sprintf("%v", self))
    return
}

func (self *effFloat) UnmarshalJSON(data []byte) (err error) {
    if bytes.Compare(data, []byte(`"NaN"`)) == 0 {
        *self = effFloat(math.NaN())
        return
    }

    f, err := strconv.ParseFloat(string(data), 64)
    if err == nil {
        *self = effFloat(f)
    }

    return
}

func (self effFloat) Float32() float32 {
    return float32(self)
}

func (self effFloat) Float64() float64 {
    return float64(self)
}