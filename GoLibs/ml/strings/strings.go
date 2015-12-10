package strings

import (
    . "fmt"
    // . "ml/dict"
    . "ml/trace"

    "bytes"
    "text/template"
    "strings"
    "strconv"
    "unicode/utf8"
    "encoding/hex"
)

type String string

func Format(format interface{}, params interface{}) String {
    t := template.Must(template.New("").Parse(Sprintf("%v", format)))
    b := bytes.NewBufferString("")

    RaiseIf(t.Execute(b, params))

    return String(b.String())
}

func (self String) String() string {
    return string(self)
}

func (self String) SizeInBytes() int {
    return len(self)
}

func (self String) Length() int {
    return utf8.RuneCountInString(string(self))
}

func (self String) IsEmpty() bool {
    return len(self) == 0
}

func (self String) IsDigit() bool {
    _, err := strconv.ParseInt(self.String(), 10, 64)
    return err == nil
}

func (self String) ToInteger(base ...int) int64 {
    if len(base) == 0 {
        base = append(base, 10)
    }

    val, err := strconv.ParseInt(self.String(), base[0], 64)
    RaiseIf(err)
    return val
}

func (self String) HexStringToBytes() []byte {
    data, err := hex.DecodeString(self.String())
    RaiseIf(err)
    return data
}

func (self String) Format(params interface{}) String {
    return Format(self, params)
}

func (self String) Encode(encoding Encoding) []byte {
    return GetEncoder(encoding).Encode(self)
}

func Decode(bytes []byte, encoding Encoding) String {
    return GetEncoder(encoding).Decode(bytes)
}

func (self String) Capitalize() String {
    if self.Length() == 0 {
        return self
    }

    return String(self[:1]).ToUpper() + String(self[1:])
}

func (self String) Replace(old, new String, count ...int) String {
    var n = 0

    switch len(count) {
        case 0:
            n = -1

        default:
            n = count[0]
    }

    return String(strings.Replace(string(self), string(old), string(new), n))
}

func (self String) Contains(substr String) bool {
    return strings.Contains(string(self), string(substr))
}

func (self String) ContainsAny(chars String) bool {
    return strings.ContainsAny(string(self), string(chars))
}

func (self String) ContainsRune(r rune) bool {
    return strings.ContainsRune(string(self), r)
}

func (self String) Count(sep String) int {
    return strings.Count(string(self), string(sep))
}

func (self String) Find(sub String) int {
    return self.Index(sub)
}

func (self String) Index(sep String) int {
    return strings.Index(string(self), string(sep))
}

func (self String) StartsWith(prefix String) bool {
    return strings.HasPrefix(string(self), string(prefix))
}

func (self String) EndsWith(suffix String) bool {
    return strings.HasSuffix(string(self), string(suffix))
}

func (self String) ToLower() String {
    return String(strings.ToLower(string(self)))
}

func (self String) ToUpper() String {
    return String(strings.ToUpper(string(self)))
}

func (self String) Trim(cutset ...String) String {
    s := " "

    if len(cutset) > 0 {
        s = string(cutset[0])
    }

    return String(strings.Trim(string(self), s))
}

func (self String) Join(a interface{}) String {
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

    return String(strings.Join(ss, string(self)))
}

func (self String) SplitLines(separator ...String) []String {
    var sep String
    switch len(separator) {
        case 1:
            sep = separator[0]

        default:
            sep = "\n"
    }

    return self.Replace("\r\n", "\n").Replace("\r", "\n").Split(sep)
}

func (self String) Split(sep String, maxSplit ...int) []String {
    var max int = 0

    switch len(maxSplit) {
        case 1:
            max = maxSplit[0]

        default:
            max = -1
    }

    switch {
        case max <= 0:
            max = -1

        case max > 0:
            max++
    }

    subs := strings.SplitN(string(self), string(sep), max)
    ss := make([]String, len(subs))

    for i := range subs {
        ss[i] = String(subs[i])
    }

    return ss
}

func (self String) RSplit(sep String, maxSplit ...int) []String {
    var max int = 0

    switch len(maxSplit) {
        case 1:
            max = maxSplit[0]

        default:
            max = -1
    }

    switch {
        case max <= 0:
            max = -1

        case max > 0:
            max++
    }

    subs := self.Split(sep, -1)
    if max < 0 {
        return subs
    }

    max--

    ss := make([]String, max+1)
    ss[0] = sep.Join(subs[:len(subs)-max])

    for i, v := range subs[len(subs)-max:] {
        ss[i+1] = v
    }

    return ss
}

func (self String) NewReader() *strings.Reader {
    return strings.NewReader(string(self))
}
