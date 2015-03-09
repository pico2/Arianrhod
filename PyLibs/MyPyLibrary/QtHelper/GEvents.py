from ml import *
import threading

def InitializeEvents(EventList):
    Events = OrderedDictEx()
    EventID = 0
    for event in EventList:
        sub = event.split('.')
        if len(sub) == 1:
            Events[sub[0]] = EventID

        else:
            e = Events
            for ev in sub[:-1]:
                if ev not in e:
                    e[ev] = OrderedDictEx()

                e = e[ev]

            e[sub[-1]] = EventID

        EventID += 1

    Events['MaximumEventID'] = EventID

    return Events

class GEvent(object):
    def __init__(self, Event, *args, **kwargs):
        self.Event       = Event
        self.args        = args
        self.kwargs      = kwargs
        self.Handled     = False
        self.ReturnValue = None
        self.waitEvent   = None

    def wait(self):
        self.waitEvent and self.waitEvent.wait()

    def set(self):
        self.waitEvent and self.waitEvent.set()

    def createWaitEvent(self):
        if self.waitEvent is not None:
            return

        self.waitEvent = threading.Event()

    def __str__(self):
        return _GEventList[self.Event]
