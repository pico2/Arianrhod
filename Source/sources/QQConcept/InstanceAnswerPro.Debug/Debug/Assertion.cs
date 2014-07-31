namespace InstanceAnswerPro.Debug
{
    using System;

    public class Assertion
    {
        private Log logField;

        public Assertion(Log log)
        {
            this.logField = log;
        }

        public void Check(bool condition)
        {
            this.Check(condition, "", "");
        }

        public void Check(bool condition, string message)
        {
            this.Check(condition, message, "");
        }

        public void Check(bool condition, string message, string detailMessage)
        {
            if ((this.logField != null) && !condition)
            {
                this.logField.WriteLine(message + "(" + detailMessage + ")", LogCategories.Assertion);
            }
        }
    }
}

