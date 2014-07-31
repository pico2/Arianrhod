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
using InstanceAnswerPro.Core.Community;
using System.Collections.ObjectModel;
using InstanceAnswerPro.Core;
using System.ComponentModel;
using Bama.Controls;
using System.Collections;
using InstanceAnswerPro.API;

namespace InstanceAnswerPro.Conversation
{
    public partial class CommunitySessionWindow : Window
    {
        private static BitmapFrame _icon;
        private CommunityManager communityManager;
        private static List<CommunitySessionWindow> CommunitySessionWindows = new List<CommunitySessionWindow>();
        private bool initXaml;
        private ObservableCollection<SessionTabItem> sessionTabItems;
        private CommunitySessionWindow()
        {
            this.sessionTabItems = new ObservableCollection<SessionTabItem>();
            this.initXaml = true;
            this.InitializeComponent();
        }

        public CommunitySessionWindow(SessionTabItem sessionTabItem)
        {
            this.sessionTabItems = new ObservableCollection<SessionTabItem>();
            //WindowHelper.Hook(this, "headerBackground", new string[] { "controlBox", "toolBar" });
            this.InitializeComponent();
            Util_UserSettings_ContactSessionWindow.SettingsChanged += new PropertyChangedEventHandler(this.Util_UserSettings_CommunitySessionWindow_SettingsChanged);
            this.SetSendButtonToolTip();
            this.AddSession(sessionTabItem);
            if (_icon == null)
            {
                _icon = BitmapFrame.Create(new Uri(EnvironmentPath.Startup + @"res\community16.ico", UriKind.Absolute));
            }
            base.Icon = _icon;
            this.BindWindowTitleAndIcon();
            this.communityManager = this.CurrentSessionTabItem.CommunitySession.Community.CommunityManager;
            this.communityManager.RefreshAllMemberInfo();
            this.communityManager.SortManager.SortEvent += new EventHandler<EventArgs>(this.CommunityMemberSortManager_Sort);
            this.communityManager.SortManager.RequestSorting();
            this.CurrentSessionTabItem.CommunitySession.Community.PropertyChanged += new PropertyChangedEventHandler(this.CommunitySessionWindow_PropertyChanged);
            Buddy.BuddyPropertyChanged += new PropertyChangedEventHandler(this.Buddy_BuddyPropertyChanged);
            this.communityManager.MemberChanged += new EventHandler(this.communityManager_MemberChanged);
            this.CalcMemberCount();
            this.SetMsgSetImage();
        }

        public CommunitySessionWindow(CommunitySession communitySession)
            : this(new SessionTabItem(communitySession))
        {
        }

        private void _sort()
        {
            ICollectionView defaultView = CollectionViewSource.GetDefaultView(this.MemberListBox.ItemsSource);
            if (defaultView != null)
            {
                if (defaultView.SortDescriptions.Count != 4)
                {
                    defaultView.SortDescriptions.Clear();
                    defaultView.SortDescriptions.Add(new SortDescription("Buddy.PresenceInfo.PresenceWeight", ListSortDirection.Descending));
                    defaultView.SortDescriptions.Add(new SortDescription("CommunityMemberWeight", ListSortDirection.Descending));
                    defaultView.SortDescriptions.Add(new SortDescription("Buddy.QQMemberWeight", ListSortDirection.Descending));
                    defaultView.SortDescriptions.Add(new SortDescription("Name", ListSortDirection.Ascending));
                }
                else
                {
                    defaultView.Refresh();
                }
            }
            this.CalcMemberCount();
        }

        public static bool ActiveSessionWhenExist(CommunitySession communitySession)
        {
            for (int i = 0; i < CommunitySessionWindows.Count; i++)
            {
                SessionTabItem item = CommunitySessionWindows[i].FindIMSession(communitySession);
                if (item != null)
                {
                    if (CommunitySessionWindows[i].WindowState == WindowState.Minimized)
                    {
                        CommunitySessionWindows[i].WindowState = WindowState.Normal;
                    }
                    CommunitySessionWindows[i].Show();
                    CommunitySessionWindows[i].Activate();
                    CommunitySessionWindows[i].CurrentSessionTabItem = item;
                    return true;
                }
            }
            return false;
        }

