#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker, "/SECTION:.Amano,ERW /MERGE:.text=.Amano")

#include "MyLibrary.cpp"

SHIM_HOOK_API_INFO*
STDCALL
GetHookAPIs(
    IN  PCWSTR ShimCommandLine,
    IN  PCWSTR CompatibilityFixName,
    OUT PULONG HookApiCount
)
{
    *HookApiCount = 0;
    return NULL;
}

VOID
STDCALL
NotifyShims(
    IN ULONG       Reason,
    IN PLDR_MODULE LoadedDll
)
{
    switch (Reason)
    {
        case SE_PROCESS_ATTACH:
            break;

        case SE_PROCESS_DETACH:
            break;
    }
}

TYPE_OF(NtCreateFile) *StubNtCreateFile;

NTSTATUS
NTAPI
HkNtCreateFile(
    PHANDLE             FileHandle,
    ACCESS_MASK         DesiredAccess,
    POBJECT_ATTRIBUTES  ObjectAttributes,
    PIO_STATUS_BLOCK    IoStatusBlock,
    PLARGE_INTEGER      AllocationSize OPTIONAL,
    ULONG               FileAttributes,
    ULONG               ShareAccess,
    ULONG               CreateDisposition,
    ULONG               CreateOptions,
    PVOID               EaBuffer,
    ULONG               EaLength
)
{
    if (Nt_FindThreadFrameByContext(TAG4('SHIM')) == NULL) LOOP_ONCE
    {
        TEB_ACTIVE_FRAME frame;

        if (ObjectAttributes == NULL)
            break;

        if (ObjectAttributes->ObjectName == NULL)
            break;

        if (ObjectAttributes->ObjectName->Buffer == NULL)
            break;

        if (ObjectAttributes->ObjectName->Length == 0)
            break;

        static WCHAR path[] = L"\\??\\C:\\Windows\\system32\\";

        if (StrNICompareW(ObjectAttributes->ObjectName->Buffer, path, CONST_STRLEN(path)))
            break;

        if (wcsstr(ObjectAttributes->ObjectName->Buffer, L".sys") == NULL)
            break;

        frame.Context = TAG4('SHIM');
        frame.Push();
        {
            FILE *fp = _wfopen(L"C:\\xlog.txt", L"ab");

            fwprintf(fp,
                L"%p %s %wZ\r\n",
                Nt_GetCurrentProcessId(),
                Nt_FindLdrModuleByHandle(NULL)->FullDllName.Buffer,
                ObjectAttributes->ObjectName
            );

            fclose(fp);

            LOOP_FOREVER
            {
                Nt_Sleep(1000);
            }
        }
        frame.Pop();
    }

    return StubNtCreateFile(FileHandle, DesiredAccess,  ObjectAttributes, IoStatusBlock, AllocationSize, FileAttributes, ShareAccess, CreateDisposition, CreateOptions, EaBuffer, EaLength);
}

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    LdrDisableThreadCalloutsForDll(BaseAddress);

    MEMORY_FUNCTION_PATCH fn[] =
    {
        INLINE_HOOK_JUMP(NtCreateFile, HkNtCreateFile, StubNtCreateFile),
    };

    Nt_PatchMemory(NULL, 0, fn, countof(fn));

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
