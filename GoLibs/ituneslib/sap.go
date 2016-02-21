package ituneslib

import (
    . "ml/trace"
    . "ml/dict"
    "unsafe"
    "plistlib"
    "ml/net/http"
)

const (
    DefaultOSXUserAgent = "iTunes/12.3.2 (Macintosh; OS X 10.10.5) AppleWebKit/600.8.9"
    DefaultWindowsUserAgent = "iTunes/12.3 (Windows; Microsoft Windows 8.1 x64 Business Edition (Build 9200); x64) AppleWebKit/7601.1056.1.1"
)

type SapSession struct {
    session         uintptr
    primeSignature  []byte
    deviceId        *FairPlayHWInfo
    HttpSession     *http.Session
    UrlBag          Dict
}

var sapSessionPool = make(chan *SapSession, 1000)

func sapInitialize() {
    for i := cap(sapSessionPool); i != 0; i-- {
        sapSessionPool <- createSapSession()
    }
}

func NewSapSession() (session *SapSession) {
    return <-sapSessionPool
}

func createSapSession() (session *SapSession) {
    var sapSession uintptr

    deviceId := NewRandomFairPlayHWInfo()

    st, _, _ := itunes.SapCreateSession.Call(uintptr(unsafe.Pointer(&sapSession)), uintptr(unsafe.Pointer(deviceId)))

    if int32(st) != 0 {
        Raise(newiTunesHelperErrorf("SapCreateSession failed: %X", uint32(st)))
    }

    h := http.NewSession()

    session = &SapSession{
                    session         : sapSession,
                    primeSignature  : []byte{},
                    deviceId        : deviceId,
                    HttpSession     : h,
                    UrlBag          : Dict{},
                }
    return
}

func (self *SapSession) Close() {
    if self.session == 0 {
        return
    }

    self.HttpSession.Close()
    itunes.SapCloseSession.Call(self.session)
    self.session = 0

    sapSessionPool <- createSapSession()
}

func (self *SapSession) Initialize(userAgent string, country CountryID, sapType SapCertType) {
    self.HttpSession.SetHeaders(Dict{
        "User-Agent"            : userAgent,
        "Accept-Encoding"       : "gzip",
        "Accept-Language"       : "zh-cn, zh;q=0.75, en-us;q=0.50, en;q=0.25",
        "X-Apple-Store-Front"   : country.StoreFront(),
        "X-Apple-Tz"            : "28800",
    })

    // self.HttpSession.SetProxy("localhost", 6789)

    self.HttpSession.DefaultOptions.AutoRetry = true

    self.initUrlbag()
    self.initSap(sapType)
}

func (self *SapSession) initUrlbag() {
    var resp *http.Response

    resp = self.HttpSession.Get("https://init.itunes.apple.com/bag.xml?ix=5&ign-bsn=1")

    plist := Dict{}
    resp.Plist(&plist)
    plistlib.Unmarshal(plist["bag"].([]byte), &self.UrlBag)
}

func (self *SapSession) initSap(sapType SapCertType) {
    signSapSetupCert := Dict{}
    self.HttpSession.Get(self.UrlBag["sign-sap-setup-cert"]).Plist(&signSapSetupCert)

    cert := self.ExchangeData(sapType, signSapSetupCert["sign-sap-setup-cert"].([]byte))

    body, err := plistlib.MarshalIndent(Dict{"sign-sap-setup-buffer": cert}, plistlib.XMLFormat, "    ")
    RaiseIf(err)

    signSapSetupBuffer := Dict{}
    self.HttpSession.Post(
        self.UrlBag["sign-sap-setup"],
        Dict{
            "headers": Dict{
                "Content-Type": "application/x-apple-plist",
            },

            "body": body,
        },
    ).Plist(&signSapSetupBuffer)

    self.ExchangeData(sapType, signSapSetupBuffer["sign-sap-setup-buffer"].([]byte))
}

func (self *SapSession) CreatePrimeSignature() []byte {
    if len(self.primeSignature) == 0 {
        var buf *byte
        var size int

        st, _, _ := itunes.SapCreatePrimeSignature.Call(
                            self.session,
                            uintptr(unsafe.Pointer(&buf)),
                            uintptr(unsafe.Pointer(&size)),
                        )
        status := getStatus(st)
        if status != 0 {
            return self.primeSignature
        }

        defer FreeSessionData(buf)
        self.primeSignature = toBytes(buf, size)
    }

    return self.primeSignature
}

func (self *SapSession) ExchangeData(sapType SapCertType, data []byte) (cert []byte) {
    var buf *byte
    var size int

    st, _, _ := itunes.SapExchangeData.Call(
                        self.session,
                        uintptr(sapType),
                        uintptr(unsafe.Pointer(self.deviceId)),
                        uintptr(unsafe.Pointer(&data[0])),
                        uintptr(len(data)),
                        uintptr(unsafe.Pointer(&buf)),
                        uintptr(unsafe.Pointer(&size)),
                    )

    status := getStatus(st)
    if status != 0 {
        Raise(newiTunesHelperErrorf("SapExchangeData return %X", uint32(status)))
    }

    if buf == nil {
        return
    }

    defer FreeSessionData(buf)
    cert = toBytes(buf, size)

    return
}

func (self *SapSession) VerifyPrimeSignature(signature []byte) {
    st, _, _ := itunes.SapVerifyPrimeSignature.Call(
                        self.session,
                        uintptr(unsafe.Pointer(&signature[0])),
                        uintptr(len(signature)),
                    )

    status := getStatus(st)
    if status != 0 {
        Raise(newiTunesHelperErrorf("SapVerifyPrimeSignature return %X", uint32(status)))
    }
}

func (self *SapSession) SignData(data []byte) (signature []byte) {
    var buf *byte
    var size int

    st, _, _ := itunes.SapSignData.Call(
                        self.session,
                        uintptr(unsafe.Pointer(&data[0])),
                        uintptr(len(data)),
                        uintptr(unsafe.Pointer(&buf)),
                        uintptr(unsafe.Pointer(&size)),
                    )

    status := getStatus(st)
    if status != 0 {
        Raise(newiTunesHelperErrorf("SapSignData return %X", uint32(status)))
    }

    defer FreeSessionData(buf)
    signature = toBytes(buf, size)

    return
}
