package downloader

import (
    . "ml/strings"

    "fmt"
    "os"
    "time"
    "regexp"
    "path/filepath"

    "ml/net/http2"
    "ml/html"
    "ml/encoding/json"
)

var videoInfoPattern = regexp.MustCompile(`VideoInfo\s*:\s*{.*data\s*:\s*({.*})\s*}.*ObjectInfo\s*:\s*{`)
var locationHrefPattern = regexp.MustCompile(`location\.href\s*=\s*'(.*)';`)

type Ku6Downloader struct {
    *baseDownloader
}

func NewKu6(url String) Downloader {
    d := &Ku6Downloader{
        baseDownloader: newBase(url),
    }

    return d
}

func (self *Ku6Downloader) Analysis() AnalysisResult {
    result := self.session.Get(self.url).Map(func(value interface{}) (interface{}, error) {
        resp := value.(*http.Response)

        content := resp.Text()
        doc := html.Parse(content)

        if innerFrame := doc.Find("iframe[id=innerFrame]"); innerFrame.Length() != 0 {
            src := innerFrame.MustAttr("src")
            result := self.session.Get(src)
            if result.Ok() == false {
                return result.Unwrap()
            }

            resp = result.Result().(*http.Response)
            content = resp.Text()

            url := locationHrefPattern.FindStringSubmatch(content.String())[1]
            result = self.session.Get(url)
            if result.Ok() == false {
                return result.Unwrap()
            }

            resp = result.Result().(*http.Response)
            content = resp.Text()
            doc = html.Parse(content)
        }

        self.title = String(doc.Find("div.ckl_main").Find("h1").MustAttr("title"))

        videoInfoData := videoInfoPattern.FindStringSubmatch(content.String())[1]

        data := json.MustLoadDataDict([]byte(videoInfoData))
        self.links = data.Map("data").Str("f").Split(",")

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

func (self *Ku6Downloader) Download(path String) DownloadResult {
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

        // continue

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
