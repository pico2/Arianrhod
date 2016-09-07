package macho

import (
    . "fmt"
    "ml/io2/filestream"
    "reflect"
    "unsafe"
)

type MachOFile struct {
    Header      Header
    Commands    []LoadCommand
}

func NewMachOFile(file *filestream.File) *MachOFile {
    hdr := file.ReadType(Header{}).(Header)
    macho := &MachOFile{
        Header      : hdr,
        Commands    : []LoadCommand{},
    }

    cmds := file.Read(int(hdr.SizeofCmds))
    // Println(cmds)

    for i := uint32(0); i != hdr.NumberOfCmds; i++ {
        cmd, size := newLoadCommand(cmds)
        macho.Commands = append(macho.Commands, cmd)
        cmds = cmds[size:]
    }

    return macho
}

func newLoadCommand(buffer []byte) (LoadCommand, int) {
    basecmd := newTypeFromBytes(BaseLoadCommand{}, buffer).(*BaseLoadCommand)
    size := int(basecmd.Size())

    switch basecmd.Cmd() {
        case LC_SEGMENT:
            return newTypeFromBytes(SegmentCommand{}, buffer).(*SegmentCommand), size

        default:
            return basecmd, size
    }
}

func newTypeFromBytes(t interface{}, buffer []byte) interface{} {
    typ := reflect.TypeOf(t)
    // Println(buffer[:typ.Size()])
    return reflect.NewAt(typ, unsafe.Pointer(&buffer[0])).Interface()
}
