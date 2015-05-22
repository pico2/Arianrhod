from ml import *

HCURSOR = PVOID

WNDPROC = ctypes.WINFUNCTYPE(INT_PTR, HWND, UINT, WPARAM, LPARAM)

class WNDCLASSEXW(Structure):
    _fields_ = [
        ('cbSize',          UINT),
        ('style',           UINT),
        ('lpfnWndProc',     WNDPROC),
        ('cbClsExtra',      INT),
        ('cbWndExtra',      INT),
        ('hInstance',       HINSTANCE),
        ('hIcon',           HICON),
        ('hCursor',         HCURSOR),
        ('hbrBackground',   HBRUSH),
        ('lpszMenuName',    PWSTR),
        ('lpszClassName',   PWSTR),
        ('hIconSm',         HICON),
    ]

PWNDCLASSEXW = ctypes.POINTER(WNDCLASSEXW)

class MSG(Structure):
    _fields_ = [
        ('hwnd',    HWND),
        ('message', UINT),
        ('wParam',  WPARAM),
        ('lParam',  LPARAM),
        ('time',    ULONG),
        ('pt',      POINT)
    ]

PMSG = ctypes.POINTER(MSG)

class WINDOWPOS(Structure):
    _fields_ = [
        ('hwnd',            HWND),
        ('hwndInsertAfter', HWND),
        ('x',               LONG),
        ('y',               LONG),
        ('cx',              LONG),
        ('cy',              LONG),
        ('flags',           ULONG),
    ]

PWINDOWPOS = ctypes.POINTER(WINDOWPOS)

class NCCALCSIZE_PARAMS(Structure):
    _fields_ = [
        ('rgrc',    RECT * 3),
        ('lppos',   PWINDOWPOS),
    ]

PNCCALCSIZE_PARAMS = ctypes.POINTER(NCCALCSIZE_PARAMS)

#
# WM_NCCALCSIZE "window valid rect" return values
#
WVR_ALIGNTOP            = 0x0010
WVR_ALIGNLEFT           = 0x0020
WVR_ALIGNBOTTOM         = 0x0040
WVR_ALIGNRIGHT          = 0x0080
WVR_HREDRAW             = 0x0100
WVR_VREDRAW             = 0x0200
WVR_REDRAW              = WVR_HREDRAW | WVR_VREDRAW
WVR_VALIDRECTS          = 0x0400


class MARGINS(Structure):
    _fields_ = [
        ('cxLeftWidth',     LONG),  # width of left border that retains its size
        ('cxRightWidth',    LONG),  # width of right border that retains its size
        ('cyTopHeight',     LONG),  # height of top border that retains its size
        ('cyBottomHeight',  LONG),  # height of bottom border that retains its size
    ]

PMARGINS = ctypes.POINTER(MARGINS)


WM_NULL                                 = 0x0000
WM_CREATE                               = 0x0001
WM_DESTROY                              = 0x0002
WM_MOVE                                 = 0x0003
WM_SIZE                                 = 0x0005
WM_ACTIVATE                             = 0x0006
WM_SETFOCUS                             = 0x0007
WM_KILLFOCUS                            = 0x0008
WM_ENABLE                               = 0x000A
WM_SETREDRAW                            = 0x000B
WM_SETTEXT                              = 0x000C
WM_GETTEXT                              = 0x000D
WM_GETTEXTLENGTH                        = 0x000E
WM_PAINT                                = 0x000F
WM_CLOSE                                = 0x0010
WM_QUERYENDSESSION                      = 0x0011
WM_QUERYOPEN                            = 0x0013
WM_ENDSESSION                           = 0x0016
WM_QUIT                                 = 0x0012
WM_ERASEBKGND                           = 0x0014
WM_SYSCOLORCHANGE                       = 0x0015
WM_SHOWWINDOW                           = 0x0018
WM_WININICHANGE                         = 0x001A
WM_SETTINGCHANGE                        = WM_WININICHANGE
WM_DEVMODECHANGE                        = 0x001B
WM_ACTIVATEAPP                          = 0x001C
WM_FONTCHANGE                           = 0x001D
WM_TIMECHANGE                           = 0x001E
WM_CANCELMODE                           = 0x001F
WM_SETCURSOR                            = 0x0020
WM_MOUSEACTIVATE                        = 0x0021
WM_CHILDACTIVATE                        = 0x0022
WM_QUEUESYNC                            = 0x0023
WM_GETMINMAXINFO                        = 0x0024
WM_PAINTICON                            = 0x0026
WM_ICONERASEBKGND                       = 0x0027
WM_NEXTDLGCTL                           = 0x0028
WM_SPOOLERSTATUS                        = 0x002A
WM_DRAWITEM                             = 0x002B
WM_MEASUREITEM                          = 0x002C
WM_DELETEITEM                           = 0x002D
WM_VKEYTOITEM                           = 0x002E
WM_CHARTOITEM                           = 0x002F
WM_SETFONT                              = 0x0030
WM_GETFONT                              = 0x0031
WM_SETHOTKEY                            = 0x0032
WM_GETHOTKEY                            = 0x0033
WM_QUERYDRAGICON                        = 0x0037
WM_COMPAREITEM                          = 0x0039
WM_GETOBJECT                            = 0x003D
WM_COMPACTING                           = 0x0041
WM_COMMNOTIFY                           = 0x0044
WM_WINDOWPOSCHANGING                    = 0x0046
WM_WINDOWPOSCHANGED                     = 0x0047
WM_POWER                                = 0x0048
WM_COPYDATA                             = 0x004A
WM_CANCELJOURNAL                        = 0x004B
WM_NOTIFY                               = 0x004E
WM_INPUTLANGCHANGEREQUEST               = 0x0050
WM_INPUTLANGCHANGE                      = 0x0051
WM_TCARD                                = 0x0052
WM_HELP                                 = 0x0053
WM_USERCHANGED                          = 0x0054
WM_NOTIFYFORMAT                         = 0x0055
WM_CONTEXTMENU                          = 0x007B
WM_STYLECHANGING                        = 0x007C
WM_STYLECHANGED                         = 0x007D
WM_DISPLAYCHANGE                        = 0x007E
WM_GETICON                              = 0x007F
WM_SETICON                              = 0x0080
WM_NCCREATE                             = 0x0081
WM_NCDESTROY                            = 0x0082
WM_NCCALCSIZE                           = 0x0083
WM_NCHITTEST                            = 0x0084
WM_NCPAINT                              = 0x0085
WM_NCACTIVATE                           = 0x0086
WM_GETDLGCODE                           = 0x0087
WM_SYNCPAINT                            = 0x0088
WM_NCMOUSEMOVE                          = 0x00A0
WM_NCLBUTTONDOWN                        = 0x00A1
WM_NCLBUTTONUP                          = 0x00A2
WM_NCLBUTTONDBLCLK                      = 0x00A3
WM_NCRBUTTONDOWN                        = 0x00A4
WM_NCRBUTTONUP                          = 0x00A5
WM_NCRBUTTONDBLCLK                      = 0x00A6
WM_NCMBUTTONDOWN                        = 0x00A7
WM_NCMBUTTONUP                          = 0x00A8
WM_NCMBUTTONDBLCLK                      = 0x00A9
WM_NCXBUTTONDOWN                        = 0x00AB
WM_NCXBUTTONUP                          = 0x00AC
WM_NCXBUTTONDBLCLK                      = 0x00AD
WM_INPUT_DEVICE_CHANGE                  = 0x00FE
WM_INPUT                                = 0x00FF
WM_KEYFIRST                             = 0x0100
WM_KEYDOWN                              = 0x0100
WM_KEYUP                                = 0x0101
WM_CHAR                                 = 0x0102
WM_DEADCHAR                             = 0x0103
WM_SYSKEYDOWN                           = 0x0104
WM_SYSKEYUP                             = 0x0105
WM_SYSCHAR                              = 0x0106
WM_SYSDEADCHAR                          = 0x0107
WM_UNICHAR                              = 0x0109
WM_KEYLAST                              = 0x0109
WM_KEYLAST                              = 0x0108
WM_IME_STARTCOMPOSITION                 = 0x010D
WM_IME_ENDCOMPOSITION                   = 0x010E
WM_IME_COMPOSITION                      = 0x010F
WM_IME_KEYLAST                          = 0x010F
WM_INITDIALOG                           = 0x0110
WM_COMMAND                              = 0x0111
WM_SYSCOMMAND                           = 0x0112
WM_TIMER                                = 0x0113
WM_HSCROLL                              = 0x0114
WM_VSCROLL                              = 0x0115
WM_INITMENU                             = 0x0116
WM_INITMENUPOPUP                        = 0x0117
WM_GESTURE                              = 0x0119
WM_GESTURENOTIFY                        = 0x011A
WM_MENUSELECT                           = 0x011F
WM_MENUCHAR                             = 0x0120
WM_ENTERIDLE                            = 0x0121
WM_MENURBUTTONUP                        = 0x0122
WM_MENUDRAG                             = 0x0123
WM_MENUGETOBJECT                        = 0x0124
WM_UNINITMENUPOPUP                      = 0x0125
WM_MENUCOMMAND                          = 0x0126
WM_CHANGEUISTATE                        = 0x0127
WM_UPDATEUISTATE                        = 0x0128
WM_QUERYUISTATE                         = 0x0129
WM_CTLCOLORMSGBOX                       = 0x0132
WM_CTLCOLOREDIT                         = 0x0133
WM_CTLCOLORLISTBOX                      = 0x0134
WM_CTLCOLORBTN                          = 0x0135
WM_CTLCOLORDLG                          = 0x0136
WM_CTLCOLORSCROLLBAR                    = 0x0137
WM_CTLCOLORSTATIC                       = 0x0138
WM_MOUSEFIRST                           = 0x0200
WM_MOUSEMOVE                            = 0x0200
WM_LBUTTONDOWN                          = 0x0201
WM_LBUTTONUP                            = 0x0202
WM_LBUTTONDBLCLK                        = 0x0203
WM_RBUTTONDOWN                          = 0x0204
WM_RBUTTONUP                            = 0x0205
WM_RBUTTONDBLCLK                        = 0x0206
WM_MBUTTONDOWN                          = 0x0207
WM_MBUTTONUP                            = 0x0208
WM_MBUTTONDBLCLK                        = 0x0209
WM_MOUSEWHEEL                           = 0x020A
WM_XBUTTONDOWN                          = 0x020B
WM_XBUTTONUP                            = 0x020C
WM_XBUTTONDBLCLK                        = 0x020D
WM_MOUSEHWHEEL                          = 0x020E
WM_MOUSELAST                            = 0x020E
WM_MOUSELAST                            = 0x020D
WM_MOUSELAST                            = 0x020A
WM_MOUSELAST                            = 0x0209
WM_PARENTNOTIFY                         = 0x0210
WM_ENTERMENULOOP                        = 0x0211
WM_EXITMENULOOP                         = 0x0212
WM_NEXTMENU                             = 0x0213
WM_SIZING                               = 0x0214
WM_CAPTURECHANGED                       = 0x0215
WM_MOVING                               = 0x0216
WM_POWERBROADCAST                       = 0x0218
WM_DEVICECHANGE                         = 0x0219
WM_MDICREATE                            = 0x0220
WM_MDIDESTROY                           = 0x0221
WM_MDIACTIVATE                          = 0x0222
WM_MDIRESTORE                           = 0x0223
WM_MDINEXT                              = 0x0224
WM_MDIMAXIMIZE                          = 0x0225
WM_MDITILE                              = 0x0226
WM_MDICASCADE                           = 0x0227
WM_MDIICONARRANGE                       = 0x0228
WM_MDIGETACTIVE                         = 0x0229
WM_MDISETMENU                           = 0x0230
WM_ENTERSIZEMOVE                        = 0x0231
WM_EXITSIZEMOVE                         = 0x0232
WM_DROPFILES                            = 0x0233
WM_MDIREFRESHMENU                       = 0x0234
WM_TOUCH                                = 0x0240
WM_IME_SETCONTEXT                       = 0x0281
WM_IME_NOTIFY                           = 0x0282
WM_IME_CONTROL                          = 0x0283
WM_IME_COMPOSITIONFULL                  = 0x0284
WM_IME_SELECT                           = 0x0285
WM_IME_CHAR                             = 0x0286
WM_IME_REQUEST                          = 0x0288
WM_IME_KEYDOWN                          = 0x0290
WM_IME_KEYUP                            = 0x0291
WM_MOUSEHOVER                           = 0x02A1
WM_MOUSELEAVE                           = 0x02A3
WM_NCMOUSEHOVER                         = 0x02A0
WM_NCMOUSELEAVE                         = 0x02A2
WM_WTSSESSION_CHANGE                    = 0x02B1
WM_TABLET_FIRST                         = 0x02c0
WM_TABLET_LAST                          = 0x02df
WM_CUT                                  = 0x0300
WM_COPY                                 = 0x0301
WM_PASTE                                = 0x0302
WM_CLEAR                                = 0x0303
WM_UNDO                                 = 0x0304
WM_RENDERFORMAT                         = 0x0305
WM_RENDERALLFORMATS                     = 0x0306
WM_DESTROYCLIPBOARD                     = 0x0307
WM_DRAWCLIPBOARD                        = 0x0308
WM_PAINTCLIPBOARD                       = 0x0309
WM_VSCROLLCLIPBOARD                     = 0x030A
WM_SIZECLIPBOARD                        = 0x030B
WM_ASKCBFORMATNAME                      = 0x030C
WM_CHANGECBCHAIN                        = 0x030D
WM_HSCROLLCLIPBOARD                     = 0x030E
WM_QUERYNEWPALETTE                      = 0x030F
WM_PALETTEISCHANGING                    = 0x0310
WM_PALETTECHANGED                       = 0x0311
WM_HOTKEY                               = 0x0312
WM_PRINT                                = 0x0317
WM_PRINTCLIENT                          = 0x0318
WM_APPCOMMAND                           = 0x0319
WM_THEMECHANGED                         = 0x031A
WM_CLIPBOARDUPDATE                      = 0x031D
WM_DWMCOMPOSITIONCHANGED                = 0x031E
WM_DWMNCRENDERINGCHANGED                = 0x031F
WM_DWMCOLORIZATIONCOLORCHANGED          = 0x0320
WM_DWMWINDOWMAXIMIZEDCHANGE             = 0x0321
WM_DWMSENDICONICTHUMBNAIL               = 0x0323
WM_DWMSENDICONICLIVEPREVIEWBITMAP       = 0x0326
WM_GETTITLEBARINFOEX                    = 0x033F
WM_HANDHELDFIRST                        = 0x0358
WM_HANDHELDLAST                         = 0x035F
WM_AFXFIRST                             = 0x0360
WM_AFXLAST                              = 0x037F
WM_PENWINFIRST                          = 0x0380
WM_PENWINLAST                           = 0x038F
WM_USER                                 = 0x0400

