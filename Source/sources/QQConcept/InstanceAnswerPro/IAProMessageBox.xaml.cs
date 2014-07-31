using System;
using System.Windows;
using System.Windows.Documents;
using System.Windows.Markup;
using System.Windows.Media.Imaging;
using Bama.Controls;
using Bama.QQ.Core;
using Bama.WPF.Utility;
using InstanceAnswerPro.Controls;

namespace InstanceAnswerPro
{
    /// <summary>
    /// Interaction logic for IAProMessageBox.xaml
    /// </summary>
    public partial class IAProMessageBox : CustomWindow, IComponentConnector, IStyleConnector
    {
        public IAProMessageBox()
        {
            this.DoModel = true;
            this.NeedOwner = true;
            this.ShowMiniBox = false;
            this.MessageBoxResult = MessageBoxResult.None;
            InitializeComponent();
        }
        private void Hyperlink_Click(object sender, RoutedEventArgs e)
        {
            Hyperlink hyperlink = sender as Hyperlink;
            if (hyperlink != null)
            {
                HyperLinkObj tag = hyperlink.Tag as HyperLinkObj;
                if (tag != null)
                {
                    if (tag is HyperLinkObj_Url)
                    {
                        HyperLinkObj_Url url = tag as HyperLinkObj_Url;
                        BrowserHelper.OpenUrl(BrowserType.System, url.Url);
                    }
                    else
                    {
                        DebugLog.Assert(false, "响应未处理");
                    }
                }
            }
        }
        private void Init()
        {
            if (this.Inlines != null)
            {
                Inline[] array = new Inline[this.Inlines.Count];
                this.Inlines.CopyTo(array, 0x0);
                foreach (Inline inline in array)
                {
                    this.paragraph_Info.Inlines.Add(inline);
                }
            }
            else
            {
                Util_MessageBox.AnalyzeUrl(this.paragraph_Info, this.MessageBoxText);
            }
            if (string.IsNullOrEmpty(this.Caption))
            {
                base.Title = "QQ";
            }
            else
            {
                base.Title = this.Caption;
            }
            if (this.MessageBoxImage != MessageBoxImage.None)
            {
                this.iconInfo.Visibility = Visibility.Visible;
                string str = null;
                switch (this.MessageBoxImage)
                {
                    case MessageBoxImage.Hand:
                        str = "Error.png";
                        break;

                    case MessageBoxImage.Question:
                        str = "Question.png";
                        break;

                    case MessageBoxImage.Exclamation:
                        str = "Warning.png";
                        break;

                    case MessageBoxImage.Asterisk:
                        str = "Information.png";
                        break;

                    default:
                        this.iconInfo.Visibility = Visibility.Collapsed;
                        break;
                }
                string uriString = "pack://application:,,,/Bama.QQ.Controls;Component/res/IAProMessageBox/" + str;
                BitmapImage image = new BitmapImage();
                image.BeginInit();
                image.UriSource = new Uri(uriString);
                image.EndInit();
                this.iconInfo.Source = image;
            }
            switch (this.MessageBoxButton)
            {
                case MessageBoxButton.OK:
                    this.okButton.Visibility = Visibility.Visible;
                    this.okButton.Focus();
                    this.okButton.IsCancel = true;
                    this.okButton.IsDefault = true;
                    this.MessageBoxResult = MessageBoxResult.OK;
                    return;

                case MessageBoxButton.OKCancel:
                    this.okButton.Visibility = Visibility.Visible;
                    this.cancelButton.Visibility = Visibility.Visible;
                    this.okButton.Focus();
                    this.okButton.IsDefault = true;
                    this.cancelButton.IsCancel = true;
                    this.MessageBoxResult = MessageBoxResult.Cancel;
                    return;

                case ((MessageBoxButton)0x2):
                    break;

                case MessageBoxButton.YesNoCancel:
                    this.yesButton.Visibility = Visibility.Visible;
                    this.noButton.Visibility = Visibility.Visible;
                    this.cancelButton.Visibility = Visibility.Visible;
                    this.yesButton.Focus();
                    this.yesButton.IsDefault = true;
                    this.cancelButton.IsCancel = true;
                    this.MessageBoxResult = MessageBoxResult.Cancel;
                    break;

                case MessageBoxButton.YesNo:
                    this.yesButton.Visibility = Visibility.Visible;
                    this.noButton.Visibility = Visibility.Visible;
                    this.yesButton.Focus();
                    this.yesButton.IsDefault = true;
                    this.noButton.IsCancel = true;
                    this.MessageBoxResult = MessageBoxResult.No;
                    return;

                default:
                    return;
            }
        }
        private static MessageBoxResult InlineShow(Window owner, IAProMessageBox messageBox)
        {
            if (messageBox.NeedOwner)
            {
                if (owner != null)
                {
                    messageBox.Owner = owner;
                }
                else if (messageBox.Owner != WindowHelper.MainFrame)
                {
                    messageBox.Owner = WindowHelper.MainFrame;
                }
            }
            if (messageBox.MessageBoxImage == MessageBoxImage.None)
            {
                messageBox.MessageBoxImage = MessageBoxImage.Asterisk;
            }
            messageBox.Init();
            if (messageBox.DoModel)
            {
                messageBox.ShowDialog();
            }
            else
            {
                messageBox.Show();
            }
            return messageBox.MessageBoxResult;
        }

