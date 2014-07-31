using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.IO;
using System.Net;
using System.Security;
using System.Windows.Resources;
using System.Windows.Threading;
using InstanceAnswerPro.Controls;

namespace InstanceAnswerPro.Controls
{
    internal class WebReadState
    {
        // Fields
        public byte[] buffer;
        public MemoryStream memoryStream;
        public Stream readStream;
        public WebRequest webRequest;
    }

 

    public partial class ImageEx : UserControl, IGUISerialized
    {
        // Fields
        private GifAnimation _gifAnimation;
        private Image _image;
        public static readonly RoutedEvent ClickedEvent = EventManager.RegisterRoutedEvent("Clicked", RoutingStrategy.Bubble, typeof(ClickedEventHandler), typeof(ImageEx));
        public static readonly DependencyProperty ForceGifAnimProperty = DependencyProperty.Register("ForceGifAnim", typeof(bool), typeof(ImageEx), new FrameworkPropertyMetadata(false));
        public static readonly DependencyProperty ForceStaticPicProperty = DependencyProperty.Register("ForceStaticPic", typeof(bool), typeof(ImageEx), new FrameworkPropertyMetadata(false));
        private bool hadMouseLeftButtonDown;
        private static readonly RoutedEvent ImageFailedEvent = EventManager.RegisterRoutedEvent("ImageFailed", RoutingStrategy.Bubble, typeof(ExceptionRoutedEventHandler), typeof(ImageEx));
        public static readonly DependencyProperty IsCacheProperty = DependencyProperty.Register("IsCache", typeof(bool), typeof(ImageEx), new FrameworkPropertyMetadata(false));
        public static readonly DependencyProperty SourceProperty = DependencyProperty.Register("Source", typeof(string), typeof(ImageEx), new FrameworkPropertyMetadata("", FrameworkPropertyMetadataOptions.AffectsRender | FrameworkPropertyMetadataOptions.AffectsMeasure, new PropertyChangedCallback(ImageEx.OnSourceChanged)));
        public static readonly DependencyProperty StretchDirectionProperty = DependencyProperty.Register("StretchDirection", typeof(StretchDirection), typeof(ImageEx), new FrameworkPropertyMetadata(StretchDirection.Both, FrameworkPropertyMetadataOptions.AffectsMeasure, new PropertyChangedCallback(ImageEx.OnStretchDirectionChanged)));
        public static readonly DependencyProperty StretchProperty = DependencyProperty.Register("Stretch", typeof(Stretch), typeof(ImageEx), new FrameworkPropertyMetadata(Stretch.Fill, FrameworkPropertyMetadataOptions.AffectsMeasure, new PropertyChangedCallback(ImageEx.OnStretchChanged)));
        public static readonly DependencyProperty StretchWithStaticProperty = DependencyProperty.Register("StretchWithStatic", typeof(Stretch), typeof(ImageEx), new FrameworkPropertyMetadata(Stretch.None, FrameworkPropertyMetadataOptions.AffectsMeasure, new PropertyChangedCallback(ImageEx.OnStretchWithStaticChanged)));

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

        private event ExceptionRoutedEventHandler ImageFailed
        {
            add
            {
                base.AddHandler(ImageFailedEvent, value);
            }
            remove
            {
                base.RemoveHandler(ImageFailedEvent, value);
            }
        }

        // Methods
        public ImageEx()
        {
            this.IsEnabledClick = false;
            base.Loaded += new RoutedEventHandler(this.ImageEx_Loaded);
        }

        private void _image_ImageFailed(object sender, ExceptionRoutedEventArgs e)
        {
            this.RaiseImageFailedEvent(e.ErrorException);
        }

        bool IGUISerialized.Deserialize(ClipboardControl serializedContent)
        {
            this.Source = serializedContent.ImagePath;
            return true;
        }

        ClipboardControl IGUISerialized.Serialize()
        {
            return new ClipboardControl { ControlType = typeof(ImageEx).FullName, ImagePath = this.Source };
        }

