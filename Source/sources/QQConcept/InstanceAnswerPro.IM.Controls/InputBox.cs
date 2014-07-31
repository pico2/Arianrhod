
namespace InstanceAnswerPro.IM.Controls
{
    using System;
    using System.Collections.Generic;
    using System.IO;
    using System.Reflection;
    using System.Windows;
    using System.Windows.Controls;
    using System.Windows.Documents;
    using System.Windows.Input;
    using System.Windows.Media;
    using InstanceAnswerPro.API;
    using InstanceAnswerPro.Controls;
    using InstanceAnswerPro.Core;
    using KernelWrapper;
    using TextElement = InstanceAnswerPro.Core.TextElement;
    public class InputBox : RichTextBox
    {
        // Fields
        private static PathGeometry _geometry;
        private Color _oppColor;
        private Color _selfColor;
        public static readonly DependencyProperty BoldProperty = DependencyProperty.Register("Bold", typeof(bool), typeof(InputBox), new PropertyMetadata(false, new PropertyChangedCallback(InputBox.OnBoldChanged)));
        private CanExecuteRoutedEventHandler canExecuteRoutedEventHandler;
        private static PropertyInfo charOffsetPropertyInfo = null;
        private ImageEx.ClickedEventHandler clickedEventHandler;
        private DataObjectCopyingEventHandler copyingEventHandler;
        public static readonly DependencyProperty DateTimeProperty = DependencyProperty.RegisterAttached("DateTime", typeof(DateTime), typeof(Section), new FrameworkPropertyMetadata(new DateTime(), FrameworkPropertyMetadataOptions.Inherits));
        private static FontFamily defaultFontFamily = new FontFamily("Microsoft YaHei");
        private ExecutedRoutedEventHandler executedRoutedEventHandler;
        public static readonly DependencyProperty GlobalColorProperty = DependencyProperty.Register("GlobalColor", typeof(Color), typeof(InputBox), new PropertyMetadata(Colors.Black, new PropertyChangedCallback(InputBox.OnGlobalColorChanged)));
        public static readonly DependencyProperty GlobalFontFamilyProperty = DependencyProperty.Register("GlobalFontFamily", typeof(FontFamily), typeof(InputBox), new PropertyMetadata(defaultFontFamily, new PropertyChangedCallback(InputBox.OnGlobalFontFamilyChanged)));
        public static readonly DependencyProperty GlobalFontSizeProperty = DependencyProperty.Register("GlobalFontSize", typeof(double), typeof(InputBox), new PropertyMetadata(12.0, new PropertyChangedCallback(InputBox.OnGlobalFontSizeChanged)));
        private static int ImageElementNum = 0;
        private Dictionary<Guid, List<ImageEx>> imagesDownloading;
        public static readonly DependencyProperty ItalicProperty = DependencyProperty.Register("Italic", typeof(bool), typeof(InputBox), new PropertyMetadata(false, new PropertyChangedCallback(InputBox.OnItalicChanged)));
        private static uint MaxPieces = 80;
        private DataObjectPastingEventHandler pastingEventHandler;
        private static uint ReservePieces = 50;
        private MenuItem saveAsMenuItem;
        private FlowDocument tempFlowDocument = new FlowDocument();
        public static readonly DependencyProperty UnderlineProperty = DependencyProperty.Register("Underline", typeof(bool), typeof(InputBox), new PropertyMetadata(false, new PropertyChangedCallback(InputBox.OnUnderlineChanged)));
        private Dictionary<string, List<ImageHyperlink>> urlInfoDownloading;

        // Events
        public event SendFileEventHandler SendFile;

        // Methods
        static InputBox()
        {
            FrameworkElement.DefaultStyleKeyProperty.OverrideMetadata(typeof(InputBox), new FrameworkPropertyMetadata(typeof(InputBox)));
        }

        public InputBox()
        {
            MenuItem item = new MenuItem
            {
                Command = ApplicationCommands.SaveAs
            };
            this.saveAsMenuItem = item;
            this.imagesDownloading = new Dictionary<Guid, List<ImageEx>>();
            this.urlInfoDownloading = new Dictionary<string, List<ImageHyperlink>>();
            this._selfColor = Color.FromArgb(0xff, 0x69, 0x98, 0x67);
            this._oppColor = Color.FromArgb(0xff, 0x52, 0x89, 0xa3);
            base.Loaded += new RoutedEventHandler(this.InputBox_Loaded);
            ComponentManager.GetGrayURLMgr().URLInfoUpdate += new TXGrayURLMgr.OnURLInfoUpdateHandler(this.InputBox_URLInfoUpdate);
            base.IsDocumentEnabled = true;
        }

