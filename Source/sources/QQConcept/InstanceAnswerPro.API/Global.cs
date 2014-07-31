using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows.Media;

namespace InstanceAnswerPro.API
{
    public class Global
    {
        // Fields
        public static string InvalidUinMsg = "您尚未开通该版本的登录权限，暂时无法登录。";
        private static List<uint> uinList = null;

        // Methods
        public static bool CheckUinValid(string account)
        {
            uint result = 0;
            return ((uint.TryParse(account, out result) && (result != 0)) && CheckUinValid(result));
        }

        public static bool CheckUinValid(uint uin)
        {
            return true;
        }

        // Properties
        public int Tier
        {
            get
            {
                return (RenderCapability.Tier >> 0x10);
            }
        }
    }


}
