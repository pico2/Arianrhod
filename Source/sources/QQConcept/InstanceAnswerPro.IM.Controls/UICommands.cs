using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows.Input;

namespace InstanceAnswerPro.IM.Controls
{
    public static class UICommands
    {
        // Fields
        public static RoutedUICommand About = new RoutedUICommand();
        public static RoutedUICommand AttentionContents = new RoutedUICommand();
        public static RoutedUICommand CommunitymemberMgr = new RoutedUICommand();
        public static RoutedUICommand CreateCommunity = new RoutedUICommand("创建一个群", "CreateCommunity", typeof(UICommands));
        public static RoutedUICommand DemoVideo = new RoutedUICommand();
        public static RoutedUICommand DisplayAllContacts = new RoutedUICommand();
        public static RoutedUICommand DisplayOnlineContactsOnly = new RoutedUICommand();
        public static RoutedUICommand ExitCommunity = new RoutedUICommand();
        public static RoutedUICommand GlobalMsgSet = new RoutedUICommand("群消息设置", "GlobalMsgSet", typeof(UICommands));
        public static RoutedUICommand ModifyRemarkName = new RoutedUICommand();
        public static RoutedUICommand MsgSet = new RoutedUICommand("群消息设置", "MsgSet", typeof(UICommands));
        public static RoutedUICommand OpenBuddyZone = new RoutedUICommand();
        public static RoutedUICommand OpenCommunityInfoWindow = new RoutedUICommand();
        public static RoutedUICommand OpenMsgMgr = new RoutedUICommand();
        public static RoutedUICommand OpenQzone = new RoutedUICommand();
        public static RoutedUICommand OpenSetting = new RoutedUICommand();
        public static RoutedUICommand OpenSystemSettingsWindow = new RoutedUICommand();
        public static RoutedUICommand RemoveContact = new RoutedUICommand();
        public static RoutedUICommand SearchCommunity = new RoutedUICommand("查找添加群", "SearchCommunity", typeof(UICommands));
        public static RoutedUICommand SendCommunityMessage = new RoutedUICommand();
        public static RoutedUICommand SendIM = new RoutedUICommand();
        public static RoutedUICommand SendMail = new RoutedUICommand();
        public static RoutedUICommand Suggestion = new RoutedUICommand();
        public static RoutedUICommand Unknown = new RoutedUICommand();
        public static RoutedUICommand UpdateProfile = new RoutedUICommand();
        public static RoutedUICommand ViewProfile = new RoutedUICommand();
        public static RoutedUICommand ViewQZone = new RoutedUICommand();
        public static RoutedUICommand VisitGroupSpace = new RoutedUICommand();
    }

 

}
