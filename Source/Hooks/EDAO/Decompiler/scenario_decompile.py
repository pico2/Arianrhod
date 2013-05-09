from ScenarioScript import *

def main():
    scena = ScenarioInfo()

    argv = sys.argv[1:]
    if len(argv) == 0:
        argv.append('m4290.b')

    for fn in argv:
        scena.open(fn)
        scena.SaveToFile(fn + '.py')

    print('done')
    #input()

TryInvoke(main)
