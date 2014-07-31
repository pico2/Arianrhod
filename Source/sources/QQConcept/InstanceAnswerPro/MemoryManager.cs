using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows.Threading;
using System.Diagnostics;

namespace InstanceAnswerPro
{
    public class MemoryManager
    {
        // Fields
        private static DispatcherTimer timer = new DispatcherTimer();

        // Methods
        static MemoryManager()
        {
            timer.Interval = TimeSpan.FromSeconds(50.0);
            timer.Tick += new EventHandler(MemoryManager.timer_Tick);
            timer.Stop();
        }

        public static void Init()
        {
            timer.Start();
        }

        public static void ResetWorkingSet()
        {
            Process currentProcess = Process.GetCurrentProcess();
            if (currentProcess.WorkingSet64 > 0x3200000L)
            {
                currentProcess.MinWorkingSet = currentProcess.MinWorkingSet;
                currentProcess.MaxWorkingSet = currentProcess.MaxWorkingSet;
            }
        }

        private static void timer_Tick(object sender, EventArgs args)
        {
            ResetWorkingSet();
        }
    }

 

}
