from mlqt import *
from .GEvents import *

class EventDispatcher(QObject):
    SyncEventReceiver = pyqtSignal(GEvent)
    AutoEventReceiver = pyqtSignal(GEvent)

    def __init__(self, DefaultDispatcher = None):
        super().__init__()

        self.DispatchTable = dict()

        self.DefaultDispatcher = DefaultDispatcher
        Dispatcher = DefaultDispatcher and self.DispatcherWrap or self.Dispatcher
        self.SyncEventReceiver.connect(Dispatcher, type = Qt.BlockingQueuedConnection)
        self.AutoEventReceiver.connect(Dispatcher, type = Qt.AutoConnection)

    def RegisterEventHandler(self, EventType, Handler):
        self.DispatchTable[EventType] = Handler

    def PostEvent(self, Event, *args, **kwargs):
        if not isinstance(Event, GEvent):
            Event = GEvent(Event, *args, **kwargs)

        self.AutoEventReceiver.emit(Event)

    def SendEvent(self, Event, *args, **kwargs):
        if not isinstance(Event, GEvent):
            Event = GEvent(Event, *args, **kwargs)

        if self.thread() == QThread.currentThread():
            self.AutoEventReceiver.emit(Event)

        else:
            Event.__EventLoop__ = QEventLoop()
            self.AutoEventReceiver.emit(Event)
            Event.__EventLoop__.exec_()

        return Event.ReturnValue

    def Dispatcher(self, Event):
        handler = self.DispatchTable.get(Event.Event)
        Event.ReturnValue = handler and handler(Event, *Event.args, **Event.kwargs)
        Event.__EventLoop__ and Event.__EventLoop__.quit()

    def DispatcherWrap(self, Event):
        self.DefaultDispatcher(Event)
        Event.__EventLoop__ and Event.__EventLoop__.quit()
