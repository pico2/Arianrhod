from ml import *
from . import GlobalData

def Run(argv):
    GlobalData.Initialize(argv)

    from . import MainWindowOperation
    return MainWindowOperation.Run(argv)
