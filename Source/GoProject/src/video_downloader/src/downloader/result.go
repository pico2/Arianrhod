package downloader


type AnalysisResult int

const (
    AnalysisSuccess AnalysisResult = iota
    AnalysisNotSupported
    AnalysisFailed
)

var analysisResultText = map[AnalysisResult]string{
    AnalysisSuccess         : "Success",
    AnalysisNotSupported    : "NotSupported",
    AnalysisFailed          : "Failed",
}

func (self AnalysisResult) String() string {
    return analysisResultText[self]
}


type DownloadResult int

const (
    DownloadSuccess DownloadResult = iota
    DownloadFailed
    DownloadTimeout
)

var downloadResultText = map[DownloadResult]string{
    DownloadSuccess : "Success",
    DownloadFailed  : "Failed",
    DownloadTimeout : "Timeout",
}

func (self DownloadResult) String() string {
    return downloadResultText[self]
}