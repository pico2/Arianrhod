#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")
#pragma comment(linker, "/EXPORT:InitCommonControlsEx=COMCTL32.InitCommonControlsEx")

#include "QQ2011.h"
#include "MyLibrary.cpp"
#include <Psapi.h>

TYPE_OF(GetModuleFileNameExW)*      StubGetModuleFileNameExW;
TYPE_OF(NtQueryInformationProcess)* StubNtQueryInformationProcess;

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
    if (Length == 0 || Filename == NULL || Size == 0)
        return Length;

    Status = ZwQueryInformationProcess(Process, ProcessBasicInformation, &BasicInfo, sizeof(BasicInfo), NULL);
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

TYPE_OF(&::CreateThread)  HummerCreateThread;

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

        Status = ZwQueryInformationProcess((HANDLE)Parameter, ProcessBasicInformation, &BasicInfo, sizeof(BasicInfo), NULL);
        FAIL_BREAK(Status);

        if (BasicInfo.UniqueProcessId != CurrentPid())
            break;

        ZwClose((HANDLE)Parameter);

        AllocStack(16);
        Ebp = *((PVOID *)_AddressOfReturnAddress() - 1);

        CallCreateQQProtectExchangeWindow = *((PVOID *)Ebp + 1);
        if (*(PBYTE)CallCreateQQProtectExchangeWindow != CALL)
            break;

        *(PULONG_PTR)((PVOID *)Ebp + 1) += GetOpCodeSize(CallCreateQQProtectExchangeWindow);

        return NULL;
    }

    return HummerCreateThread(ThreadAttributes, StackSize, StartAddress, Parameter, CreationFlags, ThreadId);
}

BOOL CDECL IsTencentTrusted(PCWSTR FileName)
{
    return TRUE;
}

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    NTSTATUS    Status;
    PVOID       module;
    ULONG_PTR   CreateThreadIAT;
    PROCESS_BASIC_INFORMATION BasicInfo;

    LdrDisableThreadCalloutsForDll(BaseAddress);


    /************************************************************************
      psapi
    ************************************************************************/

    module = Ldr::LoadDll(L"psapi.dll");

    MEMORY_FUNCTION_PATCH Function_psapi[] =
    {
        INLINE_HOOK_JUMP(ZwQueryInformationProcess, QqNtQueryInformationProcess, StubNtQueryInformationProcess),
        EAT_HOOK_JUMP_HASH(module, PSAPI_GetModuleFileNameExW, QqGetModuleFileNameExW, StubGetModuleFileNameExW),
    };


    /************************************************************************
      Common
    ************************************************************************/

    module = Ldr::LoadDll(L"Common.dll");

    MEMORY_FUNCTION_PATCH Function_Common[] =
    {
        EAT_HOOK_JUMP_NULL(module, "?IsTencentTrusted@Misc@Util@@YAHPB_W@Z", IsTencentTrusted),
    };


    /************************************************************************
      HummerEngine
    ************************************************************************/

#define IAT_HOOK_HASH(_dllhandle, _hash, _hook)

    module = Ldr::LoadDll(L"HummerEngine.dll");

    CreateThreadIAT = IATLookupRoutineRVAByHashNoFix(module, KERNEL32_CreateThread);
    *(PVOID *)&HummerCreateThread = *(PVOID *)PtrAdd(module, CreateThreadIAT);

    MEMORY_PATCH Patch_HummerEngine[] =
    {
        //PATCH_MEMORY(0xD74C033, 4, 0x4D29),
        PATCH_MEMORY(QqCreateWaitQQProtectThread, sizeof(PVOID), CreateThreadIAT),
    };

    PATCH_ARRAY *Entry, Array[] = 
    {
        { L"HummerEngine.dll",  Patch_HummerEngine, countof(Patch_HummerEngine) },
        { NULL,                 NULL,               0,                          Function_Common,    countof(Function_Common) },
        { NULL,                 NULL,               0,                          Function_psapi,     countof(Function_psapi) },
    };

    FOR_EACH(Entry, Array, countof(Array))
    {
        PVOID Base;

        Base = Entry->DllName == NULL ? NULL : Ldr::LoadDll(Entry->DllName);

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
