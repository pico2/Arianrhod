from .NtBase import *

class OBJECT_ATTRIBUTES(Structure):
    _fields_ = \
    [
        ('Length',                              ULONG),
        ('RootDirectory',                       HANDLE),
        ('ObjectName',                          PUNICODE_STRING),
        ('Attributes',                          ULONG),
        ('SecurityDescriptor',                  PVOID),         # Points to type SECURITY_DESCRIPTOR
        ('SecurityQualityOfService',            PVOID),         # Points to type SECURITY_QUALITY_OF_SERVICE
    ]

POBJECT_ATTRIBUTES = ctypes.POINTER(OBJECT_ATTRIBUTES)


def NtClose(Handle):
    return windll.ntdll.NtClose(Handle)
