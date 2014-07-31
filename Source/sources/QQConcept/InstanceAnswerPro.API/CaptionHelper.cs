using System.Windows;

namespace InstanceAnswerPro.API
{
    internal class CaptionHelper
    {
        // Fields
        private CaptionInfo captionInfo = new CaptionInfo();

        // Methods
        internal CaptionHelper()
        {
            this.captionInfo.IncludeName = null;
            this.captionInfo.ExIncludesName = null;
            this.Clear();
        }

        private void Calculate(Window win)
        {
            if (this.captionInfo.IncludeElement != null)
            {
                this.captionInfo.IncludeRect = VisualTree.GetVisualRect(win, this.captionInfo.IncludeElement);
            }
            if (this.captionInfo.ExIncludesElement != null)
            {
                this.captionInfo.ExIncludesRect = new Rect[this.captionInfo.ExIncludesElement.Length];
                for (int i = 0; i < this.captionInfo.ExIncludesElement.Length; i++)
                {
                    this.captionInfo.ExIncludesRect[i] = VisualTree.GetVisualRect(win, this.captionInfo.ExIncludesElement[i]);
                }
            }
        }

        private void Clear()
        {
            this.captionInfo.IncludeElement = null;
            this.captionInfo.ExIncludesElement = null;
            this.captionInfo.NeedCalculate = true;
            this.captionInfo.IncludeRect = Rect.Empty;
            this.captionInfo.ExIncludesRect = null;
        }

        internal bool IsInCaption(Window win, Point pt)
        {
            if (this.captionInfo.NeedCalculate)
            {
                this.captionInfo.NeedCalculate = false;
                this.Calculate(win);
            }
            if (!this.captionInfo.IncludeRect.Contains(pt))
            {
                return false;
            }
            foreach (Rect rect in this.captionInfo.ExIncludesRect)
            {
                if (rect.Contains(pt))
                {
                    return false;
                }
            }
            return true;
        }

        internal void OnLoaded(Window win)
        {
            this.Clear();
            if (!string.IsNullOrEmpty(this.captionInfo.IncludeName))
            {
                this.captionInfo.IncludeElement = win.FindName(this.captionInfo.IncludeName) as FrameworkElement;
            }
            if ((this.captionInfo.ExIncludesName != null) && (this.captionInfo.ExIncludesName.Length > 0))
            {
                this.captionInfo.ExIncludesElement = new FrameworkElement[this.captionInfo.ExIncludesName.Length];
                for (int i = 0; i < this.captionInfo.ExIncludesName.Length; i++)
                {
                    this.captionInfo.ExIncludesElement[i] = win.FindName(this.captionInfo.ExIncludesName[i]) as FrameworkElement;
                }
            }
        }

        internal void OnSizeChanged()
        {
            this.captionInfo.NeedCalculate = true;
        }

        internal void OnUnloaded()
        {
            this.Clear();
        }

        internal void SetInfo(string includeName, string[] exIncludesName)
        {
            this.captionInfo.IncludeName = includeName;
            this.captionInfo.ExIncludesName = exIncludesName;
        }

        // Properties
        internal bool CanCaption
        {
            get
            {
                return (this.captionInfo.IncludeElement != null);
            }
        }

        // Nested Types
        private class CaptionInfo
        {
            // Properties
            internal FrameworkElement[] ExIncludesElement { get; set; }

            internal string[] ExIncludesName { get; set; }

            internal Rect[] ExIncludesRect { get; set; }

            internal FrameworkElement IncludeElement { get; set; }

            internal string IncludeName { get; set; }

            internal Rect IncludeRect { get; set; }

            internal bool NeedCalculate { get; set; }
        }
    }


}
