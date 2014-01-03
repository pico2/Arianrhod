#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")
#pragma comment(linker, "/EXPORT:Netbios=_QqNetbios@4")

#include "QQ2011.h"
#include "MyLibrary.cpp"
#include <Psapi.h>
#include "QQMethod.h"

WCHAR GlobalRegistryDb[0x20];
WCHAR GlobalHistoryDb[countof(GlobalRegistryDb)];

PVOID AppUtilBase;

API_POINTER(free)                       msvcrX0_free;
API_POINTER(SetWindowPos)               StubSetWindowPos;
API_POINTER(ShowWindow)                 StubShowWindow;
API_POINTER(PostMessageW)               StubPostMessageW;
API_POINTER(GetModuleFileNameExW)       StubGetModuleFileNameExW;
API_POINTER(NtQueryInformationProcess)  StubNtQueryInformationProcess;
API_POINTER(::CreateThread)             HummerCreateThread;
API_POINTER(NtOpenFile)                 StubNtOpenFile;
API_POINTER(NtCreateFile)               StubNtCreateFile;
API_POINTER(NtQueryAttributesFile)      StubNtQueryAttributesFile;
API_POINTER(Netbios)                    StubNetbios;


HRESULT
(NTAPI
*StubShowDBClickPicture)(
    PVOID   This,
    PWSTR   PicturePath,
    PRECT   ClickPosition,
    BOOL    FromHistoryIfFalse,
    PVOID   Unknown
);

BOOL    (CDECL *StubGetPlatformCore)(PVOID *Core);
BOOL    (CDECL *StubInitPluginFileSystem)(PCWSTR PluginName);
HRESULT (NTAPI *StubPlatformCore_QueryInterface)(PVOID Object, REFGUID Guid, PVOID Output);
VOID    (FASTCALL *StubOnConnectionBroken)(PVOID This, PVOID, ULONG Param1, ULONG Param2, ULONG Param3, PVOID MessageString, ULONG Type);
HRESULT (FASTCALL *StubOnSysDataCome)(PVOID This, PVOID Dummy, USHORT Type, ULONG Param1, ULONG Param2);


/************************************************************************
  unlimited custom face
************************************************************************/

TYPE_OF(Util::Group::CheckMsgImage) StubCheckMsgImage;

/************************************************************************
  at all group member
************************************************************************/

TYPE_OF(Util::Contact::IsSuperVip)  StubIsSuperVip;
HRESULT (NTAPI *StubGroupMgr_QueryGroupObject)(PVOID Object, ULONG_PTR GroupUin, PVOID *GroupObject);
HRESULT (NTAPI *StubGroupMgr_GetAdminFlags)(PVOID Object, ULONG_PTR Uin, PBOOL IsAdmin, PBOOL IsCreator);

EXTC UCHAR NTAPI QqNetbios(PNCB pcnb)
{
    return StubNetbios(pcnb);
}

BOOL IsQQUINSpecified()
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
        { RTL_CONSTANT_STRING(L"\\All Users\\QQ\\History.db"),  CONST_STRLEN(L"History.db") * sizeof(WCHAR), GlobalHistoryDb },
        { RTL_CONSTANT_STRING(L"\\All Users\\QQ\\Registry.db"), CONST_STRLEN(L"Registry.db") * sizeof(WCHAR), GlobalRegistryDb },
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

ULONG
WINAPI
QqGetModuleFileNameExW(
    HANDLE  Process,
    PVOID   Module,
    PWSTR   Filename,
    ULONG   Size
)
{
    ULONG       Length;
    PWSTR       File;
    NTSTATUS    Status;
    PROCESS_BASIC_INFORMATION BasicInfo;

    static WCHAR QQProtect[] = L"QQProtect.exe";

    Length = StubGetModuleFileNameExW(Process, (HMODULE)Module, Filename, Size);
    if (Length == 0 || Filename == nullptr || Size == 0)
        return Length;

    Status = NtQueryInformationProcess(Process, ProcessBasicInformation, &BasicInfo, sizeof(BasicInfo), nullptr);
    if (NT_FAILED(Status) || BasicInfo.UniqueProcessId != CurrentPid())
        return Length;

    File = findnamew(Filename);
    CopyStruct(File, QQProtect, sizeof(QQProtect));

    return File - Filename + CONST_STRLEN(QQProtect);
}

NTSTATUS
NTAPI
QqNtQueryInformationProcess(
    HANDLE              ProcessHandle,
    PROCESSINFOCLASS    ProcessInformationClass,
    PVOID               ProcessInformation,
    ULONG               ProcessInformationLength,
    PULONG              ReturnLength
)
{
    NTSTATUS Status;

    union
    {
        PVOID Information;
        PPROCESS_BASIC_INFORMATION Basic;
    };

    Status = StubNtQueryInformationProcess(ProcessHandle, ProcessInformationClass, ProcessInformation, ProcessInformationLength, ReturnLength);
    FAIL_RETURN(Status);

    Information = ProcessInformation;

    switch (ProcessInformationClass)
    {
        case ProcessBasicInformation:
            if (Basic->UniqueProcessId == CurrentPid())
            {
                Basic->InheritedFromUniqueProcessId = Basic->UniqueProcessId;
            }
            break;
    }

    return Status;
}

