package downloader

import (
    . "ml/strings"
    . "ml/dict"

    "os"
    "time"
    "fmt"
    "os/exec"
    "path/filepath"

    "ml/trace"
    "ml/os2"
    "ml/net/http2"
)

var mkvmerge = filepath.Join(os2.ExecutablePath(), "mkvmerge.exe")

type DownloadLink struct {
    url     String
    name    String
}

type baseDownloader struct {
    url     String
    title   String
    links   []DownloadLink
    session *http.Session
}

func newBase(url String) *baseDownloader {
    s := http.NewSession(
        http.DefaultHeaders(Dict{
            "User-Agent"        : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36",
            "Accept"            : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding"   : "gzip, deflate, sdch",
            "Accept-Language"   : "en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2",
        }),
        http.DefaultTimeout(10 * time.Second),
        http.DefaultOption(
            http.ReadBlock(true),
        ),
    )

    s.SetHTTPProxy("localhost", 6789)

    return &baseDownloader{
        url     : url,
        session : s,
    }
}

func (self *baseDownloader) Close() {
    self.session.Close()
}

func (self *baseDownloader) Analysis() AnalysisResult {
    trace.Raise(trace.NewNotImplementedError("Analysis not implemented"))
    return AnalysisFailed
}

func (self *baseDownloader) makeFullPath(name string, path ...string) String {
    p := filepath.Join(path...)
    os.MkdirAll(p, os.ModeDir)
    return String(filepath.Join(p, name))
}

func (self *baseDownloader) Download(path String) DownloadResult {
    path = String(filepath.Join(path.String(), self.title.String()))
    os.MkdirAll(path.String(), os.ModeDir)

    fmt.Printf("%s\n\n", self.title)

    var files []string

    for index, link := range self.links {
        f := filepath.Join(path.String(), link.name.String())

        if len(self.links) == 1 {
            fmt.Println("downloading")
        } else {
            files = append(files, f)
            fmt.Printf("downloading part %d / %d\n", index + 1, len(self.links))
        }

        fmt.Println(link.url)

        self.session.Get(
            link.url,
            http.ReadBlock(true),
            http.Timeout(time.Second * 10),
            http.MaxTimeoutTimes(100),
            http.Ignore404(false),
            http.Headers(Dict{
                "X-Requested-With" : "ShockwaveFlash/23.0.0.166",
            }),
        ).Map(func(value interface{}) (interface{}, error) {
            os.MkdirAll(path.String(), os.ModeDir)

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
// mkvmerge.exe
// --output 东方卫视笑傲江湖总决赛崔大笨二人转.mkv
// ( D:\Dev\Source\GoProject\src\video_downloader\src\downloaded\东方卫视笑傲江湖总决赛崔大笨二人转_part01.flv ) + ( D:\Dev\Source\GoProject\src\video_downloader\src\downloaded\东方卫视笑傲江湖总决赛崔大笨二人转_part02.flv ) + ( D:\Dev\Source\GoProject\src\video_downloader\src\downloaded\东方卫视笑傲江湖总决赛崔大笨二人转_part03.flv ) + ( D:\Dev\Source\GoProject\src\video_downloader\src\downloaded\东方卫视笑傲江湖总决赛崔大笨二人转_part04.flv )
// --track-order 0:0,0:1
// --append-to 1:0:0:0,2:0:1:0,3:0:2:0,1:1:0:1,2:1:1:1,3:1:2:1
//

//
// D:/Software/mkvtoolnix\mkvmerge.exe
// --output D:\Dev\Source\GoProject\src\video_downloader\src\downloaded\看一颗松子如何引发星际碰撞\part1.mkv
// ( D:\Dev\Source\GoProject\src\video_downloader\src\downloaded\看一颗松子如何引发星际碰撞\part1.flv ) + ( D:\Dev\Source\GoProject\src\video_downloader\src\downloaded\看一颗松子如何引发星际碰撞\part2.flv )
// --track-order 0:0,0:1 --append-to 1:0:0:0,1:1:0:1
//

func (self *baseDownloader) merge(output string, files []string) {
    cmd := exec.Command(
                mkvmerge,
                "--output",
                output,
            )

    for i, f := range files {
        if i != 0 {
            cmd.Args = append(cmd.Args, "+")
        }

        cmd.Args = append(cmd.Args, "(")
        cmd.Args = append(cmd.Args, f)
        cmd.Args = append(cmd.Args, ")")
    }

    fmt.Println(cmd.Args)

    o, err := cmd.Output()
    fmt.Println(string(o))
    fmt.Println(err)
}
