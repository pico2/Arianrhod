#include "AntiDbgSysCallDbger.h"

HANDLE OpenExplorer()
{
    BOOLEAN     Enable;
    ULONG_PTR   ExplorerPid;
    HANDLE      ExplorerProcess;

    RtlAdjustPrivilege(SE_DEBUG_PRIVILEGE, TRUE, FALSE, &Enable);
    GetWindowThreadProcessId(GetShellWindow(), &ExplorerPid);
    ExplorerProcess = ProcessIdToHandle(ExplorerPid);
    RtlAdjustPrivilege(SE_DEBUG_PRIVILEGE, FALSE, FALSE, &Enable);

    return ExplorerProcess;
}

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
)
{
    NTSTATUS    Status;
    HANDLE      ExplorerProcess;

    if (Nt_FindThreadFrameByContext(CREATE_EXPLORER_CHILD_PROCESS_MAGIC) == NULL)
        return 0;

    ExplorerProcess = OpenExplorer();
    if (ExplorerProcess == NULL)
        return 0;

    Action->Action = BlockSystemCall;

    {
        HookPortBypassFilter hpif(SysCallInfo->ServiceIndex);

        Status = CallSysCall(
                    NtCreateProcess,
                    SysCallInfo,
                    ProcessHandle,
                    DesiredAccess,
                    ObjectAttributes,
                    ExplorerProcess,
                    InheritObjectTable,
                    SectionHandle,
                    DebugPort,
                    ExceptionPort
                );
    }

    NtClose(ExplorerProcess);

    return Status;
}

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
)
{
    NTSTATUS    Status;
    HANDLE      ExplorerProcess;

    if (Nt_FindThreadFrameByContext(CREATE_EXPLORER_CHILD_PROCESS_MAGIC) == NULL)
        return 0;

    ExplorerProcess = OpenExplorer();
    if (ExplorerProcess == NULL)
        return 0;

    Action->Action = BlockSystemCall;

    {
        HookPortBypassFilter hpif(SysCallInfo->ServiceIndex);

        Status = CallSysCall(
                    NtCreateProcessEx,
                    SysCallInfo,
                    ProcessHandle,
                    DesiredAccess,
                    ObjectAttributes,
                    ExplorerProcess,
                    Flags,
                    SectionHandle,
                    DebugPort,
                    ExceptionPort,
                    JobMemberLevel
                );
    }

    NtClose(ExplorerProcess);

    return Status;
}

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
)
{
    NTSTATUS            Status;
    HANDLE              ExplorerProcess;
    ULONG_PTR           AttributesSize;
    PPS_ATTRIBUTE_LIST  NewAttributesList;
    PPS_ATTRIBUTE       ParentProcessAttribute;

    if (Nt_FindThreadFrameByContext(CREATE_EXPLORER_CHILD_PROCESS_MAGIC) == NULL)
        return 0;

    ExplorerProcess = OpenExplorer();
    if (ExplorerProcess == NULL)
        return 0;

    Action->Action = BlockSystemCall;

    ParentProcessAttribute = NULL;
    if (AttributeList != NULL)
    {
        PPS_ATTRIBUTE Attribute = AttributeList->Attributes;
        for (ULONG_PTR Count = AttributeList->TotalLength / sizeof(*Attribute); Count; --Count)
        {
            if (Attribute->AttributeNumber == PsAttributeStdHandleInfo ||
                Attribute->AttributeNumber == PsAttributeParentProcess)
            {
                ParentProcessAttribute = Attribute;
                break;
            }

            ++Attribute;
        }
    }

    if (ParentProcessAttribute != NULL)
    {
        AttributesSize = AttributeList->TotalLength;
    }
    else
    {
        AttributesSize = sizeof(*ParentProcessAttribute) + (AttributeList == NULL ? sizeof(AttributeList->TotalLength) : AttributeList->TotalLength);
    }

    NewAttributesList = (PPS_ATTRIBUTE_LIST)AllocStack(AttributesSize);
    NewAttributesList->TotalLength = AttributesSize;
    if (AttributeList != NULL)
    {
        AttributesSize = AttributeList->TotalLength - sizeof(AttributeList->TotalLength);
        CopyMemory(NewAttributesList->Attributes, AttributeList->Attributes, AttributesSize);

        if (ParentProcessAttribute == NULL)
        {
            ParentProcessAttribute = NewAttributesList->Attributes + AttributesSize / sizeof(AttributeList->Attributes);
        }
        else
        {
            ParentProcessAttribute = PtrAdd(ParentProcessAttribute, PtrOffset(NewAttributesList, AttributeList));
        }
    }
    else
    {
        ParentProcessAttribute = NewAttributesList->Attributes;
    }

    ParentProcessAttribute->Size            = sizeof(ParentProcessAttribute->Value);
    ParentProcessAttribute->Value           = (ULONG_PTR)ExplorerProcess;
    ParentProcessAttribute->AttributeNumber = (USHORT)PsAttributeParentProcess;
    ParentProcessAttribute->AttributeFlags  = PS_ATTRIBUTE_FLAG_INPUT | PS_ATTRIBUTE_FLAG_UNKNOWN;
    ParentProcessAttribute->ReturnLength    = NULL;

    {
        HookPortBypassFilter hpif(SysCallInfo->ServiceIndex);

        Status = CallSysCall(
                    NtCreateUserProcess,
                    SysCallInfo,
                    ProcessHandle,
                    ThreadHandle,
                    ProcessDesiredAccess,
                    ThreadDesiredAccess,
                    ProcessObjectAttributes,
                    ThreadObjectAttributes,
                    ProcessFlags,
                    ThreadFlags,
                    ProcessParameters,
                    CreateInfo,
                    NewAttributesList
                );
    }

    NtClose(ExplorerProcess);

    return Status;
}
