using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace RecordViewer
{
    public class RecordViewerData
    {
        EDAOSaveData saveData = null;

        public void OpenSaveData(String FullPath)
        {
            EDAOSaveData sd = new EDAOSaveData(FullPath);
            this.saveData = sd;
        }

        public EDAOSaveData GetSaveData()
        {
            return saveData;
        }
    }
}
