from ml import *

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
    # __slots__ = ['Event', 'args', 'kwargs', 'Handled', 'ReturnValue', '__EventLoop__']

    def __init__(self, Event, *args, **kwargs):
        self.Event         = Event
        self.args          = args
        self.kwargs        = kwargs
        self.Handled       = False
        self.ReturnValue   = None
        self.__EventLoop__ = None

    def __str__(self):
        return _GEventList[self.Event]
