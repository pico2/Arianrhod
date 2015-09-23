package macho

type Section struct {
    SectionName         [16]byte
    SegmentName         [16]byte
    Address             uint32
    Size                uint32
    Offset              uint32
    Align               uint32
    RelocationOffset    uint32
    NumberOfRelocations uint32
    Flags               uint32
    reserved1           uint32
    reserved2           uint32
}

type Section64 struct {
    SectionName         [16]byte
    SegmentName         [16]byte
    Address             uint64
    Size                uint64
    Offset              uint32
    Align               uint32
    RelocationOffset    uint32
    NumberOfRelocations uint32
    Flags               uint32
    reserved1           uint32
    reserved2           uint32
}
