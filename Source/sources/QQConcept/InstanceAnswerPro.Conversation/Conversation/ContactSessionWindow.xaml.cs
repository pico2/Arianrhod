using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using InstanceAnswerPro.Core;
using TextElement = InstanceAnswerPro.Core.TextElement;
using InstanceAnswerPro.IM.Controls;

namespace InstanceAnswerPro.Conversation
{
    public partial class ContactSessionWindow : Window, IMessageProcessor
    {
        private Buddy _buddyWhenWindowCreated;
        private static List<ContactSessionWindow> ContactSessionWindows = new List<ContactSessionWindow>();
        private SessionTabItem draggingBuddy;
        private bool initXaml;
        private ObservableCollection<SessionTabItem> sessionTabItems;

        private ContactSessionWindow()
        {
            this.sessionTabItems = new ObservableCollection<SessionTabItem>();
            this.initXaml = true;
            this.InitializeComponent();
        }

        public ContactSessionWindow(SessionTabItem sessionTabItem)
        {
            RoutedEventHandler handler = null;
            this.sessionTabItems = new ObservableCollection<SessionTabItem>();
            this._buddyWhenWindowCreated = sessionTabItem.Buddy;
            base.Unloaded += new RoutedEventHandler(this.ContactSessionWindow_Unloaded);
            this.InitializeComponent();
            ContactSessionWindows.Add(this);
            CoreMessenger.Instance.MessageCenter.AddMessageProcessor(this);
            this.AddSession(sessionTabItem);
            if (handler == null)
            {
                handler = delegate
                {
                    //if (this.sessionsControl.ShouldLoseFocus)
                    //{
                    //    this.SetFocusOnInputBoxWithDelay();
                    //}
                    //this.sessionsControl.ShouldLoseFocus = false;
                };
            }
            // this.sessionsControl.AddHandler(UIElement.GotFocusEvent, handler);
        }

        public ContactSessionWindow(ContactSession session, MessagePack messagePack, bool openFromDesktopBuddy)
            : this(new SessionTabItem(session))
        {
            if (messagePack != null)
            {
                Buddy sender = ComponentManager.GetBuddyListBuilder().FindOrCreateBuddy(session.Uin, true);
                this.CurrentIMSession.AddMsg(sender, messagePack.Header.Time, messagePack);
            }
        }

        public static bool ActiveSessionWhenExist(uint uin)
        {
            return ActiveSessionWhenExist(uin, null);
        }

        public static bool ActiveSessionWhenExist(uint uin, Point? mousePosition)
        {
            for (int i = 0; i < ContactSessionWindows.Count; i++)
            {
                SessionTabItem item = ContactSessionWindows[i].FindIMSession(uin);
                if (item != null)
                {
                    ContactSessionWindow window = ContactSessionWindows[i];
                    if (window.WindowState == WindowState.Minimized)
                    {
                        window.WindowState = WindowState.Normal;
                    }
                    ContactSessionWindows[i].Activate();
                    ContactSessionWindows[i].CurrentIMSession = item;
                    return true;
                }
            }
            return false;
        }

        private void AddMsgToOutputBox(IMMessage imMessage)
        {
            string senderName = (imMessage.Sender != null) ? imMessage.Sender.NickName : null;
            this.OutputBox.AddMsgToOutputBox(imMessage, senderName, new InputBox.AddMsgToOutputBoxCallBackHandler(this.AddMsgToOutputBoxCallBack));
            IMMessage blockURLWarningMsg = Util_Misc.GetBlockURLWarningMsg(imMessage.MessagePack.Header, this.OutputBox.IsCommunity);
            if (blockURLWarningMsg != null)
            {
                this.OutputBox.AddMsgToOutputBox(blockURLWarningMsg, senderName, null);
            }
        }




