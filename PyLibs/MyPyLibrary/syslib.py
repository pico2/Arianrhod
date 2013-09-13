import os, sys, struct, traceback, configparser, shutil
from io import *
from pdb import set_trace as bp
from ctypes.wintypes import *
import xml.etree.ElementTree as ET
from ctypes.wintypes import *
from ctypes import windll

CHAR = ctypes.c_char
BYTE = ctypes.c_ubyte      # fix bug: BYTE == CHAR

LONG64 = ctypes.c_longlong
ULONG64 = ctypes.c_ulonglong


def SetConsoleTitle(text):
    windll.kernel32.SetConsoleTitleW(text)

def cls():
    os.system('cls')
