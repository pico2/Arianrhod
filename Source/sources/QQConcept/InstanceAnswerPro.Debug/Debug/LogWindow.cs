namespace InstanceAnswerPro.Debug
{
    using System;
    using System.ComponentModel;
    using System.Diagnostics;
    using System.Windows;
    using System.Windows.Controls;
    using System.Windows.Markup;

    public class LogWindow : Window, IComponentConnector
    {
        private bool _contentLoaded;
        internal Grid root;

        public LogWindow()
        {
            this.InitializeComponent();
        }

        public void Bind(LogInformation logInformation)
        {
            this.root.DataContext = logInformation;
        }

        [DebuggerNonUserCode]
        public void InitializeComponent()
        {
            if (!this._contentLoaded)
            {
                this._contentLoaded = true;
                Uri resourceLocator = new Uri("/Bama.Debug;component/logwindow.xaml", UriKind.Relative);
                Application.LoadComponent(this, resourceLocator);
            }
        }

        private void OnChangeSkin(object sender, RoutedEventArgs args)
        {
            new LogWindow().Show();
        }

        [DebuggerNonUserCode, EditorBrowsable(EditorBrowsableState.Never)]
        void IComponentConnector.Connect(int connectionId, object target)
        {
            if (connectionId == 1)
            {
                this.root = (Grid) target;
            }
            else
            {
                this._contentLoaded = true;
            }
        }
    }
}

