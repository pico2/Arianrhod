using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace InstanceAnswerPro.Controls
{
    public interface IGUISerialized
    {
        // Methods
        bool Deserialize(ClipboardControl serializedContent);
        ClipboardControl Serialize();
    }
    
}
