from .MainWindow import *
from .OperationBase import *

class MainWindowOperation(OperationBase):
    def __init__(self, argv):
        print(GlobalData.Lang)
        ibp()

        self.Argument = self.ParseCommandLine(argv)

    def ParseCommandLine(self, argv):
        pass

    def Run(self):
        pass

def Run(argv):
    return MainWindowOperation(argv).Run()
