package eff

import (
    . "ml/strings"
    "ml/io2/filestream"
)

type edaoEffFile struct {
    Magic           [4]byte             //  0x0000
    Name            [16]byte            //  0x0004
    Unknown         uint16              //  0x0014
    Padding         uint16              //  0x0016
    Count           uint16              //  0x0018
    PartDataBits    uint16              //  0x001A

    Texture         [4][16]byte         //  0x001C
    Children        [2][16]byte         //  0x005C
    // PartData        [16][]edaoPartData  //  0x007C
}

type edaoPartData struct {
    // data    [398]byte

    Header struct {
        // 0x0050
        Header      [4]uint32       // 0x0000
        Byte_10     byte            // 0x0010
        Byte_11     byte            // 0x0011
        TailCount   byte            // 0x0012
        Byte_13     byte            // 0x0013
        uint_14     uint32          // 0x0014
        Byte_18     byte            // 0x0018
        Byte_19     byte            // 0x0019
        Byte_1A     byte            // 0x001A
        Byte_1B     byte            // 0x001B
        Float_1C    [8]float32      // 0x001C
        Byte_3C     byte            // 0x003C
        Byte_3D     byte            // 0x003D
        Byte_3E     byte            // 0x003E
        Byte_3F     byte            // 0x003F
        Byte_40     byte            // 0x0040
        Byte_41     byte            // 0x0041
        Byte_42     byte            // 0x0042
        Byte_43     byte            // 0x0043
        Float_44    [3]float32      // 0x0044
    }

    Float_50        [3]float32      // 0x0050
    Float_5C        [3]float32      // 0x005C
    Float_68        float32         // 0x0068
    Float_6C        float32         // 0x006C
    Float_70        float32         // 0x0070
    Float_74        float32         // 0x0074
}

type EDAOEffect struct {
    *EffectBase
}

func NewEDAOEffect(effpath String) {
    f := filestream.Open(effpath.String())

    eff := f.ReadType(edaoEffFile{}).(edaoEffFile)
}