        private void AddMsgToOutputBoxCallBack(IMMessage imMessage, object element)
        {
            if (!imMessage.AvatarProcessed)
            {
                SysFaceElement element2 = element as SysFaceElement;
                imMessage.AvatarProcessed = true;
                if ((element2.Index == 11) && (imMessage.Sender.Uin == this.CurrentIMSession.Buddy.Uin))
                {
                    //this.PlayAvatar("Bama.QQ.Controls.AvatarFire");
                }
                else if (element2.Index == 0x26)
                {
                    if (imMessage.Sender.Uin != this.CurrentIMSession.Buddy.Uin)
                    {
                        //this.PlayAvatar("Bama.QQ.Controls.AvatarHammer");
                    }
                    else if (base.WindowState == WindowState.Normal)
                    {
                        //base.BeginStoryboard(base.FindResource("big_hammer") as Storyboard);
                        //base.BeginStoryboard(base.FindResource("beaten") as Storyboard);
                    }
                }
            }
        }

        public void AddSession(SessionTabItem sessionTabItem)
        {
            sessionTabItem.MessageIndex = 0;
            sessionTabItem.MessageAdded += new EventHandler<EventArgs>(this.OnMessageAdded);
            if (sessionTabItem.InputBoxDocument == null)
            {
                sessionTabItem.InputBoxDocument = new FlowDocument();
            }
            this.sessionTabItems.Add(sessionTabItem);
            this.CurrentIMSession = sessionTabItem;
            this.NotifyAIOSessionEvent("AIO_AddSession", (this.CurrentIMSession != null) ? this.CurrentIMSession.Buddy : null);
            ComponentManager.GetBuddyManager().Info.Refresh(this.CurrentIMSession.Buddy.Uin, IMContactInfoCat.QQInfo);
        }


        public bool BamaWindowEventProc(WindowEvent windowEvent, object parameter1, object parameter2, out object resultObj)
        {
            resultObj = null;
            if (windowEvent == WindowEvent.FindWindow)
            {
                if ((parameter1 is Buddy) && (this.CurrentIMSession != null))
                {
                    uint uin = (parameter1 as Buddy).Uin;
                    foreach (SessionTabItem item in this.sessionTabItems)
                    {
                        if ((item.Buddy != null) && (item.Buddy.Uin == uin))
                        {
                            resultObj = this;
                            return true;
                        }
                    }
                }
            }
            else if (windowEvent == WindowEvent.OnCapture)
            {
                //if ((bool)parameter1)
                //{
                //    this.InputBox.Paste(Clipboard.GetDataObject());
                //}
                //else
                //{
                //    this.InputBox.Focus();
                //}
            }
            return false;
        }

        private void CaptureButton_Click(object sender, RoutedEventArgs e)
        {
            Util_DataReport.RID_Count_AIO_Capture();
            Util_Capture.CameraScreen();
        }

        private void clearButton_Click(object sender, RoutedEventArgs e)
        {
            Util_DataReport.RID_Count_AIO_ClearMsg();
            this.CurrentIMSession.IMMessageList.Clear();
            this.CurrentIMSession.MessageIndex = 0;
            this.OutputBox.Text = "";
        }

        public static bool CloseSessionWhenExist(uint uin)
        {
            for (int i = 0; i < ContactSessionWindows.Count; i++)
            {
                SessionTabItem sessionTabItem = ContactSessionWindows[i].FindIMSession(uin);
                if (sessionTabItem != null)
                {
                    ContactSessionWindows[i].ReleaseSession(sessionTabItem, true);
                    return true;
                }
            }
            return false;
        }

        private void CloseWindow_CanExecute(object sender, CanExecuteRoutedEventArgs args)
        {
            args.CanExecute = true;
        }

        private void CloseWindow_Executed(object sender, ExecutedRoutedEventArgs args)
        {
            base.Close();
        }

        private void ContactSessionWindow_Unloaded(object sender, RoutedEventArgs e)
        {
            base.Unloaded -= new RoutedEventHandler(this.ContactSessionWindow_Unloaded);
            //this.InputBox.SaveSettings(typeof(Util_UserSettings_ContactSessionWindow).Name);
            ContactSessionWindows.Remove(this);
            CoreMessenger.Instance.MessageCenter.RemoveMessageProcessor(this);
            Buddy buddy = null;
            if (this.CurrentIMSession != null)
            {
                buddy = this.CurrentIMSession.Buddy;
            }
            foreach (SessionTabItem item in this.sessionTabItems)
            {
                item.Close();
            }
            this.sessionTabItems.Clear();
        }

