package strings

import (
    "fmt"
)

var cptable = map[int]codePageTableInfo {}

type Encoder struct {
    codepage int
    table codePageTableInfo
}

func (self *Encoder) Encode(str String) []byte {
    return UnicodeToCustomCPN(&self.table, str)
}

func (self *Encoder) Decode(bytes []byte) String {
    return CustomCPToUnicodeN(&self.table, bytes)
}

func (self *Encoder) String() string {
    return cptext[self.codepage] + " encoder"
}

func GetEncoder(codepage int) (*Encoder) {
    table, ok := cptable[codepage]

    if !ok {
        panic(fmt.Sprintf("can't find encoder for codepage %v", codepage))
    }

    table.initialize()

    return &Encoder{
                codepage: codepage,
                table: table,
            }
}

func init() {
}
