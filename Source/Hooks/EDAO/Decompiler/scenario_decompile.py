from ScenarioType import *

def main():
    scena = ScenarioInfo()

    fn = sys.argv[1] if len(sys.argv) > 1 else 'a0000.bin'

    scena.open(fn)
    scena.SaveToFile(os.path.splitext(fn)[0] + '.py')

    print('done')
    #input()

TryInvoke(main)
