using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows.Controls;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.IO;
using System.Windows;

namespace InstanceAnswerPro.Controls
{
    public class ImageExExceptionRoutedEventArgs : RoutedEventArgs
    {
        // Fields
        public Exception ErrorException;

        // Methods
        public ImageExExceptionRoutedEventArgs(RoutedEvent routedEvent, object obj)
            : base(routedEvent, obj)
        {
        }
    }
    public class GifAnimation : Viewbox
    {
        // Fields
        private Canvas _canvas = new Canvas();
        private int _currentLoop;
        private GifFrame _currentParseGifFrame;
        private int _frameCounter;
        private List<GifFrame> _frameList;
        private int _logicalHeight;
        private int _logicalWidth;
        private int _numberOfFrames;
        private int _numberOfLoops = -1;
        private TimerMgr.TimerItem timerItem;
        private Geometry totalTransparentGeometry;

        // Methods
        public GifAnimation()
        {
            this.Child = this._canvas;
        }

        private BitmapImage ConvertToBitmapImage(BitmapFrame bf)
        {
            BmpBitmapEncoder encoder = new BmpBitmapEncoder
            {
                Frames = { bf }
            };
            MemoryStream stream = new MemoryStream();
            encoder.Save(stream);
            stream.Seek(0L, SeekOrigin.Begin);
            BitmapImage image = new BitmapImage();
            image.BeginInit();
            image.StreamSource = stream;
            image.EndInit();
            stream.Close();
            return image;
        }

        public void CreateGifAnimation(MemoryStream memoryStream)
        {
            this.Reset();
            byte[] gifData = memoryStream.GetBuffer();
            GifBitmapDecoder decoder = new GifBitmapDecoder(memoryStream, BitmapCreateOptions.PreservePixelFormat, BitmapCacheOption.Default);
            this._numberOfFrames = decoder.Frames.Count;
            try
            {
                this.ParseGif(gifData);
            }
            catch
            {
                throw new FileFormatException("Unable to parse Gif file format.");
            }
            for (int i = 0; i < decoder.Frames.Count; i++)
            {
                this._frameList[i].Source = decoder.Frames[i];
                this._frameList[i].Visibility = Visibility.Hidden;
            }
            this._canvas.Height = this._logicalHeight;
            this._canvas.Width = this._logicalWidth;
            this._frameList[0].Visibility = Visibility.Visible;
            for (int j = 0; j < this._frameList.Count; j++)
            {
                Console.WriteLine(this._frameList[j].disposalMethod.ToString() + " " + this._frameList[j].width.ToString() + " " + this._frameList[j].delayTime.ToString());
            }
            if (this._frameList.Count > 1)
            {
                if (this._numberOfLoops == -1)
                {
                    this._numberOfLoops = 1;
                }
                this.SetTimer(this._frameList[0].delayTime * 10);
            }
            base.InvalidateVisual();
        }

        internal void Destroy()
        {
            this.Reset();
        }

        public ImageSource GetFirstImageSource()
        {
            if ((this._frameList != null) && (this._frameList.Count > 0))
            {
                return this._frameList[0].Source;
            }
            return null;
        }

        public void NextFrame()
        {
            this.NextFrame(null, null);
        }

