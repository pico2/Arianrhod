#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")
#pragma comment(linker, "/EXPORT:Netbios=_QqNetbios@4")
#pragma comment(linker, "/EXPORT:NetApiBufferFree=_QqNetApiBufferFree@4")
#pragma comment(linker, "/EXPORT:NetWkstaTransportEnum=_QqNetWkstaTransportEnum@28")

#include "QQ2011.h"
#include "MyLibrary.cpp"
#include <Psapi.h>
#include <Lm.h>
#include "QQMethod.h"


/*++

Req AnonymousInfo %lu
AnonymousChat

--*/


WCHAR GlobalRegistryDb[0x20];
WCHAR GlobalHistoryDb[countof(GlobalRegistryDb)];

TXReloginMgr* ReloginMgr;

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
API_POINTER(NetApiBufferFree)           StubNetApiBufferFree;
API_POINTER(NetWkstaTransportEnum)      StubNetWkstaTransportEnum;


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
VOID (FASTCALL *StubGetBanSpeechTimeStamp)(PVOID This, PVOID Edx, PULONG* TimeStampData, PULONG* What);

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

BOOL InitializeNetapi32()
{
    PVOID           module;
    NTSTATUS        Status;
    PLDR_MODULE     Self, Netapi32;
    UNICODE_STRING  SystemRoot;

    if (StubNetbios != nullptr)
        return TRUE;

    Status = Rtl::GetSystemDirectory(&SystemRoot);
    if (NT_FAILED(Status))
        return 0;

    module = Ldr::LoadDll(ml::String(SystemRoot) + L"netapi32.dll");
    RtlFreeUnicodeString(&SystemRoot);

    LdrAddRefDll(LDR_ADDREF_DLL_PIN, module);

    *(PVOID *)&StubNetbios                  = GetRoutineAddress(module, "Netbios");
    *(PVOID *)&StubNetApiBufferFree         = GetRoutineAddress(module, "NetApiBufferFree");
    *(PVOID *)&StubNetWkstaTransportEnum    = GetRoutineAddress(module, "NetWkstaTransportEnum");

    Self = FindLdrModuleByHandle(&__ImageBase);
    Netapi32 = FindLdrModuleByHandle(module);

    //RemoveEntryList(&Self->InLoadOrderLinks);
    //RemoveEntryList(&Self->InMemoryOrderLinks);
    //RemoveEntryList(&Self->InInitializationOrderLinks);

    //RtlFreeHeap(CurrentPeb()->ProcessHeap, 0, Self);

    Self->DllBase       = Netapi32->DllBase;
    Self->EntryPoint    = Netapi32->EntryPoint;
    Self->SizeOfImage   = Netapi32->SizeOfImage;

    return TRUE;
}

EXTC
NET_API_STATUS
NET_API_FUNCTION
QqNetWkstaTransportEnum(
    LPTSTR servername,
    DWORD level,
    LPBYTE *bufptr,
    DWORD prefmaxlen,
    LPDWORD entriesread,
    LPDWORD totalentries,
    LPDWORD resume_handle
)
{
    InitializeNetapi32();
    return StubNetWkstaTransportEnum(servername, level, bufptr, prefmaxlen, entriesread, totalentries, resume_handle);
}

EXTC NET_API_STATUS NET_API_FUNCTION QqNetApiBufferFree(LPVOID Buffer)
{
    InitializeNetapi32();
    return StubNetApiBufferFree(Buffer);
}

EXTC UCHAR NTAPI QqNetbios(PNCB pcnb)
{
    InitializeNetapi32();
    return StubNetbios(pcnb);
}

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
#define GROUP_WIDTH     722
#define GROUP_HEIGHT    671
#define BUDDY_WIDTH     506
#define BUDDY_HEIGHT    507

#if 0

    AllocConsole();
    ShowWindow(GetConsoleWindow(), SW_SHOW);
    PrintConsoleW(L"%d, %d\n", cx, cy);

    if (0)
    {
        FILE *fp;

        fp = fopen("D:\\desktop\\qqlog.txt", "ab");
        fprintf(fp, "%d, %d\r\n", cx, cy);
        fclose(fp);
    }

