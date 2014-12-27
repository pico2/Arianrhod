from ml import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKitWidgets import *

class QtThread(QtCore.QThread):
    def __init__(self, parent = None):
        super(type(self), self).__init__(parent)

        self.mutex = QMutex()
        self.condition = QWaitCondition()
        self.abort = False

    def __del__(self):
        self.mutex.lock()
        self.abort = True
        self.condition.wakeOne()
        self.mutex.unlock()

        self.wait()