HANDLE
NTAPI
QqCreateWaitQQProtectThread(
    PSECURITY_ATTRIBUTES    ThreadAttributes,
    ULONG_PTR               StackSize,
    PTHREAD_START_ROUTINE   StartAddress,
    PVOID                   Parameter,
    ULONG                   CreationFlags,
    PULONG                  ThreadId
)
{
    NTSTATUS    Status;
    PVOID       Ebp, CallCreateQQProtectExchangeWindow;
    PROCESS_BASIC_INFORMATION BasicInfo;

    LOOP_ONCE
    {
        if (PtrAnd(Parameter, 0xFFF00000) != 0)
            continue;

        Status = NtQueryInformationProcess((HANDLE)Parameter, ProcessBasicInformation, &BasicInfo, sizeof(BasicInfo), nullptr);
        FAIL_BREAK(Status);

        if (BasicInfo.UniqueProcessId != CurrentPid())
            break;

        AllocStack(16);
        Ebp = *((PVOID *)_AddressOfReturnAddress() - 1);

        CallCreateQQProtectExchangeWindow = *((PVOID *)Ebp + 1);
        if (*(PBYTE)CallCreateQQProtectExchangeWindow != CALL)
            break;

        NtClose((HANDLE)Parameter);

        *(PULONG_PTR)((PVOID *)Ebp + 1) += GetOpCodeSize(CallCreateQQProtectExchangeWindow);

        return nullptr;
    }

    return HummerCreateThread(ThreadAttributes, StackSize, StartAddress, Parameter, CreationFlags, ThreadId);
}

HRESULT
NTAPI
ShowDBClickPicture(
    PVOID   This,
    PWSTR   PicturePath,
    PRECT   ClickPosition,
    BOOL    FromHistoryIfFalse,
    PVOID   Unknown
)
{
    SHELLEXECUTEINFOW ShellExecueInfo;

    if (GetKeyState(VK_CONTROL) < 0)
        return StubShowDBClickPicture(This, PicturePath, ClickPosition, FromHistoryIfFalse, Unknown);

    ZeroMemory(&ShellExecueInfo, sizeof(ShellExecueInfo));
    ShellExecueInfo.cbSize  = sizeof(ShellExecueInfo);
    ShellExecueInfo.lpFile  = PicturePath;
    ShellExecueInfo.lpVerb  = L"open";

    ShellExecuteExW(&ShellExecueInfo);

    return S_OK;
}

BOOL IsWindowMessageBox(HWND hWnd)
{
    WCHAR Title[0x200];

    GetWindowTextW(hWnd, Title, countof(Title));

    return wcsstr(Title, L" - 消息盒子") != nullptr;
}

BOOL
NTAPI
QqSetWindowPos(
    HWND    hWnd,
    HWND    hWndInsertAfter,
    int     X,
    int     Y,
    int     cx,
    int     cy,
    UINT    Flags
)
{
    BOOL IsMessageBox;

    LONG BuddyWidth     = 553;
    LONG BuddyHeight    = 526;
    LONG GroupWidth     = 603;
    LONG GroupHeight    = 527;
    LONG DiscussWidth   = 556;
    LONG DiscussHeight  = 526;

#define GROUP_WIDTH     722
#define GROUP_HEIGHT    671
#define BUDDY_WIDTH     506
#define BUDDY_HEIGHT    507

#if 0

    AllocConsole();
    PrintConsoleW(L"%d, %d\n", cx, cy);

    {
        FILE *fp;

        fp = fopen("E:\\desktop\\qqlog.txt", "ab");
        fprintf(fp, "%d, %d\r\n", cx, cy);
        fclose(fp);
    }

#endif

    IsMessageBox = IsWindowMessageBox(hWnd);

    if (
        IsMessageBox                            ||
        (cx == BuddyWidth && cy == BuddyHeight) ||
        (cx == GroupWidth && cy == GroupHeight) ||
        (cx == DiscussWidth && cy == DiscussHeight)
       )
    {
        RECT WorkArea;

        SystemParametersInfoW(SPI_GETWORKAREA, 0, &WorkArea, 0);

        if (IsMessageBox)
        {
            cx = (WorkArea.right - WorkArea.left) * 80 / 100;
            cy = (WorkArea.bottom - WorkArea.top) * 90 / 100;
        }
        else if (cx == BuddyWidth)
        {
            //cx = BUDDY_WIDTH;
            //cy = BUDDY_HEIGHT;
        }
        else
        {
            cx = GROUP_WIDTH;
            cy = GROUP_HEIGHT;
        }

        X = ((WorkArea.right - WorkArea.left) - cx) / 2;
        Y = ((WorkArea.bottom - WorkArea.top) - cy) / 2;

        CLEAR_FLAG(Flags, SWP_NOSIZE | SWP_NOMOVE);
    }

    return StubSetWindowPos(hWnd, hWndInsertAfter, X, Y, cx, cy, Flags);
}