#endif

    enum
    {
        UnknownWindow,
        BuddyWindow,
        GroupWindow,
        DiscussWindow,
        MessageBox,
    };

    auto GetWindowType = [] (HWND hWnd, INT cx, INT cy)
    {
        BOOL IsMessageBox;
        PSIZE Size;

        static SIZE BuddySize[] =
        {
            { 553, 526 },
        };

        static SIZE GroupSize[] =
        {
            { 614, 546 },
            { 603, 527 },
            { 623, 546 },
            { 599, 524 },
            { 598, 522 },
        };

        static SIZE DiscussSize[] =
        {
            { 567, 545 },
            { 556, 526 },
            { 571, 545 },
        };

        IsMessageBox = IsWindowMessageBox(hWnd);
        if (IsMessageBox)
            return MessageBox;

        FOR_EACH_ARRAY(Size, BuddySize)
        {
            if (Size->cx == cx && Size->cy == cy)
                return BuddyWindow;
        }

        FOR_EACH_ARRAY(Size, GroupSize)
        {
            if (Size->cx == cx && Size->cy == cy)
                return GroupWindow;
        }

        FOR_EACH_ARRAY(Size, DiscussSize)
        {
            if (Size->cx == cx && Size->cy == cy)
                return DiscussWindow;
        }

        return UnknownWindow;
    };

    ULONG WindowType = GetWindowType(hWnd, cx, cy);

    if (WindowType != UnknownWindow)
    {
        RECT WorkArea;

        SystemParametersInfoW(SPI_GETWORKAREA, 0, &WorkArea, 0);

        switch (WindowType)
        {
            case MessageBox:
                cx = (WorkArea.right - WorkArea.left) * 80 / 100;
                cy = (WorkArea.bottom - WorkArea.top) * 90 / 100;
                break;

            case BuddyWindow:
                //cx = BUDDY_WIDTH;
                //cy = BUDDY_HEIGHT;
                break;

            case GroupWindow:
            case DiscussWindow:
                cx = GROUP_WIDTH;
                cy = GROUP_HEIGHT;
                break;
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
        QqSetWindowPos(hWnd, nullptr, 0, 0, 0, 0, 0);

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
            if (wParam > 0x10000 && msvcrX0_free != nullptr)
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
    DebugBreakPoint();
    //return TRUE;
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
        {
            *IsCreator = TRUE;
            break;
        }
    }

    return S_OK;
}

HRESULT NTAPI GroupMgr_QueryGroupObject(PVOID Object, ULONG_PTR GroupUin, PVOID *GroupObject)
{
    HRESULT Result;

    Result = StubGroupMgr_QueryGroupObject(Object, GroupUin, GroupObject);

    if (SUCCEEDED(Result) && StubGroupMgr_GetAdminFlags == nullptr)
    {
        Mp::PATCH_MEMORY_DATA p[] =
        {
            Mp::FunctionJumpVa(*(PVOID *)PtrAdd(**(PVOID **)GroupObject, 0x5C), GroupMgr_GetAdminFlags, &StubGroupMgr_GetAdminFlags),
        };

        Mp::PatchMemory(p, countof(p));
    }

    return Result;
}

HRESULT NTAPI GroupMgr_QueryInterface(PVOID Object, REFGUID Guid, PVOID *Output)
{
    HRESULT Result;

    Result = StubPlatformCore_QueryInterface(Object, Guid, Output);

    if (SUCCEEDED(Result) && StubGroupMgr_QueryGroupObject == nullptr)
    {
        Mp::PATCH_MEMORY_DATA p[] =
        {
            Mp::FunctionJumpVa(*(PVOID *)PtrAdd(**(PVOID **)Output, 0x24), GroupMgr_QueryGroupObject, &StubGroupMgr_QueryGroupObject),
        };

        Mp::PatchMemory(p, countof(p));
    }

    return Result;
}

ULONG NTAPI GroupObject_GetAtAllGroupMemberUseTimes(PVOID)
{
    return 1;
}

HRESULT NTAPI GroupObject_QueryInterface(PVOID Object, REFGUID Guid, PVOID *Output)
{
    HRESULT Result;

    Result = StubPlatformCore_QueryInterface(Object, Guid, Output);
    if (FAILED(Result))
        return Result;

    PVOID& GetAtAllGroupMemberUseTimes = *(PVOID *)PtrAdd(**(PVOID **)Output, 0x10);

    if (GetAtAllGroupMemberUseTimes == GroupObject_GetAtAllGroupMemberUseTimes)
        return Result;

    Mp::PATCH_MEMORY_DATA p[] =
    {
        Mp::MemoryPatchVa((ULONG_PTR)GroupObject_GetAtAllGroupMemberUseTimes, sizeof(ULONG_PTR), &GetAtAllGroupMemberUseTimes),
    };

    Mp::PatchMemory(p, countof(p));

    return Result;
}

