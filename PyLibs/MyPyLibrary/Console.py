from SysLib import *

getch = ctypes.CFUNCTYPE(ctypes.c_int32)(('_getch', windll.msvcrt))

def PauseConsole(text = None):
    if text is not None:
        print(text)
    getch()

def SetConsoleTitle(text):
    windll.kernel32.SetConsoleTitleW(str(text))

def cls2():
    os.system('cls')

def PrintLog(value, *args, sep=' ', end='\n', file=sys.stdout, flush=False):
    pass

class _flushstdout(TextIOWrapper):
    def __init__(self, *args):
        super().__init__(*args)
        self.stdout = args[0]

        for attr in dir(self.stdout):
            try:
                setattr(self, attr, getattr(self.stdout, attr))
            except:
                pass

        self.write = self._flush_write

    def _flush_write(self, *args):
        self.stdout.write(*args)
        self.stdout.flush()

sys.stdout = _flushstdout(sys.stdout)