BOOL NTAPI QqShowWindow(HWND hWnd, int CmdShow)
{
    if (IsWindowMessageBox(hWnd))
        QqSetWindowPos(hWnd, NULL, 0, 0, 0, 0, 0);

    return StubShowWindow(hWnd, CmdShow);
}

BOOL NTAPI QqPostMessageW(HWND hWnd, UINT Message, WPARAM wParam, LPARAM lParam)
{
    switch (Message)
    {
        case 0x7E9:
        case 0x7EA:
        case 0x7EB:
        case 0x7EC:
            if (wParam > 0x10000 && msvcrX0_free != NULL)
                msvcrX0_free((PVOID)wParam);

            return TRUE;
    }

    return StubPostMessageW(hWnd, Message, wParam, lParam);
}

BOOL NTAPI PopupSecurityFrame(PVOID, PVOID)
{
    return TRUE;
}

BOOL CDECL ReportScanResult()
{
    INLINE_ASM __emit 0xCC;
    return TRUE;
}

BOOL CDECL PluginSecurityCheck()
{
    return TRUE;
}

NTSTATUS CDECL CheckPluginList()
{
    return STATUS_SUCCESS;
}

BOOL CDECL IsTencentTrusted(PCWSTR FileName)
{
    return TRUE;
}

HRESULT NTAPI GroupMgr_GetAdminFlags(PVOID Object, ULONG_PTR Uin, PBOOL IsAdmin, PBOOL IsCreator)
{
    HRESULT Result;

    Result = StubGroupMgr_GetAdminFlags(Object, Uin, IsAdmin, IsCreator);

    if (Uin == Util::Contact::GetSelfUin()) LOOP_ONCE
    {
        if ((IsAdmin != nullptr && *IsAdmin != FALSE) || (IsCreator != nullptr && *IsCreator != FALSE))
            break;

        if (IsAdmin != nullptr)
        {
            *IsAdmin = TRUE;
            break;
        }

        if (IsCreator != nullptr)
            *IsCreator = TRUE;
    }

    return S_OK;
}

HRESULT NTAPI GroupMgr_QueryGroupObject(PVOID Object, ULONG_PTR GroupUin, PVOID *GroupObject)
{
    HRESULT Result;

    Result = StubGroupMgr_QueryGroupObject(Object, GroupUin, GroupObject);

    if (SUCCEEDED(Result) && StubGroupMgr_GetAdminFlags == nullptr)
    {
        MEMORY_FUNCTION_PATCH f[] =
        {
            INLINE_HOOK_JUMP(*(PVOID *)PtrAdd(**(PVOID **)GroupObject, 0x5C), GroupMgr_GetAdminFlags, StubGroupMgr_GetAdminFlags),
        };

        Nt_PatchMemory(nullptr, 0, f, countof(f));
    }

    return Result;
}

HRESULT NTAPI GroupMgr_QueryInterface(PVOID Object, REFGUID Guid, PVOID *Output)
{
    HRESULT Result;

    Result = StubPlatformCore_QueryInterface(Object, Guid, Output);

    if (SUCCEEDED(Result) && StubGroupMgr_QueryGroupObject == nullptr)
    {
        MEMORY_FUNCTION_PATCH f[] =
        {
            INLINE_HOOK_JUMP(*(PVOID *)PtrAdd(**(PVOID **)Output, 0x24), GroupMgr_QueryGroupObject, StubGroupMgr_QueryGroupObject),
        };

        Nt_PatchMemory(nullptr, 0, f, countof(f));
    }

    return Result;
}

// CTXComponentMgr

HRESULT NTAPI PlatformCore_QueryInterface(PVOID Object, REFGUID Guid, PVOID *Output)
{
    static GUID GUID_BlackList[] =
    {
        { 0x41D26ED5, 0x7680, 0x4631, 0xBC, 0xC1, 0x5E, 0x52, 0x30, 0x37, 0xF7, 0x0A }, // GUID_PluginCenter
        { 0x76063A86, 0xD553, 0x44A6, 0xAF, 0x7A, 0x12, 0xAE, 0x87, 0x21, 0x1A, 0xA7 }, // GUID_GroupMgr
        { 0xC8730021, 0xE7DE, 0x4F65, 0x98, 0x8C, 0x7D, 0x69, 0x4C, 0x38, 0x83, 0x6E }, // GUID_DllHashCheckMgr
    };

    GUID *BlackList;

    LOOP_ONCE
    {
        PLDR_MODULE AppUtil;

        if (Output != nullptr)
            *Output = nullptr;

        FOR_EACH_ARRAY(BlackList, GUID_BlackList)
        {
            if (Guid == *BlackList)
                break;
        }

        switch (BlackList - GUID_BlackList)
        {
            case countof(GUID_BlackList):
                continue;

            case 0:
                AppUtil = FindLdrModuleByHandle(_ReturnAddress());
                if (AppUtil != NULL && AppUtil->DllBase == AppUtilBase)
                    continue;
                break;

            case 1:
                return GroupMgr_QueryInterface(Object, Guid, Output);
        }

        return E_NOINTERFACE;
    }

    return StubPlatformCore_QueryInterface(Object, Guid, Output);
}