        public void AddMsgToOutputBox(IMMessage imMessage, string senderName, AddMsgToOutputBoxCallBackHandler callBack)
        {
            this.CheckMsgPiece();
            InputBox box = this;
            MessagePack messagePack = imMessage.MessagePack;
            if (messagePack != null)
            {
                if (messagePack.NeedShowHeader && (imMessage.Sender == null))
                {
                    messagePack.NeedShowHeader = false;
                }
                if (messagePack.NeedShowHeader && string.IsNullOrEmpty(senderName))
                {
                    senderName = imMessage.SenderName;
                    if (string.IsNullOrEmpty(senderName))
                    {
                        senderName = imMessage.Sender.NickName;
                    }
                }
                uint elemCount = messagePack.GetElemCount();
                Section newItem = new Section();
                Block lastBlock = box.Document.Blocks.LastBlock;
                if ((lastBlock != null) && (string.Compare(lastBlock.Tag as string, "LastTag") != 0))
                {
                    lastBlock = null;
                }
                if (lastBlock == null)
                {
                    Paragraph paragraph = new Paragraph
                    {
                        Tag = "LastTag",
                        Margin = new Thickness(0.0)
                    };
                    lastBlock = paragraph;
                    box.Document.Blocks.Add(lastBlock);
                }
                if (messagePack.NeedShowHeader)
                {
                    if ((imMessage.Sender != null) && (imMessage.Sender.Uin == Util_Buddy.GetCurrentBuddy().Uin))
                    {
                        newItem.Tag = "me";
                    }
                    else
                    {
                        newItem.Tag = "other";
                    }
                }
                else
                {
                    newItem.Tag = "info";
                }
                box.Document.Blocks.InsertBefore(lastBlock, newItem);
                Paragraph item = new Paragraph();
                if (messagePack.NeedShowHeader)
                {
                    string str;
                    Paragraph paragraph3 = new Paragraph
                    {
                        Foreground = new SolidColorBrush((imMessage.Sender.Uin == Util_Buddy.GetCurrentBuddy().Uin) ? this._selfColor : this._oppColor)
                    };
                    if (this.IsMsgRecord)
                    {
                        str = senderName + "  " + imMessage.DateTime.ToLocalTime().ToString();
                    }
                    else
                    {
                        str = senderName + "  " + imMessage.DateTime.ToLocalTime().ToLongTimeString();
                        item.Margin = new Thickness(13.0, 0.0, 0.0, 0.0);
                    }
                    paragraph3.Inlines.Add(str);
                    newItem.Blocks.Add(paragraph3);
                }
                SetDateTime(newItem, imMessage.DateTime);
                Paragraph paragraph4 = new Paragraph
                {
                    Margin = new Thickness(13.0, 0.0, 0.0, 0.0)
                };
                string fontName = messagePack.Header.FontName;
                if ((string.IsNullOrEmpty(fontName) || (fontName == "宋体")) || (((fontName == "新宋体") || (fontName == "仿宋")) || (fontName == "黑体")))
                {
                    fontName = "Microsoft YaHei";
                }
                if (messagePack.Header.FontSize == 0)
                {
                    messagePack.Header.FontSize = 9;
                }
                item.FontFamily = new FontFamily(fontName);
                item.FontSize = messagePack.Header.FontSize + 3;
                item.Foreground = new SolidColorBrush(messagePack.Header.FontColor);
                paragraph4.FontFamily = new FontFamily(messagePack.Header.FontName);
                paragraph4.FontSize = messagePack.Header.FontSize + 3;
                paragraph4.Foreground = new SolidColorBrush(messagePack.Header.FontColor);
                Dictionary<string, bool> imagelist = new Dictionary<string, bool>();
                Paragraph paragraph5 = item;
                bool flag = false;
                for (uint i = 0; i < elemCount; i++)
                {
                    ImageElement element4;
                    string path;
                    ImageEx ex2;
                    MessageElement elem = messagePack.GetElem(i);
                    switch (elem.Category)
                    {
                        case MsgPackCat.ELEMTYPE_TEXT:
                            {
                                Guid guid;
                                Guid guid2;
                                TextElement element2 = (TextElement)elem;
                                string text = element2.GetText();
                                if (!flag && element2.NeedIndent)
                                {
                                    Span lastInline = item.Inlines.LastInline as Span;
                                    if (lastInline != null)
                                    {
                                        Run run = lastInline.Inlines.LastInline as Run;
                                        if (run != null)
                                        {
                                            run.Text = run.Text.Replace("\r", "").Replace("\n", "");
                                        }
                                    }
                                    paragraph5 = paragraph4;
                                }
                                string url = element2.GetUrl(out guid, out guid2);
                                Span span2 = new Span();
                                Span span3 = span2;
                                paragraph5.Inlines.Add(span3);
                                if ((messagePack.Header.FontEffect & 2) != 0)
                                {
                                    span2.FontStyle = FontStyles.Italic;
                                }
                                if ((messagePack.Header.FontEffect & 1) != 0)
                                {
                                    span2.FontWeight = FontWeights.Bold;
                                }
                                if (string.IsNullOrEmpty(url))
                                {
                                    if ((messagePack.Header.FontEffect & 4) != 0)
                                    {
                                        Underline underline = new Underline();
                                        span2.Inlines.Add(underline);
                                        span2 = underline;
                                    }
                                    span2.Inlines.Add(text);
                                }
                                else
                                {
                                    ImageHyperlink hyperlink = new ImageHyperlink
                                    {
                                        Guid = guid,
                                        SoureUrl = url
                                    };
                                    span2.Inlines.Add(hyperlink);
                                    span2 = hyperlink;
                                    hyperlink.AddText(text);
                                    this.OnImageHyperLinkAdd(imMessage, hyperlink);
                                }
                                continue;
                            }
                        case MsgPackCat.ELEMTYPE_SYSFACE:
                            {
                                SysFaceElement element = (SysFaceElement)elem;
                                ImageEx uiElement = ReplaceControls.CreateImageExWithId(element.FileName, element.Index.ToString());
                                uiElement.Width = element.FaceWidth;
                                uiElement.Height = element.FaceHeight;
                                paragraph5.Inlines.Add(uiElement);
                                if (callBack != null)
                                {
                                    callBack(imMessage, element);
                                }
                                continue;
                            }
                        case MsgPackCat.ELEMTYPE_IMAGE:
                        case MsgPackCat.ELEMTYPE_OFFLINEPIC:
                            element4 = (ImageElement)elem;
                            path = element4.Path;
                            if (string.IsNullOrEmpty(path))
                            {
                                continue;
                            }
                            ex2 = new ImageEx
                            {
                                HorizontalAlignment = HorizontalAlignment.Left,
                                VerticalAlignment = VerticalAlignment.Top,
                                Stretch = Stretch.None,
                                SnapsToDevicePixels = true,
                                Tag = element4
                            };
                            path = path.ToLower();
                            if (!CheckFileExists(imagelist, path))
                            {
                                break;
                            }
                            ex2.Source = path;
                            goto Label_0710;

                        case MsgPackCat.ELEMTYPE_FILE:
                            {
                                FileElement element5 = (FileElement)elem;
                                string str7 = Helper_Icon.MakeSysIconFileByFileName(element5.Path);
                                string fileSize = element5.GetFileSize();
                                string fileName = element5.GetFileName();
                                if (!string.IsNullOrEmpty(str7))
                                {
                                    ImageEx ex3 = new ImageEx
                                    {
                                        HorizontalAlignment = HorizontalAlignment.Left,
                                        VerticalAlignment = VerticalAlignment.Top,
                                        Stretch = Stretch.Uniform,
                                        SnapsToDevicePixels = true,
                                        Width = 32.0,
                                        Height = 32.0
                                    };
                                    if (!string.IsNullOrEmpty(element5.Tip))
                                    {
                                        ex3.ToolTip = element5.Tip;
                                    }
                                    ex3.Source = str7;
                                    StackPanel panel = new StackPanel
                                    {
                                        Margin = new Thickness(0.0, 2.0, 0.0, 2.0),
                                        Orientation = Orientation.Horizontal
                                    };
                                    panel.Children.Add(ex3);
                                    TextBlock block2 = new TextBlock(new Run(fileName + "\n" + fileSize))
                                    {
                                        Margin = new Thickness(0.0, 4.0, 0.0, 0.0)
                                    };
                                    panel.Children.Add(block2);
                                    paragraph5.Inlines.Add(panel);
                                }
                                continue;
                            }
                        default:
                            goto Label_087B;
                    }
                    if (this.IsMsgRecord)
                    {
                        ex2.Source = CoreMessenger.Instance.GetAppPath(KernelWrapper.APP_PATH_TYPE.APP_PATH_DATA) + "errorBmp.gif";
                    }
                    else if (MsgPackCat.ELEMTYPE_IMAGE == elem.Category)
                    {
                        TXLog.TXLogImage(string.Concat(new object[] { "收到图片文件需要下载：", element4.Id, "  ", path }));
                        ex2.Source = CoreMessenger.Instance.GetAppPath(KernelWrapper.APP_PATH_TYPE.APP_PATH_DATA) + "sendingBmp.gif";
                        this.AddToImagesDownloadingList(element4.Id, ex2);
                    }
                    else if (MsgPackCat.ELEMTYPE_OFFLINEPIC == elem.Category)
                    {
                        TXLog.TXLogImage(string.Concat(new object[] { "收到离线图片文件需要下载：", element4.Id, "  ", path }));
                        ex2.IsEnabledClick = true;
                        ex2.Source = CoreMessenger.Instance.GetAppPath(KernelWrapper.APP_PATH_TYPE.APP_PATH_DATA) + "OfflinepicManualGet.png";
                        ex2.ToolTip = "点击获取图片";
                        ex2.Cursor = Cursors.Hand;
                    }
                Label_0710:
                    paragraph5.Inlines.Add(ex2);
                    continue;
                Label_087B:
                    TXLog.TXLog3("Msg", "AIO 未处理的消息类型, ");
                }
                if (item.Inlines.Count > 0)
                {
                    newItem.Blocks.Add(item);
                }
                if (paragraph4.Inlines.Count > 0)
                {
                    newItem.Blocks.Add(paragraph4);
                }
                box.ScrollToEnd();
            }
        }

