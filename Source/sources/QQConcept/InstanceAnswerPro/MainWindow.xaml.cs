using System;
using System.ComponentModel;
using System.Runtime.InteropServices;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Controls.Primitives;
using System.Windows.Data;
using System.Windows.Input;
using System.Windows.Interop;
using InstanceAnswerPro.Core;
using InstanceAnswerPro.IM.Controls;
using KernelWrapper;
using InstanceAnswerPro.API;
namespace InstanceAnswerPro
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        private FilterType _filterType;
        private bool _initAfterFirstLogin;
        private MessageCenter _messageCenter;
        private static BuddyList buddyList;
        private BuddyManager buddyManager;
        private MessageMonitor messagemonitor;
        private CoreMessenger messenger;
        public MainWindow()
        {
            this.messenger = App.Messenger;
            this.buddyManager = ComponentManager.GetBuddyManager();
            this._messageCenter = App.Messenger.MessageCenter;

            InitializeComponent();

            this.messenger.LoginCompleted += new EventHandler<LoginEventArgs>(this.OnLogin);
            this.messenger.ConnectionStatusChanged += new EventHandler<ConnectionStatusChangeEventArgs>(this.messenger_ConnectionStatusChanged);
            this.messagemonitor = InstanceAnswerPro.Core.ComponentManager.GetMessageMonitor();
            Buddy.BuddyPropertyChanged += new PropertyChangedEventHandler(this.Buddy_BuddyPropertyChanged);
        }
        /// <summary>
        /// 定义Buddy属性变更执行操作
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void Buddy_BuddyPropertyChanged(object sender, PropertyChangedEventArgs e)
        {
            if ((("PresenceInfo" == e.PropertyName) && ((this._filterType & FilterType.FilterByOnline) == FilterType.FilterByOnline)) && ((this._filterType & FilterType.FilterByUin) != FilterType.FilterByUin))
            {
                Buddy buddy = sender as Buddy;
                if (buddy.PresenceInfo.IsOnline)
                {
                    buddy.VisibilityInContactPanel = Visibility.Visible;
                }
                else
                {
                    buddy.VisibilityInContactPanel = Visibility.Collapsed;
                }
            }
        }
        private void SetTopMost(bool p)
        {
            this.messenger.TM.SetTopMost(p);
            base.Topmost = p;
        }

        /// <summary>
        /// 定义设置变化执行的操作
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void Settings_PropertyChanged(object sender, PropertyChangedEventArgs e)
        {
            if (e.PropertyName == Util_UserSettings_MainPanel.TopMostProperty)
            {
                this.SetTopMost(Util_UserSettings_MainPanel.Instance.TopMost);
            }
            else if (e.PropertyName == Util_UserSettings_MainPanel.AutoHideProperty)
            {
                this.messenger.TM.EnableAutoHide(Util_UserSettings_MainPanel.Instance.AutoHide);
            }
        }

        /// <summary>
        /// 主面板卸载时候的操作
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void MainPanel_Unloaded(object sender, RoutedEventArgs e)
        {
            base.Unloaded -= new RoutedEventHandler(this.MainPanel_Unloaded);
            Util_UserSettings_MainPanel.Instance.PropertyChanged -= new PropertyChangedEventHandler(this.Settings_PropertyChanged);
        }

        /// <summary>
        /// 设置窗口行为
        /// </summary>
        /// <param name="hwnd"></param>
        private void SetWindowBehavior(IntPtr hwnd)
        {
            this.messenger.TM.SetMainPanelHWnd((uint)hwnd.ToInt32());
            this.SetTopMost(Util_UserSettings_MainPanel.Instance.TopMost);
            this.messenger.TM.EnableAutoHide(Util_UserSettings_MainPanel.Instance.AutoHide);
            this.messenger.TM.ShowHiddenAppBar(false);
        }
        /// <summary>
        /// 主面板加载时的操作，包括绑定事件，设置窗口行为，重置MemoryManager
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void MainPanel_Loaded(object sender, RoutedEventArgs e)
        {

            base.Unloaded += new RoutedEventHandler(this.MainPanel_Unloaded);
            base.Loaded -= new RoutedEventHandler(this.MainPanel_Loaded);
            Util_UserSettings_MainPanel.Instance.PropertyChanged += new PropertyChangedEventHandler(this.Settings_PropertyChanged);
            IntPtr handle = new WindowInteropHelper(this).Handle;
            this.SetWindowBehavior(handle);
            MemoryManager.ResetWorkingSet();

        }
        /// <summary>
        /// 判断是否是QZone标记
        /// </summary>
        /// <param name="visual"></param>
        /// <returns></returns>
        public static bool IsQZoneFlag(DependencyObject visual)
        {
            System.Windows.Controls.Image image = visual as System.Windows.Controls.Image;
            bool flag = false;
            if (image != null)
            {
                string tag = image.Tag as string;
                if ((tag != null) && (tag.CompareTo("QZoneFlag") == 0))
                {
                    flag = true;
                }
            }
            return flag;
        }
        /// <summary>
        /// 连接状态变化
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="args"></param>
        private void messenger_ConnectionStatusChanged(object sender, ConnectionStatusChangeEventArgs args)
        {
            switch (args.EventType)
            {
                case ConnectionStatusChangeEventType.Broken:
                    break;

                case ConnectionStatusChangeEventType.KickedOut:
                    if (IMMessageBox.ServerKickoutMsgBox(this) == MessageBoxResult.Yes)
                    {
                        App.Messenger.Relogin();
                    }
                    break;

                default:
                    return;
            }
        }
        /// <summary>
        /// 绑定联系人到“联系人”面板
        /// </summary>
        private void BindContactList()
        {
            this.contactListPanel.BindContactList(buddyList);
        }
        /// <summary>
        /// 绑定昵称
        /// </summary>
        private void BindLongNickName()
        {
            System.Windows.Data.Binding binding = new System.Windows.Data.Binding("LongNickName")
            {
                Source = buddyList.Self,

                Mode = BindingMode.OneWay
            };
            this.longNickName.SetBinding(System.Windows.Controls.TextBox.TextProperty, binding);
        }

        /// <summary>
        /// 状态变化
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void status_SourceUpdated(object sender, DataTransferEventArgs e)
        {
            if ((e.Property == Selector.SelectedValueProperty) && (sender == this.status))
            {
                Util_DataReport.RID_Count_ClickStatusButton();
                ITXIM service = CoreMessenger.Instance.GetService<ITXIM>();
                try
                {
                    service.ChangeStatus((ushort)Util_Buddy.GetCurrentBuddy().PresenceInfo.Presence, "", null);
                }
                finally
                {
                    Marshal.ReleaseComObject(service);
                }
            }
        }

        /// <summary>
        /// 绑定当前账号
        /// </summary>
        private void BindSelf()
        {
            System.Windows.Data.Binding binding = new System.Windows.Data.Binding("NickName")
            {
                Source = buddyList.Self
            };
            this.userName.SetBinding(TextBlock.TextProperty, binding);
            this.BindLongNickName();
            binding = new System.Windows.Data.Binding("PresenceInfo.Presence")
            {
                Source = buddyList.Self,
                Mode = BindingMode.TwoWay,
                NotifyOnTargetUpdated = true,
                NotifyOnSourceUpdated = true
            };
            //this.status.SetBinding(Selector.SelectedValueProperty, binding);
            //this.status.SourceUpdated += new EventHandler<DataTransferEventArgs>(this.status_SourceUpdated);
            //this.avatar.Buddy = buddyList.Self;
        }

        /// <summary>
        /// 登陆成功后触发此操作
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void OnLogin(object sender, LoginEventArgs e)
        {
            if (e.Succeeded)
            {
                try
                {
                    this.buddyManager.Refresh();
                    this.InitAfterFirstLogin();
                    buddyList = BuddyListBuilder.Instance.Build(false);
                    this.BindContactList();
                    this.BindSelf();
                    ContactSortManager.RequestSorting(true);
                    //DelayTask.DelayRun(0x7d0, delegate(DelayTask task, object obj)
                    //{
                    //    EmoticonShow.Init();
                    //});
                    //if (this._desktopBuddyCollection == null)
                    //{
                    //    this._desktopBuddyCollection = Util_UserSettings_DesktopBuddy.DesktopBuddyCollection;
                    //    foreach (DesktopBuddyInfo info in this._desktopBuddyCollection)
                    //    {
                    //        System.Windows.Point point = new System.Windows.Point((double)info.Left, (double)info.Top);
                    //        Buddy buddy = BuddyListBuilder.Instance.FindOrCreateBuddy(info.Uin, false, false);
                    //        if (buddy != null)
                    //        {
                    //            Util_Buddy.OpenContactSessionWindow(buddy, new Util_Buddy.BuddySessionParameter { ContactSessionWindowStatus = Util_Buddy.ContactSessionWindowStatus.Avatar, WindowPosition = point, OpenFromDesktopBuddy = false });
                    //        }
                    //    }
                    //}
                }
                catch (Exception)
                {
                }
            }
        }

        /// <summary>
        /// 第一次登陆之后的初始化操作，初始化BuddyListBuilder.Instance，绑定排序事件，初始化联系人面板，加载消息列表面板
        /// </summary>
        private void InitAfterFirstLogin()
        {
            if (!this._initAfterFirstLogin)
            {
                this._initAfterFirstLogin = true;
                try
                {
                    BuddyListBuilder.Instance.Initialize();
                    //ContactSortManager.SortEvent += new EventHandler<EventArgs>(this.OnSort);
                    //CommunitiesSortManager.SortEvent += new EventHandler<EventArgs>(this.OnCommunitiesSort);
                    this.communityListPanel.Init();
                    this.messageListPanel.Load();
                }
                catch (Exception)
                {
                }
            }
        }
        private void OnCommunitiesSort(object sender, EventArgs args)
        {
            ICollectionView defaultView = CollectionViewSource.GetDefaultView(InstanceAnswerPro.Core.ComponentManager.GetCommunitiesManager().GetCommunityList());
            if (defaultView == null)
            {
                DebugLog.Assert(false, "严重错误，必看");
            }
            else if (defaultView.SortDescriptions.Count != 1)
            {
                defaultView.SortDescriptions.Clear();
                defaultView.SortDescriptions.Add(new SortDescription("CombineName", ListSortDirection.Ascending));
            }
            else
            {
                defaultView.Refresh();
            }
        }
        private void OnSort(object sender, EventArgs args)
        {
            if (this.BuddyList != null)
            {
                foreach (BuddyGroup group in this.BuddyList)
                {
                    ICollectionView defaultView = CollectionViewSource.GetDefaultView(group);
                    if (defaultView == null)
                    {
                        DebugLog.Assert(false, "严重错误，必看");
                    }
                    else
                    {
                        if (defaultView.SortDescriptions.Count != 3)
                        {
                            defaultView.SortDescriptions.Clear();
                            defaultView.SortDescriptions.Add(new SortDescription("PresenceInfo.PresenceWeight", ListSortDirection.Descending));
                            defaultView.SortDescriptions.Add(new SortDescription("QQMemberWeight", ListSortDirection.Descending));
                            defaultView.SortDescriptions.Add(new SortDescription("NickName", ListSortDirection.Ascending));
                            continue;
                        }
                        defaultView.Refresh();
                    }
                }
            }
        }
        internal InstanceAnswerPro.Core.BuddyList BuddyList
        {
            get
            {
                return buddyList;
            }
        }
        private enum FilterType
        {
            None,
            FilterByOnline,
            FilterByUin
        }
        public static Buddy Self
        {
            get
            {
                return buddyList.Self;
            }
        }
        /// <summary>
        /// 执行群组成员管理
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void CommunitymemberMgr_Executed(object sender, ExecutedRoutedEventArgs e)
        {
            DependencyObject originalSource = e.OriginalSource as DependencyObject;
            if (originalSource != null)
            {
                ListBox ancestorByType = VisualTree.GetAncestorByType(originalSource, typeof(ListBox)) as ListBox;
                ListBoxItem container = VisualTree.GetAncestorByType(originalSource, typeof(ListBoxItem)) as ListBoxItem;
                if ((ancestorByType != null) && (container != null))
                {
                    InstanceAnswerPro.Core.Community.Community community = ancestorByType.ItemContainerGenerator.ItemFromContainer(container) as InstanceAnswerPro.Core.Community.Community;
                    if ((community != null) && Util_Group.IsManager(community, Util_Buddy.GetCurrentBuddy().Uin))
                    {
                        Util_Group.OpenCommunityInfoWindow(community, Util_Group.CommunityInfoWindowPageTag.PageMemberInfo);
                    }
                }
            }
        }
        private int lastSearchTextLength;

        private void window_PreviewKeyDown(object sender, KeyEventArgs e)
        {
            if (((e.Key == Key.Return) && (this.lastSearchTextLength <= 0x0)) && !this.longNickName.IsFocused)
            {
                if (this.contactListPanel.Visibility == Visibility.Visible)
                {
                    e.Handled = this.contactListPanel.ProcessEnterKey();
                }
                else if (this.communityListPanel.Visibility == Visibility.Visible)
                {
                    e.Handled = this.communityListPanel.ProcessEnterKey();
                }
                else if (this.messageListPanel.Visibility == Visibility.Visible)
                {
                    e.Handled = this.messageListPanel.ProcessEnterKey();
                }
            }
        }

        protected override void OnClosed(EventArgs e)
        {
            Util_UserSettings_DesktopBuddy.Save();
            this.messageListPanel.Save();
            this.status.SourceUpdated -= new EventHandler<DataTransferEventArgs>(this.status_SourceUpdated);
            this.messenger.LoginCompleted -= new EventHandler<LoginEventArgs>(this.OnLogin);
            this.messenger.ConnectionStatusChanged -= new EventHandler<ConnectionStatusChangeEventArgs>(this.messenger_ConnectionStatusChanged);

            Buddy.BuddyPropertyChanged -= new PropertyChangedEventHandler(this.Buddy_BuddyPropertyChanged);
            HotKeyMgr hotKeyMgr = ComponentManager.GetHotKeyMgr();
            //if (hotKeyMgr != null)
            //{
            //    hotKeyMgr.UnsetHotKeyEvent(HotKeyMgr.HotKeyType.GetMsg, new EventHandler<EventArgs>(this.HotKeyEvent));
            //    hotKeyMgr.UnsetHotKeyEvent(HotKeyMgr.HotKeyType.Capture, new EventHandler<EventArgs>(this.HotKeyEvent));
            //}
            //if (this.systemTray != null)
            //{
            //    this.systemTray.Hide();
            //}
            this.messenger.ConnectionStatusChanged -= new EventHandler<ConnectionStatusChangeEventArgs>(this.messenger_ConnectionStatusChanged);
            //App.UnloadModules();
            this.messenger.WindowManager.CloseAll(null);
            base.OnClosed(e);
            ContactSortManager.SortEvent -= new EventHandler<EventArgs>(this.OnSort);
            CommunitiesSortManager.SortEvent -= new EventHandler<EventArgs>(this.OnCommunitiesSort);
            Application.Current.Shutdown();
        }

        /// <summary>
        /// 检查点击对象，执行相应操作，主要是QZone
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        protected void OnItemClicked(object sender, MouseButtonEventArgs e)
        {
            DependencyObject originalSource = e.OriginalSource as DependencyObject;
            if ((originalSource != null) && IsQZoneFlag(originalSource))
            {
                ListBox ancestorByType = VisualTree.GetAncestorByType(originalSource, typeof(ListBox)) as ListBox;
                ListBoxItem container = VisualTree.GetAncestorByType(originalSource, typeof(ListBoxItem)) as ListBoxItem;
                if ((ancestorByType != null) && (container != null))
                {
                    Buddy buddy = ancestorByType.ItemContainerGenerator.ItemFromContainer(container) as Buddy;
                    if (buddy != null)
                    {
                        Util_Buddy.ViewQZone(buddy, null);
                    }
                }
                e.Handled = true;
            }
        }


    }


}
