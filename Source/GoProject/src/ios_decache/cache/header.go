package cache

type CacheHeader struct {
    Magic               [16]byte    // e.g. "dyld_v0    i386"
    MappingOffset       uint32      // file offset to first dyld_cache_mapping_info
    MappingCount        uint32      // number of dyld_cache_mapping_info entries
    ImagesOffset        uint32      // file offset to first dyld_cache_image_info
    ImagesCount         uint32      // number of dyld_cache_image_info entries
    DyldBaseAddress     uint64      // base address of dyld when cache was built
    CodeSignatureOffset uint64      // file offset of code signature blob
    CodeSignatureSize   uint64      // size of code signature blob (zero means to end of file)
    SlideInfoOffset     uint64      // file offset of kernel slid info
    SlideInfoSize       uint64      // size of kernel slid info
    LocalSymbolsOffset  uint64      // file offset of where local symbols are stored
    LocalSymbolsSize    uint64      // size of local symbols information
    Uuid                [16]byte    // unique value for each shared cache file
}

type CacheHeader9 struct {
    CacheHeader
    CacheType           uint64      // 1 for development, 0 for optimized
}

type VMProtection int32

func (self VMProtection) Read() bool {
    return (self & 0x01) != 0
}

func (self VMProtection) Write() bool {
    return (self & 0x02) != 0
}

func (self VMProtection) Execute() bool {
    return (self & 0x04) != 0
}

type DyldCacheMappingInfo struct {
    Address     uint64
    Size        uint64
    FileOffset  uint64
    MaxProt     VMProtection
    InitProt    VMProtection
}

type CacheImageInfo struct {
    Address         uint64
    ModTime         uint64
    Inode           uint64
    PathFileOffset  uint32
    Pad             uint32
}

type DyldCacheSlideInfo struct
{
    Version            uint32       // currently 1
    TocOffset          uint32
    TocCount           uint32
    EntriesOffset      uint32
    EntriesCount       uint32
    EntriesSize        uint32       // currently 128
    // uint16_t toc[toc_count];
    // entrybitmap entries[entries_count];
}

type DyldCacheLocalSymbolsInfo struct
{
    NlistOffset         uint32      // offset into this chunk of nlist entries
    NlistCount          uint32      // count of nlist entries
    StringsOffset       uint32      // offset into this chunk of string pool
    StringsSize         uint32      // byte count of string pool
    EntriesOffset       uint32      // offset into this chunk of array of dyld_cache_local_symbols_entry
    EntriesCount        uint32      // number of elements in dyld_cache_local_symbols_entry array
}

type DyldCacheLocalSymbolsEntry struct
{
    DylibOffset         uint32      // offset in cache file of start of dylib
    NlistStartIndex     uint32      // start index of locals for this dylib
    NlistCount          uint32      // number of local symbols for this dylib
}

const (
    MACOSX_DYLD_SHARED_CACHE_DIR    = "/var/db/dyld/"
    IPHONE_DYLD_SHARED_CACHE_DIR    = "/System/Library/Caches/com.apple.dyld/"
    DYLD_SHARED_CACHE_BASE_NAME     = "dyld_shared_cache_"
)

