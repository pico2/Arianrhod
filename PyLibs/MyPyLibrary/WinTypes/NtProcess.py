from .NtBase import *
from .NtObject import *

JobObjectExtendedLimitInformation = 9
JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE = 0x00002000

class JOBOBJECT_BASIC_LIMIT_INFORMATION(Structure):
    _fields_ = \
    [
        ('PerProcessUserTimeLimit', LARGE_INTEGER),
        ('PerJobUserTimeLimit',     LARGE_INTEGER),
        ('LimitFlags',              ULONG),
        ('MinimumWorkingSetSize',   ULONG_PTR),
        ('MaximumWorkingSetSize',   ULONG_PTR),
        ('ActiveProcessLimit',      ULONG),
        ('Affinity',                ULONG_PTR),
        ('PriorityClass',           ULONG),
        ('SchedulingClass',         ULONG),
    ]

PJOBOBJECT_BASIC_LIMIT_INFORMATION = ctypes.POINTER(JOBOBJECT_BASIC_LIMIT_INFORMATION)

class IO_COUNTERS(Structure):
    _fields_ = \
    [
        ('ReadOperationCount',      ULONG64),
        ('WriteOperationCount',     ULONG64),
        ('OtherOperationCount',     ULONG64),
        ('ReadTransferCount',       ULONG64),
        ('WriteTransferCount',      ULONG64),
        ('OtherTransferCount',      ULONG64),
    ]

PIO_COUNTERS = ctypes.POINTER(IO_COUNTERS)

class JOBOBJECT_EXTENDED_LIMIT_INFORMATION(Structure):
    _fields_ = \
    [
        ('BasicLimitInformation',   JOBOBJECT_BASIC_LIMIT_INFORMATION),
        ('IoInfo',                  IO_COUNTERS),
        ('ProcessMemoryLimit',      ULONG_PTR),
        ('JobMemoryLimit',          ULONG_PTR),
        ('PeakProcessMemoryUsed',   ULONG_PTR),
        ('PeakJobMemoryUsed',       ULONG_PTR),
    ]

PJOBOBJECT_EXTENDED_LIMIT_INFORMATION = ctypes.POINTER(JOBOBJECT_EXTENDED_LIMIT_INFORMATION)


#
# Process dwCreationFlag values
#

DEBUG_PROCESS                       = 0x00000001
DEBUG_ONLY_THIS_PROCESS             = 0x00000002
CREATE_SUSPENDED                    = 0x00000004
DETACHED_PROCESS                    = 0x00000008

CREATE_NEW_CONSOLE                  = 0x00000010
NORMAL_PRIORITY_CLASS               = 0x00000020
IDLE_PRIORITY_CLASS                 = 0x00000040
HIGH_PRIORITY_CLASS                 = 0x00000080

REALTIME_PRIORITY_CLASS             = 0x00000100
CREATE_NEW_PROCESS_GROUP            = 0x00000200
CREATE_UNICODE_ENVIRONMENT          = 0x00000400
CREATE_SEPARATE_WOW_VDM             = 0x00000800

CREATE_SHARED_WOW_VDM               = 0x00001000
CREATE_FORCEDOS                     = 0x00002000
BELOW_NORMAL_PRIORITY_CLASS         = 0x00004000
ABOVE_NORMAL_PRIORITY_CLASS         = 0x00008000

INHERIT_PARENT_AFFINITY             = 0x00010000
INHERIT_CALLER_PRIORITY             = 0x00020000    # Deprecated
CREATE_PROTECTED_PROCESS            = 0x00040000
EXTENDED_STARTUPINFO_PRESENT        = 0x00080000

PROCESS_MODE_BACKGROUND_BEGIN       = 0x00100000
PROCESS_MODE_BACKGROUND_END         = 0x00200000

