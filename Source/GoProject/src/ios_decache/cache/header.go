package cache

type CacheHeader struct {
    Magic               [16]byte
    MappingOffset       uint32
    MappingCount        uint32
    ImagesOffset        uint32
    ImagesCount         uint32
    DyldBaseAddress     uint64
}

type SharedFileMappingNp struct {
    Address     uint64
    Size        uint64
    Offset      uint64
    MaxProt     int32
    InitProt    int32
}

type CacheImageInfo struct {
    Address         uint64
    ModTime         uint64
    Inode           uint64
    PathFileOffset  uint32
    Pad             uint32
}
