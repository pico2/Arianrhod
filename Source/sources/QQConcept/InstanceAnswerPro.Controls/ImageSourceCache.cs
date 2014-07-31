using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace InstanceAnswerPro.Controls
{
    using System;
    using System.Collections.Generic;
    using System.IO;
    using System.Runtime.CompilerServices;
    using System.Windows.Media;

    public static class ImageSourceCache
    {
        private static Dictionary<string, ImageCache> imageDic = new Dictionary<string, ImageCache>();

        private static ImageSource CreateFromSourceString(string file)
        {
            try
            {
                return (ImageSource)new ImageSourceConverter().ConvertFromString(file);
            }
            catch (Exception)
            {
            }
            return null;
        }

        public static ImageCache GetImageCache(string file)
        {
            file = file.ToLower();
            if (imageDic.ContainsKey(file))
            {
                return imageDic[file];
            }
            return null;
        }

        public static ImageSource GetOrCreateImageSource(string file, bool cache, bool isStaticPic)
        {
            file = file.ToLower();
            ImageCache imageCache = GetImageCache(file);
            if ((imageCache != null) && (imageCache.ImageSource != null))
            {
                if (isStaticPic)
                {
                    imageCache.SetStaticPicFlag();
                }
                return imageCache.ImageSource;
            }
            ImageSource imageSource = CreateFromSourceString(file);
            if (cache && (imageSource != null))
            {
                imageDic.Add(file, new ImageCache(imageSource, isStaticPic));
            }
            return imageSource;
        }

        internal static void SetImageSource(string file, ImageSource imageSource, bool justStaticPic)
        {
            file = file.ToLower();
            if (imageDic.ContainsKey(file))
            {
                imageDic[file].SetImageSource(imageSource);
            }
            else
            {
                imageDic.Add(file, new ImageCache(imageSource, justStaticPic));
            }
        }

        internal static void SetMemoryStream(string file, MemoryStream memoryStream)
        {
            file = file.ToLower();
            if (imageDic.ContainsKey(file))
            {
                imageDic[file].SetMemoryStream(memoryStream);
            }
            else
            {
                imageDic.Add(file, new ImageCache(memoryStream));
            }
        }

        public class ImageCache
        {
            private System.IO.MemoryStream _memoryStream;

            public ImageCache(System.IO.MemoryStream ms)
            {
                this.IsStaticPic = false;
                this.MemoryStream = ms;
            }

            public ImageCache(System.Windows.Media.ImageSource imageSource)
            {
                this.IsStaticPic = false;
                this.ImageSource = imageSource;
            }

            public ImageCache(System.Windows.Media.ImageSource imageSource, bool isStaticPic)
            {
                this.IsStaticPic = isStaticPic;
                this.ImageSource = imageSource;
            }

            public void SetImageSource(System.Windows.Media.ImageSource imageSource)
            {
                System.Windows.Media.ImageSource source1 = this.ImageSource;
                this.ImageSource = imageSource;
            }

            public void SetMemoryStream(System.IO.MemoryStream memoryStream)
            {
                bool isStaticPic = this.IsStaticPic;
                System.IO.MemoryStream stream1 = this.MemoryStream;
                this.MemoryStream = memoryStream;
                this.IsStaticPic = false;
            }

            public void SetStaticPicFlag()
            {
                this.IsStaticPic = true;
            }

            public System.Windows.Media.ImageSource ImageSource { get; private set; }

            public bool IsStaticPic { get; private set; }

            public System.IO.MemoryStream MemoryStream
            {
                get
                {
                    if (this._memoryStream != null)
                    {
                        this._memoryStream.Seek(0L, SeekOrigin.Begin);
                    }
                    return this._memoryStream;
                }
                private set
                {
                    this._memoryStream = value;
                }
            }
        }
    }
}
