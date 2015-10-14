#include "Hooks.h"
#include <Psapi.h>

using namespace Mp;

API_POINTER(GetModuleFileNameExW) StubGetModuleFileNameExW;

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

NTSTATUS HookPsapi(PVOID BaseAddress)
{
    PATCH_MEMORY_DATA Function_psapi[] =
    {
        FunctionJumpVa(LookupExportTable(BaseAddress, PSAPI_GetModuleFileNameExW), QqGetModuleFileNameExW, &StubGetModuleFileNameExW),
    };

    return PatchMemory(Function_psapi, countof(Function_psapi), BaseAddress);
}