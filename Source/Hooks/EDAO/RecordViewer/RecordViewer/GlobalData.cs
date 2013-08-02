using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace RecordViewer
{
    public class GlobalData
    {
        public delegate void SaveDataChangeDelegate(EDAOSaveData NewSaveData);
        public static SaveDataChangeDelegate SaveDataChangeHandler;

        public static EDAOSaveData CurrentSaveData { get; set; }

        public static void NotifySaveDataChange(EDAOSaveData NewSaveData)
        {
            SaveDataChangeHandler(NewSaveData);
        }
    }
}
