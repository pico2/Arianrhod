import os, glob
from FileStream import *

def EnumDirectoryFiles(path, filter = '*.*'):
    allfiles = []
    for root, dirs, files in os.walk(path):
        allfiles += glob.glob(os.path.join(root, filter))
    return allfiles
