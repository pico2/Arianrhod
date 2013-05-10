from EDAOScenaFile import *
import random, hashlib

def GenerateUniqueLable():
    return '%X' % int(random.random() * 100000000000)

def UniqueLabel(LableName):
    sha256 = hashlib.sha256()
    sha256.update(LableName.encode('936'))

    return label(sha256.hexdigest())
