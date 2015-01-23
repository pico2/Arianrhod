import os, glob, fnmatch
from .FileStream import *

def EnumDirectoryFiles(path, filter = '*.*'):
    allfiles = []
    if filter == '*.*':
        filter = '*'

    for root, dirs, files in os.walk(path):
        for f in files:
            f = os.path.join(root, f)
            fnmatch.filter([f], filter) and not os.path.isdir(f) and allfiles.append(f)

    return allfiles
