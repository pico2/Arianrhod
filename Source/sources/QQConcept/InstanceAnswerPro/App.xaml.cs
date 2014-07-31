
namespace InstanceAnswerPro
{
    using System;
    using System.Collections.Generic;
    using System.Windows;
    using System.Windows.Interop;
    using System.Windows.Threading;
    using InstanceAnswerPro.Core;
    using KernelWrapper;
    using System.IO;
    using System.Xml;
    using System.Reflection;
    using InstanceAnswerPro.API;
    using InstanceAnswerPro.IM.ModuleInterface;
    /// <summary>
    /// Interaction logic for App.xaml
    /// </summary>
    public partial class App : Application
    {
        private static List<IModule> moduleList;

        public static readonly CoreMessenger Messenger = null;
        static App()
        {
            Messenger = null;
            moduleList = new List<IModule>();
            Messenger = CoreMessenger.Instance;
        }
        public App()
        {
            base.DispatcherUnhandledException += new DispatcherUnhandledExceptionEventHandler(this.App_DispatcherUnhandledException);
        }

        private void App_DispatcherUnhandledException(object sender, DispatcherUnhandledExceptionEventArgs e)
        {
            this.My_DispatcherUnhandledException(sender, e);
        }
        private void My_DispatcherUnhandledException(object sender, DispatcherUnhandledExceptionEventArgs e)
        {
            if (e != null)
            {
                e.Handled = this.ShowException(e.Exception);
            }
        }
        private bool ShowException(Exception exception)
        {
            if (exception == null)
            {
                return true;
            }
            string text1 = "Type:\r\n" + exception.GetType().FullName + "\r\n\r\nMessage:\r\n" + exception.Message + "\r\n\r\n继续运行吗?";
            string log = ((("Exception Type : " + exception.GetType().FullName + "\r\n") + "Message : \r\n") + exception.Message + "\r\nCallStack : \r\n") + exception.StackTrace + "\r\n";
            for (Exception exception2 = exception.InnerException; exception2 != null; exception2 = exception2.InnerException)
            {
                log = ((("Exception Type : " + exception2.GetType().FullName + "\r\n") + "Message : \r\n") + exception2.Message + "\r\nCallStack : \r\n") + exception2.StackTrace + "\r\n";
                log += log;
            }
            MessageBox.Show(log);
            return ((exception is InvalidOperationException) || true);
        }
        private void ComponentDispatcher_ThreadIdle(object sender, EventArgs e)
        {
            CoreMessenger.Instance.TM.OnIdle();
        }
        private void InitXaml()
        {
            if (WindowHelper.GetMainFrame() == null)
            {

                MainWindow win = new MainWindow();
                WindowHelper.SetMainFrame(win);

            }
        }

        protected override void OnStartup(StartupEventArgs e)
        {
            try
            {
                ComponentDispatcher.ThreadIdle += new EventHandler(this.ComponentDispatcher_ThreadIdle);

                Messenger.Initialize();

                MemoryManager.Init();
                ITXData pData = Messenger.TM.CreateTXData();
                CoreMessenger.Instance.TM.EventProcessing(AsyncHandle_Type.AsyncHandle_StartUp, 0x0, pData);

                string appPath = CoreMessenger.Instance.GetAppPath(APP_PATH_TYPE.APP_PATH_ROOT);
                this.LoadModules(appPath + "modules.xml");
                this.InitXaml();

                LoginWindow window = new LoginWindow();

                window.ShowDialog();
                if (window.LoginResult)
                {
                    WindowHelper.GetMainFrame().Show();
                }
                else
                {
                    base.Shutdown();
                }
            }
            catch (Exception exception)
            {
                this.ShowException(exception);
                base.Shutdown();
            }
        }
        private void LoadModules(string moduleXmlPath)
        {

            if (File.Exists(moduleXmlPath))
            {
                XmlDocument document = new XmlDocument();
                document.Load(moduleXmlPath);
                foreach (XmlNode node in document.SelectNodes("//BamaQQModules/CommonModules/Module"))
                {
                    this.LoadModule(node.InnerText);
                }
            }
        }
        private void LoadModule(string moduleFileName)
        {
            foreach (Type type in Assembly.LoadFrom(moduleFileName).GetTypes())
            {
                if (type.GetInterface("IModule") != null)
                {
                    IModule item = Activator.CreateInstance(type) as IModule;
                    moduleList.Add(item);
                    try
                    {
                        item.Load(Messenger);
                    }
                    catch (Exception)
                    {
                        MessageBox.Show(string.Format("Load module [{0}] failed.", moduleFileName));
                    }
                    break;
                }
            }
        }

 





    }
}
