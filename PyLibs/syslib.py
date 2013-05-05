import os, sys, struct, traceback, configparser, shutil
from io import *
from pdb import set_trace as bp
from ctypes.wintypes import *
import xml.etree.ElementTree as ET
from ctypes.wintypes import *

CHAR = ctypes.c_char
BYTE = ctypes.c_ubyte      # fix bug: BYTE == CHAR

LONG64 = ctypes.c_longlong
ULONG64 = ctypes.c_ulonglong
