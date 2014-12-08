from ml import *
from .ntstatus import *

INFINITE                    = None
DELAY_ONE_MICROSECOND       = (-10)
DELAY_ONE_MILLISECOND       = (DELAY_ONE_MICROSECOND * 1000)
DELAY_ONE_SECOND            = (DELAY_ONE_MILLISECOND * 1000)
DELAY_QUAD_INFINITE         = 0x8000000000000000

class LARGE_INTEGER(Union):
    class _(Structure):
        _fields_ = \
        [
            ('LowPart',         ULONG),
            ('HighPart',        LONG),
        ]

    _anonymous_ = ('_',)
    _fields_ = \
    [
        ('_',                   _),
        ('QuadPart',            LONG64),
    ]

PLARGE_INTEGER = ctypes.POINTER(LARGE_INTEGER)


class ULARGE_INTEGER(Union):
    class _(Structure):
        _fields_ = \
        [
            ('LowPart',         ULONG),
            ('HighPart',        ULONG),
        ]

    _anonymous_ = ('_',)
    _fields_ = \
    [
        ('_',                   _),
        ('QuadPart',            ULONG64),
    ]

PULARGE_INTEGER = ctypes.POINTER(ULARGE_INTEGER)


class UNICODE_STRING(Structure):
    _fields_ = \
    [
        ('Length',              USHORT),
        ('MaximumLength',       USHORT),
        ('Buffer',              PWSTR),
    ]

    def __init__(self, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], str):
            super().__init__()
            string = args[0]
            self.Buffer = PWSTR(string)
            self.Length = len(string) * ctypes.sizeof(WCHAR)
            self.MaximumLength = self.Length

        else:
            super.__init__(*args, **kwargs)

PUNICODE_STRING = ctypes.POINTER(UNICODE_STRING)


NtCurrentProcess    = HANDLE(-1)
NtCurrentThread     = HANDLE(-2)


#
#  The following are masks for the predefined standard access types
#

DELETE                                              = 0x00010000
READ_CONTROL                                        = 0x00020000
WRITE_DAC                                           = 0x00040000
WRITE_OWNER                                         = 0x00080000
SYNCHRONIZE                                         = 0x00100000

STANDARD_RIGHTS_REQUIRED                            = 0x000F0000

STANDARD_RIGHTS_READ                                = READ_CONTROL
STANDARD_RIGHTS_WRITE                               = READ_CONTROL
STANDARD_RIGHTS_EXECUTE                             = READ_CONTROL

STANDARD_RIGHTS_ALL                                 = 0x001F0000

SPECIFIC_RIGHTS_ALL                                 = 0x0000FFFF

#
# AccessSystemAcl access type
#

ACCESS_SYSTEM_SECURITY                              = 0x01000000

#
# MaximumAllowed access type
#

MAXIMUM_ALLOWED                                     = 0x02000000

#
#  These are the generic rights.
#

GENERIC_READ                                        = 0x80000000
GENERIC_WRITE                                       = 0x40000000
GENERIC_EXECUTE                                     = 0x20000000
GENERIC_ALL                                         = 0x10000000


#
# Thread Specific Access Rights
#

THREAD_TERMINATE                                    = 0x0001
THREAD_SUSPEND_RESUME                               = 0x0002
THREAD_ALERT                                        = 0x0004
THREAD_GET_CONTEXT                                  = 0x0008
THREAD_SET_CONTEXT                                  = 0x0010
THREAD_SET_INFORMATION                              = 0x0020
THREAD_SET_LIMITED_INFORMATION                      = 0x0400
THREAD_QUERY_LIMITED_INFORMATION                    = 0x0800
THREAD_ALL_ACCESS                                   = STANDARD_RIGHTS_REQUIRED | SYNCHRONIZE | 0xFFFF

class CLIENT_ID(Structure):
    _fields_ = \
    [
        ('UniqueProcess',       HANDLE),
        ('UniqueThread',        HANDLE),
    ]

PCLIENT_ID = ctypes.POINTER(CLIENT_ID)



class Win32Error(Exception):
    def __init__(self, Status):
        Status &= 0xFFFFFFFF
        self.Status = Status
        super().__init__('%08X' % Status)

def RtlGetLastWin32Error():
    return int(windll.ntdll.RtlGetLastWin32Error())

def FormatTimeOut(Milliseconds = INFINITE):
    TimeOut = LARGE_INTEGER()

    if Milliseconds is INFINITE:
        TimeOut.QuadPart = DELAY_QUAD_INFINITE

    else:
        TimeOut.QuadPart = DELAY_ONE_MILLISECOND * Milliseconds

    return TimeOut

def main():
    pass

if __name__ == '__main__':
    TryInvoke(main)
