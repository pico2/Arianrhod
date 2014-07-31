using System;
using System.Collections.ObjectModel;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Input;
using System.Windows.Media;
using InstanceAnswerPro.API;
using InstanceAnswerPro.Core;

namespace InstanceAnswerPro
{
    /// <summary>
    /// Interaction logic for RecentContactsPanel.xaml
    /// </summary>
    public partial class RecentContactsPanel : UserControl, IMessageProcessor
    {
        protected void OnItemDoubleClicked(object sender, MouseButtonEventArgs e)
        {
            DependencyObject originalSource = e.OriginalSource as DependencyObject;
            if (originalSource != null)
            {
                if (originalSource is System.Windows.Documents.Run)
                {
                    originalSource = (originalSource as System.Windows.Documents.Run).Parent;
                }
                if ((originalSource is Visual) && !MainWindow.IsQZoneFlag(originalSource))
                {
                    ListBox ancestorByType = VisualTree.GetAncestorByType(originalSource, typeof(ListBox)) as ListBox;
                    ListBoxItem container = VisualTree.GetAncestorByType(originalSource, typeof(ListBoxItem)) as ListBoxItem;
                    if ((ancestorByType != null) && (container != null))
                    {
                        Buddy buddy = ancestorByType.ItemContainerGenerator.ItemFromContainer(container) as Buddy;
                        if (buddy != null)
                        {
                            Util_Buddy.OpenContactSessionWindow(buddy);
                        }
                        else
                        {
                            InstanceAnswerPro.Core.Community.Community community = ancestorByType.ItemContainerGenerator.ItemFromContainer(container) as InstanceAnswerPro.Core.Community.Community;
                            if (community != null)
                            {
                                Util_Buddy.OpenCommunitySessionWindow(community);
                            }
                        }
                        e.Handled = true;
                    }
                }
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
            UICommandMessage message2 = message as UICommandMessage;
            if (message2 != null)
            {
                if (message2.CommandName == "AddRecentContact")
                {
                    InstanceAnswerPro.Core.MessageType messageType = (InstanceAnswerPro.Core.MessageType)message2.Parameter1;
                    uint id = (uint)message2.Parameter2;
                    int index = ObservableCollectionHelper.FindFirst<object>(this.recentContactCollection, delegate(object contact)
                    {
                        Buddy buddy = contact as Buddy;
                        InstanceAnswerPro.Core.Community.Community community = contact as InstanceAnswerPro.Core.Community.Community;
                        return (((messageType == InstanceAnswerPro.Core.MessageType.ContactMessage) && (buddy != null)) && (id == buddy.Uin)) || (((messageType == InstanceAnswerPro.Core.MessageType.CommunityMessage) && (community != null)) && (id == community.Id));
                    });
                    if (index >= 0)
                    {
                        this.recentContactCollection.RemoveAt(index);
                    }
                    switch (messageType)
                    {
                        case InstanceAnswerPro.Core.MessageType.ContactMessage:
                            {
                                Buddy item = BuddyListBuilder.Instance.FindOrCreateBuddy(id, false, false);
                                if (item != null)
                                {
                                    this.recentContactCollection.Insert(0, item);
                                }
                                break;
                            }
                        case InstanceAnswerPro.Core.MessageType.CommunityMessage:
                            {
                                InstanceAnswerPro.Core.Community.Community community = ComponentManager.GetCommunitiesManager().GetCommunity(id);
                                if (community != null)
                                {
                                    this.recentContactCollection.Insert(0, community);
                                }
                                break;
                            }
                    }
                    int count = this.recentContactCollection.Count;
                    if (count > 30)
                    {
                        this.recentContactCollection.RemoveAt(count - 1);
                    }
                }
                else if (message2.CommandName == "RemoveRecentContact")
                {
                    InstanceAnswerPro.Core.MessageType messageType = (InstanceAnswerPro.Core.MessageType)message2.Parameter1;
                    uint id = (uint)message2.Parameter2;
                    int num3 = ObservableCollectionHelper.FindFirst<object>(this.recentContactCollection, delegate(object contact)
                    {
                        Buddy buddy = contact as Buddy;
                        InstanceAnswerPro.Core.Community.Community community = contact as InstanceAnswerPro.Core.Community.Community;
                        return (((messageType == InstanceAnswerPro.Core.MessageType.ContactMessage) && (buddy != null)) && (id == buddy.Uin)) || (((messageType == InstanceAnswerPro.Core.MessageType.CommunityMessage) && (community != null)) && (id == community.Id));
                    });
                    if (num3 >= 0)
                    {
                        this.recentContactCollection.RemoveAt(num3);
                    }
                }
            }
        }

        public void OnViewMessage(Message message)
        {
        }

        public bool ProcessEnterKey()
        {
            Buddy selectedItem = this.RecentContactsBox.SelectedItem as Buddy;
            if (selectedItem != null)
            {
                Util_Buddy.OpenContactSessionWindow(selectedItem);
                return true;
            }
            InstanceAnswerPro.Core.Community.Community community = this.RecentContactsBox.SelectedItem as InstanceAnswerPro.Core.Community.Community;
            if (community != null)
            {
                Util_Buddy.OpenCommunitySessionWindow(community);
                return true;
            }
            return false;
        }

        public void Save()
        {
            string settingValue = "";
            foreach (object obj2 in this.recentContactCollection)
            {
                if (obj2 is Buddy)
                {
                    if (settingValue.Length > 0)
                    {
                        settingValue = settingValue + ";";
                    }
                    settingValue = settingValue + string.Format("b{0}", ((Buddy)obj2).Uin);
                }
                if (obj2 is InstanceAnswerPro.Core.Community.Community)
                {
                    if (settingValue.Length > 0)
                    {
                        settingValue = settingValue + ";";
                    }
                    settingValue = settingValue + string.Format("g{0}", ((InstanceAnswerPro.Core.Community.Community)obj2).Id);
                }
            }
            if (settingValue.Length > 0)
            {
                ComponentManager.GetUserSettings().SetString("RecentContacts", settingValue);
            }
        }
        private ObservableCollection<object> recentContactCollection = new ObservableCollection<object>();
        public RecentContactsPanel()
        {
            InitializeComponent();
            Binding binding = new Binding
            {
                Source = this.recentContactCollection
            };
            this.RecentContactsBox.SetBinding(ItemsControl.ItemsSourceProperty, binding);
            CoreMessenger.Instance.MessageCenter.AddMessageProcessor(this);
        }
        public InstanceAnswerPro.Core.MessageType MessageType
        {
            get
            {
                return InstanceAnswerPro.Core.MessageType.UICommandMessage;
            }
        }
        public void Load()
        {
            this.recentContactCollection.Clear();
            string settingValue = "";
            ComponentManager.GetUserSettings().GetString("RecentContacts", ref settingValue);
            if (settingValue != null)
            {
                settingValue.Trim();
            }
            if (!string.IsNullOrEmpty(settingValue))
            {
                try
                {
                    foreach (string str2 in settingValue.Split(new char[] { ';' }))
                    {
                        if (str2.StartsWith("b"))
                        {
                            Buddy item = BuddyListBuilder.Instance.FindOrCreateBuddy(uint.Parse(str2.Substring(1)), false, false);
                            if (item != null)
                            {
                                this.recentContactCollection.Add(item);
                            }
                        }
                        else if (str2.StartsWith("g"))
                        {
                            InstanceAnswerPro.Core.Community.Community community = ComponentManager.GetCommunitiesManager().GetCommunity(uint.Parse(str2.Substring(1)));
                            if (community != null)
                            {
                                this.recentContactCollection.Add(community);
                            }
                        }
                    }
                }
                catch (Exception)
                {
                }
            }
        }
    }
}