        private void AddToImagesDownloadingList(Guid guid, ImageEx image)
        {
            if (this.imagesDownloading.ContainsKey(guid))
            {
                this.imagesDownloading[guid].Add(image);
            }
            else
            {
                List<ImageEx> list2 = new List<ImageEx> {
                image
            };
                this.imagesDownloading.Add(guid, list2);
            }
        }

        private void AddToUrlInfoDownloadingList(string url, ImageHyperlink imageHyperlink)
        {
            if (this.urlInfoDownloading.ContainsKey(url))
            {
                this.urlInfoDownloading[url].Add(imageHyperlink);
            }
            else
            {
                List<ImageHyperlink> list2 = new List<ImageHyperlink> {
                imageHyperlink
            };
                this.urlInfoDownloading.Add(url, list2);
            }
        }

        private void CanExecuteRoutedEvent(object sender, CanExecuteRoutedEventArgs e)
        {
            if ((sender == this) && ((e.Command == ApplicationCommands.Paste) && Clipboard.ContainsData(DataFormats.FileDrop)))
            {
                e.CanExecute = true;
                e.Handled = true;
            }
        }

        public bool CanSavePicAs()
        {
            return ((base.Selection != null) && (ReplaceControls.GetUserControls(base.Selection.Start, base.Selection.End).Count > 0));
        }

        private static bool CheckFileExists(Dictionary<string, bool> imagelist, string fileName)
        {
            bool flag = false;
            if (!imagelist.TryGetValue(fileName, out flag))
            {
                if (File.Exists(fileName))
                {
                    flag = true;
                }
                imagelist.Add(fileName, flag);
            }
            return flag;
        }

        private void CheckMsgPiece()
        {
            if (!this.IsMsgRecord && ((base.Document.Blocks != null) && (base.Document.Blocks.Count >= MaxPieces)))
            {
                while (base.Document.Blocks.Count > ReservePieces)
                {
                    base.Document.Blocks.Remove(base.Document.Blocks.FirstBlock);
                }
            }
        }

        public void ClearAll()
        {
            base.Document.Blocks.Clear();
            this.imagesDownloading.Clear();
            this.urlInfoDownloading.Clear();
        }

