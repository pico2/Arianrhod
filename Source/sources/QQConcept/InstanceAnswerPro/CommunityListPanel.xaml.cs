using System.Windows.Controls;
using InstanceAnswerPro.Core;
using InstanceAnswerPro.Core.Community;
using System.Windows.Input;
using KernelWrapper;
using System.Windows.Data;
using System.Windows;
using InstanceAnswerPro.API;

namespace InstanceAnswerPro
{
    /// <summary>
    /// Interaction logic for CommunityListPanel.xaml
    /// </summary>
    public partial class CommunityListPanel : UserControl
    {
        private MessageCenter _messageCenter;
        private CommunitiesManager communitiesManager;
        public CommunityListPanel()
        {
            InitializeComponent();
        }
        private void CreateCommunity_CanExecute(object sender, CanExecuteRoutedEventArgs args)
        {
            args.CanExecute = true;
        }

        private void CreateCommunity_Executed(object sender, ExecutedRoutedEventArgs args)
        {
            Util_Group.CreateCommunity();
        }

        private void GlobalMsgSet_CanExecute(object sender, CanExecuteRoutedEventArgs args)
        {
            args.CanExecute = true;
        }

        private void GlobalMsgSet_Executed(object sender, ExecutedRoutedEventArgs e)
        {
            if (e.Parameter is GROUPMSG_RECEIVETYPE)
            {
                GROUPMSG_RECEIVETYPE parameter = (GROUPMSG_RECEIVETYPE)e.Parameter;
                CoreMessenger.Instance.GetService<ITXGroupMgr>().UnifySetGroupListMsgRevType((byte)parameter);
            }
        }

        /// <summary>
        /// 
        /// </summary>
        public void Init()
        {
            this._messageCenter = CoreMessenger.Instance.MessageCenter;
            this.communitiesManager = ComponentManager.GetCommunitiesManager();
            Binding binding = new Binding();
            binding.Source = this.communitiesManager.GetCommunityList();
            this.communityListBox.SetBinding(ItemsControl.ItemsSourceProperty, binding);
        }

        protected void OnItemDoubleClicked(object sender, MouseButtonEventArgs e)
        {
            DependencyObject originalSource = e.OriginalSource as DependencyObject;
            if (originalSource != null)
            {
                ListBox ancestorByType = VisualTree.GetAncestorByType(originalSource, typeof(ListBox)) as ListBox;
                ListBoxItem container = VisualTree.GetAncestorByType(originalSource, typeof(ListBoxItem)) as ListBoxItem;
                if ((ancestorByType != null) && (container != null))
                {
                    Community community = ancestorByType.ItemContainerGenerator.ItemFromContainer(container) as Community;
                    if (community != null)
                    {
                        UICommandMessage message = new UICommandMessage("OpenCommunitySessionWindow", community, null);
                        this._messageCenter.NotifyMessage(message);
                    }
                    e.Handled = true;
                }
            }
        }

        public bool ProcessEnterKey()
        {
            InstanceAnswerPro.Core.Community.Community selectedItem = this.communityListBox.SelectedItem as InstanceAnswerPro.Core.Community.Community;
            if (selectedItem != null)
            {
                UICommandMessage message = new UICommandMessage("OpenCommunitySessionWindow", selectedItem, null);
                this._messageCenter.NotifyMessage(message);
                return true;
            }
            return false;
        }

        private void SearchCommunity_CanExecute(object sender, CanExecuteRoutedEventArgs args)
        {
            args.CanExecute = true;
        }

        private void SearchCommunity_Executed(object sender, ExecutedRoutedEventArgs args)
        {
            Util_Group.SearchCommunity();
        }

    }
}
