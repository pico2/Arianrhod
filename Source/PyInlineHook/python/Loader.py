from ml import *
import pyhooker
import binascii

def HookNtClose(context):
    print('%X' % context.OriginalEip)
    print(binascii.hexlify(context.OriginalEip.read(16)))
    print(binascii.hexlify(context.Eip.read(16)))
    # print('%X' % context.Eip)
    # print()
    # print('%X' % context.GetArgument(context.ARG_RETURN_ADDRESS))
    pass

def main():
    NtClose = windll.kernel32.GetProcAddress(windll.ntdll._handle, b'NtClose')
    pyhooker.Hook(NtClose, HookNtClose)
