#define AUTHOR_NAME "Amano"
#define SECTION_NAME "."AUTHOR_NAME

#define _WIN32_WINNT 0x601

#pragma comment(linker,"/ENTRY:main2")
#pragma comment(linker,"/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker, "/SECTION:"SECTION_NAME",ERW /MERGE:.text="SECTION_NAME)
#pragma warning(disable:4995 4273)

#ifndef UNICODE
    #define UNICODE
#endif

#ifndef _UNICODE
    #define _UNICODE
#endif

#define  _DECL_DLLMAIN

#include <ws2spi.h>
#include "MyLibrary.cpp"

#if defined(UNICODE)
    #define __WSTRING(str) L##str
    #define WSTRING(str) __WSTRING(str)
#else
    #define WSTRING(str) (str)
#endif

// OVERLOAD_CPP_NEW_WITH_HEAP(MemoryAllocator::GetGlobalHeap())

#include "../Drivers/AntiAntiKernelDebug/ShadowSysCall.h"

ULONG GetBitSetCount(ULONG Value)
{
    Value -= ((Value >> 1) & 0x55555555);
    Value  = (((Value >> 2) & 0x33333333) + (Value & 0x33333333));
    Value  = (((Value >> 4) + Value) & 0x0F0F0F0F);
    Value += (Value >> 8);
    Value += (Value>>16);
    Value &= 0x3F;

    return Value;
}

NTSTATUS MapNtdll(HANDLE Process)
{
    NTSTATUS            Status;
    SIZE_T              ViewSize;
    HANDLE              FileHandle, SectionHandle;
    PVOID               NtdllModule;
    OBJECT_ATTRIBUTES   ObjectAttributes;
    UNICODE_STRING      NtPath;
    IO_STATUS_BLOCK     IoStatus;
    PVOID BaseAddress;

    BaseAddress = NULL;

    RtlDosPathNameToNtPathName_U(GetNtdllLdrModule()->FullDllName.Buffer, &NtPath, NULL, NULL);
    InitializeObjectAttributes(&ObjectAttributes, &NtPath, OBJ_CASE_INSENSITIVE, NULL, NULL);
    Status = NtCreateFile(
                &FileHandle,
                GENERIC_READ | SYNCHRONIZE | FILE_READ_ATTRIBUTES,
                &ObjectAttributes,
                &IoStatus,
                NULL,
                FILE_ATTRIBUTE_NORMAL,
                FILE_SHARE_READ,
                FILE_OPEN,
                FILE_SYNCHRONOUS_IO_ALERT | FILE_OPEN_FOR_BACKUP_INTENT,
                NULL,
                0
             );
    RtlFreeUnicodeString(&NtPath);
    if (!NT_SUCCESS(Status))
        return Status;

    Status = NtCreateSection(
                &SectionHandle,
                GENERIC_READ,
                NULL,
                NULL,
                PAGE_READONLY,
                SEC_IMAGE,
                FileHandle
             );

    NtClose(FileHandle);
    if (!NT_SUCCESS(Status))
        return Status;

    ViewSize = 0;
    Status = NtMapViewOfSection(
                SectionHandle,
                Process,
                &BaseAddress,
                0,
                0,
                NULL,
                &ViewSize,
                ViewShare,
                0,
                PAGE_READONLY
             );

    NtUnmapViewOfSection(Process, BaseAddress);

    NtClose(SectionHandle);

    return Status;
}

ULONG NTAPI StubThread(PVOID)
{
    return NtTerminateThread(NtCurrentThread(), 0);
}

#if !ML_AMD64

ULONG NTAPI UnMapSectionThread(HANDLE Thread)
{
    MapNtdll(NtCurrentProcess());

    SEH_TRY
    {
        INLINE_ASM int 3;
    }
    SEH_EXCEPT(EXCEPTION_EXECUTE_HANDLER)
    {
    }

//    NtResumeThread(Thread, NULL);
//    NtClose(Thread);

    if (NT_SUCCESS(Nt_CreateThread(StubThread, NULL, FALSE, NtCurrentProcess(), &Thread)))
    {
        NtWaitForSingleObject(Thread, TRUE, NULL);
        NtClose(Thread);
    }

    return NtTerminateProcess(NtCurrentProcess(), 0);
}

#endif // amd64

#if !ML_AMD64

NAKED VOID X64_Mode_Start()
{
    INLINE_ASM
    {
        push    [esp];
        mov     dword ptr [esp + 4], 33h;
        retf;
    }
}

NAKED VOID X64_Mode_End()
{
    INLINE_ASM
    {
        mov     dword ptr [esp + 4], 23h;
        retf;
    }
}

typedef LARGE_INTEGER LARGE_POINTER;

#define PUSH_R8 _asm __emit 0x41 _asm __emit 0x50
#define PREFIX_44 _asm __emit 0x44 _asm
#define PREFIX_48 _asm __emit 0x48 _asm
#define PREFIX_4C _asm __emit 0x4C _asm

NAKED
LARGE_POINTER
STDCALL
Nt_LoadLibraryWow64(
    PUNICODE_STRING64   LibraryPath,
    PVOID               LdrLoadDll64
)
{
    INLINE_ASM
    {
        call X64_Mode_Start;

        push ebp;                                   // push rbp

        PREFIX_48 mov ebp, esp;                     // mov rbp, rsp
        PREFIX_48 and esp, -10h;                    // and rsp, -10h
        PREFIX_48 add esp, -20h;                    // shadow space

        PREFIX_48 xor edx, edx;                     // xor rdx, rdx                 Flags
        PREFIX_48 xor ecx, ecx;                     // xor rcx, rcx                 PathToFile
        PREFIX_44 mov eax, dword ptr [ebp+0Ch];     // mov r8d, [rbp+0Ch]           LibraryPath
        mov     eax, [ebp + 10h];                   //                              LdrLoadDll64
        push    ecx;                                // sub rsp, 4
        PREFIX_4C lea ecx, dword ptr [esp];         // lea r9, [rsp]                ModuleHandle
        call    eax;                                //                              LdrLoadDll
        pop     eax;                                // pop rax
        PREFIX_48 mov edx, eax;                     // mov rdx, rax
        PREFIX_48 shr edx, 32;                      // shr rdx, 32

        PREFIX_48 mov esp, ebp;                     // mov rsp, rbp
        pop ebp;                                    // pop rbp

        call X64_Mode_End;

        ret 8;
    }
}

NAKED VOID FASTCALL Callx64Routine(PVOID Routine, PVOID Parameter)
{
    INLINE_ASM
    {
        call X64_Mode_Start;

        push ebp;

        PREFIX_48 mov ebp, esp;
        PREFIX_48 and esp, -16;
        PREFIX_48 add esp, -100h;
        PREFIX_48 mov eax, ecx;
        PREFIX_48 mov ecx, edx;

        call eax;

        PREFIX_48 mov esp, ebp;
        pop ebp;

        call X64_Mode_End;

        ret;
    }
}

PVOID Findx64NtdllBase()
{
    HANDLE                              Process;
    NTSTATUS                            Status;
    PVOID                               Wow64Ntdll, BaseAddress, LastAllocationBase;
    SYSTEM_BASIC_INFORMATION            SystemBasic;
    MEMORY_BASIC_INFORMATION            MemoryBasic;
    MEMORY_MAPPED_FILENAME_INFORMATION2 MappedFile;

    Wow64Ntdll = GetNtdllHandle();

    NtQuerySystemInformation(SystemBasicInformation, &SystemBasic, sizeof(SystemBasic), NULL);

    Process = NtCurrentProcess();
    LastAllocationBase = (PVOID)IMAGE_INVALID_RVA;
    BaseAddress = (PVOID)SystemBasic.MinimumUserModeAddress;

    for (; (ULONG_PTR)BaseAddress < SystemBasic.MaximumUserModeAddress; BaseAddress = PtrAdd(BaseAddress, MemoryBasic.RegionSize))
    {
        MemoryBasic.RegionSize = MEMORY_PAGE_SIZE;
        Status = NtQueryVirtualMemory(Process, BaseAddress, MemoryBasicInformation, &MemoryBasic, sizeof(MemoryBasic), NULL);
        FAIL_CONTINUE(Status);

        BaseAddress = MemoryBasic.BaseAddress;

        if (MemoryBasic.Type != MEM_IMAGE || MemoryBasic.AllocationBase == LastAllocationBase)
            continue;

        LastAllocationBase = MemoryBasic.AllocationBase;
        if (LastAllocationBase == Wow64Ntdll)
            continue;

        Status = NtQueryVirtualMemory(Process, BaseAddress, MemoryMappedFilenameInformation, &MappedFile, sizeof(MappedFile), NULL);
        if (!NT_SUCCESS(Status) || MappedFile.Name.Length == 0)
            continue;

        if (!StrICompareW(findnamew(MappedFile.Name.Buffer), L"ntdll.dll"))
            return LastAllocationBase;
    }

    return NULL;
}

