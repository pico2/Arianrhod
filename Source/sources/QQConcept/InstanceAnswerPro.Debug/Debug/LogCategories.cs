namespace InstanceAnswerPro.Debug
{
    using System;

    public class LogCategories
    {
        public static readonly LogCategories Assertion = new LogCategories("A");
        private string categoryField;
        public static readonly LogCategories Error = new LogCategories("E");
        public static readonly LogCategories Information = new LogCategories("I");
        public static readonly LogCategories Warning = new LogCategories("W");

        private LogCategories(string category)
        {
            this.categoryField = category;
        }

        public override string ToString()
        {
            return this.categoryField;
        }
    }
}

