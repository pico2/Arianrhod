from ml import *
import pyhooker
import binascii

def HookNtClose(context):
    # print('%s' % context.OriginalEip.read(16))
    # print(pyhooker._pyhooker.ReadAnsi(int(context.Eip)))
    # print('%X' % context.Eip)
    # print()
    # print('%X' % context.GetArgument(context.ARG_RETURN_ADDRESS))

    ctx = WinTypes.CONTEXT()
    ctx.Eip = 0x87654321
    pyhooker.Call(ctx)
    pass

def main():
    NtClose = windll.kernel32.GetProcAddress(windll.ntdll._handle, b'NtClose')
    pyhooker.Hook(NtClose, HookNtClose)