BOOL CDECL GetPlatformCore(PVOID *Core)
{
    BOOL Success;

    Success = StubGetPlatformCore(Core);
    if (!Success)
        return Success;

    if (StubPlatformCore_QueryInterface != nullptr)
        return Success;

    MEMORY_FUNCTION_PATCH f[] =
    {
        INLINE_HOOK_JUMP(*(PVOID *)PtrAdd(**(PVOID **)Core, 0x20), PlatformCore_QueryInterface, StubPlatformCore_QueryInterface),
    };

    Nt_PatchMemory(nullptr, 0, f, countof(f));

    return Success;
}

BOOL CDECL InitPluginFileSystem(PCWSTR PluginName)
{
    PWSTR       Buffer, Name;
    ULONG_PTR   BufferSize, Length;
    PLDR_MODULE Module;

    static WCHAR PluginPath[] = L"..\\Plugin\\";

    Module = FindLdrModuleByHandle(nullptr);
    Length = (StrLengthW(PluginName) + 1) * sizeof(WCHAR);
    BufferSize = Module->FullDllName.Length + Length + sizeof(PluginPath);
    Buffer = (PWSTR)AllocStack(BufferSize);
    CopyMemory(Buffer, Module->FullDllName.Buffer, Module->FullDllName.Length);

    Name = findnamew(Buffer);
    CopyMemory(Name, PluginPath, sizeof(PluginPath));
    CopyMemory(Name + CONST_STRLEN(PluginPath), PluginName, Length);

    if (!Io::IsPathExists(Buffer))
        return FALSE;

    return StubInitPluginFileSystem(PluginName);
}

VOID FASTCALL OnConnectionBroken(PVOID This, PVOID Dummy, ULONG Param1, ULONG Param2, ULONG Param3, PVOID MessageString, ULONG RetryTimeOut)
{
    if (RetryTimeOut == 0xB)
        return;

    StubOnConnectionBroken(This, Dummy, Param1, Param2, Param3, MessageString, RetryTimeOut);
}

HRESULT FASTCALL OnSysDataCome(PVOID This, PVOID Dummy, USHORT Type, ULONG Param1, ULONG Param2)
{
    if (Type == 0x30)
    {
        return S_OK;
    }

    WCHAR buf[0x100];

    swprintf(buf, L"%p", Type);
    MessageBoxW(0, buf, 0, 64);

    return StubOnSysDataCome(This, Dummy, Type, Param1, Param2);
}

BOOL CDECL CheckMsgImage(PVOID GroupObject, CTXStringW &Message)
{
    BOOL Success;

    Success = StubCheckMsgImage(GroupObject, Message);

    if (!Success && !Message.IsEmpty())
    {
        if (wcsstr(Message.Buffer, L"发送") != nullptr)
        {
            Success = TRUE;
            Message.Empty();
        }
    }

    return Success;
}

BOOL CDECL IsSuperVip(ULONG_PTR Uin, PULONG_PTR SVipLevel)
{
    if (Uin == Util::Contact::GetSelfUin())
    {
        if (SVipLevel != nullptr)
            *SVipLevel = 7;

        return TRUE;
    }

    return StubIsSuperVip(Uin, SVipLevel);
}

ULONG CDECL GetAtAllGroupMemberUseTimes()
{
    return 1;
}

HRESULT CDECL GetCurrentAtNumber(PVOID Object, PULONG Number)
{
    *Number = 0;
    return S_OK;
}

/************************************************************************
  init functions
************************************************************************/

PVOID SearchStringReference(PLDR_MODULE Module, PVOID String, ULONG_PTR SizeInBytes, ULONG_PTR BeginOffset = 0)
{
    PVOID StringValue, StringReference;

    SEARCH_PATTERN_DATA Str[] =
    {
        ADD_PATTERN_(String, SizeInBytes),
    };

    StringValue = SearchPattern(Str, countof(Str), Module->DllBase, Module->SizeOfImage);
    if (StringValue == nullptr)
        return nullptr;

    SEARCH_PATTERN_DATA Stub[] =
    {
        ADD_PATTERN(&StringValue),
    };

    StringReference = SearchPattern(Stub, countof(Stub), PtrAdd(Module->DllBase, BeginOffset), PtrSub(Module->SizeOfImage, BeginOffset));
    if (StringReference == nullptr)
        return nullptr;

    return StringReference;
}