        private void CreateFromSourceString(string source)
        {
            this.DeletePreviousImage();
            if (string.IsNullOrEmpty(source))
            {
                this.RaiseImageFailedEvent(new Exception("字符串为空"));
            }
            else
            {
                ImageSourceCache.ImageCache imageCache = ImageSourceCache.GetImageCache(this.Source);
                if (imageCache != null)
                {
                    if (imageCache.IsStaticPic || this.ForceStaticPic)
                    {
                        this.CreateNonGifAnimationImage(false);
                        return;
                    }
                    if (imageCache.MemoryStream != null)
                    {
                        this.CreateGifAnimation(imageCache.MemoryStream, false);
                        return;
                    }
                }
                Uri uri = new Uri(source, UriKind.RelativeOrAbsolute);
                if (!this.ForceStaticPic && (source.Trim().ToUpper().EndsWith(".GIF") || this.ForceGifAnim))
                {
                    try
                    {
                        if (!uri.IsAbsoluteUri)
                        {
                            this.GetGifStreamFromPack(uri);
                        }
                        else
                        {
                            string leftPart = uri.GetLeftPart(UriPartial.Scheme);
                            switch (leftPart)
                            {
                                case "http://":
                                case "ftp://":
                                    this.GetGifStreamFromHttp(uri);
                                    return;
                            }
                            if (leftPart == "file://")
                            {
                                using (FileStream stream = new FileStream(uri.LocalPath, FileMode.Open, FileAccess.Read))
                                {
                                    this.ReadGifStreamSynch(stream);
                                    stream.Close();
                                    stream.Dispose();
                                    return;
                                }
                            }
                            if (leftPart == "pack://")
                            {
                                this.GetGifStreamFromPack(uri);
                            }
                            else
                            {
                                this.CreateNonGifAnimationImage(true);
                            }
                        }
                    }
                    catch (Exception)
                    {
                        this.CreateNonGifAnimationImage(true);
                    }
                }
                else
                {
                    this.CreateNonGifAnimationImage(false);
                }
            }
        }

        private void CreateGifAnimation(MemoryStream memoryStream, bool cache)
        {
            try
            {
                this.DeletePreviousImage();
                if (!base.HasContent)
                {
                    this.CreateImage(true);
                    this._gifAnimation.Tag = this.Source;
                    this._gifAnimation.CreateGifAnimation(memoryStream);
                    if (cache && this.IsCache)
                    {
                        ImageSourceCache.SetMemoryStream(this.Source, memoryStream);
                    }
                }
            }
            catch (Exception)
            {
                this.CreateNonGifAnimationImage(true);
            }
        }

        private void CreateImage(bool isGif)
        {
            if (isGif)
            {
                if (this._gifAnimation == null)
                {
                    this._gifAnimation = new GifAnimation();
                    this._gifAnimation.Stretch = this.Stretch;
                    this._gifAnimation.StretchDirection = this.StretchDirection;
                    this.AddChild(this._gifAnimation);
                }
            }
            else if (this._image == null)
            {
                this._image = new Image();
                if (this.StretchWithStatic != Stretch.None)
                {
                    this._image.Stretch = this.StretchWithStatic;
                }
                else
                {
                    this._image.Stretch = this.Stretch;
                }
                this._image.StretchDirection = this.StretchDirection;
                this.AddChild(this._image);
            }
        }

        private void CreateNonGifAnimationImage(bool isStaticPic)
        {
            this.DeletePreviousImage();
            if (!string.IsNullOrEmpty(this.Source))
            {
                this.CreateImage(false);
                this._image.Source = ImageSourceCache.GetOrCreateImageSource(this.Source, this.IsCache, isStaticPic);
            }
        }

        private void DeletePreviousImage()
        {
            if (this._image != null)
            {
                base.RemoveLogicalChild(this._image);
                base.Content = null;
                this._image = null;
            }
            if (this._gifAnimation != null)
            {
                base.RemoveLogicalChild(this._gifAnimation);
                base.Content = null;
                this._gifAnimation.Destroy();
                this._gifAnimation = null;
            }
            if (base.Content != null)
            {
                base.RemoveLogicalChild(base.Content);
                base.Content = null;
            }
        }

        private void GetGifStreamFromHttp(Uri uri)
        {
            try
            {
                WebReadState state = new WebReadState
                {
                    memoryStream = new MemoryStream(),
                    webRequest = WebRequest.Create(uri)
                };
                state.webRequest.Timeout = 0x2710;
                state.webRequest.BeginGetResponse(new AsyncCallback(this.WebResponseCallback), state);
            }
            catch (SecurityException)
            {
                this.CreateNonGifAnimationImage(true);
            }
        }

