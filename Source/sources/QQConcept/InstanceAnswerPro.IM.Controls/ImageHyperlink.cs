using System;
using System.Windows;
using System.Windows.Documents;
using System.Windows.Media;
using InstanceAnswerPro.Controls;

namespace InstanceAnswerPro.IM.Controls
{
    class ImageHyperlink:Span
    {
        // Fields
    public static readonly RoutedEvent ClickedEvent = EventManager.RegisterRoutedEvent("Clicked", RoutingStrategy.Bubble, typeof(ClickedEventHandler), typeof(ImageHyperlink));
    private InlineUIContainer container;
    public static readonly DependencyProperty EnableCopyProperty = DependencyProperty.RegisterAttached("EnableCopy", typeof(bool), typeof(ImageEx), new UIPropertyMetadata(true));
    private double height = 14.0;
    private Hyperlink hyperlink = new Hyperlink();
    private ImageEx icon;
    private bool isClick = true;
    private bool isInsertedImage;
    private double width = 14.0;

    // Events
    public event ClickedEventHandler Clicked
    {
        add
        {
            base.AddHandler(ClickedEvent, value);
        }
        remove
        {
            base.RemoveHandler(ClickedEvent, value);
        }
    }

    // Methods
    public ImageHyperlink()
    {
        base.Inlines.Add(this.hyperlink);
        this.hyperlink.Click += new RoutedEventHandler(this.hyperlink_Click);
        base.Unloaded += new RoutedEventHandler(this.ImageHyperlink_Unloaded);
    }

    public void AddText(string text)
    {
        this.hyperlink.Inlines.Add(text);
    }

    public void DisabledHyperLink()
    {
        this.hyperlink.TextDecorations = null;
        this.hyperlink.IsEnabled = false;
        this.isClick = false;
        this.hyperlink.Cursor = null;
    }

    private static void DisabledHyperLink(Hyperlink hyperlink)
    {
        hyperlink.TextDecorations = null;
        hyperlink.IsEnabled = false;
        hyperlink.Cursor = null;
    }

    public static bool GetEnableCopy(DependencyObject obj)
    {
        return (bool) obj.GetValue(EnableCopyProperty);
    }

    private void hyperlink_Click(object sender, RoutedEventArgs e)
    {
        e.Handled = true;
        if (this.isClick)
        {
            this.RaiseClicked();
        }
    }

    private void ImageHyperlink_Unloaded(object sender, RoutedEventArgs e)
    {
        base.Unloaded -= new RoutedEventHandler(this.ImageHyperlink_Unloaded);
        this.hyperlink.Click -= new RoutedEventHandler(this.hyperlink_Click);
    }

    public void InsertImage(string path)
    {
        if (!this.isInsertedImage)
        {
            if (this.icon == null)
            {
                this.icon = new ImageEx();
                this.icon.Width = this.Width;
                this.icon.Height = this.Height;
                this.icon.Stretch = Stretch.Fill;
                this.icon.IsCache = true;
                SetEnableCopy(this.icon, false);
            }
            if (this.container == null)
            {
                this.container = new InlineUIContainer();
                this.container.Child = this.icon;
            }
            base.Inlines.InsertBefore(this.hyperlink, this.container);
            this.isInsertedImage = true;
        }
        this.icon.Source = path;
    }

    private void RaiseClicked()
    {
        RoutedEventArgs e = new RoutedEventArgs(ClickedEvent, this);
        base.RaiseEvent(e);
    }

    public void RemoveImage()
    {
        base.Inlines.Remove(this.container);
        this.isInsertedImage = false;
    }

    public static void SetEnableCopy(DependencyObject obj, bool value)
    {
        obj.SetValue(EnableCopyProperty, value);
    }

    internal void SetToolTip(string tips)
    {
        base.ToolTip = tips;
    }

    // Properties
    public Guid Guid { get; set; }

    public double Height
    {
        get
        {
            return this.height;
        }
        set
        {
            this.height = value;
            if (this.icon != null)
            {
                this.icon.Height = this.height;
            }
        }
    }

    public string SoureUrl { get; set; }

    public double Width
    {
        get
        {
            return this.width;
        }
        set
        {
            this.width = value;
            if (this.icon != null)
            {
                this.icon.Width = this.width;
            }
        }
    }

    // Nested Types
    public delegate void ClickedEventHandler(object sender, RoutedEventArgs args);
}

}
