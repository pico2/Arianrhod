#ifndef _ANTIDBGSYSCALLDBGEE_H_b8eea012_7249_470d_acff_a3281e976272_
#define _ANTIDBGSYSCALLDBGEE_H_b8eea012_7249_470d_acff_a3281e976272_

#include "OD.h"

NTSTATUS
HOOKPORT_CALLTYPE
HookNtQueryInformationProcess(
    PSYSCALL_INFO               SysCallInfo,
    PSYSTEM_CALL_ACTION         Action,
    HANDLE                      ProcessHandle,
    PROCESS_INFORMATION_CLASS   ProcessInformationClass,
    PVOID                       ProcessInformation,
    ULONG                       ProcessInformationLength,
    PULONG                      ReturnLength
);

NTSTATUS
HOOKPORT_CALLTYPE
HookNtSetInformationThread(
    PSYSCALL_INFO               SysCallInfo,
    PSYSTEM_CALL_ACTION         Action,
    HANDLE                      ThreadHandle,
    THREAD_INFORMATION_CLASS    ThreadInformationClass,
    PVOID                       ThreadInformation,
    ULONG                       ThreadInformationLength
);

NTSTATUS
HOOKPORT_CALLTYPE
HookNtClose(
    PSYSCALL_INFO       SysCallInfo,
    PSYSTEM_CALL_ACTION Action,
    HANDLE              Handle
);

NTSTATUS
HOOKPORT_CALLTYPE
HookNtYieldExecution(
    PSYSCALL_INFO               SysCallInfo,
    PSYSTEM_CALL_ACTION         Action
);

NTSTATUS
HOOKPORT_CALLTYPE
HookNtOpenProcess(
    PSYSCALL_INFO       SysCallInfo,
    PSYSTEM_CALL_ACTION Action,
    PHANDLE             ProcessHandle,
    ACCESS_MASK         DesiredAccess,
    POBJECT_ATTRIBUTES  ObjectAttributes,
    PCLIENT_ID          ClientId
);

#endif // _ANTIDBGSYSCALLDBGEE_H_b8eea012_7249_470d_acff_a3281e976272_
