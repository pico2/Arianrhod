package main

import (
    . "fmt"
    . "ml/strings"
    . "ml/trace"

    "os"
    "reflect"
    "unsafe"

    "./cache"
)

type DyldCacheExtractor struct {
    file    *os.File
    header  *cache.CacheHeader
    mapping *cache.SharedFileMappingNp
    images  *cache.CacheImageInfo
}

func NewDyldCacheExtractor(path String) *DyldCacheExtractor {
    file, err := os.Open(path.String())
    RaiseIf(err)

    return &DyldCacheExtractor{
        file    : file,
    }
}

func (self *DyldCacheExtractor) Close() {
    if self.file != nil {
        self.file.Close()
    }
}

func (self *DyldCacheExtractor) Open() {
    self.header     = readStruct(cache.CacheHeader{}, self.file).(*cache.CacheHeader)
    self.mapping    = readStruct(cache.SharedFileMappingNp{}, self.file).(*cache.SharedFileMappingNp)
    self.images     = readStruct(cache.CacheImageInfo{}, self.file).(*cache.CacheImageInfo)

    Println(string(self.header.Magic[:]))
}

func readStruct(t interface{}, file *os.File) interface{} {
    typ := reflect.TypeOf(t)
    bytes := make([]byte, typ.Size())
    file.Read(bytes)

    return reflect.NewAt(typ, unsafe.Pointer(&bytes[0])).Interface()
}

func main() {
    cache := NewDyldCacheExtractor("dyld_shared_cache_armv7")
    cache.Open()
}