EM_GETSEL                               = 0x00B0
EM_SETSEL                               = 0x00B1
EM_GETRECT                              = 0x00B2
EM_SETRECT                              = 0x00B3
EM_SETRECTNP                            = 0x00B4
EM_SCROLL                               = 0x00B5
EM_LINESCROLL                           = 0x00B6
EM_SCROLLCARET                          = 0x00B7
EM_GETMODIFY                            = 0x00B8
EM_SETMODIFY                            = 0x00B9
EM_GETLINECOUNT                         = 0x00BA
EM_LINEINDEX                            = 0x00BB
EM_SETHANDLE                            = 0x00BC
EM_GETHANDLE                            = 0x00BD
EM_GETTHUMB                             = 0x00BE
EM_LINELENGTH                           = 0x00C1
EM_REPLACESEL                           = 0x00C2
EM_GETLINE                              = 0x00C4
EM_LIMITTEXT                            = 0x00C5
EM_CANUNDO                              = 0x00C6
EM_UNDO                                 = 0x00C7
EM_FMTLINES                             = 0x00C8
EM_LINEFROMCHAR                         = 0x00C9
EM_SETTABSTOPS                          = 0x00CB
EM_SETPASSWORDCHAR                      = 0x00CC
EM_EMPTYUNDOBUFFER                      = 0x00CD
EM_GETFIRSTVISIBLELINE                  = 0x00CE
EM_SETREADONLY                          = 0x00CF
EM_SETWORDBREAKPROC                     = 0x00D0
EM_GETWORDBREAKPROC                     = 0x00D1
EM_GETPASSWORDCHAR                      = 0x00D2
EM_SETMARGINS                           = 0x00D3
EM_GETMARGINS                           = 0x00D4
EM_GETLIMITTEXT                         = 0x00D5
EM_POSFROMCHAR                          = 0x00D6
EM_CHARFROMPOS                          = 0x00D7
EM_SETIMESTATUS                         = 0x00D8
EM_GETIMESTATUS                         = 0x00D9

SBM_SETPOS                              = 0x00E0
SBM_GETPOS                              = 0x00E1
SBM_SETRANGE                            = 0x00E2
SBM_SETRANGEREDRAW                      = 0x00E6
SBM_GETRANGE                            = 0x00E3
SBM_ENABLE_ARROWS                       = 0x00E4
SBM_SETSCROLLINFO                       = 0x00E9
SBM_GETSCROLLINFO                       = 0x00EA
SBM_GETSCROLLBARINFO                    = 0x00EB

CB_GETEDITSEL                           = 0x0140
CB_LIMITTEXT                            = 0x0141
CB_SETEDITSEL                           = 0x0142
CB_ADDSTRING                            = 0x0143
CB_DELETESTRING                         = 0x0144
CB_DIR                                  = 0x0145
CB_GETCOUNT                             = 0x0146
CB_GETCURSEL                            = 0x0147
CB_GETLBTEXT                            = 0x0148
CB_GETLBTEXTLEN                         = 0x0149
CB_INSERTSTRING                         = 0x014A
CB_RESETCONTENT                         = 0x014B
CB_FINDSTRING                           = 0x014C
CB_SELECTSTRING                         = 0x014D
CB_SETCURSEL                            = 0x014E
CB_SHOWDROPDOWN                         = 0x014F
CB_GETITEMDATA                          = 0x0150
CB_SETITEMDATA                          = 0x0151
CB_GETDROPPEDCONTROLRECT                = 0x0152
CB_SETITEMHEIGHT                        = 0x0153
CB_GETITEMHEIGHT                        = 0x0154
CB_SETEXTENDEDUI                        = 0x0155
CB_GETEXTENDEDUI                        = 0x0156
CB_GETDROPPEDSTATE                      = 0x0157
CB_FINDSTRINGEXACT                      = 0x0158
CB_SETLOCALE                            = 0x0159
CB_GETLOCALE                            = 0x015A
CB_GETTOPINDEX                          = 0x015b
CB_SETTOPINDEX                          = 0x015c
CB_GETHORIZONTALEXTENT                  = 0x015d
CB_SETHORIZONTALEXTENT                  = 0x015e
CB_GETDROPPEDWIDTH                      = 0x015f
CB_SETDROPPEDWIDTH                      = 0x0160
CB_INITSTORAGE                          = 0x0161
CB_MULTIPLEADDSTRING                    = 0x0163
CB_GETCOMBOBOXINFO                      = 0x0164

STM_SETICON                             = 0x0170
STM_GETICON                             = 0x0171
STM_SETIMAGE                            = 0x0172
STM_GETIMAGE                            = 0x0173