        private void AddMsgToOutputBox(IMMessage imMessage)
        {
            Buddy sender = imMessage.Sender;
            string senderName = null;
            if (sender != null)
            {
                CommunityMember member = this.CurrentSessionTabItem.CommunitySession.Community.Members.FindMember(sender.Uin);
                if (member != null)
                {
                    senderName = member.CombineName;
                }
                else
                {
                    senderName = sender.CombineName;
                }
            }
            this.OutputBox.AddMsgToOutputBox(imMessage, senderName, null);
            IMMessage blockURLWarningMsg = Util_Misc.GetBlockURLWarningMsg(imMessage.MessagePack.Header, this.OutputBox.IsCommunity);
            if (blockURLWarningMsg != null)
            {
                this.OutputBox.AddMsgToOutputBox(blockURLWarningMsg, senderName, null);
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
            this.CurrentSessionTabItem = sessionTabItem;
            this.CurrentSessionTabItem.CommunitySession.Community.CommunityManager.RefreshCommunityFromServer();
            this.CurrentSessionTabItem.CommunitySession.Community.CommunityManager.UpdateMemberStatus(true);
            this.CurrentSessionTabItem.CommunitySession.Community.CommunityManager.UpdateMemCardInfo(Util_Buddy.GetCurrentBuddy().Uin);
        }


        private void BindWindowTitleAndIcon()
        {
            this.caption.DataContext = this.CurrentSessionTabItem.CommunitySession.Community;
            this.MemberListBox.DataContext = this.caption.DataContext;
            this.Announcement.DataContext = this.caption.DataContext;
            this.msgSetButton.DataContext = this.caption.DataContext;
            this.memberExpander.DataContext = this;
        }

        private void Buddy_BuddyPropertyChanged(object sender, PropertyChangedEventArgs e)
        {
            if (e.PropertyName == "PresenceInfo")
            {
                Buddy buddy = (Buddy)sender;
                if (this.CurrentSessionTabItem.CommunitySession.Community.Members.FindMember(buddy.Uin) != null)
                {
                    this.communityManager.SortManager.RequestSorting();
                }
            }
        }

        private void CalcMemberCount()
        {
            if ((this.CurrentSessionTabItem != null) && (this.CurrentSessionTabItem.CommunitySession != null))
            {
                CommunityMemberList members = this.CurrentSessionTabItem.CommunitySession.Community.Members;
                int count = members.Count;
                int num2 = 0;
                foreach (CommunityMember member in members)
                {
                    if (member.Buddy.PresenceInfo.IsOnline)
                    {
                        num2++;
                    }
                }
                this.memberExpander.Header = string.Format("群成员({0}/{1})", num2, count);
            }
        }

        private void CaptureButton_Click(object sender, RoutedEventArgs e)
        {
            Util_DataReport.RID_Count_AIO_Capture();
            Util_Capture.CameraScreen();
        }

        private void clearButton_Click(object sender, RoutedEventArgs e)
        {
            this.OutputBox.Document.Blocks.Clear();
        }

        public static void CloseCommunityWindowByID(uint communityID)
        {
            for (int i = 0; i < CommunitySessionWindows.Count; i++)
            {
                SessionTabItem sessionTabItem = CommunitySessionWindows[i].FindIMSession(communityID);
                CommunitySessionWindows[i].ReleaseSession(sessionTabItem, true);
            }
        }

        private void CloseWindow_CanExecute(object sender, CanExecuteRoutedEventArgs args)
        {
            args.CanExecute = true;
        }

        private void CloseWindow_Executed(object sender, ExecutedRoutedEventArgs args)
        {
            base.Close();
        }

        private void communityManager_MemberChanged(object sender, EventArgs e)
        {
            if (this.communityManager != null)
            {
                this.communityManager.SortManager.RequestSorting();
            }
        }

        private void CommunityMemberSortManager_Sort(object sender, EventArgs e)
        {
            this._sort();
        }

        private void CommunitySessionWindow_PropertyChanged(object sender, PropertyChangedEventArgs e)
        {
            if ((e.PropertyName == "MsgRecvType") || (e.PropertyName == "IsForbidPic"))
            {
                this.SetMsgSetImage();
            }
        }

        protected void CommunitySessionWindowStateChanged(object sender, EventArgs e)
        {
            this.ResetMargin();
        }

        private void emoticonButton_Click(object sender, RoutedEventArgs e)
        {
            Util_DataReport.RID_Count_AIO_Emoticon();
            //EmoticonShow.ShowActivate(this.emoticonButton, this, new EmoticonShow.EmoticonSelectedHandler(this.EmoticonShow_EmoticonSelected));
        }

        private bool EmoticonShow_EmoticonSelected(EmoticonItem emoticon)
        {
            this.InputBox.InsertEmoticon(emoticon.Fileorg, emoticon);
            if (Keyboard.IsKeyDown(Key.LeftCtrl) || Keyboard.IsKeyDown(Key.RightCtrl))
            {
                return false;
            }
            this.InputBox.Focus();
            return true;
        }

        public SessionTabItem FindIMSession(CommunitySession communitySession)
        {
            foreach (SessionTabItem item in this.sessionTabItems)
            {
                if (item.CommunitySession == communitySession)
                {
                    return item;
                }
            }
            return null;
        }

        private SessionTabItem FindIMSession(uint communityID)
        {
            foreach (SessionTabItem item in this.sessionTabItems)
            {
                if (item.CommunitySession.Community.Id == communityID)
                {
                    return item;
                }
            }
            return null;
        }

        private void fontButton_Click(object sender, RoutedEventArgs e)
        {
            Util_DataReport.RID_Count_AIO_Font();
            //this.fontStyleSelectorPopup.IsOpen = true;
        }

        private void Grid_MouseLeftButtonDown(object sender, MouseButtonEventArgs e)
        {
            e.Handled = true;
        }

        private void Grid_MouseLeftButtonUp(object sender, MouseButtonEventArgs e)
        {
            if ((sender == this.mail) && (this.CurrentSessionTabItem != null))
            {
                Util_Group.SendMail(this.CurrentSessionTabItem.CommunitySession.Community);
            }
        }

        private void Hyperlink_Click(object sender, RoutedEventArgs e)
        {
            Hyperlink originalSource = e.OriginalSource as Hyperlink;
            if (originalSource != null)
            {
                // ConversationModule.OnClickHyperlink(originalSource, this, this.CurrentSessionTabItem);
            }
        }

        public static void InitXaml()
        {
            new CommunitySessionWindow();
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

        private void InputBox_TextChanged(object sender, TextChangedEventArgs e)
        {

        }

        private void MsgSet_CanExecute(object sender, CanExecuteRoutedEventArgs args)
        {
            args.CanExecute = true;
        }

        private void MsgSet_Executed(object sender, ExecutedRoutedEventArgs args)
        {
            MenuItem parameter = args.Parameter as MenuItem;
            MsgRecvType tag = (MsgRecvType)parameter.Tag;
            Util_Group.SetMsgType(this.CurrentSessionTabItem.CommunitySession.Community, tag);
        }

        private void msgSetButton_Click(object sender, RoutedEventArgs e)
        {
            InstanceAnswerPro.Core.Community.Community community = this.CurrentSessionTabItem.CommunitySession.Community;
            ItemCollection items = this.msgSetButton.DropDown.Items;
            Util_Group.SetMenuStatus(community, items);
        }

        protected override void OnClosed(EventArgs args)
        {
            this.CurrentSessionTabItem = null;
            Util_UserSettings_ContactSessionWindow.SettingsChanged -= new PropertyChangedEventHandler(this.Util_UserSettings_CommunitySessionWindow_SettingsChanged);
            Buddy.BuddyPropertyChanged -= new PropertyChangedEventHandler(this.Buddy_BuddyPropertyChanged);
            if (this.communityManager != null)
            {
                this.communityManager.SortManager.SortEvent -= new EventHandler<EventArgs>(this.CommunityMemberSortManager_Sort);
                this.communityManager.MemberChanged -= new EventHandler(this.communityManager_MemberChanged);
            }
            base.StateChanged -= new EventHandler(this.CommunitySessionWindowStateChanged);
            this.InputBox.SaveSettings(typeof(Util_UserSettings_CommunitySessionWindow).Name);
            foreach (SessionTabItem item in this.sessionTabItems)
            {
                item.Close();
            }
            this.sessionTabItems.Clear();
            CommunitySessionWindows.Remove(this);
        }

        protected override void OnInitialized(EventArgs e)
        {
            base.OnInitialized(e);
            if (!this.initXaml)
            {
                this.ResetMargin();
                base.StateChanged += new EventHandler(this.CommunitySessionWindowStateChanged);
                base.AddHandler(Bama.Controls.TabItem.DeleteEvent, new RoutedEventHandler(this.OnTabItemDeleted));
                this.sessionsControl.SelectionChanged += new SelectionChangedEventHandler(this.OnSelectedTabItemChanged);
                this.send.Click += new RoutedEventHandler(this.OnSendButtonClicked);
                //this.emoticonButton.Click += new RoutedEventHandler(this.emoticonButton_Click);
                //this.CaptureButton.Click += new RoutedEventHandler(this.CaptureButton_Click);
                this.sessionsControl.ItemsSource = this.sessionTabItems;
                CommunitySessionWindows.Add(this);
                this.InputBox.LoadSettings(typeof(Util_UserSettings_CommunitySessionWindow).Name);
            }
        }

        private void OnItemDoubleClicked(object sender, RoutedEventArgs e)
        {
            CommunityMember member = this.MemberListBox.ItemContainerGenerator.ItemFromContainer((DependencyObject)sender) as CommunityMember;
            if ((member != null) && Util_Buddy.IsOnlineStatus())
            {
                Buddy buddy = member.Buddy;
                if ((buddy != null) && Util_Buddy.IsFriend(buddy.Uin))
                {
                    Util_Buddy.OpenContactSessionWindow(buddy);
                    e.Handled = true;
                }
            }
        }

        public void OnMessageAdded(object sender, EventArgs args)
        {
            SessionTabItem item = (SessionTabItem)sender;
            if (item == this.CurrentSessionTabItem)
            {
                this.RefreshOutputBox();
            }
            else
            {
                item.HasNewMessage = true;
            }
        }

        internal void OnSelectedTabItemChanged(object sender, RoutedEventArgs e)
        {
            SessionTabItem selectedItem = this.sessionsControl.SelectedItem as SessionTabItem;
            if (selectedItem != null)
            {
                base.Title = string.Format("{0} - 群窗口", selectedItem.CommunitySession.Community.CombineRemarkName);
                this.InputBox.Document = selectedItem.InputBoxDocument;
                selectedItem.MessageIndex = 0;
                this.OutputBox.Document.Blocks.Clear();
                this.RefreshOutputBox();
            }
            else
            {
                this.InputBox.Document = new FlowDocument();
            }
        }

        private void OnSendButtonClicked(object sender, RoutedEventArgs e)
        {
            Util_DataReport.RID_Count_AIO_SendMsg();
            this.SendMsg();
            this.InputBox.Focus();
        }

        internal void OnTabItemDeleted(object sender, RoutedEventArgs e)
        {
            if (this.sessionsControl.ItemsSource != null)
            {
                Bama.Controls.TabItem originalSource = e.OriginalSource as Bama.Controls.TabItem;
                if (originalSource != null)
                {
                    SessionTabItem sessionTabItem = (SessionTabItem)this.sessionsControl.ItemContainerGenerator.ItemFromContainer(originalSource);
                    if (sessionTabItem != null)
                    {
                        this.ReleaseSession(sessionTabItem, true);
                    }
                }
            }
        }

        private void ParseImage(MessagePack msgPack, ImageEx image)
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
            }
        }