BOOL FuckX64Ntdll(PVOID ntdll)
{
    BYTE LdrpLdrDatabaseIsSetupHeader[] = { 0x48, 0x89, 0x11, 0x48, 0x89, 0x41, 0x08, 0x48, 0x89, 0x08, 0x48, 0x89 };
    BYTE LdrpLdrDatabaseIsSetupCmpHeader[] = { 0x80, 0x3D };
    BYTE LdrpLdrDatabaseIsSetupCmpTailAndJzHeader[] = { 0x00, 0x0F, 0x84 };

    SEARCH_PATTERN_DATA LdrpLdrDatabaseIsSetupPattern[] =
    {
        ADD_PATTERN(LdrpLdrDatabaseIsSetupHeader,               PATTERN_AUTO_SEARCH),
        ADD_PATTERN_F(LdrpLdrDatabaseIsSetupCmpHeader,          PATTERN_AUTO_SEARCH, 0, 0x11),
        ADD_PATTERN_F(LdrpLdrDatabaseIsSetupCmpTailAndJzHeader, PATTERN_AUTO_SEARCH, 0, 0x06),
    };

    NTSTATUS                Status;
    PBOOLEAN                LdrpLdrDatabaseIsSetup;
    ULONG                   Protect, SectionCount;
    PIMAGE_DOS_HEADER       DosHeader;
    PIMAGE_NT_HEADERS64     NtHeaders;
    PIMAGE_SECTION_HEADER   Section;

    DosHeader   = (PIMAGE_DOS_HEADER)ntdll;
    NtHeaders   = (PIMAGE_NT_HEADERS64)PtrAdd(DosHeader, DosHeader->e_lfanew);
    Section     = (PIMAGE_SECTION_HEADER)PtrAdd(&NtHeaders->OptionalHeader, NtHeaders->FileHeader.SizeOfOptionalHeader);

    LdrpLdrDatabaseIsSetup = (PBOOLEAN)SearchPattern(
                                LdrpLdrDatabaseIsSetupPattern,
                                countof(LdrpLdrDatabaseIsSetupPattern),
                                PtrAdd(ntdll, Section->VirtualAddress),
                                Section->Misc.VirtualSize
                             );

    if (LdrpLdrDatabaseIsSetup == NULL)
        return FALSE;

    LdrpLdrDatabaseIsSetup = PtrAdd(LdrpLdrDatabaseIsSetup, 0x12);
    LdrpLdrDatabaseIsSetup = GetCallDestination(LdrpLdrDatabaseIsSetup) + 1;

    for (SectionCount = NtHeaders->FileHeader.NumberOfSections - 1; SectionCount != 0; --SectionCount)
    {
        ++Section;
        if (!StrNCompareA((PSTR)Section->Name, ".rdata", countof(Section->Name)))
            break;
    }

    if (SectionCount == 0)
        return FALSE;

    PWSTR LdrpKernel32DllNameBuffer;

    SEARCH_PATTERN_DATA LdrpKernel32DllNamePattern[] =
    {
        ADD_PATTERN(L"KERNEL32.DLL"),
    };

    LdrpKernel32DllNameBuffer = (PWSTR)SearchPattern(
                                    LdrpKernel32DllNamePattern,
                                    countof(LdrpKernel32DllNamePattern),
                                    PtrAdd(ntdll, Section->VirtualAddress),
                                    Section->Misc.VirtualSize
                                );

    if (LdrpKernel32DllNameBuffer == NULL)
        return FALSE;

    Status = Nt_ProtectMemory(NtCurrentProcess(), LdrpKernel32DllNameBuffer, sizeof(*LdrpKernel32DllNameBuffer), PAGE_READWRITE, &Protect);
    if (!NT_SUCCESS(Status))
        return FALSE;

    LdrpKernel32DllNameBuffer[0] = 0;
    if (Protect != PAGE_READWRITE)
        Nt_ProtectMemory(NtCurrentProcess(), LdrpKernel32DllNameBuffer, sizeof(*LdrpKernel32DllNameBuffer), Protect, &Protect);

    *LdrpLdrDatabaseIsSetup = TRUE;

    return TRUE;
}

#endif // ML_AMD64

#include "../ShimEngine/BypassUACDriver/DriverHelper.h"

typedef struct
{
    ULONG_PTR   IconIndex;
    HRSRC       Resource;

} LOAD_ICON_PARAM, *PLOAD_ICON_PARAM;

BOOL CALLBACK LoadPeIconEnumResProc(HMODULE hModule, LPCTSTR lpszType, LPTSTR lpszName, PLOAD_ICON_PARAM lParam)
{
    if (lParam->IconIndex-- != 0)
        return TRUE;

    lParam->Resource = FindResourceExW(hModule, lpszType, lpszName, MAKELANGID(LANG_NEUTRAL, SUBLANG_NEUTRAL));

    return FALSE;
}

NTSTATUS
LoadIconFromPePrivate(
    HMODULE     Module,
    ULONG_PTR   IconIndex,
    PVOID*      IcoBuffer,
    PULONG_PTR  IcoSize
)
{
    PVOID                   Buffer;
    ULONG_PTR               IconCount, Offset, Size, HeaderSize;
    PGROUP_ICON_ENTRY       GroupIconEntry;
    PGROUP_ICON             GroupIcon;
    PIMAGE_ICO_HEADER       IcoHeader;
    PIMAGE_ICO_IMAGE_ENTRY  IcoEntry;
    LOAD_ICON_PARAM         Param;

    Param.Resource = NULL;
    Param.IconIndex = IconIndex;

    EnumResourceNamesW(Module, RT_GROUP_ICON, (ENUMRESNAMEPROCW)LoadPeIconEnumResProc, (LONG_PTR)&Param);
    if (Param.Resource == NULL)
        return STATUS_UNSUCCESSFUL;

    GroupIcon = (PGROUP_ICON)LockResource(LoadResource(Module, Param.Resource));

    IconCount = GroupIcon->Count;
    IcoHeader = (PIMAGE_ICO_HEADER)AllocateMemoryP(IconCount * sizeof(IcoHeader->Entry) + RTL_SIZEOF_THROUGH_FIELD(IMAGE_ICO_HEADER, NumberOfImage));
    if (IcoHeader == NULL)
        return STATUS_NO_MEMORY;

    IcoHeader->Reserve = 0;
    IcoHeader->FileType = 1;
    IcoHeader->NumberOfImage = IconCount;

    IcoEntry = IcoHeader->Entry;

    Offset = PtrOffset(IcoEntry + IconCount, IcoHeader);
    HeaderSize = Offset;

    GroupIconEntry = GroupIcon->Entries;
    FOR_EACH(GroupIconEntry, GroupIconEntry, IconCount)
    {
        IcoEntry->Width = GroupIconEntry->Width;
        IcoEntry->Height = GroupIconEntry->Height;
        IcoEntry->NumberOfColorInPalette = GroupIconEntry->ColorCount;
        IcoEntry->Reserve = 0;

        IcoEntry->Ico.Planes = GroupIconEntry->Planes;
        IcoEntry->Ico.BitsPerPixel = GroupIconEntry->BitCount;

        IcoEntry->ImageOffset = Offset;
        IcoEntry->ImageSize = GroupIconEntry->BytesInRes;

        Offset += IcoEntry->ImageSize;

        ++IcoEntry;
    }

    Size = Offset;
    Buffer = AllocateMemoryP(Size);
    if (Buffer == NULL)
    {
        FreeMemoryP(IcoHeader);
        return STATUS_NO_MEMORY;
    }

    *IcoBuffer = Buffer;
    *IcoSize = Size;

    CopyMemory(Buffer, IcoHeader, HeaderSize);

    Buffer = PtrAdd(Buffer, HeaderSize);
    GroupIconEntry = GroupIcon->Entries;
    FOR_EACH(GroupIconEntry, GroupIconEntry, IconCount)
    {
        Param.Resource = FindResourceExW(Module, RT_ICON, MAKEINTRESW(GroupIconEntry->ID), 0);
        if (Param.Resource == NULL)
            break;

        Size = GroupIconEntry->BytesInRes;
        CopyMemory(Buffer, LockResource(LoadResource(Module, Param.Resource)), Size);
        Buffer = PtrAdd(Buffer, Size);
    }

    FreeMemoryP(IcoHeader);

    if (Param.Resource == NULL)
    {
        FreeMemoryP(*IcoBuffer);
        *IcoBuffer = NULL;

        return STATUS_NO_MEMORY;
    }

    return STATUS_SUCCESS;;
}

