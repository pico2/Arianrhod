from ml import *
import pyhooker

def HookNtClose(context):
    print(context)

def main():
    print(pyhooker.Hook)
    print(pyhooker.UnHook)
    NtClose = windll.kernel32.GetProcAddress(windll.ntdll._handle, b'NtClose')
    print('%08X' % NtClose)

    ibp()
    pyhooker.Hook(NtClose, HookNtClose)
