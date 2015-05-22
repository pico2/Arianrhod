from ml import *
import asyncio
from .EventBase import EventDispatcher

class OperationBase(object):
    def __init__(self, parent = None):
        self.parent = parent
        if parent:
            self.RegisterEventHandler   = parent.RegisterEventHandler
            self.UnRegisterEventHandler = parent.UnRegisterEventHandler
            self.PostEvent              = parent.PostEvent
            self.SendEvent              = parent.SendEvent
            self.AsyncSendEvent         = parent.AsyncSendEvent

        self.eventHandlers = {}
        self.Dispatcher = EventDispatcher(self.EventHandler)

    @property
    def rootParent(self):
        parent = self
        while parent.parent:
            parent = parent.parent

        return parent

    def RegisterEventHandler(self, event, handler, insertFront = False):
        handlerList = self.eventHandlers.setdefault(event, [])
        handlerList.append(handler) if insertFront is False else handlerList.insert(0, Handler)

    def UnRegisterEventHandler(self, event, handler):
        try:
            self.eventHandlers[event].remove(handler)
            if len(self.eventHandlers[event]) == 0:
                del self.eventHandlers[event]

        except (KeyError, ValueError):
            pass


    def PostEvent(self, event, *args, **kwargs):
        return self.Dispatcher.PostEvent(event, *args, **kwargs)

    def SendEvent(self, event, *args, **kwargs):
        return self.Dispatcher.SendEvent(event, *args, **kwargs)

    def EventHandler(self, event):
        try:
            handlerList = self.eventHandlers[event.Event]
        except KeyError:
            return

        for handler in handlerList:
            event.Handled = True
            event.ReturnValue = handler(event, *event.args, **event.kwargs)
            if event.Handled is True:
                return

    @asyncio.coroutine
    def AsyncSendEvent(self, Event, *args, **kwargs):
        raise NotImplementedError

    @asyncio.coroutine
    def AsyncEvent(self, *args, **kwargs):
        pass
