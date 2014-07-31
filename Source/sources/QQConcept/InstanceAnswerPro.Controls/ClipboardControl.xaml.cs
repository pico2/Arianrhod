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

namespace InstanceAnswerPro.Controls
{
    public partial class ClipboardControl : UserControl
    {

        // Methods
        public ClipboardControl()
        {
            this.InitializeComponent();
        }

        // Properties
        public string ControlType { get; set; }

        public string ImagePath { get; set; }

        public string SysId { get; set; }
    }


}
