from .MainWindow import *
from .OperationBase import *
from . import GlobalData as GD

GlobalData = None

class MainWindowOperation(OperationBase):
    def __init__(self, argv):
        GD.Initialize(argv)
        GlobalData = GD.GlobalData
        ibp()

    def Run(self):
        pass

def Run(argv):
    return MainWindowOperation(argv).Run()
