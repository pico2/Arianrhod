from ml import *
import imp
import _pyhooker

POINTER_SIZE = ctypes.sizeof(PVOID)

class Register(object):
    def __init__(self, address):
        self.address = address

    def __float__(self):
        return float(self.address)

    def __int__(self):
        return int(self.address)

    def __hex__(self):
        return '%X' % self.address

    def __eq__(self, y):
        if isinstance(y, str):
            return self.unicode() == y

        return self.address == y

    def __add__(self, y):
        return Register(self.address + int(y))

    def __sub__(self, y):
        return Register(self.address - int(y))

    def __mul__(self, y):
        return Register(self.address * int(y))

    def __truediv__(self, y):
        return Register(self.address / int(y))

    def read(self, size):
        return _pyhooker.ReadMemory(self.address, int(size))

    def gbk(self):
        return _pyhooker.ReadAnsi(self.address).decode('GBK')

    def utf8(self):
        return _pyhooker.ReadAnsi(self.address).decode('UTF8')

    def unicode(self):
        return _pyhooker.ReadUnicode(self.address)

    def u64(self):
        return Register(struct.unpack('<Q', self.read(8))[0])

    def u32(self):
        return Register(struct.unpack('<I', self.read(4))[0])

    def u16(self):
        return Register(struct.unpack('<H', self.read(2))[0])

    def u8(self):
        return Register(struct.unpack('<B', self.read(1))[0])

    def s64(self):
        return Register(struct.unpack('<q', self.read(8))[0])

    def s32(self):
        return Register(struct.unpack('<i', self.read(4))[0])

    def s16(self):
        return Register(struct.unpack('<h', self.read(2))[0])

    def s8(self):
        return Register(struct.unpack('<b', self.read(1))[0])

class HookContext(object):
    # __slots__ = ('Eax', 'Ecx', 'Edx', 'Ebx', 'Esp', 'Ebp', 'Esi', 'Edi')

    ARG_RETURN_ADDRESS = -1

    def __init__(self, OriginalEip, Context):
        self.OriginalEip = Register(OriginalEip)
        self.Eax = Register(Context.Eax)
        self.Ecx = Register(Context.Ecx)
        self.Edx = Register(Context.Edx)
        self.Ebx = Register(Context.Ebx)
        self.Esp = Register(Context.Esp)
        self.Ebp = Register(Context.Ebp)
        self.Esi = Register(Context.Esi)
        self.Edi = Register(Context.Edi)
        self.Eip = Register(Context.Eip)

        self.Flush = self.Flush32

    def Flush32(self, Context):
        Context.Eax = int(self.Eax)
        Context.Ecx = int(self.Ecx)
        Context.Edx = int(self.Edx)
        Context.Ebx = int(self.Ebx)
        Context.Esp = int(self.Esp)
        Context.Ebp = int(self.Ebp)
        Context.Esi = int(self.Esi)
        Context.Edi = int(self.Edi)
        Context.Eip = int(self.Eip)

    def GetArgument(self, Index):
        if POINTER_SIZE == 4:
            return (self.Esp + (Index + 1) * POINTER_SIZE).u32()

        elif POINTER_SIZE == 8:
            return (self.Rsp + (Index + 1) * POINTER_SIZE).u64()

    def SetArgument(self, Index, Value):
        raise

class PyHooker(object):
    FASTCALL, STDCALL, CDECL, SPEC_CONTEXT = range(4)

    def __init__(self):
        self.AddressTable = {}

    def Hook(self, address, callback):
        address = int(address)
        cb = self.AddressTable.get(address)

        if cb is not None:
            cb.add(callback)
            return

        self.AddressTable.setdefault(address, OrderedSet()).add(callback)
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

    def Dispatcher(self, address, context):
        ctx = WinTypes.CONTEXT.from_address(context)
        hookctx = HookContext(address, ctx)

        for cb in self.AddressTable[address]:
            try:
                cb(hookctx)
            except:
                traceback.print_exception(*sys.exc_info())

        hookctx.Flush(ctx)

    def FastCall(self, Address):
        def wrapper(*args, **kwargs):
            return self._Call(self.FASTCALL, Address, *args, **kwargs)
        return wrapper

    def Cdecl(self, Address):
        def wrapper(*args, **kwargs):
            return self._Call(self.CDECL, Address, *args, **kwargs)
        return wrapper

    def StdCall(self, Address):
        def wrapper(*args, **kwargs):
            return self._Call(self.STDCALL, Address, *args, **kwargs)
        return wrapper

    def _Call(self, CallingConventions, Address, *args, **kwargs):
        converter = {
            int         : lambda arg : ULONG_PTR(arg),
            float       : lambda arg : FLOAT(arg),
            str         : lambda arg : PWSTR(arg),
            bytes       : lambda arg : (BYTE * len(arg)).from_buffer_copy(arg),
            bytearray   : lambda arg : (BYTE * len(arg)).from_buffer(arg),
        }

        nativeargs = [converter[type(arg)](arg) for arg in args]

        if CallingConventions == self.STDCALL:
            func = ctypes.WINFUNCTYPE(ULONG_PTR, *[type(arg) for arg in nativeargs])

        elif CallingConventions == self.CDECL:
            func = ctypes.CFUNCTYPE(ULONG_PTR, *[type(arg) for arg in nativeargs])

        elif CallingConventions == self.FASTCALL:
            raise NotImplementedError

        elif CallingConventions == self.SPEC_CONTEXT:
            raise NotImplementedError

        return func(Address)(*nativeargs)

    def FindRoutine(self, module, routine):
        return windll.kernel32.GetProcAddress(getattr(windll, module)._handle, routine.encode('mbcs'))

_hooker = PyHooker()

Hook                = _hooker.Hook
UnHook              = _hooker.UnHook
FastCall            = _hooker.FastCall
Cdecl               = _hooker.Cdecl
StdCall             = _hooker.StdCall
FindRoutine         = _hooker.FindRoutine

def main():
    name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
    mod = imp.importlib.import_module(name)
    mod.main()
