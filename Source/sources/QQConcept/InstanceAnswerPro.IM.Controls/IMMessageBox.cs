using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows.Documents;
using InstanceAnswerPro.Core;
using System.Windows.Controls;
using TextElement = InstanceAnswerPro.Core.TextElement;
using System.Windows;
using InstanceAnswerPro.API;

namespace InstanceAnswerPro.IM.Controls
{
    public class IMMessageBox
    {
        // Methods
        public static void AddLinkText(InlineCollection inlines, string text, HyperLinkObj obj)
        {
            Hyperlink item = new Hyperlink(new Run(text))
            {
                Tag = obj
            };
            inlines.Add(item);
        }

        public static void AddNormalText(InlineCollection inlines, string text)
        {
            inlines.Add(new Run(text));
        }

        public static void AnalyzeUrl(TextBlock textBlock, string messageBoxText)
        {
            if (string.IsNullOrEmpty(messageBoxText))
            {
                textBlock.Text = messageBoxText;
            }
            else
            {
                Paragraph paragraph = new Paragraph();
                AddNormalText(paragraph.Inlines, messageBoxText);
                MessagePack msgPack = new MessagePack();
                InputBox.ParseInlines(msgPack, paragraph.Inlines);
                MessagePack pack2 = new MessagePack(CoreMessenger.Instance.MsgStorage.TransformMsg(msgPack.Key));
                uint elemCount = pack2.GetElemCount();
                for (uint i = 0; i < elemCount; i++)
                {
                    MessageElement elem = pack2.GetElem(i);
                    if (elem.Category == MsgPackCat.ELEMTYPE_TEXT)
                    {
                        Guid guid;
                        Guid guid2;
                        TextElement element2 = (TextElement)elem;
                        string text = element2.GetText();
                        string url = element2.GetUrl(out guid, out guid2);
                        if (string.IsNullOrEmpty(url))
                        {
                            AddNormalText(textBlock.Inlines, text);
                        }
                        else
                        {
                            AddLinkText(textBlock.Inlines, text, new HyperLinkObj_Url(url));
                        }
                    }
                }
            }
        }

        public static MessageBoxResult CustomHeadMsgBox(Window owner)
        {
            Paragraph paragraph = new Paragraph();
            AddNormalText(paragraph.Inlines, "您没有上传自定义头像的权限，");
            AddLinkText(paragraph.Inlines, "查看详情", new HyperLinkObj_Url("http://im.qq.com/client/description/avatar.shtml"));
            AddNormalText(paragraph.Inlines, "。");
            return IAMessageBox.Show(owner, paragraph.Inlines, "提示");
        }

        public static void InvalidUinMsg(Window owner, string uin)
        {
            Paragraph paragraph = new Paragraph();
            AddNormalText(paragraph.Inlines, Global.InvalidUinMsg);
            AddLinkText(paragraph.Inlines, "[详情请点击]", new HyperLinkObj_Url(string.Format("http://exp.qq.com/cgi-bin/present/tec_cgi_index?source_flag=0&uin={0}", uin)));
            IAMessageBox.Show(owner, paragraph.Inlines, "QQ");
        }

        public static MessageBoxResult ServerKickoutMsgBox(Window owner)
        {
            Paragraph paragraph = new Paragraph();
            AddNormalText(paragraph.Inlines, "您的QQ帐号在另一个地方登录了，您已被迫下线。\r\n\r\n请注意: 如果这不是您本人的操作，那么您的密码很可能已经泄露，建议您立刻");
            AddLinkText(paragraph.Inlines, "修改密码", new HyperLinkObj_Url(CoreMessenger.Instance.MiscHelper.TXLoadString("ConfigCenter_ChangePwd_URL")));
            AddNormalText(paragraph.Inlines, "。\n\n\n 是否重新登录？");
            return IAMessageBox.Show(owner, paragraph.Inlines, "系统消息", MessageBoxButton.YesNo, MessageBoxImage.Exclamation);
        }
    }


}
