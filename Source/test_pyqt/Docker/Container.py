from .Common import *
from .Manager import *

class DockerContainer(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.central = QDockWidget(self)

        self.tab = QTabWidget()
        self.tab.setStyleSheet('QTabBar::tab { min-width: 100px; }')
        self.tabBar = self.tab.tabBar()
        self.tabBar.tabCloseRequested.connect(self.tabCloseRequested)
        self.tabBar.setMovable(True)
        self.tabBar.setTabsClosable(True)

        self.central.setWidget(self.tab)
        self.setCentralWidget(self.central)

        self.setTabPosition(Qt.AllDockWidgetAreas, QTabWidget.North)
        self.setDockOptions(QMainWindow.AnimatedDocks | QMainWindow.AllowNestedDocks | QMainWindow.AllowTabbedDocks)
        self.setGeometry(550, 340, 720, 500)

        self.mgr = DockerManager(self)

    def tabCloseRequested(self, index):
        docker = self.tab.widget(index)

        print(docker)

        self.tab.removeTab(index)
        self.addDockWidget(Qt.TopDockWidgetArea, docker)

        docker.setTitleBarVisible(True)
        docker.setFloating(True)
        docker.show()
