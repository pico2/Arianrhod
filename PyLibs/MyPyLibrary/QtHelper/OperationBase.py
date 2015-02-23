from ml import *
import asyncio

class OperationBase(object):
    def __init__(self, parent):
        self.parent = parent
        if parent:
            self.RegisterEventHandler   = parent.RegisterEventHandler
            self.UnRegisterEventHandler = parent.UnRegisterEventHandler
            self.PostEvent              = parent.PostEvent
            self.SendEvent              = parent.SendEvent

    @property
    def rootParent(self):
        parent = self
        while parent.parent:
            parent = parent.parent

        return parent

    def RegisterEventHandler(self, Event, Handler):
        raise NotImplementedError

    def UnRegisterEventHandler(self, Event, Handler):
        raise NotImplementedError

    def PostEvent(self, Event, *args, **kwargs):
        raise NotImplementedError

    def SendEvent(self, Event, *args, **kwargs):
        raise NotImplementedError

    @asyncio.coroutine
    def AsyncEvent(self, *args, **kwargs):
        pass
