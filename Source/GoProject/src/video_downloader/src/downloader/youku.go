package downloader

import (
    . "ml/strings"
    . "ml/dict"

    "fmt"
    "os"
    "time"
    "regexp"
    "path/filepath"

    "spew"

    "ml/net/http2"
    "ml/html"
    "ml/random"
    "ml/encoding/json"
)

var youkuVideoIdPattern = regexp.MustCompile(`(?U)currentEncodeVid\s*:\s*"(.*)"`)


type YoukuVideoInfoSeg struct {
    totalMillisecondsAudio      int64
    totalMillisecondsVideo      int64
    size                        int64
    fileid                      String
    key                         String
}

type YoukuVideoInfo struct {
    segs    []YoukuVideoInfoSeg

    security struct {
        encryptString  String
        ip              int64
    }
}

type YoukuDownloader struct {
    *baseDownloader

    vid     String
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
        // doc := html.Parse(content)

        // self.title = String(doc.Find("div[id=sMain]").Find("h1.title").MustAttr("title"))

        vid := String(youkuVideoIdPattern.FindStringSubmatch(content.String())[1])

        self.getVideoInfo(vid)

        fmt.Println(self.title)

        // videoInfoData := videoInfoPattern.FindStringSubmatch(content.String())[1]

        // data := json.MustLoadDataDict([]byte(videoInfoData))
        // self.links = data.Map("data").Str("f").Split(",")

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

func (self *YoukuDownloader) getVideoInfo(vid String) (videoInfo YoukuVideoInfo) {
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

    videoInfo.security.encryptString = security.Str("encrypt_string")
    videoInfo.security.ip = int64(security.Int("ip"))

    stream := data.Array("stream")

    for index := range stream {
        s := stream.Map(index)
        segs := s.Array("segs")

        fmt.Println("stream_type", s.Str("stream_type"))

        for index := range segs {
            seg := segs.Map(index)

            videoInfo.segs = append(videoInfo.segs, YoukuVideoInfoSeg{
                totalMillisecondsAudio  : seg.Str("total_milliseconds_audio").ToInt64(),
                totalMillisecondsVideo  : seg.Str("total_milliseconds_video").ToInt64(),
                size                    : seg.Str("size").ToInt64(),
                fileid                  : seg.Str("fileid"),
                key                     : seg.Str("key"),
            })
        }
    }

    fmt.Printf("%+v\n", spew.Sdump(videoInfo))

    return
}
