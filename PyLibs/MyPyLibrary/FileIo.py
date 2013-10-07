import os, glob
from MyPyLibrary.FileStream import *

def EnumDirectoryFiles(path, filter = '*.*'):
    allfiles = []
    for root, dirs, files in os.walk(path):
        files = glob.glob(os.path.join(root, filter))

        for f in files:
            if os.path.isdir(f):
                continue

            allfiles.append(f)

    return allfiles
