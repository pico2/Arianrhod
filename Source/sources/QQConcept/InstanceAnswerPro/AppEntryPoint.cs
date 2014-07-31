using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Diagnostics;
using System.Windows;
using System.IO;
using System.ComponentModel;
using Microsoft.Win32;
using System.Runtime.InteropServices;
using WinAPI = InstanceAnswerPro.API.WinAPI;
namespace InstanceAnswerPro
{
    class AppEntryPoint
    {
        [DebuggerNonUserCode, STAThread]
        public static int Main(string[] arr)
        {
            if (!CheckKernelWrapperEx())
            {
                MessageBox.Show("Register IACom failed.", "Error");
                return 0;
            }
            App app = new App();
            app.InitializeComponent();
            app.Run();
            return 0;
        }
        public static bool RegKernelWrapper()
        {
            return RegisterServer(EnvironmentPath.Startup + "KernelWrapper.dll");
        }
        public static bool RegisterServer(string regDll)
        {
            IntPtr dllModule = WinAPI.LoadLibraryW(regDll);
            Marshal.GetLastWin32Error();
            if (dllModule != IntPtr.Zero)
            {
                WinAPI.DllRegisterServer server = (WinAPI.DllRegisterServer)WinAPI.GetFunctionAddress(dllModule, "DllRegisterServer", typeof(WinAPI.DllRegisterServer));
                if (server != null)
                {
                    IntPtr ptr2 = server();
                    Marshal.GetLastWin32Error();
                    if (ptr2 == IntPtr.Zero)
                    {
                        return true;
                    }
                }
            }
            return false;
        }
        public static bool CheckKernelWrapperEx()
        {
            string regDll = EnvironmentPath.Startup + "KernelWrapper.dll";
            if (!CheckRegistry(regDll))
            {
                RegKernelWrapper();
                return CheckRegistry(regDll);
            }
            else
            {
                return true;
            }
        }
        public static bool CheckRegistry(string regDll)
        {
            try
            {
                RegistryKey classesRoot = Registry.ClassesRoot;
                RegistryKey key2 = classesRoot.OpenSubKey(@"CLSID\{BCDC2282-68B6-4A06-932D-494949D98840}\InprocServer32");
                string path = key2.GetValue("").ToString();
                key2.Close();
                classesRoot.Close();
                string directoryName = Path.GetDirectoryName(path);
                string strB = Path.GetDirectoryName(regDll);
                if (string.Compare(directoryName, strB, true) == 0)
                {
                    return true;
                }
            }
            catch (Exception)
            {
            }
            return false;
        }
        public static class EnvironmentPath
        {
            private static string _startup;

            public static string Startup
            {
                get
                {
                    if (_startup == null)
                    {
                        _startup = System.Windows.Forms.Application.StartupPath + @"\";
                    }
                    return _startup;
                }
            }
        }
    }
}