        private static Section CreateUICtrlMsg(UIControlMessage uiControlMsg)
        {
            Section section = new Section();
            string iconPath = uiControlMsg.IconPath;
            Paragraph item = new Paragraph
            {
                Foreground = Brushes.DimGray
            };
            Paragraph paragraph2 = new Paragraph
            {
                Margin = new Thickness(19.0, 0.0, 0.0, 0.0)
            };
            if (!string.IsNullOrEmpty(iconPath))
            {
                Image uiElement = new Image
                {
                    Width = 16.0,
                    Height = 16.0,
                    HorizontalAlignment = HorizontalAlignment.Left,
                    VerticalAlignment = VerticalAlignment.Top,
                    Stretch = Stretch.None,
                    SnapsToDevicePixels = true,
                    Source = new BitmapImage(new Uri(iconPath, UriKind.RelativeOrAbsolute))
                };
                item.Inlines.Add(uiElement);
                item.Inlines.Add(uiControlMsg.Title);
                section.Blocks.Add(item);
            }
            UIElement uIControl = uiControlMsg.UIControl;
            paragraph2.Inlines.Add(uIControl);
            section.Blocks.Add(paragraph2);
            return section;
        }

        public SessionTabItem FindIMSession(ContactSession session)
        {
            foreach (SessionTabItem item in this.sessionTabItems)
            {
                if (item.ContactSession == session)
                {
                    return item;
                }
            }
            return null;
        }

        public SessionTabItem FindIMSession(uint uin)
        {
            foreach (SessionTabItem item in this.sessionTabItems)
            {
                if (item.ContactSession.Uin == uin)
                {
                    return item;
                }
            }
            return null;
        }

        public bool ForceClose()
        {
            return false;
        }

        public static void InitXaml()
        {
            new ContactSessionWindow();
        }

        private void InputBox_PreviewKeyDown(object sender, KeyEventArgs e)
        {
            if (e.Key == Key.Return)
            {
                bool flag = Keyboard.IsKeyDown(Key.LeftCtrl) || Keyboard.IsKeyDown(Key.RightCtrl);
                bool flag2 = Keyboard.IsKeyDown(Key.LeftShift) || Keyboard.IsKeyDown(Key.RightShift);
                if (!Util_UserSettings_ContactSessionWindow.SendByEnter)
                {
                    if (flag && !flag2)
                    {
                        this.SendMsg();
                        this.InputBox.Focus();
                        e.Handled = true;
                    }
                }
                else if (!flag && !flag2)
                {
                    this.SendMsg();
                    this.InputBox.Focus();
                    e.Handled = true;
                }
                else if (flag)
                {
                    EditingCommands.EnterParagraphBreak.Execute(null, this.InputBox);
                    e.Handled = true;
                }
            }
            else if (e.SystemKey == Key.S)
            {
                this.SendMsg();
                this.InputBox.Focus();
                e.Handled = true;
            }
        }

        private void NotifyAIOSessionEvent(string aioHandle, Buddy buddy)
        {
            UICommandMessage message = new UICommandMessage("AIOSession", aioHandle, new UICommand.Parameter2.AIOSessionEventInfo(this, buddy));
            CoreMessenger.Instance.MessageCenter.NotifyMessage(message);
        }

        public static void OnImageTransferStatusChanged(ImageTransferStatusChangedrEventArgs args)
        {
            IList<InstanceAnswerPro.Core.ImageStatus> statusList = args.StatusList;
            int count = statusList.Count;
            TXLog.TXLogImage("图片下载 返回，个数 = " + count);
            for (int i = 0; i < ContactSessionWindows.Count; i++)
            {
                if (ContactSessionWindows[i].FindIMSession(args.TargetUin) != null)
                {
                    for (int j = 0; j < count; j++)
                    {
                        //ContactSessionWindows[i].OutputBox.OnImageTransferStatusChanged(statusList[j]);
                    }
                    return;
                }
            }
        }