NTSTATUS
LoadIconFromPe(
    PWSTR       File,
    ULONG_PTR   IconIndex,
    PVOID*      IcoBuffer,
    PULONG_PTR  IcoSize
)
{
    HMODULE mod;
    NTSTATUS st;

    mod = LoadLibraryExW(File, NULL, LOAD_LIBRARY_AS_DATAFILE | LOAD_LIBRARY_AS_IMAGE_RESOURCE);
    if (mod == NULL)
        return STATUS_UNSUCCESSFUL;

    st = LoadIconFromPePrivate(mod, IconIndex, IcoBuffer, IcoSize);

    FreeLibrary(mod);

    return st;
}

VOID ReleaseIcon(PVOID Buffer)
{
    FreeMemoryP(Buffer);
}

void listfunc(PWSTR dll)
{
    PVOID base;

    PCSTR *funclist;
    ULONG n;

    funclist = (PCSTR *)AllocateMemory(0x10000 * sizeof(*funclist), HEAP_ZERO_MEMORY);

    ReLoadDll(dll, &base, NULL, RELOAD_DLL_IGNORE_IAT);

    n = 0;
    WalkExportTableT(base,
        WalkEATCallbackM(ImageBase, AddressOfFunction, Dll, Ordinal, Func, Context)
        {
            ++n;
            funclist[Ordinal] = Func;
            return 0;
        },
        0
    );

    ++n;
    while (--n)
    {
        if (*funclist == NULL)
        {
            ++funclist;
            continue;
        }
        PrintConsoleA("    '%s',\n", *funclist++);
    }

    UnLoadDll(base);
}

#if ML_X86

BOOL IsRunningInVMWare()
{
    BOOL Result;

    SEH_TRY
    {
        INLINE_ASM
        {
            mov     eax, 'VMXh';
            mov     ecx, 0xA;
            mov     edx, 'VX';
            in      eax, dx;
            sub     ebx, 'VMXh';
            sete    al;
            movzx   eax, al;
            mov     Result, eax;
        }
    }
    SEH_EXCEPT(EXCEPTION_EXECUTE_HANDLER)
    {
        Result = FALSE;
    }

    return Result;
}

#endif

#pragma comment(lib, NT6_LIB(kernel32))
#pragma comment(lib, NT6_LIB(ws2_32))

#include "../Drivers/AntiAntiKernelDebug/ShadowSysCall.h"

#include "String.hpp"

TYPE_OF(::CreateProcessW)*  Shell32CreateProcessWPtr;
TYPE_OF(::CreateProcessW)** Shell32CreateProcessWIAT;

UNICODE_STRING  ProbeApplicationName, ProbeCommandLine;
PVOID           InvokeReturnAddress;

BOOL TryIsProbeProcess(PCWSTR ApplicationName, PWSTR CommandLine)
{
    UNICODE_STRING  AppName, CmdLine;

    RtlInitUnicodeString(&AppName, ApplicationName);
    RtlInitUnicodeString(&CmdLine, CommandLine);

    SEH_TRY
    {
        if (CmdLine.Length < ProbeCommandLine.Length)
            return FALSE;

        CmdLine.Buffer = PtrAdd(CmdLine.Buffer, CmdLine.Length - ProbeCommandLine.Length);
        CmdLine.Length = ProbeCommandLine.Length;

        if (!RtlEqualUnicodeString(&CmdLine, &ProbeCommandLine, TRUE))
            return FALSE;

        if (!RtlEqualUnicodeString(&AppName, &ProbeApplicationName, TRUE))
            return FALSE;

        return TRUE;
    }
    SEH_EXCEPT(EXCEPTION_EXECUTE_HANDLER)
    {
        return FALSE;
    }
}

BOOL
NTAPI
ProbeInvokeCreateProcessW(
    PCWSTR                  ApplicationName,
    PWSTR                   CommandLine,
    PSECURITY_ATTRIBUTES    ProcessAttributes,
    PSECURITY_ATTRIBUTES    ThreadAttributes,
    BOOL                    InheritHandles,
    ULONG                   CreationFlags,
    PVOID                   Environment,
    PCWSTR                  CurrentDirectory,
    LPSTARTUPINFOW          StartupInfo,
    PPROCESS_INFORMATION    ProcessInformation
)
{
    if (TryIsProbeProcess(ApplicationName, CommandLine))
    {
        PVOID BackTrace[3];

        AllocStack(16);

        //PrintConsoleW(L"%d\n", RtlCaptureStackBackTrace(0, countof(BackTrace), BackTrace, NULL));

        RtlCaptureStackBackTrace(0, countof(BackTrace), BackTrace, NULL);
        InvokeReturnAddress = BackTrace[1];
        RtlSetLastWin32Error(NO_ERROR);

        return FALSE;
    }

    return Shell32CreateProcessWPtr(ApplicationName, CommandLine, ProcessAttributes, ThreadAttributes, InheritHandles, CreationFlags, Environment, CurrentDirectory, StartupInfo, ProcessInformation);
}

BOOL
NTAPI
SpeedUpCreateProcessW(
    PCWSTR                  ApplicationName,
    PWSTR                   CommandLine,
    PSECURITY_ATTRIBUTES    ProcessAttributes,
    PSECURITY_ATTRIBUTES    ThreadAttributes,
    BOOL                    InheritHandles,
    ULONG                   CreationFlags,
    PVOID                   Environment,
    PCWSTR                  CurrentDirectory,
    LPSTARTUPINFOW          StartupInfo,
    PPROCESS_INFORMATION    ProcessInformation
)
{
    LOOP_ONCE
    {
        PrintConsoleW(L"%s\n%s\n\n", ApplicationName, CommandLine);
    }

    return (*Shell32CreateProcessWIAT)(ApplicationName, CommandLine, ProcessAttributes, ThreadAttributes, InheritHandles, CreationFlags, Environment, CurrentDirectory, StartupInfo, ProcessInformation);
}

PVOID ProbeInvokeCreateProcessAddress()
{
    PVOID               Shell32, Shell32CreateProcessW, CreateProcessW;
    PLDR_MODULE         Shell32Module, MainModule;
    SHELLEXECUTEINFOW   ExecuteInfo;
    PIMAGE_NT_HEADERS   NtHeaders;

    Shell32 = Ldr::LoadDll(L"Shell32.dll");

    Shell32CreateProcessW = PtrAdd(Shell32, IATLookupRoutineRVAByHashNoFix(Shell32, KERNEL32_CreateProcessW));

    MainModule = FindLdrModuleByHandle(NULL);

    RtlDuplicateUnicodeString(RTL_DUPSTR_ADD_NULL, &MainModule->FullDllName, &ProbeApplicationName);
    RtlInitUnicodeString(&ProbeCommandLine, L"ML_PROBE_APPLICATION_COMMAMD_LINE");

    ZeroMemory(&ExecuteInfo, sizeof(ExecuteInfo));

    ExecuteInfo.cbSize          = sizeof(ExecuteInfo);
    ExecuteInfo.fMask           = SEE_MASK_NOASYNC | SEE_MASK_FLAG_NO_UI;
    ExecuteInfo.lpVerb          = L"open";
    ExecuteInfo.lpFile          = ProbeApplicationName.Buffer;
    ExecuteInfo.lpParameters    = ProbeCommandLine.Buffer;
    ExecuteInfo.nShow           = SW_SHOW;

    *(PVOID *)&Shell32CreateProcessWIAT = Shell32CreateProcessW;
    *(PVOID *)&Shell32CreateProcessWPtr = *(PVOID *)Shell32CreateProcessWIAT;

    CreateProcessW = ProbeInvokeCreateProcessW;
    WriteProtectMemory(CurrentProcess, Shell32CreateProcessW, &CreateProcessW, sizeof(CreateProcessW));
    ShellExecuteExW(&ExecuteInfo);
    WriteProtectMemory(CurrentProcess, Shell32CreateProcessW, &Shell32CreateProcessWPtr, sizeof(Shell32CreateProcessWPtr));

    RtlFreeUnicodeString(&ProbeApplicationName);

    NtHeaders = RtlImageNtHeader(Shell32);

    if (InvokeReturnAddress < Shell32 || InvokeReturnAddress > PtrAdd(Shell32, NtHeaders->OptionalHeader.SizeOfImage))
        return NULL;

    return InvokeReturnAddress;
}

