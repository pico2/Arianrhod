from .NtBase import *

FILE_NAME_NORMALIZED        = 0x0
FILE_NAME_OPENED            = 0x8

VOLUME_NAME_DOS             = 0x0
VOLUME_NAME_GUID            = 0x1
VOLUME_NAME_NT              = 0x2
VOLUME_NAME_NONE            = 0x4

def GetFinalPathNameByHandle(FileHandle, Flags = FILE_NAME_NORMALIZED | VOLUME_NAME_DOS):
    size = int(windll.kernel32.GetFinalPathNameByHandleW(FileHandle, None, 0, Flags))
    name = (WCHAR * size)()
    size = int(windll.kernel32.GetFinalPathNameByHandleW(FileHandle, byref(name), size, Flags))
    return name.value.lstrip('\\\\?\\')

def GetFileSize(FileHandle):
    size = LARGE_INTEGER()
    success = bool(windll.kernel32.GetFileSizeEx(FileHandle, PLARGE_INTEGER(size)))
    return success and size.QuadPart or None

def ReadFile(FileHandle, NumberOfBytesToRead):
    buffer = (BYTE * NumberOfBytesToRead)()
    success = bool(windll.kernel32.ReadFile(FileHandle, byref(buffer), NumberOfBytesToRead, None, None))
    return success and bytes(buffer) or b''
