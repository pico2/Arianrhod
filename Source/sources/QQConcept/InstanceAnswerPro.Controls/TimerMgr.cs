using System;
using System.Collections.Generic;
using System.Windows.Threading;

namespace InstanceAnswerPro.Controls
{
    public static class TimerMgr
    {
        // Fields
        private static DispatcherTimer _RenderTimer = null;
        private static List<TimerItem> curTasks = new List<TimerItem>();
        private static List<TimerItem> delTasks = new List<TimerItem>();

        // Methods
        static TimerMgr()
        {
            _RenderTimer = new DispatcherTimer(DispatcherPriority.Render);
            _RenderTimer.Interval = TimeSpan.FromMilliseconds(10.0);
            _RenderTimer.Tick += new EventHandler(TimerMgr._RenderTimer_Tick);
        }

        private static void _RenderTimer_Tick(object sender, EventArgs e)
        {
            if (RealRemoveItem())
            {
                foreach (TimerItem item in curTasks)
                {
                    InternalRun(item);
                }
                RealRemoveItem();
            }
        }

        public static void EraseTimerCallback(TimerItem item)
        {
            if (delTasks.IndexOf(item) == -1)
            {
                delTasks.Add(item);
            }
        }

        private static void InternalRun(TimerItem item)
        {
            item.Ticks += 10;
            if (item.Ticks >= item.Elapse)
            {
                if (item.Handler != null)
                {
                    item.Handler(item);
                }
                item.Ticks = 0;
            }
        }

        private static bool RealRemoveItem()
        {
            foreach (TimerItem item in delTasks)
            {
                curTasks.Remove(item);
            }
            delTasks.Clear();
            if (curTasks.Count == 0)
            {
                _RenderTimer.Stop();
                return false;
            }
            return true;
        }

        public static TimerItem SetInterval(uint elapse, TimerCallBacktHandler handler)
        {
            TimerItem item = new TimerItem
            {
                Elapse = elapse,
                Handler = handler
            };
            if (delTasks != null)
            {
                delTasks.Remove(item);
            }
            if (curTasks.IndexOf(item) == -1)
            {
                curTasks.Add(item);
            }
            if (!_RenderTimer.IsEnabled)
            {
                _RenderTimer.Start();
            }
            return item;
        }

        // Nested Types
        public delegate void TimerCallBacktHandler(TimerMgr.TimerItem item);

        public class TimerItem
        {
            // Properties
            public uint Elapse { get; set; }

            public TimerMgr.TimerCallBacktHandler Handler { get; set; }

            public uint Ticks { get; set; }
        }
    }

 

}
