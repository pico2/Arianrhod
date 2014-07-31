using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows;
using System.Windows.Media;
using System.Windows.Media.Imaging;

namespace InstanceAnswerPro.API
{
    public class VisualTree
    {
        // Methods
        public static DependencyObject GetAncestorByType(DependencyObject dependencyObject, Type type)
        {
            if (dependencyObject != null)
            {
                if (dependencyObject.GetType() == type)
                {
                    return dependencyObject;
                }
                if (dependencyObject is Visual)
                {
                    return GetAncestorByType(VisualTreeHelper.GetParent(dependencyObject), type);
                }
            }
            return null;
        }

        public static void GetChildrenByType(DependencyObject dependencyObject, Type type, List<DependencyObject> objectList)
        {
            if (dependencyObject != null)
            {
                int childrenCount = VisualTreeHelper.GetChildrenCount(dependencyObject);
                for (int i = 0; i < childrenCount; i++)
                {
                    DependencyObject child = VisualTreeHelper.GetChild(dependencyObject, i);
                    if (child.GetType() == type)
                    {
                        objectList.Add(child);
                    }
                    GetChildrenByType(child, type, objectList);
                }
            }
        }

        public static Point GetTopLeft(FrameworkElement frameworkElement, FrameworkElement target)
        {
            if (frameworkElement == null)
            {
                return new Point(0.0, 0.0);
            }
            FrameworkElement parent = VisualTreeHelper.GetParent(frameworkElement) as FrameworkElement;
            if (parent == null)
            {
                throw new Exception("target 不是 frameworkElement 的上级");
            }
            Vector offset = VisualTreeHelper.GetOffset(frameworkElement);
            Point point = new Point(offset.X, offset.Y);
            if (parent != target)
            {
                Point topLeft = GetTopLeft(parent, target);
                point.X += topLeft.X;
                point.Y += topLeft.Y;
            }
            return point;
        }

        public static Rect GetVisualRect(Window win, FrameworkElement frameworkElement)
        {
            return new Rect(GetVisualTopLeftRelativeParent(frameworkElement, win), new Size(frameworkElement.ActualWidth, frameworkElement.ActualHeight));
        }

        public static Point GetVisualTopLeft(FrameworkElement reference, Window parent)
        {
            Point visualTopLeftRelativeParent = GetVisualTopLeftRelativeParent(reference, parent);
            return new Point(parent.Left + visualTopLeftRelativeParent.X, parent.Top + visualTopLeftRelativeParent.Y);
        }

        public static Point GetVisualTopLeftRelativeParent(FrameworkElement reference, Window parent)
        {
            return reference.TransformToAncestor(parent).Transform(new Point(0.0, 0.0));
        }

        public static void Print(int depth, DependencyObject dependencyObject)
        {
            int childrenCount = VisualTreeHelper.GetChildrenCount(dependencyObject);
            for (int i = 0; i < childrenCount; i++)
            {
                Print(depth + 1, VisualTreeHelper.GetChild(dependencyObject, i));
            }
        }

        public static BitmapSource Snapshot(FrameworkElement element)
        {
            RenderTargetBitmap bitmap = new RenderTargetBitmap((int)((element.ActualWidth + element.Margin.Left) + element.Margin.Right), (int)((element.ActualHeight + element.Margin.Top) + element.Margin.Bottom), 0.0, 0.0, PixelFormats.Default);
            bitmap.Render(element);
            return bitmap;
        }
    }


}
