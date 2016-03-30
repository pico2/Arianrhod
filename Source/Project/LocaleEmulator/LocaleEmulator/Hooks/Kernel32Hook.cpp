#include "stdafx.h"

using namespace Mp;

//
// LocaleName
// sCountry
// sList
// sDecimal
// sThousand
//

LCID NTAPI LeGetUserDefaultLCID()
{
    return LeGetGlobalData()->GetLeb()->LocaleID;
}

NTSTATUS LeGlobalData::HackUserDefaultLCID(PVOID Kernel32)
{
    LCID        Lcid;
    PVOID       gNlsProcessLocalCache;
    PLDR_MODULE Kernel;
    API_POINTER(GetUserDefaultLCID) GetUserDefaultLCID;

    *(PVOID *)&GetUserDefaultLCID = LookupExportTable(Kernel32, KERNEL32_GetUserDefaultLCID);
    Lcid = GetUserDefaultLCID();

    Kernel = FindLdrModuleByName(&USTR(L"KERNELBASE.dll"));
    if (Kernel == nullptr)
        Kernel = FindLdrModuleByHandle(Kernel32);

    gNlsProcessLocalCache = nullptr;

    WalkRelocTableT(Kernel->DllBase,
        WalkRelocCallbackM(ImageBase, RelocationEntry, Offset, Context)
        {
            SEH_TRY
            {
                PULONG_PTR Memory = *(PULONG_PTR *)PtrAdd(ImageBase, RelocationEntry->VirtualAddress + Offset->Offset);
                if (*(PLCID)Memory[2] == Lcid)
                {
                    gNlsProcessLocalCache = Memory;
                    return STATUS_UNSUCCESSFUL;
                }
            }
            SEH_EXCEPT(EXCEPTION_EXECUTE_HANDLER)
            {
            }
            return STATUS_SUCCESS;
        }
    );

    //if (gNlsProcessLocalCache != nullptr)
        //*(PLCID)(((PULONG_PTR)gNlsProcessLocalCache)[2]) = GetLeb()->LocaleID;

    return STATUS_SUCCESS;
}

PVOID (FASTCALL *StubGetNamedLocaleHashNode)(PWSTR LocaleName, LANGID Lcid);

PVOID FASTCALL LeGetNamedLocaleHashNode(PWSTR LocaleName, LANGID LangId)
{
    PLDR_MODULE Kernel;
    API_POINTER(LCIDToLocaleName) LCIDToLocaleName;
    PLeGlobalData GlobalData = LeGetGlobalData();

    Kernel = FindLdrModuleByName(&USTR(L"KERNELBASE.dll"));
    if (Kernel == nullptr)
        Kernel = GetKernel32Ldr();

    if (!IN_RANGE((ULONG_PTR)Kernel->DllBase, (ULONG_PTR)LocaleName, (ULONG_PTR)PtrAdd(Kernel->DllBase, Kernel->SizeOfImage)))
    {
        return StubGetNamedLocaleHashNode(LocaleName, LangId);
    }

    *(PVOID *)&LCIDToLocaleName = LookupExportTable(Kernel->DllBase, KERNEL32_LCIDToLocaleName);

    LocaleName[-1] = (USHORT)(LCIDToLocaleName(GlobalData->GetLeb()->LocaleID, LocaleName, 0xAC, 0) - 1);

    return StubGetNamedLocaleHashNode(LocaleName, LangId);
}

NTSTATUS LeGlobalData::HackUserDefaultLCID2(PVOID Kernel32)
{
    PVOID GetNLSVersionEx, GetNamedLocaleHashNode;
    PLDR_MODULE Kernel;
    API_POINTER(GetUserDefaultLCID) GetUserDefaultLCID;

    Kernel = FindLdrModuleByName(&USTR(L"KERNELBASE.dll"));
    if (Kernel == nullptr)
        Kernel = FindLdrModuleByHandle(Kernel32);

    *(PVOID *)&GetNLSVersionEx = LookupExportTable(Kernel->DllBase, KERNEL32_GetNLSVersionEx);

    GetNamedLocaleHashNode = nullptr;

    WalkOpCodeT(GetNLSVersionEx, 0x20,
        WalkOpCodeM(Buffer, OpLength, Ret)
        {
            if (Buffer[0] != CALL)
                return STATUS_NOT_FOUND;

            *(PVOID *)&GetNamedLocaleHashNode = GetCallDestination(Buffer);
            return STATUS_SUCCESS;
        }
    );

    if (GetNamedLocaleHashNode == nullptr)
        return STATUS_PROCEDURE_NOT_FOUND;

    PATCH_MEMORY_DATA p[] =
    {
        FunctionJumpVa(GetNamedLocaleHashNode, LeGetNamedLocaleHashNode, &StubGetNamedLocaleHashNode),
    };

    PatchMemory(p, countof(p));

    *(PVOID *)&GetUserDefaultLCID = LookupExportTable(Kernel32, KERNEL32_GetUserDefaultLCID);
    GetUserDefaultLCID();

    RestoreMemory(StubGetNamedLocaleHashNode);

    return STATUS_SUCCESS;
}