LB_ADDSTRING                            = 0x0180
LB_INSERTSTRING                         = 0x0181
LB_DELETESTRING                         = 0x0182
LB_SELITEMRANGEEX                       = 0x0183
LB_RESETCONTENT                         = 0x0184
LB_SETSEL                               = 0x0185
LB_SETCURSEL                            = 0x0186
LB_GETSEL                               = 0x0187
LB_GETCURSEL                            = 0x0188
LB_GETTEXT                              = 0x0189
LB_GETTEXTLEN                           = 0x018A
LB_GETCOUNT                             = 0x018B
LB_SELECTSTRING                         = 0x018C
LB_DIR                                  = 0x018D
LB_GETTOPINDEX                          = 0x018E
LB_FINDSTRING                           = 0x018F
LB_GETSELCOUNT                          = 0x0190
LB_GETSELITEMS                          = 0x0191
LB_SETTABSTOPS                          = 0x0192
LB_GETHORIZONTALEXTENT                  = 0x0193
LB_SETHORIZONTALEXTENT                  = 0x0194
LB_SETCOLUMNWIDTH                       = 0x0195
LB_ADDFILE                              = 0x0196
LB_SETTOPINDEX                          = 0x0197
LB_GETITEMRECT                          = 0x0198
LB_GETITEMDATA                          = 0x0199
LB_SETITEMDATA                          = 0x019A
LB_SELITEMRANGE                         = 0x019B
LB_SETANCHORINDEX                       = 0x019C
LB_GETANCHORINDEX                       = 0x019D
LB_SETCARETINDEX                        = 0x019E
LB_GETCARETINDEX                        = 0x019F
LB_SETITEMHEIGHT                        = 0x01A0
LB_GETITEMHEIGHT                        = 0x01A1
LB_FINDSTRINGEXACT                      = 0x01A2
LB_SETLOCALE                            = 0x01A5
LB_GETLOCALE                            = 0x01A6
LB_SETCOUNT                             = 0x01A7
LB_INITSTORAGE                          = 0x01A8
LB_ITEMFROMPOINT                        = 0x01A9
LB_MULTIPLEADDSTRING                    = 0x01B1
LB_GETLISTBOXINFO                       = 0x01B2


#
# WM_NCHITTEST and MOUSEHOOKSTRUCT Mouse Position Codes
#

HTERROR                                 = (-2)
HTTRANSPARENT                           = (-1)
HTNOWHERE                               = 0
HTCLIENT                                = 1
HTCAPTION                               = 2
HTSYSMENU                               = 3
HTGROWBOX                               = 4
HTSIZE                                  = HTGROWBOX
HTMENU                                  = 5
HTHSCROLL                               = 6
HTVSCROLL                               = 7
HTMINBUTTON                             = 8
HTMAXBUTTON                             = 9
HTLEFT                                  = 10
HTRIGHT                                 = 11
HTTOP                                   = 12
HTTOPLEFT                               = 13
HTTOPRIGHT                              = 14
HTBOTTOM                                = 15
HTBOTTOMLEFT                            = 16
HTBOTTOMRIGHT                           = 17
HTBORDER                                = 18
HTREDUCE                                = HTMINBUTTON
HTZOOM                                  = HTMAXBUTTON
HTSIZEFIRST                             = HTLEFT
HTSIZELAST                              = HTBOTTOMRIGHT
HTOBJECT                                = 19
HTCLOSE                                 = 20
HTHELP                                  = 21


#
# SetWindowPos Flags
#

SWP_NOSIZE                              = 0x0001
SWP_NOMOVE                              = 0x0002
SWP_NOZORDER                            = 0x0004
SWP_NOREDRAW                            = 0x0008
SWP_NOACTIVATE                          = 0x0010
SWP_FRAMECHANGED                        = 0x0020  # The frame changed: send WM_NCCALCSIZE
SWP_SHOWWINDOW                          = 0x0040
SWP_HIDEWINDOW                          = 0x0080
SWP_NOCOPYBITS                          = 0x0100
SWP_NOOWNERZORDER                       = 0x0200  # Don't do owner Z ordering
SWP_NOSENDCHANGING                      = 0x0400  # Don't send WM_WINDOWPOSCHANGING

SWP_DRAWFRAME                           = SWP_FRAMECHANGED
SWP_NOREPOSITION                        = SWP_NOOWNERZORDER

#
# Window Styles
#

WS_OVERLAPPED                           = 0x00000000
WS_POPUP                                = 0x80000000
WS_CHILD                                = 0x40000000
WS_MINIMIZE                             = 0x20000000
WS_VISIBLE                              = 0x10000000
WS_DISABLED                             = 0x08000000
WS_CLIPSIBLINGS                         = 0x04000000
WS_CLIPCHILDREN                         = 0x02000000
WS_MAXIMIZE                             = 0x01000000
WS_CAPTION                              = 0x00C00000   # WS_BORDER | WS_DLGFRAME
WS_BORDER                               = 0x00800000
WS_DLGFRAME                             = 0x00400000
WS_VSCROLL                              = 0x00200000
WS_HSCROLL                              = 0x00100000
WS_SYSMENU                              = 0x00080000
WS_THICKFRAME                           = 0x00040000
WS_GROUP                                = 0x00020000
WS_TABSTOP                              = 0x00010000

WS_MINIMIZEBOX                          = 0x00020000
WS_MAXIMIZEBOX                          = 0x00010000


#
# Common Window Styles
#

WS_OVERLAPPEDWINDOW                     = (WS_OVERLAPPED     | \
                                             WS_CAPTION        | \
                                             WS_SYSMENU        | \
                                             WS_THICKFRAME     | \
                                             WS_MINIMIZEBOX    | \
                                             WS_MAXIMIZEBOX)

WS_POPUPWINDOW                          = (WS_POPUP          | \
                                             WS_BORDER         | \
                                             WS_SYSMENU)

WS_CHILDWINDOW                          = (WS_CHILD)


WS_TILED                                = WS_OVERLAPPED
WS_ICONIC                               = WS_MINIMIZE
WS_SIZEBOX                              = WS_THICKFRAME
WS_TILEDWINDOW                          = WS_OVERLAPPEDWINDOW

#
# Extended Window Styles
#
WS_EX_DLGMODALFRAME                     = 0x00000001
WS_EX_NOPARENTNOTIFY                    = 0x00000004
WS_EX_TOPMOST                           = 0x00000008
WS_EX_ACCEPTFILES                       = 0x00000010
WS_EX_TRANSPARENT                       = 0x00000020

WS_EX_MDICHILD                          = 0x00000040
WS_EX_TOOLWINDOW                        = 0x00000080
WS_EX_WINDOWEDGE                        = 0x00000100
WS_EX_CLIENTEDGE                        = 0x00000200
WS_EX_CONTEXTHELP                       = 0x00000400

WS_EX_RIGHT                             = 0x00001000
WS_EX_LEFT                              = 0x00000000
WS_EX_RTLREADING                        = 0x00002000
WS_EX_LTRREADING                        = 0x00000000
WS_EX_LEFTSCROLLBAR                     = 0x00004000
WS_EX_RIGHTSCROLLBAR                    = 0x00000000

WS_EX_CONTROLPARENT                     = 0x00010000
WS_EX_STATICEDGE                        = 0x00020000
WS_EX_APPWINDOW                         = 0x00040000

WS_EX_OVERLAPPEDWINDOW                  = WS_EX_WINDOWEDGE | WS_EX_CLIENTEDGE
WS_EX_PALETTEWINDOW                     = WS_EX_WINDOWEDGE | WS_EX_TOOLWINDOW | WS_EX_TOPMOST

WS_EX_LAYERED                           = 0x00080000

WS_EX_NOINHERITLAYOUT                   = 0x00100000 # Disable inheritence of mirroring by children
WS_EX_LAYOUTRTL                         = 0x00400000 # Right to left mirroring

WS_EX_COMPOSITED                        = 0x02000000
WS_EX_NOACTIVATE                        = 0x08000000




#
# Window field offsets for GetWindowLong()
#

GWL_STYLE                               = (-16)
GWL_EXSTYLE                             = (-20)
GWL_ID                                  = (-12)
GWLP_WNDPROC                            = (-4)
GWLP_HINSTANCE                          = (-6)
GWLP_HWNDPARENT                         = (-8)
GWLP_USERDATA                           = (-21)
GWLP_ID                                 = (-12)

MessageText = []

i = 0
while i <= WM_USER:
    MessageText.append('0x%04X' % i)
    i = i + 1

