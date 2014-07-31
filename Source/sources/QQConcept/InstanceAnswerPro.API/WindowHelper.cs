using System;
using System.Runtime.InteropServices;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Input;
using System.Windows.Interop;
using System.Windows.Media;
using InstanceAnswerPro.API;

namespace InstanceAnswerPro.API
{
    public class WindowHelper : DependencyObject
    {
        // Fields
        private static Window bamaMainFrame = null;
        private Border border;
        private CaptionHelper captionHelper = new CaptionHelper();
        private Window curwin;
        public static readonly DependencyProperty HandleHitTestMessageProperty = DependencyProperty.Register("HandleHitTestMessage", typeof(bool), typeof(WindowHelper), new UIPropertyMetadata(true));
        private bool initBorder;
        private Grid layoutRoot;
        private HwndSource source;

        // Methods
        private WindowHelper(Window win, string includeName, params string[] exIncludesName)
        {
            this.captionHelper.SetInfo(includeName, exIncludesName);
            this.CaptionHeight = 0x1a;
            this.curwin = win;
            this.curwin.Loaded += new RoutedEventHandler(this.CustomWindow_Loaded);
            this.curwin.Unloaded += new RoutedEventHandler(this.curwin_Unloaded);
            this.curwin.Closed += new EventHandler(this.curwin_Closed);
            this.curwin.StateChanged += new EventHandler(this.curwin_StateChanged);
        }

        public static void BindingTopmost(Window win)
        {
            Binding binding = new Binding("Topmost")
            {
                Source = MainFrame,
                Mode = BindingMode.OneWay
            };
            win.SetBinding(Window.TopmostProperty, binding);
        }

        public static WindowHelper CreateForBuddyZoneWindow(Window win)
        {
            return new WindowHelper(win, null, null) { HandleHitTestMessage = false };
        }

        private void curwin_Closed(object sender, EventArgs e)
        {
            if (this.curwin == sender)
            {
                this.Dispose();
            }
        }

        private void curwin_SizeChanged(object sender, SizeChangedEventArgs e)
        {
            this.captionHelper.OnSizeChanged();
        }

        private void curwin_StateChanged(object sender, EventArgs e)
        {
            if (this.curwin == sender)
            {
                if (this.curwin.WindowState == WindowState.Maximized)
                {
                    if (!this.initBorder)
                    {
                        this.initBorder = true;
                        Grid content = this.curwin.Content as Grid;
                        if (content != null)
                        {
                            this.border = new Border();
                            this.border.BorderBrush = Brushes.Black;
                            this.border.BorderThickness = new Thickness(3.0);
                            content.Children.Insert(0, this.border);
                        }
                    }
                    if (this.border != null)
                    {
                        this.border.Visibility = Visibility.Visible;
                    }
                }
                else if (this.border != null)
                {
                    this.border.Visibility = Visibility.Hidden;
                }
            }
        }

        private void curwin_Unloaded(object sender, RoutedEventArgs e)
        {
            if (this.curwin == sender)
            {
                this.curwin.SizeChanged -= new SizeChangedEventHandler(this.curwin_SizeChanged);
                this.curwin.Unloaded -= new RoutedEventHandler(this.curwin_Unloaded);
                this.captionHelper.OnUnloaded();
                this.Dispose();
            }
        }

        private void CustomWindow_Loaded(object sender, RoutedEventArgs e)
        {
            this.curwin.Loaded -= new RoutedEventHandler(this.CustomWindow_Loaded);
            this.layoutRoot = this.curwin.FindName("LayoutRoot") as Grid;
            this.curwin.SizeChanged += new SizeChangedEventHandler(this.curwin_SizeChanged);
            Grid content = this.curwin.Content as Grid;
            IntPtr handle = new WindowInteropHelper(this.curwin).Handle;
            this.source = HwndSource.FromHwnd(handle);
            if (this.source != null)
            {
                this.source.AddHook(new HwndSourceHook(this.WindowProc));
            }
            this.captionHelper.OnLoaded(this.curwin);
        }

        private void Dispose()
        {
            this.border = null;
            if (this.source != null)
            {
                this.source.Dispose();
                this.source = null;
            }
            this.curwin.StateChanged -= new EventHandler(this.curwin_StateChanged);
            this.curwin.Closed -= new EventHandler(this.curwin_Closed);
            this.curwin = null;
            this.layoutRoot = null;
        }

        public static Window GetMainFrame()
        {
            return bamaMainFrame;
        }

