using System;
using System.Collections.Generic;
using System.Text;
using System.Data;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Shapes;
using Itenso.Windows.Controls.ListViewLayout;
using System.ComponentModel;
using System.Windows.Markup;
using Newtonsoft.Json;

namespace RecordViewer
{
    /// <summary>
    /// Interaction logic for TreasureBoxHunter.xaml
    /// </summary>
    public partial class TreasureBoxHunter : PanelContext
    {
        Dictionary<String, ItemInformation> ItemIdMap;
        Dictionary<String, String> HeaderPropertyMap;
        RecordViewerData viewerData = null;

        GridViewColumnHeader    lastHeaderClicked = null;
        ListSortDirection       lastDirection = ListSortDirection.Ascending;

        class ListViewColumnItem
        {
            public String              Header       { get; set; }
            public String              Binding      { get; set; }
            public long                WidthPercent { get; set; }
            public HorizontalAlignment Alignment    { get; set; }

            public ListViewColumnItem(String Header, String Binding, long WidthPercent, HorizontalAlignment Alignment)
            {
                this.Header         = Header;
                this.Binding        = Binding;
                this.WidthPercent   = WidthPercent;
                this.Alignment      = Alignment;
            }
        }

        public class ItemInformation
        {
            public String   ID                    { get; set; }
            public String   Map                   { get; set; }
            public int      Offset                { get; set; }
            public int      Bit                   { get; set; }
            public String   Item                  { get; set; }
            public int      Line                  { get; set; }
            public String   File                  { get; set; }
            public int      TriggerX              { get; set; }
            public int      TriggerZ              { get; set; }
            public int      TriggerY              { get; set; }
            public int      TriggerRange          { get; set; }
            public int      ActorX                { get; set; }
            public int      ActorZ                { get; set; }
            public int      ActorY                { get; set; }
            public int      TalkScenaIndex        { get; set; }
            public int      TalkFunctionIndex     { get; set; }
            public String   Description           { get; set; }
            public String   Screenshot            { get; set; }
            public Boolean  Opened                { get; set; }

            public String   Status
            {
                get
                {
                    return Opened ? "已开启" : "未开启";
                }
            }

            public
            ItemInformation(
                String   ID                 = "",
                String   Map                = "",
                int      Offset             = 0,
                int      Bit                = 0,
                String   Item               = "",
                int      Line               = 0,
                String   File               = "",
                int      TriggerX           = 0,
                int      TriggerZ           = 0,
                int      TriggerY           = 0,
                int      TriggerRange       = 0,
                int      ActorX             = 0,
                int      ActorZ             = 0,
                int      ActorY             = 0,
                int      TalkScenaIndex     = 0,
                int      TalkFunctionIndex  = 0,
                String   Description        = "",
                String   Screenshot         = "",
                Boolean  Opened             = false
            )
            {
                this.ID                 = ID;
                this.Map                = Map;
                this.Offset             = Offset;
                this.Bit                = Bit;
                this.Item               = Item;
                this.Line               = Line;
                this.File               = File;
                this.TriggerX           = TriggerX;
                this.TriggerZ           = TriggerZ;
                this.TriggerY           = TriggerY;
                this.TriggerRange       = TriggerRange;
                this.ActorX             = ActorX;
                this.ActorZ             = ActorZ;
                this.ActorY             = ActorY;
                this.TalkScenaIndex     = TalkScenaIndex;
                this.TalkFunctionIndex  = TalkFunctionIndex;
                this.Description        = Description;
                this.Screenshot         = Screenshot;
                this.Opened             = Opened;
            }
        }

        DataTemplate CreateColumnTemplate(String bind, HorizontalAlignment align)
        {
            const String xamlTemplate =
                "<DataTemplate>\r\n" +
                "   <TextBlock Text=\"{{Binding {0}}}\" TextAlignment=\"{1}\" />\r\n" +
                "</DataTemplate>";

            var xaml = String.Format(xamlTemplate, bind, align.ToString());

            var context = new ParserContext();

            context.XamlTypeMapper = new XamlTypeMapper(new string[0]);

            context.XmlnsDictionary.Add("", "http://schemas.microsoft.com/winfx/2006/xaml/presentation");
            context.XmlnsDictionary.Add("x", "http://schemas.microsoft.com/winfx/2006/xaml");

            return XamlReader.Parse(xaml, context) as DataTemplate;
        }

