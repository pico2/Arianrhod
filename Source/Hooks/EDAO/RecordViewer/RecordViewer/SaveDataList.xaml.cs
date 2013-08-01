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

namespace RecordViewer
{
    /// <summary>
    /// Interaction logic for SaveDataList.xaml
    /// </summary>
    public partial class SaveDataList : PanelContext
    {
        public SaveDataList()
        {
            InitializeComponent();

            for (int i = 0; i != 10; ++i)
            {
                var btn = new SaveDataListItem();

                btn.thumb.Source = new BitmapImage(new Uri(String.Format(@"J:\Falcom\ED_AO\savedata\SAV{0:D4}\icon0.png", i + 1)));

                //saveDataList.Items.Add(btn);
            }
        }
    }
}
