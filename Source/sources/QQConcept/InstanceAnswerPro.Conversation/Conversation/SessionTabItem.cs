using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.ComponentModel;
using System.Collections;
using System.Windows.Documents;
using InstanceAnswerPro.Core.Community;
using InstanceAnswerPro.Core;

namespace InstanceAnswerPro.Conversation
{
    public class SessionTabItem : INotifyPropertyChanged
    {
        private InstanceAnswerPro.Core.Community.CommunitySession _communitySession;
        private InstanceAnswerPro.Core.ContactSession _contactSession;
        private bool _isPreviw;
        private InstanceAnswerPro.Core.Buddy buddyField;
        private bool hasNewMessage;
        private ArrayList imMessageList;
        private FlowDocument inputBoxDocument;
        private int messageIndex;

        public event EventHandler<EventArgs> MessageAdded;

        public event PropertyChangedEventHandler PropertyChanged;

        public SessionTabItem(InstanceAnswerPro.Core.Buddy buddy)
        {
            this.imMessageList = new ArrayList();
            this.buddyField = buddy;
            this._isPreviw = true;
        }

        public SessionTabItem(InstanceAnswerPro.Core.Community.CommunitySession communitySession)
        {
            this.imMessageList = new ArrayList();
            this._communitySession = communitySession;
            this._communitySession.MessageReceived = (EventHandler<CommunityMessageReceivedEventArgs>)Delegate.Combine(this._communitySession.MessageReceived, new EventHandler<CommunityMessageReceivedEventArgs>(this.OnCommunityMessageReceived));
            this._communitySession.InfoMessageReceived = (EventHandler<InfoMessageReceivedEventArgs>)Delegate.Combine(this._communitySession.InfoMessageReceived, new EventHandler<InfoMessageReceivedEventArgs>(this.OnInfoMessageReceived));
            this._communitySession.SendMessageCompleted += new EventHandler<CommandKeyedCallbackArgs<MessagePack>>(this.session_SendMessageCompleted);
        }

        public SessionTabItem(InstanceAnswerPro.Core.ContactSession session)
        {
            this.imMessageList = new ArrayList();
            this._contactSession = session;
            this.buddyField = ComponentManager.GetBuddyListBuilder().FindOrCreateBuddy(session.Uin, true);
            this._contactSession.MessageReceived = (EventHandler<ContactMessageReceivedEventArgs>)Delegate.Combine(this._contactSession.MessageReceived, new EventHandler<ContactMessageReceivedEventArgs>(this.OnContactMessageReceived));
            this._contactSession.InfoMessageReceived = (EventHandler<InfoMessageReceivedEventArgs>)Delegate.Combine(this._contactSession.InfoMessageReceived, new EventHandler<InfoMessageReceivedEventArgs>(this.OnInfoMessageReceived));
            this._contactSession.SendMessageCompleted += new EventHandler<CommandKeyedCallbackArgs<MessagePack>>(this.session_SendMessageCompleted);
        }

        public void AddMsg(InstanceAnswerPro.Core.Buddy sender, DateTime time, MessagePack messagePack)
        {
            IMMessage message = new IMMessage(sender, time, messagePack);
            this.imMessageList.Add(message);
            if (this.MessageAdded != null)
            {
                this.MessageAdded(this, null);
            }
        }

        public void Close()
        {
            if (this._contactSession != null)
            {
                this._contactSession.MessageReceived = (EventHandler<ContactMessageReceivedEventArgs>)Delegate.Remove(this._contactSession.MessageReceived, new EventHandler<ContactMessageReceivedEventArgs>(this.OnContactMessageReceived));
                this._contactSession.InfoMessageReceived = (EventHandler<InfoMessageReceivedEventArgs>)Delegate.Remove(this._contactSession.InfoMessageReceived, new EventHandler<InfoMessageReceivedEventArgs>(this.OnInfoMessageReceived));
                this._contactSession.SendMessageCompleted -= new EventHandler<CommandKeyedCallbackArgs<MessagePack>>(this.session_SendMessageCompleted);
                ComponentManager.GetContactSessionManager().DestroySession(this._contactSession);
                this._contactSession = null;
            }
            if (this._communitySession != null)
            {
                this._communitySession.MessageReceived = (EventHandler<CommunityMessageReceivedEventArgs>)Delegate.Remove(this._communitySession.MessageReceived, new EventHandler<CommunityMessageReceivedEventArgs>(this.OnCommunityMessageReceived));
                this._communitySession.InfoMessageReceived = (EventHandler<InfoMessageReceivedEventArgs>)Delegate.Remove(this._communitySession.InfoMessageReceived, new EventHandler<InfoMessageReceivedEventArgs>(this.OnInfoMessageReceived));
                this._communitySession.SendMessageCompleted -= new EventHandler<CommandKeyedCallbackArgs<MessagePack>>(this.session_SendMessageCompleted);
                ComponentManager.GetCommunitySessionManager().DestroySession(this._communitySession);
                this._communitySession = null;
            }
        }

        private void OnCommunityMessageReceived(object sender, CommunityMessageReceivedEventArgs args)
        {
            this.ReceiveMessage(args.Message);
        }

        private void OnContactMessageReceived(object sender, ContactMessageReceivedEventArgs args)
        {
            this.ReceiveMessage(args.Message);
        }

        private void OnInfoMessageReceived(object sender, InfoMessageReceivedEventArgs args)
        {
            this.ReceiveMessage(args.Message);
        }

        protected void OnPropertyChanged(string propertyName)
        {
            if (this.PropertyChanged != null)
            {
                this.PropertyChanged(this, new PropertyChangedEventArgs(propertyName));
            }
        }

