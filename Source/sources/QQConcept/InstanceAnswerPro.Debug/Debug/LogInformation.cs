namespace InstanceAnswerPro.Debug
{
    using System;
    using System.ComponentModel;
    using System.Runtime.CompilerServices;

    public class LogInformation : INotifyPropertyChanged
    {
        private string text = "";

        public event PropertyChangedEventHandler PropertyChanged;

        protected void OnPropertyChanged(string propertyName)
        {
            if (this.PropertyChanged != null)
            {
                this.PropertyChanged(this, new PropertyChangedEventArgs(propertyName));
            }
        }

        public string Text
        {
            get
            {
                return this.text;
            }
            set
            {
                if (this.text != value)
                {
                    this.text = value;
                    this.OnPropertyChanged("Text");
                }
            }
        }
    }
}

