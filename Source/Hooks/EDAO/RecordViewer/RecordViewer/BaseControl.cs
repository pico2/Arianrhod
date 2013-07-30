using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RecordViewer
{
    public class RVTabItem : Fluent.RibbonTabItem
    {
    }

    public class PanelContext : System.Windows.Controls.Grid
    {
        Boolean ContextInitialized = false;

        public void Refresh()
        {
            ShowContext();
        }

        public void ShowContext()
        {
            if (ContextInitialized)
                return;

            ContextInitialized = true;
        }
    }

    public class LowerPanel : System.Windows.Controls.Grid
    {
        public void SwapPanelContext(PanelContext context)
        {
            Children.Clear();
            if (context == null)
                return;

            Children.Add(context);
            context.Refresh();
        }
    }
}