        public MessagePack CreateMessagePack()
        {
            int imageCount = 0;
            return this.CreateMessagePack(out imageCount);
        }

        public MessagePack CreateMessagePack(out int imageCount)
        {
            ImageElementNum = 0;
            imageCount = 0;
            //if (this.IsEmpty()==true)
            //{
            //    return null;
            //}
            BlockCollection blocks = base.Document.Blocks;
            //if (blocks.Count == 0)
            //{
            //    return null;
            //}
            MessagePack msgPack = new MessagePack
            {
                Header = { FontName = base.Document.FontFamily.ToString(), FontSize = (byte)(base.Document.FontSize - 3.0) }
            };
            SolidColorBrush foreground = base.Document.Foreground as SolidColorBrush;
            if (foreground != null)
            {
                msgPack.Header.FontColor = foreground.Color;
            }
            byte num = 0;
            if (base.Document.FontWeight == FontWeights.Bold)
            {
                num = (byte)(num | 1);
            }
            if (base.Document.FontStyle == FontStyles.Italic)
            {
                num = (byte)(num | 2);
            }
            if (this.Underline)
            {
                num = (byte)(num | 4);
            }
            msgPack.Header.FontEffect = num;
            bool flag = false;
            foreach (Block block in blocks)
            {
                if (flag)
                {
                    ((TextElement)msgPack.CreateElement(MsgPackCat.ELEMTYPE_TEXT)).SetText("\r\n");
                }
                else
                {
                    flag = true;
                }
                if (block is Paragraph)
                {
                    Paragraph paragraph = block as Paragraph;
                    ParseInlines(msgPack, paragraph.Inlines);
                }
                else if (block is BlockUIContainer)
                {
                    BlockUIContainer container = block as BlockUIContainer;
                    ImageEx child = container.Child as ImageEx;
                    if (child != null)
                    {
                        ParseImage(msgPack, child);
                    }
                }
            }
            ITXMsgPack xcdbca = CoreMessenger.Instance.MsgStorage.TransformMsg(msgPack.Key);
            imageCount = ImageElementNum;
            ImageElementNum = 0;
            return new MessagePack(xcdbca);
        }

        private static void DisabledImageClickStyle(ImageEx image)
        {
            image.IsEnabledClick = false;
            image.ToolTip = null;
            image.Cursor = null;
            if (image.Tag is ImageElement)
            {
                image.Tag = null;
            }
        }

        private void ExecutedRoutedEvent(object sender, ExecutedRoutedEventArgs e)
        {
            if ((((sender == this) && (e.Command == ApplicationCommands.Paste)) && !Clipboard.ContainsData(DataFormats.Bitmap)) && Clipboard.ContainsData(DataFormats.FileDrop))
            {
                string[] data = Clipboard.GetData(DataFormats.FileDrop) as string[];
                if (this.SendFile != null)
                {
                    this.SendFile(data);
                }
                e.Handled = true;
            }
        }

        public static DateTime GetDateTime(DependencyObject obj)
        {
            return (DateTime)obj.GetValue(DateTimeProperty);
        }

        private static ImageEx GetImage(IInputElement source)
        {
            Point position = Mouse.GetPosition(source);
            Visual reference = source as Visual;
            if (reference != null)
            {
                if (!VisualTreeHelper.GetDescendantBounds(reference).Contains(position))
                {
                    return null;
                }
                if (reference is ImageEx)
                {
                    return (ImageEx)reference;
                }
            }
            DependencyObject current = source as DependencyObject;
            if (current != null)
            {
                foreach (object obj3 in LogicalTreeHelper.GetChildren(current))
                {
                    IInputElement element = obj3 as IInputElement;
                    if (element != null)
                    {
                        ImageEx image = GetImage(element);
                        if (image != null)
                        {
                            return image;
                        }
                    }
                }
            }
            return null;
        }

        public ImageEx GetRightClickImage()
        {
            if (base.ContextMenu != null)
            {
                Point point = base.ContextMenu.PointToScreen(new Point(0.0, 0.0));
                Point point2 = base.PointFromScreen(point);
                IInputElement source = base.InputHitTest(point2);
                if (source != null)
                {
                    return GetImage(source);
                }
            }
            return null;
        }

        public int GetTextLength()
        {
            int num = 0;
            try
            {
                if (charOffsetPropertyInfo == null)
                {
                    Type type = typeof(TextPointer);
                    BindingFlags bindingAttr = BindingFlags.GetProperty | BindingFlags.NonPublic | BindingFlags.Instance;
                    charOffsetPropertyInfo = type.GetProperty("CharOffset", bindingAttr);
                }
                num = (int)charOffsetPropertyInfo.GetValue(base.Document.ContentEnd, null);
            }
            catch (Exception)
            {
            }
            return num;
        }

        private void InputBox_Copying(object sender, DataObjectCopyingEventArgs e)
        {
            using (new Util_Perf.FunLog("InputBox.InputBox_Copying"))
            {
                ClipboardMgr.GenerateClipBoardData(e, base.Selection);
            }
        }