// CTXComponentMgr

HRESULT NTAPI PlatformCore_QueryInterface(PVOID Object, REFGUID Guid, PVOID *Output)
{
    static GUID GUID_FilterList[] =
    {
        { 0x41D26ED5, 0x7680, 0x4631, 0xBC, 0xC1, 0x5E, 0x52, 0x30, 0x37, 0xF7, 0x0A }, // GUID_PluginCenter
        { 0x76063A86, 0xD553, 0x44A6, 0xAF, 0x7A, 0x12, 0xAE, 0x87, 0x21, 0x1A, 0xA7 }, // GUID_GroupMgr
        { 0xC8730021, 0xE7DE, 0x4F65, 0x98, 0x8C, 0x7D, 0x69, 0x4C, 0x38, 0x83, 0x6E }, // GUID_DllHashCheckMgr
        { 0x3A990F4E, 0x95BC, 0x4F00, 0xAE, 0x52, 0xFD, 0xD9, 0xFB, 0xFF, 0x30, 0x3E }, // GUID_ReloginMgr
        { 0xD302C850, 0x939F, 0x4575, 0x85, 0xBE, 0xE0, 0x45, 0x11, 0x42, 0x1A, 0x75 }, // GUID_GroupObject
    };

    enum
    {
        GUID_PluginCenter,
        GUID_GroupMgr,
        GUID_DllHashCheckMgr,
        GUID_ReloginMgr,
        GUID_GroupObject,
    };

    GUID *Filter;

    LOOP_ONCE
    {
        PLDR_MODULE AppUtil;

        if (Output != nullptr)
            *Output = nullptr;

        FOR_EACH_ARRAY(Filter, GUID_FilterList)
        {
            if (Guid == *Filter)
                break;
        }

        switch (Filter - GUID_FilterList)
        {
            case countof(GUID_FilterList):
                continue;

            case GUID_PluginCenter:
                AppUtil = FindLdrModuleByHandle(_ReturnAddress());
                if (AppUtil != nullptr && AppUtil->DllBase == AppUtilBase)
                    continue;
                break;

            case GUID_GroupMgr:
                return GroupMgr_QueryInterface(Object, Guid, Output);

            case GUID_ReloginMgr:
            {
                HRESULT hr = StubPlatformCore_QueryInterface(Object, Guid, Output);

                if (ReloginMgr == nullptr && SUCCEEDED(hr))
                {
                    ReloginMgr = (TXReloginMgr *)*Output;
                    ReloginMgr->AddRef();
                }

                return hr;
            }

            case GUID_GroupObject:
                return GroupObject_QueryInterface(Object, Guid, Output);
        }

        return E_NOINTERFACE;
    }

    return StubPlatformCore_QueryInterface(Object, Guid, Output);
}

