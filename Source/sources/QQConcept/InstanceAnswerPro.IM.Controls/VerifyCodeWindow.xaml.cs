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
using System.ComponentModel;
using System.IO;

namespace InstanceAnswerPro.IM.Controls
{
    public enum VerifyCodeWindowEventType
    {
        Change,
        Submit,
        Cancel
    }
    public partial class VerifyCodeWindow : Window, INotifyPropertyChanged
    {
        // Fields
        private string _encryptedKey;
        private MemoryStream _memoryStreamPng;
        private string _verifyCodeString = string.Empty;
        private VerifyCodeWindowEventHandler _verifycodewindoweventhandler;
        private string _verifyCodPng;
        internal Button btnCancel;
        internal Button btnChange;
        internal Button btnOK;
        internal TextBox codeTextBox;
        internal TextBlock textBlockInfo;
        internal Image VCImage;

        // Events
        public event PropertyChangedEventHandler PropertyChanged;

        // Methods
        private VerifyCodeWindow(string verifyCodPng, MemoryStream memoryStreamPng)
        {
            base.DataContext = this;
            this._verifyCodPng = verifyCodPng;
            this._memoryStreamPng = memoryStreamPng;
            this.InitializeComponent();
            this.VCImage.Stretch = Stretch.None;
            this.SetImage();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            if (this._verifycodewindoweventhandler == null)
            {
                if (e.Source == this.btnChange)
                {
                    this._verifyCodeString = "";
                    base.DialogResult = true;
                }
                else if (e.Source == this.btnOK)
                {
                    base.DialogResult = true;
                }
                else if (e.Source == this.btnCancel)
                {
                    base.DialogResult = false;
                }
                base.Close();
            }
            else
            {
                if (e.Source == this.btnChange)
                {
                    this._verifyCodeString = "";
                    this._verifycodewindoweventhandler(this, this._encryptedKey, this._verifyCodeString, VerifyCodeWindowEventType.Change);
                }
                else if (e.Source == this.btnOK)
                {
                    this._verifycodewindoweventhandler(this, this._encryptedKey, this._verifyCodeString, VerifyCodeWindowEventType.Submit);
                }
                else if (e.Source == this.btnCancel)
                {
                    this._verifycodewindoweventhandler(this, this._encryptedKey, this._verifyCodeString, VerifyCodeWindowEventType.Cancel);
                }
                this.DisableInput(true);
            }
        }

        public static VerifyCodeWindow CreateWindow(string verifyCodPng, string encryptedKey, Window win, VerifyCodeWindowEventHandler eventHandler)
        {
            return new VerifyCodeWindow(verifyCodPng, null) { _encryptedKey = encryptedKey, Owner = win, _verifycodewindoweventhandler = eventHandler };
        }

        private void DisableInput(bool disable)
        {
            this.btnOK.IsEnabled = !disable;
            this.btnChange.IsEnabled = !disable;
            this.textBlockInfo.Visibility = disable ? Visibility.Visible : Visibility.Collapsed;
        }

        protected override void OnClosed(EventArgs e)
        {
            base.OnClosed(e);
        }

        internal void ReFlash(string src, MemoryStream memoryStreamPng, string EncryptedKey)
        {
            this._encryptedKey = EncryptedKey;
            this._verifyCodPng = src;
            this._memoryStreamPng = memoryStreamPng;
            this.SetImage();
            this.codeTextBox.SelectAll();
            this.codeTextBox.Focus();
            this.DisableInput(false);
        }

        private void SetImage()
        {
            if (!string.IsNullOrEmpty(this._verifyCodPng))
            {
                BitmapImage image = new BitmapImage();
                image.BeginInit();
                image.UriSource = new Uri(this._verifyCodPng, UriKind.Absolute);
                image.EndInit();
                this.VCImage.Source = image;
            }
            else if (this._memoryStreamPng != null)
            {
                BitmapImage image2 = new BitmapImage();
                image2.BeginInit();
                image2.StreamSource = this._memoryStreamPng;
                image2.EndInit();
                this.VCImage.Source = image2;
            }
        }

        internal static bool ShowVerifyCode(MemoryStream memorystreamPng, Window win, out string enterCode)
        {
            VerifyCodeWindow window = new VerifyCodeWindow(null, memorystreamPng)
            {
                Owner = win
            };
            window.ShowDialog();
            enterCode = window.VerifyCodeString;
            return (window.DialogResult == true);
        }

       
        // Properties
        public string VerifyCodeString
        {
            get
            {
                return this._verifyCodeString;
            }
            set
            {
                if (this._verifyCodeString != value)
                {
                    this._verifyCodeString = value;
                    if (this.PropertyChanged != null)
                    {
                        this.PropertyChanged(this, new PropertyChangedEventArgs("VerifyCodeString"));
                    }
                }
            }
        }

        // Nested Types
        public delegate void VerifyCodeWindowEventHandler(object sender, string encryptedKey, string enterCode, VerifyCodeWindowEventType eventType);
    }


}
