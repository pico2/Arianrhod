using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RecordViewer
{
    public class EDAOSaveData
    {
        byte[] saveData;

        int ScenaFlagsOffset = 0x1B008;

        public EDAOSaveData(String SaveDataPath)
        {
            using (System.IO.FileStream fs = new System.IO.FileStream(SaveDataPath, System.IO.FileMode.Open))
            {
                using (System.IO.BinaryReader br = new System.IO.BinaryReader(fs))
                {
                    saveData = br.ReadBytes((int)fs.Length);
                }
            }
        }

        int MakeScenarioFlags(int Offset, int Bit)
        {
            return (Offset << 3) | (Bit & 7);
        }

        public Boolean TestScenaFlag(int Offset, int Bit)
        {
            if (Offset >= 0x220 || Offset < 0)
                return false;

            return (saveData[ScenaFlagsOffset + Offset] & (1 << Bit)) != 0;
        }
    }
}