BOOL HookCallCreateProcessFast(PVOID InvokeReturnAddress)
{
    PBYTE               InvokeBuffer;
    PVOID               *JumpAddressBegin, *JumpAddressEnd, HookRoutine;
    PIMAGE_NT_HEADERS   NtHeaders;
    PLDR_MODULE         Shell32;

    InvokeBuffer = (PBYTE)InvokeReturnAddress;
    LOOP_ONCE
    {
        PrintConsoleW(L"phase 0\n");

        if (*(PUSHORT)&InvokeBuffer[-6] != 0x15FF)
            break;

#if ML_X86

        if (*(PULONG)&InvokeBuffer[-4] != (ULONG)Shell32CreateProcessWIAT)
            break;

#elif ML_AMD64

        if ((PVOID)PtrAdd(InvokeBuffer, *(PULONG)&InvokeBuffer[-4]) != Shell32CreateProcessWIAT)
            break;

#endif // arch

        PrintConsoleW(L"phase 1\n");

        Shell32 = FindLdrModuleByName(&WCS2US(L"SHELL32.dll"));
        NtHeaders = RtlImageNtHeader(Shell32->DllBase);
        if (NtHeaders == NULL)
            break;

        PrintConsoleW(L"phase 2\n");

        JumpAddressEnd = (PVOID *)PtrAdd(Shell32->DllBase, ROUND_UP(NtHeaders->OptionalHeader.SizeOfHeaders, NtHeaders->OptionalHeader.SectionAlignment));
        JumpAddressBegin = (PVOID *)(IMAGE_FIRST_SECTION(NtHeaders) + NtHeaders->FileHeader.NumberOfSections);

        while (JumpAddressBegin < JumpAddressEnd)
        {
            if (*JumpAddressBegin == NULL)
                break;

            ++JumpAddressBegin;
        }

        if (JumpAddressBegin >= JumpAddressEnd)
            break;

        PrintConsoleW(L"phase 3\n");

        HookRoutine = SpeedUpCreateProcessW;
        WriteProtectMemory(CurrentProcess, JumpAddressBegin, &HookRoutine, sizeof(HookRoutine));

#if ML_X86

        WriteProtectMemory(CurrentProcess, &InvokeBuffer[-4], &JumpAddressBegin, sizeof(JumpAddressBegin));

#elif ML_AMD64

        LONG64 RelateOffset;

        RelateOffset = (TYPE_OF(RelateOffset))PtrSub(JumpAddressBegin, InvokeBuffer);

        PrintConsoleW(L"target = %I64X\n", PtrOffset(PtrAdd(InvokeBuffer, RelateOffset), Shell32->DllBase));

        WriteProtectMemory(CurrentProcess, &InvokeBuffer[-4], &RelateOffset, sizeof(LONG));

#endif
    }

    return FALSE;
}

BOOL HookCallCreateProcess()
{
    PVOID InvokeReturnAddress;

    SEH_TRY
    {
        InvokeReturnAddress = ProbeInvokeCreateProcessAddress();
        if (InvokeReturnAddress == NULL)
            return FALSE;

        return HookCallCreateProcessFast(InvokeReturnAddress);
    }
    SEH_EXCEPT(EXCEPTION_EXECUTE_HANDLER)
    {
        return FALSE;
    }
}

// {5a936bef-668d-4f6e-b057-7da30869c871}
SET_GUID(GUID_ShellOverlayHook,
0x5a936bef, 0x668d, 0x4f6e, 0xb0, 0x57, 0x7d, 0xa3, 0x08, 0x69, 0xc8, 0x71);

WCHAR IconOverlayKey[] = L"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ShellIconOverlayIdentifiers\\" L"\x01" L"Arianrhod";

ULONG_PTR FormatDllClassId(PWSTR Buffer, PCUNICODE_STRING GuidString)
{
    return swprintf(Buffer, L"CLSID\\%wZ\\InprocServer32", GuidString);
}

#pragma comment(lib, "advapi32.lib")

NTSTATUS UnInstallShellOverlayHook()
{
    WCHAR           DllClassIdKey[MAX_NTPATH];
    ULONG_PTR       Length;
    NTSTATUS        Status;
    UNICODE_STRING  GuidString;

    Status = RtlStringFromGUID(GUID_ShellOverlayHook, &GuidString);
    FAIL_RETURN(Status);

    Length = FormatDllClassId(DllClassIdKey, &GuidString);

    Reg::DeleteKey(HKEY_MACHINE_CLASS, DllClassIdKey, KEY_WOW64_64KEY);

    DllClassIdKey[Length - countof(L"\\InprocServer32") + 1] = 0;

    Reg::DeleteKey(HKEY_MACHINE_CLASS, DllClassIdKey, KEY_WOW64_64KEY);

    Reg::DeleteKey(HKEY_LOCAL_MACHINE, IconOverlayKey, KEY_WOW64_64KEY);

    RtlFreeUnicodeString(&GuidString);

    return 0;
}

NTSTATUS InstallShellOverlayHook()
{
    WCHAR           DllClassIdKey[MAX_NTPATH];
    PWSTR           DllFullPath;
    ULONG_PTR       Length;
    NTSTATUS        Status;
    UNICODE_STRING  GuidString, DllPath, ThreadingModel;
    PLDR_MODULE     ExeModule;

    static WCHAR DllFileName[] = L"IconOverlayHandler.dll";

    ExeModule               = FindLdrModuleByHandle(NULL);
    DllPath                 = ExeModule->FullDllName;
    DllPath.Length          = (USHORT)PtrOffset(findnamew(DllPath.Buffer), DllPath.Buffer);
    DllPath.MaximumLength   = DllPath.Length;

    Status = RtlStringFromGUID(GUID_ShellOverlayHook, &GuidString);
    FAIL_RETURN(Status);

    SCOPE_EXIT
    {
        RtlFreeUnicodeString(&GuidString);
    }
    SCOPE_EXIT_END;

    FormatDllClassId(DllClassIdKey, &GuidString);

    DllFullPath = (PWSTR)AllocStack(DllPath.Length + sizeof(DllFileName));
    Length = swprintf(DllFullPath, L"%wZ%s", &DllPath, DllFileName);

    Status = Reg::SetKeyValue(HKEY_MACHINE_CLASS, DllClassIdKey, NULL, REG_SZ, DllFullPath, Length * sizeof(WCHAR), KEY_WOW64_64KEY);
    FAIL_RETURN(Status);


    RTL_CONST_STRING(ThreadingModel, L"Apartment");

    Status = Reg::SetKeyValue(HKEY_MACHINE_CLASS, DllClassIdKey, L"ThreadingModel", REG_SZ, ThreadingModel.Buffer, ThreadingModel.Length, KEY_WOW64_64KEY);
    FAIL_RETURN(Status);

    Status = Reg::SetKeyValue(HKEY_LOCAL_MACHINE, IconOverlayKey, NULL, REG_SZ, GuidString.Buffer, GuidString.Length, KEY_WOW64_64KEY);

    return Status;
}

#include <ShlObj.h>

