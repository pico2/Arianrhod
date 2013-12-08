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


ANSI_CODE_PAGE = 'mbcs'


class dict2(dict):
    def __init__(self, *args):
        super().__init__(*args)

        self.convert_all(self)

    def convert_all(self, obj):
        for k, v in obj.items():
            if not isinstance(v, dict):
                continue

            v = dict2(v)
            obj[k] = v
            self.convert_all(v)

    def __setattr__(self, name, value):
        return super().__setitem__(name, value)

    def __getattr__(self, name):
        try:
            attr = super().__getattr__(name)
        except AttributeError:
            attr = super().__getitem__(name)

        return attr

    def __deepcopy__(self, memo):
        import copy
        return copy._deepcopy_dict(self, memo)