        /// <summary>
        /// 初始化联系人回话窗口
        /// </summary>
        /// <param name="e"></param>
        protected override void OnInitialized(EventArgs e)
        {
            base.OnInitialized(e);
            if (!this.initXaml)
            {
                base.AddHandler(Bama.Controls.TabItem.DeleteEvent, new RoutedEventHandler(this.OnTabItemDeleted));
                //this.sessionsControl.SelectionChanged += new SelectionChangedEventHandler(this.OnSelectedTabItemChanged);
                this.send.Click += new RoutedEventHandler(this.OnSendButtonClicked);
                //this.sessionsControl.ItemsSource = this.sessionTabItems;
                //this.InputBox.LoadSettings(typeof(Util_UserSettings_ContactSessionWindow).Name);
            }
        }

        public void OnMessageAdded(object sender, EventArgs args)
        {
            SessionTabItem item = (SessionTabItem)sender;
            if (item == this.CurrentIMSession)
            {
                this.RefreshOutputBox();
            }
            else
            {
                item.HasNewMessage = true;
            }
        }

        public void OnMessagePopped(Message message)
        {
        }

        public void OnMessagePushed(Message message)
        {
        }

        public void OnNotifyMessage(Message message)
        {
            if (message.Type == InstanceAnswerPro.Core.MessageType.UIControlMessage)
            {
                UIControlMessage uiControlMsg = message as UIControlMessage;
                if (((this.CurrentIMSession != null) && (uiControlMsg.Uin == this.CurrentIMSession.Buddy.Uin)) && ("ContactSessionWindow" == (uiControlMsg.Parameter as string)))
                {
                    Section item = CreateUICtrlMsg(uiControlMsg);
                    //if (this.OutputBox.Document.Blocks.FirstBlock == null)
                    //{
                    //    this.OutputBox.Document.Blocks.Add(item);
                    //}
                    //else
                    //{
                    //    this.OutputBox.Document.Blocks.InsertBefore(this.OutputBox.Document.Blocks.FirstBlock, item);
                    //}
                    //this.OutputBox.ScrollToEnd();
                }
            }
        }

        internal void OnSelectedTabItemChanged(object sender, RoutedEventArgs e)
        {
            //SessionTabItem selectedItem = this.sessionsControl.SelectedItem as SessionTabItem;
            //if (selectedItem != null)
            //{
            //    uint uin = selectedItem.Buddy.Uin;
            //    this.OutputBox.Uin = uin;
            //    this.InputBox.Uin = uin;
            //    this.OutputBox.IsCommunity = false;
            //    this.InputBox.IsCommunity = false;
            //    //this.msgRecordPanel.MsgType = MsgTypeTags.Buddy;
            //    //this.msgRecordPanel.Uin = uin;
            //    //this.LayoutRoot.DataContext = selectedItem.Buddy;
            //    //this.avatar.Buddy = selectedItem.Buddy;
            //    //this.expandbar.DataContext = selectedItem.Buddy;
            //    base.Title = string.Format("{0} - 会话窗口", selectedItem.Buddy.NickName);
            //    this.InputBox.Document = selectedItem.InputBoxDocument;
            //    selectedItem.MessageIndex = 0;
            //    this.OutputBox.ClearAll();
            //    this.RefreshOutputBox();
            //    this.NotifyAIOSessionEvent("AIO_SelectionChanged", (selectedItem != null) ? selectedItem.Buddy : null);
            //}
            //else
            //{
            //    this.InputBox.Document = new FlowDocument();
            //    this.NotifyAIOSessionEvent("AIO_SelectionChanged", (selectedItem != null) ? selectedItem.Buddy : null);
            //}
        }

        /// <summary>
        /// 点击发送
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void OnSendButtonClicked(object sender, RoutedEventArgs e)
        {
            this.SendMsg();
            this.InputBox.Focus();
        }