        private void InputBox_ImageClicked(object sender, RoutedEventArgs args)
        {
            if (this.Uin != 0)
            {
                ImageEx source = args.Source as ImageEx;
                if (source.Tag is ImageElement)
                {
                    ImageElement tag = source.Tag as ImageElement;
                    ITXOfflinePicMgr service = CoreMessenger.Instance.GetService<ITXOfflinePicMgr>();
                    using (new ComObjectHelper<ITXOfflinePicMgr>(service))
                    {
                        if (File.Exists(tag.Path))
                        {
                            source.Source = tag.Path;
                        }
                        else
                        {
                            source.Source = CoreMessenger.Instance.GetAppPath(KernelWrapper.APP_PATH_TYPE.APP_PATH_DATA) + "sendingBmp.gif";
                            if (!Util_Buddy.IsOnlineStatus())
                            {
                                TXLog.TXLogImage("RecvSinglePic,接口调用失败 guid = " + tag.Id);
                                source.Source = CoreMessenger.Instance.GetAppPath(KernelWrapper.APP_PATH_TYPE.APP_PATH_FACE) + "errorBmp.gif";
                            }
                            else
                            {
                                TXLog.TXLogImage("RecvSinglePic,等待返回 guid = " + tag.Id);
                                service.RecvSinglePic(this.Uin, tag.TXMsgImage);
                                this.AddToImagesDownloadingList(tag.Id, source);
                            }
                        }
                        source.ToolTip = null;
                        source.Cursor = null;
                        if (source.Tag is ImageElement)
                        {
                            source.Tag = null;
                        }
                    }
                }
            }
        }

        private void InputBox_Loaded(object sender, RoutedEventArgs e)
        {
            base.Loaded -= new RoutedEventHandler(this.InputBox_Loaded);
            ContextMenu menu = new ContextMenu
            {
                FontSize = 12.0
            };
            MenuItem newItem = new MenuItem
            {
                Command = ApplicationCommands.Cut
            };
            menu.Items.Add(newItem);
            MenuItem item2 = new MenuItem
            {
                Command = ApplicationCommands.Copy
            };
            menu.Items.Add(item2);
            MenuItem item3 = new MenuItem
            {
                Command = ApplicationCommands.Paste
            };
            menu.Items.Add(item3);
            menu.Items.Add(this.saveAsMenuItem);
            this.saveAsMenuItem.CommandTarget = WindowHelper.MainFrame;
            this.saveAsMenuItem.CommandParameter = this;
            base.ContextMenu = menu;
        }

        private void InputBox_Pasting(object sender, DataObjectPastingEventArgs e)
        {
            base.BeginChange();
            try
            {
                using (new Util_Perf.FunLog("InputBox.InputBox_Pasting"))
                {
                    if (ClipboardMgr.PasteContentData(this, e.DataObject))
                    {
                        e.CancelCommand();
                        e.Handled = true;
                    }
                }
            }
            catch (Exception)
            {
            }
            base.EndChange();
        }

        protected void InputBox_Unloaded(object sender, RoutedEventArgs args)
        {
            this.ClearAll();
            base.Unloaded -= new RoutedEventHandler(this.InputBox_Unloaded);
            ComponentManager.GetGrayURLMgr().URLInfoUpdate -= new TXGrayURLMgr.OnURLInfoUpdateHandler(this.InputBox_URLInfoUpdate);
            base.RemoveHandler(DataObject.PastingEvent, this.pastingEventHandler);
            base.RemoveHandler(DataObject.CopyingEvent, this.copyingEventHandler);
            base.RemoveHandler(CommandManager.PreviewExecutedEvent, this.executedRoutedEventHandler);
            base.RemoveHandler(CommandManager.PreviewCanExecuteEvent, this.canExecuteRoutedEventHandler);
        }

        private void InputBox_URLInfoUpdate(string url, KernelWrapper.ITXDataRead pUrlInfo)
        {
            if (this.urlInfoDownloading.ContainsKey(url))
            {
                List<ImageHyperlink> list = this.urlInfoDownloading[url];
                foreach (ImageHyperlink hyperlink in list)
                {
                    this.SetURLInfo(hyperlink, pUrlInfo);
                }
                this.urlInfoDownloading.Remove(url);
            }
        }

        public void InsertEmoticon(string file, EmoticonItem emoticon)
        {
            ImageEx image = ReplaceControls.CreateImageEx(file, emoticon);
            this.InsertImage(image);
        }

        private void InsertImage(ImageEx image)
        {
            base.Selection.Text = "";
            TextPointer insertionPosition = base.CaretPosition.GetInsertionPosition(LogicalDirection.Forward);
            InlineUIContainer container = new InlineUIContainer(image, insertionPosition);
            insertionPosition = insertionPosition.GetNextContextPosition(LogicalDirection.Forward);
            base.CaretPosition = container.ElementEnd;
        }

        public bool IsEmpty()
        {
            return ((base.Document == null) || ((base.Document.Blocks == null) || ((base.Document.Blocks.Count == 0) || (this.GetTextLength() == 0))));
        }

        public bool LoadSettings(string prefix)
        {
            try
            {
                if (typeof(Util_UserSettings_ContactSessionWindow).Name == prefix)
                {
                    this.GlobalFontFamily = Util_UserSettings_ContactSessionWindow.FontFamily;
                    this.GlobalFontSize = Util_UserSettings_ContactSessionWindow.FontSize;
                    this.Bold = Util_UserSettings_ContactSessionWindow.Bold;
                    this.Italic = Util_UserSettings_ContactSessionWindow.Italic;
                    this.Underline = Util_UserSettings_ContactSessionWindow.Underline;
                    this.GlobalColor = Util_UserSettings_ContactSessionWindow.FontColor;
                }
                else if (typeof(Util_UserSettings_CommunitySessionWindow).Name == prefix)
                {
                    this.GlobalFontFamily = Util_UserSettings_CommunitySessionWindow.FontFamily;
                    this.GlobalFontSize = Util_UserSettings_CommunitySessionWindow.FontSize;
                    this.Bold = Util_UserSettings_CommunitySessionWindow.Bold;
                    this.Italic = Util_UserSettings_CommunitySessionWindow.Italic;
                    this.Underline = Util_UserSettings_CommunitySessionWindow.Underline;
                    this.GlobalColor = Util_UserSettings_CommunitySessionWindow.FontColor;
                }
                return true;
            }
            catch (Exception)
            {
                return false;
            }
        }