BOOL CDECL GetPlatformCore(PVOID *Core)
{
    BOOL Success;

    //AllocConsole();
    //ShowWindow(GetConsoleWindow(), SW_SHOW);
    //PrintConsole(L"%p: query\n", (ULONG)NtGetTickCount());
    NtTestAlert();

    Success = StubGetPlatformCore(Core);
    if (!Success)
        return Success;

    if (StubPlatformCore_QueryInterface != nullptr)
        return Success;

    Mp::PATCH_MEMORY_DATA f[] =
    {
        Mp::FunctionJumpVa(*(PVOID *)PtrAdd(**(PVOID **)Core, 0x20), PlatformCore_QueryInterface, &StubPlatformCore_QueryInterface),
    };

    Mp::PatchMemory(f, countof(f));

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
    HRESULT hr;

    //WCHAR buf[0x100];
    //swprintf(buf, L"掉线了 %p", Type);
    //MessageBoxW(0, buf, 0, 64);

    hr = StubOnSysDataCome(This, Dummy, Type, Param1, Param2);

    if (Type == 0x30 && ReloginMgr != nullptr)
    {
        Io::SetAsyncCall(
            []()
            {
                PITXData Data;

                Util::Data::CreateTXData(&Data);
                Data->SetDWord(L"cReloginFlag", 2);

                ReloginMgr->Relogin(nullptr, Data);
                Data->Release();

                //MessageBoxW(0, L"done", 0, 64);
            },
            500
        );
    }

    return hr;
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

ULONG_PTR BanSpeechObjectOffset;

VOID FASTCALL GetBanSpeechTimeStamp(PVOID This, PVOID Edx, PULONG* TimeStampData, PULONG* What)
{
    StubGetBanSpeechTimeStamp(This, Edx, TimeStampData, What);

    ULONG& TimeStamp = (*TimeStampData)[4];

    if (*TimeStampData == *(PULONG*)PtrAdd(PtrSub(This, BanSpeechObjectOffset), BanSpeechObjectOffset + 4))
        return;

    if (GetKeyState(VK_CONTROL) < 0)
    {
        TimeStamp = INT32_MAX;
    }
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

PVOID SearchGroupApp_GroupBanSpeech(PVOID ImageBase)
{
    PVOID Function, CallGetBanSpeechTimeStamp;

    static WCHAR String[] = LR"({"groupuin":%lu;"currenttime":%lu;"banspeechtime":%lu;"useruin":%lu})";

    Function = SearchStringAndReverseSearchHeader(ImageBase, String, sizeof(String) - sizeof(String[0]), 0x320);
    if (Function == IMAGE_INVALID_VA)
        return IMAGE_INVALID_VA;

    CallGetBanSpeechTimeStamp = IMAGE_INVALID_VA;

    WalkOpCodeT(Function, 0x270,
        WalkOpCodeM(Buffer, OpLength, Ret)
        {
            if (
                OpLength == 3 &&
                Buffer[0] == 0x83 && Buffer[1] == 0xC1 && // Buffer[2] == 0x58 &&       // add ecx, const
                Buffer[3] == 0xE8                                                       // call const
               )
            {
                BanSpeechObjectOffset = (ULONG_PTR)Buffer[2];
                CallGetBanSpeechTimeStamp = Buffer + 3;
                return STATUS_SUCCESS;
            }

            return STATUS_NOT_FOUND;
        }
    );

    return CallGetBanSpeechTimeStamp;
}

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

BOOL Initialize2(PVOID BaseAddress)
{
    BOOL                        QQUINSpecified;
    NTSTATUS                    Status;
    PVOID                       module;
    ULONG_PTR                   CreateThreadIAT;
    PROCESS_BASIC_INFORMATION   BasicInfo;
    PLDR_MODULE                 Self, Netapi32;

    ml::MlInitialize();
    LdrDisableThreadCalloutsForDll(BaseAddress);

    Self = FindLdrModuleByHandle(nullptr);
    if (RtlEqualUnicodeString(&Self->BaseDllName, &USTR(L"QQ.exe"), TRUE) == FALSE)
        return TRUE;

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

    Mp::PATCH_MEMORY_DATA Function_user32[] =
    {
        Mp::FunctionJumpVa(LookupExportTable(module, USER32_SetWindowPos), QqSetWindowPos, &StubSetWindowPos),
        //EAT_HOOK_JUMP_HASH(module, USER32_ShowWindow,   QqShowWindow,   StubShowWindow),
        Mp::FunctionJumpVa(LookupExportTable(module, USER32_PostMessageW), QqPostMessageW, &StubPostMessageW)
    };


    /************************************************************************
      ntdll
    ************************************************************************/

    QQUINSpecified = InitializeUin();

    Mp::PATCH_MEMORY_DATA Function_ntdll[] =
    {
        Mp::FunctionJumpVa(QQUINSpecified ? NtOpenFile            : IMAGE_INVALID_VA, QqNtOpenFile,               &StubNtOpenFile),
        Mp::FunctionJumpVa(QQUINSpecified ? NtCreateFile          : IMAGE_INVALID_VA, QqNtCreateFile,             &StubNtCreateFile),
        Mp::FunctionJumpVa(QQUINSpecified ? NtQueryAttributesFile : IMAGE_INVALID_VA, QqNtQueryAttributesFile,    &StubNtQueryAttributesFile),
        Mp::FunctionJumpVa(NtQueryInformationProcess,                                 QqNtQueryInformationProcess,&StubNtQueryInformationProcess),
        //Mp::FunctionJumpVa(NtFreeVirtualMemory,                                       QqNtFreeVirtualMemory,      &StubNtFreeVirtualMemory),
    };


    /************************************************************************
      psapi
    ************************************************************************/

    module = Ldr::LoadDll(L"psapi.dll");

    Mp::PATCH_MEMORY_DATA Function_psapi[] =
    {
        Mp::FunctionJumpVa(LookupExportTable(module, PSAPI_GetModuleFileNameExW), QqGetModuleFileNameExW, &StubGetModuleFileNameExW),
    };


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

    Mp::PATCH_MEMORY_DATA Function_AppUtil[] =
    {
        Mp::FunctionJumpVa(LookupExportTable(module, "?ReportScanResult@Misc@Util@@YAHKVCTXStringW@@0@Z"),  ReportScanResult),
        Mp::FunctionJumpVa(LookupExportTable(module, "?PluginSecurityCheck@Misc@Util@@YAHXZ"),              PluginSecurityCheck),
        Mp::FunctionJumpVa(SearchAppUtil_CheckImportantModule(module),                                      CheckPluginList),
    };


    /************************************************************************
      Common
    ************************************************************************/

    module = Ldr::LoadDll(L"Common.dll");

    Mp::PATCH_MEMORY_DATA Function_Common[] =
    {
        Mp::FunctionJumpVa(LookupExportTable(module, "?IsTencentTrusted@Misc@Util@@YAHPB_W@Z"),            IsTencentTrusted),
        Mp::FunctionJumpVa(LookupExportTable(module, "?InitPluginFileSystem@Boot@Util@@YAHPA_W@Z"),        InitPluginFileSystem,   &StubInitPluginFileSystem),
        Mp::FunctionJumpVa(LookupExportTable(module, "?GetPlatformCore@Core@Util@@YAHPAPAUITXCore@@@Z"),   GetPlatformCore,        &StubGetPlatformCore),
    };


    /************************************************************************
      HummerEngine
    ************************************************************************/

    module = Ldr::LoadDll(L"HummerEngine.dll");

    CreateThreadIAT = IATLookupRoutineRVAByHashNoFix(module, KERNEL32_CreateThread);
    if (CreateThreadIAT != IMAGE_INVALID_RVA)
        CreateThreadIAT = PtrAdd(CreateThreadIAT, module);

    *(PVOID *)&HummerCreateThread = *(PVOID *)CreateThreadIAT;

    Mp::PATCH_MEMORY_DATA Patch_HummerEngine[] =
    {
        Mp::MemoryPatchVa((ULONG64)QqCreateWaitQQProtectThread, sizeof(PVOID), CreateThreadIAT),
    };


    /************************************************************************
      KernelUtil

        CF_Group_Image_TooManyImage
    ************************************************************************/

    Mp::PATCH_MEMORY_DATA Function_KernelUtil[] =
    {
        Mp::FunctionJumpVa(Util::Group::CheckMsgImage, CheckMsgImage, &StubCheckMsgImage),
        Mp::FunctionJumpVa(Util::Contact::IsSuperVip,  IsSuperVip,    &StubIsSuperVip),
    };


    /************************************************************************
      GroupApp
    ************************************************************************/

    BOOL AtAllGroupMemberFound, AtGroupMemberMaxFound;
    PVOID GetAdminFlag, GetUseTimes, AtGroupMemberMax;

    module = Ldr::LoadDll(L"GroupApp.dll");

    AtAllGroupMemberFound = SearchGroupApp_AtAllGroupMember(module, &GetAdminFlag, &GetUseTimes);
    AtGroupMemberMaxFound = SearchGroupApp_AtAllGroupMemberMax(module, &AtGroupMemberMax);

    Mp::PATCH_MEMORY_DATA Function_GroupApp[] =
    {
        Mp::FunctionJumpVa(AtAllGroupMemberFound ? GetUseTimes : IMAGE_INVALID_VA, GetAtAllGroupMemberUseTimes),
        Mp::FunctionCallVa(AtGroupMemberMaxFound ? AtGroupMemberMax : IMAGE_INVALID_VA, GetCurrentAtNumber),
        Mp::FunctionCallVa(SearchGroupApp_GroupBanSpeech(module), GetBanSpeechTimeStamp, &StubGetBanSpeechTimeStamp),
    };


    /************************************************************************
      AppMisc

        L"PluginListCheck"
        mov     eax, 0x80004005

        ShowPicInMultiPic begin
    ************************************************************************/

    module = Ldr::LoadDll(L"AppMisc.dll");

    Mp::PATCH_MEMORY_DATA Function_AppMisc[] =
    {
        Mp::FunctionJumpVa(SearchAppMisc_PluginListCheck(module),    CheckPluginList), // addition SetTimeOut
        Mp::FunctionJumpVa(SearchAppMisc_ShowPicInMultiPic(module),  ShowDBClickPicture, &StubShowDBClickPicture),
    };


    /************************************************************************
      MainFrame
    ************************************************************************/

    module = Ldr::LoadDll(L"MainFrame.dll");

    Mp::PATCH_MEMORY_DATA Function_MainFrame[] =
    {
        Mp::FunctionJumpVa(SearchMainFrame_SecurityFrame(module),    PopupSecurityFrame),
    };



    /************************************************************************
      ChatFrameApp

        L"exit for invalid version.17
    ************************************************************************/
/*
    module = Ldr::LoadDll(L"ChatFrameApp.dll");

    Mp::PATCH_MEMORY_DATA Function_ChatFrame[] =
    {
        //INLINE_HOOK_JUMP_RVA_NULL(0x93C3, IsTencentTrusted),
        INLINE_HOOK_JUMP_RVA_NULL(SearchChatFrame_CheckModule(module), IsTencentTrusted),
    };

*/


    /************************************************************************
      PreLogin
    ************************************************************************/

    module = Ldr::LoadDll(L"PreloginLogic.dll");

    Mp::PATCH_MEMORY_DATA Function_PreLogin[] =
    {
        //INLINE_HOOK_JUMP(SearchPreLogin_OnConnectionBroken(module), OnConnectionBroken, StubOnConnectionBroken),
        Mp::FunctionJumpVa(SearchPreLogin_OnSysDataCome(module), OnSysDataCome, &StubOnSysDataCome),
    };


    /************************************************************************
      end
    ************************************************************************/

    PATCH_ARRAY *Entry, Array[] =
    {
        { nullptr,  Patch_HummerEngine,     countof(Patch_HummerEngine)  },
        { nullptr,  Function_KernelUtil,    countof(Function_KernelUtil) },
        { nullptr,  Function_GroupApp,      countof(Function_GroupApp)   },
        { nullptr,  Function_AppUtil,       countof(Function_AppUtil)    },
        { nullptr,  Function_AppMisc,       countof(Function_AppMisc)    },
        { nullptr,  Function_MainFrame,     countof(Function_MainFrame)  },
        { nullptr,  Function_PreLogin,      countof(Function_PreLogin)   },
        { nullptr,  Function_Common,        countof(Function_Common)     },
        { nullptr,  Function_ntdll,         countof(Function_ntdll)      },
        { nullptr,  Function_psapi,         countof(Function_psapi)      },
        { nullptr,  Function_user32,        countof(Function_user32)     },
    };

    FOR_EACH_ARRAY(Entry, Array)
    {
        PVOID Base;

        Base = Entry->DllName == nullptr ? nullptr : Ldr::LoadDll(Entry->DllName);

        Mp::PatchMemory(Entry->PatchData, Entry->PatchCount, Base);
    }

    return TRUE;
}

BOOL Initialize(PVOID BaseAddress)
{
    auto Apc = [] (PVOID BaseAddress, PVOID, PVOID)
    {
        Initialize2(BaseAddress);
    };

    LdrDisableThreadCalloutsForDll(BaseAddress);

    return NT_SUCCESS(NtQueueApcThread(CurrentThread, Apc, BaseAddress, 0, 0));
}

BOOL WINAPI DllMain(PVOID BaseAddress, ULONG Reason, PVOID Reserved)
{
    switch (Reason)
    {
        case DLL_PROCESS_ATTACH:
            return Initialize2(BaseAddress) || UnInitialize(BaseAddress);

        case DLL_PROCESS_DETACH:
            UnInitialize(BaseAddress);
            break;
    }

    return TRUE;
}
