using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Windows.Documents;
using System.Windows;
using System.Windows.Media;
using InstanceAnswerPro.Core;
using InstanceAnswerPro.Controls;
using TextElement = System.Windows.Documents.TextElement;
using System.Windows.Controls;

namespace InstanceAnswerPro.IM.Controls
{
    public class ReplaceControls
    {
        // Fields
        private static readonly Regex blockEmptyUIContainerRegex = new Regex(@"\<BlockUIContainer[^\>]*\>[^\<]*</BlockUIContainer\>", RegexOptions.Compiled);
        private static readonly Regex inlineEmptyUIContainerRegex = new Regex(@"\<InlineUIContainer[^\>]*\>[^\<]*</InlineUIContainer\>", RegexOptions.Compiled);

        // Methods
        internal static void AddBlocksToSpan(FlowDocument tempFlowDocument, Span newspan)
        {
            List<Inline> ic = new List<Inline>();
            CollectInlineFromBlocks(tempFlowDocument.Blocks, ic);
            if ((ic.Count > 0) && (ic[ic.Count - 1] is LineBreak))
            {
                ic.RemoveAt(ic.Count - 1);
            }
            newspan.Inlines.AddRange(ic);
        }

        private static void CollectInlineFromBlocks(BlockCollection blocks, List<Inline> ic)
        {
            IEnumerator<Block> enumerator = blocks.GetEnumerator();
            enumerator.Reset();
            while (enumerator.MoveNext())
            {
                Block current = enumerator.Current;
                if (current is Paragraph)
                {
                    Paragraph paragraph = current as Paragraph;
                    IEnumerator<Inline> enumerator2 = paragraph.Inlines.GetEnumerator();
                    enumerator2.Reset();
                    while (enumerator2.MoveNext())
                    {
                        Inline item = enumerator2.Current;
                        if (item is InlineUIContainer)
                        {
                            InlineUIContainer container = item as InlineUIContainer;
                            UIElement childUIElement = ReplaceWithMyControls(container.Child);
                            ic.Add(new InlineUIContainer(childUIElement));
                        }
                        else
                        {
                            ic.Add(item);
                        }
                    }
                    ic.Add(new LineBreak());
                }
                else if (current is Section)
                {
                    Section section = current as Section;
                    CollectInlineFromBlocks(section.Blocks, ic);
                }
                else if (current is BlockUIContainer)
                {
                    BlockUIContainer container2 = current as BlockUIContainer;
                    UIElement element2 = ReplaceWithMyControls(container2.Child);
                    ic.Add(new InlineUIContainer(element2));
                    ic.Add(new LineBreak());
                }
            }
        }

        public static string CreateFileFromImageSource(ImageSource imageSource)
        {
            if (imageSource != null)
            {
                return Helper_Icon.CreateTempImageFile(imageSource);
            }
            return null;
        }

        public static ImageEx CreateImageEx(string file, EmoticonItem item)
        {
            ImageEx ex = new ImageEx();
            if (item == null)
            {
                ex.Tag = EmoticonItem.CreateImageItem(file, null);
            }
            else
            {
                ex.Tag = item;
            }
            ex.Source = file;
            ex.HorizontalAlignment = HorizontalAlignment.Left;
            ex.VerticalAlignment = VerticalAlignment.Top;
            ex.Stretch = Stretch.None;
            return ex;
        }

        internal static ImageEx CreateImageExWithId(string file, string id)
        {
            EmoticonItem item = EmoticonItem.CreateImageItem(file, id);
            return CreateImageEx(file, item);
        }

        public static List<DependencyObject> GetUserControls(TextPointer start, TextPointer end)
        {
            List<DependencyObject> list = new List<DependencyObject>();
            for (TextPointer pointer = start; pointer.CompareTo(end) < 0; pointer = pointer.GetNextContextPosition(LogicalDirection.Forward))
            {
                if (((pointer.Parent is BlockUIContainer) || (pointer.Parent is InlineUIContainer)) && !list.Contains(pointer.Parent))
                {
                    list.Add(pointer.Parent);
                }
            }
            return list;
        }

