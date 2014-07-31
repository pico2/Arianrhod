namespace Bama
{
    using System;
    using System.ComponentModel;
    using System.Diagnostics;
    using System.Windows;
    using System.Windows.Controls;
    using System.Windows.Markup;

    public class UserControl1 : System.Windows.Controls.UserControl, IComponentConnector
    {
        private bool _contentLoaded;
        internal Grid LayoutRoot;
        internal UserControl1 UserControl;

        public UserControl1()
        {
            this.InitializeComponent();
        }

        [DebuggerNonUserCode]
        public void InitializeComponent()
        {
            if (!this._contentLoaded)
            {
                this._contentLoaded = true;
                Uri resourceLocator = new Uri("/Bama.Debug;component/usercontrol1.xaml", UriKind.Relative);
                Application.LoadComponent(this, resourceLocator);
            }
        }

        [EditorBrowsable(EditorBrowsableState.Never), DebuggerNonUserCode]
        void IComponentConnector.Connect(int connectionId, object target)
        {
            switch (connectionId)
            {
                case 1:
                    this.UserControl = (UserControl1) target;
                    return;

                case 2:
                    this.LayoutRoot = (Grid) target;
                    return;
            }
            this._contentLoaded = true;
        }
    }
}

