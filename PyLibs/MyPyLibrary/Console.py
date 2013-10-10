from syslib import *

def SetConsoleTitle(text):
    windll.kernel32.SetConsoleTitleW(str(text))

def cls():
    os.system('cls')

def PrintLog(value, *args, sep=' ', end='\n', file=sys.stdout, flush=False):
    pass