        private void GetGifStreamFromPack(Uri uri)
        {
            try
            {
                StreamResourceInfo contentStream;
                if (!uri.IsAbsoluteUri)
                {
                    contentStream = Application.GetContentStream(uri);
                    if (contentStream == null)
                    {
                        contentStream = Application.GetResourceStream(uri);
                    }
                }
                else if (uri.GetLeftPart(UriPartial.Authority).Contains("siteoforigin"))
                {
                    contentStream = Application.GetRemoteStream(uri);
                }
                else
                {
                    contentStream = Application.GetContentStream(uri);
                    if (contentStream == null)
                    {
                        contentStream = Application.GetResourceStream(uri);
                    }
                }
                if (contentStream == null)
                {
                    throw new FileNotFoundException("Resource not found.", uri.ToString());
                }
                this.ReadGifStreamSynch(contentStream.Stream);
            }
            catch (Exception exception)
            {
                this.RaiseImageFailedEvent(exception);
            }
        }

        public ImageSource GetImageSource()
        {
            if (this._image != null)
            {
                return this._image.Source;
            }
            if (this._gifAnimation != null)
            {
                return this._gifAnimation.GetFirstImageSource();
            }
            return null;
        }

        private void ImageEx_Loaded(object sender, RoutedEventArgs e)
        {
            base.Unloaded += new RoutedEventHandler(this.ImageEx_Unloaded);
            base.MouseLeftButtonUp += new MouseButtonEventHandler(this.ImageEx_MouseLeftButtonUp);
            base.MouseLeftButtonDown += new MouseButtonEventHandler(this.ImageEx_MouseLeftButtonDown);
            this.CreateFromSourceString(this.Source);
        }

        private void ImageEx_MouseLeftButtonDown(object sender, MouseButtonEventArgs e)
        {
            this.hadMouseLeftButtonDown = true;
            e.Handled = this.IsEnabledClick;
        }

        private void ImageEx_MouseLeftButtonUp(object sender, MouseButtonEventArgs e)
        {
            if (this.hadMouseLeftButtonDown)
            {
                this.RaiseImageClicked();
            }
            this.hadMouseLeftButtonDown = false;
        }

        private void ImageEx_Unloaded(object sender, RoutedEventArgs e)
        {
            base.Unloaded -= new RoutedEventHandler(this.ImageEx_Unloaded);
            base.MouseLeftButtonUp -= new MouseButtonEventHandler(this.ImageEx_MouseLeftButtonUp);
            base.MouseLeftButtonDown -= new MouseButtonEventHandler(this.ImageEx_MouseLeftButtonDown);
            if (this._gifAnimation != null)
            {
                this._gifAnimation.Destroy();
                this._gifAnimation = null;
            }
        }

        private static void OnSourceChanged(DependencyObject d, DependencyPropertyChangedEventArgs e)
        {
            ImageEx ex = (ImageEx)d;
            ex.SetValue(RenderOptions.EdgeModeProperty, EdgeMode.Aliased);
            string newValue = (string)e.NewValue;
            ex.CreateFromSourceString(newValue);
        }

        private static void OnStretchChanged(DependencyObject d, DependencyPropertyChangedEventArgs e)
        {
            ImageEx ex = (ImageEx)d;
            Stretch newValue = (Stretch)e.NewValue;
            if (ex._gifAnimation != null)
            {
                ex._gifAnimation.Stretch = newValue;
            }
            else if (ex._image != null)
            {
                ex._image.Stretch = newValue;
                if (ex.StretchWithStatic != Stretch.None)
                {
                    ex._image.Stretch = ex.StretchWithStatic;
                }
                else
                {
                    ex._image.Stretch = newValue;
                }
            }
        }

        private static void OnStretchDirectionChanged(DependencyObject d, DependencyPropertyChangedEventArgs e)
        {
            ImageEx ex = (ImageEx)d;
            StretchDirection newValue = (StretchDirection)e.NewValue;
            if (ex._gifAnimation != null)
            {
                ex._gifAnimation.StretchDirection = newValue;
            }
            else if (ex._image != null)
            {
                ex._image.StretchDirection = newValue;
            }
        }

        private static void OnStretchWithStaticChanged(DependencyObject d, DependencyPropertyChangedEventArgs e)
        {
            ImageEx ex = (ImageEx)d;
            Stretch newValue = (Stretch)e.NewValue;
            if (ex._image != null)
            {
                if (newValue != Stretch.None)
                {
                    ex._image.Stretch = newValue;
                }
                else
                {
                    ex._image.Stretch = ex.Stretch;
                }
            }
        }

        private void RaiseImageClicked()
        {
            if (this.IsEnabledClick)
            {
                RoutedEventArgs e = new RoutedEventArgs(ClickedEvent, this);
                base.RaiseEvent(e);
            }
        }

