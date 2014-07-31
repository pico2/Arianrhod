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
using System.Windows.Shapes;
using KernelWrapper;
using InstanceAnswerPro.Core;

namespace InstanceAnswerPro.Controls
{
    /// <summary>
    /// Interaction logic for ReLoginWindow.xaml
    /// </summary>
    public partial class ReLoginWindow : Window
    {
        private string _reasontext; 
        private string _pwdstring;

        public ReLoginWindow(string reason)
        {
            this._reasontext = reason;

            InitializeComponent();
        }
        private ITXBuffer GetPassWord()
        {
            return CoreMessenger.CalculatePasswordHash(this._pwdstring);
        }
        internal static bool ShowReLoginWindow(string reason, Window win, out ITXBuffer ppbufPwd)
        {
            ReLoginWindow window = new ReLoginWindow(reason)
            {
                Owner = win
            };
            window.ShowDialog();
            ppbufPwd = window.GetPassWord();
            return (window.DialogResult == true);
        }
        private void StackPanel_Click(object sender, RoutedEventArgs e)
        {
            if (e.Source == this.btnOK)
            {
                base.DialogResult = true;
            }
            else if (e.Source == this.btnCancel)
            {
                base.DialogResult = false;
            }
            base.Close();
        }
        // Properties
        public string PwdString
        {
            get
            {
                return this._pwdstring;
            }
            set
            {
                if (this._pwdstring != value)
                {
                    this._pwdstring = value;
                }
            }
        }

        public string ReasonText
        {
            get
            {
                return this._reasontext;
            }
        }


    }
}