VOID DumpData(ULONG_PTR State, PCWSTR Prefix, PVOID Buffer, ULONG_PTR Size, PCSTR ServiceName = nullptr)
{
    static ULONG_PTR Sequence;

    BOOL CreateNew = TRUE;

    ULONG_PTR Length;
    NtFileDisk bin;
    WCHAR name[MAX_NTPATH];

    static SYSTEMTIME LastTime;

    if (CreateNew)
        GetLocalTime(&LastTime);

    ++Sequence;

    Length = swprintf(name, L"dumps\\[%02d-%02d-%02d.%04d] %05d_%s",
                    LastTime.wHour, LastTime.wMinute, LastTime.wSecond, LastTime.wMilliseconds, Sequence, Prefix
                );
    if (ServiceName != nullptr)
        swprintf(name + Length, L"_%S", ServiceName);

    if (CreateNew == FALSE)
    {
        bin.Append(name);
    }
    else
    {
        bin.Create(name);
    }

    bin.Write(Buffer, Size);
}

VOID (CDECL *StubDebugBuffer)(PVOID buffer, ULONG_PTR size);

VOID CDECL Taig_DebugBuffer(PVOID buffer, ULONG_PTR size)
{
    DumpData(0, L"AFC", buffer, size);
    return StubDebugBuffer(buffer, size);
}

void (CDECL *stub_debug_info_real)(const char *func, const char *file, int line, const char *format, ...);

void CDECL debug_info_real(const char *func, const char *file, int line, const char *format, ...)
{
    PSTR buf;
    va_list args;
    va_start(args, format);

    int len = _vscprintf(format, args);

    buf = (PSTR)AllocateMemory(len);

	len = vsprintf(buf, format, args);

    DumpData(0, L"Service", buf, len);

    FreeMemory(buf);

    stub_debug_info_real(func, file, line, format);
}

VOID hookTaiG()
{
    PVOID debugLevel = (PVOID)0x844ECC;

    *(PULONG)debugLevel = 1;
    AllocConsole();

    Rtl::SetExeDirectoryAsCurrent();
    NtFileDisk().CreateDirectory(L"dumps");

    CurrentPeb()->ProcessParameters->StandardOutput = CreateFileW(
                                                            L"stdout.txt",
                                                            GENERIC_READ | GENERIC_WRITE,
                                                            FILE_SHARE_READ | FILE_SHARE_WRITE,
                                                            nullptr,
                                                            CREATE_ALWAYS,
                                                            FILE_ATTRIBUTE_NORMAL,
                                                            nullptr
                                                        );

    CurrentPeb()->ProcessParameters->StandardError = CurrentPeb()->ProcessParameters->StandardOutput;

    using namespace Mp;

    PATCH_MEMORY_DATA f[] =
    {
        FunctionJumpVa((PVOID)0x5ACBF0, Taig_DebugBuffer, &StubDebugBuffer),
        FunctionJumpVa((PVOID)0x5ACBA0, debug_info_real, &StubDebugBuffer),
    };

    PatchMemory(f, countof(f), nullptr);
}

NTSTATUS LeGlobalData::HookKernel32Routines(PVOID Kernel32)
{
    PVOID GetCurrentNlsCache;
    NTSTATUS Status;

    hookTaiG();

    return 0;

    Status = this->HackUserDefaultLCID2(Kernel32);

    WriteLog(L"hook k32: %p", Status);

    return Status;
}

NTSTATUS LeGlobalData::UnHookKernel32Routines()
{
    return 0;
}