ForceInline Void main2(LongPtr argc, TChar **argv)
{

#if 0

    Ps::CreateThread(
        ThreadLambdaType_(PVOID)
        {
            return PrintConsoleW(L"fuck\n");
        },
        nullptr
    );

    return;

#endif

    NTSTATUS Status;

    Status = Nt_AdjustPrivilege(SE_DEBUG_PRIVILEGE, TRUE, FALSE);

    if (Status == STATUS_PRIVILEGE_NOT_HELD)
    {
        ShellExecuteW(NULL, L"runas", FindLdrModuleByHandle(NULL)->FullDllName.Buffer, NULL, NULL, SW_SHOW);
        Ps::ExitProcess(0);
    }

    if (NT_FAILED(Status))
    {
        Ps::ExitProcess(0);
    }

    if (NT_FAILED(InstallShellOverlayHook()))
    {
        UnInstallShellOverlayHook();
        Ps::ExitProcess(0);
    }

    ULONG ExplorerPid;

    if (GetWindowThreadProcessId(GetShellWindow(), &ExplorerPid) != 0)
    {
        HANDLE Explorer = PidToHandle(ExplorerPid);
        if (Explorer != NULL)
        {
            NtTerminateProcess(Explorer, 1);
            NtClose(Explorer);

            Ps::CreateProcess(NULL, L"explorer.exe");
            //ShellExecuteW(NULL, L"open", L"explorer.exe", NULL, NULL, SW_SHOW);
        }
    }

    PauseConsole(L"Press any key to uninstall ...");
    UnInstallShellOverlayHook();

    Ps::ExitProcess(0);

    return;

    HookCallCreateProcess();

    PrintConsoleW(L"\n");

    ShellExecuteA(0, "open", "notepad", "", 0, SW_SHOW);
    ShellExecuteA(0, "open", "mspaint", "", 0, SW_SHOW);

    PauseConsole();
    Ps::ExitProcess(0);

    return;

    LOGFONTW lf;

    HDC dc = CreateCompatibleDC(NULL);

    lf.lfCharSet = 0x80;
    lf.lfFaceName[0] = 0;

    EnumFontFamiliesExW(GetDC(NULL), &lf,
        [] (CONST LOGFONTW *lf, CONST TEXTMETRICW *, DWORD, LPARAM dc)
        {
            HFONT ft;

            ft = CreateFontW(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, lf->lfFaceName);
            DeleteObject(SelectObject((HDC)dc, ft));

            LOOP_ONCE
            {
                ULONG dw;
                PVOID buf;

                dw = GetFontData((HDC)dc, 'eman', 0, NULL, 0);
                if (dw == GDI_ERROR)
                    break;

                buf = AllocateMemory(dw);
                GetFontData((HDC)dc, 'eman', 0, buf, dw);
            }

            PrintConsoleW(L"%02X, %s\n", lf->lfCharSet, lf->lfFaceName);
            return TRUE;
        },
        (LPARAM)dc,
        0
    );

    DeleteDC(dc);

    PauseConsole();

    return;

#if 0

    SC_HANDLE       ScManager, Service, Themes;
    SERVICE_STATUS  ServiceStatus;
    WCHAR           DriverPath[MAX_NTPATH];

    ScManager   = NULL;
    Service     = NULL;

    RtlWow64EnableFsRedirection(FALSE);
    ScManager = OpenSCManagerW(NULL, NULL, SC_MANAGER_CREATE_SERVICE);
    if (ScManager == NULL)
        return;

    PrintConsoleW(L"open scmgr\n");
    Status = STATUS_UNSUCCESSFUL;

    SCOPE_EXIT
    {
        if (Service != NULL)
        {
            if (!NT_SUCCESS(Status))
            {
                ControlService(Service, SERVICE_CONTROL_STOP, &ServiceStatus);
                DeleteService(Service);
            }
            CloseServiceHandle(Service);
        }

        if (ScManager != NULL)
            CloseServiceHandle(ScManager);

        PauseConsole();
        Nt_ExitProcess(0);
    }
    SCOPE_EXIT_END;

    Service = OpenServiceW(ScManager, BYPASS_UAC_SERVICE_NAME, SERVICE_ALL_ACCESS);

    PrintConsoleW(L"open svr\n");
    if (Service == NULL)
    {
        static WCHAR drv[] = BYPASS_UAC_DRIVER_NAME;
        CopyStruct(DriverPath + Nt_GetExeDirectory(DriverPath, countof(DriverPath)), drv, sizeof(drv));

        Service = CreateServiceW(
                        ScManager,
                        BYPASS_UAC_SERVICE_NAME,
                        BYPASS_UAC_SERVICE_NAME,
                        SERVICE_ALL_ACCESS,
                        SERVICE_KERNEL_DRIVER,
                        SERVICE_BOOT_START,
                        SERVICE_ERROR_IGNORE,
                        DriverPath,
                        NULL,
                        NULL,
                        NULL,
                        NULL,
                        NULL
                  );

        PrintConsoleW(L"create svr\n");
        if (Service == NULL)
            return;
    }

    if (!StartServiceW(Service, 0, NULL) && RtlGetLastWin32Error() != ERROR_SERVICE_ALREADY_RUNNING)
    {
        PrintConsoleW(L"lasterr %d\n", RtlGetLastWin32Error());
        return;
    }

    PrintConsoleW(L"start svr\n");
    Status = 0;

    return;

    NtFileDisk Device;

    Status = Device.OpenDevice(SHADOW_SYSCALL_DEVICE_SYMBOLIC);
    if (!NT_SUCCESS(Status))
        return;

    SS_PROBE_DEBUG_PORT Pdp;
    CONTEXT Context;
    ULONG_PTR CC;
    ULONG_PTR RemoteBase;
    HANDLE Thread;

    PROCESS_INFORMATION pi;

    if (!NT_SUCCESS(Nt_CreateProcess(NULL, Nt_CurrentPeb()->ProcessParameters->ImagePathName.Buffer, NULL, NULL, CREATE_SUSPENDED, NULL, &pi)))
        return;

    Context.ContextFlags = CONTEXT_ALL;
    NtGetContextThread(pi.hThread, &Context);

    RemoteBase = PtrSub(Context.Eax, PtrOffset(main2, &__ImageBase));

//    Nt_CreateThread((PVOID)(RemoteBase + PtrOffset(StubThread, &__ImageBase)), NULL, TRUE, pi.hProcess, &Thread);
//    Nt_WriteMemory(pi.hProcess, (PVOID)(Context.Esp + sizeof(PVOID)), &Thread, sizeof(Thread));
    Context.Eax = RemoteBase + PtrOffset(UnMapSectionThread, &__ImageBase);
    NtSetContextThread(pi.hThread, &Context);

    Pdp.DebugProcessId  = pi.dwProcessId;
    Pdp.DebugThreadId   = pi.dwThreadId;
    Pdp.UserContext     = &Context;

    Status = Device.DeviceIoControl(IOCTL_PROBE_DEBUG_PORT_ADDRESS, &Pdp, sizeof(Pdp), NULL, 0);
    PrintConsoleW(L"IOCTL_PROBE_DEBUG_PORT_ADDRESS: %08X\n", Status);

    NtTerminateProcess(pi.hProcess, 0);
    NtClose(pi.hProcess);
    NtClose(pi.hThread);

    PauseConsole();

    return;

#endif

#if 0
    INT   Height;
    HDC   hDC;
    HFONT hFont;
    BYTE  Buffer[0x5000];
    GLYPHMETRICS gm;
    MAT2 mat = { { 0, 1 }, { 0, 0 }, { 0, 0 }, { 0, 1 } };

    _wsetlocale(LC_CTYPE, L"");
    Height = 50;

#if 0
    ULONG BitsPerRow = 0x3E;
    PBYTE p = BitMap + sizeof(BitMap) - ROUND_UP(BitsPerRow / 8, 4);
    for (ULONG i = Height; i; --i)
    {
        PBYTE bak = p;
        for (ULONG j = BitsPerRow / 8; j; --j)
        {
            BYTE b = *p++;
            TEST_BIT(b, 7) ? printf("@") : printf(" ");
            TEST_BIT(b, 6) ? printf("@") : printf(" ");
            TEST_BIT(b, 5) ? printf("@") : printf(" ");
            TEST_BIT(b, 4) ? printf("@") : printf(" ");
            TEST_BIT(b, 3) ? printf("@") : printf(" ");
            TEST_BIT(b, 2) ? printf("@") : printf(" ");
            TEST_BIT(b, 1) ? printf("@") : printf(" ");
            TEST_BIT(b, 0) ? printf("@") : printf(" ");
        }
        p = bak - ROUND_UP(BitsPerRow / 8, 4);
        printf("#\n");
    }

//    return;

#endif

    hDC = CreateCompatibleDC(NULL);
    hFont = CreateFontW(
                Height,
                0,
                0,
                0,
                FW_NORMAL,
                0,
                0,
                0,
                GB2312_CHARSET,
                0,
                0,
                ANTIALIASED_QUALITY,
                FIXED_PITCH,
                L"ºÚÌå");
    SelectObject(hDC, hFont);
    WCHAR c = L'´ô';
    GetGlyphOutlineW(hDC, c, GGO_GRAY8_BITMAP, &gm, sizeof(Buffer), Buffer, &mat);

    INT nBytesPerLine;
    PBYTE pbBuffer = Buffer;

    printf(
        "Height             = %08X\n"
        "gmBlackBoxX        = %08X\n"
        "gmBlackBoxY        = %08X\n"
        "gmptGlyphOrigin.x  = %08X\n"
        "gmptGlyphOrigin.y  = %08X\n"
        "gmCellIncX         = %08X\n"
        "gmCellIncY         = %08X\n"
        "=========================\n",
        Height, gm.gmBlackBoxX, gm.gmBlackBoxY, gm.gmptGlyphOrigin.x, gm.gmptGlyphOrigin.y,
        gm.gmCellIncX, gm.gmCellIncY);

    nBytesPerLine = ROUND_UP(gm.gmBlackBoxX, sizeof(DWORD));

#if 0
    int nByteCount = ((gm.gmBlackBoxX +31) >> 5) << 2;
//    nByteCount = ROUND_UP(gm.gmBlackBoxX / 8, 8);
//    printf("%08X\n", nByteCount);

    PBYTE p1 = Buffer + (gm.gmBlackBoxY - 1) * nByteCount;
    p1 = Buffer;

    for (int i = ROUND_UP(gm.gmptGlyphOrigin.y, 32) / 8; i; --i)
        printf("\n");

    for ( int i = 0; i < gm.gmBlackBoxY; i++)
    {
        for (int j = gm.gmptGlyphOrigin.x; j; --j)
            printf(" ");

        PBYTE bak = p1;
        for (int j = 0; j < nByteCount; j++)
        {
            BYTE b;
            b = *p1++;
            TEST_BIT(b, 7) ? printf("@") : printf(" ");
            TEST_BIT(b, 6) ? printf("@") : printf(" ");
            TEST_BIT(b, 5) ? printf("@") : printf(" ");
            TEST_BIT(b, 4) ? printf("@") : printf(" ");
            TEST_BIT(b, 3) ? printf("@") : printf(" ");
            TEST_BIT(b, 2) ? printf("@") : printf(" ");
            TEST_BIT(b, 1) ? printf("@") : printf(" ");
            TEST_BIT(b, 0) ? printf("@") : printf(" ");
        }
//        p1 = bak - nByteCount;
        printf("#\n");
    }

    for (int i = (Height - gm.gmBlackBoxY) / 8; i; --i)
        printf("\n");

#else

    for (int j = 0; j != gm.gmBlackBoxY; ++j)
    {
        for (int i = 0; i != nBytesPerLine; ++i)
        {
            char c = *pbBuffer++;
            if (c > 31 && i < Height)
                printf("@");
            else
                printf(" ");
        }

        printf("#\n");
    }
#endif
#endif
    return;

/*
    HANDLE hFile, hMap;
    PBYTE  pbImage;
    PULONG_PTR pRVA;
    hFile = CreateFileW(
                name,
                GENERIC_READ|GENERIC_WRITE,
                FILE_SHARE_READ,
                NULL,
                OPEN_EXISTING,
                FILE_ATTRIBUTE_NORMAL,
                NULL);
    if (hFile == INVALID_HANDLE_VALUE)
        return;

    hMap = CreateFileMappingW(hFile, NULL, PAGE_READWRITE, 0, 0, NULL);
    CloseHandle(hFile);
    if (hMap == NULL)
        return;

    pbImage = (PBYTE)MapViewOfFile(hMap, FILE_MAP_READ|FILE_MAP_WRITE, 0, 0, 0);
    CloseHandle(hMap);
    if (pbImage == NULL)
        return;

    pRVA = (PULONG_PTR)(pbImage + 0x21440C);
    for (DWORD i = 266; i; --i)
    {
        if (*pRVA)
            *pRVA = *pRVA - 0x214400 + 0x21D000;
        else
            break;
        pRVA += 5;
    }

    UnmapViewOfFile(pbImage);
*/
}

