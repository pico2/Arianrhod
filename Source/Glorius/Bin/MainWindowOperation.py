from . import MainWindowView
from .OperationBase import *

class MainWindowOperation(OperationBase):
    def __init__(self, argv):
        self.argv = argv
        self.Argument = self.ParseCommandLine(argv)

    def ParseCommandLine(self, argv):
        pass

    def Run(self):
        app = MainWindowView.QApplication(self.argv)
        wnd = MainWindowView.MainWindow(self)
        wnd.show()
        return app.exec_()

def Run(argv):
    return MainWindowOperation(argv).Run()
