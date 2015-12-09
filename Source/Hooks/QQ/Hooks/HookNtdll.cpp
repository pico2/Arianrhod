#include "Hooks.h"

using namespace Mp;

API_POINTER(NtQueryInformationProcess)  StubNtQueryInformationProcess;
API_POINTER(::CreateThread)             HummerCreateThread;
API_POINTER(NtOpenFile)                 StubNtOpenFile;
API_POINTER(NtCreateFile)               StubNtCreateFile;
API_POINTER(NtQueryAttributesFile)      StubNtQueryAttributesFile;
API_POINTER(RegOpenKeyExW)              StubRegOpenKeyExW;
API_POINTER(RegQueryValueExW)           StubRegQueryValueExW;

WCHAR GlobalRegistryDb[0x20];
WCHAR GlobalHistoryDb[countof(GlobalRegistryDb)];
WCHAR GlobalPerfreDb[countof(GlobalRegistryDb)];

BOOL InitializeUin()
{
    ULONG_PTR Length;
    WCHAR ch;
    PWSTR CommandLine, QQUIN;

    CommandLine = CurrentPeb()->ProcessParameters->CommandLine.Buffer;

    QQUIN = wcsstr(CommandLine, L"QQUIN:");
    if (QQUIN == nullptr)
        return FALSE;

    QQUIN += CONST_STRLEN(L"QQUIN:");

    CommandLine = QQUIN;
    while (*CommandLine != ' ' && *CommandLine != '\t' && *CommandLine != 0)
        ++CommandLine;

    Length = PtrOffset(CommandLine, QQUIN);
    if (Length >= sizeof(GlobalRegistryDb) - sizeof(L".db"))
        return FALSE;

    Length /= sizeof(WCHAR);

    swprintf(GlobalRegistryDb, L"Registry_%.*s.db", Length, QQUIN);
    swprintf(GlobalHistoryDb, L"History_%.*s.db", Length, QQUIN);
    swprintf(GlobalPerfreDb, L"Perfre_%.*s.db", Length, QQUIN);

    return TRUE;
}

NTSTATUS GetRedirectFile(PUNICODE_STRING Redirected, PUNICODE_STRING Original)
{
    ULONG_PTR       Length;
    PWSTR           Buffer;
    UNICODE_STRING  FileName;

    typedef struct
    {
        UNICODE_STRING  SubPath;
        ULONG_PTR       SuffixLength;
        PCWSTR          NewSubPath;

    } REDIRECT_ENTRY, *PDB_REDIRECT;

    PDB_REDIRECT Entry;

    static REDIRECT_ENTRY RedirectEntries[] =
    {
        { RTL_CONSTANT_STRING(L"\\All Users\\QQ\\History.db"),  CONST_STRLEN(L"History.db")  * sizeof(WCHAR), GlobalHistoryDb },
        { RTL_CONSTANT_STRING(L"\\All Users\\QQ\\Registry.db"), CONST_STRLEN(L"Registry.db") * sizeof(WCHAR), GlobalRegistryDb },
        { RTL_CONSTANT_STRING(L"\\All Users\\QQ\\Perfre.db"),   CONST_STRLEN(L"Perfre.db")   * sizeof(WCHAR), GlobalPerfreDb },
        //{ RTL_CONSTANT_STRING(L"QQProtect.exe"),                CONST_STRLEN(L"QQProtect.exe") * sizeof(WCHAR), NULL },
    };

    RtlInitEmptyString(Redirected);

    LOOP_ONCE
    {
        if (Original == nullptr)
            continue;

        FOR_EACH_ARRAY(Entry, RedirectEntries)
        {
            if (Original->Length <= Entry->SubPath.Length)
                continue;

            FileName = *Original;
            FileName.Buffer = PtrSub(PtrAdd(FileName.Buffer, FileName.Length), Entry->SubPath.Length);
            FileName.Length = Entry->SubPath.Length;

            if (!RtlEqualUnicodeString(&FileName, &Entry->SubPath, TRUE))
                continue;
/*
            if (Entry->NewSubPath == NULL)
            {
                ExceptionBox(L"qqprotect");
                ++Entry;
            }
*/
            break;
        }

        if (Entry == &RedirectEntries[countof(RedirectEntries)])
            break;

        Length = Original->Length + Entry->SubPath.Length + Entry->SuffixLength + sizeof(Entry->NewSubPath);
        Buffer = (PWSTR)AllocStack(Length);

        FileName.MaximumLength = Length;
        FileName.Buffer = Buffer;

        Length = StrLengthW(Entry->NewSubPath) * sizeof(WCHAR);

        RtlCopyUnicodeString(&FileName, Original);
        CopyMemory(PtrSub(PtrAdd(FileName.Buffer, FileName.Length), Entry->SuffixLength), Entry->NewSubPath, Length + sizeof(WCHAR));
        FileName.Length = FileName.Length - Entry->SuffixLength + Length;

        RtlDuplicateUnicodeString(RTL_DUPSTR_ADD_NULL, &FileName, Redirected);

        return STATUS_SUCCESS;
    }

    return STATUS_NOT_FOUND;
}

