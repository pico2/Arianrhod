using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using Fluent;

namespace RecordViewer
{
    /// <summary>
    /// Interaction logic for RecordViewerMainWindow.xaml
    /// </summary>
    public partial class RecordViewerMainWindow : Fluent.MetroWindow
    {
        private Dictionary<RVTabItem, PanelContext> TabPanelMap;

        public RecordViewerMainWindow()
        {
            InitializeComponent();

            TabPanelMap = new Dictionary<RVTabItem, PanelContext>();

            TabPanelMap[tabTreasureBox] = new TreasureBoxHunter();

            this.MinWidth = 500;
            this.MinHeight = 400;

            ribbon.SelectedTabChanged += Ribbon_SelectedTabChanged;
        }

        void Ribbon_SelectedTabChanged(object sender, SelectionChangedEventArgs e)
        {
            var ribbon = sender as Ribbon;

            if (ribbon.SelectedTabItem == null)
                return;

            var tabitem = ribbon.SelectedTabItem as RVTabItem;
            bool containsKey = TabPanelMap.ContainsKey(tabitem);

            var context = containsKey ? TabPanelMap[tabitem] : null;

            lowerPanel.SwapPanelContext(context);
        }

        private void OnBtnOpenSaveData(object sender, RoutedEventArgs e)
        {
            MessageBox.Show("fuck", null, MessageBoxButton.OKCancel, MessageBoxImage.Asterisk);
        }

        private void OnBtnExit(object sender, RoutedEventArgs e)
        {
            Close();
        }
    }
}
