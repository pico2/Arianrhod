from ml import *
from . import MainWindowOperation

def Run(argv):
    return MainWindowOperation.Run(argv)

def main():
    Glorius.Run(sys.argv)

if __name__ == '__main__':
    TryInvoke(main)
