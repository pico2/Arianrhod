from .Common import *
from .Docker import Docker

class DockerManager(QObject):
    def __init__(self, mainWindow):
        super().__init__()

        self.tabs = []
        self.mainWindow = mainWindow

        self.dockerIdMap = {}

    def createDocker(self, *args, **kwargs):
        docker = Docker(*args, **kwargs)
        docker.topLevelChanged.connect(self.dockerTopLevelChanged)
        # docker.toggleViewAction().triggered.connect(self.dockerToggleViewActionTriggered)

        return docker

    def updateDocker(self, docker, state):
        docker.setTitleBarVisible({
            Docker.Floating    : True,
            Docker.Docked      : True,
            Docker.Tabified    : False,
        }[state])

    def dockerTopLevelChanged(self, topLevel):
        docker = self.sender()

        print(docker)

        if topLevel:
            state = Docker.Floating

        else:
            tabifiedDockers = self.mainWindow.tabifiedDockWidgets(docker)
            if tabifiedDockers:
                state = Docker.Tabified

                for tab in self.mainWindow.findChildren(QTabBar):
                    self.dockerIdMap[tab.tabData(0)] = docker
                    print(tab)
                    for i in range(tab.count()):
                        print('%X, %X' % (tab.tabData(i), id(docker)))

            else:
                state = Docker.Docked

        # self.updateDocker(docker, state)

    def dockerToggleViewActionTriggered(self, visible):
        pass

    def dockFromTab(self, tabbar, index):
        pass
