package downloader

import (
    . "ml/strings"
    . "ml/dict"

    "fmt"
    "os"
    "time"
    "regexp"
    "path/filepath"
    "crypto/des"
    "crypto/md5"

    "spew"

    "ml/net/http2"
    "ml/random"
    "ml/encoding/base64"
    "ml/logging/logger"
)

var youkuVideoIdPattern = regexp.MustCompile(`(?U)currentEncodeVid\s*:\s*"(.*)"`)

type YoukuVideoInfoSeg struct {
    totalMillisecondsAudio      int64
    totalMillisecondsVideo      int64
    size                        int64
    fileid                      String
    key                         String
    hd                          int
    container                   String
}

type YoukuVideoInfo struct {
    segs    []YoukuVideoInfoSeg

    security struct {
        sid             String
        token           String
        encryptString   String
        ip              int64
    }
}

type YoukuDownloader struct {
    *baseDownloader
    vid         String
    videoInfo   YoukuVideoInfo
}

func NewYouku(url String) Downloader {
    d := &YoukuDownloader{
        baseDownloader: newBase(url),
    }

    return d
}

func (self *YoukuDownloader) Analysis() AnalysisResult {
    result := self.session.Get(self.url).Map(func(value interface{}) (interface{}, error) {
        resp := value.(*http.Response)

        content := resp.Text()
        vid := String(youkuVideoIdPattern.FindStringSubmatch(content.String())[1])

        self.getVideoInfo(vid)

        for index, seg := range self.videoInfo.segs {
            // com\youku\utils\GetUrl.as

            url := fmt.Sprintf("http://k.youku.com/player/getFlvPath/sid/%s_00/st/flv/fileid/%s", self.videoInfo.security.sid, seg.fileid)
            result := self.session.Get(
                            url,
                            http.Params(Dict{
                                "start"     : "0",
                                "K"         : seg.key,
                                "hd"        : seg.hd,
                                "myp"       : "0",
                                "ts"        : "64",
                                "ypp"       : "0",      // P2PConfig.ypp @ com\youku\P2PConfig.as
                                "ctype"     : "10",     // PlayerConstant.CTYPE @ com\youku\data\PlayerConstant.as
                                "ev"        : "1",      // PlayerConstant.EV @ com\youku\data\PlayerConstant.as
                                "token"     : self.videoInfo.security.token,
                                "oip"       : self.videoInfo.security.ip,
                                "ep"        : self.encryptEp(self.videoInfo, seg.fileid),
                                "yxon"      : "1",
                                "special"   : "true",
                            }),
                        )

            if err := result.Err(); err != nil {
                logger.Critical("get seg %d failed: %v", index, err)
                panic(nil)
            }

            var r JsonArray

            result.Result().(*http.Response).Json(&r)
            self.links = append(self.links, r.Map(0).Str("server"))
        }

        return nil, nil

    }).MapErr(func(err error) error {
        fmt.Println(err)
        return err

    })

    if result.Ok() {
        return AnalysisSuccess
    }

    return AnalysisNotSupported
}

func (self *YoukuDownloader) Download(path String) DownloadResult {
    path = String(filepath.Join(path.String(), self.title.String()))

    os.MkdirAll(path.String(), os.ModeDir)

    fmt.Printf("%s\n\n", self.title)

    var files []string

    for index, link := range self.links {
        var f string

        if len(self.links) == 1 {
            f = filepath.Join(path.String(), fmt.Sprintf("%s.flv", self.title))
            fmt.Println("downloading")
        } else {
            f = filepath.Join(path.String(), fmt.Sprintf("%s.part%02d.flv", self.title, index + 1))
            files = append(files, f)

            fmt.Printf("downloading part %d / %d\n", index + 1, len(self.links))
        }

        fmt.Println(link)

        self.session.Get(
            link,
            http.ReadBlock(true),
            http.Timeout(time.Second * 10),
            http.MaxTimeoutTimes(100),
            http.Ignore404(false),
        ).Map(func(value interface{}) (interface{}, error) {
            fd, err := os.Create(f)
            if err != nil {
                fmt.Println(err)
                return nil, err
            }

            content := value.(*http.Response).Content

            fmt.Println("length", len(content))

            fd.Write(content)
            fd.Close()

            return nil, nil

        }).MapErr(func(err error) error {
            fmt.Println(err)
            return err
        })

        fmt.Println()
    }

    if len(files) != 0 {
        self.merge(filepath.Join(path.String(), self.title.String() + ".mkv"), files)
    }

    return DownloadSuccess
}

