#ifndef _ANTIDBGSYSCALLDBGER_H_e8e597c8_1121_47c0_96fe_3f1d1f7f5239_
#define _ANTIDBGSYSCALLDBGER_H_e8e597c8_1121_47c0_96fe_3f1d1f7f5239_

#include "MyLibrary.h"
#include "HookPort.h"

#define CREATE_EXPLORER_CHILD_PROCESS_MAGIC   TAG4('CEPM')

NTSTATUS
HOOKPORT_CALLTYPE
OdCreateProcess(
    PSYSCALL_INFO       SysCallInfo,
    SYSTEM_CALL_ACTION *Action,
    PHANDLE             ProcessHandle,
    ACCESS_MASK         DesiredAccess,
    POBJECT_ATTRIBUTES  ObjectAttributes OPTIONAL,
    HANDLE              ParentProcess,
    BOOLEAN             InheritObjectTable,
    HANDLE              SectionHandle OPTIONAL,
    HANDLE              DebugPort OPTIONAL,
    HANDLE              ExceptionPort OPTIONAL
);

NTSTATUS
HOOKPORT_CALLTYPE
OdCreateProcessEx(
    PSYSCALL_INFO       SysCallInfo,
    SYSTEM_CALL_ACTION *Action,
    PHANDLE             ProcessHandle,
    ACCESS_MASK         DesiredAccess,
    POBJECT_ATTRIBUTES  ObjectAttributes OPTIONAL,
    HANDLE              ParentProcess,
    ULONG               Flags,
    HANDLE              SectionHandle OPTIONAL,
    HANDLE              DebugPort OPTIONAL,
    HANDLE              ExceptionPort OPTIONAL,
    ULONG               JobMemberLevel
);

NTSTATUS
HOOKPORT_CALLTYPE
OdCreateUserProcess(
    PSYSCALL_INFO       SysCallInfo,
    PSYSTEM_CALL_ACTION Action,
    PHANDLE             ProcessHandle,
    PHANDLE             ThreadHandle,
    ACCESS_MASK         ProcessDesiredAccess,
    ACCESS_MASK         ThreadDesiredAccess,
    POBJECT_ATTRIBUTES  ProcessObjectAttributes OPTIONAL,
    POBJECT_ATTRIBUTES  ThreadObjectAttributes OPTIONAL,
    ULONG               ProcessFlags,                   // PROCESS_CREATE_FLAGS_*
    ULONG               ThreadFlags,                    // THREAD_CREATE_FLAGS_*
    PVOID               ProcessParameters OPTIONAL,
    PPS_CREATE_INFO     CreateInfo,
    PPS_ATTRIBUTE_LIST  AttributeList OPTIONAL
);

#endif // _ANTIDBGSYSCALLDBGER_H_e8e597c8_1121_47c0_96fe_3f1d1f7f5239_
