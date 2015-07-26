from .Common import *
from .Manager import *

class DockerContainer(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setTabPosition(Qt.AllDockWidgetAreas, QTabWidget.North)
        self.setDockOptions(QMainWindow.AnimatedDocks | QMainWindow.AllowNestedDocks | QMainWindow.AllowTabbedDocks)
        self.setGeometry(550, 340, 720, 500)

        self.manager = DockerManager(self)

    def createDocker(self, *args, **kwargs):
        return self.manager.createDocker(*args, **kwargs)
