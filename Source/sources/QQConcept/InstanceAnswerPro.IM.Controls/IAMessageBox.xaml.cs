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
    public partial class IAMessageBox : Window
    {
        // Fields
        internal Button cancelButton;
        internal Image iconInfo;
        internal Button noButton;
        internal Button okButton;
        internal TextBlock paragraph_Info;
        internal Button yesButton;

        // Methods
        private IAMessageBox()
        {
            this.DoModel = true;
            this.NeedOwner = true;
            this.MessageBoxResult = MessageBoxResult.None;
            this.InitializeComponent();
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
                this.Inlines.CopyTo(array, 0);
                foreach (Inline inline in array)
                {
                    this.paragraph_Info.Inlines.Add(inline);
                }
            }
            else
            {
                IMMessageBox.AnalyzeUrl(this.paragraph_Info, this.MessageBoxText);
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
                string uriString = "pack://application:,,,/Bama.QQ.Controls;Component/res/BamaMessageBox/" + str;
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

                case ((MessageBoxButton)2):
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

        

        private static MessageBoxResult InlineShow(Window owner, IAMessageBox messageBox)
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
            IAMessageBox box2 = new IAMessageBox
            {
                MessageBoxText = messageBoxText,
                Caption = caption,
                MessageBoxButton = button,
                MessageBoxImage = icon
            };
            IAMessageBox iAMessageBox = box2;
            return InlineShow(owner, iAMessageBox);
        }

        public static MessageBoxResult Show(Window owner, InlineCollection inlines, string caption, MessageBoxButton messageBoxButton, MessageBoxImage messageBoxImage)
        {
            IAMessageBox box2 = new IAMessageBox
            {
                Inlines = inlines,
                Caption = caption,
                MessageBoxButton = messageBoxButton,
                MessageBoxImage = messageBoxImage
            };
            IAMessageBox bamaMessageBox = box2;
            return InlineShow(owner, bamaMessageBox);
        }

        public static void ShowNormal(string messageBoxText)
        {
            IAMessageBox box2 = new IAMessageBox
            {
                MessageBoxText = messageBoxText,
                DoModel = false,
                NeedOwner = false
            };
            IAMessageBox bamaMessageBox = box2;
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
