package downloader

import (
    . "ml/strings"

    "fmt"
    "regexp"

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
        links := data.Map("data").Str("f").Split(",")

        if len(links) == 1 {
            self.links = append(self.links, DownloadLink{
                url : links[0],
                name: String(fmt.Sprintf("%s.flv", self.title)),
            })
        } else {
            for index, url := range links {
                self.links = append(self.links, DownloadLink{
                    url : url,
                    name: String(fmt.Sprintf("%s.part%02d.flv", self.title, index + 1)),
                })
            }
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
