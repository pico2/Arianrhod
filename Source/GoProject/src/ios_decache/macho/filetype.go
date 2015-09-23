package macho

const (
    MH_OBJECT       = 0x1       /* relocatable object file */
    MH_EXECUTE      = 0x2       /* demand paged executable file */
    MH_FVMLIB       = 0x3       /* fixed VM shared library file */
    MH_CORE         = 0x4       /* core file */
    MH_PRELOAD      = 0x5       /* preloaded executable file */
    MH_DYLIB        = 0x6       /* dynamically bound shared library */
    MH_DYLINKER     = 0x7       /* dynamic link editor */
    MH_BUNDLE       = 0x8       /* dynamically bound bundle file */
    MH_DYLIB_STUB   = 0x9       /* shared library stub for static */
                                /* linking only, no section contents */
    MH_DSYM         = 0xA       /* companion file with only debug sections */
    MH_KEXT_BUNDLE  = 0xB       /* x86_64 kexts */
)

type FileType uint32

func (self FileType) String() string {
    return types[self]
}

var types = map[FileType]string{
    MH_OBJECT       : "MH_OBJECT",
    MH_EXECUTE      : "MH_EXECUTE",
    MH_FVMLIB       : "MH_FVMLIB",
    MH_CORE         : "MH_CORE",
    MH_PRELOAD      : "MH_PRELOAD",
    MH_DYLIB        : "MH_DYLIB",
    MH_DYLINKER     : "MH_DYLINKER",
    MH_BUNDLE       : "MH_BUNDLE",
    MH_DYLIB_STUB   : "MH_DYLIB_STUB",
    MH_DSYM         : "MH_DSYM",
    MH_KEXT_BUNDLE  : "MH_KEXT_BUNDLE",
}
