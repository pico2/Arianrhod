def AppendRelativePath(path, file = None):
    import sys, os
    if file is not None:
        path = os.path.dirname(file) + '\\' + path

    path = os.path.abspath(path)

    if path not in sys.path:
        sys.path.append(path)

AppendRelativePath('.', __file__)

from Libs import *
