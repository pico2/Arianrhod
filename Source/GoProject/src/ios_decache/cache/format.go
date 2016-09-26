package cache

import (
    "fmt"
)

func (self CacheHeader) String() string {
    return fmt.Sprintf(
        "Magic               = %s\n" +
        "MappingOffset       = %08X\n" +
        "MappingCount        = %d\n" +
        "ImagesOffset        = %08X\n" +
        "ImagesCount         = %d\n" +
        "DyldBaseAddress     = %08X\n" +
        "CodeSignatureOffset = %08X\n" +
        "CodeSignatureSize   = %08X\n" +
        "SlideInfoOffset     = %08X\n" +
        "SlideInfoSize       = %08X\n" +
        "LocalSymbolsOffset  = %08X\n" +
        "LocalSymbolsSize    = %08X\n" +
        "Uuid                = %08X\n",
        self.Magic,
        self.MappingOffset,
        self.MappingCount,
        self.ImagesOffset,
        self.ImagesCount,
        self.DyldBaseAddress,
        self.CodeSignatureOffset,
        self.CodeSignatureSize,
        self.SlideInfoOffset,
        self.SlideInfoSize,
        self.LocalSymbolsOffset,
        self.LocalSymbolsSize,
        self.Uuid,
    )
}

func (self DyldCacheMappingInfo) String() string {
    return fmt.Sprintf(
        "Address    = %016X\n" +
        "Size       = %X\n" +
        "FileOffset = %X\n" +
        "MaxProt    = %08X\n" +
        "InitProt   = %08X\n",
        self.Address,
        self.Size,
        self.FileOffset,
        self.MaxProt,
        self.InitProt,
    )
}

func (self CacheImageInfo) String() string {
    return fmt.Sprintf(
        "Address        = %016X\n" +
        "ModTime        = %016X\n" +
        "Inode          = %d\n" +
        "PathFileOffset = %08X\n",
        self.Address,
        self.ModTime,
        self.Inode,
        self.PathFileOffset,
    )
}