        private void OkButton_Click(object sender, RoutedEventArgs e)
        {
            if (sender == this.okButton)
            {
                this.MessageBoxResult = MessageBoxResult.OK;
            }
            else if (sender == this.cancelButton)
            {
                this.MessageBoxResult = MessageBoxResult.Cancel;
            }
            else if (sender == this.yesButton)
            {
                this.MessageBoxResult = MessageBoxResult.Yes;
            }
            else if (sender == this.noButton)
            {
                this.MessageBoxResult = MessageBoxResult.No;
            }
            base.Close();
        }
        protected override void OnClosed(EventArgs e)
        {
            base.OnClosed(e);
        }

        public static MessageBoxResult Show(Window owner, string messageBoxText)
        {
            return Show(owner, messageBoxText, "", MessageBoxButton.OK, MessageBoxImage.None);
        }

        public static MessageBoxResult Show(Window owner, string messageBoxText, string caption)
        {
            return Show(owner, messageBoxText, caption, MessageBoxButton.OK, MessageBoxImage.None);
        }

        public static MessageBoxResult Show(Window owner, InlineCollection inlines, string caption)
        {
            return Show(owner, inlines, caption, MessageBoxButton.OK, MessageBoxImage.None);
        }

        public static MessageBoxResult Show(Window owner, string messageBoxText, string caption, MessageBoxButton button)
        {
            return Show(owner, messageBoxText, caption, button, MessageBoxImage.None);
        }

        public static MessageBoxResult Show(Window owner, string messageBoxText, string caption, MessageBoxButton button, MessageBoxImage icon)
        {
            IAProMessageBox bamaMessageBox = new IAProMessageBox
            {
                MessageBoxText = messageBoxText,
                Caption = caption,
                MessageBoxButton = button,
                MessageBoxImage = icon
            };
            return InlineShow(owner, bamaMessageBox);
        }

        public static MessageBoxResult Show(Window owner, InlineCollection inlines, string caption, MessageBoxButton messageBoxButton, MessageBoxImage messageBoxImage)
        {
            IAProMessageBox bamaMessageBox = new IAProMessageBox
            {
                Inlines = inlines,
                Caption = caption,
                MessageBoxButton = messageBoxButton,
                MessageBoxImage = messageBoxImage
            };
            return InlineShow(owner, bamaMessageBox);
        }

        public static void ShowNormal(string messageBoxText)
        {
            IAProMessageBox bamaMessageBox = new IAProMessageBox
            {
                MessageBoxText = messageBoxText,
                DoModel = false,
                NeedOwner = false
            };
            InlineShow(null, bamaMessageBox);
        }
        // Properties
        private string Caption { get; set; }

        private bool DoModel { get; set; }

        private InlineCollection Inlines { get; set; }

        private MessageBoxButton MessageBoxButton { get; set; }

        private MessageBoxImage MessageBoxImage { get; set; }

        private MessageBoxResult MessageBoxResult { get; set; }

        private string MessageBoxText { get; set; }

        private bool NeedOwner { get; set; }


    }
}
