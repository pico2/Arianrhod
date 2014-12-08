from .NtBase import *
from .NtException import *
from .NtProcess import *

# DBG_CONTINUE
# DBG_EXCEPTION_HANDLED
# DBG_EXCEPTION_NOT_HANDLED

DbgIdle                         = 0
DbgReplyPending                 = 1
DbgCreateThreadStateChange      = 2
DbgCreateProcessStateChange     = 3
DbgExitThreadStateChange        = 4
DbgExitProcessStateChange       = 5
DbgExceptionStateChange         = 6
DbgBreakpointStateChange        = 7
DbgSingleStepStateChange        = 8
DbgLoadDllStateChange           = 9
DbgUnloadDllStateChange         = 10


DBG_STATE = \
{
    0  : 'DbgIdle',
    1  : 'DbgReplyPending',
    2  : 'DbgCreateThreadStateChange',
    3  : 'DbgCreateProcessStateChange',
    4  : 'DbgExitThreadStateChange',
    5  : 'DbgExitProcessStateChange',
    6  : 'DbgExceptionStateChange',
    7  : 'DbgBreakpointStateChange',
    8  : 'DbgSingleStepStateChange',
    9  : 'DbgLoadDllStateChange',
    10 : 'DbgUnloadDllStateChange',
}

#
# Debug Message Structures
#
class DBGKM_EXCEPTION(Structure):
    _fields_ = \
    [
        ('ExceptionRecord',         EXCEPTION_RECORD),
        ('FirstChance',             ULONG),
    ]

PDBGKM_EXCEPTION = ctypes.POINTER(DBGKM_EXCEPTION)


class DBGKM_CREATE_THREAD(Structure):
    _fields_ = \
    [
        ('SubSystemKey',            ULONG),
        ('StartAddress',            PVOID),
    ]

PDBGKM_CREATE_THREAD = ctypes.POINTER(DBGKM_CREATE_THREAD)


class DBGKM_CREATE_PROCESS(Structure):
    _fields_ = \
    [
        ('SubSystemKey',            ULONG),
        ('FileHandle',              HANDLE),
        ('BaseOfImage',             PVOID),
        ('DebugInfoFileOffset',     ULONG_PTR),
        ('DebugInfoSize',           ULONG_PTR),
        ('InitialThread',           DBGKM_CREATE_THREAD),
    ]

PDBGKM_CREATE_PROCESS = ctypes.POINTER(DBGKM_CREATE_PROCESS)

class DBGKM_EXIT_THREAD(Structure):
    _fields_ = \
    [
        ('ExitStatus',              NTSTATUS),
    ]

PDBGKM_EXIT_THREAD = ctypes.POINTER(DBGKM_EXIT_THREAD)


class DBGKM_EXIT_PROCESS(Structure):
    _fields_ = \
    [
        ('ExitStatus',              NTSTATUS),
    ]

PDBGKM_EXIT_PROCESS = ctypes.POINTER(DBGKM_EXIT_PROCESS)

class DBGKM_LOAD_DLL(Structure):
    _fields_ = \
    [
        ('FileHandle',              HANDLE),
        ('BaseOfDll',               PVOID),
        ('DebugInfoFileOffset',     ULONG),
        ('DebugInfoSize',           ULONG),
        ('NamePointer',             PVOID),
    ]

PDBGKM_LOAD_DLL = ctypes.POINTER(DBGKM_LOAD_DLL)

class DBGKM_UNLOAD_DLL(Structure):
    _fields_ = \
    [
        ('BaseAddress',             PVOID),
    ]

PDBGKM_UNLOAD_DLL = ctypes.POINTER(DBGKM_UNLOAD_DLL)

class DBGUI_CREATE_THREAD(Structure):
    _fields_ = \
    [
        ('HandleToThread',          HANDLE),
        ('NewThread',               DBGKM_CREATE_THREAD),
    ]

PDBGUI_CREATE_THREAD = ctypes.POINTER(DBGUI_CREATE_THREAD)

class DBGUI_CREATE_PROCESS(Structure):
    _fields_ = \
    [
        ('HandleToProcess',         HANDLE),
        ('HandleToThread',          HANDLE),
        ('NewProcess',              DBGKM_CREATE_PROCESS),
    ]

PDBGUI_CREATE_PROCESS = ctypes.POINTER(DBGUI_CREATE_PROCESS)

#
# User-Mode Debug State Change Structure
#

class DBGUI_WAIT_STATE_CHANGE(Structure):
    class StateInfo(Union):
        _fields_ = \
        [
            ('Exception',           DBGKM_EXCEPTION),
            ('CreateThread',        DBGUI_CREATE_THREAD),
            ('CreateProcessInfo',   DBGUI_CREATE_PROCESS),
            ('ExitThread',          DBGKM_EXIT_THREAD),
            ('ExitProcess',         DBGKM_EXIT_PROCESS),
            ('LoadDll',             DBGKM_LOAD_DLL),
            ('UnloadDll',           DBGKM_UNLOAD_DLL),
        ]

    _fields_ = \
    [
        ('NewState',                LONG),
        ('AppClientId',             CLIENT_ID),
        ('StateInfo',               StateInfo),
    ]

PDBGUI_WAIT_STATE_CHANGE = ctypes.POINTER(DBGUI_WAIT_STATE_CHANGE)


def DbgUiConnectToDbg():
    windll.ntdll.DbgUiConnectToDbg()

def DbgUiGetThreadDebugObject():
    return windll.ntdll.DbgUiGetThreadDebugObject()

def DbgUiIssueRemoteBreakin(Process):
    Status = windll.ntdll.DbgUiIssueRemoteBreakin(Process)
    if NT_FAILED(Status):
        raise Win32Error(Status)

def DbgUiContinue(ClientId, ContinueStatus):
    Status = windll.ntdll.DbgUiContinue(PCLIENT_ID(ClientId), ContinueStatus)
    if NT_FAILED(Status):
        raise Win32Error(Status)

def DbgUiDebugActiveProcess(Process):
    Status = windll.ntdll.DbgUiDebugActiveProcess(Process)
    if NT_FAILED(Status):
        raise Win32Error(Status)

def DbgUiStopDebugging(Process):
    Status = windll.ntdll.DbgUiStopDebugging(Process)
    if NT_FAILED(Status):
        raise Win32Error(Status)

def DbgUiWaitStateChange(Milliseconds = INFINITE):
    XTimeOut = FormatTimeOut(Milliseconds)
    StateChange = DBGUI_WAIT_STATE_CHANGE()

    Status = windll.ntdll.DbgUiWaitStateChange(PDBGUI_WAIT_STATE_CHANGE(StateChange), PLARGE_INTEGER(XTimeOut))
    if NT_FAILED(Status):
        raise Win32Error(Status)

    return StateChange

def DbgUiRemoteBreakin(Parameter):
    return windll.ntdll.DbgUiRemoteBreakin(PVOID(Parameter))

def main():
    pass

if __name__ == '__main__':
    TryInvoke(main)
