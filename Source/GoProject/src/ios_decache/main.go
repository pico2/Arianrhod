package main

import (
    . "fmt"
    . "ml/strings"

    "os"
    "path/filepath"
    "ml/os2"
    "ml/io2/filestream"
    "./cache"
    "./macho"
)

type DyldCacheExtractor struct {
    file        *filestream.File
    header      cache.CacheHeader
    mappings    []cache.SharedFileMappingNp
    images      []cache.CacheImageInfo
}

func NewDyldCacheExtractor(path string) *DyldCacheExtractor {
    file := filestream.Open(path)

    return &DyldCacheExtractor{
        file    : file,
        mappings: []cache.SharedFileMappingNp{},
        images  : []cache.CacheImageInfo{},
    }
}

func (self *DyldCacheExtractor) Close() {
    if self.file != nil {
        self.file.Close()
    }
}

func (self *DyldCacheExtractor) Open() {
    self.header = self.file.ReadType(cache.CacheHeader{}).(cache.CacheHeader)

    self.file.Seek(int64(self.header.MappingOffset), filestream.SEEK_SET)
    for i := uint32(0); i != self.header.MappingCount; i++ {
        self.mappings = append(self.mappings, self.file.ReadType(cache.SharedFileMappingNp{}).(cache.SharedFileMappingNp))
    }

    self.file.Seek(int64(self.header.ImagesOffset), filestream.SEEK_SET)
    for i := uint32(0); i != self.header.ImagesCount; i++ {
        self.images = append(self.images, self.file.ReadType(cache.CacheImageInfo{}).(cache.CacheImageInfo))
    }
}

func (self *DyldCacheExtractor) SaveAllImages(path string) {
    os.MkdirAll(path, 0755)
    for _, image := range self.images {
        self.SaveImage(image, filepath.Join(path, self.GetImagePath(image).String()))
    }
}

func (self *DyldCacheExtractor) SaveImage(image cache.CacheImageInfo, path string) {
    // os.MkdirAll(path, 0755)

    offset := self.OffsetFromVa(image.Address)
    self.file.SetPosition(int64(offset))

    mach := macho.NewMachOFile(self.file)

    Printf("%X\n", mach.Header.Magic)
}

func (self *DyldCacheExtractor) GetImagePath(image cache.CacheImageInfo) String {
    self.file.SetPosition(int64(image.PathOffset))
    return self.file.ReadMultiByte(CP_UTF8)
}

func (self *DyldCacheExtractor) OffsetFromVa(address uint64) uint64 {
    for _, mapping := range self.mappings {
        if mapping.Address <= address && address < mapping.Address + mapping.Size {
            return address - mapping.Address + mapping.Offset
        }
    }

    return ^uint64(0)
}

func main() {
    cache := NewDyldCacheExtractor(filepath.Join(os2.ExecutablePath(), "dyld_shared_cache_armv7s"))
    cache.Open()
    cache.SaveAllImages(filepath.Join(os2.ExecutablePath(), "dumps"))
}
