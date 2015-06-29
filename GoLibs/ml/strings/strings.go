package strings

import (
    "strings"
    "unicode/utf8"
)

type String string

func (self String) String() string {
    return string(self)
}

func (self *String) SizeInBytes() (int) {
    return len(*self)
}

func (self *String) Length() (int) {
    return utf8.RuneCountInString(string(*self))
}

func (self *String) IsEmpty() bool {
    return len(*self) == 0
}

func (self *String) Encode(encoding int) []byte {
    return GetEncoder(encoding).Encode(*self)
}

func Decode(bytes []byte, encoding int) String {
    return GetEncoder(encoding).Decode(bytes)
}

func (self *String) Replace(old, new String, count ...int) String {
    var n = 0

    switch len(count) {
        case 0:
            n = -1

        default:
            n = count[0]
    }

    return String(strings.Replace(string(*self), string(old), string(new), n))
}

func (self *String) Contains(substr String) bool {
    return strings.Contains(string(*self), string(substr))
}

func (self *String) ContainsAny(chars String) bool {
    return strings.ContainsAny(string(*self), string(chars))
}

func (self *String) ContainsRune(r rune) bool {
    return strings.ContainsRune(string(*self), r)
}

func (self *String) Count(sep String) int {
    return strings.Count(string(*self), string(sep))
}

func (self *String) Find(sub String) int {
    return self.Index(sub)
}

func (self *String) Index(sep String) int {
    return strings.Index(string(*self), string(sep))
}

func (self *String) StartsWith(prefix String) bool {
    return strings.HasPrefix(string(*self), string(prefix))
}

func (self *String) EndsWith(suffix String) bool {
    return strings.HasSuffix(string(*self), string(suffix))
}

func (self *String) ToLower() String {
    return String(strings.ToLower(string(*self)))
}

func (self *String) ToUpper() String {
    return String(strings.ToUpper(string(*self)))
}

func (self *String) Trim(cutset ...String) String {
    s := " "

    if len(cutset) > 0 {
        s = string(cutset[0])
    }

    return String(strings.Trim(string(*self), s))
}

func (self *String) Join(a interface{}) String {
    var ss []string

    switch v := a.(type) {
        case []string:
            ss = v

        case []String:
            ss = make([]string, len(v))
            for i := range v {
                ss[i] = string(v[i])
            }

        default:
            panic("only []string and []String can be joined")
    }

    return String(strings.Join(ss, string(*self)))
}

func (self *String) Split(sep String, maxSplit ...int) []String {
    var max int = 0

    switch len(maxSplit) {
        case 1:
            max = maxSplit[0]

        default:
            max = -1
    }

    switch {
        case max < 0:
            fallthrough
        case max == 0:
            max = -1

        case max > 0:
            max++
    }

    subs := strings.SplitN(string(*self), string(sep), max)
    ss := make([]String, len(subs))

    for i := range subs {
        ss[i] = String(subs[i])
    }

    return ss
}

func (self *String) RSplit(sep String, maxSplit ...int) []String {
    var max int = 0

    switch len(maxSplit) {
        case 1:
            max = maxSplit[0]

        default:
            max = -1
    }

    switch {
        case max < 0:
            fallthrough
        case max == 0:
            max = -1

        case max > 0:
            max++
    }

    subs := self.Split(sep, -1)
    if max < 0 {
        return subs
    }

    max--

    ss := make([]String, max + 1)
    ss[0] = sep.Join(subs[:len(subs) - max])

    for i, v := range subs[len(subs) - max:] {
        ss[i + 1] = v
    }

    return ss
}

func init() {
}
