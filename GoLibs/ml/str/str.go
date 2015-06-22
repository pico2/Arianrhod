package str

import (
    "strings"
)

type String string

func (self String) String() string {
    return string(self)
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

func (self *String) HasPrefix(prefix String) bool {
    return strings.HasPrefix(string(*self), string(prefix))
}

func (self *String) HasSuffix(suffix String) bool {
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

func New(str string) String {
    return String(str)
}

func init() {
}