        public void ReceiveMessage(CommunityMessage communityMessage)
        {
            try
            {
                InstanceAnswerPro.Core.Buddy sender = ComponentManager.GetBuddyListBuilder().FindOrCreateBuddy(communityMessage.Uin, true);
                if (sender != null)
                {
                    this.AddMsg(sender, communityMessage.Time, communityMessage.MessagePack);
                }
            }
            catch (Exception)
            {
            }
        }

        public void ReceiveMessage(ContactMessage contactMessage)
        {
            try
            {
                InstanceAnswerPro.Core.Buddy sender = ComponentManager.GetBuddyListBuilder().FindOrCreateBuddy(contactMessage.Uin, true);
                if (sender != null)
                {
                    this.AddMsg(sender, contactMessage.Time, contactMessage.MessagePack);
                }
            }
            catch (Exception)
            {
            }
        }

        public void ReceiveMessage(InfoMessage infoMessage)
        {
            try
            {
                InstanceAnswerPro.Core.Buddy sender = ComponentManager.GetBuddyListBuilder().FindOrCreateBuddy(infoMessage.Uin, true);
                if (sender != null)
                {
                    this.AddMsg(sender, infoMessage.Time, infoMessage.MessagePack);
                }
            }
            catch (Exception)
            {
            }
        }

        public void SendMessage(MessagePack messagePack)
        {
            if (this._contactSession != null)
            {
                this._contactSession.SendMessage(messagePack);
            }
            else if (this._communitySession != null)
            {
                this._communitySession.SendMessage(messagePack);
            }
        }

        private void session_SendMessageCompleted(object sender, CommandKeyedCallbackArgs<MessagePack> e)
        {
            uint uin = 0;
            bool isCommunityMsg = false;
            if (sender == this._contactSession)
            {
                uin = this._contactSession.Uin;
                isCommunityMsg = false;
            }
            else if (sender == this._communitySession)
            {
                uin = this._communitySession.Community.Id;
                isCommunityMsg = true;
            }
            else
            {
                return;
            }
            if (e.Code == CallbackCode.Succeeded)
            {
                if (((e.DataCallback != null) && (TXDataHelper.GetDWord(e.DataCallback, SessionMsg.CCSenderExSendData_dwResult) == 7)) && (TXDataHelper.GetDWord(e.DataCallback, SessionMsg.CCSenderExSendData_SensitiveInfo_dwURLID) > 0))
                {
                    ushort word = TXDataHelper.GetWord(e.DataCallback, SessionMsg.wUnlawfulURLTipsID);
                    string str = ComponentManager.GetGrayURLMgr().QueryBlockURLWarningMsg(false, word);
                    if (!string.IsNullOrEmpty(str))
                    {
                        Util_Misc.NotifyMsgToConversation(uin, isCommunityMsg, str);
                    }
                }
            }
            else
            {
                string msgAbstract = CoreMessenger.Instance.MiscHelper.GetMsgAbstract(e.Key.Key);
                string str4 = CoreMessenger.Instance.MiscHelper.TXLoadString("CF_SEND_C2CMSG_FAILED").Replace("$MSG$", msgAbstract);
                if (!string.IsNullOrEmpty(str4))
                {
                    Util_Misc.NotifyMsgToConversation(uin, isCommunityMsg, str4);
                }
            }
        }

        public override string ToString()
        {
            return this.Title;
        }

        public InstanceAnswerPro.Core.Buddy Buddy
        {
            get
            {
                return this.buddyField;
            }
        }

        public InstanceAnswerPro.Core.Community.CommunitySession CommunitySession
        {
            get
            {
                return this._communitySession;
            }
        }

        public InstanceAnswerPro.Core.ContactSession ContactSession
        {
            get
            {
                return this._contactSession;
            }
        }

        public string Descryption
        {
            get
            {
                if (this._communitySession != null)
                {
                    return this._communitySession.Community.Description;
                }
                if (!string.IsNullOrEmpty(this.buddyField.QQInfo.LongNickname))
                {
                    return this.buddyField.QQInfo.LongNickname;
                }
                return "";
            }
        }

        public bool HasNewMessage
        {
            get
            {
                return this.hasNewMessage;
            }
            set
            {
                if (value != this.hasNewMessage)
                {
                    this.hasNewMessage = value;
                    this.OnPropertyChanged("HasNewMessage");
                }
            }
        }

        public string Icon
        {
            get
            {
                return string.Format(@"{0}\temp_{1:D2}.png", ConversationModule.Messenger.GetAppPath(KernelWrapper.APP_PATH_TYPE.APP_PATH_ROOT), (this.Uin % 7) + 1);
            }
        }

        public ArrayList IMMessageList
        {
            get
            {
                return this.imMessageList;
            }
        }

        public FlowDocument InputBoxDocument
        {
            get
            {
                return this.inputBoxDocument;
            }
            set
            {
                this.inputBoxDocument = value;
            }
        }

        public bool IsPreview
        {
            get
            {
                return this._isPreviw;
            }
        }

        public int MessageIndex
        {
            get
            {
                return this.messageIndex;
            }
            set
            {
                this.messageIndex = value;
            }
        }

        public bool Online
        {
            get
            {
                return ((this.buddyField != null) && this.buddyField.PresenceInfo.IsOnline);
            }
        }

        public string Title
        {
            get
            {
                if (this._communitySession != null)
                {
                    return this._communitySession.Community.Name;
                }
                return this.buddyField.NickName;
            }
        }

        public uint Uin
        {
            get
            {
                if (this.buddyField != null)
                {
                    return this.buddyField.Uin;
                }
                return 0;
            }
        }
    }
}