        private void ParseInlines(MessagePack msgPack, InlineCollection inlines)
        {
            foreach (Inline inline in inlines)
            {
                if (inline is System.Windows.Documents.Run)
                {
                    this.ParseRun(msgPack, (System.Windows.Documents.Run)inline);
                }
                else if (inline is Span)
                {
                    this.ParseSpan(msgPack, (Span)inline);
                }
                else if (inline is LineBreak)
                {
                    this.ParseLineBreak(msgPack, (LineBreak)inline);
                }
                else if (inline is InlineUIContainer)
                {
                    this.ParseInlineUIContainer(msgPack, (InlineUIContainer)inline);
                }
            }
        }

        private void ParseInlineUIContainer(MessagePack msgPack, InlineUIContainer inlineUIContainer)
        {
            ImageEx child = inlineUIContainer.Child as ImageEx;
            if (child != null)
            {
                this.ParseImage(msgPack, child);
            }
        }

        private void ParseLineBreak(MessagePack msgPack, LineBreak lineBreak)
        {
            ((InstanceAnswerPro.Core.TextElement)msgPack.CreateElement(MsgPackCat.ELEMTYPE_TEXT)).SetText("\r\n");
        }

        private void ParseRun(MessagePack msgPack, System.Windows.Documents.Run run)
        {
            string text = run.Text;
            if (!string.IsNullOrEmpty(text))
            {
                ((InstanceAnswerPro.Core.TextElement)msgPack.CreateElement(MsgPackCat.ELEMTYPE_TEXT)).SetText(text);
            }
        }

