package ituneslib

import (
    . "ml/trace"
    "unsafe"
    "ml/os2"
    "path/filepath"
)

type KeybagSyncType int

const (
    Keybag_Buy          = KeybagSyncType(1)
    Keybag_Refetch      = KeybagSyncType(1)
    Keybag_Default      = KeybagSyncType(2)
    Keybag_Upgrade      = KeybagSyncType(5)
    Keybag_Authorize    = KeybagSyncType(8)
    Keybag_Update       = KeybagSyncType(11)
    Keybag_LoginiOS     = KeybagSyncType(0x135)
)

type KeybagSession struct {
    session uintptr
}

func NewKeybagSession(uniqueDeviceID []byte) *KeybagSession {
    var kbsyncSession uintptr

    // scinfo := String(`C:\ProgramData\Apple Computer\iTunes\SC Info`).Encode(CP_UTF8)
    // scinfo := []byte(`C:\ProgramData\Apple Computer\iTunes\SC Info`)

    scinfo := []byte(filepath.Join(os2.ExecutablePath(), "SC Info"))

    var udid *FairPlayHWInfo = nil

    if uniqueDeviceID != nil {
        udid = &FairPlayHWInfo{
            Length: int32(len(uniqueDeviceID)),
        }

        copy(udid.Id[:], uniqueDeviceID)
        udid.Length = 6
    }

    st, _, _ := itunes.KbsyncCreateSession.Call(
                    uintptr(unsafe.Pointer(&kbsyncSession)),
                    uintptr(unsafe.Pointer(udid)),
                    0,
                    uintptr(unsafe.Pointer(&scinfo[0])),
                )

    if int32(st) != 0 {
        Raise(newiTunesHelperErrorf("NewKeybagSession failed: %X", uint32(st)))
    }

    session := &KeybagSession{
        session : kbsyncSession,
    }

    return session
}

func (self *KeybagSession) Close() {
    if self.session == 0 {
        return
    }

    itunes.KbsyncCloseSession.Call(self.session)
    self.session = 0
}

func (self *KeybagSession) GetData(dsid int64, syncType KeybagSyncType) []byte {
    var buf *byte
    var size int

    var status uint32

    switch unsafe.Sizeof(uintptr(0)) {
        case 4:
            st, _, _ := itunes.KbsyncGetData.Call(
                            self.session,
                            uintptr(dsid & 0xFFFFFFFF),
                            uintptr((dsid >> 32) & 0xFFFFFFFF),
                            0,
                            uintptr(syncType),
                            uintptr(unsafe.Pointer(&buf)),
                            uintptr(unsafe.Pointer(&size)),
                        )
            status = uint32(st)

        case 8:
            st, _, _ := itunes.KbsyncGetData.Call(
                            self.session,
                            uintptr(dsid),
                            0,
                            uintptr(syncType),
                            uintptr(unsafe.Pointer(&buf)),
                            uintptr(unsafe.Pointer(&size)),
                        )
            status = uint32(st)
    }

    if status != 0 {
        Raise(newiTunesHelperErrorf("Keybag.GetData failed: %X", status))
    }

    defer FreeSessionData(buf)

    return toBytes(buf, size)
}
