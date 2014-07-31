using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows.Media.Imaging;
using System.Windows;
using System.Windows.Media;

namespace InstanceAnswerPro.Controls
{
    public class PixelBitmap : FrameworkElement
    {
        // Fields
        private Point _pixelOffset;
        private EventHandler _sourceDownloaded;
        private EventHandler<ExceptionEventArgs> _sourceFailed;
        public static readonly DependencyProperty SourceProperty = DependencyProperty.Register("Source", typeof(BitmapSource), typeof(PixelBitmap), new FrameworkPropertyMetadata(null, FrameworkPropertyMetadataOptions.AffectsRender | FrameworkPropertyMetadataOptions.AffectsMeasure, new PropertyChangedCallback(PixelBitmap.OnSourceChanged)));

        // Events
        public event EventHandler<ExceptionEventArgs> BitmapFailed;

        // Methods
        public PixelBitmap()
        {
            this._sourceDownloaded = new EventHandler(this.OnSourceDownloaded);
            this._sourceFailed = new EventHandler<ExceptionEventArgs>(this.OnSourceFailed);
            base.LayoutUpdated += new EventHandler(this.OnLayoutUpdated);
        }

        private Point ApplyVisualTransform(Point point, Visual v, bool inverse)
        {
            bool success = true;
            return this.TryApplyVisualTransform(point, v, inverse, true, out success);
        }

        private bool AreClose(double value1, double value2)
        {
            if (value1 == value2)
            {
                return true;
            }
            double num = value1 - value2;
            return ((num < 1.53E-06) && (num > -1.53E-06));
        }

        private bool AreClose(Point point1, Point point2)
        {
            return (this.AreClose(point1.X, point2.X) && this.AreClose(point1.Y, point2.Y));
        }

        private Point GetPixelOffset()
        {
            Point point = new Point();
            PresentationSource source = PresentationSource.FromVisual(this);
            if (source != null)
            {
                Visual rootVisual = source.RootVisual;
                point = base.TransformToAncestor(rootVisual).Transform(point);
                point = this.ApplyVisualTransform(point, rootVisual, false);
                point = source.CompositionTarget.TransformToDevice.Transform(point);
                point.X = Math.Round(point.X);
                point.Y = Math.Round(point.Y);
                point = source.CompositionTarget.TransformFromDevice.Transform(point);
                point = this.ApplyVisualTransform(point, rootVisual, true);
                point = rootVisual.TransformToDescendant(this).Transform(point);
            }
            return point;
        }

        private Matrix GetVisualTransform(Visual v)
        {
            if (v == null)
            {
                return Matrix.Identity;
            }
            Matrix identity = Matrix.Identity;
            Transform transform = VisualTreeHelper.GetTransform(v);
            if (transform != null)
            {
                Matrix matrix2 = transform.Value;
                identity = Matrix.Multiply(identity, matrix2);
            }
            Vector offset = VisualTreeHelper.GetOffset(v);
            identity.Translate(offset.X, offset.Y);
            return identity;
        }

        protected override Size MeasureOverride(Size availableSize)
        {
            Size size = new Size();
            BitmapSource source = this.Source;
            if (source != null)
            {
                PresentationSource source2 = PresentationSource.FromVisual(this);
                if (source2 != null)
                {
                    Matrix transformFromDevice = source2.CompositionTarget.TransformFromDevice;
                    Vector vector = new Vector((double)source.PixelWidth, (double)source.PixelHeight);
                    Vector vector2 = transformFromDevice.Transform(vector);
                    size = new Size(vector2.X, vector2.Y);
                }
            }
            return size;
        }

        private void OnLayoutUpdated(object sender, EventArgs e)
        {
            if ((base.ActualHeight != 0.0) && (base.ActualWidth != 0.0))
            {
                Point pixelOffset = this.GetPixelOffset();
                if (!this.AreClose(pixelOffset, this._pixelOffset))
                {
                    base.InvalidateVisual();
                }
            }
        }

        protected override void OnRender(DrawingContext dc)
        {
            BitmapSource imageSource = this.Source;
            if (imageSource != null)
            {
                this._pixelOffset = this.GetPixelOffset();
                double width = 0.0;
                double height = 0.0;
                switch (base.HorizontalAlignment)
                {
                    case HorizontalAlignment.Left:
                    case HorizontalAlignment.Right:
                        width = (base.DesiredSize.Width - base.Margin.Left) - base.Margin.Right;
                        break;

                    case HorizontalAlignment.Center:
                    case HorizontalAlignment.Stretch:
                        width = base.DesiredSize.Width;
                        break;
                }
                switch (base.VerticalAlignment)
                {
                    case VerticalAlignment.Top:
                    case VerticalAlignment.Bottom:
                        height = (base.DesiredSize.Height - base.Margin.Top) - base.Margin.Bottom;
                        break;

                    case VerticalAlignment.Center:
                    case VerticalAlignment.Stretch:
                        height = base.DesiredSize.Height;
                        break;
                }
                if (height < 0.0)
                {
                    height = 0.0;
                }
                if (width < 0.0)
                {
                    width = 0.0;
                }
                dc.DrawImage(imageSource, new Rect(this._pixelOffset, new Size(width, height)));
            }
        }

        private static void OnSourceChanged(DependencyObject d, DependencyPropertyChangedEventArgs e)
        {
            PixelBitmap bitmap = (PixelBitmap)d;
            BitmapSource oldValue = (BitmapSource)e.OldValue;
            BitmapSource newValue = (BitmapSource)e.NewValue;
            if (((oldValue != null) && (bitmap._sourceDownloaded != null)) && (!oldValue.IsFrozen && (oldValue != null)))
            {
                oldValue.DownloadCompleted -= bitmap._sourceDownloaded;
                oldValue.DownloadFailed -= bitmap._sourceFailed;
            }
            if (((newValue != null) && (newValue != null)) && !newValue.IsFrozen)
            {
                newValue.DownloadCompleted += bitmap._sourceDownloaded;
                newValue.DownloadFailed += bitmap._sourceFailed;
            }
        }

        private void OnSourceDownloaded(object sender, EventArgs e)
        {
            base.InvalidateMeasure();
            base.InvalidateVisual();
        }

        private void OnSourceFailed(object sender, ExceptionEventArgs e)
        {
            this.Source = null;
            this.BitmapFailed(this, e);
        }

        private Point TryApplyVisualTransform(Point point, Visual v, bool inverse, bool throwOnError, out bool success)
        {
            success = true;
            if (v != null)
            {
                Matrix visualTransform = this.GetVisualTransform(v);
                if (inverse)
                {
                    if (!throwOnError && !visualTransform.HasInverse)
                    {
                        success = false;
                        return new Point(0.0, 0.0);
                    }
                    visualTransform.Invert();
                }
                point = visualTransform.Transform(point);
            }
            return point;
        }

        // Properties
        public BitmapSource Source
        {
            get
            {
                return (BitmapSource)base.GetValue(SourceProperty);
            }
            set
            {
                base.SetValue(SourceProperty, value);
            }
        }
    }


}
