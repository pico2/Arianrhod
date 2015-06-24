package encoding

import (
    . "ml/str"
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
        return nil
    }

    table.initialize()

    return &Encoder{
                codepage: codepage,
                table: table,
            }
}

func init() {
}