MessageText[WM_NULL] = 'WM_NULL'
MessageText[WM_CREATE] = 'WM_CREATE'
MessageText[WM_DESTROY] = 'WM_DESTROY'
MessageText[WM_MOVE] = 'WM_MOVE'
MessageText[WM_SIZE] = 'WM_SIZE'
MessageText[WM_ACTIVATE] = 'WM_ACTIVATE'
MessageText[WM_SETFOCUS] = 'WM_SETFOCUS'
MessageText[WM_KILLFOCUS] = 'WM_KILLFOCUS'
MessageText[WM_ENABLE] = 'WM_ENABLE'
MessageText[WM_SETREDRAW] = 'WM_SETREDRAW'
MessageText[WM_SETTEXT] = 'WM_SETTEXT'
MessageText[WM_GETTEXT] = 'WM_GETTEXT'
MessageText[WM_GETTEXTLENGTH] = 'WM_GETTEXTLENGTH'
MessageText[WM_PAINT] = 'WM_PAINT'
MessageText[WM_CLOSE] = 'WM_CLOSE'
MessageText[WM_QUERYENDSESSION] = 'WM_QUERYENDSESSION'
MessageText[WM_QUERYOPEN] = 'WM_QUERYOPEN'
MessageText[WM_ENDSESSION] = 'WM_ENDSESSION'
MessageText[WM_QUIT] = 'WM_QUIT'
MessageText[WM_ERASEBKGND] = 'WM_ERASEBKGND'
MessageText[WM_SYSCOLORCHANGE] = 'WM_SYSCOLORCHANGE'
MessageText[WM_SHOWWINDOW] = 'WM_SHOWWINDOW'
MessageText[WM_WININICHANGE] = 'WM_WININICHANGE'
MessageText[WM_SETTINGCHANGE] = 'WM_SETTINGCHANGE'
MessageText[WM_DEVMODECHANGE] = 'WM_DEVMODECHANGE'
MessageText[WM_ACTIVATEAPP] = 'WM_ACTIVATEAPP'
MessageText[WM_FONTCHANGE] = 'WM_FONTCHANGE'
MessageText[WM_TIMECHANGE] = 'WM_TIMECHANGE'
MessageText[WM_CANCELMODE] = 'WM_CANCELMODE'
MessageText[WM_SETCURSOR] = 'WM_SETCURSOR'
MessageText[WM_MOUSEACTIVATE] = 'WM_MOUSEACTIVATE'
MessageText[WM_CHILDACTIVATE] = 'WM_CHILDACTIVATE'
MessageText[WM_QUEUESYNC] = 'WM_QUEUESYNC'
MessageText[WM_GETMINMAXINFO] = 'WM_GETMINMAXINFO'
MessageText[WM_PAINTICON] = 'WM_PAINTICON'
MessageText[WM_ICONERASEBKGND] = 'WM_ICONERASEBKGND'
MessageText[WM_NEXTDLGCTL] = 'WM_NEXTDLGCTL'
MessageText[WM_SPOOLERSTATUS] = 'WM_SPOOLERSTATUS'
MessageText[WM_DRAWITEM] = 'WM_DRAWITEM'
MessageText[WM_MEASUREITEM] = 'WM_MEASUREITEM'
MessageText[WM_DELETEITEM] = 'WM_DELETEITEM'
MessageText[WM_VKEYTOITEM] = 'WM_VKEYTOITEM'
MessageText[WM_CHARTOITEM] = 'WM_CHARTOITEM'
MessageText[WM_SETFONT] = 'WM_SETFONT'
MessageText[WM_GETFONT] = 'WM_GETFONT'
MessageText[WM_SETHOTKEY] = 'WM_SETHOTKEY'
MessageText[WM_GETHOTKEY] = 'WM_GETHOTKEY'
MessageText[WM_QUERYDRAGICON] = 'WM_QUERYDRAGICON'
MessageText[WM_COMPAREITEM] = 'WM_COMPAREITEM'
MessageText[WM_GETOBJECT] = 'WM_GETOBJECT'
MessageText[WM_COMPACTING] = 'WM_COMPACTING'
MessageText[WM_COMMNOTIFY] = 'WM_COMMNOTIFY'
MessageText[WM_WINDOWPOSCHANGING] = 'WM_WINDOWPOSCHANGING'
MessageText[WM_WINDOWPOSCHANGED] = 'WM_WINDOWPOSCHANGED'
MessageText[WM_POWER] = 'WM_POWER'
MessageText[WM_COPYDATA] = 'WM_COPYDATA'
MessageText[WM_CANCELJOURNAL] = 'WM_CANCELJOURNAL'
MessageText[WM_NOTIFY] = 'WM_NOTIFY'
MessageText[WM_INPUTLANGCHANGEREQUEST] = 'WM_INPUTLANGCHANGEREQUEST'
MessageText[WM_INPUTLANGCHANGE] = 'WM_INPUTLANGCHANGE'
MessageText[WM_TCARD] = 'WM_TCARD'
MessageText[WM_HELP] = 'WM_HELP'
MessageText[WM_USERCHANGED] = 'WM_USERCHANGED'
MessageText[WM_NOTIFYFORMAT] = 'WM_NOTIFYFORMAT'
MessageText[WM_CONTEXTMENU] = 'WM_CONTEXTMENU'
MessageText[WM_STYLECHANGING] = 'WM_STYLECHANGING'
MessageText[WM_STYLECHANGED] = 'WM_STYLECHANGED'
MessageText[WM_DISPLAYCHANGE] = 'WM_DISPLAYCHANGE'
MessageText[WM_GETICON] = 'WM_GETICON'
MessageText[WM_SETICON] = 'WM_SETICON'
MessageText[WM_NCCREATE] = 'WM_NCCREATE'
MessageText[WM_NCDESTROY] = 'WM_NCDESTROY'
MessageText[WM_NCCALCSIZE] = 'WM_NCCALCSIZE'
MessageText[WM_NCHITTEST] = 'WM_NCHITTEST'
MessageText[WM_NCPAINT] = 'WM_NCPAINT'
MessageText[WM_NCACTIVATE] = 'WM_NCACTIVATE'
MessageText[WM_GETDLGCODE] = 'WM_GETDLGCODE'
MessageText[WM_SYNCPAINT] = 'WM_SYNCPAINT'
MessageText[WM_NCMOUSEMOVE] = 'WM_NCMOUSEMOVE'
MessageText[WM_NCLBUTTONDOWN] = 'WM_NCLBUTTONDOWN'
MessageText[WM_NCLBUTTONUP] = 'WM_NCLBUTTONUP'
MessageText[WM_NCLBUTTONDBLCLK] = 'WM_NCLBUTTONDBLCLK'
MessageText[WM_NCRBUTTONDOWN] = 'WM_NCRBUTTONDOWN'
MessageText[WM_NCRBUTTONUP] = 'WM_NCRBUTTONUP'
MessageText[WM_NCRBUTTONDBLCLK] = 'WM_NCRBUTTONDBLCLK'
MessageText[WM_NCMBUTTONDOWN] = 'WM_NCMBUTTONDOWN'
MessageText[WM_NCMBUTTONUP] = 'WM_NCMBUTTONUP'
MessageText[WM_NCMBUTTONDBLCLK] = 'WM_NCMBUTTONDBLCLK'
MessageText[WM_NCXBUTTONDOWN] = 'WM_NCXBUTTONDOWN'
MessageText[WM_NCXBUTTONUP] = 'WM_NCXBUTTONUP'
MessageText[WM_NCXBUTTONDBLCLK] = 'WM_NCXBUTTONDBLCLK'
MessageText[WM_INPUT_DEVICE_CHANGE] = 'WM_INPUT_DEVICE_CHANGE'
MessageText[WM_INPUT] = 'WM_INPUT'
MessageText[WM_KEYFIRST] = 'WM_KEYFIRST'
MessageText[WM_KEYDOWN] = 'WM_KEYDOWN'
MessageText[WM_KEYUP] = 'WM_KEYUP'
MessageText[WM_CHAR] = 'WM_CHAR'
MessageText[WM_DEADCHAR] = 'WM_DEADCHAR'
MessageText[WM_SYSKEYDOWN] = 'WM_SYSKEYDOWN'
MessageText[WM_SYSKEYUP] = 'WM_SYSKEYUP'
MessageText[WM_SYSCHAR] = 'WM_SYSCHAR'
MessageText[WM_SYSDEADCHAR] = 'WM_SYSDEADCHAR'
MessageText[WM_UNICHAR] = 'WM_UNICHAR'
MessageText[WM_KEYLAST] = 'WM_KEYLAST'
MessageText[WM_KEYLAST] = 'WM_KEYLAST'
MessageText[WM_IME_STARTCOMPOSITION] = 'WM_IME_STARTCOMPOSITION'
MessageText[WM_IME_ENDCOMPOSITION] = 'WM_IME_ENDCOMPOSITION'
MessageText[WM_IME_COMPOSITION] = 'WM_IME_COMPOSITION'
MessageText[WM_IME_KEYLAST] = 'WM_IME_KEYLAST'
MessageText[WM_INITDIALOG] = 'WM_INITDIALOG'
MessageText[WM_COMMAND] = 'WM_COMMAND'
MessageText[WM_SYSCOMMAND] = 'WM_SYSCOMMAND'
MessageText[WM_TIMER] = 'WM_TIMER'
MessageText[WM_HSCROLL] = 'WM_HSCROLL'
MessageText[WM_VSCROLL] = 'WM_VSCROLL'
MessageText[WM_INITMENU] = 'WM_INITMENU'
MessageText[WM_INITMENUPOPUP] = 'WM_INITMENUPOPUP'
MessageText[WM_GESTURE] = 'WM_GESTURE'
MessageText[WM_GESTURENOTIFY] = 'WM_GESTURENOTIFY'
MessageText[WM_MENUSELECT] = 'WM_MENUSELECT'
MessageText[WM_MENUCHAR] = 'WM_MENUCHAR'
MessageText[WM_ENTERIDLE] = 'WM_ENTERIDLE'
MessageText[WM_MENURBUTTONUP] = 'WM_MENURBUTTONUP'
MessageText[WM_MENUDRAG] = 'WM_MENUDRAG'
MessageText[WM_MENUGETOBJECT] = 'WM_MENUGETOBJECT'
MessageText[WM_UNINITMENUPOPUP] = 'WM_UNINITMENUPOPUP'
MessageText[WM_MENUCOMMAND] = 'WM_MENUCOMMAND'
MessageText[WM_CHANGEUISTATE] = 'WM_CHANGEUISTATE'
MessageText[WM_UPDATEUISTATE] = 'WM_UPDATEUISTATE'
MessageText[WM_QUERYUISTATE] = 'WM_QUERYUISTATE'
MessageText[WM_CTLCOLORMSGBOX] = 'WM_CTLCOLORMSGBOX'
MessageText[WM_CTLCOLOREDIT] = 'WM_CTLCOLOREDIT'
MessageText[WM_CTLCOLORLISTBOX] = 'WM_CTLCOLORLISTBOX'
MessageText[WM_CTLCOLORBTN] = 'WM_CTLCOLORBTN'
MessageText[WM_CTLCOLORDLG] = 'WM_CTLCOLORDLG'
MessageText[WM_CTLCOLORSCROLLBAR] = 'WM_CTLCOLORSCROLLBAR'
MessageText[WM_CTLCOLORSTATIC] = 'WM_CTLCOLORSTATIC'
MessageText[WM_MOUSEFIRST] = 'WM_MOUSEFIRST'
MessageText[WM_MOUSEMOVE] = 'WM_MOUSEMOVE'
MessageText[WM_LBUTTONDOWN] = 'WM_LBUTTONDOWN'
MessageText[WM_LBUTTONUP] = 'WM_LBUTTONUP'
MessageText[WM_LBUTTONDBLCLK] = 'WM_LBUTTONDBLCLK'
MessageText[WM_RBUTTONDOWN] = 'WM_RBUTTONDOWN'
MessageText[WM_RBUTTONUP] = 'WM_RBUTTONUP'
MessageText[WM_RBUTTONDBLCLK] = 'WM_RBUTTONDBLCLK'
MessageText[WM_MBUTTONDOWN] = 'WM_MBUTTONDOWN'
MessageText[WM_MBUTTONUP] = 'WM_MBUTTONUP'
MessageText[WM_MBUTTONDBLCLK] = 'WM_MBUTTONDBLCLK'
MessageText[WM_MOUSEWHEEL] = 'WM_MOUSEWHEEL'
MessageText[WM_XBUTTONDOWN] = 'WM_XBUTTONDOWN'
MessageText[WM_XBUTTONUP] = 'WM_XBUTTONUP'
MessageText[WM_XBUTTONDBLCLK] = 'WM_XBUTTONDBLCLK'
MessageText[WM_MOUSEHWHEEL] = 'WM_MOUSEHWHEEL'
MessageText[WM_MOUSELAST] = 'WM_MOUSELAST'
MessageText[WM_MOUSELAST] = 'WM_MOUSELAST'
MessageText[WM_MOUSELAST] = 'WM_MOUSELAST'
MessageText[WM_MOUSELAST] = 'WM_MOUSELAST'
MessageText[WM_PARENTNOTIFY] = 'WM_PARENTNOTIFY'
MessageText[WM_ENTERMENULOOP] = 'WM_ENTERMENULOOP'
MessageText[WM_EXITMENULOOP] = 'WM_EXITMENULOOP'
MessageText[WM_NEXTMENU] = 'WM_NEXTMENU'
MessageText[WM_SIZING] = 'WM_SIZING'
MessageText[WM_CAPTURECHANGED] = 'WM_CAPTURECHANGED'
MessageText[WM_MOVING] = 'WM_MOVING'
MessageText[WM_POWERBROADCAST] = 'WM_POWERBROADCAST'
MessageText[WM_DEVICECHANGE] = 'WM_DEVICECHANGE'
MessageText[WM_MDICREATE] = 'WM_MDICREATE'
MessageText[WM_MDIDESTROY] = 'WM_MDIDESTROY'
MessageText[WM_MDIACTIVATE] = 'WM_MDIACTIVATE'
MessageText[WM_MDIRESTORE] = 'WM_MDIRESTORE'
MessageText[WM_MDINEXT] = 'WM_MDINEXT'
MessageText[WM_MDIMAXIMIZE] = 'WM_MDIMAXIMIZE'
MessageText[WM_MDITILE] = 'WM_MDITILE'
MessageText[WM_MDICASCADE] = 'WM_MDICASCADE'
MessageText[WM_MDIICONARRANGE] = 'WM_MDIICONARRANGE'
MessageText[WM_MDIGETACTIVE] = 'WM_MDIGETACTIVE'
MessageText[WM_MDISETMENU] = 'WM_MDISETMENU'
MessageText[WM_ENTERSIZEMOVE] = 'WM_ENTERSIZEMOVE'
MessageText[WM_EXITSIZEMOVE] = 'WM_EXITSIZEMOVE'
MessageText[WM_DROPFILES] = 'WM_DROPFILES'
MessageText[WM_MDIREFRESHMENU] = 'WM_MDIREFRESHMENU'
MessageText[WM_TOUCH] = 'WM_TOUCH'
MessageText[WM_IME_SETCONTEXT] = 'WM_IME_SETCONTEXT'
MessageText[WM_IME_NOTIFY] = 'WM_IME_NOTIFY'
MessageText[WM_IME_CONTROL] = 'WM_IME_CONTROL'
MessageText[WM_IME_COMPOSITIONFULL] = 'WM_IME_COMPOSITIONFULL'
MessageText[WM_IME_SELECT] = 'WM_IME_SELECT'
MessageText[WM_IME_CHAR] = 'WM_IME_CHAR'
MessageText[WM_IME_REQUEST] = 'WM_IME_REQUEST'
MessageText[WM_IME_KEYDOWN] = 'WM_IME_KEYDOWN'
MessageText[WM_IME_KEYUP] = 'WM_IME_KEYUP'
MessageText[WM_MOUSEHOVER] = 'WM_MOUSEHOVER'
MessageText[WM_MOUSELEAVE] = 'WM_MOUSELEAVE'
MessageText[WM_NCMOUSEHOVER] = 'WM_NCMOUSEHOVER'
MessageText[WM_NCMOUSELEAVE] = 'WM_NCMOUSELEAVE'
MessageText[WM_WTSSESSION_CHANGE] = 'WM_WTSSESSION_CHANGE'
MessageText[WM_TABLET_FIRST] = 'WM_TABLET_FIRST'
MessageText[WM_TABLET_LAST] = 'WM_TABLET_LAST'
MessageText[WM_CUT] = 'WM_CUT'
MessageText[WM_COPY] = 'WM_COPY'
MessageText[WM_PASTE] = 'WM_PASTE'
MessageText[WM_CLEAR] = 'WM_CLEAR'
MessageText[WM_UNDO] = 'WM_UNDO'
MessageText[WM_RENDERFORMAT] = 'WM_RENDERFORMAT'
MessageText[WM_RENDERALLFORMATS] = 'WM_RENDERALLFORMATS'
MessageText[WM_DESTROYCLIPBOARD] = 'WM_DESTROYCLIPBOARD'
MessageText[WM_DRAWCLIPBOARD] = 'WM_DRAWCLIPBOARD'
MessageText[WM_PAINTCLIPBOARD] = 'WM_PAINTCLIPBOARD'
MessageText[WM_VSCROLLCLIPBOARD] = 'WM_VSCROLLCLIPBOARD'
MessageText[WM_SIZECLIPBOARD] = 'WM_SIZECLIPBOARD'
MessageText[WM_ASKCBFORMATNAME] = 'WM_ASKCBFORMATNAME'
MessageText[WM_CHANGECBCHAIN] = 'WM_CHANGECBCHAIN'
MessageText[WM_HSCROLLCLIPBOARD] = 'WM_HSCROLLCLIPBOARD'
MessageText[WM_QUERYNEWPALETTE] = 'WM_QUERYNEWPALETTE'
MessageText[WM_PALETTEISCHANGING] = 'WM_PALETTEISCHANGING'
MessageText[WM_PALETTECHANGED] = 'WM_PALETTECHANGED'
MessageText[WM_HOTKEY] = 'WM_HOTKEY'
MessageText[WM_PRINT] = 'WM_PRINT'
MessageText[WM_PRINTCLIENT] = 'WM_PRINTCLIENT'
MessageText[WM_APPCOMMAND] = 'WM_APPCOMMAND'
MessageText[WM_THEMECHANGED] = 'WM_THEMECHANGED'
MessageText[WM_CLIPBOARDUPDATE] = 'WM_CLIPBOARDUPDATE'
MessageText[WM_DWMCOMPOSITIONCHANGED] = 'WM_DWMCOMPOSITIONCHANGED'
MessageText[WM_DWMNCRENDERINGCHANGED] = 'WM_DWMNCRENDERINGCHANGED'
MessageText[WM_DWMCOLORIZATIONCOLORCHANGED] = 'WM_DWMCOLORIZATIONCOLORCHANGED'
MessageText[WM_DWMWINDOWMAXIMIZEDCHANGE] = 'WM_DWMWINDOWMAXIMIZEDCHANGE'
MessageText[WM_DWMSENDICONICTHUMBNAIL] = 'WM_DWMSENDICONICTHUMBNAIL'
MessageText[WM_DWMSENDICONICLIVEPREVIEWBITMAP] = 'WM_DWMSENDICONICLIVEPREVIEWBITMAP'
MessageText[WM_GETTITLEBARINFOEX] = 'WM_GETTITLEBARINFOEX'
MessageText[WM_HANDHELDFIRST] = 'WM_HANDHELDFIRST'
MessageText[WM_HANDHELDLAST] = 'WM_HANDHELDLAST'
MessageText[WM_AFXFIRST] = 'WM_AFXFIRST'
MessageText[WM_AFXLAST] = 'WM_AFXLAST'
MessageText[WM_PENWINFIRST] = 'WM_PENWINFIRST'
MessageText[WM_PENWINLAST] = 'WM_PENWINLAST'
MessageText[WM_USER] = 'WM_USER'