        private static void ParseBlocks(BlockCollection blocks, List<TextElement> list)
        {
            foreach (Block block in blocks)
            {
                if (block is Paragraph)
                {
                    ParseParagraph(block as Paragraph, list);
                }
                else if (block is BlockUIContainer)
                {
                    ParseBlockUIContainer(block as BlockUIContainer, list);
                }
            }
        }

        private static void ParseBlockUIContainer(BlockUIContainer blockUIContainer, List<TextElement> list)
        {
            list.Add(blockUIContainer);
        }

        private static void ParseInlines(InlineCollection inlines, List<TextElement> list)
        {
            foreach (Inline inline in inlines)
            {
                if (inline is Run)
                {
                    ParseRun(inline as Run, list);
                }
                else if (inline is Span)
                {
                    ParseSpan(inline as Span, list);
                }
                else if (inline is InlineUIContainer)
                {
                    ParseInlineUIContainer(inline as InlineUIContainer, list);
                }
            }
        }

        private static void ParseInlineUIContainer(InlineUIContainer inlineUIContainer, List<TextElement> list)
        {
            list.Add(inlineUIContainer);
        }

        private static void ParseParagraph(Paragraph paragraph, List<TextElement> list)
        {
            ParseInlines(paragraph.Inlines, list);
            list.Add(new LineBreak());
        }

        private static void ParseRun(Run run, List<TextElement> list)
        {
            list.Add(run);
        }

        private static void ParseSpan(Span span, List<TextElement> list)
        {
            ParseInlines(span.Inlines, list);
        }

        public static string ReplaceGUIWithClipboardControl(string xaml, TextPointer start, TextPointer end)
        {
            List<DependencyObject> userControls = GetUserControls(start, end);
            if (userControls.Count == 0)
            {
                return xaml;
            }
            string input = xaml;
            foreach (DependencyObject obj2 in userControls)
            {
                string str2 = null;
                UIElement child = null;
                if (obj2 is BlockUIContainer)
                {
                    str2 = "BlockUIContainer";
                    child = (obj2 as BlockUIContainer).Child;
                }
                else if (obj2 is InlineUIContainer)
                {
                    str2 = "InlineUIContainer";
                    child = (obj2 as InlineUIContainer).Child;
                }
                string replacement = null;
                if (child is ImageEx)
                {
                    ImageEx ex = child as ImageEx;
                    EmoticonItem tag = ex.Tag as EmoticonItem;
                    string id = "";
                    if ((tag != null) && tag.IsSysEmoticon)
                    {
                        id = tag.Id;
                    }
                    if (ImageHyperlink.GetEnableCopy(ex))
                    {
                        ex.Source.Replace("$", "$$");
                        string str5 = string.Format("<wpfgui:ClipboardControl ControlType=\"{0}\" ImagePath=\"{1}\" SysId=\"{2}\"/>", typeof(ImageEx).FullName, ex.Source, id);
                        string str6 = "Bama.Controls";
                        string str7 = "Bama.Controls";
                        string str8 = string.Format("xmlns:wpfgui=\"clr-namespace:{0};assembly={1}\"", str6, str7);
                        replacement = string.Format("<{0} {1}>{2}</{0}>", str2, str8, str5);
                    }
                    else
                    {
                        replacement = "";
                    }
                }
                if (replacement != null)
                {
                    if (obj2 is BlockUIContainer)
                    {
                        input = blockEmptyUIContainerRegex.Replace(input, replacement, 1);
                    }
                    else
                    {
                        input = inlineEmptyUIContainerRegex.Replace(input, replacement, 1);
                    }
                }
            }
            return input;
        }

        public static UIElement ReplaceWithMyControls(UIElement control)
        {
            if (control is Image)
            {
                Image image = control as Image;
                return CreateImageEx(CreateFileFromImageSource(image.Source), null);
            }
            ClipboardControl cc = control as ClipboardControl;
            if (cc != null)
            {
                return ClipboardMgr.CreateUserControl(cc);
            }
            return null;
        }
    }


}
