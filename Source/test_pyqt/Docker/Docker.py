from .Common import *

class Docker(QDockWidget):
    Floating    = 0
    Docked      = 1
    Tabified    = 2

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.emptyTitleBar = QWidget()

    def setTitleBarVisible(self, visible):
        if visible:
            self.setTitleBarWidget(None)
        else:
            self.setTitleBarWidget(self.emptyTitleBar)