MessageText[EM_GETSEL] = 'EM_GETSEL'
MessageText[EM_SETSEL] = 'EM_SETSEL'
MessageText[EM_GETRECT] = 'EM_GETRECT'
MessageText[EM_SETRECT] = 'EM_SETRECT'
MessageText[EM_SETRECTNP] = 'EM_SETRECTNP'
MessageText[EM_SCROLL] = 'EM_SCROLL'
MessageText[EM_LINESCROLL] = 'EM_LINESCROLL'
MessageText[EM_SCROLLCARET] = 'EM_SCROLLCARET'
MessageText[EM_GETMODIFY] = 'EM_GETMODIFY'
MessageText[EM_SETMODIFY] = 'EM_SETMODIFY'
MessageText[EM_GETLINECOUNT] = 'EM_GETLINECOUNT'
MessageText[EM_LINEINDEX] = 'EM_LINEINDEX'
MessageText[EM_SETHANDLE] = 'EM_SETHANDLE'
MessageText[EM_GETHANDLE] = 'EM_GETHANDLE'
MessageText[EM_GETTHUMB] = 'EM_GETTHUMB'
MessageText[EM_LINELENGTH] = 'EM_LINELENGTH'
MessageText[EM_REPLACESEL] = 'EM_REPLACESEL'
MessageText[EM_GETLINE] = 'EM_GETLINE'
MessageText[EM_LIMITTEXT] = 'EM_LIMITTEXT'
MessageText[EM_CANUNDO] = 'EM_CANUNDO'
MessageText[EM_UNDO] = 'EM_UNDO'
MessageText[EM_FMTLINES] = 'EM_FMTLINES'
MessageText[EM_LINEFROMCHAR] = 'EM_LINEFROMCHAR'
MessageText[EM_SETTABSTOPS] = 'EM_SETTABSTOPS'
MessageText[EM_SETPASSWORDCHAR] = 'EM_SETPASSWORDCHAR'
MessageText[EM_EMPTYUNDOBUFFER] = 'EM_EMPTYUNDOBUFFER'
MessageText[EM_GETFIRSTVISIBLELINE] = 'EM_GETFIRSTVISIBLELINE'
MessageText[EM_SETREADONLY] = 'EM_SETREADONLY'
MessageText[EM_SETWORDBREAKPROC] = 'EM_SETWORDBREAKPROC'
MessageText[EM_GETWORDBREAKPROC] = 'EM_GETWORDBREAKPROC'
MessageText[EM_GETPASSWORDCHAR] = 'EM_GETPASSWORDCHAR'
MessageText[EM_SETMARGINS] = 'EM_SETMARGINS'
MessageText[EM_GETMARGINS] = 'EM_GETMARGINS'
MessageText[EM_GETLIMITTEXT] = 'EM_GETLIMITTEXT'
MessageText[EM_POSFROMCHAR] = 'EM_POSFROMCHAR'
MessageText[EM_CHARFROMPOS] = 'EM_CHARFROMPOS'
MessageText[EM_SETIMESTATUS] = 'EM_SETIMESTATUS'
MessageText[EM_GETIMESTATUS] = 'EM_GETIMESTATUS'

