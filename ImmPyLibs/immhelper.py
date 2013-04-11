import os, sys, traceback

def is_unicode(text):
    return type(text) == unicode

def mbcs(text):
    return text.encode('936') if is_unicode(text) else text

def utf8(text):
    return text.decode('utf8') if not is_unicode(text) else text

def gbk(text):
    return text.decode('936') if not is_unicode(text) else text

def sjis(text):
    return text.decode('932') if not is_unicode(text) else text

def FormatException(e = None):
    return traceback.format_exception(*sys.exc_info())

def loadmod(modname):
    pypath = os.path.dirname(modname)
    pyfile = os.path.basename(modname)
    name, ext = os.path.splitext(pyfile)
    ext = ext.lower()
    if ext == '.py' or ext == '.pyc':
        pyfile = name

    if pypath != '':
        sys.path.insert(0, pypath)

    try:
        mod = __import__(pyfile, globals=globals())
    except Exception as e:
        if pypath != '':
            del sys.path[0]
        raise e

    if pypath != '':
        del sys.path[0]

    return mod

def reloadmod(module):
    modname = module.__file__
    pypath = os.path.dirname(modname)
    pyfile = os.path.basename(modname)
    name, ext = os.path.splitext(pyfile)
    ext = ext.lower()
    if ext == '.py' or ext == '.pyc':
        pyfile = name

    if pypath != '':
        sys.path.insert(0, pypath)

    try:
        mod = reload(module)
    except Exception as e:
        if pypath != '':
            del sys.path[0]
        raise e

    if pypath != '':
        del sys.path[0]

    return mod
