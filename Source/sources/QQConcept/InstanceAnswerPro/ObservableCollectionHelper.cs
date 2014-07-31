using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Collections.ObjectModel;

namespace InstanceAnswerPro
{
    public static class ObservableCollectionHelper
    {
        // Methods
        public static int FindFirst<T>(ObservableCollection<T> collection, Predicate<T> match)
        {
            int count = collection.Count;
            for (int i = 0; i < count; i++)
            {
                if (match(collection[i]))
                {
                    return i;
                }
            }
            return -1;
        }

        public static int RemoveAll<T>(ObservableCollection<T> collection, Predicate<T> match)
        {
            List<T> list = new List<T>();
            foreach (T local in collection)
            {
                if (match(local))
                {
                    list.Add(local);
                }
            }
            int count = list.Count;
            if (count > 0)
            {
                foreach (T local2 in list)
                {
                    collection.Remove(local2);
                }
                list.Clear();
            }
            return count;
        }
    }


}
