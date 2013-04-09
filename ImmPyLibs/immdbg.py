import pefile
import debugger
import os, sys, struct, traceback
import immutils
from immlib2 import *
from libhook import *
from wintypes2 import *

imm = Debugger2()

def is_unicode(text):
    return type(text) == unicode

def utf8(text):
    return text.decode('utf8') if not is_unicode(text) else text

def gbk(text):
    return text.decode('936') if not is_unicode(text) else text

def sjis(text):
    return text.decode('932') if not is_unicode(text) else text

def FormatException(e = None):
    return traceback.format_exception(*sys.exc_info())

def PrintException(e = None):
    excinfo = FormatException(e)
    for line in excinfo:
        imm.log(line)
