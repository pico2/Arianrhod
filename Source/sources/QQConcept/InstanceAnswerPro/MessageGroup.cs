using System.Collections.Generic;
using System.ComponentModel;
using InstanceAnswerPro.Core;
using InstanceAnswerPro.Core.Community;

namespace InstanceAnswerPro
{
    public class MessageGroup : INotifyPropertyChanged
    {
        // Fields
        private string _description = "";
        private string _iconPath;
        private List<Message> _messages = new List<Message>();
        private MessageType _messageType;
        private string _title = "";
        public string MessageTag;

        // Events
        public event PropertyChangedEventHandler PropertyChanged;

        // Methods
        public MessageGroup(MessageType messageType, string messageTag)
        {
            this._messageType = messageType;
            this.MessageTag = messageTag;
        }

        public void AddMessage(Message message)
        {
            if ((message.Type == this._messageType) && (message.Tag == this.MessageTag))
            {
                this._messages.Insert(0, message);
                if (message.Title != this._title)
                {
                    this._title = message.Title;
                    this.OnPropertyChanged("Title");
                }
                if (message.Description != this._description)
                {
                    this._description = message.Description;
                    this.OnPropertyChanged("Description");
                }
                if (message.IconPath != this._iconPath)
                {
                    this._iconPath = message.IconPath;
                    this.OnPropertyChanged("IconPath");
                }
                this.OnPropertyChanged("MessageCount");
                this.OnMessageCountChange();
            }
        }

        private void OnMessageCountChange()
        {
            if (this._messageType == MessageType.CommunityMessage)
            {
                uint result = 0;
                if (uint.TryParse(this.MessageTag, out result) && (result > 0))
                {
                    ComponentManager.GetCommunitiesManager().GetCommunity(result).MessageCount = this.MessageCount;
                }
            }
        }

        protected void OnPropertyChanged(string propertyName)
        {
            if (this.PropertyChanged != null)
            {
                this.PropertyChanged(this, new PropertyChangedEventArgs(propertyName));
            }
        }

        public void RemoveMessage(Message message)
        {
            if ((message.Type == this._messageType) && (message.Tag == this.MessageTag))
            {
                this._messages.Remove(message);
                if (this._messages.Count > 0)
                {
                    string title = this._messages[0].Title;
                    if (this._title != title)
                    {
                        this._title = title;
                        this.OnPropertyChanged("Title");
                    }
                    string description = this._messages[0].Description;
                    if (this._description != description)
                    {
                        this._description = description;
                        this.OnPropertyChanged("Description");
                    }
                    string iconPath = this._messages[0].IconPath;
                    if (this._iconPath != iconPath)
                    {
                        this._iconPath = iconPath;
                        this.OnPropertyChanged("IconPath");
                    }
                }
                this.OnPropertyChanged("MessageCount");
                this.OnMessageCountChange();
            }
        }

        public void View()
        {
            if (this._messages.Count > 0)
            {
                CoreMessenger.Instance.MessageCenter.ViewMessage(this._messages[0]);
            }
            else if (this._messageType == MessageType.CommunityMessage)
            {
                uint communityID = uint.Parse(this.MessageTag);
                CommunityManager communityManager = ComponentManager.GetCommunitiesManager().GetCommunityManager(communityID, false);
                if (communityManager != null)
                {
                    InstanceAnswerPro.Core.Community.Community community = communityManager.GetCommunity(false);
                    if (community != null)
                    {
                        UICommandMessage message = new UICommandMessage("OpenCommunitySessionWindow", community, null);
                        CoreMessenger.Instance.MessageCenter.NotifyMessage(message);
                    }
                }
            }
            else if (this._messageType == MessageType.ContactMessage)
            {
                Util_Buddy.OpenContactSessionWindow(uint.Parse(this.MessageTag));
            }
        }

        // Properties
        public string Description
        {
            get
            {
                return this._description;
            }
        }

        public string IconPath
        {
            get
            {
                if (!string.IsNullOrEmpty(this._iconPath))
                {
                    return this._iconPath;
                }
                return null;
            }
        }

        public int MessageCount
        {
            get
            {
                return this._messages.Count;
            }
        }

        public MessageType MessageType
        {
            get
            {
                return this._messageType;
            }
        }

        public string Title
        {
            get
            {
                return this._title;
            }
        }
    }


}
