from .CommonWindow import *
from . import WindowCpu

class MainWindow(QMainWindow):
    def __init__(self, Operation):
        super().__init__()

        self.Operation = Operation

        self.setDockNestingEnabled(True)
        self.setWindowTitle(GlobalData.Lang.WindowTitle)

        self.CreateStatusBar()
        self.CreateActions()
        self.CreateMenus()
        self.CreateDockWindows()

    def CreateStatusBar(self):
        self.statusBar()

    def CreateActions(self):
        def CreateAction(text, shortcut, tip, triggered):
            return QAction(text, self, shortcut = shortcut or '', statusTip = tip, triggered = triggered)

        class __Actions(object):
            __slots__ = ['File', 'View', 'Debug', 'Plugins', 'Options', 'Window', 'Help']


        Lang = GlobalData.Lang
        Shortcuts = GlobalData.Preferences.Shortcuts

        self.Actions = __Actions()

        self.Actions.File = \
        [
            CreateAction(Lang.Menu.File.Open,   Shortcuts.Menu.File.get('Open'),   Lang.Menu.get('Open:Tip'),      self.ActionOpen),
            CreateAction(Lang.Menu.File.Attach, Shortcuts.Menu.File.get('Attach'), Lang.Menu.get('Attach:Tip'),    self.ActionAttach),
            CreateAction(Lang.Menu.File.Detach, Shortcuts.Menu.File.get('Detach'), Lang.Menu.get('Detach:Tip'),    self.ActionDetach),
            None,
            CreateAction(Lang.Menu.File.Exit,   Shortcuts.Menu.File.get('Exit'),   Lang.Menu.get('Exit:Tip'),      self.ActionExit),
        ]

        self.Actions.View = \
        [
            CreateAction(Lang.Menu.File.Open,   Shortcuts.Menu.File.get('Open'),   Lang.Menu.get('Open:Tip'),      self.ActionOpen),
        ]

    def CreateMenus(self):
        MenuBar = self.menuBar()
        self.FileMenu = MenuBar.addMenu(GlobalData.Lang.Menu.FileMenu)

        for act in self.Actions.File:
            self.FileMenu.addSeparator() if act is None else self.FileMenu.addAction(act)

        self.ViewMenu = MenuBar.addMenu(GlobalData.Lang.Menu.ViewMenu)

    def CreateDockWindows(self):
        dock = GDockWindow(GlobalData.Lang.Docks.Cpu, self)
        dock.setAllowedAreas(Qt.AllDockWidgetAreas)
        dock.setWidget(WindowCpu.WindowCpu())
        self.addDockWidget(Qt.LeftDockWidgetArea, dock)
        self.ViewMenu.addAction(dock.toggleViewAction())

    def sizeHint(self):
        return QSize(800, 600)

    ##################################################
    # action handler
    ##################################################

    def ActionOpen(self):
        pass

    def ActionAttach(self):
        pass

    def ActionDetach(self):
        pass

    def ActionExit(self):
        self.close()

