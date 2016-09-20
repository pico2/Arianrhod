package downloader

import (
    . "ml/strings"
    . "ml/dict"
    "ml/net/http2"
    "ml/trace"
)

type baseDownloader struct {
    url     String
    title   String
    links   []String
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

func (self *baseDownloader) Download(path String) DownloadResult {
    trace.Raise(trace.NewNotImplementedError("Download not implemented"))
    return DownloadFailed
}
