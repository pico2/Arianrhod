from .NtBase import *

class MEMORY_INFORMATION_CLASS:
    MemoryBasicInformation              = 0
    MemoryWorkingSetInformation         = 1
    MemoryMappedFilenameInformation     = 2
    MemoryRegionInformation             = 3
    MemoryWorkingSetExInformation       = 4

class MEMORY_BASIC_INFORMATION(Structure):
    _fields_ = \
    [
        ('BaseAddress',                 PVOID),
        ('AllocationBase',              PVOID),
        ('AllocationProtect',           ULONG),
        ('RegionSize',                  ULONG_PTR),
        ('State',                       ULONG),
        ('Protect',                     ULONG),
        ('Type',                        ULONG),
    ]

PMEMORY_BASIC_INFORMATION = ctypes.POINTER(MEMORY_BASIC_INFORMATION)

def NtQueryVirtualMemory(ProcessHandle, BaseAddress, MemoryInformationClass, MemoryInformation, MemoryInformationLength):
    ReturnLength = ULONG_PTR(0)
    Status = windll.ntdll.NtQueryVirtualMemory(
                HANDLE(ProcessHandle),
                PVOID(BaseAddress),
                LONG(MemoryInformationClass),
                MemoryInformation and ctypes.POINTER(type(MemoryInformation))(MemoryInformation) or PVOID(),
                ULONG_PTR(MemoryInformationLength),
                PULONG_PTR(ReturnLength)
            )

    return Status, ReturnLength.value

def NtReadVirtualMemory(ProcessHandle, BaseAddress, NumberOfBytesToRead):
    Buffer = (BYTE * NumberOfBytesToRead)()
    NumberOfBytesRead = ULONG_PTR(0)

    Status = windll.ntdll.NtReadVirtualMemory(
                HANDLE(ProcessHandle),
                PVOID(BaseAddress),
                byref(Buffer),
                len(Buffer),
                PULONG_PTR(NumberOfBytesRead)
            )

    return bytearray(Buffer[:NumberOfBytesRead])

def NtWriteVirtualMemory(ProcessHandle, BaseAddress, Buffer):
    Buffer = (BYTE * NumberOfBytesToWrite)()
    buf = (BYTE * len(Buffer)).from_buffer_copy(Buffer)
    NumberOfBytesWritten = ULONG_PTR(0)

    Status = windll.ntdll.NtWriteVirtualMemory(
                HANDLE(ProcessHandle),
                PVOID(BaseAddress),
                byref(buf),
                len(buf),
                PULONG_PTR(NumberOfBytesWritten)
            )

    return NumberOfBytesWritten.value
