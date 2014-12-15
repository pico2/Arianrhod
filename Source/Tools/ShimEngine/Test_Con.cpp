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

#include "MyLibrary.cpp"

#if defined(UNICODE)
#define __WSTRING(str) L##str
#define WSTRING(str) __WSTRING(str)
#else
#define WSTRING(str) (str)
#endif

OVERLOAD_CPP_NEW_WITH_HEAP(MemoryAllocator::GetGlobalHeap())

static WCHAR SdbInstaller[] = L"sdbinst.exe";

VOID NotifyApplications()
{
    SendNotifyMessageW(HWND_BROADCAST, WM_WININICHANGE, NULL, (LPARAM)L"Environment");
//    if (IsUserAnAdmin())
    {
//        ULONG Recipients = BSM_APPLICATIONS;
//        BroadcastSystemMessageW(BSF_QUERY, &Recipients, WM_WININICHANGE, 0, (LPARAM)L"Environment");
    }
}

NTSTATUS UnInstallShimDatabase(PCWSTR DatabasePath)
{
    PDB             Sdb;
    GUID            DatabaseGuid;
    BOOL            Result;
    WCHAR           CommandLine[MAX_NTPATH + 0x50];
    ULONG           Length;
    NTSTATUS        Status;
    UNICODE_STRING  GuidString;
    STARTUPINFOW    StartupInfo;

    Length = Nt_GetWindowsDirectory(CommandLine, MAX_NTPATH);
    CopyStruct(CommandLine + Length, L"AppPatch\\ShimEng.dll", sizeof(L"AppPatch\\ShimEng.dll"));
    Nt_DeleteFile(CommandLine);

    Sdb = SdbOpenDatabase(DatabasePath, DOS_PATH);
    if (Sdb == NULL)
        return STATUS_UNSUCCESSFUL;

    Result = SdbGetDatabaseID(Sdb, &DatabaseGuid);
    SdbCloseDatabase(Sdb);
    if (!Result)
        return STATUS_UNSUCCESSFUL;

    Status = RtlStringFromGUID(DatabaseGuid, &GuidString);
    if (!NT_SUCCESS(Status))
        return Status;

    Length = Nt_GetSystemDirectory(CommandLine, ARRAYSIZE(CommandLine));
    CopyStruct(CommandLine + Length, SdbInstaller, sizeof(SdbInstaller));
    Length += CONST_STRLEN(SdbInstaller);
    *(PULONG64)&CommandLine[Length] = TAG4W(' -g ');
    Length += 4;
    CopyMemory(CommandLine + Length, GuidString.Buffer, GuidString.Length);
    CommandLine[Length + GuidString.Length / sizeof(WCHAR)] = 0;

    RtlFreeUnicodeString(&GuidString);

    ZeroMemory(&StartupInfo, sizeof(StartupInfo));
    StartupInfo.cb = sizeof(StartupInfo);
    StartupInfo.dwFlags = STARTF_USESHOWWINDOW;
    StartupInfo.wShowWindow = SW_HIDE;

    Status = Nt_CreateProcess(NULL, CommandLine);
    if (!NT_SUCCESS(Status))
        return Status;

    Status = Nt_RegDeleteValue(
                HKEY_LOCAL_MACHINE,
                L"SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment",
                L"__COMPAT_LAYER"
             );

    NotifyApplications();

    return Status == ERROR_SUCCESS ? STATUS_SUCCESS : STATUS_UNSUCCESSFUL;
}

NTSTATUS InstallShimDatabase(PCWSTR DatabasePath)
{
    WCHAR           CommandLine[MAX_NTPATH * 2 + 0x20];
    PWCHAR          SourceEngine, DestinationEngine;
    ULONG           Length;
    STARTUPINFOW    StartupInfo;
    NTSTATUS        Status;
    static WCHAR    CompatibilityLayer[] = L"# ShimEngineTestSdb";

    SourceEngine = CommandLine;
    DestinationEngine = CommandLine + MAX_NTPATH + 0x10;
    Length = Nt_GetExeDirectory(SourceEngine, MAX_NTPATH);
    CopyStruct(SourceEngine + Length, L"ShimEng.dll", sizeof(L"ShimEng.dll"));

    Length = Nt_GetWindowsDirectory(DestinationEngine, MAX_NTPATH);
    CopyStruct(DestinationEngine + Length, L"AppPatch\\ShimEng.dll", sizeof(L"AppPatch\\ShimEng.dll"));

    Nt_CopyFile(SourceEngine, DestinationEngine, FALSE);

    Length = Nt_GetSystemDirectory(CommandLine, ARRAYSIZE(CommandLine));
    CopyStruct(CommandLine + Length, SdbInstaller, sizeof(SdbInstaller));
    Length += CONST_STRLEN(SdbInstaller);
    *(PULONG64)&CommandLine[Length] = TAG4W(' -q ');
    Length += 4;
    CommandLine[Length++] = '"';
    Length += RtlGetFullPathName_U(DatabasePath, sizeof(CommandLine) - Length * sizeof(WCHAR), CommandLine + Length, NULL) / sizeof(WCHAR);
    CommandLine[Length++] = '"';
    CommandLine[Length++] = 0;

    ZeroMemory(&StartupInfo, sizeof(StartupInfo));
    StartupInfo.cb = sizeof(StartupInfo);
    StartupInfo.dwFlags = STARTF_USESHOWWINDOW;
    StartupInfo.wShowWindow = SW_HIDE;

    Status = Nt_CreateProcess(NULL, CommandLine, NULL, 0, &StartupInfo);
    if (!NT_SUCCESS(Status))
        return Status;

    Status = Nt_RegSetValue(
                HKEY_LOCAL_MACHINE,
                L"SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment",
                L"__COMPAT_LAYER",
                REG_SZ,
                CompatibilityLayer,
                sizeof(CompatibilityLayer)
             );
/*
    Status = SHSetValueW(
                HKEY_LOCAL_MACHINE,
                L"SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment",
                L"__COMPAT_LAYER",
                REG_SZ,
                CompatibilityLayer,
                sizeof(CompatibilityLayer)
             );
*/
    if (!NT_SUCCESS(Status))
    {
        UnInstallShimDatabase(DatabasePath);
        return STATUS_UNSUCCESSFUL;
    }

    NotifyApplications();

    return STATUS_SUCCESS;
}

Void main2(Int argc, TChar **argv)
{
    NotifyApplications();

    return;

    InstallShimDatabase(L"applocale_mod.sdb");
    PauseConsole();
    UnInstallShimDatabase(L"applocale_mod.sdb");
}
