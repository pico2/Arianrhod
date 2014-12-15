#define BYPASS_UAC_DEVICE_NAME      L"\\Device\\BypassUACDriver"
#define BYPASS_UAC_DEVICE_SYMBOLIC  L"\\DosDevices\\BypassUACDriver"
#define BYPASS_UAC_SERVICE_NAME     L"BypassUACDriver"
#define BYPASS_UAC_DRIVER_NAME      L"BypassUACDriver.sys"


#define FUNCTION_FROM_CTL_CODE(ctrlCode)     (((ULONG)(ctrlCode) & 0x00003FFC) >> 2)

#define BH_IOCTL_CODE(Function, Method)   ((ULONG)CTL_CODE(FILE_DEVICE_UNKNOWN, Function, Method, FILE_ANY_ACCESS) | (1 << 31))
#define BH_IOCTL_METHOD (METHOD_OUT_DIRECT)

#define IOCTL_HANDLER(_func) NTSTATUS _func(PAAKDI Info, PDEVICE_OBJECT DeviceObject, PIRP Irp,PULONG_PTR BytesWritten)
#define CALL_IOCTL_HANDLER(_func) Status = (_func)(Info, DeviceObject, Irp, &BytesWritten)
#define HANDLE_IOCTL(_ioctl, _func) case (_ioctl): CALL_IOCTL_HANDLER((_func)); break

#define IOCTL_OPEN_PROCESS_TOKEN        BH_IOCTL_CODE(BhOpenProcessToken,       BH_IOCTL_METHOD)
#define IOCTL_CREATE_TOKEN              BH_IOCTL_CODE(BhCreateToken,            BH_IOCTL_METHOD)
#define IOCTL_ADJUST_PRIVILEGE          BH_IOCTL_CODE(BhAdjustPrivilege,        BH_IOCTL_METHOD)

enum
{
    BhFunctionFirst         = 0x800,
        
    BhOpenProcessToken,
    BhCreateToken,
    BhAdjustPrivilege,

    BhFcunctionLast,
};

#pragma pack(push, 8)

typedef struct
{
    HANDLE64    Process;
    ACCESS_MASK Access;
    PVOID64     Token;

} BH_OPEN_PROCESS_TOKEN, *PBH_OPEN_PROCESS_TOKEN;

typedef struct
{
    PHANDLE                 TokenHandle;
    ACCESS_MASK             DesiredAccess;
    POBJECT_ATTRIBUTES      ObjectAttributes;
    TOKEN_TYPE              TokenType;
    PLUID                   AuthenticationId;
    PLARGE_INTEGER          ExpirationTime;
    PTOKEN_USER             User;
    PTOKEN_GROUPS           Groups;
    PTOKEN_PRIVILEGES       Privileges;
    PTOKEN_OWNER            Owner;
    PTOKEN_PRIMARY_GROUP    PrimaryGroup;
    PTOKEN_DEFAULT_DACL     DefaultDacl;
    PTOKEN_SOURCE           TokenSource;

} BH_CREATE_TOKEN, *PBH_CREATE_TOKEN;

typedef struct 
{
    HANDLE64 Process;

} BH_ADJUST_PRIVILEG, *PBH_ADJUST_PRIVILEG;

#pragma pack(pop)
