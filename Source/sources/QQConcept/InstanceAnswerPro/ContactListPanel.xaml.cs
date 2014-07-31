using System.Windows.Controls;
using System.Windows.Data;
using InstanceAnswerPro.Core;
using System.Windows.Controls.Primitives;
using System.Windows;
using System.Collections;
using System.Windows.Input;
using System;
using System.Windows.Media;
using System.Collections.Generic;
using System.Windows.Documents;

namespace InstanceAnswerPro
{
    public partial class ContactListPanel : UserControl
    {
        // Fields
        private List<TreeViewItem> collapsedList;
        public static readonly DependencyProperty ContactItemHeightProperty;
        
        public static readonly DependencyProperty MaxItemHeightProperty = DependencyProperty.Register("MaxItemHeight", typeof(int), typeof(ContactListPanel), new UIPropertyMetadata(0x30));
        
        public static readonly DependencyProperty MinItemHeightProperty = DependencyProperty.Register("MinItemHeight", typeof(int), typeof(ContactListPanel), new UIPropertyMetadata(0x1c));

        // Methods
        static ContactListPanel()
        {
            ContactItemHeightProperty = DependencyProperty.Register("ContactItemHeight", typeof(double), typeof(ContactListPanel), new FrameworkPropertyMetadata(30.0, delegate(DependencyObject s, DependencyPropertyChangedEventArgs e)
            {
                double newValue = (double)e.NewValue;
                if (newValue < 0.0)
                {
                    newValue = 0.0;
                }
            }));
        }

        public ContactListPanel()
        {
            //this.qqtips =  new QQTipsFrame();
            this.InitializeComponent();
            //this.qqtips.AddUI(base.Resources["QQBuddyTips"] as UIElement);
        }

        /// <summary>
        /// 绑定联系人列表到“联系人”面板
        /// </summary>
        /// <param name="buddyList"></param>
        public void BindContactList(BuddyList buddyList)
        {
            Binding binding = new Binding
            {
                Source = buddyList
            };
            this.buddyTree.SetBinding(ItemsControl.ItemsSourceProperty, binding);
        }

        /// <summary>
        /// 展开所有分组
        /// </summary>
        public void ExpandAllGroups()
        {
            foreach (BuddyGroup group in (IEnumerable)this.buddyTree.Items)
            {
                TreeViewItem item = this.buddyTree.ItemContainerGenerator.ContainerFromItem(group) as TreeViewItem;
                if ((item != null) && !item.IsExpanded)
                {
                    item.IsExpanded = true;
                }
            }
        }

        public Point GetPositionReletiveToContainer(StylusEventArgs e, Window win)
        {
            return e.GetPosition(win);
        }

        /// <summary>
        /// 双击联系人头像
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        protected void OnItemDoubleClicked(object sender, MouseButtonEventArgs e)
        {
            Action method = null;
            Buddy buddy;
            DependencyObject originalSource = e.OriginalSource as DependencyObject;
            if (originalSource != null)
            {
                if (originalSource is Run)
                {
                    originalSource = (originalSource as Run).Parent;
                }
                if ((originalSource is Visual) && !MainWindow.IsQZoneFlag(originalSource))
                {
                    buddy = this.contactListPanel.buddyTree.SelectedItem as Buddy;
                    if ((buddy != null) && (buddy != Util_Buddy.GetCurrentBuddy()))
                    {
                        if (method == null)
                        {
                            method = delegate
                            {
                                Util_Buddy.OpenContactSessionWindow(buddy);
                            };
                        }
                        base.Dispatcher.BeginInvoke(method, new object[0]);
                        e.Handled = true;
                    }
                }
            }
        }

 


        /// <summary>
        /// 鼠标进入
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void OnItemMouseEnter(object sender, MouseEventArgs e)
        {
            TreeViewItem item = sender as TreeViewItem;
            Image tag = null;
            if (item.Tag is Image)
            {
                tag = item.Tag as Image;
            }
            else
            {
                tag = ElementTreeHelper.FindVisualChild<Image>(sender as Visual);
                item.Tag = tag;
            }
            //this.qqtips.PlacementTarget = tag;
        }
        /// <summary>
        /// 右键按下
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void OnItemMouseRightButtonDown(object sender, MouseButtonEventArgs e)
        {
            TreeViewItem item = sender as TreeViewItem;
            if (item != null)
            {
                item.IsSelected = true;
            }
        }

        /// <summary>
        /// 回车键
        /// </summary>
        /// <returns></returns>
        public bool ProcessEnterKey()
        {
            Buddy selectedItem = this.buddyTree.SelectedItem as Buddy;
            if ((selectedItem != null) && (selectedItem != Util_Buddy.GetCurrentBuddy()))
            {
                Util_Buddy.OpenContactSessionWindow(selectedItem);
                return true;
            }
            return false;
        }
        public void ReleaseCapturedStylus()
        {
            base.ReleaseStylusCapture();
        }

        public void RestoreCollapsedGroups()
        {
            if ((this.collapsedList != null) && (this.collapsedList.Count != 0x0))
            {
                foreach (TreeViewItem item in this.collapsedList)
                {
                    if (item.IsExpanded)
                    {
                        item.IsExpanded = false;
                    }
                }
            }
        }

        public void SaveCollapsedGroups()
        {
            if (this.collapsedList == null)
            {
                this.collapsedList = new List<TreeViewItem>();
            }
            else
            {
                this.collapsedList.Clear();
            }
            foreach (BuddyGroup group in (IEnumerable)this.buddyTree.Items)
            {
                TreeViewItem item = this.buddyTree.ItemContainerGenerator.ContainerFromItem(group) as TreeViewItem;
                if ((item != null) && !item.IsExpanded)
                {
                    this.collapsedList.Add(item);
                }
            }
        }

        /// <summary>
        /// 文本区域左键起，打开资料窗口
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void TextBlock_MouseLeftButtonUp(object sender, MouseButtonEventArgs e)
        {
            if (sender is TextBlock)
            {
                TextBlock block = sender as TextBlock;
                Util_Buddy.OpenProfileWindow((uint)block.Tag);
            }
        }


        // Properties
        public double ContactItemHeight
        {
            get
            {
                return (double)base.GetValue(ContactItemHeightProperty);
            }
            set
            {
                base.SetValue(ContactItemHeightProperty, value);
            }
        }

        public int MaxItemHeight
        {
            get
            {
                return (int)base.GetValue(MaxItemHeightProperty);
            }
            set
            {
                base.SetValue(MaxItemHeightProperty, value);
            }
        }

        public int MinItemHeight
        {
            get
            {
                return (int)base.GetValue(MinItemHeightProperty);
            }
            set
            {
                base.SetValue(MinItemHeightProperty, value);
            }
        }
    }


}