PVOID ReverseSearchFunctionHeader(PVOID Start, ULONG_PTR Length)
{
    PBYTE Buffer;

    Buffer = (PBYTE)Start;

    for (; Length != 0; --Buffer, --Length)
    {
        switch (Buffer[0])
        {
            case CALL:
                // push    local_var_size
                // mov     eax, exception_handler
                // call    _SEH_prolog

                if (Buffer[-5] != 0xB8)
                    continue;

                if (Buffer[-7] == 0x6A)
                {
                    Buffer -= 7;
                }
                else if (Buffer[-10] == 0x68)
                {
                        Buffer -= 10;
                }
                else
                {
                    continue;
                }

                break;

            case 0x55:
                if (Buffer[1] != 0x8B || Buffer[2] != 0xEC)
                    continue;

                // push ebp
                // mov ebp, esp

                break;

            default:
                continue;
        }

        return Buffer;
    }

    return nullptr;
}

PVOID
SearchStringAndReverseSearchHeader(
    PVOID       ImageBase,
    PVOID       BytesSequence,
    ULONG_PTR   SizeInBytes,
    ULONG_PTR   SearchRange
)
{
    PVOID       StringReference;
    PLDR_MODULE Module;

    Module = FindLdrModuleByHandle(ImageBase);

    StringReference = SearchStringReference(Module, BytesSequence, SizeInBytes);
    if (StringReference == nullptr)
        return IMAGE_INVALID_VA;

    StringReference = ReverseSearchFunctionHeader(PtrAdd(StringReference, 4), SearchRange);

    return StringReference == nullptr ? IMAGE_INVALID_VA : StringReference;
}

PVOID SearchAppMisc_PluginListCheck(PVOID ImageBase)
{
    static WCHAR String[] = L"PluginListCheck　Begin";

    return SearchStringAndReverseSearchHeader(ImageBase, String, sizeof(String), 0x60);
}

PVOID SearchAppMisc_ShowPicInMultiPic(PVOID ImageBase)
{
    static WCHAR String[] = L"ShowPicInMultiPic begin";

    return SearchStringAndReverseSearchHeader(ImageBase, String, sizeof(String) - sizeof(WCHAR), 0x20);
}

PVOID SearchChatFrame_CheckModule(PVOID ChatFrame)
{
    PBYTE       Buffer;
    PVOID       StringReference, LastCall[3];
    PLDR_MODULE Module;

    static WCHAR String[] = L"exit for invalid version";

    Module = FindLdrModuleByHandle(ChatFrame);

    StringReference = SearchStringReference(Module, String, sizeof(String) - sizeof(WCHAR));
    if (StringReference == nullptr)
        return IMAGE_INVALID_VA;

    Buffer = (PBYTE)StringReference + 4;

    ZeroMemory(LastCall, sizeof(LastCall));

    LOOP_FOREVER
    {
        ULONG_PTR Length;

        if (Buffer[0] == 0xC3 || Buffer[0] == 0xC2)
            break;

        if (Buffer[0] == CALL)
        {
            LastCall[0] = LastCall[1];
            LastCall[1] = LastCall[2];
            LastCall[2] = Buffer;
        }

        Length = GetOpCodeSize(Buffer);
        Buffer += Length;
    }

    return LastCall[0] == nullptr ? IMAGE_INVALID_VA : GetCallDestination(LastCall[0]);
}

PVOID SearchAppUtil_CheckImportantModule(PVOID ImageBase)
{
    static WCHAR String[] = L"PerfStand.CheckImportantModule.Begin";

    return SearchStringAndReverseSearchHeader(ImageBase, String, sizeof(String), 0x20);
}

PVOID SearchMainFrame_SecurityFrame(PVOID ImageBase)
{
    static WCHAR String[] = L"Misc\\SecurityFrame.xml|SecurityWnd";

    return SearchStringAndReverseSearchHeader(ImageBase, String, sizeof(String), 0xB0);
}

PVOID SearchPreLogin_OnConnectionBroken(PVOID ImageBase)
{
    static WCHAR String[] = L"CTXServerConnectionDectecter::OnConnectionBroken Stop CSProcessor";

    return SearchStringAndReverseSearchHeader(ImageBase, String, sizeof(String), 0xB0);
}

PVOID SearchPreLogin_OnSysDataCome(PVOID ImageBase)
{
    static WCHAR String[] = L"CTXServerConnectionDectecter::OnSysDataCome";

    return SearchStringAndReverseSearchHeader(ImageBase, String, sizeof(String) - sizeof(String[0]), 0x20);
}