        public void RaiseImageFailedEvent(Exception exp)
        {
            ImageExExceptionRoutedEventArgs e = new ImageExExceptionRoutedEventArgs(ImageFailedEvent, this)
            {
                ErrorException = exp
            };
            base.RaiseEvent(e);
        }

        private void ReadGifStreamSynch(Stream s)
        {
            MemoryStream stream;
            using (s)
            {
                stream = new MemoryStream((int)s.Length);
                byte[] buffer = new BinaryReader(s).ReadBytes((int)s.Length);
                stream.Write(buffer, 0, (int)s.Length);
                stream.Flush();
            }
            this.CreateGifAnimation(stream, true);
        }

        private void WebReadCallback(IAsyncResult asyncResult)
        {
            WebReadState asyncState = (WebReadState)asyncResult.AsyncState;
            int count = asyncState.readStream.EndRead(asyncResult);
            if (count > 0)
            {
                asyncState.memoryStream.Write(asyncState.buffer, 0, count);
                try
                {
                    asyncState.readStream.BeginRead(asyncState.buffer, 0, asyncState.buffer.Length, new AsyncCallback(this.WebReadCallback), asyncState);
                }
                catch (WebException exception)
                {
                    base.Dispatcher.Invoke(DispatcherPriority.Render, new WebRequestErrorDelegate(this.WebRequestError), exception);
                }
            }
            else
            {
                base.Dispatcher.Invoke(DispatcherPriority.Render, new WebRequestFinishedDelegate(this.WebRequestFinished), asyncState.memoryStream);
            }
        }

        private void WebRequestError(Exception exp)
        {
            this.RaiseImageFailedEvent(exp);
        }

        private void WebRequestFinished(MemoryStream memoryStream)
        {
            this.CreateGifAnimation(memoryStream, true);
        }

        private void WebResponseCallback(IAsyncResult asyncResult)
        {
            WebReadState asyncState = (WebReadState)asyncResult.AsyncState;
            try
            {
                asyncState.readStream = asyncState.webRequest.EndGetResponse(asyncResult).GetResponseStream();
                asyncState.buffer = new byte[0x186a0];
                asyncState.readStream.BeginRead(asyncState.buffer, 0, asyncState.buffer.Length, new AsyncCallback(this.WebReadCallback), asyncState);
            }
            catch (WebException exception)
            {
                base.Dispatcher.Invoke(DispatcherPriority.Render, new WebRequestErrorDelegate(this.WebRequestError), exception);
            }
        }

        // Properties
        public bool ForceGifAnim
        {
            get
            {
                return (bool)base.GetValue(ForceGifAnimProperty);
            }
            set
            {
                base.SetValue(ForceGifAnimProperty, value);
            }
        }

        public bool ForceStaticPic
        {
            get
            {
                return (bool)base.GetValue(ForceStaticPicProperty);
            }
            set
            {
                base.SetValue(ForceStaticPicProperty, value);
            }
        }

        public bool IsCache
        {
            get
            {
                return (bool)base.GetValue(IsCacheProperty);
            }
            set
            {
                base.SetValue(IsCacheProperty, value);
            }
        }

        public bool IsEnabledClick { get; set; }

        public string Source
        {
            get
            {
                return (string)base.GetValue(SourceProperty);
            }
            set
            {
                base.SetValue(SourceProperty, value);
            }
        }

        public Stretch Stretch
        {
            get
            {
                return (Stretch)base.GetValue(StretchProperty);
            }
            set
            {
                base.SetValue(StretchProperty, value);
            }
        }

        public StretchDirection StretchDirection
        {
            get
            {
                return (StretchDirection)base.GetValue(StretchDirectionProperty);
            }
            set
            {
                base.SetValue(StretchDirectionProperty, value);
            }
        }

        public Stretch StretchWithStatic
        {
            get
            {
                return (Stretch)base.GetValue(StretchWithStaticProperty);
            }
            set
            {
                base.SetValue(StretchWithStaticProperty, value);
            }
        }

        // Nested Types
        public delegate void ClickedEventHandler(object sender, RoutedEventArgs args);

        public delegate void ExceptionRoutedEventHandler(object sender, ImageExExceptionRoutedEventArgs args);

        private delegate void WebRequestErrorDelegate(Exception exp);

        private delegate void WebRequestFinishedDelegate(MemoryStream memoryStream);
    }



 

}
