from mlqt import *

class DockWindowBase(QDockWidget):
    def __init__(self, *args, **kwarg):
        super().__init__(*args, **kwarg)

class GDockWindow(DockWindowBase):
    def __init__(self, *args, **kwarg):
        super().__init__(*args, **kwarg)
