from ml import *
from PyQt5.QtWidgets import QApplication, QDialog, QWidget
import PyQt5.QtWidgets as QtWidgets
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

class QuitButton(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')

        quit = QtWidgets.QPushButton('Close', self)
        quit.setGeometry(10, 10, 64, 35)

        quit.clicked.connect(self.close)

        self.centerOnScreen()

    def centerOnScreen (self):
        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))


def main():
    app = QApplication(sys.argv)

    qb = QuitButton()
    qb.show()

    return app.exec_()

if __name__ == '__main__':
    TryInvoke(main)
