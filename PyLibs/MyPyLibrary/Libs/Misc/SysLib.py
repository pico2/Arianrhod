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

PLONG = ctypes.POINTER(LONG)
PULONG = ctypes.POINTER(ULONG)

LONG64  = ctypes.c_longlong
ULONG64 = ctypes.c_ulonglong

PLONG64  = ctypes.POINTER(LONG64)
PULONG64 = ctypes.POINTER(ULONG64)

PVOID   = ctypes.c_void_p
PSTR    = ctypes.c_char_p

NTSTATUS = LONG

ANSI_CODE_PAGE = 'mbcs'


class dict2(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if kwargs.get('deep_convert') is not False:
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
            return super().__getattr__(name)
        except AttributeError:
            pass

        try:
            return super().__getitem__(name)
        except KeyError:
            raise AttributeError(''''%s' object has no attribute '%s' ''' % (type(self), name))

    def __deepcopy__(self, memo):
        import copy
        return copy._deepcopy_dict(self, memo)

from collections import OrderedDict

class OrderedDictEx(OrderedDict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if kwargs.get('deep_convert') is not False:
            self.convert_all(self)

    def convert_all(self, obj):
        for k, v in obj.items():
            if not isinstance(v, dict):
                continue

            v = type(self)(v)
            obj[k] = v
            self.convert_all(v)

    def __getattr__(self, name):
        try:
            return super().__getattr__(name)
        except AttributeError:
            pass

        try:
            return super().__getitem__(name)
        except KeyError:
            pass

        raise AttributeError(''''%s' object has no attribute '%s' ''' % (type(self), name))