BOOL SearchGroupApp_AtAllGroupMember(PVOID GroupApp, PVOID *GetAdminFlag, PVOID *GetUseTimes)
{
    static WCHAR String[] = L"AtAllGroupMember_MsgBox_Title";

    PVOID Found;
    PBYTE Buffer;
    PLDR_MODULE Module;

    Module = FindLdrModuleByHandle(GroupApp);

    Found = SearchStringReference(Module, String, sizeof(String));
    if (Found == nullptr)
        return FALSE;

    Buffer = (PBYTE)Found - 1;

    if (Buffer[0] != PUSH ||
        Buffer[-2] != 0x6A ||
        Buffer[-4] != 0x75)
    {
        return FALSE;
    }

    *GetAdminFlag = &Buffer[-4];

    Found = SearchStringReference(Module, String, sizeof(String), PtrOffset(Buffer + 5, Module->DllBase));
    if (Found == nullptr)
        return FALSE;

    Buffer = (PBYTE)Found - 1;

    if (Buffer[0] != PUSH ||
        Buffer[-2] != 0x6A ||
        Buffer[-4] != 0x75 ||
        Buffer[-0xB] != CALL)
    {
        return FALSE;
    }

    *GetUseTimes = GetCallDestination(&Buffer[-0xB]);

    return TRUE;
}