NTSTATUS
NTAPI
QqNtCreateFile(
    PHANDLE             FileHandle,
    ACCESS_MASK         DesiredAccess,
    POBJECT_ATTRIBUTES  ObjectAttributes,
    PIO_STATUS_BLOCK    IoStatusBlock,
    PLARGE_INTEGER      AllocationSize,
    ULONG               FileAttributes,
    ULONG               ShareAccess,
    ULONG               CreateDisposition,
    ULONG               CreateOptions,
    PVOID               EaBuffer,
    ULONG               EaLength
)
{
    NTSTATUS            Status;
    OBJECT_ATTRIBUTES   LocalObjectAttributes;
    UNICODE_STRING      Redirected;

    RtlInitEmptyString(&Redirected);

    LOOP_ONCE
    {
        if (ObjectAttributes == nullptr)
            break;

        Status = GetRedirectFile(&Redirected, ObjectAttributes->ObjectName);
        FAIL_BREAK(Status);

        LocalObjectAttributes = *ObjectAttributes;
        LocalObjectAttributes.ObjectName = &Redirected;
        ObjectAttributes = &LocalObjectAttributes;
    }

    Status = StubNtCreateFile(FileHandle, DesiredAccess, ObjectAttributes, IoStatusBlock, AllocationSize, FileAttributes, ShareAccess, CreateDisposition, CreateOptions, EaBuffer, EaLength);

    RtlFreeUnicodeString(&Redirected);

    return Status;
}

NTSTATUS
NTAPI
QqNtOpenFile(
    PHANDLE             FileHandle,
    ACCESS_MASK         DesiredAccess,
    POBJECT_ATTRIBUTES  ObjectAttributes,
    PIO_STATUS_BLOCK    IoStatusBlock,
    ULONG               ShareAccess,
    ULONG               OpenOptions
)
{
    NTSTATUS            Status;
    OBJECT_ATTRIBUTES   LocalObjectAttributes;
    UNICODE_STRING      Redirected;

    RtlInitEmptyString(&Redirected);

    LOOP_ONCE
    {
        if (ObjectAttributes == nullptr)
            break;

        Status = GetRedirectFile(&Redirected, ObjectAttributes->ObjectName);
        FAIL_BREAK(Status);

        LocalObjectAttributes = *ObjectAttributes;
        LocalObjectAttributes.ObjectName = &Redirected;
        ObjectAttributes = &LocalObjectAttributes;
    }

    Status = StubNtOpenFile(FileHandle, DesiredAccess, ObjectAttributes, IoStatusBlock, ShareAccess, OpenOptions);

    RtlFreeUnicodeString(&Redirected);

    return Status;
}

