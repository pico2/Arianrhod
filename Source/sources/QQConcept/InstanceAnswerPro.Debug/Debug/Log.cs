namespace InstanceAnswerPro.Debug
{
    using System;

    public class Log
    {
        private InstanceAnswerPro.Debug.Assertion assertion;
        public static Log Instance;
        private LogInformation logInformation;
        private LogModes logModeField;
        private LogWindow logWindow;

        private Log()
        {
            this.logInformation = new LogInformation();
        }

        public Log(LogModes logMode)
        {
            this.logInformation = new LogInformation();
            this.assertion = new InstanceAnswerPro.Debug.Assertion(this);
            this.logModeField = logMode;
            Instance = this;
        }

        private void logWindow_Closed(object sender, EventArgs e)
        {
            this.logWindow.Closed -= new EventHandler(this.logWindow_Closed);
            this.logWindow = null;
        }

        public void ShowLogWindow()
        {
            if (this.logWindow == null)
            {
                this.logWindow = new LogWindow();
                this.logWindow.Closed += new EventHandler(this.logWindow_Closed);
                this.logWindow.Bind(this.logInformation);
            }
            this.logWindow.Show();
        }

        private void Write(string message, LogCategories category)
        {
        }

        public void WriteLine(string message)
        {
        }

        public void WriteLine(string message, LogCategories category)
        {
        }

        public InstanceAnswerPro.Debug.Assertion Assertion
        {
            get
            {
                return this.assertion;
            }
        }

        public LogModes LogMode
        {
            get
            {
                return this.logModeField;
            }
            set
            {
                this.logModeField = value;
            }
        }
    }
}