        public TreasureBoxHunter(RecordViewerData viewerData)
        {
            InitializeComponent();

            this.viewerData = viewerData;

            ItemIdMap = new Dictionary<String, ItemInformation>();
            HeaderPropertyMap = new Dictionary<String, String>();

            ListViewColumnItem[] Columns = new ListViewColumnItem[]
            {
                new ListViewColumnItem("ID",      "ID",              1,     HorizontalAlignment.Center),
                new ListViewColumnItem("地图",    "Map",             20,    HorizontalAlignment.Center),
                new ListViewColumnItem("物品",    "Item",            20,    HorizontalAlignment.Left),
                new ListViewColumnItem("状态",    "Status",          1,     HorizontalAlignment.Center),
                new ListViewColumnItem("X",       "ActorX",          1,     HorizontalAlignment.Center),
                new ListViewColumnItem("Y",       "ActorY",          1,     HorizontalAlignment.Center),
                new ListViewColumnItem("Z",       "ActorZ",          1,     HorizontalAlignment.Center),
                new ListViewColumnItem("描述",    "Description",     55,    HorizontalAlignment.Center),
            };

            Func<Double, long> GetWidth = (Double percent) =>
                                            {
                                                return (long)Math.Ceiling(percent * Columns.Length / 100);
                                            };

            var lvlmgr = new ListViewLayoutManager(treasureBoxList);

            lvlmgr.VerticalScrollBarVisibility = ScrollBarVisibility.Auto;
            lvlmgr.HorizontalScrollBarVisibility = ScrollBarVisibility.Auto;
            lvlmgr.AttachScrollViewerScrollChanged = true;

            Style headerStyle = new Style();
            headerStyle.Setters.Add(new Setter(Control.BackgroundProperty, Brushes.White));

            treasureBoxGridView.SetValue(GridView.ColumnHeaderContainerStyleProperty, headerStyle);

            foreach (var col in Columns)
            {
                HeaderPropertyMap[col.Header] = col.Binding;

                GridViewColumn column = new GridViewColumn();

                column.Header = col.Header;
                column.CellTemplate = CreateColumnTemplate(col.Binding, col.Alignment);
                column.SetValue(GridViewColumn.HeaderContainerStyleProperty, headerStyle);

                treasureBoxGridView.Columns.Add(ProportionalColumn.ApplyWidth(column, GetWidth(col.WidthPercent)));
            }

            String boxinfo = @"E:\Desktop\Source\Hooks\EDAO\Decompiler\GameData\box.json";

            try
            {
                InitializeTreasureBoxInfo(boxinfo);
            }
            catch (Exception e)
            {
                MessageBox.Show(e.ToString());
                return;
            }
        }

        override public void Refresh()
        {
            EDAOSaveData saveData = viewerData.GetSaveData();

            treasureBoxList.Items.Clear();

            foreach (var pair in ItemIdMap)
            {
                if (saveData == null)
                {
                    pair.Value.Opened = false;
                }
                else
                {
                    pair.Value.Opened = saveData.TestScenaFlag(pair.Value.Offset, pair.Value.Bit);
                }

                InsertItemInfo(pair.Value);
            }

            if (lastHeaderClicked != null)
            {
                Sort(lastHeaderClicked, lastDirection);
            }
        }

        public void InitializeTreasureBoxInfo(String boxinfo)
        {
            String json;
            using (System.IO.StreamReader reader = new System.IO.StreamReader(boxinfo))
            {
                json = reader.ReadToEnd();
            }

            dynamic items = JsonConvert.DeserializeObject(json);

            foreach (var y in items)
            {
                var item = new ItemInformation();

                item.ID                     = y.ID;
                item.Map                    = y.Map;
                item.Offset                 = Convert.ToInt32((String)y.Offset, 16);
                item.Bit                    = y.Bit;
                item.Item                   = y.Item;
                item.Line                   = y.Line;
                item.File                   = y.File;
                item.TriggerX               = y.TriggerX;
                item.TriggerZ               = y.TriggerZ;
                item.TriggerY               = y.TriggerY;
                item.TriggerRange           = y.TriggerRange;
                item.ActorX                 = y.ActorX;
                item.ActorZ                 = y.ActorZ;
                item.ActorY                 = y.ActorY;
                item.TalkScenaIndex         = y.TalkScenaIndex;
                item.TalkFunctionIndex      = y.TalkFunctionIndex;
                item.Description            = y.Description;
                item.Screenshot             = y.Screenshot;

                ItemIdMap[item.ID] = item;
            }
        }

        public void InsertItemInfo(ItemInformation item)
        {
            treasureBoxList.Items.Add(item);
        }

        void GridViewColumnHeaderClickedHandler(object sender, RoutedEventArgs e)
        {
            GridViewColumnHeader headerClicked = e.OriginalSource as GridViewColumnHeader;
            ListSortDirection direction;

            if (headerClicked == null)
                return;

            if (headerClicked != lastHeaderClicked)
            {
                direction = ListSortDirection.Ascending;
            }
            else
            {
                direction = lastDirection == ListSortDirection.Ascending ? ListSortDirection.Descending : ListSortDirection.Ascending;
            }

            try
            {
                Sort(headerClicked, direction);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString());
            }

            if (direction == ListSortDirection.Ascending)
            {
                headerClicked.Column.HeaderTemplate = Resources["HeaderTemplateArrowUp"] as DataTemplate;
            }
            else
            {
                headerClicked.Column.HeaderTemplate = Resources["HeaderTemplateArrowDown"] as DataTemplate;
            }

            if (lastHeaderClicked != null && lastHeaderClicked != headerClicked)
            {
                lastHeaderClicked.Column.HeaderTemplate = null;
            }

            lastHeaderClicked = headerClicked;
            lastDirection = direction;
        }

        private void Sort(GridViewColumnHeader headerClicked, ListSortDirection direction)
        {
            var lv = treasureBoxList;
            lv.Items.SortDescriptions.Clear();
            SortDescription sd = new SortDescription(HeaderPropertyMap[headerClicked.Column.Header as String], direction);
            lv.Items.SortDescriptions.Add(sd);
            lv.Items.Refresh();
        }
    }
}