        internal void OnTabItemDeleted(object sender, RoutedEventArgs e)
        {
            //if (this.sessionsControl.ItemsSource != null)
            //{
            //    Bama.Controls.TabItem originalSource = e.OriginalSource as Bama.Controls.TabItem;
            //    if (originalSource != null)
            //    {
            //        SessionTabItem sessionTabItem = (SessionTabItem)this.sessionsControl.ItemContainerGenerator.ItemFromContainer(originalSource);
            //        if (sessionTabItem != null)
            //        {
            //            this.ReleaseSession(sessionTabItem, true);
            //        }
            //    }
            //}
        }

        public void OnViewMessage(Message message)
        {
        }


        /// <summary>
        /// 接收消息
        /// </summary>
        /// <param name="session"></param>
        /// <param name="message"></param>
        public void ReceiveMessage(ContactSession session, Message message)
        {
            try
            {
                if (message.Type == InstanceAnswerPro.Core.MessageType.ContactMessage)
                {
                    ContactMessage message2 = message as ContactMessage;
                    Buddy sender = ComponentManager.GetBuddyListBuilder().FindOrCreateBuddy(message2.Uin, true);
                    SessionTabItem item = this.FindIMSession(session);
                    if ((sender != null) && (item != null))
                    {
                        item.AddMsg(sender, message2.Time, message2.MessagePack);
                    }
                }
                else if (message.Type == InstanceAnswerPro.Core.MessageType.InfoMessage)
                {
                    InfoMessage message3 = message as InfoMessage;
                    SessionTabItem item2 = this.FindIMSession(session);
                    if (item2 != null)
                    {
                        item2.AddMsg(null, message3.Time, message3.MessagePack);
                    }
                }
            }
            catch (Exception)
            {
            }
        }

        /// <summary>
        /// 刷新输出
        /// </summary>
        private void RefreshOutputBox()
        {
            if (this.CurrentIMSession != null)
            {
                this.CurrentIMSession.HasNewMessage = false;
                ArrayList iMMessageList = this.CurrentIMSession.IMMessageList;
                int count = iMMessageList.Count;
                for (int i = this.CurrentIMSession.MessageIndex; i < count; i++)
                {
                    IMMessage imMessage = (IMMessage)iMMessageList[i];
                    this.AddMsgToOutputBox(imMessage);
                }
                this.CurrentIMSession.MessageIndex = count;
            }
            ConversationModule.FlashConversationWindow(this);
        }

        /// <summary>
        /// 释放session
        /// </summary>
        /// <param name="sessionTabItem"></param>
        /// <param name="close"></param>
        public void ReleaseSession(SessionTabItem sessionTabItem, bool close)
        {
            if (sessionTabItem == null)
            {
                throw new ArgumentNullException("sessionTabItem");
            }
            if (close)
            {
                sessionTabItem.Close();
            }
            sessionTabItem.MessageAdded -= new EventHandler<EventArgs>(this.OnMessageAdded);
            if (this.sessionTabItems.Contains(sessionTabItem))
            {
                this.sessionTabItems.Remove(sessionTabItem);
                if (this.sessionTabItems.Count > 0)
                {
                    this.CurrentIMSession = this.sessionTabItems[0];
                }
                else
                {
                    this.CurrentIMSession = null;
                    base.Close();
                }
            }
            this.NotifyAIOSessionEvent("AIO_ReleaseSession", (sessionTabItem != null) ? sessionTabItem.Buddy : null);
        }

