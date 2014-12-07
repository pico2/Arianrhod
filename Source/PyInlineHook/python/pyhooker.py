from ml import *
import imp
import _pyhooker

class PyHooker(object):
    def __init__(self):
        self.AddressTable = {}

    def Hook(self, address, callback):
        address = int(address)
        cb = self.AddressTable.get(address)

        if cb is not None:
            cb.add(callback)
            return

        cb = self.AddressTable.setdefault(address, OrderedSet())
        cb.add(callback)

        _pyhooker.Hook(address, self.Dispatcher)

    def UnHook(self, address, callback):
        address = int(address)

        try:
            cb = self.AddressTable[address]
            cb.remove(callback)
        except KeyError:
            return

        if cb:
            return

        del self.AddressTable[address]
        _pyhooker.UnHook(address)

    def Dispatcher(self, context):
        print(context)
        context = PVOID(context)
        print(context)

_hooker = PyHooker()

Hook = _hooker.Hook
UnHook = _hooker.UnHook

def main():
    name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
    mod = imp.importlib.import_module(name)
    mod.main()
