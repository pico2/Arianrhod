from mlqt import *
from .GEvents import *

class EventDispatcher(QObject):
    AutoEventReceiver = pyqtSignal(GEvent)

    def __init__(self, DefaultDispatcher = None):
        super().__init__()

        self.DispatchTable = dict()

        self.DefaultDispatcher = DefaultDispatcher
        Dispatcher = DefaultDispatcher and self.DispatcherWrap or self.Dispatcher
        self.AutoEventReceiver.connect(Dispatcher, type = Qt.AutoConnection)

    def RegisterEventHandler(self, EventType, Handler):
        self.DispatchTable[EventType] = Handler

    def PostEvent(self, event, *args, **kwargs):
        if not isinstance(event, GEvent):
            event = GEvent(event, *args, **kwargs)

        self.AutoEventReceiver.emit(event)

    def SendEvent(self, event, *args, **kwargs):
        if not isinstance(event, GEvent):
            event = GEvent(event, *args, **kwargs)

        if self.thread() == QThread.currentThread():
            self.AutoEventReceiver.emit(event)

        else:
            event.createWaitEvent()
            self.AutoEventReceiver.emit(event)
            event.wait()

        return event.ReturnValue

    def Dispatcher(self, event):
        handler = self.DispatchTable.get(event.Event)
        event.ReturnValue = handler and handler(event, *event.args, **event.kwargs)
        event.set()

    def DispatcherWrap(self, event):
        self.DefaultDispatcher(event)
        event.set()