BOOL SearchGroupApp_AtAllGroupMemberMax(PVOID GroupApp, PVOID *ConditionJump)
{
    PVOID Found, Buffer;
    PLDR_MODULE Module;

    /************************************************************************
    360C9908    .  E8 93F0FFFF         call    0x360C89A0
    360C990D    .  83BD 74FFFFFF 14    cmp     dword ptr [ebp-0x8C], 0x14
    360C9914    .  59                  pop     ecx
    360C9915    .  59                  pop     ecx
    360C9916    .  7C 12               jl      short 0x360C992A
    ************************************************************************/

    BYTE CallStub[]      = { CALL };
    BYTE CmpEbp[]        = { 0x83, 0xBD };
    BYTE CmpR32_0x14[]   = { 0x14 };

    SEARCH_PATTERN_DATA Pattern[] =
    {
        ADD_PATTERN(CallStub,       0, 5),
        ADD_PATTERN(CmpEbp,         0, 6),
        ADD_PATTERN(CmpR32_0x14),
    };

    Module = FindLdrModuleByHandle(GroupApp);
    Buffer = SearchPattern(Pattern, countof(Pattern), Module->DllBase, Module->SizeOfImage);
    if (Buffer == nullptr)
        return FALSE;

    Found = IMAGE_INVALID_VA;

    WalkOpCodeT(Buffer, 0x20,
        WalkOpCodeM(Buffer, OpLength, Ret)
        {
            switch (Buffer[0])
            {
                case 0x7C:  // jl short
                    Found = Buffer;
                    return STATUS_SUCCESS;
            }

            return STATUS_NOT_FOUND;
        }
    );

    *ConditionJump = Buffer;

    return Found != IMAGE_INVALID_VA;
}

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    BOOL                        QQUINSpecified;
    NTSTATUS                    Status;
    PVOID                       module;
    ULONG_PTR                   CreateThreadIAT;
    PROCESS_BASIC_INFORMATION   BasicInfo;
    UNICODE_STRING              SystemRoot;
    PLDR_MODULE                 Self, Netapi32;

    ml::MlInitialize();

    LdrDisableThreadCalloutsForDll(BaseAddress);

    Status = Rtl::GetSystemDirectory(&SystemRoot);
    if (NT_FAILED(Status))
        return FALSE;

    module = Ldr::LoadDll(ml::String(SystemRoot) + L"netapi32.dll");
    RtlFreeUnicodeString(&SystemRoot);

    *(PVOID *)&StubNetbios = GetRoutineAddress(module, "Netbios");

    Self = FindLdrModuleByHandle(BaseAddress);
    Netapi32 = FindLdrModuleByHandle(module);

    Self->DllBase       = Netapi32->DllBase;
    Self->EntryPoint    = Netapi32->EntryPoint;
    Self->SizeOfImage   = Netapi32->SizeOfImage;

    LdrAddRefDll(LDR_ADDREF_DLL_PIN, module);

    InitializeQqFunctionTable();


    /************************************************************************
      msvcrxx
    ************************************************************************/

    {
        PLDR_MODULE crt;
        PUNICODE_STRING crtname;

        static UNICODE_STRING msvcrt[] =
        {
            RTL_CONSTANT_STRING(L"msvcr80.dll"),
            RTL_CONSTANT_STRING(L"msvcr90.dll"),
            RTL_CONSTANT_STRING(L"msvcr100.dll"),
            RTL_CONSTANT_STRING(L"msvcr110.dll"),
        };

        FOR_EACH_ARRAY(crtname, msvcrt)
        {
            crt = FindLdrModuleByName(crtname);
            if (crt == nullptr)
                continue;

            *(PVOID *)&msvcrX0_free = GetRoutineAddress(crt->DllBase, "free");
            break;
        }
    }


    /************************************************************************
      user32
    ************************************************************************/

    module = Ldr::LoadDll(L"USER32.dll");

    MEMORY_FUNCTION_PATCH Function_user32[] =
    {
        EAT_HOOK_JUMP_HASH(module, USER32_SetWindowPos, QqSetWindowPos, StubSetWindowPos),
        //EAT_HOOK_JUMP_HASH(module, USER32_ShowWindow,   QqShowWindow,   StubShowWindow),
        EAT_HOOK_JUMP_HASH(module, USER32_PostMessageW, QqPostMessageW, StubPostMessageW)
    };


    /************************************************************************
      ntdll
    ************************************************************************/

    QQUINSpecified = IsQQUINSpecified();

    MEMORY_FUNCTION_PATCH Function_ntdll[] =
    {
        INLINE_HOOK_JUMP(QQUINSpecified ? NtOpenFile            : IMAGE_INVALID_VA, QqNtOpenFile,               StubNtOpenFile),
        INLINE_HOOK_JUMP(QQUINSpecified ? NtCreateFile          : IMAGE_INVALID_VA, QqNtCreateFile,             StubNtCreateFile),
        INLINE_HOOK_JUMP(QQUINSpecified ? NtQueryAttributesFile : IMAGE_INVALID_VA, QqNtQueryAttributesFile,    StubNtQueryAttributesFile),
        INLINE_HOOK_JUMP(NtQueryInformationProcess,                                 QqNtQueryInformationProcess,StubNtQueryInformationProcess),
    };


    /************************************************************************
      psapi
    ************************************************************************/

    module = Ldr::LoadDll(L"psapi.dll");

    MEMORY_FUNCTION_PATCH Function_psapi[] =
    {
        EAT_HOOK_JUMP_HASH(module, PSAPI_GetModuleFileNameExW, QqGetModuleFileNameExW, StubGetModuleFileNameExW),
    };


    /************************************************************************
      Common
    ************************************************************************/

    module = Ldr::LoadDll(L"Common.dll");

    MEMORY_FUNCTION_PATCH Function_Common[] =
    {
        EAT_HOOK_JUMP_NULL(module, "?IsTencentTrusted@Misc@Util@@YAHPB_W@Z",            IsTencentTrusted),
        EAT_HOOK_JUMP     (module, "?InitPluginFileSystem@Boot@Util@@YAHPA_W@Z",        InitPluginFileSystem,   StubInitPluginFileSystem),
        EAT_HOOK_JUMP     (module, "?GetPlatformCore@Core@Util@@YAHPAPAUITXCore@@@Z",   GetPlatformCore,        StubGetPlatformCore),
    };


    /************************************************************************
      HummerEngine
    ************************************************************************/

    module = Ldr::LoadDll(L"HummerEngine.dll");

    CreateThreadIAT = IATLookupRoutineRVAByHashNoFix(module, KERNEL32_CreateThread);
    if (CreateThreadIAT != IMAGE_INVALID_RVA)
        CreateThreadIAT = PtrAdd(CreateThreadIAT, module);

    *(PVOID *)&HummerCreateThread = *(PVOID *)CreateThreadIAT;

    MEMORY_PATCH Patch_HummerEngine[] =
    {
        PATCH_MEMORY(QqCreateWaitQQProtectThread, sizeof(PVOID), CreateThreadIAT),
    };


    /************************************************************************
      KernelUtil

        CF_Group_Image_TooManyImage
    ************************************************************************/

    MEMORY_FUNCTION_PATCH Function_KernelUtil[] =
    {
        INLINE_HOOK_JUMP(Util::Group::CheckMsgImage, CheckMsgImage, StubCheckMsgImage),
        INLINE_HOOK_JUMP(Util::Contact::IsSuperVip,  IsSuperVip,    StubIsSuperVip),
    };


    /************************************************************************
      GroupApp
    ************************************************************************/

    BOOL AtAllGroupMemberFound, AtGroupMemberMaxFound;
    PVOID GetAdminFlag, GetUseTimes, AtGroupMemberMax;

    module = Ldr::LoadDll(L"GroupApp.dll");

    AtAllGroupMemberFound = SearchGroupApp_AtAllGroupMember(module, &GetAdminFlag, &GetUseTimes);
    AtGroupMemberMaxFound = SearchGroupApp_AtAllGroupMemberMax(module, &AtGroupMemberMax);

    MEMORY_FUNCTION_PATCH Function_GroupApp[] =
    {
        INLINE_HOOK_JUMP_NULL(AtAllGroupMemberFound ? GetUseTimes : IMAGE_INVALID_VA, GetAtAllGroupMemberUseTimes),
        INLINE_HOOK_CALL_NULL(AtGroupMemberMaxFound ? AtGroupMemberMax : IMAGE_INVALID_VA, GetCurrentAtNumber),
    };


    /************************************************************************
      AppMisc

        L"PluginListCheck"
        mov     eax, 0x80004005

        ShowPicInMultiPic begin
    ************************************************************************/

    module = Ldr::LoadDll(L"AppMisc.dll");

    MEMORY_FUNCTION_PATCH Function_AppMisc[] =
    {
        INLINE_HOOK_JUMP_NULL(SearchAppMisc_PluginListCheck(module),    CheckPluginList), // addition SetTimeOut
        INLINE_HOOK_JUMP     (SearchAppMisc_ShowPicInMultiPic(module),  ShowDBClickPicture, StubShowDBClickPicture),
    };


    /************************************************************************
      MainFrame
    ************************************************************************/

    module = Ldr::LoadDll(L"MainFrame.dll");

    MEMORY_FUNCTION_PATCH Function_MainFrame[] =
    {
        INLINE_HOOK_JUMP_NULL(SearchMainFrame_SecurityFrame(module),    PopupSecurityFrame),
    };



    /************************************************************************
      ChatFrameApp

        L"exit for invalid version.17
    ************************************************************************/
