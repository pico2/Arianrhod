from ml import *

class OperationBase(object):
    def __init__(self, Parent):
        self.Parent = Parent
        if Parent:
            self.RegisterEventHandler   = Parent.RegisterEventHandler
            self.UnRegisterEventHandler = Parent.UnRegisterEventHandler
            self.PostEvent              = Parent.PostEvent
            self.SendEvent              = Parent.SendEvent

    def RegisterEventHandler(self, Event, Handler):
        raise NotImplementedError

    def UnRegisterEventHandler(self, Event, Handler):
        raise NotImplementedError

    def PostEvent(self, Event, *args, **kwargs):
        raise NotImplementedError

    def SendEvent(self, Event, *args, **kwargs):
        raise NotImplementedError
