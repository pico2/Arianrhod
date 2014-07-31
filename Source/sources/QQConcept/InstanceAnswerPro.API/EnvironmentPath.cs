using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace InstanceAnswerPro.API
{
    public static class EnvironmentPath
    {
        // Fields
        private static string _startup;

        // Properties
        public static string Startup
        {
            get
            {
                if (_startup == null)
                {
                    _startup = Application.StartupPath + @"\";
                }
                return _startup;
            }
        }
    }

 

}