        private void ParseSpan(MessagePack msgPack, Span span)
        {
            this.ParseInlines(msgPack, span.Inlines);
        }

        public void ReceiveMessage(CommunitySession session, Message message)
        {
            try
            {
                if (message.Type == MessageType.CommunityMessage)
                {
                    CommunityMessage message2 = message as CommunityMessage;
                    SessionTabItem item = this.FindIMSession(session);
                    Buddy sender = ComponentManager.GetBuddyListBuilder().FindOrCreateBuddy(message2.Uin, true);
                    if ((sender != null) && (item != null))
                    {
                        item.AddMsg(sender, message2.Time, message2.MessagePack);
                    }
                }
                else if (message.Type == MessageType.InfoMessage)
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

        public static void RefreshConversationPic(uint communityID, Guid picguid, bool IsPicReceiveSuccess, string info)
        {
            for (int i = 0; i < CommunitySessionWindows.Count; i++)
            {
                if (CommunitySessionWindows[i].FindIMSession(communityID) != null)
                {
                    CommunitySessionWindows[i].OutputBox.OnImageTransferStatusChanged(picguid, IsPicReceiveSuccess, info);
                }
                else
                {
                    TXLog.TXLogImage(string.Format("收到群图片 {0} {1} {2},但找不到对应的群 ", picguid, IsPicReceiveSuccess, info));
                }
            }
        }

        private void RefreshOutputBox()
        {
            if (this.CurrentSessionTabItem != null)
            {
                this.CurrentSessionTabItem.HasNewMessage = false;
                ArrayList iMMessageList = this.CurrentSessionTabItem.IMMessageList;
                int count = iMMessageList.Count;
                for (int i = this.CurrentSessionTabItem.MessageIndex; i < count; i++)
                {
                    IMMessage imMessage = (IMMessage)iMMessageList[i];
                    this.AddMsgToOutputBox(imMessage);
                }
                this.CurrentSessionTabItem.MessageIndex = count;
            }
            ConversationModule.FlashConversationWindow(this);
        }

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
                    this.CurrentSessionTabItem = this.sessionTabItems[0];
                }
                else
                {
                    this.CurrentSessionTabItem = null;
                    base.Close();
                }
            }
        }

