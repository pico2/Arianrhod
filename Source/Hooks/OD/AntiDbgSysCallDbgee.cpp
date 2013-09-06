#include "AntiDbgSysCallDbgee.h"

NTSTATUS IsObjectValid(HANDLE Object)
{
    OBJECT_HANDLE_FLAG_INFORMATION HandleFlag;

    return NtQueryObject(Object, ObjectHandleFlagInformation, &HandleFlag, sizeof(HandleFlag), NULL);
}

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
)
{
    NTSTATUS Status;

/*
    static ULONG Count;

    PrintConsoleW(
        L"%08X: %S\n"
        L"ProcessInformationClass   = %08d\n"
        L"ProcessInformation        = %08X\n"
        L"ProcessInformationLength  = %08X\n"
        L"ReturnLength              = %08X\n"
        L"\n",

        Count++,
        g_pSysCallFilters[ServiceIndex].Reserve,
        ProcessInformationClass,
        ProcessInformation,
        ProcessInformationLength,
        ReturnLength
    );
*/
    Status = IsObjectValid(ProcessHandle);
    if (!NT_SUCCESS(Status))
        goto _Exit;

    switch (ProcessInformationClass)
    {
        case ProcessDebugObjectHandle:
            Status = STATUS_PORT_NOT_SET;

        case ProcessDebugPort:
            if (ProcessInformation != NULL)
            {
                ZeroMemory(ProcessInformation, ProcessInformationLength);
            }
            if (ReturnLength != NULL)
            {
                *ReturnLength = 4;
            }
            break;
/*
        case ProcessDebugFlags:
            if (ProcessInformation != 0)
                *(PULONG)ProcessInformation = TRUE;
            if (ReturnLength != NULL)
                *ReturnLength = 4;
            break;
*/
/*
        case ProcessBasicInformation:
            if (ProcessHandle != NtCurrentProcess())
                goto _Exit;

            Status = CallSysCall(
                        NtQueryInformationProcess,
                        SysCallInfo,
                        ProcessHandle,
                        ProcessInformationClass,
                        ProcessInformation,
                        ProcessInformationLength,
                        ReturnLength
                     );
            if (NT_SUCCESS(Status))
                ((PPROCESS_BASIC_INFORMATION)ProcessInformation)->InheritedFromUniqueProcessId = g_ExplorerPID;

            break;
*/
        default:
            goto _Exit;
    }

    Action->Action = BlockSystemCall;

_Exit:

    return Status;
}

NTSTATUS
HOOKPORT_CALLTYPE
HookNtSetInformationThread(
    PSYSCALL_INFO               SysCallInfo,
    PSYSTEM_CALL_ACTION         Action,
    HANDLE                      ThreadHandle,
    THREAD_INFORMATION_CLASS    ThreadInformationClass,
    PVOID                       ThreadInformation,
    ULONG                       ThreadInformationLength
)
{
    NTSTATUS Status;

    switch (ThreadInformationClass)
    {
        case ThreadHideFromDebugger:
            Status = IsObjectValid(ThreadHandle);
            if (NT_SUCCESS(Status))
                break;

            return Status;

        default:
            return STATUS_SUCCESS;
    }

    Action->Action = BlockSystemCall;

    return Status;
}

NTSTATUS
HOOKPORT_CALLTYPE
HookNtClose(
    PSYSCALL_INFO       SysCallInfo,
    PSYSTEM_CALL_ACTION Action,
    HANDLE              Handle
)
{
    NTSTATUS Status;

    Status = IsObjectValid(Handle);
    if (!NT_SUCCESS(Status))
        Action->Action = BlockSystemCall;

    return Status;
}

NTSTATUS
HOOKPORT_CALLTYPE
HookNtYieldExecution(
    PSYSCALL_INFO       SysCallInfo,
    PSYSTEM_CALL_ACTION Action
)
{
    CallSysCall(NtYieldExecution, SysCallInfo);

    return STATUS_NO_YIELD_PERFORMED;
}

NTSTATUS
HOOKPORT_CALLTYPE
HookNtOpenProcess(
    PSYSCALL_INFO       SysCallInfo,
    PSYSTEM_CALL_ACTION Action,
    PHANDLE             ProcessHandle,
    ACCESS_MASK         DesiredAccess,
    POBJECT_ATTRIBUTES  ObjectAttributes,
    PCLIENT_ID          ClientId
)
{
    PrintConsoleW(L"%d\n", ClientId->UniqueProcess);
    return STATUS_SUCCESS;
}

/*
    \??\SICE
    \??\SIWVID
    \??\NTICE
*/