int CDECL main(Long_Ptr argc, TChar **argv)
{
//    MyLib_Initialize();
//    my_initterm(&__xi_a, &__xi_z);
//    my_initterm(&__xc_a, &__xc_z);
    getargs(&argc, &argv);
    main2(argc, argv);

//    MyLib_UnInitialize();

    Nt_ExitProcess(0);
}

#if 0
Void FASTCALL ExtractSubtitles(Int argc, PWChar *argv)
{
    UInt32 cur;
    WChar path[MAX_PATH];
    HANDLE hPipeRead, hPipeWrite;
    STARTUPINFOW si;
    PROCESS_INFORMATION pi;
    SECURITY_ATTRIBUTES sa;

    if (argc < 2)
        return;
/*
    cur = GetModuleFileNameW(0, path, countof(path));
    while (path[--cur] != '\\');
    path[++cur] = 0;
*/

    _wsetlocale(LC_CTYPE, L"");

    sa.nLength = sizeof(sa);
    sa.lpSecurityDescriptor = NULL;
    sa.bInheritHandle = True;

    ZeroMemory(&si, sizeof(si));
    si.cb = sizeof(si);

    wcscpy(path, L"G:\\x\\mkvtoolnix\\mkvinfo.exe");
    cur = wcslen(path);
    for (Int i = 1; i != argc; ++i)
    {
        if (CreatePipe(&hPipeRead, &hPipeWrite, &sa, 0x2000) == False)
        {
            PrintError(GetLastError());
            continue;
        }

        si.dwFlags = STARTF_USESTDHANDLES;
        si.hStdOutput = hPipeWrite;
        swprintf(path + cur, L" \"%s\"", *++argv);
        if (CreateProcessW(NULL, path, NULL, NULL, True, 0, NULL, NULL, &si, &pi) == False)
        {
            PrintError(GetLastError());
            CloseHandle(hPipeWrite);
            CloseHandle(hPipeRead);
            continue;
        }

        WaitForSingleObjectEx(pi.hProcess, INFINITE, False);
        CloseHandle(pi.hProcess);
        CloseHandle(pi.hThread);
        CloseHandle(hPipeWrite);

        PChar pBuf, p1;
        DWORD dwRead, dwAvail;

        if (PeekNamedPipe(hPipeRead, 0, 0, NULL, &dwAvail, NULL))
        {
            pBuf = (PChar)malloc(dwAvail + 4);
            p1 = pBuf;
            ReadFile(hPipeRead, pBuf, dwAvail, &dwRead, NULL);
            *(PUInt32)&pBuf[dwRead] = 0;

            UInt32 count, n;
            PChar psubid, p;
            WChar cmd[MAX_PATH * 3];

            n = 0;
            count = swprintf(cmd, L"%s\"%s\" ", L"G:\\x\\mkvtoolnix\\mkvextract.exe tracks ", *argv);
            rmextw(*argv);
            while (psubid = strstr(pBuf, "Track type: subtitles"))
            {
                p = pBuf;
                pBuf = psubid + 1;
                psubid = StrRStrIA(p, psubid, "Track number:");
                if (psubid == NULL)
                    continue;

                if (sscanf(psubid, "Track number: %u", &dwRead) != 1)
                    continue;

                PCWChar fmt, param;
                static WChar *lang[] = { L"sc", L"tc", L"jp" };

                count += swprintf(cmd + count, L"%u:\"%s.", dwRead, *argv);

                if (n >= 0 && n < countof(lang))
                {
                    fmt = L"%s.ass\" ";
                    param = lang[n];
                }
                else
                {
                    fmt = L"%u.ass\" ";
                    param = (PCWChar)n;
                }

                count += swprintf(cmd + count, fmt, param);
                ++n;
            }

            si.dwFlags = 0;
            if (n && CreateProcessW(NULL, cmd, 0, 0, 0, 0, 0, 0, &si, &pi))
            {
                WaitForSingleObjectEx(pi.hProcess, INFINITE, False);
                CloseHandle(pi.hThread);
                CloseHandle(pi.hProcess);
            }

            free(p1);
        }

        CloseHandle(hPipeRead);
    }
}

#endif





#if 0



// #include "JsonParser.h"

HANDLE g_hHeap;

typedef struct
{
    TYPE_OF(NtWaitForSingleObject)  *NtWaitForSingleObject;
    TYPE_OF(DeleteFileW)            *DeleteFileW;
    TYPE_OF(NtTerminateProcess)     *NtTerminateProcess;
    TYPE_OF(NtClose)                *NtClose;

    HANDLE ProcessHandle;
    WCHAR  FullPath[1];

} DELETE_SELF_INFO, *PDELETE_SELF_INFO;

#if !ML_AMD64

VOID FASTCALL DeleteSelfImpl(PDELETE_SELF_INFO dsi)
{
    INLINE_ASM
    {
        call SELF_LOCATE;
SELF_LOCATE:
        pop eax;
        and eax, not (MEMORY_PAGE_SIZE - 1);
        mov dsi, eax;
    }

    dsi->NtWaitForSingleObject(dsi->ProcessHandle, FALSE, NULL);
    dsi->NtClose(dsi->ProcessHandle);
    dsi->DeleteFileW(dsi->FullPath);
    dsi->NtTerminateProcess(NtCurrentProcess(), 0);
}

ASM VOID DeleteSelfImplEnd() {}

VOID DeleteSelf()
{
    NTSTATUS            Status;
    ULONG               Length;
    WCHAR               path[MAX_PATH];
    STARTUPINFOW        si;
    PROCESS_INFORMATION pi;
    DELETE_SELF_INFO    dsi, *pdsi;
    CONTEXT             Context;
    PVOID               FuncAddress;

    CopyStruct(path + Nt_GetSystemDirectory(path, countof(path)), L"\\cmd.exe", sizeof(L"\\cmd.exe"));
    ZeroMemory(&si, sizeof(si));
    si.cb = sizeof(si);

//    pi.hProcess = NtCurrentProcess();
//    pi.hThread = NtCurrentThread();
    Status = Nt_CreateProcess(NULL, path, NULL, CREATE_SUSPENDED, NULL, &pi);
    if (!NT_SUCCESS(Status))
        return;

    pdsi = NULL;
    Status = Nt_AllocateMemory(pi.hProcess, (PVOID *)&pdsi, 0x1000);

    NtDuplicateObject(
        NtCurrentProcess(),
        NtCurrentProcess(),
        pi.hProcess,
        &dsi.ProcessHandle,
        0,
        FALSE,
        DUPLICATE_SAME_ACCESS
    );

    dsi.NtWaitForSingleObject   = NtWaitForSingleObject;
    dsi.DeleteFileW             = DeleteFileW;
    dsi.NtTerminateProcess      = NtTerminateProcess;
    dsi.NtClose                 = NtClose;

    Nt_WriteMemory(pi.hProcess, pdsi, &dsi, sizeof(dsi), (PSIZE_T)&Length);
    Length = Nt_GetModuleFileName(NULL, path, countof(path));
    Nt_WriteMemory(pi.hProcess, pdsi->FullPath, path, (Length + 1) * sizeof(WCHAR), (PSIZE_T)&Length);

    FuncAddress = (PBYTE)&pdsi->FullPath + Length;
    Nt_WriteMemory(
        pi.hProcess,
        FuncAddress,
        DeleteSelfImpl,
        (ULONG_PTR)DeleteSelfImplEnd - (ULONG_PTR)DeleteSelfImpl,
        (PSIZE_T)&Length
    );

    Context.ContextFlags = CONTEXT_CONTROL;
    NtGetContextThread(pi.hThread, &Context);
    Context.Eip = (ULONG_PTR)FuncAddress;
    Context.Ecx = (ULONG_PTR)pdsi;
    NtSetContextThread(pi.hThread, &Context);

    NtResumeThread(pi.hThread, NULL);
    NtClose(pi.hProcess);
    NtClose(pi.hThread);
}

