#include "Stdafx.h"
#include "MyLibrary.cpp"

PVOID DllBaseAddress;

BOOL UnInitialize(PVOID BaseAddress)
{
    ml::MlUnInitialize();
    return FALSE;
}

extern PyGetSetDef PyAMFBody_GetSetList[];

NTSTATUS AppendSelfPathToPath(PVOID BaseAddress)
{
    UNICODE_STRING  Path;
    PLDR_MODULE     Module;
    PWSTR           Buffer, SelfPath;
    ULONG_PTR       Length;

    Buffer = (PWSTR)AllocStack(CurrentPeb()->ProcessParameters->EnvironmentSize);
    RtlInitEmptyString(&Path, Buffer, CurrentPeb()->ProcessParameters->EnvironmentSize);
    FAIL_RETURN(RtlExpandEnvironmentStrings_U(nullptr, &USTR(L"%Path%"), &Path, nullptr));

    Module = FindLdrModuleByHandle(BaseAddress);
    SelfPath = (PWSTR)AllocStack(Module->FullDllName.Length + sizeof(*SelfPath));

    CopyMemory(SelfPath, Module->FullDllName.Buffer, Module->FullDllName.Length + sizeof(*SelfPath));
    rmnamew(SelfPath);

    Length = StrLengthW(SelfPath);

    Buffer = Path.Buffer;
    LOOP_FOREVER
    {
        Buffer = wcsstr(Buffer, SelfPath);
        if (Buffer == nullptr)
            break;

        if (Buffer[Length] == ';' || Buffer[Length] == 0)
            return STATUS_SUCCESS;

        Buffer += Length;
    }

    Buffer = PtrAdd(Path.Buffer, Path.Length);
    *Buffer++ = ';';

    CopyMemory(Buffer, SelfPath, (Length + 1) * sizeof(*SelfPath));
    Path.Length += (Length + 1) * sizeof(*SelfPath);

    return RtlSetEnvironmentVariable(nullptr, &USTR(L"Path"), &Path);
}

BOOL Initialize(PVOID BaseAddress)
{
    ml::MlInitialize();

    //AppendSelfPathToPath(BaseAddress);

    DllBaseAddress = BaseAddress;

    return TRUE;
}

BOOL WINAPI DllMain(PVOID BaseAddress, ULONG Reason, PVOID Reserved)
{
    //ManagedDllMain(BaseAddress, Reason, Reserved);
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