        private void GetMinMaxInfo(IntPtr hwnd, IntPtr lParam)
        {
            WinAPI.MINMAXINFO structure = (WinAPI.MINMAXINFO)Marshal.PtrToStructure(lParam, typeof(WinAPI.MINMAXINFO));
            int flags = 2;
            IntPtr hMonitor = WinAPI.MonitorFromWindow(hwnd, flags);
            if (hMonitor != IntPtr.Zero)
            {
                WinAPI.MONITORINFO lpmi = new WinAPI.MONITORINFO();
                WinAPI.GetMonitorInfo(hMonitor, lpmi);
                WinAPI.RECT rcWork = lpmi.rcWork;
                WinAPI.RECT rcMonitor = lpmi.rcMonitor;
                structure.ptMaxPosition.x = Math.Abs((int)(rcWork.left - rcMonitor.left));
                structure.ptMaxPosition.y = Math.Abs((int)(rcWork.top - rcMonitor.top));
                structure.ptMaxSize.x = Math.Abs((int)(rcWork.right - rcWork.left));
                structure.ptMaxSize.y = Math.Abs((int)(rcWork.bottom - rcWork.top));
                structure.ptMinTrackSize.x = (int)this.curwin.MinWidth;
                structure.ptMinTrackSize.y = (int)this.curwin.MinHeight;
            }
            Marshal.StructureToPtr(structure, lParam, true);
        }

        public static WindowHelper Hook(Window win, string includeName, params string[] exIncludesName)
        {
            return new WindowHelper(win, includeName, exIncludesName);
        }

        public static void ModifyMainPanelWindowStyle(IntPtr hwnd)
        {
            int dwNewLong = WinAPI.GetWindowLong(hwnd, -16) & -65537;
            dwNewLong |= 0x40000;
            WinAPI.SetWindowLong(hwnd, -16, dwNewLong);
        }

        private bool MouseInToolBar(MouseButtonEventArgs e)
        {
            bool flag = false;
            Point visualTopLeft = VisualTree.GetVisualTopLeft(this.curwin, this.curwin);
            if ((MouseHelper.GetCursorPos().Y - visualTopLeft.Y) <= 70.0)
            {
                flag = true;
            }
            return flag;
        }

        public static void SetMainFrame(Window win)
        {
            bamaMainFrame = win;
            Application.Current.MainWindow = win;
        }

        private IntPtr WindowProc(IntPtr hwnd, int msg, IntPtr wParam, IntPtr lParam, ref bool handled)
        {
            switch (msg)
            {
                case 0x24:
                    this.GetMinMaxInfo(hwnd, lParam);
                    handled = true;
                    break;

                case 0x84:
                    if (this.HandleHitTestMessage)
                    {
                        IntPtr zero = IntPtr.Zero;
                        handled = this.WmNcHitTest(lParam, ref zero);
                        return zero;
                    }
                    break;
            }
            return IntPtr.Zero;
        }

        private bool WmNcHitTest(IntPtr lParam, ref IntPtr result)
        {
            int num = WinAPI.SignedLOWORD(lParam);
            int num2 = WinAPI.SignedHIWORD(lParam);
            Point visualTopLeft = VisualTree.GetVisualTopLeft(this.layoutRoot, this.curwin);
            double x = visualTopLeft.X;
            double y = visualTopLeft.Y;
            double num5 = x + this.layoutRoot.ActualWidth;
            double num6 = visualTopLeft.Y + this.layoutRoot.ActualHeight;
            double num7 = 4.0;
            bool flag = ((num - x) <= num7) && ((num - x) >= 0.0);
            bool flag2 = ((num5 - num) <= num7) && ((num5 - num) >= 0.0);
            bool flag3 = ((num2 - y) <= num7) && ((num2 - y) >= 0.0);
            bool flag4 = ((num6 - num2) <= num7) && ((num6 - num2) >= 0.0);
            if ((flag || flag2) || (flag3 || flag4))
            {
                if (flag && flag3)
                {
                    result = (IntPtr)13L;
                }
                else if (flag && flag4)
                {
                    result = (IntPtr)0x10L;
                }
                else if (flag2 && flag3)
                {
                    result = (IntPtr)14L;
                }
                else if (flag2 && flag4)
                {
                    result = (IntPtr)0x11L;
                }
                else if (flag)
                {
                    result = (IntPtr)10L;
                }
                else if (flag2)
                {
                    result = (IntPtr)11L;
                }
                else if (flag3)
                {
                    result = (IntPtr)12L;
                }
                else if (flag4)
                {
                    result = (IntPtr)15L;
                }
                return true;
            }
            bool flag5 = false;
            if (this.captionHelper.CanCaption)
            {
                flag5 = this.captionHelper.IsInCaption(this.curwin, this.curwin.PointFromScreen(new Point((double)num, (double)num2)));
            }
            else
            {
                flag5 = (((num > (x + 62.0)) && (num < (num5 - 70.0))) && (num2 > (y + 1.0))) && (num2 < (y + this.CaptionHeight));
            }
            if (flag5)
            {
                result = (IntPtr)2L;
                return true;
            }
            return false;
        }

        // Properties
        public int CaptionHeight { get; set; }

        public bool HandleHitTestMessage
        {
            get
            {
                return (bool)base.GetValue(HandleHitTestMessageProperty);
            }
            set
            {
                base.SetValue(HandleHitTestMessageProperty, value);
            }
        }

        public static Window MainFrame
        {
            get
            {
                return bamaMainFrame;
            }
        }

        public Visibility MaxBorderVisibility
        {
            get
            {
                return this.border.Visibility;
            }
            set
            {
                this.border.Visibility = value;
            }
        }
    }


}
