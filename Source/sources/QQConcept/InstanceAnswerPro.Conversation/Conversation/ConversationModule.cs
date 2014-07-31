using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using InstanceAnswerPro.Core;
using InstanceAnswerPro.Core.Community;
using System.Runtime.InteropServices;
using System.Windows.Interop;
using System.IO;
using System.Windows;
using System.Diagnostics;
using System.Windows.Media.Imaging;
using System.Windows.Forms;
using InputBox = InstanceAnswerPro.IM.Controls.InputBox;
using InstanceAnswerPro.API;
using InstanceAnswerPro.IM.ModuleInterface;

namespace InstanceAnswerPro.Conversation
{
    [ModuleInformation("IAPro.ConversationModule")]
    public class ConversationModule : IModule, IMessageProcessor
    {
        private CommunitySessionManager _communitySessionManager;
        private ContactSessionManager _contactSessionManager;
        private MessageCenter _messageCenter;
        public static CoreMessenger Messenger;

        private void CalculateUnreadCommunityMessageCount(InstanceAnswerPro.Core.Message message)
        {
            InstanceAnswerPro.Core.Community.Community community = InstanceAnswerPro.Core.ComponentManager.GetCommunitiesManager().GetCommunity((message as CommunityMessage).CommunityID);
            int messagesCount = this._messageCenter.GetMessagesCount(msg => msg.Tag == message.Tag);
            community.MessageCount = messagesCount;
        }

        private void ContactSessionManager_ImageTransferStatusChanged(object sender, ImageTransferStatusChangedrEventArgs e)
        {
            ContactSessionWindow.OnImageTransferStatusChanged(e);
        }

        private void CreateCommunitySessionWindow(uint communityID)
        {
            this.CreateCommunitySessionWindow(communityID, null);
        }

        private void CreateCommunitySessionWindow(uint communityID, object parameter)
        {
            List<InstanceAnswerPro.Core.Message> list = Util_Group.PopMessages(communityID);
            CommunitySession communitySession = this._communitySessionManager.GetCommunitySession(communityID, true);
            CommunitySessionWindow window = new CommunitySessionWindow(communitySession);
            foreach (InstanceAnswerPro.Core.Message message in list)
            {
                window.ReceiveMessage(communitySession, message);
            }
            Util_Buddy.BuddySessionParameter parameter2 = parameter as Util_Buddy.BuddySessionParameter;
            if (parameter2 != null)
            {
                window.Left = parameter2.WindowPosition.X;
                window.Top = parameter2.WindowPosition.Y;
            }
            window.Show();
            window.Activate();
        }

        private void CreateContactSessionWindow(uint uin)
        {
            this.CreateContactSessionWindow(uin, null);
        }

        private void CreateContactSessionWindow(uint uin, object parameter)
        {
            //DesktopBuddy buddy = null;
            //object obj2 = CoreMessenger.Instance.WindowManager.FireEvent("DesktopBuddy", WindowEvent.FindWindow, uin, null);
            Util_Buddy.BuddySessionParameter parameter2 = parameter as Util_Buddy.BuddySessionParameter;
            //if (obj2 is DesktopBuddy)
            //{
            //    buddy = (DesktopBuddy) obj2;
            //    if (parameter2 == null)
            //    {
            //        parameter2 = new Util_Buddy.BuddySessionParameter {
            //            ContactSessionWindowStatus = Util_Buddy.ContactSessionWindowStatus.Dialog
            //        };
            //    }
            //    parameter2.OpenFromDesktopBuddy = true;
            //    parameter2.WindowPosition = new Point(buddy.Left, buddy.Top);
            //    buddy.DestroySession();
            //    buddy.Close();
            //}
            ContactSession contactSession = this._contactSessionManager.GetContactSession(uin, true);
            ContactSessionWindow window = new ContactSessionWindow(contactSession, null, (parameter2 != null) ? parameter2.OpenFromDesktopBuddy : false);
            foreach (InstanceAnswerPro.Core.Message message in this._messageCenter.PopMessages(delegate(InstanceAnswerPro.Core.Message message)
            {
                if (message.Type == InstanceAnswerPro.Core.MessageType.ContactMessage)
                {
                    ContactMessage message2 = message as ContactMessage;
                    if (message2.Uin == uin)
                    {
                        return true;
                    }
                }
                else if (message.Type == InstanceAnswerPro.Core.MessageType.InfoMessage)
                {
                    InfoMessage message3 = message as InfoMessage;
                    if (!message3.IsCommunityMsg && (message3.Uin == uin))
                    {
                        return true;
                    }
                }
                return false;
            }, true))
            {
                window.ReceiveMessage(contactSession, message);
            }
            if (parameter2 != null)
            {
                FrameworkElement content = window.Content as FrameworkElement;
                window.Left = parameter2.WindowPosition.X - content.Margin.Left;
                window.Top = parameter2.WindowPosition.Y - content.Margin.Top;
            }
            window.Show();
        }