MessageText[SBM_SETPOS] = 'SBM_SETPOS'
MessageText[SBM_GETPOS] = 'SBM_GETPOS'
MessageText[SBM_SETRANGE] = 'SBM_SETRANGE'
MessageText[SBM_SETRANGEREDRAW] = 'SBM_SETRANGEREDRAW'
MessageText[SBM_GETRANGE] = 'SBM_GETRANGE'
MessageText[SBM_ENABLE_ARROWS] = 'SBM_ENABLE_ARROWS'
MessageText[SBM_SETSCROLLINFO] = 'SBM_SETSCROLLINFO'
MessageText[SBM_GETSCROLLINFO] = 'SBM_GETSCROLLINFO'
MessageText[SBM_GETSCROLLBARINFO] = 'SBM_GETSCROLLBARINFO'

MessageText[CB_GETEDITSEL] = 'CB_GETEDITSEL'
MessageText[CB_LIMITTEXT] = 'CB_LIMITTEXT'
MessageText[CB_SETEDITSEL] = 'CB_SETEDITSEL'
MessageText[CB_ADDSTRING] = 'CB_ADDSTRING'
MessageText[CB_DELETESTRING] = 'CB_DELETESTRING'
MessageText[CB_DIR] = 'CB_DIR'
MessageText[CB_GETCOUNT] = 'CB_GETCOUNT'
MessageText[CB_GETCURSEL] = 'CB_GETCURSEL'
MessageText[CB_GETLBTEXT] = 'CB_GETLBTEXT'
MessageText[CB_GETLBTEXTLEN] = 'CB_GETLBTEXTLEN'
MessageText[CB_INSERTSTRING] = 'CB_INSERTSTRING'
MessageText[CB_RESETCONTENT] = 'CB_RESETCONTENT'
MessageText[CB_FINDSTRING] = 'CB_FINDSTRING'
MessageText[CB_SELECTSTRING] = 'CB_SELECTSTRING'
MessageText[CB_SETCURSEL] = 'CB_SETCURSEL'
MessageText[CB_SHOWDROPDOWN] = 'CB_SHOWDROPDOWN'
MessageText[CB_GETITEMDATA] = 'CB_GETITEMDATA'
MessageText[CB_SETITEMDATA] = 'CB_SETITEMDATA'
MessageText[CB_GETDROPPEDCONTROLRECT] = 'CB_GETDROPPEDCONTROLRECT'
MessageText[CB_SETITEMHEIGHT] = 'CB_SETITEMHEIGHT'
MessageText[CB_GETITEMHEIGHT] = 'CB_GETITEMHEIGHT'
MessageText[CB_SETEXTENDEDUI] = 'CB_SETEXTENDEDUI'
MessageText[CB_GETEXTENDEDUI] = 'CB_GETEXTENDEDUI'
MessageText[CB_GETDROPPEDSTATE] = 'CB_GETDROPPEDSTATE'
MessageText[CB_FINDSTRINGEXACT] = 'CB_FINDSTRINGEXACT'
MessageText[CB_SETLOCALE] = 'CB_SETLOCALE'
MessageText[CB_GETLOCALE] = 'CB_GETLOCALE'
MessageText[CB_GETTOPINDEX] = 'CB_GETTOPINDEX'
MessageText[CB_SETTOPINDEX] = 'CB_SETTOPINDEX'
MessageText[CB_GETHORIZONTALEXTENT] = 'CB_GETHORIZONTALEXTENT'
MessageText[CB_SETHORIZONTALEXTENT] = 'CB_SETHORIZONTALEXTENT'
MessageText[CB_GETDROPPEDWIDTH] = 'CB_GETDROPPEDWIDTH'
MessageText[CB_SETDROPPEDWIDTH] = 'CB_SETDROPPEDWIDTH'
MessageText[CB_INITSTORAGE] = 'CB_INITSTORAGE'
MessageText[CB_MULTIPLEADDSTRING] = 'CB_MULTIPLEADDSTRING'
MessageText[CB_GETCOMBOBOXINFO] = 'CB_GETCOMBOBOXINFO'

MessageText[STM_SETICON] = 'STM_SETICON'
MessageText[STM_GETICON] = 'STM_GETICON'
MessageText[STM_SETIMAGE] = 'STM_SETIMAGE'
MessageText[STM_GETIMAGE] = 'STM_GETIMAGE'

MessageText[LB_ADDSTRING] = 'LB_ADDSTRING'
MessageText[LB_INSERTSTRING] = 'LB_INSERTSTRING'
MessageText[LB_DELETESTRING] = 'LB_DELETESTRING'
MessageText[LB_SELITEMRANGEEX] = 'LB_SELITEMRANGEEX'
MessageText[LB_RESETCONTENT] = 'LB_RESETCONTENT'
MessageText[LB_SETSEL] = 'LB_SETSEL'
MessageText[LB_SETCURSEL] = 'LB_SETCURSEL'
MessageText[LB_GETSEL] = 'LB_GETSEL'
MessageText[LB_GETCURSEL] = 'LB_GETCURSEL'
MessageText[LB_GETTEXT] = 'LB_GETTEXT'
MessageText[LB_GETTEXTLEN] = 'LB_GETTEXTLEN'
MessageText[LB_GETCOUNT] = 'LB_GETCOUNT'
MessageText[LB_SELECTSTRING] = 'LB_SELECTSTRING'
MessageText[LB_DIR] = 'LB_DIR'
MessageText[LB_GETTOPINDEX] = 'LB_GETTOPINDEX'
MessageText[LB_FINDSTRING] = 'LB_FINDSTRING'
MessageText[LB_GETSELCOUNT] = 'LB_GETSELCOUNT'
MessageText[LB_GETSELITEMS] = 'LB_GETSELITEMS'
MessageText[LB_SETTABSTOPS] = 'LB_SETTABSTOPS'
MessageText[LB_GETHORIZONTALEXTENT] = 'LB_GETHORIZONTALEXTENT'
MessageText[LB_SETHORIZONTALEXTENT] = 'LB_SETHORIZONTALEXTENT'
MessageText[LB_SETCOLUMNWIDTH] = 'LB_SETCOLUMNWIDTH'
MessageText[LB_ADDFILE] = 'LB_ADDFILE'
MessageText[LB_SETTOPINDEX] = 'LB_SETTOPINDEX'
MessageText[LB_GETITEMRECT] = 'LB_GETITEMRECT'
MessageText[LB_GETITEMDATA] = 'LB_GETITEMDATA'
MessageText[LB_SETITEMDATA] = 'LB_SETITEMDATA'
MessageText[LB_SELITEMRANGE] = 'LB_SELITEMRANGE'
MessageText[LB_SETANCHORINDEX] = 'LB_SETANCHORINDEX'
MessageText[LB_GETANCHORINDEX] = 'LB_GETANCHORINDEX'
MessageText[LB_SETCARETINDEX] = 'LB_SETCARETINDEX'
MessageText[LB_GETCARETINDEX] = 'LB_GETCARETINDEX'
MessageText[LB_SETITEMHEIGHT] = 'LB_SETITEMHEIGHT'
MessageText[LB_GETITEMHEIGHT] = 'LB_GETITEMHEIGHT'
MessageText[LB_FINDSTRINGEXACT] = 'LB_FINDSTRINGEXACT'
MessageText[LB_SETLOCALE] = 'LB_SETLOCALE'
MessageText[LB_GETLOCALE] = 'LB_GETLOCALE'
MessageText[LB_SETCOUNT] = 'LB_SETCOUNT'
MessageText[LB_INITSTORAGE] = 'LB_INITSTORAGE'
MessageText[LB_ITEMFROMPOINT] = 'LB_ITEMFROMPOINT'
MessageText[LB_MULTIPLEADDSTRING] = 'LB_MULTIPLEADDSTRING'
MessageText[LB_GETLISTBOXINFO] = 'LB_GETLISTBOXINFO'


