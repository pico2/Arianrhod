from ml import *

def main():
    dlls = EnumDirectoryFiles(os.path.dirname(__file__), '*.dll')

    for dll in dlls:
        debug = os.path.splitext(dll)[0] + 'd.dll'
        if os.path.exists(debug):
            os.remove(debug)

    PauseConsole()

if __name__ == '__main__':
    TryInvoke(main)
