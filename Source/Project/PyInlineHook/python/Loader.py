from ml import *
import pyhooker
import binascii

def HookNtClose(context):
    # print('%s' % context.OriginalEip.read(16))
    # print(pyhooker._pyhooker.ReadAnsi(int(context.Eip)))
    # print('%X' % context.Eip)
    # print()
    # print('%X' % context.GetArgument(context.ARG_RETURN_ADDRESS))

    st = 2
    NtClose = pyhooker.StdCall(pyhooker.FindRoutine('ntdll', 'NtClose'))
    st = NtClose(0)
    print(type(st))
    PauseConsole('%X' % st)
    pass

def main():
    NtClose = windll.kernel32.GetProcAddress(windll.ntdll._handle, b'NtClose')
    pyhooker.Hook(NtClose, HookNtClose)
