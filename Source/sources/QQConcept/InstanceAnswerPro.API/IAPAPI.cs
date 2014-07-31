using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Runtime.InteropServices;
using System.Windows;

namespace InstanceAnswerPro.API
{
    public static class WinAPI
    {
        // Fields
        public const int GWL_STYLE = -16;
        public const int WM_COPYDATA = 0x4a;
        public const int WM_DWMCOMPOSITIONCHANGED = 0x31e;
        public const int WM_GETMINMAXINFO = 0x24;
        public const int WM_NCHITTEST = 0x84;
        public const int WM_SETHEAD = 0xbd0;
        public const int WM_SETREDRAW = 11;
        public const int WM_SYSCOMMAND = 0x112;
        private const int WM_USER = 0x400;
        public const int WM_USER_LOADER_NOTIFY = 0xc28;
        public const int WM_USER_LOGIN_WINDOW_LOADED = 0x500;
        public const int WS_MAXIMIZEBOX = 0x10000;
        public const int WS_THICKFRAME = 0x40000;

        // Methods
        [return: MarshalAs(UnmanagedType.Bool)]
        [DllImport("user32.dll")]
        public static extern bool FlashWindowEx(ref FLASHWINFO pwfi);
        [DllImport("Kernel32", CharSet = CharSet.Unicode, SetLastError = true)]
        public static extern IntPtr FreeLibrary(IntPtr handle);
        public static Delegate GetFunctionAddress(IntPtr dllModule, string functionName, Type t)
        {
            IntPtr procAddress = GetProcAddress(dllModule, functionName);
            Marshal.GetLastWin32Error();
            if (procAddress == IntPtr.Zero)
            {
                return null;
            }
            return Marshal.GetDelegateForFunctionPointer(procAddress, t);
        }

        [DllImport("user32.dll")]
        public static extern bool GetIconInfo(IntPtr hIcon, out ICONINFO piconinfo);
        [DllImport("user32")]
        public static extern bool GetMonitorInfo(IntPtr hMonitor, MONITORINFO lpmi);
        [DllImport("kernel32.dll", CharSet = CharSet.Ansi, SetLastError = true)]
        public static extern IntPtr GetProcAddress(IntPtr hModule, string procName);
        [DllImport("user32.dll")]
        public static extern int GetWindowLong(IntPtr hwnd, int nIndex);
        public static bool IsRightHanded()
        {
            bool lpvParam = true;
            if (SystemParametersInfo(0x1b, 0, ref lpvParam, 0) != 0)
            {
                return lpvParam;
            }
            return true;
        }

        [DllImport("kernel32", CharSet = CharSet.Unicode, SetLastError = true)]
        public static extern IntPtr LoadLibraryW(string lpFileName);
        [DllImport("User32")]
        public static extern IntPtr MonitorFromWindow(IntPtr handle, int flags);
        [return: MarshalAs(UnmanagedType.Bool)]
        [DllImport("user32.dll", SetLastError = true)]
        public static extern bool PostMessage(IntPtr hWnd, uint Msg, IntPtr wParam, IntPtr lParam);
        [DllImport("user32.dll", CharSet = CharSet.Auto, SetLastError = true)]
        public static extern IntPtr SendMessage(IntPtr hWnd, int Msg, IntPtr wParam, IntPtr lParam);
        [return: MarshalAs(UnmanagedType.Bool)]
        [DllImport("user32.dll")]
        public static extern bool SetForegroundWindow(IntPtr hWnd);
        [DllImport("kernel32.dll")]
        public static extern int SetProcessWorkingSetSize(int hProcess, int dwMinimumWorkingSetSize, int dwMaximumWorkingSetSize);
        [DllImport("user32.dll")]
        public static extern int SetWindowLong(IntPtr hMenu, int nIndex, int dwNewLong);
        [DllImport("shell32.dll", CharSet = CharSet.Auto)]
        public static extern IntPtr SHGetFileInfo(string pszPath, uint dwFileAttributes, ref SHFILEINFO psfi, uint cbFileInfo, uint uFlags);
        public static int SignedHIWORD(IntPtr intPtr)
        {
            return (short)((intPtr.ToInt32() >> 0x10) & 0xffff);
        }

        public static int SignedLOWORD(IntPtr intPtr)
        {
            return (short)(intPtr.ToInt32() & 0xffff);
        }

        [DllImport("user32.dll", CharSet = CharSet.Auto, SetLastError = true)]
        public static extern int SystemParametersInfo(int uAction, int uParam, ref bool lpvParam, int fuWinIni);

        // Nested Types
        public delegate IntPtr DllRegisterServer();

        [StructLayout(LayoutKind.Sequential)]
        public struct FLASHWINFO
        {
            public uint cbSize;
            public IntPtr hwnd;
            public uint dwFlags;
            public uint uCount;
            public uint dwTimeout;
        }

