from .NtBase import *

EXCEPTION_MAXIMUM_PARAMETERS = 15

class EXCEPTION_RECORD(Structure):
    pass

PEXCEPTION_RECORD = ctypes.POINTER(EXCEPTION_RECORD)

EXCEPTION_RECORD._fields_ = \
[
    ('ExceptionCode',               ULONG),
    ('ExceptionFlags',              ULONG),
    ('ExceptionRecord',             PEXCEPTION_RECORD),
    ('ExceptionAddress',            PVOID),
    ('NumberParameters',            ULONG),
    ('ExceptionInformation',        ULONG_PTR * EXCEPTION_MAXIMUM_PARAMETERS),
]

def main():
    pass

if __name__ == '__main__':
    TryInvoke(main)
