package downloader

import (
    . "ml/strings"
)

type Downloader interface {
    Analysis() AnalysisResult
    Download(path String) DownloadResult
    Close()
}
