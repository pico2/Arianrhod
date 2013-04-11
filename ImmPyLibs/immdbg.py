import os, sys, struct

if sys.winver == '2.7':
    import pefile
    import debugger
    import immutils
    from immlib2 import *
    from libhook import *
    from wintypes2 import *
    from immhelper import *

    imm = Debugger2()

    def PrintException(e = None):
        excinfo = FormatException(e)
        for line in excinfo:
            imm.log(line)

