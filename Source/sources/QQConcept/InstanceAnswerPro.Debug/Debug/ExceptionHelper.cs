namespace InstanceAnswerPro.Debug
{
    using System;

    public class ExceptionHelper
    {
        public static string GetExceptionMessage(Exception e)
        {
            Exception innerException = e.InnerException;
            string message = e.Message;
            while (innerException != null)
            {
                message = innerException.Message + "\r\n" + message;
                innerException = innerException.InnerException;
            }
            return message;
        }

        public static string GetExceptionStackTrace(Exception e)
        {
            Exception innerException = e.InnerException;
            string stackTrace = e.StackTrace;
            while (innerException != null)
            {
                stackTrace = innerException.StackTrace + "\r\n" + stackTrace;
                innerException = innerException.InnerException;
            }
            return stackTrace;
        }
    }
}