#
# GetSystemMetrics() codes
#

SM_CXSCREEN                             = 0
SM_CYSCREEN                             = 1
SM_CXVSCROLL                            = 2
SM_CYHSCROLL                            = 3
SM_CYCAPTION                            = 4
SM_CXBORDER                             = 5
SM_CYBORDER                             = 6
SM_CXDLGFRAME                           = 7
SM_CYDLGFRAME                           = 8
SM_CYVTHUMB                             = 9
SM_CXHTHUMB                             = 10
SM_CXICON                               = 11
SM_CYICON                               = 12
SM_CXCURSOR                             = 13
SM_CYCURSOR                             = 14
SM_CYMENU                               = 15
SM_CXFULLSCREEN                         = 16
SM_CYFULLSCREEN                         = 17
SM_CYKANJIWINDOW                        = 18
SM_MOUSEPRESENT                         = 19
SM_CYVSCROLL                            = 20
SM_CXHSCROLL                            = 21
SM_DEBUG                                = 22
SM_SWAPBUTTON                           = 23
SM_RESERVED1                            = 24
SM_RESERVED2                            = 25
SM_RESERVED3                            = 26
SM_RESERVED4                            = 27
SM_CXMIN                                = 28
SM_CYMIN                                = 29
SM_CXSIZE                               = 30
SM_CYSIZE                               = 31
SM_CXFRAME                              = 32
SM_CYFRAME                              = 33
SM_CXMINTRACK                           = 34
SM_CYMINTRACK                           = 35
SM_CXDOUBLECLK                          = 36
SM_CYDOUBLECLK                          = 37
SM_CXICONSPACING                        = 38
SM_CYICONSPACING                        = 39
SM_MENUDROPALIGNMENT                    = 40
SM_PENWINDOWS                           = 41
SM_DBCSENABLED                          = 42
SM_CMOUSEBUTTONS                        = 43


SM_CXFIXEDFRAME                         = SM_CXDLGFRAME  # win40 name change
SM_CYFIXEDFRAME                         = SM_CYDLGFRAME  # win40 name change
SM_CXSIZEFRAME                          = SM_CXFRAME     # win40 name change
SM_CYSIZEFRAME                          = SM_CYFRAME     # win40 name change

SM_SECURE                               = 44
SM_CXEDGE                               = 45
SM_CYEDGE                               = 46
SM_CXMINSPACING                         = 47
SM_CYMINSPACING                         = 48
SM_CXSMICON                             = 49
SM_CYSMICON                             = 50
SM_CYSMCAPTION                          = 51
SM_CXSMSIZE                             = 52
SM_CYSMSIZE                             = 53
SM_CXMENUSIZE                           = 54
SM_CYMENUSIZE                           = 55
SM_ARRANGE                              = 56
SM_CXMINIMIZED                          = 57
SM_CYMINIMIZED                          = 58
SM_CXMAXTRACK                           = 59
SM_CYMAXTRACK                           = 60
SM_CXMAXIMIZED                          = 61
SM_CYMAXIMIZED                          = 62
SM_NETWORK                              = 63
SM_CLEANBOOT                            = 67
SM_CXDRAG                               = 68
SM_CYDRAG                               = 69
SM_SHOWSOUNDS                           = 70
SM_CXMENUCHECK                          = 71   # Use instead of GetMenuCheckMarkDimensions()!
SM_CYMENUCHECK                          = 72
SM_SLOWMACHINE                          = 73
SM_MIDEASTENABLED                       = 74
SM_MOUSEWHEELPRESENT                    = 75
SM_XVIRTUALSCREEN                       = 76
SM_YVIRTUALSCREEN                       = 77
SM_CXVIRTUALSCREEN                      = 78
SM_CYVIRTUALSCREEN                      = 79
SM_CMONITORS                            = 80
SM_SAMEDISPLAYFORMAT                    = 81
SM_IMMENABLED                           = 82
SM_CXFOCUSBORDER                        = 83
SM_CYFOCUSBORDER                        = 84

SM_TABLETPC                             = 86
SM_MEDIACENTER                          = 87
SM_STARTER                              = 88
SM_SERVERR2                             = 89

SM_MOUSEHORIZONTALWHEELPRESENT          = 91
SM_CXPADDEDBORDER                       = 92

SM_DIGITIZER                            = 94
SM_MAXIMUMTOUCHES                       = 95

SM_REMOTESESSION                        = 0x1000

SM_SHUTTINGDOWN                         = 0x2000
SM_REMOTECONTROL                        = 0x2001
SM_CARETBLINKINGENABLED                 = 0x2002


#
# Standard Cursor IDs
#
IDC_ARROW                               = 32512
IDC_IBEAM                               = 32513
IDC_WAIT                                = 32514
IDC_CROSS                               = 32515
IDC_UPARROW                             = 32516
IDC_SIZE                                = 32640     # OBSOLETE: use IDC_SIZEALL
IDC_ICON                                = 32641     # OBSOLETE: use IDC_ARROW
IDC_SIZENWSE                            = 32642
IDC_SIZENESW                            = 32643
IDC_SIZEWE                              = 32644
IDC_SIZENS                              = 32645
IDC_SIZEALL                             = 32646
IDC_NO                                  = 32648     # not in win3.1
IDC_HAND                                = 32649
IDC_APPSTARTING                         = 32650     # not in win3.1
IDC_HELP                                = 32651


#
# Class styles
#
CS_VREDRAW                              = 0x0001
CS_HREDRAW                              = 0x0002
CS_DBLCLKS                              = 0x0008
CS_OWNDC                                = 0x0020
CS_CLASSDC                              = 0x0040
CS_PARENTDC                             = 0x0080
CS_NOCLOSE                              = 0x0200
CS_SAVEBITS                             = 0x0800
CS_BYTEALIGNCLIENT                      = 0x1000
CS_BYTEALIGNWINDOW                      = 0x2000
CS_GLOBALCLASS                          = 0x4000
CS_IME                                  = 0x00010000
CS_DROPSHADOW                           = 0x00020000

#
# WM_SIZE message wParam values
#
SIZE_RESTORED                           = 0
SIZE_MINIMIZED                          = 1
SIZE_MAXIMIZED                          = 2
SIZE_MAXSHOW                            = 3
SIZE_MAXHIDE                            = 4

#
# RedrawWindow() flags
#
RDW_INVALIDATE                          = 0x0001
RDW_INTERNALPAINT                       = 0x0002
RDW_ERASE                               = 0x0004

RDW_VALIDATE                            = 0x0008
RDW_NOINTERNALPAINT                     = 0x0010
RDW_NOERASE                             = 0x0020

RDW_NOCHILDREN                          = 0x0040
RDW_ALLCHILDREN                         = 0x0080

RDW_UPDATENOW                           = 0x0100
RDW_ERASENOW                            = 0x0200

RDW_FRAME                               = 0x0400
RDW_NOFRAME                             = 0x0800

#
# ShowWindow() Commands
#
SW_HIDE                                 = 0
SW_SHOWNORMAL                           = 1
SW_NORMAL                               = 1
SW_SHOWMINIMIZED                        = 2
SW_SHOWMAXIMIZED                        = 3
SW_MAXIMIZE                             = 3
SW_SHOWNOACTIVATE                       = 4
SW_SHOW                                 = 5
SW_MINIMIZE                             = 6
SW_SHOWMINNOACTIVE                      = 7
SW_SHOWNA                               = 8
SW_RESTORE                              = 9
SW_SHOWDEFAULT                          = 10
SW_FORCEMINIMIZE                        = 11
SW_MAX                                  = 11



#
# Virtual Keys, Standard Set
#
VK_LBUTTON                              = 0x01
VK_RBUTTON                              = 0x02
VK_CANCEL                               = 0x03
VK_MBUTTON                              = 0x04    # NOT contiguous with L & RBUTTON

VK_XBUTTON1                             = 0x05    # NOT contiguous with L & RBUTTON
VK_XBUTTON2                             = 0x06    # NOT contiguous with L & RBUTTON

#
# 0x07 : unassigned
#

VK_BACK                                 = 0x08
VK_TAB                                  = 0x09

#
# 0x0A - 0x0B : reserved
#

VK_CLEAR                                = 0x0C
VK_RETURN                               = 0x0D

VK_SHIFT                                = 0x10
VK_CONTROL                              = 0x11
VK_MENU                                 = 0x12
VK_PAUSE                                = 0x13
VK_CAPITAL                              = 0x14

VK_KANA                                 = 0x15
VK_HANGEUL                              = 0x15  # old name - should be here for compatibility
VK_HANGUL                               = 0x15
VK_JUNJA                                = 0x17
VK_FINAL                                = 0x18
VK_HANJA                                = 0x19
VK_KANJI                                = 0x19

VK_ESCAPE                               = 0x1B

VK_CONVERT                              = 0x1C
VK_NONCONVERT                           = 0x1D
VK_ACCEPT                               = 0x1E
VK_MODECHANGE                           = 0x1F

VK_SPACE                                = 0x20
VK_PRIOR                                = 0x21
VK_NEXT                                 = 0x22
VK_END                                  = 0x23
VK_HOME                                 = 0x24
VK_LEFT                                 = 0x25
VK_UP                                   = 0x26
VK_RIGHT                                = 0x27
VK_DOWN                                 = 0x28
VK_SELECT                               = 0x29
VK_PRINT                                = 0x2A
VK_EXECUTE                              = 0x2B
VK_SNAPSHOT                             = 0x2C
VK_INSERT                               = 0x2D
VK_DELETE                               = 0x2E
VK_HELP                                 = 0x2F

