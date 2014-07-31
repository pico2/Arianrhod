using System;
using System.Windows;
using System.Windows.Controls;

namespace InstanceAnswerPro
{
    public class ContactPanel : Panel
    {
        // Methods
        protected override Size ArrangeOverride(Size finalSize)
        {
            if (base.Children.Count < 2)
            {
                return base.ArrangeOverride(finalSize);
            }
            bool flag = false;
            double num = 0.0;
            if (((base.Children[0].DesiredSize.Height + base.Children[1].DesiredSize.Height) > finalSize.Height) || ((base.Children[0].DesiredSize.Width + base.Children[1].DesiredSize.Width) < finalSize.Width))
            {
                flag = true;
                num = Math.Max(base.Children[0].DesiredSize.Height, base.Children[1].DesiredSize.Height);
            }
            else
            {
                flag = false;
                num = base.Children[0].DesiredSize.Height + base.Children[1].DesiredSize.Height;
            }
            int num2 = 2;
            for (int i = 2; i < base.Children.Count; i++)
            {
                if ((num + base.Children[i].DesiredSize.Height) > finalSize.Height)
                {
                    break;
                }
                num2 = i + 1;
                num += base.Children[i].DesiredSize.Height;
            }
            Rect finalRect = new Rect(0.0, (finalSize.Height - num) / 2.0, finalSize.Width, 0.0);
            if (flag)
            {
                double num4 = Math.Max(base.Children[0].DesiredSize.Height, base.Children[1].DesiredSize.Height);
                finalRect.Width = Math.Min(base.Children[0].DesiredSize.Width, finalSize.Width);
                finalRect.Height = num4;
                base.Children[0].Arrange(finalRect);
                finalRect.X = base.Children[0].DesiredSize.Width;
                finalRect.Width = Math.Max((double)0.0, (double)(finalSize.Width - base.Children[0].DesiredSize.Width));
                base.Children[1].Arrange(finalRect);
                finalRect.X = 0.0;
                finalRect.Y += num4;
                finalRect.Width = finalSize.Width;
            }
            for (int j = flag ? 2 : 0; j < num2; j++)
            {
                finalRect.Height = base.Children[j].DesiredSize.Height;
                base.Children[j].Arrange(finalRect);
                finalRect.Offset(0.0, finalRect.Height);
            }
            finalRect.Height = 0.0;
            for (int k = num2; k < base.Children.Count; k++)
            {
                base.Children[k].Arrange(finalRect);
            }
            return finalSize;
        }

        protected override Size MeasureOverride(Size availableSize)
        {
            if (base.Children.Count < 2)
            {
                return base.MeasureOverride(availableSize);
            }
            double num = 0.0;
            double num2 = 0.0;
            for (int i = 0; i < base.Children.Count; i++)
            {
                base.Children[i].Measure(availableSize);
                num += base.Children[i].DesiredSize.Height;
                num2 = Math.Max(num2, base.Children[i].DesiredSize.Width);
            }
            if ((base.Children[0].DesiredSize.Height + base.Children[1].DesiredSize.Height) > availableSize.Height)
            {
                Size size2 = new Size(availableSize.Width - base.Children[0].DesiredSize.Width, availableSize.Height);
                base.Children[1].Measure(size2);
                return new Size(Math.Min(base.Children[0].DesiredSize.Width + base.Children[1].DesiredSize.Width, availableSize.Width), Math.Min(Math.Max(base.Children[0].DesiredSize.Height, base.Children[1].DesiredSize.Height), availableSize.Height));
            }
            return new Size(Math.Min(num2, availableSize.Width), Math.Min(num, availableSize.Height));
        }
    }


}
