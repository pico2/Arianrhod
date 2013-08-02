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
        String savePath = @"J:\Falcom\ED_AO\savedata";

        public SaveDataList()
        {
            InitializeComponent();

            saveDataPathTextBox.Text = savePath;

            for (int i = 0; i != 10; ++i)
            {
                var btn = new SaveDataListItem();

                btn.thumb.Source = new BitmapImage(new Uri(String.Format(@"J:\Falcom\ED_AO\savedata\SAV{0:D4}\icon0.png", i + 1)));

                saveDataList.Items.Add(btn);
            }
        }

        private void saveDataPath_MouseDoubleClick(object sender, MouseButtonEventArgs e)
        {
            // Windows API code pack
            // http://www.cnblogs.com/wdhust/archive/2010/06/07/1753200.html

            var dialog = new System.Windows.Forms.FolderBrowserDialog();
            System.Windows.Forms.DialogResult result;

            dialog.SelectedPath = savePath;
            
            result = dialog.ShowDialog();

            if (result != System.Windows.Forms.DialogResult.OK)
                return;

            savePath = dialog.SelectedPath;
            saveDataPathTextBox.Text = savePath;
        }

        private void refreshSaveList_Click(object sender, RoutedEventArgs e)
        {
            savePath = saveDataPathTextBox.Text;
            System.Windows.MessageBox.Show(savePath);
        }
    }
}