//
// http://k.youku.com/player/getFlvPath/sid/1474526152477 10f8 1137_00/st/mp4/fileid/030008010057E0B89D83C2019C3C1CAEE308CE-FEF5-6CE1-579C-51C872568410
// start=0
// K=dbcbe7f68e9006d7282bbfbe
// hd=1
// myp=0
// ts=68
// ymovie=1
// ypp=0
// ctype=10
// ev=1
// token=0939
// oip=244858955
// ep=p6F36Pjts%2BtCLWpTKCmthZj6RxeWJBP6lq77e%2FGGIqfo1mmyw7J4c2kYmVCZ5DuJFtEHjVM2G9unL9LD4GYQw0Hi%2BuI2jYE4rOI3l9%2BAxO8c8VxcnEnSiNdLuaWLAtdsasw%2FFBjp2uM%3D
// p6F36Pjts+tCLWpTKCmthZj6RxeWJBP6lq77e/GGIqfo1mmyw7J4c2kYmVCZ5DuJFtEHjVM2G9unL9LD4GYQw0Hi+uI2jYE4rOI3l9+AxO8c8VxcnEnSiNdLuaWLAtdsasw/FBjp2uM=
// yxon=1
// special=true
//

func (self *YoukuDownloader) getVideoInfo(vid String) {
    var info JsonDict

    result := self.session.Get(
                    "http://play.youku.com/play/get.json",
                    http.Params(Dict{
                        "vid"   : vid,
                        "ct"    : 10,
                        "ran"   : random.IntRange(1000, 10000),
                    }),
                )

    if result.Ok() == false {
        return
    }

    if result.Result().(*http.Response).Json(&info).Ok() == false {
        return
    }

    data := info.Map("data")

    self.title = data.Map("video").Str("title")

    security := data.Map("security")

    self.videoInfo.security.encryptString = security.Str("encrypt_string")
    self.videoInfo.security.ip = int64(security.Int("ip"))

    stream := data.Array("stream")

    type StreamType struct {
        name        String
        profile     String
        container   String
        priority    int
        hd          int
    }

    getStreamType := func (stream JsonDict) StreamType {
        var st StreamType

        switch t := stream.Str("stream_type"); t {
            case "mp4hd3", "hd3":
                st.priority = 6
                st.profile = "1080P"
                st.container = "flv"
                st.hd = 3

            case "mp4hd2", "hd2":
                st.priority = 5
                st.profile = "超清"
                st.container = "flv"
                st.hd = 2

            case "mp4hd", "mp4":
                st.priority = 4
                st.profile = "高清"
                st.container = "mp4"
                st.hd = 1

            case "flvhd", "flv":
                st.priority = 2
                st.profile = "标清"
                st.container = "flv"
                st.hd = 0

            case "3gphd":
                st.priority = 1
                st.profile = "标清（3GP）"
                st.container = "3gp"
                st.hd = 0

            default:
                logger.Critical("unsupported stream type: %v", t)
                panic(nil)
        }

        return st
    }

    var streamType StreamType

    for index := range stream {
        s := stream.Map(index)

        st := getStreamType(s)
        if st.priority < streamType.priority {
            continue
        }

        streamType = st

        segs := s.Array("segs")

        fmt.Printf("stream_type: %+v\n", streamType)

        self.videoInfo.segs = nil

        for index := range segs {
            seg := segs.Map(index)

            self.videoInfo.segs = append(self.videoInfo.segs, YoukuVideoInfoSeg{
                totalMillisecondsAudio  : seg.Str("total_milliseconds_audio").ToInt64(),
                totalMillisecondsVideo  : seg.Str("total_milliseconds_video").ToInt64(),
                size                    : seg.Str("size").ToInt64(),
                fileid                  : seg.Str("fileid"),
                key                     : seg.Str("key"),
                hd                      : streamType.hd,
                container               : streamType.container,
            })
        }
    }

    self.videoInfo.security.sid, self.videoInfo.security.token = self.decryptSidAndToken(self.videoInfo.security.encryptString)

    fmt.Printf("%+v\n", spew.Sdump(self.videoInfo))

    return
}

func (self *YoukuDownloader) decryptSidAndToken(encryptString String) (sid, token String) {
    fmt.Println(encryptString)

    data := base64.DecodeString(encryptString.String())

    cipher, _ := des.NewCipher([]byte("00149ad5"))
    for i := 0; i < len(data); i += cipher.BlockSize() {
        cipher.Decrypt(data[i:], data[i:])
    }

    decrypted := String(data).Split("\x00", 1)[0].Split("_", 1)

    sid = decrypted[0]
    token = decrypted[1]
    return
}

func (self *YoukuDownloader) encryptEp(info YoukuVideoInfo, fileId String) String {
    bctime := 0
    ep := fmt.Sprintf("%v_%v_%v_%v", info.security.sid, fileId, info.security.token, bctime)
    sum := md5.Sum([]byte(ep + "_kservice"))

    ep = ep + "_" + fmt.Sprintf("%x", sum[:])[:4]

    data := []byte(ep)

    cipher, _ := des.NewCipher([]byte("21dd8110"))

    for len(data) % cipher.BlockSize() != 0 {
        data = append(data, 0)
    }

    for i := 0; i < len(data); i += cipher.BlockSize() {
        cipher.Encrypt(data[i:], data[i:])
    }

    return base64.EncodeToString(data)
}
