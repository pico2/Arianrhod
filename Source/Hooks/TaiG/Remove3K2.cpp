#include "TaiG2.h"
#include <DbgHelp.h>

//#pragma comment(linker, "/EXPORT:MiniDumpWriteDump=_StMiniDumpWriteDump@28")

NAKED VOID SetDebEntry()
{
    INLINE_ASM
    {
        mov     byte ptr [esi+0xA02], 0x1;
        mov     eax, dword ptr [ebp-0xDC];
        cmp     eax, 1;
        or      eax, eax;
        je      IS_CYDIA;

        xor     eax, eax;
        mov     byte ptr [esi+0xA02], al;   // Selected

IS_CYDIA:
        ret;
    }
}

BOOL CDECL IsJailbroken2(HANDLE Device)
{
    RtlSetLastWin32Error(0xE8000022);
    return FALSE;
}

PVOID NTAPI TgLoadLibrary(PCSTR Library)
{
    PVOID base = LoadLibraryA(Library);
    using namespace Mp;

    {
        PATCH_MEMORY_DATA p[] =
        {
            FunctionJumpRva(0xF340, IsJailbroken2),
            MemoryPatchRva("com.saurik.Cybia", 16, 0x652FC),
        };

        PatchMemory(p, countof(p), base);
    }

    return base;
}

API_POINTER(MiniDumpWriteDump) DbghlpMiniDumpWriteDump;

VOID InitializeDbghelp()
{
    if (DbghlpMiniDumpWriteDump != nullptr)
        return;

    PVOID module;
    PLDR_MODULE self, dbghlp;
    ml::String path;

    Rtl::GetModuleDirectory(path, GetNtdllHandle());

    path += L"dbghelp.dll";

    module = Ldr::LoadDll(path);
    if (module == nullptr)
        return;

    *(PVOID *)&DbghlpMiniDumpWriteDump = GetRoutineAddress(module, "MiniDumpWriteDump");

    self = FindLdrModuleByHandle(&__ImageBase);
    dbghlp = FindLdrModuleByHandle(module);

    self->DllBase = dbghlp->DllBase;
    self->EntryPoint = dbghlp->EntryPoint;
    self->SizeOfImage = dbghlp->SizeOfImage;
}

API_POINTER(CreateFileW) StubCreateFileW;

HANDLE
WINAPI
TgCreateFileW(
    PCWSTR                  FileName,
    ULONG                   DesiredAccess,
    ULONG                   ShareMode,
    LPSECURITY_ATTRIBUTES   SecurityAttributes,
    ULONG                   CreationDisposition,
    ULONG                   FlagsAndAttributes,
    HANDLE                  TemplateFile
)
{
    if (_ReturnAddress() == PtrAdd(GetExeModuleHandle(), 0x92FED74))
    {
        RtlSetLastWin32Error(ERROR_ACCESS_DENIED);
        return INVALID_HANDLE_VALUE;
    }

    return StubCreateFileW(FileName, DesiredAccess, ShareMode, SecurityAttributes, CreationDisposition, FlagsAndAttributes, TemplateFile);
}

static NTSTATUS Initialize2()
{
    using namespace Mp;
/*

    PBYTE buf;

    buf = (PBYTE)AllocateMemory(0x100);
    AllocConsole();
    for (int i = 0; i != 0x100; ++i)
    {
        PrintConsole(L"%02X ", buf[i]);
    }

    FreeMemory(buf);
*/

    {
        PATCH_MEMORY_DATA p[] =
        {
            //MemoryPatchRva(0x00ull, 4, 0x15EB2),
            //FunctionCallRva(0x1533B, TgLoadLibrary),
            FunctionCallRva(0x15E71, SetDebEntry),  // 2.0 2.1
            MemoryPatchRva(0x80, 1, 0x1A423),       // jo
        };

        PatchMemory(p, countof(p), GetExeModuleHandle());
    }

    return STATUS_SUCCESS;
}

API_POINTER(CreateMutexW) StubCreateMutexW;

HANDLE
NTAPI
TgCreateMutexW(
    LPSECURITY_ATTRIBUTES   MutexAttributes,
    BOOL                    InitialOwner,
    PCWSTR                  Name
)
{
    HANDLE Mutex;

    Mutex = StubCreateMutexW(MutexAttributes, InitialOwner, Name);

    if (RtlGetLastWin32Error() == ERROR_ALREADY_EXISTS)
        return Mutex;

    if (Name != nullptr && StrICompareW(Name, L"TaiG_Mutex") == 0)
    {
        Initialize2();
    }

    return Mutex;
}

NTSTATUS Remove3K2_Initialize(PVOID TaiGBase)
{
    using namespace Mp;

    static CHAR VersionDll[] = "VERSION.dll";

    PVOID Kernel32 = GetKernel32Handle();

    {
        PATCH_MEMORY_DATA p[] =
        {
            //MemoryPatchRva(0x00ull, 4, 0x15EB2),
            //FunctionCallRva(0x1533B, TgLoadLibrary),
            //FunctionCallRva(0x15E71, SetDebEntry),  // 2.0 2.1
            //MemoryPatchRva(0x80, 1, 0x1A423),       // jo
            MemoryPatchRva(VersionDll, sizeof(VersionDll), 0x475DC9D),
            FunctionJumpVa(LookupExportTable(Kernel32, KERNEL32_CreateFileW), TgCreateFileW, &StubCreateFileW),
            FunctionJumpVa(LookupExportTable(Kernel32, KERNEL32_CreateMutexW), TgCreateMutexW, &StubCreateMutexW),
        };

        PatchMemory(p, countof(p), GetExeModuleHandle());
    }

    return STATUS_SUCCESS;
}
