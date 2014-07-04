import os, sys, struct, traceback, configparser, shutil, json
from io import *
from ctypes.wintypes import *
import xml.etree.ElementTree as ET
from ctypes.wintypes import *
from ctypes import windll, cdll, byref, wintypes
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

class qtbp(object):
    def __init__(self):
        from PyQt5.QtCore import pyqtRemoveInputHook
        pyqtRemoveInputHook()
        ibp()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        from PyQt5.QtCore import pyqtRestoreInputHook
        pyqtRestoreInputHook()


ibp = ibp_init

CHAR        = ctypes.c_char
BYTE        = ctypes.c_ubyte      # fix bug: BYTE == CHAR
UCHAR       = BYTE

PLONG       = ctypes.POINTER(LONG)
PULONG      = ctypes.POINTER(ULONG)

LONG64      = ctypes.c_longlong
LONGLONG    = LONG64
ULONG64     = ctypes.c_ulonglong
ULONGLONG   = ULONG64

PLONG64     = ctypes.POINTER(LONG64)
PULONG64    = ctypes.POINTER(ULONG64)

PVOID       = ctypes.c_void_p
PSTR        = ctypes.c_char_p

NTSTATUS    = LONG

ANSI_CODE_PAGE = 'mbcs'

class IncorrectLengthOfData(Exception):
    def __init__(self, type):
        super().__init__('Incorrect length of data while initializing %s' % type)

class StructureUnionBase(object):
    def __init__(self, basetype, *args, **kwargs):

        from ..IO.FileStream import FileStream

        if len(args) == 1 and isinstance(args[0], (bytes, bytearray, FileStream)):
            basetype.__init__(self)
            buf = args[0]
            if isinstance(buf, FileStream):
                buf = buf.Read(len(self))
                if len(buf) != len(self):
                    raise IncorrectLengthOfData(type(self))

            self.__frombytes__(buf)

        else:
            basetype.__init__(self, *args, **kwargs)

    def __tobytes__(self):
        size = len(self)
        buff = (CHAR * size)()
        ctypes.memmove(buff, ctypes.addressof(self), size)

        return bytearray(buff)

    def __frombytes__(self, buffer):
        size = len(buffer)
        buff = (CHAR * size).from_buffer_copy(buffer)
        ctypes.memmove(ctypes.addressof(self), ctypes.addressof(buff), size)

        return self

    def __len__(self):
        return ctypes.sizeof(self)

class Structure(ctypes.Structure, StructureUnionBase):
    def __init__(self, *args, **kwargs):
        StructureUnionBase.__init__(self, ctypes.Structure, *args, **kwargs)

class Union(ctypes.Union, StructureUnionBase):
    def __init__(self, *args, **kwargs):
        StructureUnionBase.__init__(self, ctypes.Union, *args, **kwargs)


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

from collections import *
from .ordered_set import OrderedSet

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

class CaseInsensitiveDict(dict):
    """Dictionary that enables case insensitive searching while preserving case sensitivity
when keys are listed, ie, via keys() or items() methods.

Works by storing a lowercase version of the key as the new key and stores the original key-value
pair as the key's value (values become dictionaries)."""

    def __init__(self, initval = None):

        if isinstance(initval, dict):
            for key, value in initval.iteritems():
                self.__setitem__(key, value)

        elif isinstance(initval, list):
            for (key, value) in initval:
                self.__setitem__(key, value)

    def __contains__(self, key):
        return dict.__contains__(self, key.lower())

    def __getitem__(self, key):
        return dict.__getitem__(self, key.lower())['val']

    def __setitem__(self, key, value):
        return dict.__setitem__(self, key.lower(), {'key': key, 'val': value})

    def get(self, key, default=None):
        try:
            v = dict.__getitem__(self, key.lower())
        except KeyError:
            return default
        else:
            return v['val']

    def has_key(self,key):
        if self.get(key):
            return True
        else:
            return False

    def items(self):
        return [(v['key'], v['val']) for v in dict.itervalues(self)]

    def keys(self):
        return [v['key'] for v in dict.itervalues(self)]

    def values(self):
        return [v['val'] for v in dict.itervalues(self)]

    def iteritems(self):
        for v in dict.itervalues(self):
            yield v['key'], v['val']

    def iterkeys(self):
        for v in dict.itervalues(self):
            yield v['key']

    def itervalues(self):
        for v in dict.itervalues(self):
            yield v['val']