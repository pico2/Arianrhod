from ml import *
from .UI import GlobalData

def Run(argv):
    GlobalData.Initialize(argv)

    from .UI import MainWindowOperation
    return MainWindowOperation.Run(argv)