        private void ResetMargin()
        {
        }

        private void SendMsg()
        {
            if (!Util_Buddy.GetCurrentBuddy().PresenceInfo.IsOnline)
            {
                Util_Misc.NotifyMsgToConversation(this.CurrentSessionTabItem.CommunitySession.Community.Id, true, CoreMessenger.Instance.MiscHelper.TXLoadString("CF_SELF_OFFLINE"));
            }
            else if (this.InputBox.GetTextLength() > 0x1194)
            {
                Util_Misc.NotifyMsgToConversation(this.CurrentSessionTabItem.CommunitySession.Community.Id, true, CoreMessenger.Instance.MiscHelper.TXLoadString("CF_EDITMSG_LARGE_MESSAGE"));
            }
            else
            {
                int imageCount = 0;
                MessagePack messagePack = this.InputBox.CreateMessagePack(out imageCount);
                if (imageCount > 1)
                {
                    Util_Misc.NotifyMsgToConversation(this.CurrentSessionTabItem.CommunitySession.Community.Id, true, CoreMessenger.Instance.MiscHelper.TXLoadString("CF_Group_Image_TooManyImage"));
                }
                else if ((messagePack != null) && (this.CurrentSessionTabItem != null))
                {
                    this.CurrentSessionTabItem.SendMessage(messagePack);
                    Buddy currentBuddy = Util_Buddy.GetCurrentBuddy();
                    this.CurrentSessionTabItem.AddMsg(currentBuddy, TimeConverter.Now, messagePack);
                    try
                    {
                        this.InputBox.Document.Blocks.Clear();
                    }
                    catch (Exception)
                    {
                    }
                }
            }
        }

