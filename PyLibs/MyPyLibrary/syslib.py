import os, sys, struct, traceback, configparser, shutil
from io import *
from ctypes.wintypes import *
import xml.etree.ElementTree as ET
from ctypes.wintypes import *
from ctypes import windll
from pdb import set_trace as bp


def ibp_init():
    global ibp
    try:
        from ipdb import set_trace as ibp
    except:
        ibp = ibp_stub

    return ibp()

def ibp_stub():
    bp()

def ibp_worker():
    pass

ibp = ibp_init


CHAR    = ctypes.c_char
BYTE    = ctypes.c_ubyte      # fix bug: BYTE == CHAR

LONG64  = ctypes.c_longlong
ULONG64 = ctypes.c_ulonglong

PVOID   = ctypes.c_void_p
PSTR    = ctypes.c_char_p

