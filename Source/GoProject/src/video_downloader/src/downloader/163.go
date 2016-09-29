package downloader

import (
    . "ml/strings"
    . "ml/dict"

    "os"
    "fmt"
    "regexp"
    "crypto/aes"
    "encoding/hex"
    xmllib "encoding/xml"

    "spew"

    "ml/net/http2"
    "ml/crypto/cipher"
    "ml/encoding/xml"
)

type NetEaseDownloader struct {
    *baseDownloader
    subtitle String
}

func NewNetEase(url String) Downloader {
    d := &NetEaseDownloader{
        baseDownloader: newBase(url),
    }

    return d
}

func (self *NetEaseDownloader) Analysis() AnalysisResult {
    result := self.session.Get(self.url).Map(func(value interface{}) (interface{}, error) {
        resp := value.(*http.Response)

        content := resp.Text()

        pattern := regexp.MustCompile(`(?sU)getCurrentMovie.*\s+src\s*:\s*'(.*)',`)
        swfUrl := String(pattern.FindStringSubmatch(content.String())[1])

        pattern = regexp.MustCompile(`(?sU)getCurrentMovie.*\s+title\s*:\s*'(.*)',`)
        self.title = String(pattern.FindStringSubmatch(content.String())[1])

        info := swfUrl.Split("-")
        vid := info[2]
        xmlurl := fmt.Sprintf("http://live.ws.126.net/movie/%s/%s/%s.xml", vid.SubString(len(vid) - 2, len(vid) - 1), vid.SubString(len(vid) - 1, len(vid)), vid)

        self.session.Get(
            xmlurl,
            http.Headers(Dict{
                "X-Requested-With" : "ShockwaveFlash/23.0.0.166",
            }),
        ).Map(func(value interface{}) (interface{}, error) {
            resp := value.(*http.Response)

            type FlvURL struct {
                HD struct {
                    Default     bool            `xml:"default,attr"`
                    FLV         []String        `xml:"flv"`
                } `xml:"hd"`
            }

            type PlayURL struct {
                SD struct {
                    Default     bool            `xml:"default,attr"`
                    MP4         []String        `xml:"mp4"`
                } `xml:"SD"`
            }

            type SubtitleURL struct {
                Name            String        `xml:"name"`
                Url             String        `xml:"url"`
            }

            type VideoInfo struct {
                XMLName         xmllib.Name     `xml:"all"`
                Title           String          `xml:"title"`
                PNumber         int             `xml:"pnumber"`
                Encrypt         int             `xml:"encrypt"`

                FlvUrl          FlvURL          `xml:"flvUrl"`
                FlvUrlOrigin    FlvURL          `xml:"flvUrlOrigin"`
                PlayUrl         PlayURL         `xml:"playurl"`
                PlayUrlOrigin   PlayURL         `xml:"playurl_origin"`
                Subtitles       []SubtitleURL   `xml:"subs>sub"`
            }

            var info VideoInfo

            content := resp.Content
            e := xml.Unmarshal([]byte(content), &info)

            links := []String{}

            for index, url := range info.FlvUrlOrigin.HD.FLV {
                encrypted, _ := hex.DecodeString(url.String())
                info.FlvUrlOrigin.HD.FLV[index] = self.decryptoVideoUrl(encrypted, info.Encrypt)
                links = append(links, info.FlvUrlOrigin.HD.FLV[index])
            }

            for index, url := range info.PlayUrlOrigin.SD.MP4 {
                encrypted, _ := hex.DecodeString(url.String())
                info.PlayUrlOrigin.SD.MP4[index] = self.decryptoVideoUrl(encrypted, info.Encrypt)
                links = append(links, info.PlayUrlOrigin.SD.MP4[index])
            }

            for index, url := range info.FlvUrl.HD.FLV {
                encrypted, _ := hex.DecodeString(url.String())
                info.FlvUrl.HD.FLV[index] = self.decryptoVideoUrl(encrypted, info.Encrypt)
                links = append(links, info.FlvUrl.HD.FLV[index])
            }

            for index, url := range info.PlayUrl.SD.MP4 {
                encrypted, _ := hex.DecodeString(url.String())
                info.PlayUrl.SD.MP4[index] = self.decryptoVideoUrl(encrypted, info.Encrypt)
                links = append(links, info.PlayUrl.SD.MP4[index])
            }

            for _, sub := range info.Subtitles {
                if sub.Name == "中文" {
                    self.subtitle = sub.Url
                }
            }

            self.title = info.Title + " " + self.title
            self.links = append(self.links, DownloadLink{
                url     : links[0],
                name    : self.title + ".flv",
            })

            return nil, nil

        }).MapErr(func(err error) error {
            fmt.Println(err)
            return err
        })

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

func (self *NetEaseDownloader) Download(path String) DownloadResult {
    if self.subtitle.IsEmpty() == false {

        fmt.Println("download subtitle")

        self.session.Get(
            self.subtitle,
            http.Headers(Dict{
                "X-Requested-With" : "ShockwaveFlash/23.0.0.166",
            }),
        ).Map(func(value interface{}) (interface{}, error) {
            resp := value.(*http.Response)

            p := self.makeFullPath(self.title.String() + ".srt", path.String(), self.title.String())
            fmt.Println(p)
            fd, err := os.Create(p.String())
            if err != nil {
                fmt.Println(err)
                return nil, nil
            }

            fd.Write(resp.Content)
            fd.Close()

            return nil, nil

        }).MapErr(func (err error) error {
            fmt.Printf("download subtitle failed: %v", err)
            return err
        })
    }

    return self.baseDownloader.Download(path)
}

func (self *NetEaseDownloader) decryptoVideoUrl(encrypted []byte, version int) String {
    key := []string{
        "4fxGZqoGmesXqg2o",     // 1
        "3fxVNqoPmesAqg2o",     // 2
    }[version - 1]

    c, _ := aes.NewCipher([]byte(key))
    dec := cipher.NewECBDecrypter(c)

    data := make([]byte, len(encrypted))
    copy(data, encrypted)

    dec.CryptBlocks(data, data)

    return String(data[:len(data) - int(data[len(data) - 1])])
}