CREATE_BREAKAWAY_FROM_JOB           = 0x01000000
CREATE_PRESERVE_CODE_AUTHZ_LEVEL    = 0x02000000
CREATE_DEFAULT_ERROR_MODE           = 0x04000000
CREATE_NO_WINDOW                    = 0x08000000

PROFILE_USER                        = 0x10000000
PROFILE_KERNEL                      = 0x20000000
PROFILE_SERVER                      = 0x40000000
CREATE_IGNORE_SYSTEM_DEFAULT        = 0x80000000


class STARTUPINFOW(Structure):
    _fields_ = \
    [
        ('cb',                  ULONG),
        ('lpReserved',          PWSTR),
        ('lpDesktop',           PWSTR),
        ('lpTitle',             PWSTR),
        ('dwX',                 ULONG),
        ('dwY',                 ULONG),
        ('dwXSize',             ULONG),
        ('dwYSize',             ULONG),
        ('dwXCountChars',       ULONG),
        ('dwYCountChars',       ULONG),
        ('dwFillAttribute',     ULONG),
        ('dwFlags',             ULONG),
        ('wShowWindow',         WORD),
        ('cbReserved2',         WORD),
        ('lpReserved2',         PBYTE),
        ('hStdInput',           HANDLE),
        ('hStdOutput',          HANDLE),
        ('hStdError',           HANDLE),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cb = len(self)

PSTARTUPINFOW = ctypes.POINTER(STARTUPINFOW)


class PROCESS_INFORMATION(Structure):
    _fields_ = \
    [
        ('hProcess',            HANDLE),
        ('hThread',             HANDLE),
        ('dwProcessId',         ULONG),
        ('dwThreadId',          ULONG),
    ]

PPROCESS_INFORMATION = ctypes.POINTER(PROCESS_INFORMATION)


class SECURITY_ATTRIBUTES(Structure):
    _fields_ = \
    [
        ('nLength',                 ULONG),
        ('lpSecurityDescriptor',    PVOID),
        ('bInheritHandle',          BOOL),
    ]

PSECURITY_ATTRIBUTES = ctypes.POINTER(SECURITY_ATTRIBUTES)


SIZE_OF_80387_REGISTERS                     = 80

CONTEXT_i386                                =  0x00010000    # this assumes that i386 and
CONTEXT_i486                                =  0x00010000    # i486 have identical context records

CONTEXT_CONTROL                             = (CONTEXT_i386 | 0x00000001) # SS:SP, CS:IP, FLAGS, BP
CONTEXT_INTEGER                             = (CONTEXT_i386 | 0x00000002) # AX, BX, CX, DX, SI, DI
CONTEXT_SEGMENTS                            = (CONTEXT_i386 | 0x00000004) # DS, ES, FS, GS
CONTEXT_FLOATING_POINT                      = (CONTEXT_i386 | 0x00000008) # 387 state
CONTEXT_DEBUG_REGISTERS                     = (CONTEXT_i386 | 0x00000010) # DB 0-3,6,7
CONTEXT_EXTENDED_REGISTERS                  = (CONTEXT_i386 | 0x00000020) # cpu specific extensions
CONTEXT_FULL                                = (CONTEXT_CONTROL | CONTEXT_INTEGER | CONTEXT_SEGMENTS)
CONTEXT_ALL                                 = (CONTEXT_CONTROL | CONTEXT_INTEGER | CONTEXT_SEGMENTS | CONTEXT_FLOATING_POINT | CONTEXT_DEBUG_REGISTERS | CONTEXT_EXTENDED_REGISTERS)


MAXIMUM_SUPPORTED_EXTENSION     = 512

class FLOATING_SAVE_AREA(Structure):
    _fields_ = \
    [
        ('ControlWord',         ULONG),
        ('StatusWord',          ULONG),
        ('TagWord',             ULONG),
        ('ErrorOffset',         ULONG),
        ('ErrorSelector',       ULONG),
        ('DataOffset',          ULONG),
        ('DataSelector',        ULONG),
        ('RegisterArea',        UCHAR * SIZE_OF_80387_REGISTERS),
        ('Cr0NpxState',         ULONG),
    ]

PFLOATING_SAVE_AREA = ctypes.POINTER(FLOATING_SAVE_AREA)

class CONTEXT32(Structure):
    _fields_ = \
    [

        #
        # The flags values within this flag control the contents of
        # a CONTEXT record.
        #
        # If the context record is used as an input parameter, then
        # for each portion of the context record controlled by a flag
        # whose value is set, it is assumed that that portion of the
        # context record contains valid context. If the context record
        # is being used to modify a threads context, then only that
        # portion of the threads context will be modified.
        #
        # If the context record is used as an IN OUT parameter to capture
        # the context of a thread, then only those portions of the thread's
        # context corresponding to set flags will be returned.
        #
        # The context record is never used as an OUT only parameter.
        #

        ('ContextFlags',                 ULONG),

        #
        # This section is specified/returned if CONTEXT_DEBUG_REGISTERS is
        # set in ContextFlags.  Note that CONTEXT_DEBUG_REGISTERS is NOT
        # included in CONTEXT_FULL.
        #

        ('Dr0',                         ULONG),
        ('Dr1',                         ULONG),
        ('Dr2',                         ULONG),
        ('Dr3',                         ULONG),
        ('Dr6',                         ULONG),
        ('Dr7',                         ULONG),

        #
        # This section is specified/returned if the
        # ContextFlags word contains the flag CONTEXT_FLOATING_POINT.
        #

        ('FloatSave',                   FLOATING_SAVE_AREA),

        #
        # This section is specified/returned if the
        # ContextFlags word contains the flag CONTEXT_SEGMENTS.
        #

        ('SegGs',                       ULONG),
        ('SegFs',                       ULONG),
        ('SegEs',                       ULONG),
        ('SegDs',                       ULONG),

        #
        # This section is specified/returned if the
        # ContextFlags word contains the flag CONTEXT_INTEGER.
        #

        ('Edi',                         ULONG),
        ('Esi',                         ULONG),
        ('Ebx',                         ULONG),
        ('Edx',                         ULONG),
        ('Ecx',                         ULONG),
        ('Eax',                         ULONG),

        #
        # This section is specified/returned if the
        # ContextFlags word contains the flag CONTEXT_CONTROL.
        #

        ('Ebp',                         ULONG),
        ('Eip',                         ULONG),
        ('SegCs',                       ULONG),             # MUST BE SANITIZED
        ('EFlags',                      ULONG),             # MUST BE SANITIZED
        ('Esp',                         ULONG),
        ('SegSs',                       ULONG),

        #
        # This section is specified/returned if the ContextFlags word
        # contains the flag CONTEXT_EXTENDED_REGISTERS.
        # The format and contexts are processor specific
        #

        ('ExtendedRegisters',           UCHAR * MAXIMUM_SUPPORTED_EXTENSION),
    ]

PCONTEXT32 = ctypes.POINTER(CONTEXT32)


#
# Define 128-bit 16-byte aligned xmm register type.
#

class M128A(Structure):
    _pack_ = 16
    _fields_ = \
    [
        ('Low',                         ULONGLONG),
        ('High',                        LONGLONG),
    ]

PM128A = ctypes.POINTER(M128A)

#
# Format of data for 32-bit fxsave/fxrstor instructions.
#

class XMM_SAVE_AREA32(Structure):
    _fields_ = \
    [
        ('ControlWord',                 USHORT),
        ('StatusWord',                  USHORT),
        ('TagWord',                     UCHAR),
        ('Reserved1',                   UCHAR),
        ('ErrorOpcode',                 USHORT),
        ('ErrorOffset',                 ULONG),
        ('ErrorSelector',               USHORT),
        ('Reserved2',                   USHORT),
        ('DataOffset',                  ULONG),
        ('DataSelector',                USHORT),
        ('Reserved3',                   USHORT),
        ('MxCsr',                       ULONG),
        ('MxCsr_Mask',                  ULONG),
        ('FloatRegisters',              M128A * 8),
        ('XmmRegisters',                M128A * 16),
        ('Reserved4',                   UCHAR * 96),
    ]

PXMM_SAVE_AREA32 = ctypes.POINTER(XMM_SAVE_AREA32)


class CONTEXT64(Structure):
    class FLOATING_POINT_STATE(Union):
        class DUMMY(Structure):
            _fields_ = \
            [
                ('Header',          M128A * 2),
                ('Legacy',          M128A * 8),
                ('Xmm0',            M128A),
                ('Xmm1',            M128A),
                ('Xmm2',            M128A),
                ('Xmm3',            M128A),
                ('Xmm4',            M128A),
                ('Xmm5',            M128A),
                ('Xmm6',            M128A),
                ('Xmm7',            M128A),
                ('Xmm8',            M128A),
                ('Xmm9',            M128A),
                ('Xmm10',           M128A),
                ('Xmm11',           M128A),
                ('Xmm12',           M128A),
                ('Xmm13',           M128A),
                ('Xmm14',           M128A),
                ('Xmm15',           M128A),
            ]

        _anonymous_ = ('DUMMY', )
        _fields_ = \
        [
            ('FltSave',             XMM_SAVE_AREA32),
            ('DUMMY',               DUMMY),
        ]


    _anonymous_ = ('FLOATING_POINT_STATE', )
    _fields_ = \
    [
        #
        # Register parameter home addresses.
        #
        # N.B. These fields are for convenience - they could be used to extend the
        #      context record in the future.
        #

        ('P1Home',                      ULONG64),
        ('P2Home',                      ULONG64),
        ('P3Home',                      ULONG64),
        ('P4Home',                      ULONG64),
        ('P5Home',                      ULONG64),
        ('P6Home',                      ULONG64),

        #
        # Control flags.
        #

        ('ContextFlags',                ULONG),
        ('MxCsr',                       ULONG),

        #
        # Segment Registers and processor flags.
        #

        ('SegCs',                       USHORT),
        ('SegDs',                       USHORT),
        ('SegEs',                       USHORT),
        ('SegFs',                       USHORT),
        ('SegGs',                       USHORT),
        ('SegSs',                       USHORT),
        ('EFlags',                      ULONG),

        #
        # Debug registers
        #

        ('Dr0',                         ULONG64),
        ('Dr1',                         ULONG64),
        ('Dr2',                         ULONG64),
        ('Dr3',                         ULONG64),
        ('Dr6',                         ULONG64),
        ('Dr7',                         ULONG64),

        #
        # Integer registers.
        #

        ('Rax',                         ULONG64),
        ('Rcx',                         ULONG64),
        ('Rdx',                         ULONG64),
        ('Rbx',                         ULONG64),
        ('Rsp',                         ULONG64),
        ('Rbp',                         ULONG64),
        ('Rsi',                         ULONG64),
        ('Rdi',                         ULONG64),
        ('R8',                          ULONG64),
        ('R9',                          ULONG64),
        ('R10',                         ULONG64),
        ('R11',                         ULONG64),
        ('R12',                         ULONG64),
        ('R13',                         ULONG64),
        ('R14',                         ULONG64),
        ('R15',                         ULONG64),

        #
        # Program counter.
        #

        ('Rip',                         ULONG64),

        #
        # Floating point state.
        #
        ('FLOATING_POINT_STATE',        FLOATING_POINT_STATE),

        #
        # Vector registers.
        #

        ('VectorRegister',              M128A * 26),
        ('VectorControl',               ULONG64),

        #
        # Special debug control registers.
        #

        ('DebugControl',                ULONG64),
        ('LastBranchToRip',             ULONG64),
        ('LastBranchFromRip',           ULONG64),
        ('LastExceptionToRip',          ULONG64),
        ('LastExceptionFromRip',        ULONG64),
    ]

PCONTEXT64 = ctypes.POINTER(CONTEXT64)


if ctypes.sizeof(PVOID) == ctypes.sizeof(ULONG):
    CONTEXT     = CONTEXT32
    PCONTEXT    = PCONTEXT32

elif ctypes.sizeof(PVOID) == ctypes.sizeof(ULONG64):
    CONTEXT     = CONTEXT64
    PCONTEXT    = PCONTEXT64

def NtOpenThread(ClientId, ObjectAttributes = None, DesiredAccess = THREAD_ALL_ACCESS):
    ThreadHandle = HANDLE()

    if isinstance(ClientId, (int, HANDLE)):
        ClientId = CLIEND_ID(NtCurrentProcess, ClientId)

    ObjectAttributes = ObjectAttributes or OBJECT_ATTRIBUTES()

    Status = windll.ntdll.NtOpenThread(
                PHANDLE(ThreadHandle),
                ULONG(DesiredAccess),
                POBJECT_ATTRIBUTES(ObjectAttributes),
                PCLIENT_ID(ClientId)
            )

    if NT_FAILED(Status):
        raise Win32Error(Status)

    return ThreadHandle

def NtTerminateProcess(Process, ExitStatus = 0):
    Status = windll.ntdll.NtTerminateProcess(Process, ExitStatus)
    return Status

    if NT_FAILED(Status):
        raise Win32Error(Status)

def CreateProcessInternalW(
    Token,
    ApplicationName,
    CommandLine,
    ProcessAttributes,
    ThreadAttributes,
    InheritHandles,
    CreationFlags,
    Environment,
    CurrentDirectory,
    StartupInfo,
    ProcessInformation,
    NewToken
):

    Result = windll.kernel32.CreateProcessInternalW(
                HANDLE(Token),
                PWSTR(ApplicationName),
                PWSTR(CommandLine),
                PSECURITY_ATTRIBUTES(ProcessAttributes) if ProcessAttributes is not None else PVOID(),
                PSECURITY_ATTRIBUTES(ThreadAttributes) if ThreadAttributes is not None else PVOID(),
                BOOL(InheritHandles),
                ULONG(CreationFlags),
                PWSTR(Environment),
                PWSTR(CurrentDirectory),
                PSTARTUPINFOW(StartupInfo),
                PPROCESS_INFORMATION(ProcessInformation),
                PHANDLE(NewToken) if NewToken is not None else PVOID()
            )

    return bool(Result)

def CreateProcess(
    ApplicationName,
    CommandLine         = None,
    CurrentDirectory    = None,
    CreationFlags       = 0,
    StartupInfo         = None,
    ProcessInformation  = None,
    ProcessAttributes   = None,
    ThreadAttributes    = None,
    Environment         = None,
    Token               = None,
    InheritHandles      = False
):

    DefaultStartupInfo          = None
    DefaultProcessInformation   = None

    if StartupInfo is None:
        DefaultStartupInfo = STARTUPINFOW()
        StartupInfo = DefaultStartupInfo

    if ProcessInformation is None:
        DefaultProcessInformation = PROCESS_INFORMATION()
        ProcessInformation = DefaultProcessInformation

    Result = CreateProcessInternalW(
                    Token,
                    ApplicationName,
                    CommandLine,
                    ProcessAttributes,
                    ThreadAttributes,
                    InheritHandles,
                    CreationFlags,
                    Environment,
                    CurrentDirectory,
                    StartupInfo,
                    ProcessInformation,
                    None
             )

    if Result is False:
        raise Win32Error(NTSTATUS_FROM_WIN32(RtlGetLastWin32Error()))

    if ProcessInformation is DefaultProcessInformation:
        NtClose(DefaultProcessInformation.hProcess)
        NtClose(DefaultProcessInformation.hThread)

def main():
    pass

if __name__ == '__main__':
    TryInvoke(main)