        private void sendPicButton_Click(object sender, RoutedEventArgs e)
        {
            Util_DataReport.RID_Count_AIO_SendPic();
            //ConversationModule.SendImage(this, this.InputBox);
        }

        private void SetMsgSetImage()
        {
            bool flag = this.CurrentSessionTabItem.CommunitySession.Community.IsPrevent == true;
            BitmapImage image = new BitmapImage();
            image.BeginInit();
            if (flag)
            {
                image.UriSource = new Uri("pack://application:,,,/res/toolbar_msg.png");
            }
            else
            {
                image.UriSource = new Uri("pack://application:,,,/res/toolbar_msg_default.png");
            }
            image.EndInit();
            this.msgSetImage.Source = image;
        }

        private void SetSendButtonToolTip()
        {
            this.send.ToolTip = string.Format("按 {0} 键发送消息，按 {1} 键换行。\r\n（快捷键可以在 QQ 系统设置里修改）", Util_UserSettings_ContactSessionWindow.SendByEnter ? "Enter" : "Ctrl+Enter", Util_UserSettings_ContactSessionWindow.SendByEnter ? "Ctrl+Enter" : "Enter");
        }


        private void Util_UserSettings_CommunitySessionWindow_SettingsChanged(object sender, PropertyChangedEventArgs e)
        {
            if (e.PropertyName == "SendByEnter")
            {
                this.SetSendButtonToolTip();
            }
        }

        private void viewMsgRecordButton_Click(object sender, RoutedEventArgs e)
        {

            //if (this.msgRecordPanel.IsPanelVisible)
            //{
            //    this.msgRecordPanel.Hide();
            //}
            //else
            //{
            //    this.msgRecordPanel.Show();
            //}
        }

        public SessionTabItem CurrentSessionTabItem
        {
            get
            {
                if (this.sessionsControl == null)
                {
                    return null;
                }
                return (this.sessionsControl.SelectedItem as SessionTabItem);
            }
            set
            {
                if (value != this.sessionsControl.SelectedItem)
                {
                    if ((this.CurrentSessionTabItem != null) && (this.CurrentSessionTabItem.CommunitySession != null))
                    {
                        this.CurrentSessionTabItem.CommunitySession.Community.SoundPlayed = false;
                        this.CurrentSessionTabItem.CommunitySession.Community.PropertyChanged -= new PropertyChangedEventHandler(this.CommunitySessionWindow_PropertyChanged);
                        this.CurrentSessionTabItem.CommunitySession.Community.CommunityManager.UpdateMemberStatus(false);
                    }
                    this.sessionsControl.SelectedItem = value;
                    if (this.CurrentSessionTabItem != null)
                    {
                        //this.msgRecordPanel.MsgType = MsgTypeTags.Group;
                        if (this.CurrentSessionTabItem.CommunitySession != null)
                        {
                            //this.msgRecordPanel.Uin = this.CurrentSessionTabItem.CommunitySession.Community.Id;
                            this.OutputBox.Uin = this.CurrentSessionTabItem.CommunitySession.Community.Id;
                            this.InputBox.Uin = this.CurrentSessionTabItem.CommunitySession.Community.Id;
                        }
                    }
                    this.OutputBox.IsCommunity = true;
                    this.InputBox.IsCommunity = true;
                }
            }
        }

        public int SessionCount
        {
            get
            {
                return this.sessionTabItems.Count;
            }
        }
    }
}
