from ScenarioType import *

def main():
    scena = ScenarioInfo()

    fn = sys.argv[1] if len(sys.argv) > 1 else 'm4220.bbb'

    scena.open(fn)
    scena.SaveToFile(fn + '.py')

    print('done')
    #input()

TryInvoke(main)
