from .QCommon import *
from WinTypes import *

class QBorderlessWindow(QObject):
    def __init__(self, childWindow, title = '', hWndParent = 0):
        super().__init__()

        self.childWindow = childWindow

        self.windowProc = WNDPROC(self.WindowProc)
        self.className  = PWSTR('QBorderlessWindow_Wrapper')
        self.windowName = PWSTR(title)

        wndcls = WNDCLASSEXW()

        wndcls.cbSize = len(wndcls)
        wndcls.style = CS_HREDRAW | CS_VREDRAW
        wndcls.hInstance = 0
        wndcls.lpfnWndProc = self.windowProc
        wndcls.lpszClassName = self.className
        wndcls.hbrBackground = windll.gdi32.CreateSolidBrush(0x00FFFFFF)
        wndcls.hCursor = LoadCursorW(0, IDC_ARROW)

        ret = windll.user32.RegisterClassExW(PWNDCLASSEXW(wndcls))
        if ret == 0:
            raise Exception('RegisterClassExW failed')

        desktop = QApplication.desktop()
        workAreaRect = desktop.availableGeometry()

        windowRect = QRect(0, 0, workAreaRect.width() * 0.75, workAreaRect.height() * 0.75)
        windowRect.moveCenter(workAreaRect.center())

        self.hwnd = windll.user32.CreateWindowExW(
                        0,
                        self.className,
                        self.windowName,
                        WS_CAPTION | WS_MINIMIZEBOX | WS_MAXIMIZEBOX | WS_SYSMENU | WS_VISIBLE,
                        windowRect.left(),
                        windowRect.top(),
                        windowRect.width(),
                        windowRect.height(),
                        hWndParent,
                        0,
                        windll.kernel32.GetModuleHandleW(0),
                        0
                    )

        if self.hwnd == 0:
            raise Exception('CreateWindowExW failed')

        winId = int(self.childWindow.winId())

        SetWindowLongW(winId, GWL_STYLE, WS_CHILD | WS_CLIPCHILDREN | WS_CLIPSIBLINGS)
        SetParent(winId, self.hwnd)

        e = QEvent(QEvent.EmbeddingControl)
        QApplication.sendEvent(self.childWindow, e)

        self.childWindow.setFocus(Qt.MouseFocusReason)

        self.childWindow.show()
        self.setupWindowFrame()

    def setupWindowFrame(self):
        self.show()

        self.setupBorderless()

        client = RECT()

        leftTop = POINT()
        rightBottom = POINT()

        GetClientRect(self.hwnd, PRECT(client))
        ClientToScreen(self.hwnd, PRECT(client))

        rc = QRect(client.left, client.top, client.right - client.left, client.bottom - client.top)
        SetWindowPos(self.hwnd, 0, rc.left(), rc.top(), rc.width(), rc.height(), SWP_FRAMECHANGED | SWP_NOMOVE)

    def setupBorderless(self):
        SetWindowLongW(self.hwnd, GWL_STYLE, WS_POPUP | WS_CAPTION | WS_THICKFRAME | WS_MAXIMIZEBOX | WS_MINIMIZEBOX)

        margins = MARGINS(1, 1, 1, 1)
        windll.dwmapi.DwmExtendFrameIntoClientArea(self.hwnd, PMARGINS(margins))

    def show(self):
        ShowWindow(self.hwnd, SW_SHOW)

    def hide(self):
        ShowWindow(self.hwnd, SW_HIDE)

    def close(self):
        qApp.quit()

    def mousePressEvent(self, event):
        print('mousePressEvent')
        ReleaseCapture()
        SendMessageW(self.hwnd, WM_NCLBUTTONDOWN, HTCAPTION, 0)

    def handleNcHitText(self, hwnd, x, y):
        borderWidth = 8

        rc = RECT()
        GetWindowRect(hwnd, rc)

        touchLeft   = rc.left <= x <= rc.left + borderWidth
        touchTop    = rc.top <= y <= rc.top + borderWidth
        touchRight  = rc.right - borderWidth <= x <= rc.right
        touchBottom = rc.bottom - borderWidth <= y <= rc.bottom

        # top left corner
        if touchTop and touchLeft:
            return HTTOPLEFT

        # bottom left corner
        if touchBottom and touchLeft:
            return HTBOTTOMLEFT

        # bottom right corner
        if touchBottom and touchRight:
            return HTBOTTOMRIGHT

        # top right corner
        if touchTop and touchRight:
            return HTTOPRIGHT

        # left border
        if touchLeft:
            return HTLEFT

        # right border
        if touchRight:
            return HTRIGHT

        # bottom border
        if touchBottom:
            return HTBOTTOM

        # top border
        if touchTop:
            return HTTOP

        return HTCAPTION

    def WindowProc(self, hwnd, message, wParam, lParam):
        if message == WM_CLOSE:
            qApp.quit()

        elif message == WM_NCCALCSIZE:
            return 0

        elif message == WM_NCHITTEST:
            return self.handleNcHitText(hwnd, lParam & 0xFFFF, (lParam >> 16))

        elif message == WM_SIZE:
            client = RECT()
            GetClientRect(hwnd, PRECT(client))

            cxframe   = GetSystemMetrics(SM_CXFRAME)
            cyframe   = GetSystemMetrics(SM_CYFRAME)
            cycaption = GetSystemMetrics(SM_CYCAPTION)

            rc = QRect(cxframe, cyframe + cycaption, client.right - client.left, client.bottom - client.top)
            if wParam not in [SIZE_MINIMIZED]:
                self.childWindow.setGeometry(rc)

        elif message == WM_SETFOCUS:
            self.childWindow.setFocus()

            # print('%08X, %s' % (hwnd, MessageText[message]))
            # reason = Qt.FocusReason()

            # if GetKeyState(VK_LBUTTON) < 0 or GetKeyState(VK_RBUTTON) < 0:
            #     reason = Qt.MouseFocusReason

            # elif GetKeyState(VK_SHIFT) < 0:
            #     reason = Qt.BacktabFocusReason

            # else:
            #     reason = Qt.TabFocusReason

            # self.childWindow.setFocus(reason)

        elif message == WM_ACTIVATE:
            return 0

        # if message < len(MessageText): print(MessageText[message])

        return DefWindowProcW(hwnd, message, wParam, lParam)
