import os, sys, struct, traceback, configparser, shutil
from io import *
from ctypes.wintypes import *
import xml.etree.ElementTree as ET
from ctypes.wintypes import *
from ctypes import windll
from pdb import set_trace as bp

try:
    from ipdb import set_trace as ibp
except:
    pass

CHAR = ctypes.c_char
BYTE = ctypes.c_ubyte      # fix bug: BYTE == CHAR

LONG64 = ctypes.c_longlong
ULONG64 = ctypes.c_ulonglong


