def AppendRelativePath(path, file = None):
    import sys, os
    if file is not None:
        path = os.path.dirname(file) + '\\' + path

    path = os.path.abspath(path)

    if path not in sys.path:
        sys.path.append(path)

AppendRelativePath('.', __file__)

from Libs.Misc import *
from Libs.Image import *
from Libs.IO import *
from Libs.Network import *
from Libs.Helper import *
