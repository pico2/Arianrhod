package eff

import (
    . "fmt"
    . "ml/strings"
    . "ml/trace"

    "path/filepath"
    "ml/encoding/json"
    "ml/io2/filestream"
    "bytes"
    "encoding/binary"

    "../../utility"
)

const (
    partDataCount = 16
)

type edaoEffFileHeader struct {
    Magic           magicByteArray      //  0x0000
    Name            textByteArray       //  0x0004
    Unknown         uint16              //  0x0014
    Padding         uint16              //  0x0016
    Flags           uint16              //  0x0018
    PartDataBits    uint16              //  0x001A
    Texture         [4]textByteArray    //  0x001C
    Children        [2]textByteArray    //  0x005C
    // PartData        [16][]edaoPartData  //  0x007C
}

type effCoord struct {
    X effFloat
    Y effFloat
    Z effFloat
}

type PartDataFlags uint32

const (
    NoTextureName           = 0x00000001
    BlendMode1              = 0x00000002
    BlendMode2              = 0x00000004
    BlendMode3              = 0x00000040
    Culling1                = 0x00000800
    Culling2                = 0x00008000
)

type edaoPartData struct {                      // 0x3B8 bytes
    Header struct {                             // 0x0050 bytes
        Name                    textByteArray   // 0x0000
        Byte_10                 byte            // 0x0010
        Byte_11                 byte            // 0x0011
        ExtraCount              byte            // 0x0012
        Byte_13                 byte            // 0x0013
        Flags                   uint32          // 0x0014
        Uint_18                 uint32          // 0x0018
        Float_1C                effFloat         // 0x001C
        Byte_1C                 [0x1C]byte      // 0x0020
        Byte_3C                 byte            // 0x003C
        Byte_3D                 byte            // 0x003D
        TextureIndex            byte            // 0x003E
        Byte_3F                 byte            // 0x003F
        Byte_40                 byte            // 0x0040
        Byte_41                 byte            // 0x0041
        Byte_42                 byte            // 0x0042
        Byte_43                 byte            // 0x0043
        Coord_44                effCoord        // 0x0044
    }

    Coord_50                    effCoord        // 0x0050
    Coord_5C                    effCoord        // 0x005C
    Float_68                    effFloat         // 0x0068
    Float_6C                    effFloat         // 0x006C
    Float_70                    effFloat         // 0x0070
    Float_74                    effFloat         // 0x0074
    Uint_78                     uint32          // 0x0078
    Float_7C                    effFloat         // 0x007C
    Float_80                    effFloat         // 0x0080
    Float_84                    effFloat         // 0x0084
    Float_88                    effFloat         // 0x0088
    Float_8C                    effFloat         // 0x008C
    Float_90                    effFloat         // 0x0090
    Float_94                    effFloat         // 0x0094
    Float_98                    effFloat         // 0x0098
    Uint_9C                     uint32          // 0x009C
    Uint_A0                     uint32          // 0x00A0
    Coord_A4                    effCoord        // 0x00A4
    Coord_B0                    effCoord        // 0x00B0
    Coord_BC                    effCoord        // 0x00BC
    Ushort_C8                   uint16          // 0x00C8
    Ushort_CA                   uint16          // 0x00CA
    Ushort_CC                   uint16          // 0x00CC
    Ushort_CE                   uint16          // 0x00CE
    Ushort_D0                   uint16          // 0x00D0
    Ushort_D2                   uint16          // 0x00D2
    Uint_D4                     uint32          // 0x00D4
    Uint_D8                     uint32          // 0x00D8
    Float_DC                    [36]effFloat     // 0x00DC
    Float_16C                   [36]effFloat     // 0x016C
    Float_1FC                   [36]effFloat     // 0x01FC
    Float_28C                   [36]effFloat     // 0x028C
    Uint_31C                    [16]uint32      // 0x031C
    Uint_35C                    [16]uint32      // 0x035C
    Options                     [8]byte         // 0x039C

    Struct_3A4 struct {
        Ushort_3A4              uint16          // 0x03A4
        Ushort_3A6              uint16          // 0x03A6
        Uint_3A8                uint32          // 0x03A8
        Uint_3AC                uint32          // 0x03AC
        Uint_3B0                uint32          // 0x03B0
        Uint_3B4                uint32          // 0x03B4
    }

    // [Header.ExtraCount]edaoPartDataExtra
}

type edaoPartDataExtra struct {
    Byte_00     byte
    Byte_01     byte
    Byte_02     byte
    Byte_03     byte
    Uint_04     uint32
    Uint_08     uint32
    Coord_0C    effCoord
}