        public void NextFrame(object sender, EventArgs e)
        {
            if (this._numberOfFrames != 0)
            {
                if (this._frameList[this._frameCounter].disposalMethod == 2)
                {
                    for (int i = 0; i < this._frameCounter; i++)
                    {
                        if (this._frameList[i].Visibility == Visibility.Visible)
                        {
                            GifFrame frame = this._frameList[this._frameCounter];
                            RectangleGeometry geometry = new RectangleGeometry(new Rect((double)frame.left, (double)frame.top, (double)frame.width, (double)frame.height));
                            this.totalTransparentGeometry = new CombinedGeometry(GeometryCombineMode.Union, this.totalTransparentGeometry, geometry);
                            GifFrame frame2 = this._frameList[i];
                            RectangleGeometry geometry2 = new RectangleGeometry(new Rect((double)frame2.left, (double)frame2.top, (double)frame2.width, (double)frame2.height));
                            CombinedGeometry geometry3 = new CombinedGeometry(GeometryCombineMode.Exclude, geometry2, this.totalTransparentGeometry);
                            GeometryDrawing drawing = new GeometryDrawing(Brushes.Black, new Pen(Brushes.Black, 0.0), geometry3);
                            DrawingBrush brush = new DrawingBrush(drawing);
                            this._frameList[i].OpacityMask = brush;
                        }
                    }
                    this._frameList[this._frameCounter].Visibility = Visibility.Hidden;
                }
                if (this._frameList[this._frameCounter].disposalMethod >= 3)
                {
                    this._frameList[this._frameCounter].Visibility = Visibility.Hidden;
                }
                this._frameCounter++;
                if (this._frameCounter < this._numberOfFrames)
                {
                    this._frameList[this._frameCounter].Visibility = Visibility.Visible;
                    this.SetTimer(this._frameList[this._frameCounter].delayTime * 10);
                }
                else
                {
                    if (this._numberOfLoops != 0)
                    {
                        this._currentLoop++;
                    }
                    if ((this._currentLoop < this._numberOfLoops) || (this._numberOfLoops == 0))
                    {
                        for (int j = 0; j < this._frameList.Count; j++)
                        {
                            this._frameList[j].Visibility = Visibility.Hidden;
                            this._frameList[j].OpacityMask = null;
                        }
                        this.totalTransparentGeometry = null;
                        this._frameCounter = 0;
                        this._frameList[this._frameCounter].Visibility = Visibility.Visible;
                        this.SetTimer(this._frameList[this._frameCounter].delayTime * 10);
                    }
                }
                base.InvalidateVisual();
            }
        }

        protected override void OnRender(DrawingContext drawingContext)
        {
            base.OnRender(drawingContext);
            if (this._frameList != null)
            {
                foreach (GifFrame frame in this._frameList)
                {
                    if ((frame != null) && (frame.Visibility == Visibility.Visible))
                    {
                        if (base.Stretch != Stretch.None)
                        {
                            drawingContext.DrawImage(frame.Source, new Rect((double)frame.left, (double)frame.top, base.ActualWidth, base.ActualHeight));
                        }
                        else
                        {
                            drawingContext.DrawImage(frame.Source, new Rect((double)frame.left, (double)frame.top, (double)frame.width, (double)frame.height));
                        }
                    }
                }
            }
        }

        private int ParseBlock(byte[] gifData, int offset)
        {
            switch (gifData[offset])
            {
                case 0x21:
                    if (gifData[offset + 1] == 0xf9)
                    {
                        return this.ParseGraphicControlExtension(gifData, offset);
                    }
                    return this.ParseExtensionBlock(gifData, offset);

                case 0x2c:
                    offset = this.ParseGraphicBlock(gifData, offset);
                    this._frameList.Add(this._currentParseGifFrame);
                    this._currentParseGifFrame = new GifFrame();
                    return offset;

                case 0x3b:
                    return -1;
            }
            throw new Exception("GIF format incorrect: missing graphic block or special-purpose block. ");
        }

        private int ParseExtensionBlock(byte[] gifData, int offset)
        {
            int index = offset;
            int num2 = gifData[offset + 2];
            index = ((offset + num2) + 2) + 1;
            if (((gifData[offset + 1] == 0xff) && (num2 > 10)) && (Encoding.ASCII.GetString(gifData, offset + 3, 8) == "NETSCAPE"))
            {
                this._numberOfLoops = BitConverter.ToUInt16(gifData, offset + 0x10);
                if (this._numberOfLoops > 0)
                {
                    this._numberOfLoops++;
                }
            }
            while (gifData[index] != 0)
            {
                index = (index + gifData[index]) + 1;
            }
            index++;
            return index;
        }

        private void ParseGif(byte[] gifData)
        {
            this._frameList = new List<GifFrame>();
            this._currentParseGifFrame = new GifFrame();
            this.ParseGifDataStream(gifData, 0);
        }

