def __init():
    pass
    # import sys
    # sys.dont_write_bytecode = True

    # mod = sys.modules[__name__]
    # path = mod.__path__[0]
    # sys.path.append(path)

__init()
del __init

from .common import *
from .otypes import *
from .otypes.wintypes import *

from . import console
from . import dbghelp
from . import network
from . import fileio
from . import cipher
from . import logger
from . import encoding
from . import iterlib
from . import asynclib

from .dbghelp import Try, TryInvoke, bp, ibp