        private static void OnBoldChanged(DependencyObject d, DependencyPropertyChangedEventArgs e)
        {
            bool newValue = (bool)e.NewValue;
            InputBox box = (InputBox)d;
            box.FontWeight = newValue ? FontWeights.Bold : FontWeights.Normal;
            if (box.Document != null)
            {
                box.Document.FontWeight = newValue ? FontWeights.Bold : FontWeights.Normal;
            }
        }

        private static void OnGlobalColorChanged(DependencyObject d, DependencyPropertyChangedEventArgs e)
        {
            Color newValue = (Color)e.NewValue;
            InputBox box = (InputBox)d;
            box.Foreground = new SolidColorBrush(newValue);
            if (box.Document != null)
            {
                box.Document.Foreground = new SolidColorBrush(newValue);
            }
        }

        private static void OnGlobalFontFamilyChanged(DependencyObject d, DependencyPropertyChangedEventArgs e)
        {
            FontFamily newValue = (FontFamily)e.NewValue;
            InputBox box = (InputBox)d;
            box.FontFamily = newValue;
            if (box.Document != null)
            {
                box.Document.FontFamily = newValue;
            }
        }

        private static void OnGlobalFontSizeChanged(DependencyObject d, DependencyPropertyChangedEventArgs e)
        {
            double newValue = (double)e.NewValue;
            InputBox box = (InputBox)d;
            box.FontSize = newValue;
            if (box.Document != null)
            {
                box.Document.FontSize = newValue;
            }
        }

        private void OnImageHyperLinkAdd(IMMessage imMessage, ImageHyperlink hyperlink)
        {
            Guid guid = hyperlink.Guid;
            if (guid.Equals(MessageElementTags.GuidLinkSafePage) || guid.Equals(MessageElementTags.GuidLinkHttp))
            {
                TXGrayURLMgr grayURLMgr = ComponentManager.GetGrayURLMgr();
                ITXDataRead txData = grayURLMgr.QueryURLInfo(hyperlink.SoureUrl);
                if (txData != null)
                {
                    this.SetURLInfo(hyperlink, txData);
                }
                else
                {
                    GrayURL.QueryType eQueryType = GrayURL.QueryType.QueryType_Unknown;
                    uint uin = 0;
                    if (imMessage.Sender != null)
                    {
                        uin = imMessage.Sender.Uin;
                    }
                    if (uin == 0)
                    {
                        eQueryType = GrayURL.QueryType.QueryType_Unknown;
                    }
                    else if (Util_Buddy.GetCurrentBuddy().Uin == uin)
                    {
                        eQueryType = GrayURL.QueryType.QueryType_Sender;
                    }
                    else
                    {
                        eQueryType = GrayURL.QueryType.QueryType_Reciver;
                    }
                    GrayURL.MSGType msgType = this.IsCommunity ? GrayURL.MSGType.MSGType_Group : GrayURL.MSGType.MSGType_Buddy;
                    grayURLMgr.UpdateURLInfoEx(msgType, hyperlink.SoureUrl, eQueryType);
                    this.AddToUrlInfoDownloadingList(hyperlink.SoureUrl, hyperlink);
                }
            }
        }

        public bool OnImageTransferStatusChanged(ImageStatus imageStatus)
        {
            if (!this.imagesDownloading.ContainsKey(imageStatus.Id))
            {
                return false;
            }
            List<ImageEx> list = this.imagesDownloading[imageStatus.Id];
            if ((imageStatus.Status == C2CImageTransferTags.ImageStatus.IS_Recv_Suc) && File.Exists(imageStatus.Path))
            {
                TXLog.TXLogImage("图片下载 成功" + imageStatus.Path);
                foreach (ImageEx ex in list)
                {
                    ex.Source = imageStatus.Path;
                    DisabledImageClickStyle(ex);
                }
            }
            else
            {
                TXLog.TXLogImage("图片下载 失败" + imageStatus.Path);
                foreach (ImageEx ex2 in list)
                {
                    ex2.Source = CoreMessenger.Instance.GetAppPath(KernelWrapper.APP_PATH_TYPE.APP_PATH_DATA) + "errorBmp.gif";
                    DisabledImageClickStyle(ex2);
                }
            }
            if (base.CaretPosition.Parent != null)
            {
                TXLog.TXLogImage("InputBox.CaretPosition.Parent Type : " + base.CaretPosition.Parent.GetType().Name);
            }
            else
            {
                TXLog.TXLogImage("InputBox.CaretPosition.Parent == NULL");
            }
            if (base.CaretPosition.Parent is FrameworkElement)
            {
                (base.CaretPosition.Parent as FrameworkElement).BringIntoView();
            }
            else
            {
                base.ScrollToEnd();
            }
            this.imagesDownloading.Remove(imageStatus.Id);
            return true;
        }

        public bool OnImageTransferStatusChanged(Guid picguid, bool IsPicReceiveSuccess, string info)
        {
            TXLog.TXLogImage(string.Format("收到群图片 picguid = {0}; IsPicReceiveSuccess = {1}; info = {2} ", picguid, IsPicReceiveSuccess, info));
            if (this.imagesDownloading.ContainsKey(picguid))
            {
                List<ImageEx> list = this.imagesDownloading[picguid];
                if (list.Count > 0)
                {
                    string path = (list[0].Tag as ImageElement).Path;
                    bool flag = File.Exists(path);
                    foreach (ImageEx ex in list)
                    {
                        if (IsPicReceiveSuccess && flag)
                        {
                            ex.Source = path;
                        }
                        else
                        {
                            ex.Source = CoreMessenger.Instance.GetAppPath(KernelWrapper.APP_PATH_TYPE.APP_PATH_DATA) + "errorBmp.gif";
                        }
                        DisabledImageClickStyle(ex);
                    }
                }
                this.imagesDownloading.Remove(picguid);
                return true;
            }
            TXLog.TXLog3("群图片", "收到群图片 没找到对应的guid");
            return false;
        }

