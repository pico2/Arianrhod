using System;
using System.IO;
using System.Windows;
using System.Windows.Documents;
using System.Windows.Markup;
using InstanceAnswerPro.Controls;

namespace InstanceAnswerPro.IM.Controls
{
    public static class ClipboardMgr
    {
        // Fields
        public static readonly string BamaDataFormat = "MyDataFormat";

        // Methods
        internal static UIElement CreateUserControl(ClipboardControl cc)
        {
            if (cc.ControlType == "Bama.Controls.ImageEx")
            {
                return ReplaceControls.CreateImageExWithId(cc.ImagePath, cc.SysId);
            }
            return null;
        }

        public static void GenerateClipBoardData(DataObjectCopyingEventArgs e, TextSelection selection)
        {
            string str;
            using (MemoryStream stream = new MemoryStream())
            {
                TextRange range = new TextRange(selection.Start, selection.End);
                range.ClearAllProperties();
                range.Save(stream, DataFormats.Xaml, true);
                stream.Flush();
                stream.Position = 0L;
                using (StreamReader reader = new StreamReader(stream))
                {
                    str = reader.ReadToEnd();
                }
            }
            if (!string.IsNullOrEmpty(str))
            {
                string str2 = ReplaceControls.ReplaceGUIWithClipboardControl(str, selection.Start, selection.End);
                if (!string.IsNullOrEmpty(str2) && (str2 != str))
                {
                    e.DataObject.SetData(BamaDataFormat, str2);
                }
            }
        }

        internal static bool PasteContentData(InputBox inputBox, IDataObject iDataObject)
        {
            TextData data = TryGetText(iDataObject);
            if (!data.ContainsData)
            {
                if (iDataObject.GetDataPresent(DataFormats.Bitmap, true))
                {
                    inputBox.Paste(iDataObject);
                    return true;
                }
                return false;
            }
            inputBox.TempFlowDocument.Blocks.Clear();
            TextRange range = null;
            if (data.Format == BamaDataFormat)
            {
                object obj2 = XamlReader.Parse(data.Data);
                if (obj2 is Block)
                {
                    inputBox.TempFlowDocument.Blocks.Add(obj2 as Block);
                }
                else if (obj2 is Inline)
                {
                    Span span = new Span(inputBox.TempFlowDocument.ContentStart, inputBox.TempFlowDocument.ContentEnd)
                    {
                        Inlines = { obj2 as Span }
                    };
                }
                range = new TextRange(inputBox.TempFlowDocument.ContentStart, inputBox.TempFlowDocument.ContentEnd);
                range.ClearAllProperties();
                inputBox.Selection.Text = "";
                Span newspan = new Span(inputBox.Selection.Start, inputBox.Selection.End);
                ReplaceControls.AddBlocksToSpan(inputBox.TempFlowDocument, newspan);
                inputBox.CaretPosition = newspan.ElementEnd.GetInsertionPosition(LogicalDirection.Forward);
            }
            else
            {
                range = new TextRange(inputBox.TempFlowDocument.ContentStart, inputBox.TempFlowDocument.ContentEnd);
                using (MemoryStream stream = new MemoryStream())
                {
                    using (StreamWriter writer = new StreamWriter(stream))
                    {
                        writer.Write(data.Data);
                        writer.Flush();
                        stream.Position = 0L;
                        range.Load(stream, data.Format);
                    }
                }
                range.ClearAllProperties();
                inputBox.Selection.Text = "";
                Span span3 = new Span(inputBox.Selection.Start, inputBox.Selection.End);
                ReplaceControls.AddBlocksToSpan(inputBox.TempFlowDocument, span3);
                inputBox.CaretPosition = span3.ElementEnd.GetInsertionPosition(LogicalDirection.Forward);
            }
            inputBox.TempFlowDocument.Blocks.Clear();
            return true;
        }

        public static TextData TryGetText(IDataObject iDataObject)
        {
            try
            {
                if (iDataObject.GetDataPresent(BamaDataFormat, true))
                {
                    return new TextData(iDataObject.GetData(BamaDataFormat) as string, BamaDataFormat, true);
                }
                if (iDataObject.GetDataPresent(DataFormats.Rtf, true))
                {
                    return new TextData(iDataObject.GetData(DataFormats.Rtf) as string, DataFormats.Rtf, true);
                }
                if (iDataObject.GetDataPresent(DataFormats.Xaml, true))
                {
                    return new TextData(iDataObject.GetData(DataFormats.Xaml) as string, DataFormats.Xaml, true);
                }
            }
            catch (Exception)
            {
            }
            return new TextData(null, null, false);
        }

        // Nested Types
        public class TextData
        {
            // Methods
            public TextData(string data, string format, bool containsData)
            {
                this.Data = data;
                this.Format = format;
                this.ContainsData = containsData;
            }

            // Properties
            public bool ContainsData { get; private set; }

            public string Data { get; private set; }

            public string Format { get; private set; }
        }
    }


}
