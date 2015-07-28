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

        docker.installEventFilter(self)

        return docker

    def updateDocker(self, docker, state):
        docker.setTitleBarVisible({
            Docker.Floating    : True,
            Docker.Docked      : True,
            Docker.Tabified    : False,
        }[state])

    def eventFilter(self, target, event):
        if isinstance(target, Docker):
            return self.handleDockerEvent(target, event)

        return super().eventFilter(target, event)

    def handleDockerEvent(self, docker, event):
        eventType = event.type()
        if eventType == QEvent.KeyPress:
            key = event.key()
            if key == Qt.Key_F5:
                floating = docker.titleBarWidget() is None
                docker.setTitleBarVisible(not floating)
                docker.setFloating(not floating)

                return True

        return super().eventFilter(docker, event)

    def dockerTopLevelChanged(self, topLevel):
        docker = self.sender()

        if not topLevel:
            for d in self.mainWindow.tabifiedDockWidgets(docker):
                print(d)
                d.setTitleBarVisible(False)

    def dockerToggleViewActionTriggered(self, visible):
        pass

    def dockFromTab(self, tabbar, index):
        pass
