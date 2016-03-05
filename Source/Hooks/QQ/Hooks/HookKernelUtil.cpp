#include "Hooks.h"

TYPE_OF(Util::Group::CheckMsgImage) StubCheckMsgImage;
TYPE_OF(Util::Contact::IsSuperVip)  StubIsSuperVip;
TYPE_OF(Version::Init)              StubVersionInit;
API_POINTER(CreateProcessInternalW) StubCreateProcessInternalW;

BOOL CDECL CheckMsgImage(PVOID GroupObject, CTXStringW &Message)
{
    BOOL Success;

    Success = StubCheckMsgImage(GroupObject, Message);

    if (!Success && !Message.IsEmpty())
    {
        if (wcsstr(Message.Buffer, L"·¢ËÍ") != nullptr)
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

BOOL CDECL Version_Init()
{
    BOOL success;
    PLDR_MODULE self;
    UNICODE_STRING FullDllName;
    ml::String FullPath;
    PVOID cookie;

    LdrLockLoaderLock(0, nullptr, &cookie);

    self = FindLdrModuleByHandle(nullptr);
    FullDllName = self->FullDllName;
    FullPath = FullDllName;
    FullPath = FullPath.Replace(L"QQ2.exe", L"QQ.exe");

    self->FullDllName = FullPath;

    success = StubVersionInit();

    self->FullDllName = FullDllName;

    LdrUnlockLoaderLock(0, cookie);

    return success;
}

BOOL
NTAPI
QqCreateProcessInternalW(
    HANDLE                  Token,
    PCWSTR                  ApplicationName,
    PWSTR                   CommandLine,
    LPSECURITY_ATTRIBUTES   ProcessAttributes,
    LPSECURITY_ATTRIBUTES   ThreadAttributes,
    BOOL                    InheritHandles,
    DWORD                   CreationFlags,
    LPVOID                  Environment,
    PCWSTR                  CurrentDirectory,
    LPSTARTUPINFOW          StartupInfo,
    LPPROCESS_INFORMATION   ProcessInformation,
    PHANDLE                 NewToken
)
{
    ml::String appName, cmdLine;

    if (RtlEqualUnicodeString(&FindLdrModuleByHandle(nullptr)->BaseDllName, &USTR(L"QQ2.exe"), TRUE))
    {
        if (ApplicationName != nullptr)
        {
            appName = ApplicationName;
            if (appName.IndexOf(L"QQ.exe") != appName.kInvalidIndex)
                appName = appName.Replace(L"QQ.exe", L"QQ2.exe");

            ApplicationName = appName;
        }

        if (CommandLine != nullptr)
        {
            cmdLine = CommandLine;

            if (cmdLine.IndexOf(L"QQ.exe") != cmdLine.kInvalidIndex)
            {
                cmdLine = cmdLine.Replace(L"QQ.exe", L"QQ2.exe");
            }
            else if (cmdLine.IndexOf(L"QQExternal.exe") != cmdLine.kInvalidIndex)
            {
                cmdLine = cmdLine.Replace(L"--high-dpi-support=1", L"--high-dpi-support=0");
            }

            CommandLine = cmdLine;
        }
    }

    return StubCreateProcessInternalW(
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
            );
}

NTSTATUS HookKernelUtil(PVOID BaseAddress)
{
    /************************************************************************
      KernelUtil

        CF_Group_Image_TooManyImage
    ************************************************************************/

    Mp::PATCH_MEMORY_DATA Function_KernelUtil[] =
    {
        Mp::FunctionJumpVa(Util::Group::CheckMsgImage,  CheckMsgImage, &StubCheckMsgImage),
        Mp::FunctionJumpVa(Util::Contact::IsSuperVip,   IsSuperVip,    &StubIsSuperVip),
        Mp::FunctionJumpVa(Version::Init,               Version_Init,  &StubVersionInit),
        Mp::FunctionJumpVa(LookupExportTable(FindLdrModuleByName(PUSTR(L"KERNELBASE.dll"))->DllBase, KERNEL32_CreateProcessInternalW), QqCreateProcessInternalW,  &StubCreateProcessInternalW),
    };

    return Mp::PatchMemory(Function_KernelUtil, countof(Function_KernelUtil), BaseAddress);
}
