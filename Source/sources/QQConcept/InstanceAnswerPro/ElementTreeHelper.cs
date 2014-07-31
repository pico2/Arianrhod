using System.IO;
using System.Windows;
using System.Windows.Markup;
using System.Windows.Media;
using System.Xml;

namespace InstanceAnswerPro
{
    public class ElementTreeHelper
    {
        // Methods
        public static object CloneElement(object elementToClone)
        {
            if (elementToClone == null)
            {
                return null;
            }
            return XamlReader.Load(new XmlTextReader(new StringReader(XamlWriter.Save(elementToClone))));
        }

        public static T FindVisualChild<T>(Visual visual) where T : Visual
        {
            if (visual == null)
            {
                return default(T);
            }
            T local = default(T);
            int childrenCount = VisualTreeHelper.GetChildrenCount(visual);
            for (int i = 0; i < childrenCount; i++)
            {
                Visual child = VisualTreeHelper.GetChild(visual, i) as Visual;
                T local1 = child as T;
                if (local1 != null)
                {
                    local = local1;
                }
                else
                {
                    local = FindVisualChild<T>(child);
                }
                if (local != null)
                {
                    return local;
                }
            }
            return local;
        }

        public static T FindVisualParent<T>(DependencyObject outerDependencyObject) where T : DependencyObject
        {
            if (outerDependencyObject == null)
            {
                return default(T);
            }
            DependencyObject parent = VisualTreeHelper.GetParent(outerDependencyObject);
            T local1 = parent as T;
            if (local1 != null)
            {
                return local1;
            }
            return FindVisualParent<T>(parent);
        }
    }


}
