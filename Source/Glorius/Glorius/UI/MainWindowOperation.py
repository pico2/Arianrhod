from . import MainWindow
from .OperationBase import *

class MainWindowOperation(OperationBase):
    def __init__(self, argv):
        self.argv = argv
        self.Argument = self.ParseCommandLine(argv)

    def ParseCommandLine(self, argv):
        pass

    def Run(self):
        app = MainWindow.QApplication(self.argv)
        wnd = MainWindow.MainWindow(self)
        wnd.show()
        return app.exec_()

def Run(argv):
    return MainWindowOperation(argv).Run()