        private void ParseGifDataStream(byte[] gifData, int offset)
        {
            offset = this.ParseHeader(gifData, offset);
            offset = this.ParseLogicalScreen(gifData, offset);
            while (offset != -1)
            {
                offset = this.ParseBlock(gifData, offset);
            }
        }

        private int ParseGraphicBlock(byte[] gifData, int offset)
        {
            this._currentParseGifFrame.left = BitConverter.ToUInt16(gifData, offset + 1);
            this._currentParseGifFrame.top = BitConverter.ToUInt16(gifData, offset + 3);
            this._currentParseGifFrame.width = BitConverter.ToUInt16(gifData, offset + 5);
            this._currentParseGifFrame.height = BitConverter.ToUInt16(gifData, offset + 7);
            if (this._currentParseGifFrame.width > this._logicalWidth)
            {
                this._logicalWidth = this._currentParseGifFrame.width;
            }
            if (this._currentParseGifFrame.height > this._logicalHeight)
            {
                this._logicalHeight = this._currentParseGifFrame.height;
            }
            byte num = gifData[offset + 9];
            bool flag = (num & 0x80) > 0;
            int index = offset + 9;
            if (flag)
            {
                int num3 = num & 7;
                num3 = ((int)Math.Pow(2.0, (double)(num3 + 1))) * 3;
                index += num3;
            }
            index++;
            index++;
            while (gifData[index] != 0)
            {
                byte num1 = gifData[index];
                index += gifData[index];
                index++;
            }
            index++;
            return index;
        }

        private int ParseGraphicControlExtension(byte[] gifData, int offset)
        {
            int index = offset;
            int num2 = gifData[offset + 2];
            index = ((offset + num2) + 2) + 1;
            byte num3 = gifData[offset + 3];
            this._currentParseGifFrame.disposalMethod = (num3 & 0x1c) >> 2;
            int num4 = BitConverter.ToUInt16(gifData, offset + 4);
            num4 = (num4 < 5) ? 5 : num4;
            this._currentParseGifFrame.delayTime = num4;
            while (gifData[index] != 0)
            {
                index = (index + gifData[index]) + 1;
            }
            index++;
            return index;
        }

        private int ParseHeader(byte[] gifData, int offset)
        {
            if (Encoding.ASCII.GetString(gifData, offset, 3) != "GIF")
            {
                throw new Exception("Not a proper GIF file: missing GIF header");
            }
            return 6;
        }

        private int ParseLogicalScreen(byte[] gifData, int offset)
        {
            this._logicalWidth = BitConverter.ToUInt16(gifData, offset);
            this._logicalHeight = BitConverter.ToUInt16(gifData, offset + 2);
            byte num = gifData[offset + 4];
            bool flag = (num & 0x80) > 0;
            int num2 = offset + 7;
            if (flag)
            {
                int num3 = num & 7;
                num3 = ((int)Math.Pow(2.0, (double)(num3 + 1))) * 3;
                num2 += num3;
            }
            return num2;
        }

        private void Reset()
        {
            if (this._frameList != null)
            {
                this._frameList.Clear();
            }
            this._frameList = null;
            this._frameCounter = 0;
            this._numberOfFrames = 0;
            this._numberOfLoops = -1;
            this._currentLoop = 0;
            this._logicalWidth = 0;
            this._logicalHeight = 0;
            if (this.timerItem != null)
            {
                TimerMgr.EraseTimerCallback(this.timerItem);
                this.timerItem = null;
            }
        }

        private void SetTimer(int elapse)
        {
            if (this.timerItem == null)
            {
                this.timerItem = TimerMgr.SetInterval((uint)elapse, new TimerMgr.TimerCallBacktHandler(this.TimerCallBacktHandler));
            }
            else
            {
                this.timerItem.Elapse = (uint)elapse;
            }
        }

        private void TimerCallBacktHandler(TimerMgr.TimerItem item)
        {
            this.NextFrame();
        }
    }


}