#
# VK_0 - VK_9 are the same as ASCII '0' - '9' (0x30 - 0x39)
# 0x40 : unassigned
# VK_A - VK_Z are the same as ASCII 'A' - 'Z' (0x41 - 0x5A)
#

VK_LWIN                                 = 0x5B
VK_RWIN                                 = 0x5C
VK_APPS                                 = 0x5D

#
# 0x5E : reserved
#

VK_SLEEP                                = 0x5F

VK_NUMPAD0                              = 0x60
VK_NUMPAD1                              = 0x61
VK_NUMPAD2                              = 0x62
VK_NUMPAD3                              = 0x63
VK_NUMPAD4                              = 0x64
VK_NUMPAD5                              = 0x65
VK_NUMPAD6                              = 0x66
VK_NUMPAD7                              = 0x67
VK_NUMPAD8                              = 0x68
VK_NUMPAD9                              = 0x69
VK_MULTIPLY                             = 0x6A
VK_ADD                                  = 0x6B
VK_SEPARATOR                            = 0x6C
VK_SUBTRACT                             = 0x6D
VK_DECIMAL                              = 0x6E
VK_DIVIDE                               = 0x6F
VK_F1                                   = 0x70
VK_F2                                   = 0x71
VK_F3                                   = 0x72
VK_F4                                   = 0x73
VK_F5                                   = 0x74
VK_F6                                   = 0x75
VK_F7                                   = 0x76
VK_F8                                   = 0x77
VK_F9                                   = 0x78
VK_F10                                  = 0x79
VK_F11                                  = 0x7A
VK_F12                                  = 0x7B
VK_F13                                  = 0x7C
VK_F14                                  = 0x7D
VK_F15                                  = 0x7E
VK_F16                                  = 0x7F
VK_F17                                  = 0x80
VK_F18                                  = 0x81
VK_F19                                  = 0x82
VK_F20                                  = 0x83
VK_F21                                  = 0x84
VK_F22                                  = 0x85
VK_F23                                  = 0x86
VK_F24                                  = 0x87

#
# 0x88 - 0x8F : unassigned
#

VK_NUMLOCK                              = 0x90
VK_SCROLL                               = 0x91

#
# NEC PC-9800 kbd definitions
#
VK_OEM_NEC_EQUAL                        = 0x92   # '=' key on numpad

#
# Fujitsu/OASYS kbd definitions
#
VK_OEM_FJ_JISHO                         = 0x92   # 'Dictionary' key
VK_OEM_FJ_MASSHOU                       = 0x93   # 'Unregister word' key
VK_OEM_FJ_TOUROKU                       = 0x94   # 'Register word' key
VK_OEM_FJ_LOYA                          = 0x95   # 'Left OYAYUBI' key
VK_OEM_FJ_ROYA                          = 0x96   # 'Right OYAYUBI' key

#
# 0x97 - 0x9F : unassigned
#

#
# VK_L* & VK_R* - left and right Alt, Ctrl and Shift virtual keys.
# Used only as parameters to GetAsyncKeyState() and GetKeyState().
# No other API or message will distinguish left and right keys in this way.
#
VK_LSHIFT                               = 0xA0
VK_RSHIFT                               = 0xA1
VK_LCONTROL                             = 0xA2
VK_RCONTROL                             = 0xA3
VK_LMENU                                = 0xA4
VK_RMENU                                = 0xA5

VK_BROWSER_BACK                         = 0xA6
VK_BROWSER_FORWARD                      = 0xA7
VK_BROWSER_REFRESH                      = 0xA8
VK_BROWSER_STOP                         = 0xA9
VK_BROWSER_SEARCH                       = 0xAA
VK_BROWSER_FAVORITES                    = 0xAB
VK_BROWSER_HOME                         = 0xAC

VK_VOLUME_MUTE                          = 0xAD
VK_VOLUME_DOWN                          = 0xAE
VK_VOLUME_UP                            = 0xAF
VK_MEDIA_NEXT_TRACK                     = 0xB0
VK_MEDIA_PREV_TRACK                     = 0xB1
VK_MEDIA_STOP                           = 0xB2
VK_MEDIA_PLAY_PAUSE                     = 0xB3
VK_LAUNCH_MAIL                          = 0xB4
VK_LAUNCH_MEDIA_SELECT                  = 0xB5
VK_LAUNCH_APP1                          = 0xB6
VK_LAUNCH_APP2                          = 0xB7


#
# 0xB8 - 0xB9 : reserved
#

VK_OEM_1                                = 0xBA   # ';:' for US
VK_OEM_PLUS                             = 0xBB   # '+' any country
VK_OEM_COMMA                            = 0xBC   # ',' any country
VK_OEM_MINUS                            = 0xBD   # '-' any country
VK_OEM_PERIOD                           = 0xBE   # '.' any country
VK_OEM_2                                = 0xBF   # '/?' for US
VK_OEM_3                                = 0xC0   # '`~' for US

#
# 0xC1 - 0xD7 : reserved
#

#
# 0xD8 - 0xDA : unassigned
#

VK_OEM_4                                = 0xDB  #  '[{' for US
VK_OEM_5                                = 0xDC  #  '\|' for US
VK_OEM_6                                = 0xDD  #  ']}' for US
VK_OEM_7                                = 0xDE  #  ''"' for US
VK_OEM_8                                = 0xDF

#
# 0xE0 : reserved
#

#
# Various extended or enhanced keyboards
#
VK_OEM_AX                               = 0xE1  #  'AX' key on Japanese AX kbd
VK_OEM_102                              = 0xE2  #  "<>" or "\|" on RT 102-key kbd.
VK_ICO_HELP                             = 0xE3  #  Help key on ICO
VK_ICO_00                               = 0xE4  #  00 key on ICO

VK_PROCESSKEY                           = 0xE5

VK_ICO_CLEAR                            = 0xE6


VK_PACKET                               = 0xE7

#
# 0xE8 : unassigned
#

#
# Nokia/Ericsson definitions
#
VK_OEM_RESET                            = 0xE9
VK_OEM_JUMP                             = 0xEA
VK_OEM_PA1                              = 0xEB
VK_OEM_PA2                              = 0xEC
VK_OEM_PA3                              = 0xED
VK_OEM_WSCTRL                           = 0xEE
VK_OEM_CUSEL                            = 0xEF
VK_OEM_ATTN                             = 0xF0
VK_OEM_FINISH                           = 0xF1
VK_OEM_COPY                             = 0xF2
VK_OEM_AUTO                             = 0xF3
VK_OEM_ENLW                             = 0xF4
VK_OEM_BACKTAB                          = 0xF5

VK_ATTN                                 = 0xF6
VK_CRSEL                                = 0xF7
VK_EXSEL                                = 0xF8
VK_EREOF                                = 0xF9
VK_PLAY                                 = 0xFA
VK_ZOOM                                 = 0xFB
VK_NONAME                               = 0xFC
VK_PA1                                  = 0xFD
VK_OEM_CLEAR                            = 0xFE

#
# 0xFF : reserved
#


def __BOOL(v):
    return bool(BOOL(v).value)

def GetKeyState(vk):
    r = windll.user32.GetKeyState(vk)
    return SHORT(r).value

def GetClientRect(hwnd, rect):
    if not isinstance(hwnd, (HWND, int)):
        hwnd = int(hwnd)

    return __BOOL(windll.user32.GetClientRect(hwnd, rect))

def ClientToScreen(hwnd, pt):
    if isinstance(pt, PPOINT):
        return __BOOL(windll.user32.ClientToScreen(HWND(hwnd), pt))

    if isinstance(pt, PRECT):
        leftTop = POINT()
        rightBottom = POINT()

        client = pt.contents

        leftTop.x, leftTop.y = client.left, client.top
        rightBottom.x, rightBottom.y = client.right, client.bottom

        if not (ClientToScreen(hwnd, PPOINT(leftTop)) and ClientToScreen(hwnd, PPOINT(rightBottom))):
            return False

        client.left, client.top = leftTop.x, leftTop.y
        client.right, client.bottom = rightBottom.x, rightBottom.y

        return True

    raise

def GetSystemMetrics(index):
    return INT(windll.user32.GetSystemMetrics(index)).value

def DefWindowProcW(hwnd, message, wParam, lParam):
    return LONG_PTR(windll.user32.DefWindowProcW(HWND(hwnd), UINT(message), WPARAM(wParam), LPARAM(lParam))).value

def ReleaseCapture():
    return __BOOL(windll.user32.ReleaseCapture())

def SendMessageW(hwnd, message, wParam, lParam):
    return LONG_PTR(windll.user32.SendMessageW(HWND(hwnd), UINT(message), WPARAM(wParam), LPARAM(lParam))).value

def ShowWindow(hwnd, cmd):
    return bool(windll.user32.ShowWindow(HWND(hwnd), INT(cmd)))

def SetWindowLongW(hwnd, index, value):
    return LONG_PTR(windll.user32.SetWindowLongW(HWND(hwnd), INT(index), LONG_PTR(value))).value

def SetWindowPos(hWnd, hWndInsertAfter, X, Y, cx, cy, Flags):
    return __BOOL(windll.user32.SetWindowPos(HWND(hWnd), HWND(hWndInsertAfter), INT(X), INT(Y), INT(cx), INT(cy), UINT(Flags)))

def SetParent(child, parent):
    return HWND(windll.user32.SetParent(HWND(child), HWND(parent))).value

def GetWindowRect(hWnd, rect):
    return __BOOL(windll.user32.GetWindowRect(HWND(hWnd), PRECT(rect)))

def LoadCursorW(hInstance, cursorName):
    if isinstance(cursorName, str):
        cursorName = PWSTR(cursorName)

    elif isinstance(cursorName, int):
        cursorName = ULONG_PTR(cursorName)

    return HCURSOR(windll.user32.LoadCursorW(hInstance, cursorName)).value