#endif // x86

#if 0

#include "json-c/json.h"
#include "json-c/json_object_private.h"

#include "E:/Desktop/Source/GUI/Celestial Globe/Internal/CG_Script.h"

#define CG_SCRIPT_CONFIG_ROOT_TAG       L"CoreConfig"
#define CG_SCRIPT_CONFIG_UI_MODULE      L"UIModule"
#define CG_SCRIPT_CONFIG_IMAGE_PLUGIN   L"ImagePlugin"
#define CG_SCRIPT_CONFIG_CATEGORY       L"Category"
#define CG_SCRIPT_CONFIG_CATEGORY_LIST  L"List"

#define CG_SCRIPT_GAMELIST_ROOT_TAG     L"GameList"

#define PARSE_SCRIPT_CHECK_BUFFER_SIZE(size, info) \
            if ((size) < sizeof(info)) \
                return STATUS_BUFFER_TOO_SMALL

CGSTATUS
ParseCoreConfig(
    JSON_OBJECT            *Script,
    CG_SCRIPT_CORE_CONFIG  *CoreConfig,
    ULONG                   InfoSize
)
{
    CGSTATUS     Status;
    JSON_OBJECT *Object, *CategoryObject, *CategoryItem;
    CG_GAME_CATEGORY_ENTRY *CategoryEntry;

    PARSE_SCRIPT_CHECK_BUFFER_SIZE(InfoSize, CoreConfig);

    ZeroMemory(CoreConfig, sizeof(*CoreConfig));
    CoreConfig->ScriptType = CG_SCRIPT_TYPE_CONFIG;

    Status = STATUS_SUCCESS;
    Object = Script->Value.Object.Object;
    for (ULONG Count = Script->Value.Object.Count; Count; ++Object, --Count)
    {
        if (!StrICompareW(Object->Name.Buffer, CG_SCRIPT_CONFIG_CATEGORY))
        {
            if (Object->Type != JSON_TYPE_OBJECT)
            {
                Status = STATUS_UNSUCCESSFUL;
                break;
            }

            CoreConfig->Category.Count = Object->Value.Object.Count;
            CategoryEntry = (CG_GAME_CATEGORY_ENTRY *)malloc(sizeof(*CategoryEntry) * CoreConfig->Category.Count);
            if (CategoryEntry == NULL)
            {
                Status = STATUS_NO_MEMORY;
                break;
            }

            CoreConfig->Category.pCategory = CategoryEntry;

            CategoryObject = Object->Value.Object.Object;
            for (ULONG Count = Object->Value.Object.Count; Count; --Count)
            {
                if (CategoryObject->Type != JSON_TYPE_OBJECT)
                    continue;

                CategoryItem = CategoryObject->Value.Object.Object;
                RtlCreateUnicodeString(&CategoryEntry->Name, CategoryObject->Name.Buffer);
                for (ULONG ItemCount = CategoryObject->Value.Object.Count; ItemCount; --ItemCount)
                {
                    if (!StrICompareW(CategoryItem->Name.Buffer, CG_SCRIPT_CONFIG_CATEGORY_LIST))
                    {
                        if (CategoryItem->Type != JSON_TYPE_STRING)
                            continue;

                        RtlCreateUnicodeString(
                            &CategoryEntry->ScriptPath,
                            CategoryItem->Value.String.Buffer
                        );
                    }
                }

                ++CategoryObject;
                ++CategoryEntry;
            }
        }
        else if (!StrICompareW(Object->Name.Buffer, CG_SCRIPT_CONFIG_UI_MODULE))
        {
            RtlCreateUnicodeString(&CoreConfig->UIModule, Object->Value.String.Buffer);
        }
    }

    return Status;
}

CGSTATUS FreeScript(CG_SCRIPT_BASE *ScriptInfo)
{
    union
    {
        CG_SCRIPT_BASE          *Base;
        CG_SCRIPT_CORE_CONFIG   *CoreConfig;
        CG_SCRIPT_PLUGIN        *Plugin;
    };

    CGSTATUS Status;
    CG_GAME_CATEGORY_ENTRY *pCategory;

    Status = STATUS_SUCCESS;
    Base = ScriptInfo;
    switch (Base->ScriptType)
    {
        case CG_SCRIPT_TYPE_CONFIG:
            RtlFreeUnicodeString(&CoreConfig->UIModule);
            RtlFreeUnicodeString(&CoreConfig->ImagePlugin);

            pCategory = CoreConfig->Category.pCategory;
            for (ULONG Count = CoreConfig->Category.Count; Count; ++pCategory, --Count)
            {
                RtlFreeUnicodeString(&pCategory->Name);
                RtlFreeUnicodeString(&pCategory->ScriptPath);
            }

            free(CoreConfig->Category.pCategory);
            break;
    }

    ZeroMemory(CoreConfig, sizeof(*CoreConfig));

    return Status;
}

CGSTATUS
ParseScript(
    PVOID           Script,
    ULONG           ScriptSize,
    CG_SCRIPT_BASE *ScriptInfo,
    ULONG           InfoSize
)
{
    CGSTATUS    Status;
    JSON_OBJECT Object, *ScriptObject;
    CJsonParser JsonParser;

    Status = JsonParser.Parse(Script, ScriptSize, &Object);
    if (!CG_SUCCESS(Status))
        return Status;

    Status = STATUS_UNSUCCESSFUL;
    LOOP_ONCE
    {
        if (Object.Type != JSON_TYPE_OBJECT ||
            Object.Value.Object.Count < 1   ||
            Object.Value.Object.Object->Type != JSON_TYPE_OBJECT)
        {
            break;
        }

        ScriptObject = Object.Value.Object.Object;
        if (!StrICompare(ScriptObject->Name.Buffer, CG_SCRIPT_CONFIG_ROOT_TAG))
        {
            Status = ParseCoreConfig(ScriptObject, (CG_SCRIPT_CORE_CONFIG *)ScriptInfo, InfoSize);
        }
        else if (StrICompareW(ScriptObject->Name.Buffer, CG_SCRIPT_GAMELIST_ROOT_TAG))
        {
            ;
        }
    }

    JsonParser.Destroy(&Object);
    if (!CG_SUCCESS(Status))
        FreeScript(ScriptInfo);

    return Status;
}

#endif

#if 0

#define _JUNK_CODE(label, junk_bytes) \
            label: INLINE_ASM push label + 0xC3654321 + 0xE + junk_bytes \
            INLINE_ASM sub  dword ptr [esp], 0xC3654321 - junk_bytes + 4 \
            INLINE_ASM __emit 0xEB INLINE_ASM __emit 0xFD \
            INLINE_ASM __emit 0x28

#define JUNK_CODE() _JUNK_CODE(MAKE_UNIQUE_NAME(__COUNTER__), 1)

PCHAR SkipSpace(PCHAR p, BOOL Forward)
{
    ULONG delta = Forward ? 1 : -1;

    while (*p == ' ' || *p == '\t')
        p += delta;

    return p;
}

VOID AntiDllInject()
{
    ULONG Version, ClientLoadDllIndex;

    Version = 500;
    switch (Version)
    {
        case 500:
            ClientLoadDllIndex = 0x40;
            break;

        case 501:
        case 600:
            ClientLoadDllIndex = 0x42;
            break;

        case 601:
            ClientLoadDllIndex = 0x41;
            break;

        default:
            return;
    }
}

#define HANDLE_INDEX_MASK 0xFC000000u

template<class HandleType>
class HandleTableManager
{
protected:
    RTL_HANDLE_TABLE m_HandleTable;

