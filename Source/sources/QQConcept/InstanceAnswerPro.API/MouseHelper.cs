using System;
using System.Runtime.InteropServices;
using System.Windows;
using System.Windows.Media;

namespace InstanceAnswerPro.API
{
    public class MouseHelper
    {
        // Methods
        public static Point GetCursorPos()
        {
            Win32Point pt = new Win32Point();
            GetCursorPos(ref pt);
            return new Point((double)pt.X, (double)pt.Y);
        }

        [DllImport("user32.dll")]
        private static extern bool GetCursorPos(ref Win32Point pt);
        public static Point GetCursorPos(Visual relativeTo)
        {
            Win32Point pt = new Win32Point();
            GetCursorPos(ref pt);
            return relativeTo.PointFromScreen(new Point((double)pt.X, (double)pt.Y));
        }

        [DllImport("user32.dll")]
        private static extern bool ScreenToClient(IntPtr hwnd, ref Win32Point pt);

        // Nested Types
        [StructLayout(LayoutKind.Sequential)]
        private struct Win32Point
        {
            public int X;
            public int Y;
        }
    }


}
