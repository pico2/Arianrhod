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
using InstanceAnswerPro.Core;
using InstanceAnswerPro.API;

namespace InstanceAnswerPro.IM.Controls
{
    public class QZoneCtrl : UserControl
    {

        // Methods
        public QZoneCtrl()
        {
            this.InitializeComponent();
        }


        private void ListBoxMouseLeftButtonUp(object sender, MouseEventArgs e)
        {
            if (base.DataContext is Buddy)
            {
                ListBoxItem ancestorByType = VisualTree.GetAncestorByType(e.OriginalSource as DependencyObject, typeof(ListBoxItem)) as ListBoxItem;
                if (ancestorByType != null)
                {
                    PhotoInfo info = this.listPhoto.ItemContainerGenerator.ItemFromContainer(ancestorByType) as PhotoInfo;
                    if (info != null)
                    {
                        Util_Buddy.ViewQZone(base.DataContext as Buddy, info.PhotoJumpUrl);
                    }
                }
            }
        }

        private void MouseEvent(object sender, MouseEventArgs e)
        {
            if (e.RoutedEvent == Mouse.MouseEnterEvent)
            {
                if (e.Source == this.texttitle)
                {
                    this.texttitle.TextDecorations = TextDecorations.Underline;
                }
                else if (e.Source == this.textcontent)
                {
                    this.textcontent.TextDecorations = TextDecorations.Underline;
                }
            }
            else if (e.RoutedEvent == Mouse.MouseLeaveEvent)
            {
                if (e.Source == this.texttitle)
                {
                    this.texttitle.TextDecorations = null;
                }
                else if (e.Source == this.textcontent)
                {
                    this.textcontent.TextDecorations = null;
                }
            }
            else if (e.RoutedEvent == UIElement.MouseLeftButtonUpEvent)
            {
                if (base.DataContext is Buddy)
                {
                    Buddy dataContext = base.DataContext as Buddy;
                    if ((e.Source == this.texttitle) || (e.Source == this.textcontent))
                    {
                        Util_Buddy.ViewQZone(dataContext, dataContext.QZoneInfo.AbstractUrl);
                    }
                }
            }
            else if (e.RoutedEvent == UIElement.MouseLeftButtonDownEvent)
            {
                e.Handled = true;
            }
        }
       
    }


}