    const static ULONG m_kHandleSize = sizeof(HandleType);

public:
    HandleTableManager()
    {
        ZeroMemory(&m_HandleTable, sizeof(m_HandleTable));
    }

    HandleTableManager(ULONG MaximumHandleCount)
    {
        Initialize(MaximumHandleCount);
    }

    ~HandleTableManager()
    {
        RtlDestroyHandleTable(&m_HandleTable);
    }

    VOID Initialize(ULONG MaximumHandleCount)
    {
        RtlInitializeHandleTable(
            MaximumHandleCount * m_kHandleSize,
            m_kHandleSize,
            &m_HandleTable
        );
    }

    HANDLE AllocateHandle(PRTL_HANDLE_TABLE_ENTRY *Object = NULL)
    {
        ULONG_PTR Handle;
        PRTL_HANDLE_TABLE_ENTRY Entry;

        if (Object != NULL)
            *Object = NULL;

        Entry = RtlAllocateHandle(&m_HandleTable, &Handle);
        if (Entry == NULL)
            return NULL;

        SET_FLAG(Entry->Flags, RTL_HANDLE_VALID);

        if (Object != NULL)
            *Object = Entry;

        return GetHandleByIndex(Handle);
    }

    BOOL ReferenceObjectByHandle(HANDLE Handle, HandleType **Object)
    {
        return IsValidHandle(Handle, (PVOID *)Object);
    }

    BOOL FreeHandle(HandleType *Object)
    {
        if (!RtlIsValidHandle(&m_HandleTable, (PRTL_HANDLE_TABLE_ENTRY)Object))
            return FALSE;

        return RtlFreeHandle(&m_HandleTable, (PRTL_HANDLE_TABLE_ENTRY)Object);
    }

    BOOL FreeHandle(HANDLE Handle)
    {
        HandleType *Object;

        if (!ReferenceObjectByHandle(Handle, &Object))
            return FALSE;

        return FreeHandle(Object);
    }

protected:
    BOOL IsValidHandle(HANDLE Handle, PVOID *Object = NULL)
    {
        ULONG_PTR Index;

        if (Handle == NULL || PtrAnd(Handle, 3) != 0)
            return FALSE;

        Index = GetIndexByHandle(Handle);

        return IsValidIndexHandle(Index, Object);
    }

    BOOL IsValidIndexHandle(ULONG_PTR Index, PVOID *Object = NULL)
    {
        PRTL_HANDLE_TABLE_ENTRY Entry;

        if (Object == NULL)
            Object = (PVOID *)&Entry;

        return RtlIsValidIndexHandle(&m_HandleTable, Index, (PRTL_HANDLE_TABLE_ENTRY *)Object);
    }

    ULONG_PTR GetIndexByHandle(HANDLE Handle)
    {
        return (ULONG_PTR)Handle / 4 - 1;
    }

    HANDLE GetHandleByIndex(ULONG_PTR Index)
    {
        return (HANDLE)(++Index * 4);
    }
};

struct HANDLE_OBJECT
{
    enum HandleObjectTypeClass
    {
        ObjectFile,
    };

    ULONG RefCount;
    ULONG Flags;        // HANDLE_FLAG_PROTECT_FROM_CLOSE
    ULONG ObjectType;

    union
    {
        struct
        {
            UNICODE_STRING  FileName;
            LARGE_INTEGER   FileSize;
            LARGE_INTEGER   CurrentPosition;
        } FileObject;

    } Data;

    HANDLE_OBJECT()
    {
        RefCount    = 1;
        Flags       = 0;
    }

    ULONG AddRef()
    {
        return _InterlockedIncrement((PLONG)&RefCount);
    }

    ULONG Release()
    {
        ULONG Ref;

        Ref = _InterlockedDecrement((PLONG)&RefCount);
        if (Ref == 0)
            delete this;

        return Ref;
    }
};

DECL_ALIGN(8) struct HANDLE_ENTRY : public RTL_HANDLE_TABLE_ENTRY
{
    HANDLE_OBJECT *Object;
};

typedef enum
{
    RTMP_HEADER_LENGTH_12   = 0,
    RTMP_HEADER_LENGTH_8    = 1,
    RTMP_HEADER_LENGTH_4    = 2,
    RTMP_HEADER_LENGTH_1    = 3,

} RtmpHeaderLengthClass;

DECL_ALIGN(1) struct RTMP_HEADER
{
    union
    {
        struct
        {
            BYTE Type   : 6;
            BYTE Length : 2;
        };

        ULONG TimeStamp;
    };

    BYTE  AMFSize[3];
    BYTE  AMFType;
    ULONG StreamID;

    ULONG GetType()
    {
        return Type;
    }

    ULONG GetLength()
    {
        BYTE RtmpLengthMap[] = { 12, 8, 4, 1 };

        return Length > countof(RtmpLengthMap) ? -1 : RtmpLengthMap[Length];
    }

    ULONG GetLengthRaw()
    {
        return Length;
    }

    ULONG GetTimeStamp()
    {
        return Bswap(TimeStamp >> 8);
    }

    ULONG GetAMFSize()
    {
        ULONG Size = *(PULONG)AMFSize & 0xFFFFFF;

        return ((Size & 0xFF) << 16) | (Size & 0x0000FF00) | (Size >> 16);
    }

    ULONG GetAMFType()
    {
        return AMFType;
    }

    ULONG GetStreamID()
    {
        return Bswap(StreamID);
    }

    PVOID GetAMFData()
    {
        return PtrAdd((PVOID)this, GetLength());
    }
};

typedef enum
{
    AMF_TYPE_NUMBER         = 0x00,
    AMF_TYPE_BOOLEAN        = 0x01,
    AMF_TYPE_STRING         = 0x02,
    AMF_TYPE_OBJECT         = 0x03,
    AMF_TYPE_MOVIECLIP      = 0x04 ,
    AMF_TYPE_NULL           = 0x05,
    AMF_TYPE_UNDEFINED      = 0x06,
    AMF_TYPE_REFERENCE      = 0x07,
    AMF_TYPE_ECMA_ARRAY     = 0x08,
    AMF_TYPE_END_OF_OBJECT  = 0x09,
    AMF_TYPE_ARRAY          = 0x0A,
    AMF_TYPE_DATE           = 0x0B,
    AMF_TYPE_LONG_STRING    = 0x0C,
    AMF_TYPE_UNSUPPORTED    = 0x0D,
    AMF_TYPE_RECORDSET      = 0x0E,
    AMF_TYPE_XML            = 0x0F,
    AMF_TYPE_TYPED_OBJECT   = 0x10,
    AMF_TYPE_AMF3_OBJECT    = 0x11,

} AmfTypeClass;

#endif

#endif



















/*

void CPUUsage()
{
    SYSTEM_PERFORMANCE_INFORMATION SysPerfInfo;
    SYSTEM_TIME_INFORMATION SysTimeInfo;
    SYSTEM_BASIC_INFORMATION SysBaseInfo;
    DOUBLE dbIdleTime;
    LONG64 dbSystemTime;
    LONG status;
    LARGE_INTEGER liOldIdleTime = {0,0};
    LARGE_INTEGER liOldSystemTime = {0,0};

    // get number of processors in the system
    status = NtQuerySystemInformation(SystemBasicInformation,
        &SysBaseInfo, sizeof(SysBaseInfo), NULL);

    printf("CPU Usage\n");
    while(!_kbhit())
    {
        // get new system time
        NtQuerySystemInformation(SystemTimeInformation, &SysTimeInfo, sizeof(SysTimeInfo), 0);
        // get new CPU'sname idle time
        NtQuerySystemInformation(SystemPerformanceInformation,
            &SysPerfInfo, sizeof(SysPerfInfo), NULL);

        // if it'sname a first call-skip it
        if (liOldIdleTime.QuadPart != 0)
        {
            // CurrentValue = NewValue - OldValue
            dbIdleTime   = (DOUBLE)SysPerfInfo.liIdleTime.QuadPart - liOldIdleTime.QuadPart;
            dbSystemTime = SysTimeInfo.liKeSystemTime.QuadPart - liOldSystemTime.QuadPart;

            // CurrentCpuIdle = IdleTime / SystemTime
            dbIdleTime = dbIdleTime / dbSystemTime;

            // CurrentCpuUsage% = 100 - (CurrentCpuIdle * 100) / NumberOfProcessors
            dbIdleTime = 100.0 - dbIdleTime * 100.0 / SysBaseInfo.bKeNumberProcessors + 0.5;

            printf("%d%%             \r",(UINT)dbIdleTime);
        }

        // store new CPU'sname idle and system time
        liOldIdleTime = SysPerfInfo.liIdleTime;
        liOldSystemTime = SysTimeInfo.liKeSystemTime;

        // wait one second
        Sleep(1000);
    }
    printf("\n");
}
*/
// & > ^ > |