        protected override void OnInitialized(EventArgs e)
        {
            base.AllowDrop = true;
            base.OnInitialized(e);
            base.Unloaded += new RoutedEventHandler(this.InputBox_Unloaded);
            this.pastingEventHandler = new DataObjectPastingEventHandler(this.InputBox_Pasting);
            this.copyingEventHandler = new DataObjectCopyingEventHandler(this.InputBox_Copying);
            base.AddHandler(DataObject.PastingEvent, this.pastingEventHandler, true);
            base.AddHandler(DataObject.CopyingEvent, this.copyingEventHandler, true);
            this.clickedEventHandler = new ImageEx.ClickedEventHandler(this.InputBox_ImageClicked);
            base.AddHandler(ImageEx.ClickedEvent, this.clickedEventHandler, false);
            base.FontFamily = defaultFontFamily;
            base.FontSize = 12.0;
            this.executedRoutedEventHandler = new ExecutedRoutedEventHandler(this.ExecutedRoutedEvent);
            this.canExecuteRoutedEventHandler = new CanExecuteRoutedEventHandler(this.CanExecuteRoutedEvent);
            base.AddHandler(CommandManager.PreviewExecutedEvent, this.executedRoutedEventHandler, true);
            base.AddHandler(CommandManager.PreviewCanExecuteEvent, this.canExecuteRoutedEventHandler, true);
        }

        private static void OnItalicChanged(DependencyObject d, DependencyPropertyChangedEventArgs e)
        {
            bool newValue = (bool)e.NewValue;
            InputBox box = (InputBox)d;
            box.FontStyle = newValue ? FontStyles.Italic : FontStyles.Normal;
            if (box.Document != null)
            {
                box.Document.FontStyle = newValue ? FontStyles.Italic : FontStyles.Normal;
            }
        }

        private static void OnUnderlineChanged(DependencyObject d, DependencyPropertyChangedEventArgs e)
        {
            bool newValue = (bool)e.NewValue;
            InputBox box = (InputBox)d;
            if (newValue)
            {
                Style style = new Style(typeof(Run))
                {
                    Setters = { new Setter(Inline.TextDecorationsProperty, TextDecorations.Underline) }
                };
                box.Resources.Add(typeof(Run), style);
            }
            else
            {
                box.Resources.Clear();
            }
        }

        public static void ParseImage(MessagePack msgPack, ImageEx image)
        {
            EmoticonItem tag = image.Tag as EmoticonItem;
            if (tag.IsSysEmoticon)
            {
                SysFaceElement element = (SysFaceElement)msgPack.CreateElement(MsgPackCat.ELEMTYPE_SYSFACE);
                element.Index = Convert.ToByte(tag.Id);
            }
            else
            {
                ImageElement element2 = (ImageElement)msgPack.CreateElement(MsgPackCat.ELEMTYPE_IMAGE);
                element2.Path = "OSRoot:" + tag.Fileorg;
                ImageElementNum++;
            }
        }

        public static void ParseInlines(MessagePack msgPack, InlineCollection inlines)
        {
            foreach (Inline inline in inlines)
            {
                if (inline is Run)
                {
                    ParseRun(msgPack, (Run)inline);
                }
                else if (inline is Span)
                {
                    ParseSpan(msgPack, (Span)inline);
                }
                else if (inline is LineBreak)
                {
                    ParseLineBreak(msgPack, (LineBreak)inline);
                }
                else if (inline is InlineUIContainer)
                {
                    ParseInlineUIContainer(msgPack, (InlineUIContainer)inline);
                }
            }
        }

        public static void ParseInlineUIContainer(MessagePack msgPack, InlineUIContainer inlineUIContainer)
        {
            ImageEx child = inlineUIContainer.Child as ImageEx;
            if (child != null)
            {
                ParseImage(msgPack, child);
            }
        }

        public static void ParseLineBreak(MessagePack msgPack, LineBreak lineBreak)
        {
            ((TextElement)msgPack.CreateElement(MsgPackCat.ELEMTYPE_TEXT)).SetText("\r\n");
        }

        public static void ParseRun(MessagePack msgPack, Run run)
        {
            string text = run.Text;
            if (!string.IsNullOrEmpty(text))
            {
                ((TextElement)msgPack.CreateElement(MsgPackCat.ELEMTYPE_TEXT)).SetText(text);
            }
        }

        public static void ParseSpan(MessagePack msgPack, Span span)
        {
            ParseInlines(msgPack, span.Inlines);
        }

        public void Paste(IDataObject dataObject)
        {
            try
            {
                ImageSource data = dataObject.GetData(DataFormats.Bitmap, true) as ImageSource;
                if (data != null)
                {
                    string file = Helper_Icon.CreateTempImageFile(data);
                    this.InsertEmoticon(file, null);
                }
            }
            catch (Exception)
            {
            }
        }

        public void RefreshBubble()
        {
            if (base.Document != null)
            {
                foreach (Block block in base.Document.Blocks)
                {
                    Section section = block as Section;
                    if (((section != null) && (section.Background == null)) && (section.Tag != null))
                    {
                        TextPointer elementStart = section.ElementStart;
                        TextPointer elementEnd = section.ElementEnd;
                        Point topLeft = elementStart.GetCharacterRect(elementStart.LogicalDirection).TopLeft;
                        double height = (elementEnd.GetCharacterRect(elementEnd.LogicalDirection).BottomRight.Y - topLeft.Y) + 8.0;
                        if (height > 0.0)
                        {
                            RectangleGeometry geometry = new RectangleGeometry(new Rect(18.0, 0.0, 375.0, height), 5.0, 5.0);
                            if (section.Tag.ToString() == "me")
                            {
                                section.Background = new DrawingBrush(new GeometryDrawing((Brush)new BrushConverter().ConvertFromString("#FFFCFEFB"), new Pen((Brush)new BrushConverter().ConvertFromString("#FFD4DBD4"), 1.0), geometry));
                            }
                            else if (section.Tag.ToString() == "other")
                            {
                                section.Background = new DrawingBrush(new GeometryDrawing((Brush)new BrushConverter().ConvertFromString("#FFF2F8FC"), new Pen((Brush)new BrushConverter().ConvertFromString("#FFD3E0E6"), 1.0), geometry));
                            }
                        }
                    }
                }
            }
        }