        //private void CreateDesktopBuddy(Buddy buddy, Point? point)
        //{
        //    MessageCenter.MessageFilter messageFilter = null;
        //    DesktopBuddy buddy2 = null;
        //    object obj2 = CoreMessenger.Instance.WindowManager.FireEvent("DesktopBuddy", WindowEvent.FindWindow, buddy, null);
        //    if (obj2 is DesktopBuddy)
        //    {
        //        buddy2 = (DesktopBuddy)obj2;
        //        if (point.HasValue)
        //        {
        //            buddy2.MoveTo(point.Value);
        //        }
        //    }
        //    else
        //    {
        //        ContactSession contactSession = this._contactSessionManager.GetContactSession(buddy.Uin, true);
        //        buddy2 = new DesktopBuddy(buddy, contactSession, point);
        //        if (messageFilter == null)
        //        {
        //            messageFilter = delegate(IAPro.Core.Message message)
        //            {
        //                if (message.Type == IAPro.Core.MessageType.ContactMessage)
        //                {
        //                    ContactMessage message2 = message as ContactMessage;
        //                    if (message2.Uin == buddy.Uin)
        //                    {
        //                        return true;
        //                    }
        //                }
        //                return false;
        //            };
        //        }
        //        foreach (IAPro.Core.Message message in this._messageCenter.PopMessages(messageFilter, true))
        //        {
        //            buddy2.ReceiveMessage(contactSession, message);
        //        }
        //    }
        //    buddy2.Show();
        //}

        public static void FlashConversationWindow(Window win)
        {
            if (!win.IsActive)
            {
                WinAPI.FLASHWINFO flashwinfo;
                flashwinfo = new WinAPI.FLASHWINFO
                {
                    //cbSize = (uint)Marshal.SizeOf(flashwinfo),
                    hwnd = new WindowInteropHelper(win).Handle,
                    dwFlags = 2,
                    uCount = 3,
                    dwTimeout = 400
                };
                WinAPI.FlashWindowEx(ref flashwinfo);
            }
        }

        private void InitXaml()
        {
            ContactSessionWindow.InitXaml();
            CommunitySessionWindow.InitXaml();

        }

        public void Load(object root)
        {
            Messenger = (CoreMessenger)root;
            this._contactSessionManager = InstanceAnswerPro.Core.ComponentManager.GetContactSessionManager();
            this._contactSessionManager.ImageTransferStatusChanged += new EventHandler<ImageTransferStatusChangedrEventArgs>(this.ContactSessionManager_ImageTransferStatusChanged);
            this._communitySessionManager = InstanceAnswerPro.Core.ComponentManager.GetCommunitySessionManager();
            this._messageCenter = Messenger.MessageCenter;
            this._messageCenter.AddMessageProcessor(this);
            this.InitXaml();
        }

        //internal static void OnClickHyperlink(ImageHyperlink hyperlink, Window window, SessionTabItem sessionTabItem)
        //{
        //    try
        //    {
        //        Guid guid = hyperlink.Guid;
        //        string soureUrl = hyperlink.SoureUrl;
        //        if (!string.IsNullOrEmpty(soureUrl))
        //        {
        //            if (guid.Equals(MessageElementTags.GuidLinkFile))
        //            {
        //                if (File.Exists(soureUrl))
        //                {
        //                    BrowserHelper.OpenUrl(BrowserType.System, soureUrl);
        //                }
        //                else
        //                {
        //                    hyperlink.DisabledHyperLink();
        //                    MessageBox.Show(window, "此文件不存在");
        //                }
        //            }
        //            else if (guid.Equals(MessageElementTags.GuidLinkDirectory))
        //            {
        //                if (File.Exists(soureUrl))
        //                {
        //                    Process.Start("explorer.exe", "/select," + soureUrl);
        //                }
        //                else
        //                {
        //                    soureUrl = Path.GetDirectoryName(soureUrl);
        //                    if (Directory.Exists(soureUrl))
        //                    {
        //                        BrowserHelper.OpenUrl(BrowserType.System, soureUrl);
        //                    }
        //                    else
        //                    {
        //                        hyperlink.DisabledHyperLink();
        //                        MessageBox.Show(window, "此目录不存在");
        //                    }
        //                }
        //            }
        //            else if (guid.Equals(MessageElementTags.GuidLinkSendAgain))
        //            {
        //                hyperlink.DisabledHyperLink();
        //                Util_Misc.OpenSendFile(sessionTabItem.Uin, soureUrl);
        //            }
        //            else if (guid.Equals(MessageElementTags.GuidLinkSafePage) || guid.Equals(MessageElementTags.GuidLinkHttp))
        //            {
        //                BrowserHelper.OpenUrl(BrowserType.System, soureUrl);
        //            }
        //        }
        //    }
        //    catch (Exception)
        //    {
        //    }
        //}