type EDAOPartData struct {
    edaoPartData

    Extra []edaoPartDataExtra
}

type EDAOEffect struct {
    *EffectBase

    Magic           String
    Unknown         int
    Flags           int
    PartDataBits    int
    PartData        [partDataCount]*EDAOPartData
}

func LoadEDAOEffect(jsonpath string) *EDAOEffect {
    f := filestream.Open(jsonpath)
    defer f.Close()

    eff := &EDAOEffect{}
    eff.Unserialize(f.ReadAll())

    return eff
}

func NewEDAOEffect(effpath string) *EDAOEffect {
    f := filestream.Open(effpath)
    defer f.Close()

    header := f.ReadType(edaoEffFileHeader{}).(edaoEffFileHeader)

    eff := &EDAOEffect{
        EffectBase      : newEffectBase(),
        Magic           : utility.BytesToString(header.Magic[:]),
        Unknown         : int(header.Unknown),
        Flags           : int(header.Flags),
        PartDataBits    : int(header.PartDataBits),
        PartData        : [partDataCount]*EDAOPartData{},
    }

    eff.fileName = String(filepath.Base(effpath))
    eff.name = utility.BytesToString(header.Name[:])

    for _, texture := range header.Texture {
        t := utility.BytesToString(texture[:])
        eff.texture = append(eff.texture, t)
    }

    for _, child := range header.Children {
        c := utility.BytesToString(child[:])
        eff.children = append(eff.children, c)
    }

    for i := uint(0); i != partDataCount; i++ {
        if ((1 << i) & eff.PartDataBits) == 0 {
            continue
        }

        part := &EDAOPartData{
            edaoPartData: f.ReadType(edaoPartData{}).(edaoPartData),
            Extra: []edaoPartDataExtra{},
        }

        for j := uint(0); j != uint(part.Header.ExtraCount); j++ {
            part.Extra = append(part.Extra, f.ReadType(edaoPartDataExtra{}).(edaoPartDataExtra))
        }

        eff.PartData[i] = part
    }

    return eff
}

func (self *EDAOEffect) PartDataNames() []String {
    v := []String{}

    for _, part := range self.PartData {
        if part == nil {
            v = append(v, "NONE")
            continue
        }

        v = append(v, String(Sprintf("%q", utility.BytesToString(part.Header.Name[:]))))
    }

    return v
}

func (self EDAOEffect) String() string {
    return String("\n").Join([]string{
        Sprintf("Magic          = %v",      self.Magic),
        Sprintf("FileName       = %v",      self.FileName()),
        Sprintf("Name           = %v",      self.Name()),
        Sprintf("Unknown        = %08X",    self.Unknown),
        Sprintf("Flags          = %08X",    self.Flags),
        Sprintf("Texture        = %v",      String(" ").Join(self.Texture())),
        Sprintf("Children       = %v",      String(" ").Join(self.Children())),
        Sprintf("PartDataBits   = %08X",    self.PartDataBits),
        Sprintf("Parts          = %v",      String(" ").Join(self.PartDataNames())),
        Sprintf("data           = %v",      self.PartData),
    }).String()
}

func (self *EDAOEffect) Serialize() (data []byte) {
    data, err := json.MarshalIndent(self, "", "  ")
    RaiseIf(err)
    return
}

func (self *EDAOEffect) Unserialize(data []byte) {
    RaiseIf(json.Unmarshal(data, self))
}

func (self *EDAOEffect) ToBinary() (data []byte) {
    buf := filestream.CreateMemory()

    header := edaoEffFileHeader{
        Unknown         : uint16(self.Unknown),
        Flags           : uint16(self.Flags),
        PartDataBits    : uint16(self.PartDataBits),
    }

    copy(header.Magic[:], self.Magic.Encode(utility.ENCODING))
    copy(header.Name[:], self.Name().Encode(utility.ENCODING))

    texture := self.Texture()
    for i, _ := range header.Texture {
        copy(header.Texture[i][:], texture[i].Encode(utility.ENCODING))
    }

    children := self.Children()
    for i, _ := range header.Children {
        copy(header.Children[i][:], children[i].Encode(utility.ENCODING))
    }

    buf.WriteType(&header)

    for _, part := range self.PartData {
        if part == nil {
            continue
        }

        buf.WriteType(&part.edaoPartData)

        for _, extra := range part.Extra {
            buf.WriteType(&extra)
        }
    }

    buf.SetPosition(0)
    data = buf.ReadAll()

    return
}
