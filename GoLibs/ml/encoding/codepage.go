package encoding

const (
    CP_GBK          = 936
    CP_SHIFT_JIS    = 932
    CP_BIG5         = 950
    CP_UTF8         = 65001
    CP_UTF16_LE     = 1200
    CP_UTF16_BE     = 1201
)

var cptext = map[int]string {
    CP_GBK          : "GBK",
    CP_SHIFT_JIS    : "SHIFT JIS",
    CP_BIG5         : "BIG5",
    CP_UTF8         : "UTF8",
    CP_UTF16_LE     : "UTF16_LE",
    CP_UTF16_BE     : "UTF16_BE",
}