        public enum HitTestResult
        {
            HTBORDER = 0x12,
            HTBOTTOM = 15,
            HTBOTTOMLEFT = 0x10,
            HTBOTTOMRIGHT = 0x11,
            HTCAPTION = 2,
            HTCLIENT = 1,
            HTCLOSE = 20,
            HTERROR = -2,
            HTGROWBOX = 4,
            HTHELP = 0x15,
            HTHSCROLL = 6,
            HTLEFT = 10,
            HTMAXBUTTON = 9,
            HTMENU = 5,
            HTMINBUTTON = 8,
            HTNOWHERE = 0,
            HTOBJECT = 0x13,
            HTREDUCE = 8,
            HTRIGHT = 11,
            HTSIZE = 4,
            HTSIZEFIRST = 10,
            HTSIZELAST = 0x11,
            HTSYSMENU = 3,
            HTTOP = 12,
            HTTOPLEFT = 13,
            HTTOPRIGHT = 14,
            HTTRANSPARENT = -1,
            HTVSCROLL = 7,
            HTZOOM = 9
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct ICONINFO
        {
            public bool fIcon;
            public int xHotspot;
            public int yHotspot;
            public IntPtr hbmMask;
            public IntPtr hbmColor;
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct MINMAXINFO
        {
            public WinAPI.POINT ptReserved;
            public WinAPI.POINT ptMaxSize;
            public WinAPI.POINT ptMaxPosition;
            public WinAPI.POINT ptMinTrackSize;
            public WinAPI.POINT ptMaxTrackSize;
        }

        [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Auto)]
        public class MONITORINFO
        {
            public int cbSize = Marshal.SizeOf(typeof(WinAPI.MONITORINFO));
            public WinAPI.RECT rcMonitor;
            public WinAPI.RECT rcWork;
            public int dwFlags;
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct POINT
        {
            public int x;
            public int y;
            public POINT(int x, int y)
            {
                this.x = x;
                this.y = y;
            }
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct RECT
        {
            public int left;
            public int top;
            public int right;
            public int bottom;
            public static readonly WinAPI.RECT Empty;
            public int Width
            {
                get
                {
                    return Math.Abs((int)(this.right - this.left));
                }
            }
            public int Height
            {
                get
                {
                    return (this.bottom - this.top);
                }
            }
            public RECT(int left, int top, int right, int bottom)
            {
                this.left = left;
                this.top = top;
                this.right = right;
                this.bottom = bottom;
            }

            public RECT(WinAPI.RECT rcSrc)
            {
                this.left = rcSrc.left;
                this.top = rcSrc.top;
                this.right = rcSrc.right;
                this.bottom = rcSrc.bottom;
            }

            public bool IsEmpty
            {
                get
                {
                    if (this.left < this.right)
                    {
                        return (this.top >= this.bottom);
                    }
                    return true;
                }
            }
            public override string ToString()
            {
                if (this == Empty)
                {
                    return "RECT {Empty}";
                }
                return string.Concat(new object[] { "RECT { left : ", this.left, " / top : ", this.top, " / right : ", this.right, " / bottom : ", this.bottom, " }" });
            }

            public override bool Equals(object obj)
            {
                return ((obj is Rect) && (this == ((WinAPI.RECT)obj)));
            }

            public override int GetHashCode()
            {
                return (((this.left.GetHashCode() + this.top.GetHashCode()) + this.right.GetHashCode()) + this.bottom.GetHashCode());
            }

            public static bool operator ==(WinAPI.RECT rect1, WinAPI.RECT rect2)
            {
                return ((((rect1.left == rect2.left) && (rect1.top == rect2.top)) && (rect1.right == rect2.right)) && (rect1.bottom == rect2.bottom));
            }

            public static bool operator !=(WinAPI.RECT rect1, WinAPI.RECT rect2)
            {
                return !(rect1 == rect2);
            }
        }

        [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Auto)]
        public struct SHFILEINFO
        {
            public IntPtr hIcon;
            public int iIcon;
            public uint dwAttributes;
            [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 260)]
            public string szDisplayName;
            [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 80)]
            public string szTypeName;
        }

        [Flags]
        public enum SHGFI
        {
            AddOverlays = 0x20,
            Attr_Specified = 0x20000,
            Attributes = 0x800,
            DisplayName = 0x200,
            ExeType = 0x2000,
            Icon = 0x100,
            IconLocation = 0x1000,
            LargeIcon = 0,
            LinkOverlay = 0x8000,
            OpenIcon = 2,
            OverlayIndex = 0x40,
            PIDL = 8,
            Selected = 0x10000,
            ShellIconSize = 4,
            SmallIcon = 1,
            SysIconIndex = 0x4000,
            TypeName = 0x400,
            UseFileAttributes = 0x10
        }
    }


}