        /// <summary>
        /// 发送消息
        /// </summary>
        private void SendMsg()
        {
            if (!Util_Buddy.IsOnlineStatus())
            {
                Util_Misc.NotifyMsgToConversation(this.CurrentIMSession.Buddy.Uin, false, CoreMessenger.Instance.MiscHelper.TXLoadString("CF_SELF_OFFLINE"));
            }
            else if (this.InputBox.Text.Length > 0x1194)
            {
                Util_Misc.NotifyMsgToConversation(this.CurrentIMSession.Buddy.Uin, false, CoreMessenger.Instance.MiscHelper.TXLoadString("CF_EDITMSG_LARGE_MESSAGE"));
            }
            else
            {
                MessagePack messagePack = CreateMessagePack();
                if ((messagePack != null) && (this.CurrentIMSession != null))
                {
                    this.CurrentIMSession.SendMessage(messagePack);
                    Buddy currentBuddy = Util_Buddy.GetCurrentBuddy();
                    this.CurrentIMSession.AddMsg(currentBuddy, TimeConverter.Now, messagePack);
                    try
                    {
                        this.InputBox.Text = "";
                    }
                    catch (Exception)
                    {
                    }
                }
            }
        }

        /// <summary>
        /// 创建消息包
        /// </summary>
        /// <returns></returns>
        public MessagePack CreateMessagePack()
        {
            MessagePack msgPack = new MessagePack
            {
                Header = { FontName = this.InputBox.FontFamily.ToString(), FontSize = (byte)(this.InputBox.FontSize - 3.0) }
            };
            SolidColorBrush foreground = this.InputBox.Foreground as SolidColorBrush;
            if (foreground != null)
            {
                msgPack.Header.FontColor = foreground.Color;
            }
            byte num = 0;
            if (this.InputBox.FontWeight == FontWeights.Bold)
            {
                num = (byte)(num | 1);
            }
            if (this.InputBox.FontStyle == FontStyles.Italic)
            {
                num = (byte)(num | 2);
            }
            if (true)//Underline
            {
                num = (byte)(num | 4);
            }
            msgPack.Header.FontEffect = num;

            if (!string.IsNullOrEmpty(this.InputBox.Text))
            {
                ((TextElement)msgPack.CreateElement(MsgPackCat.ELEMTYPE_TEXT)).SetText(this.InputBox.Text);
            }
            return new MessagePack(CoreMessenger.Instance.MsgStorage.TransformMsg(msgPack.Key));
        }
        private void SetFocusOnInputBoxWithDelay()
        {
            base.Dispatcher.BeginInvoke(new Action(delegate
            {
                if (base.IsActive)
                {
                    this.InputBox.Focus();
                }
            }), new object[0]);
        }

        public void ShowDropPreview(Buddy buddy)
        {
            base.Activate();
            //this.sessionsControl.ShowDropPreview();
            if ((this.draggingBuddy == null) || (this.draggingBuddy.Buddy != buddy))
            {
                this.draggingBuddy = new SessionTabItem(buddy);
                this.sessionTabItems.Add(this.draggingBuddy);
            }
        }

        public void StopDropPreview()
        {
            //this.sessionsControl.StopDropPreview();
            if ((this.draggingBuddy != null) && this.sessionTabItems.Contains(this.draggingBuddy))
            {
                this.sessionTabItems.Remove(this.draggingBuddy);
            }
            this.draggingBuddy = null;
        }
        private void TextBlock_MouseLeftButtonUp(object sender, MouseButtonEventArgs e)
        {
            if (sender is TextBlock)
            {
                TextBlock block = sender as TextBlock;
                Util_Buddy.OpenProfileWindow((uint)block.Tag);
            }
        }

        public SessionTabItem CurrentIMSession
        {
            get;
            set;
            //get
            //{
            //    return (this.sessionsControl.SelectedItem as SessionTabItem);
            //}
            //set
            //{
            //    if (value != this.sessionsControl.SelectedItem)
            //    {
            //        this.sessionsControl.SelectedItem = value;
            //    }
            //}
        }


        public InstanceAnswerPro.Core.MessageType MessageType
        {
            get
            {
                return InstanceAnswerPro.Core.MessageType.UIControlMessage;
            }
        }

        public int SessionCount
        {
            get
            {
                return this.sessionTabItems.Count;
            }
        }

        public object WindowCreatedParam1
        {
            get
            {
                return this._buddyWhenWindowCreated;
            }
        }

        public object WindowCreatedParam2
        {
            get
            {
                return null;
            }
        }
    }
}
