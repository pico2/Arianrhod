package ituneslib

import (
    . "ml/trace"
    "unsafe"
)

type SapSession struct {
    session         uintptr
    primeSignature  []byte
    deviceId        *FairPlayHWInfo
}

func NewSapSession() (session *SapSession) {
    var sapSession uintptr

    deviceId := NewRandomFairPlayHWInfo()

    st, _, _ := itunes.SapCreateSession.Call(uintptr(unsafe.Pointer(&sapSession)), uintptr(unsafe.Pointer(deviceId)))

    if int32(st) != 0 {
        Raise(newiTunesHelperErrorf("SapCreateSession failed: %X", uint32(st)))
    }

    session = &SapSession{
                    session         : sapSession,
                    primeSignature  : []byte{},
                    deviceId        : deviceId,
                }
    return
}

func (self *SapSession) Close() {
    if self.session == 0 {
        return
    }

    itunes.SapCloseSession.Call(self.session)
    self.session = 0
}

func (self *SapSession) CreatePrimeSignature() []byte {
    if len(self.primeSignature) == 0 {
        var buf *byte
        var size int
        var status int32

        st, _, _ := itunes.SapCreatePrimeSignature.Call(
                            self.session,
                            uintptr(unsafe.Pointer(&buf)),
                            uintptr(unsafe.Pointer(&size)),
                        )
        status = int32(st)
        if status != 0 {
            return self.primeSignature
        }

        defer itunes.iTunesFreeMemory.Call(uintptr(unsafe.Pointer(buf)))
        self.primeSignature = toBytes(buf, size)
    }

    return self.primeSignature
}

func (self *SapSession) ExchangeData(sapType SapCertType, data []byte) (cert []byte) {
    var buf *byte
    var size int
    var status int32

    st, _, _ := itunes.SapExchangeData.Call(
                        self.session,
                        uintptr(sapType),
                        uintptr(unsafe.Pointer(self.deviceId)),
                        uintptr(unsafe.Pointer(&data[0])),
                        uintptr(len(data)),
                        uintptr(unsafe.Pointer(&buf)),
                        uintptr(unsafe.Pointer(&size)),
                    )

    status = int32(st)
    if status != 0 {
        Raise(newiTunesHelperErrorf("SapExchangeData return %X", uint32(status)))
    }

    if buf == nil {
        return
    }

    defer itunes.iTunesFreeMemory.Call(uintptr(unsafe.Pointer(buf)))
    cert = toBytes(buf, size)

    return
}

func (self *SapSession) VerifyPrimeSignature(signature []byte) {
    var status int32

    st, _, _ := itunes.SapVerifyPrimeSignature.Call(
                        self.session,
                        uintptr(unsafe.Pointer(&signature[0])),
                        uintptr(len(signature)),
                    )

    status = int32(st)
    if status != 0 {
        Raise(newiTunesHelperErrorf("SapVerifyPrimeSignature return %X", uint32(status)))
    }
}

func (self *SapSession) SignData(data []byte) (signature []byte) {
    var buf *byte
    var size int
    var status int32

    st, _, _ := itunes.SapSignData.Call(
                        self.session,
                        uintptr(unsafe.Pointer(&data[0])),
                        uintptr(len(data)),
                        uintptr(unsafe.Pointer(&buf)),
                        uintptr(unsafe.Pointer(&size)),
                    )

    status = int32(st)
    if status != 0 {
        Raise(newiTunesHelperErrorf("SapSignData return %X", uint32(status)))
    }

    defer itunes.iTunesFreeMemory.Call(uintptr(unsafe.Pointer(buf)))
    signature = toBytes(buf, size)

    return
}
