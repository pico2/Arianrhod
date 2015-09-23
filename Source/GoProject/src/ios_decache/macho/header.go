package macho

const (
    MH_MAGIC    = 0xFEEDFACE  /* the mach magic number */
    MH_CIGAM    = 0xCEFAEDFE  /* NXSwapInt(MH_MAGIC) */

    MH_MAGIC64    = 0xFEEDFACF  /* the mach magic number */
    MH_CIGAM64    = 0xCFFAEDFE  /* NXSwapInt(MH_MAGIC) */
)

type Header struct {
    Magic           uint32
    CpuType         CpuType
    CpuSubtype      CpuSubType
    FileType        FileType
    NumberOfCmds    uint32
    SizeofCmds      uint32
    Flags           uint32
}