        public void OnMessagePopped(InstanceAnswerPro.Core.Message message)
        {
            if (message.Type == InstanceAnswerPro.Core.MessageType.CommunityMessage)
            {
                this.CalculateUnreadCommunityMessageCount(message);
            }
        }

        public void OnMessagePushed(InstanceAnswerPro.Core.Message message)
        {
            if (message.Type == InstanceAnswerPro.Core.MessageType.InfoMessage)
            {
                InfoMessage infoMessage = (InfoMessage)message;
                if (!infoMessage.IsCommunityMsg)
                {
                    ContactSession contactSession = this._contactSessionManager.GetContactSession(infoMessage.Uin, false);
                    if (contactSession != null)
                    {
                        contactSession.OnMessageReceived(infoMessage);
                        this._messageCenter.PopMessage(infoMessage);
                    }
                }
                else
                {
                    CommunitySession communitySession = this._communitySessionManager.GetCommunitySession(infoMessage.Uin, false);
                    if (communitySession != null)
                    {
                        communitySession.OnMessageReceived(infoMessage);
                        this._messageCenter.PopMessage(infoMessage);
                    }
                }
            }
            else if (message.Type == InstanceAnswerPro.Core.MessageType.ContactMessage)
            {
                ContactMessage message3 = (ContactMessage)message;
                this._messageCenter.NotifyMessage(new UICommandMessage("AddRecentContact", InstanceAnswerPro.Core.MessageType.ContactMessage, message3.Uin));
            }
            else if (message.Type == InstanceAnswerPro.Core.MessageType.CommunityMessage)
            {
                CommunityMessage message4 = (CommunityMessage)message;
                this._messageCenter.NotifyMessage(new UICommandMessage("AddRecentContact", InstanceAnswerPro.Core.MessageType.CommunityMessage, message4.CommunityID));
                this.CalculateUnreadCommunityMessageCount(message4);
            }
        }

        public void OnNotifyMessage(InstanceAnswerPro.Core.Message message)
        {
            UICommandMessage message2 = message as UICommandMessage;
            if (message2 != null)
            {
                if (message2.CommandName == "OpenContactSessionWindow")
                {
                    Buddy buddy = message2.Parameter1 as Buddy;
                    Util_Buddy.BuddySessionParameter parameter = message2.Parameter2 as Util_Buddy.BuddySessionParameter;
                    Point? mousePosition = null;
                    if (parameter != null)
                    {
                        mousePosition = new Point?(parameter.WindowPosition);
                    }
                    if ((parameter == null) || (parameter.ContactSessionWindowStatus != Util_Buddy.ContactSessionWindowStatus.Avatar))
                    {
                        if (!ContactSessionWindow.ActiveSessionWhenExist(buddy.Uin, mousePosition))
                        {
                            this.CreateContactSessionWindow(buddy.Uin, message2.Parameter2);
                        }
                    }
                    else if (!ContactSessionWindow.ActiveSessionWhenExist(buddy.Uin, mousePosition))
                    {
                        //this.CreateDesktopBuddy(buddy, mousePosition);
                    }
                }
                else if (message2.CommandName == "OpenCommunitySessionWindow")
                {
                    InstanceAnswerPro.Core.Community.Community community = message2.Parameter1 as InstanceAnswerPro.Core.Community.Community;
                    if (!CommunitySessionWindow.ActiveSessionWhenExist(this._communitySessionManager.GetCommunitySession(community.Id, true)))
                    {
                        this.CreateCommunitySessionWindow(community.Id);
                    }
                }
                else if (message2.CommandName == "OpenContactSession")
                {
                    ContactSessionWindow.CloseSessionWhenExist((uint)message2.Parameter1);
                }
                else if (message2.CommandName == "Conversation")
                {
                    string str = message2.Parameter1 as string;
                    UICommand.Parameter2.ConversationEventInfo info = message2.Parameter2 as UICommand.Parameter2.ConversationEventInfo;
                    switch (str)
                    {
                        case "CloseConversation":
                            CommunitySessionWindow.CloseCommunityWindowByID(info.ConversationID);
                            return;

                        case "RefreshConversationPic":
                            CommunitySessionWindow.RefreshConversationPic(info.ConversationID, info.PicGuid, info.IsPicReceiveSuccess, info.Info);
                            break;
                    }
                }
            }
        }

