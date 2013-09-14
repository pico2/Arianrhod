using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Runtime.InteropServices;
using RGiesecke.DllExport;

namespace Test_CSharp
{
    public class Class1
    {
        [DllExport("add", CallingConvention = CallingConvention.StdCall)]
        public static int TestExport(int left, int right)
        {
            return left + right;
        } 
    }
}
