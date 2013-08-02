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
using System.IO;

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

            RefreshSaveData();
        }

        List<String> QuerySaveDatas(String SaveDataPath)
        {
            return new List<String>(Directory.EnumerateDirectories(SaveDataPath));
        }

        void RefreshSaveData()
        {
            List<String> list;

            saveDataList.Items.Clear();

            try
            {
                list = QuerySaveDatas(savePath);
            }
            catch
            {
                return;
            }

            foreach (var save in list)
            {
                try
                {
                    EDAOSaveData savedata = new EDAOSaveData(save + "\\savedata.dat");

                    var item = new SaveDataListItem(savedata);
                    this.saveDataList.Items.Add(item);
                }
                catch
                {
                }
            }
        }

        private void saveDataPath_MouseDoubleClick(object sender, MouseButtonEventArgs e)
        {
            try
            {
                var dialog = new Microsoft.WindowsAPICodePack.Dialogs.CommonOpenFileDialog();

                dialog.IsFolderPicker = true;
                dialog.InitialDirectory = savePath;
                dialog.DefaultFileName = savePath;

                var result = dialog.ShowDialog();

                if (result != Microsoft.WindowsAPICodePack.Dialogs.CommonFileDialogResult.Ok)
                    return;

                savePath = dialog.FileName;
            }
            catch (System.PlatformNotSupportedException)
            {
                var dialog = new System.Windows.Forms.FolderBrowserDialog();

                dialog.SelectedPath = savePath;

                var result = dialog.ShowDialog();

                if (result != System.Windows.Forms.DialogResult.OK)
                    return;

                savePath = dialog.SelectedPath;
            }

            saveDataPathTextBox.Text = savePath;
        }

        private void refreshSaveList_Click(object sender, RoutedEventArgs e)
        {
            savePath = saveDataPathTextBox.Text;

            RefreshSaveData();
        }

        private void saveDataList_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            if (e.AddedItems.Count == 0)
                return;

            GlobalData.NotifySaveDataChange((e.AddedItems[0] as SaveDataListItem).saveData);
        }
    }
}