        public void OnViewMessage(InstanceAnswerPro.Core.Message message)
        {
            InfoMessage message4;
            InstanceAnswerPro.Core.MessageType type = message.Type;
            if (type != InstanceAnswerPro.Core.MessageType.ContactMessage)
            {
                if (type != InstanceAnswerPro.Core.MessageType.CommunityMessage)
                {
                    if (type != InstanceAnswerPro.Core.MessageType.InfoMessage)
                    {
                        return;
                    }
                    goto Label_00B2;
                }
            }
            else
            {
                using (new Util_Perf.FunLog("ConversationModule.OnViewMessage  MessageType.ContactMessage"))
                {
                    ContactMessage message2 = message as ContactMessage;
                    if (!ContactSessionWindow.ActiveSessionWhenExist(message2.Uin, null))
                    {
                        this.CreateContactSessionWindow(message2.Uin);
                    }
                    return;
                }
            }
            using (new Util_Perf.FunLog("ConversationModule.OnViewMessage  MessageType.CommunityMessage"))
            {
                CommunityMessage message3 = message as CommunityMessage;
                if (!CommunitySessionWindow.ActiveSessionWhenExist(this._communitySessionManager.GetCommunitySession(message3.CommunityID, true)))
                {
                    this.CreateCommunitySessionWindow(message3.CommunityID);
                }
                return;
            }
        Label_00B2:
            message4 = message as InfoMessage;
            if (message4.IsCommunityMsg)
            {
                if (!CommunitySessionWindow.ActiveSessionWhenExist(this._communitySessionManager.GetCommunitySession(message4.Uin, true)))
                {
                    this.CreateCommunitySessionWindow(message4.Uin);
                }
            }
            else if (!ContactSessionWindow.ActiveSessionWhenExist(message4.Uin, null))
            {
                this.CreateContactSessionWindow(message4.Uin);
            }
        }

        internal static void SendImage(Window owner, InputBox inputBox)
        {
            OpenFileDialog dialog = new OpenFileDialog
            {
                Multiselect = false,
                Filter = "图像文件(bmp;jpg;jpeg;gif)|*.bmp;*.jpg;*.jpeg;*.gif"
            };
            if (dialog.ShowDialog() == DialogResult.OK)
            {
                FileInfo info = new FileInfo(dialog.FileName);
                if (info.Length > 0x100000L)
                {
                    System.Windows.MessageBox.Show(owner, "发送消息中包含的图片大小超过1M，请采用传文件的方式发送。");
                }
                else
                {
                    try
                    {
                        new BitmapImage(new Uri(dialog.FileName));
                    }
                    catch (Exception)
                    {
                        System.Windows.MessageBox.Show("图片格式错误。");
                        return;
                    }
                    inputBox.InsertEmoticon(dialog.FileName, null);
                }
            }
        }

        public void Unload()
        {
            this._messageCenter.RemoveMessageProcessor(this);
            CoreMessenger.Instance.WindowManager.CloseAll(typeof(ContactSessionWindow));
            CoreMessenger.Instance.WindowManager.CloseAll(typeof(CommunitySessionWindow));
            InstanceAnswerPro.Core.ComponentManager.GetContactSessionManager().ImageTransferStatusChanged -= new EventHandler<ImageTransferStatusChangedrEventArgs>(this.ContactSessionManager_ImageTransferStatusChanged);
        }

        public InstanceAnswerPro.Core.MessageType MessageType
        {
            get
            {
                return (InstanceAnswerPro.Core.MessageType.InfoMessage | InstanceAnswerPro.Core.MessageType.UICommandMessage | InstanceAnswerPro.Core.MessageType.CommunityMessage | InstanceAnswerPro.Core.MessageType.ContactMessage);
            }
        }
    }
}