        public bool SaveSettings(string prefix)
        {
            try
            {
                if (typeof(Util_UserSettings_ContactSessionWindow).Name == prefix)
                {
                    Util_UserSettings_ContactSessionWindow.FontFamily = this.GlobalFontFamily;
                    Util_UserSettings_ContactSessionWindow.FontSize = (int)this.GlobalFontSize;
                    Util_UserSettings_ContactSessionWindow.Bold = this.Bold;
                    Util_UserSettings_ContactSessionWindow.Italic = this.Italic;
                    Util_UserSettings_ContactSessionWindow.Underline = this.Underline;
                    Util_UserSettings_ContactSessionWindow.FontColor = this.GlobalColor;
                }
                else if (typeof(Util_UserSettings_CommunitySessionWindow).Name == prefix)
                {
                    Util_UserSettings_CommunitySessionWindow.FontFamily = this.GlobalFontFamily;
                    Util_UserSettings_CommunitySessionWindow.FontSize = (int)this.GlobalFontSize;
                    Util_UserSettings_CommunitySessionWindow.Bold = this.Bold;
                    Util_UserSettings_CommunitySessionWindow.Italic = this.Italic;
                    Util_UserSettings_CommunitySessionWindow.Underline = this.Underline;
                    Util_UserSettings_CommunitySessionWindow.FontColor = this.GlobalColor;
                }
                return true;
            }
            catch (Exception)
            {
                return false;
            }
        }

        public static void SetDateTime(DependencyObject obj, DateTime value)
        {
            obj.SetValue(DateTimeProperty, value);
        }

        private void SetURLInfo(ImageHyperlink hyperlink, KernelWrapper.ITXDataRead txData)
        {
            GrayURL.URLType dWord = (GrayURL.URLType)TXDataHelper.GetDWord(txData, "eURLType");
            bool @bool = TXDataHelper.GetBool(txData, "bShowURLReportNum");
            string appPath = CoreMessenger.Instance.GetAppPath(KernelWrapper.APP_PATH_TYPE.GlobalSys_Path_Misc);
            string path = null;
            bool flag2 = false;
            switch (dWord)
            {
                case GrayURL.URLType.URLType_Gray:
                    if (!@bool)
                    {
                        path = appPath + @"Safe\main_QQdoctortip14_help.png";
                        flag2 = true;
                    }
                    else
                    {
                        path = appPath + @"Safe\main_QQdoctortip14_attention.png";
                    }
                    break;

                case GrayURL.URLType.URLType_Black:
                    path = appPath + @"Safe\main_QQdoctortip14_alert.png";
                    break;

                case GrayURL.URLType.URLType_TencentWhite:
                    path = appPath + @"Safe\main_tencent14_normal.png";
                    flag2 = true;
                    break;

                case GrayURL.URLType.URLType_NonTencentWhite:
                    path = appPath + @"Safe\main_QQdoctortip14_good.png";
                    flag2 = true;
                    break;

                default:
                    path = appPath + @"Safe\main_QQdoctortip14_help.png";
                    break;
            }
            if (!flag2)
            {
                hyperlink.DisabledHyperLink();
            }
            ushort word = TXDataHelper.GetWord(txData, "wURLTipsID");
            string tips = ComponentManager.GetGrayURLMgr().QueryURLTips(word);
            hyperlink.InsertImage(path);
            hyperlink.SetToolTip(tips);
        }

        // Properties
        public bool Bold
        {
            get
            {
                return (bool)base.GetValue(BoldProperty);
            }
            set
            {
                base.SetValue(BoldProperty, value);
            }
        }

        public Color GlobalColor
        {
            get
            {
                return (Color)base.GetValue(GlobalColorProperty);
            }
            set
            {
                base.SetValue(GlobalColorProperty, value);
            }
        }

        public FontFamily GlobalFontFamily
        {
            get
            {
                return (FontFamily)base.GetValue(GlobalFontFamilyProperty);
            }
            set
            {
                base.SetValue(GlobalFontFamilyProperty, value);
            }
        }

        public double GlobalFontSize
        {
            get
            {
                return (double)base.GetValue(GlobalFontSizeProperty);
            }
            set
            {
                base.SetValue(GlobalFontSizeProperty, value);
            }
        }

        public bool IsCommunity { get; set; }

        public bool IsMsgRecord { get; set; }

        public bool Italic
        {
            get
            {
                return (bool)base.GetValue(ItalicProperty);
            }
            set
            {
                base.SetValue(ItalicProperty, value);
            }
        }

        public FlowDocument TempFlowDocument
        {
            get
            {
                return this.tempFlowDocument;
            }
        }

        public uint Uin { get; set; }

        public bool Underline
        {
            get
            {
                return (bool)base.GetValue(UnderlineProperty);
            }
            set
            {
                base.SetValue(UnderlineProperty, value);
            }
        }

        // Nested Types
        public delegate void AddMsgToOutputBoxCallBackHandler(IMMessage imMessage, object element);

        public delegate void SendFileEventHandler(string[] fileList);
    }
}