NTSTATUS
NTAPI
QqNtQueryAttributesFile(
    POBJECT_ATTRIBUTES      ObjectAttributes,
    PFILE_BASIC_INFORMATION FileInformation
)
{
    NTSTATUS            Status;
    OBJECT_ATTRIBUTES   LocalObjectAttributes;
    UNICODE_STRING      Redirected;

    RtlInitEmptyString(&Redirected);

    LOOP_ONCE
    {
        if (ObjectAttributes == nullptr)
            break;

        Status = GetRedirectFile(&Redirected, ObjectAttributes->ObjectName);
        FAIL_BREAK(Status);

        LocalObjectAttributes = *ObjectAttributes;
        LocalObjectAttributes.ObjectName = &Redirected;
        ObjectAttributes = &LocalObjectAttributes;
    }

    Status = StubNtQueryAttributesFile(ObjectAttributes, FileInformation);

    RtlFreeUnicodeString(&Redirected);

    return Status;
}

LSTATUS
NTAPI
QqRegOpenKeyExW(
    HKEY    hKey,
    PCWSTR  SubKey,
    DWORD   Options,
    REGSAM  Desired,
    PHKEY   Result
)
{
    LSTATUS ret;

    ret = StubRegOpenKeyExW(hKey, SubKey, Options, Desired, Result);
    if (ret == NO_ERROR)
        return ret;

    if (hKey == HKEY_LOCAL_MACHINE && StrICompareW(SubKey, L"SYSTEM\\CurrentControlSet\\Services\\QPCore") == 0)
    {
        *Result = nullptr;
        ret = NO_ERROR;
    }

    return ret;
}

LSTATUS
NTAPI
QqRegQueryValueExW(
    HKEY    hKey,
    PCWSTR  ValueName,
    PULONG  Reserved,
    PULONG  Type,
    PBYTE   Data,
    PULONG  DataSize
)
{
    if (hKey != nullptr)
        return StubRegQueryValueExW(hKey, ValueName, Reserved, Type, Data, DataSize);

    if (StrICompareW(ValueName, L"QQProtectDir") == 0)
    {
        String qqpath;
        ULONG_PTR Length;

        Rtl::GetModuleDirectory(qqpath, nullptr);

        qqpath += L"..\\";

        Length = (ULONG_PTR)(qqpath.GetSize() + 2);
        Length = ML_MIN(Length, *DataSize);
        CopyMemory(Data, (PWSTR)qqpath, Length);
        *DataSize = Length;

        if (Type != nullptr)
            *Type = REG_SZ;

        return NO_ERROR;
    }

    return ERROR_INVALID_HANDLE;
}

NTSTATUS HookNtdll(PVOID BaseAddress)
{
    BOOL QQUINSpecified = InitializeUin();

    PATCH_MEMORY_DATA Function_ntdll[] =
    {
        FunctionJumpVa(QQUINSpecified ? NtOpenFile            : IMAGE_INVALID_VA, QqNtOpenFile,               &StubNtOpenFile),
        FunctionJumpVa(QQUINSpecified ? NtCreateFile          : IMAGE_INVALID_VA, QqNtCreateFile,             &StubNtCreateFile),
        FunctionJumpVa(QQUINSpecified ? NtQueryAttributesFile : IMAGE_INVALID_VA, QqNtQueryAttributesFile,    &StubNtQueryAttributesFile),
        //FunctionJumpVa(NtQueryInformationProcess,                                 QqNtQueryInformationProcess,&StubNtQueryInformationProcess),
        //FunctionJumpVa(NtFreeVirtualMemory,                                       QqNtFreeVirtualMemory,      &StubNtFreeVirtualMemory),

        //FunctionJumpVa(RegOpenKeyExW,       QqRegOpenKeyExW,    &StubRegOpenKeyExW),
        //FunctionJumpVa(RegQueryValueExW,    QqRegQueryValueExW, &StubRegQueryValueExW),
    };

    return PatchMemory(Function_ntdll, countof(Function_ntdll), BaseAddress);
}