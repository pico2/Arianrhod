def init():
    import sys

    # sys.dont_write_bytecode = True

    # mod = sys.modules[__name__]
    # path = mod.__path__[0]
    # sys.path.append(path)

init()
del init

from .common import *
from .otypes import *

from . import console
from . import dbghelp
from . import network
from . import fileio
from . import cipher

from .dbghelp import Try, TryInvoke, bp, ibp