/*
    module = Ldr::LoadDll(L"ChatFrameApp.dll");

    MEMORY_FUNCTION_PATCH Function_ChatFrame[] =
    {
        //INLINE_HOOK_JUMP_RVA_NULL(0x93C3, IsTencentTrusted),
        INLINE_HOOK_JUMP_RVA_NULL(SearchChatFrame_CheckModule(module), IsTencentTrusted),
    };

*/
    /************************************************************************
      AppUtil

        L"PerfStand.CheckImportantModule.Begin"
        L"DllCheck"
        L"Dll Check Fail"

        check:
            QQExternal.exe
            TXPlatform.exe
            ...
    ************************************************************************/

    module = Ldr::LoadDll(L"AppUtil.dll");

    AppUtilBase = module;

    MEMORY_FUNCTION_PATCH Function_AppUtil[] =
    {
        EAT_HOOK_JUMP_NULL(module, "?ReportScanResult@Misc@Util@@YAHKVCTXStringW@@0@Z", ReportScanResult),
        EAT_HOOK_JUMP_NULL(module, "?PluginSecurityCheck@Misc@Util@@YAHXZ",             PluginSecurityCheck),
        INLINE_HOOK_JUMP_NULL(SearchAppUtil_CheckImportantModule(module),               CheckPluginList),
    };


    /************************************************************************
      PreLogin
    ************************************************************************/

    module = Ldr::LoadDll(L"PreloginLogic.dll");

    MEMORY_FUNCTION_PATCH Function_PreLogin[] =
    {
        //INLINE_HOOK_JUMP(SearchPreLogin_OnConnectionBroken(module), OnConnectionBroken, StubOnConnectionBroken),
        INLINE_HOOK_JUMP(SearchPreLogin_OnSysDataCome(module), OnSysDataCome, StubOnSysDataCome),
    };


    /************************************************************************
      end
    ************************************************************************/

    PATCH_ARRAY *Entry, Array[] =
    {
        { nullptr,              Patch_HummerEngine,     countof(Patch_HummerEngine) },
        { nullptr,              nullptr,                0,                          Function_KernelUtil, countof(Function_KernelUtil)},
        { nullptr,              nullptr,                0,                          Function_GroupApp,   countof(Function_GroupApp)  },
        { nullptr,              nullptr,                0,                          Function_AppUtil,    countof(Function_AppUtil)   },
        { nullptr,              nullptr,                0,                          Function_AppMisc,    countof(Function_AppMisc)   },
        { nullptr,              nullptr,                0,                          Function_MainFrame,  countof(Function_MainFrame) },
        { nullptr,              nullptr,                0,                          Function_PreLogin,   countof(Function_PreLogin)  },
        { nullptr,              nullptr,                0,                          Function_Common,     countof(Function_Common)    },

        { nullptr,              nullptr,                0,                          Function_ntdll,      countof(Function_ntdll)     },
        { nullptr,              nullptr,                0,                          Function_psapi,      countof(Function_psapi)     },
        { nullptr,              nullptr,                0,                          Function_user32,     countof(Function_user32)    },
    };

    FOR_EACH_ARRAY(Entry, Array)
    {
        PVOID Base;

        Base = Entry->DllName == nullptr ? nullptr : Ldr::LoadDll(Entry->DllName);

        Nt_PatchMemory(Entry->Patch, Entry->PatchCount, Entry->FunctionPatch, Entry->FunctionCount, Base);
    }

    return TRUE;
}

BOOL WINAPI DllMain(PVOID BaseAddress, ULONG Reason, PVOID Reserved)
{
    switch (Reason)
    {
        case DLL_PROCESS_ATTACH:
            return Initialize(BaseAddress) || UnInitialize(BaseAddress);

        case DLL_PROCESS_DETACH:
            UnInitialize(BaseAddress);
            break;
    }

    return TRUE;
}
