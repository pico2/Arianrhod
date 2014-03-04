#include "stdafx.h"

typedef struct
{
    USHORT  Size;
    USHORT  Unknown;
    WCHAR   Version16Name[1];

} IMAGE_VERSION_INFO_DATA_ENTRY, *PIMAGE_VERSION_INFO_DATA_ENTRY;

PVOID SearchLdrInitNtContinue()
{
    return WalkOpCodeT(LdrInitializeThunk, 0x25,
                WalkOpCodeM(Buffer, OpLength, Ret)
                {
                    if (Buffer[0] == CALL && (PVOID)GetCallDestination(Buffer) == NtContinue)
                    {
                        Ret = Buffer;
                        return STATUS_SUCCESS;
                    }

                    return STATUS_NOT_FOUND;
                }
            );
}

NTSTATUS ReplaceMUIVersionLocaleInfo(PVOID& VersionData, ULONG& VersionSize)
{
    PVOID       TlbBuffer;
    PBYTE       Buffer;
    LONG_PTR    Size;
    PUSHORT     LangID, CharsetID;
    PIMAGE_VERSION_INFO_DATA_ENTRY Entry;

    static WCHAR VarFileInfo[] = L"VarFileInfo";
    static WCHAR Translation[] = L"Translation";

    TlbBuffer = (PBYTE)THREAD_LOCAL_BUFFER::GetTlb(TRUE)->GetBuffer();
    if (TlbBuffer == nullptr)
        return STATUS_NO_MEMORY;

    CopyMemory(TlbBuffer, VersionData, VersionSize);

    Entry = (PIMAGE_VERSION_INFO_DATA_ENTRY)TlbBuffer;
    Size = Entry->Size;

    if (Size < 8 || Size > 0x8000)
        return STATUS_DATA_NOT_ACCEPTED;

    // ansi version
    if (Entry->Version16Name[0] == TAG2('VS'))
        return STATUS_DATA_NOT_ACCEPTED;

    Buffer = (PBYTE)KMP(Entry, Size, VarFileInfo, sizeof(VarFileInfo));
    if (Buffer == nullptr)
        return STATUS_RESOURCE_DATA_NOT_FOUND;

    Size = Entry->Size - PtrOffset(Buffer, Entry) - sizeof(VarFileInfo);
    if (Size <= 0)
        return STATUS_RESOURCE_DATA_NOT_FOUND;

    Buffer += sizeof(VarFileInfo);

    Buffer = (PBYTE)KMP(Buffer, Size, Translation, sizeof(Translation));
    if (Buffer == nullptr)
        return STATUS_RESOURCE_DATA_NOT_FOUND;

    Size = Entry->Size - PtrOffset(Buffer, Entry) - sizeof(Translation);
    if (Size <= 0)
        return STATUS_RESOURCE_DATA_NOT_FOUND;

    Entry = (PIMAGE_VERSION_INFO_DATA_ENTRY)PtrSub(Buffer, 6);

    LangID = (PUSHORT)PtrAdd(Entry, ROUND_DOWN(CONST_STRSIZE(Translation) + 11, 4));
    CharsetID = LangID + 1;

    *LangID = LeGetGlobalData()->GetLeb()->LocaleID;

    VersionData = TlbBuffer;

    return STATUS_SUCCESS;
}

NTSTATUS QueryRegKeyFullPath(HANDLE Key, PUNICODE_STRING KeyFullPath)
{
    NTSTATUS                    Status;
    PKEY_NAME_INFORMATION       KeyFullName;
    ULONG_PTR                   MaxLength;
    ULONG                       ReturnedLength;

    KeyFullName = nullptr;
    MaxLength   = 0;

    LOOP_FOREVER
    {
        Status = NtQueryKey(Key, KeyNameInformation, KeyFullName, MaxLength, &ReturnedLength);
        if (Status != STATUS_BUFFER_TOO_SMALL)
            break;

        KeyFullName = (PKEY_NAME_INFORMATION)ReAllocateMemoryP(KeyFullName, ReturnedLength + sizeof(WCHAR));
        if (KeyFullName == nullptr)
        {
            Status = STATUS_NO_MEMORY;
            break;
        }

        MaxLength = ReturnedLength;
    }

    if (NT_SUCCESS(Status))
    {
        PtrAdd(KeyFullName->Name, KeyFullName->NameLength)[0] = 0;
        Status = RtlCreateUnicodeString(KeyFullPath, KeyFullName->Name) ? STATUS_SUCCESS : STATUS_NO_MEMORY;
    }

    FreeMemoryP(KeyFullName);
    return Status;
}

NoInline PVOID FASTCALL LoadSelfAsFirstDll(PVOID ReturnAddress)
{
    PVOID   BaseToFree;
    PLEPEB  LePeb;

    BaseToFree = nullptr;

    LOOP_ONCE
    {
        PVOID DllHandle;

        LePeb = OpenOrCreateLePeb();
        if (LePeb == nullptr)
            break;

        // LePeb->SelfShadowToFree = &__ImageBase;

        WriteProtectMemory(CurrentProcess, LePeb->LdrLoadDllAddress, LePeb->LdrLoadDllBackup, LePeb->LdrLoadDllBackupSize);

        UNICODE_STRING DllPath;

        RtlInitUnicodeString(&DllPath, LePeb->LeDllFullPath);

        if (NT_FAILED(LdrLoadDll(nullptr, nullptr, &DllPath, &DllHandle)))
        {
            CloseLePeb(LePeb);
            break;
        }

        *(PULONG_PTR)_AddressOfReturnAddress() += PtrOffset(DllHandle, &__ImageBase);

        CloseLePeb(LePeb);

        BaseToFree = &__ImageBase;
    }

    return BaseToFree;
}

NTSTATUS
NTAPI
LoadFirstDll(
    PWCHAR              PathToFile OPTIONAL,
    PULONG              DllCharacteristics OPTIONAL,
    PCUNICODE_STRING    ModuleFileName,
    PVOID*              DllHandle
)
{
    PVOID BaseToFree;

    //ExceptionBox(L"inject");

    BaseToFree = LoadSelfAsFirstDll(_ReturnAddress());
    if (BaseToFree != nullptr)
        Mm::FreeVirtualMemory(BaseToFree);

    return LdrLoadDll(PathToFile, DllCharacteristics, ModuleFileName, DllHandle);
}

NTSTATUS
HPCALL
LeNtQuerySystemInformation(
    HPARGS
    SYSTEM_INFORMATION_CLASS    SystemInformationClass,
    PVOID                       SystemInformation,
    ULONG_PTR                   SystemInformationLength,
    PULONG                      ReturnLength OPTIONAL
)
{
    NTSTATUS Status = 0;
    PLeGlobalData GlobalData = (PLeGlobalData)HpGetFilterContext();

    switch (SystemInformationClass)
    {
        case SystemCurrentTimeZoneInformation:
            if (SystemInformation == nullptr)
                break;

            if (SystemInformationLength < sizeof(GlobalData->GetLeb()->Timezone))
                break;

            *((PRTL_TIME_ZONE_INFORMATION)SystemInformation) = GlobalData->GetLeb()->Timezone;

            if (ReturnLength != nullptr)
                *ReturnLength = SystemInformationLength;

            HpSetFilterAction(BlockSystemCall);

            return STATUS_SUCCESS;
    }

    return Status;
}

NTSTATUS
HPCALL
LeNtQueryInformationThread(
    HPARGS
    HANDLE          ThreadHandle,
    THREADINFOCLASS ThreadInformationClass,
    PVOID           ThreadInformation,
    ULONG           ThreadInformationLength,
    PULONG          ReturnLength
)
{
    NTSTATUS Status;

    switch (ThreadInformationClass)
    {
        case ThreadTimes:
            break;

        default:
            return 0;
    }

    HpSetFilterAction(BlockSystemCall);

    Status = HpCallSysCall(NtQueryInformationThread, ThreadHandle, ThreadInformationClass, ThreadInformation, ThreadInformationLength, ReturnLength);
    FAIL_RETURN(Status);

    PKERNEL_USER_TIMES Times;

    Times = (PKERNEL_USER_TIMES)ThreadInformation;

    //Times->CreateTime.QuadPart = 0;
    Times->KernelTime.QuadPart = 0x26161;
    Times->UserTime.QuadPart = 0x26161;

    AllocConsole();
    PrintConsoleW(L"%I64X, %I64X\n", Times->KernelTime, Times->UserTime);

    return Status;
}

NTSTATUS LeGlobalData::InjectSelfToChildProcess(HANDLE Process, PCLIENT_ID Cid)
{
    NTSTATUS    Status;
    PVOID       SelfShadow, LocalSelfShadow, ShadowLoadFirstDll;
    ULONG_PTR   SizeOfImage, ExtraSize;
    LONG        Offset;
    PLEPEB      TargetLePeb, LePeb;
    HANDLE      Section;
    BYTE        Backup[LDR_LOAD_DLL_BACKUP_SIZE];

    // Process = CurrentProcess;

    if (this->Wow64 && !Ps::IsWow64Process(Process))
        return STATUS_NOT_SUPPORTED;

    SizeOfImage = FindLdrModuleByHandle(&__ImageBase)->SizeOfImage;

    SelfShadow = nullptr;
    Status = AllocVirtualMemoryEx(Process, &SelfShadow, SizeOfImage);
    if (NT_FAILED(Status))
        return Status;

    LocalSelfShadow = AllocateMemoryP(SizeOfImage);
    if (LocalSelfShadow == nullptr)
    {
        Mm::FreeVirtualMemory(SelfShadow, Process);
        return STATUS_NO_MEMORY;
    }

    CopyMemory(LocalSelfShadow, &__ImageBase, SizeOfImage);
    RelocPeImage(LocalSelfShadow, &__ImageBase, nullptr, SelfShadow);

    Status = WriteMemory(Process, SelfShadow, LocalSelfShadow, SizeOfImage);
    FreeMemoryP(LocalSelfShadow);

    if (NT_FAILED(Status))
    {
        Mm::FreeVirtualMemory(SelfShadow, Process);
        return Status;
    }

    LePeb = GetLePeb();

    PVOID ooxxAddress = LePeb->LdrLoadDllAddress;
    BYTE ooxxBuffer[16];

    Status = ReadMemory(Process, ooxxAddress, Backup, LDR_LOAD_DLL_BACKUP_SIZE);
    if (NT_FAILED(Status))
    {
        Mm::FreeVirtualMemory(SelfShadow, Process);
        return Status;
    }

    ShadowLoadFirstDll = PtrAdd(LoadFirstDll, PtrOffset(SelfShadow, &__ImageBase));
    Offset = PtrOffset(ShadowLoadFirstDll, PtrAdd(ooxxAddress, 5));

    ooxxBuffer[0] = JUMP;
    *(PULONG)&ooxxBuffer[1] = Offset;

    Status = WriteProtectMemory(Process, ooxxAddress, ooxxBuffer, 5);
    if (NT_FAILED(Status))
    {
        Mm::FreeVirtualMemory(SelfShadow, Process);
        return Status;
    }

    ExtraSize = this->GetLePeb()->RegistryReplacementEntry.GetSize() * sizeof(TargetLePeb->Leb.RegistryReplacement[0]);
    if (ExtraSize != 0)
    {
        PREGISTRY_REPLACEMENT_ENTRY Entry;
        FOR_EACH_VEC(Entry, this->GetLePeb()->RegistryReplacementEntry)
        {
            ExtraSize += Entry->Origin.DataSize + Entry->Replacement.DataSize;
            ExtraSize += Entry->Origin.SubKey.GetSize() + Entry->Replacement.SubKey.GetSize();
            ExtraSize += Entry->Origin.Value.GetSize() + Entry->Replacement.Value.GetSize();
        }
    }

    TargetLePeb = OpenOrCreateLePeb((ULONG_PTR)Cid->UniqueProcess, TRUE, ExtraSize);
    if (TargetLePeb == nullptr)
        return STATUS_UNSUCCESSFUL;

    Section = TargetLePeb->Section;
    *TargetLePeb = *LePeb;
    TargetLePeb->Section = Section;
    CopyStruct(TargetLePeb->LdrLoadDllBackup, Backup, LDR_LOAD_DLL_BACKUP_SIZE);
    TargetLePeb->LdrLoadDllBackupSize = LDR_LOAD_DLL_BACKUP_SIZE;

    CloseLePeb(TargetLePeb);

    return STATUS_SUCCESS;
}

NTSTATUS
HPCALL
LeNtCreateUserProcess(
    HPARGS
    PHANDLE                         ProcessHandle,
    PHANDLE                         ThreadHandle,
    ACCESS_MASK                     ProcessDesiredAccess,
    ACCESS_MASK                     ThreadDesiredAccess,
    POBJECT_ATTRIBUTES              ProcessObjectAttributes,
    POBJECT_ATTRIBUTES              ThreadObjectAttributes,
    ULONG                           ProcessFlags,
    ULONG                           ThreadFlags,
    PRTL_USER_PROCESS_PARAMETERS    ProcessParameters,
    PPS_CREATE_INFO                 CreateInfo,
    PPS_ATTRIBUTE_LIST              AttributeList
)
{
    PLEPEB              TargetLePeb;
    NTSTATUS            Status, Status2;
    PLeGlobalData       GlobalData;
    PPS_ATTRIBUTE_LIST  LocalAttributeList;
    PPS_ATTRIBUTE       Attribute;
    CLIENT_ID           LocalCid, *Cid;
    ULONG_PTR           ReturnLength;
    LONG                Offset;
    PVOID               SelfShadow;

    HpSetFilterAction(BlockSystemCall);

    WriteLog(L"create proc");

    LocalAttributeList = nullptr;
    Attribute = nullptr;
    Cid = nullptr;

    if (AttributeList != nullptr)
    {
        ULONG_PTR Count;

        Attribute = AttributeList->Attributes;
        Count = (PPS_ATTRIBUTE)PtrAdd(AttributeList, AttributeList->TotalLength) - Attribute;
        FOR_EACH(Attribute, AttributeList->Attributes, Count)
        {
            if (Attribute->AttributeNumber != PsAttributeClientId)
                continue;

//            if (Attribute->AttributeFlags != PS_ATTRIBUTE_FLAG_THREAD)
//                break;

            Cid = (PCLIENT_ID)Attribute->ValuePtr;
            break;
        }
    }

    if (Cid == nullptr)
    {
        ULONG_PTR ListLength;

        ListLength = (AttributeList != nullptr ? AttributeList->TotalLength : sizeof(AttributeList->TotalLength)) + sizeof(*Attribute);
        LocalAttributeList = (PPS_ATTRIBUTE_LIST)AllocStack(ListLength);

        if (AttributeList != nullptr)
            CopyMemory(LocalAttributeList, AttributeList, AttributeList->TotalLength);

        LocalAttributeList->TotalLength = ListLength;
        Attribute = (PPS_ATTRIBUTE)PtrAdd(LocalAttributeList, LocalAttributeList->TotalLength) - 1;

        Attribute->AttributeNumber  = PsAttributeClientId;
        Attribute->AttributeFlags   = PS_ATTRIBUTE_FLAG_THREAD;
        Attribute->ValuePtr         = &LocalCid;
        Attribute->Size             = sizeof(LocalCid);
        Attribute->ReturnLength     = &ReturnLength;

        Cid = &LocalCid;

        AttributeList = LocalAttributeList;
    }

    Status = HpCallSysCall(
                NtCreateUserProcess,
                ProcessHandle,
                ThreadHandle,
                ProcessDesiredAccess,
                ThreadDesiredAccess,
                ProcessObjectAttributes,
                ThreadObjectAttributes,
                ProcessFlags,
                ThreadFlags,
                ProcessParameters,
                CreateInfo,
                AttributeList
            );

    WriteLog(L"create proc %p", Status);

    if (NT_FAILED(Status))
        return Status;

    GlobalData = (PLeGlobalData)HpGetFilterContext();

    Status2 = GlobalData->InjectSelfToChildProcess(*ProcessHandle, Cid);

    WriteLog(L"inject %p", Status2);

    return Status;
}

NTSTATUS
HPCALL
LeNtInitializeNlsFiles(
    HPARGS
    PVOID*          BaseAddress,
    PLCID           DefaultLocaleId,
    PLARGE_INTEGER  DefaultCasingTableSize
)
{
    NTSTATUS Status;
    PLeGlobalData GlobalData;

    HpSetFilterAction(BlockSystemCall);

    Status = HpCallSysCall(
                NtInitializeNlsFiles,
                BaseAddress,
                DefaultLocaleId,
                DefaultCasingTableSize
            );

    FAIL_RETURN(Status);

    GlobalData = (PLeGlobalData)HpGetFilterContext();

    *DefaultLocaleId = GlobalData->GetLeb()->LocaleID;

    return Status;
}

NTSTATUS
HPCALL
LeNtTerminateThread(
    HPARGS
    HANDLE      ThreadHandle,
    NTSTATUS    ExitStatus
)
{
    if (ThreadHandle == CurrentThread || ThreadHandle == nullptr)
    {
        THREAD_LOCAL_BUFFER::ReleaseTlb();
    }

    return 0;
}

NTSTATUS
HPCALL
LeNtQueryValueKey(
    HPARGS
    HANDLE                      KeyHandle,
    PUNICODE_STRING             ValueName,
    KEY_VALUE_INFORMATION_CLASS KeyValueInformationClass,
    PVOID                       KeyValueInformation,
    ULONG                       Length,
    PULONG                      ResultLength
)
{
    NTSTATUS        Status;
    UNICODE_STRING  KeyFulPath;
    PLeGlobalData   GlobalData;
    ULONG_PTR       KeyType, BufferLength;
    WCHAR           Buffer[MAX_NTPATH];

    enum { CodePageKeyHandle, LanguageKeyHandle };

    if (NT_FAILED(RtlValidateUnicodeString(0, ValueName)))
        return 0;

    Status = QueryRegKeyFullPath(KeyHandle, &KeyFulPath);
    FAIL_RETURN(Status);

    GlobalData = (PLeGlobalData)HpGetFilterContext();

    if (RtlEqualUnicodeString(&KeyFulPath, &GlobalData->HookRoutineData.Ntdll.CodePageKey, TRUE))
    {
        KeyType = CodePageKeyHandle;
    }
    else if (RtlEqualUnicodeString(&KeyFulPath, &GlobalData->HookRoutineData.Ntdll.LanguageKey, TRUE))
    {
        KeyType = LanguageKeyHandle;
    }
    else
    {
        RtlFreeUnicodeString(&KeyFulPath);
        return 0;
    }

    RtlFreeUnicodeString(&KeyFulPath);

    switch (KeyType)
    {
        default:
            return 0;

        case CodePageKeyHandle:
            if (RtlEqualUnicodeString(ValueName, &USTR(REGKEY_ACP), TRUE))
            {
                BufferLength = swprintf(Buffer, L"%d", GlobalData->GetLeb()->AnsiCodePage);
            }
            else if (RtlEqualUnicodeString(ValueName, &USTR(REGKEY_OEMCP), TRUE))
            {
                BufferLength = swprintf(Buffer, L"%d", GlobalData->GetLeb()->OemCodePage);
            }
            else
            {
                return 0;
            }
            break;

        case LanguageKeyHandle:
            if (RtlEqualUnicodeString(ValueName, &USTR(REGKEY_DEFAULT_LANGUAGE), TRUE))
            {
                BufferLength = swprintf(Buffer, L"%04x", GlobalData->GetLeb()->LocaleID);
            }
            else
            {
                return 0;
            }
            break;
    }

    ++BufferLength;
    BufferLength *= sizeof(WCHAR);

    HpSetFilterAction(BlockSystemCall);

    Status = HpCallSysCall(
                NtQueryValueKey,
                KeyHandle,
                ValueName,
                KeyValueInformationClass,
                KeyValueInformation,
                Length,
                ResultLength
            );

    if (Status == STATUS_BUFFER_TOO_SMALL)
    {
        if (ResultLength != nullptr)
            *ResultLength += BufferLength;
    }

    if (NT_FAILED(Status))
        return Status;

    union
    {
        PKEY_VALUE_PARTIAL_INFORMATION          PartialInfo;
        PKEY_VALUE_PARTIAL_INFORMATION_ALIGN64  PartialInfoAlign64;
        PKEY_VALUE_FULL_INFORMATION             FullInfo;
        PVOID                                   ValueInformation;
    };

    ValueInformation = KeyValueInformation;

    switch (KeyValueInformationClass)
    {
        case KeyValuePartialInformation:
            if (PartialInfo->Type != REG_SZ)
                break;

            CopyMemory(PartialInfo->Data, Buffer, BufferLength);
            PartialInfo->DataLength = BufferLength - sizeof(WCHAR);
            break;

        case KeyValueFullInformation:
            if (FullInfo->Type != REG_SZ)
                break;

            CopyMemory(PtrAdd(FullInfo, FullInfo->DataOffset), Buffer, BufferLength);
            FullInfo->DataLength = BufferLength - sizeof(WCHAR);
            break;

        case KeyValuePartialInformationAlign64:
            if (PartialInfoAlign64->Type != REG_SZ)
                break;

            CopyMemory(PartialInfoAlign64->Data, Buffer, BufferLength);
            PartialInfoAlign64->DataLength = BufferLength - sizeof(WCHAR);
            break;
    }

    return Status;
}

NTSTATUS
HPCALL
LeNtQueryDefaultLocale(
    HPARGS
    BOOLEAN UserProfile,
    PLCID   DefaultLocaleId
)
{
    HpSetFilterAction(BlockSystemCall);

    SEH_TRY
    {
        *DefaultLocaleId = ((PLeGlobalData)HpGetFilterContext())->GetLeb()->LocaleID;
        return STATUS_SUCCESS;
    }
    SEH_EXCEPT(EXCEPTION_EXECUTE_HANDLER)
    {
        return GetExceptionCode();
    }
}

NTSTATUS
HPCALL
LeNtQueryDefaultUILanguage(
    HPARGS
    LANGID *DefaultUILanguageId
)
{
    HpSetFilterAction(BlockSystemCall);

    SEH_TRY
    {
        *DefaultUILanguageId = ((PLeGlobalData)HpGetFilterContext())->GetLeb()->LocaleID;
        return STATUS_SUCCESS;
    }
    SEH_EXCEPT(EXCEPTION_EXECUTE_HANDLER)
    {
        return GetExceptionCode();
    }
}

NTSTATUS
HPCALL
LeNtQueryInstallUILanguage(
    HPARGS
    LANGID *InstallUILanguageId
)
{
    HpSetFilterAction(BlockSystemCall);

    SEH_TRY
    {
        *InstallUILanguageId = ((PLeGlobalData)HpGetFilterContext())->GetLeb()->LocaleID;
        return STATUS_SUCCESS;
    }
    SEH_EXCEPT(EXCEPTION_EXECUTE_HANDLER)
    {
        return GetExceptionCode();
    }
}

NTSTATUS NTAPI LeLdrInitNtContinue(PCONTEXT Context, BOOLEAN TestAlert)
{
    PLeGlobalData GlobalData = LeGetGlobalData();

    CurrentTeb()->CurrentLocale = GlobalData->GetLeb()->LocaleID;

    return GlobalData->HookStub.StubLdrInitNtContinue(Context, TestAlert);
}

NTSTATUS
NTAPI
LeLdrResSearchResource(
    PVOID       DllHandle,
    PULONG_PTR  ResourceIdPath,
    ULONG       ResourceIdPathLength,
    ULONG       Flags,
    PVOID*      Resource,
    PULONG      Size,
    PVOID       Reserve1,
    PVOID       Reserve2
)
{
    NTSTATUS Status;
    PLeGlobalData GlobalData = LeGetGlobalData();

    Status = GlobalData->HookStub.StubLdrResSearchResource(DllHandle, ResourceIdPath, ResourceIdPathLength, Flags, Resource, Size, Reserve1, Reserve2);
    FAIL_RETURN(Status);

    if (ResourceIdPathLength != 3)
        return Status;

    if (ResourceIdPath[0] != (ULONG_PTR)RT_VERSION || ResourceIdPath[1] != 1 || ResourceIdPath[2] != 0)
        return Status;

    if (Resource == nullptr)
        return Status;

    ReplaceMUIVersionLocaleInfo(*Resource, *Size);

    return Status;
}

NTSTATUS LeGlobalData::HookNtdllRoutines(PVOID Ntdll)
{
    NTSTATUS            Status;
    HANDLE              RootKey;
    OBJECT_ATTRIBUTES   ObjectAttributes;
    UNICODE_STRING      SubKey;
    PVOID               LdrInitNtContinue;

    LdrInitNtContinue = SearchLdrInitNtContinue();
    if (LdrInitNtContinue == nullptr)
        return STATUS_NOT_SUPPORTED;

    RootKey = nullptr;

    LOOP_ONCE
    {
        HANDLE CodePageKey, LanguageKey;

        Status = OpenPredefinedKeyHandle(&RootKey, REGKEY_ROOT, KEY_QUERY_VALUE);
        FAIL_BREAK(Status);

        RTL_CONST_STRING(SubKey, REGPATH_CODEPAGE);
        InitializeObjectAttributes(&ObjectAttributes, &SubKey, OBJ_CASE_INSENSITIVE, RootKey, nullptr);
        Status = NtOpenKey(&CodePageKey, KEY_QUERY_VALUE, &ObjectAttributes);
        FAIL_BREAK(Status);

        Status = QueryRegKeyFullPath(CodePageKey, &HookRoutineData.Ntdll.CodePageKey);
        NtClose(CodePageKey);
        FAIL_BREAK(Status);

        RTL_CONST_STRING(SubKey, REGPATH_LANGUAGE);
        Status = NtOpenKey(&LanguageKey, KEY_QUERY_VALUE, &ObjectAttributes);
        FAIL_BREAK(Status);

        Status = QueryRegKeyFullPath(LanguageKey, &HookRoutineData.Ntdll.LanguageKey);
        NtClose(LanguageKey);
        FAIL_BREAK(Status);

        ADD_FILTER_(NtQueryValueKey, LeNtQueryValueKey, this);
    }

    if (RootKey != nullptr)
        NtClose(RootKey);

    ADD_FILTER_(NtQuerySystemInformation,   LeNtQuerySystemInformation, this);
    //ADD_FILTER_(NtQueryInformationThread,   LeNtQueryInformationThread, this);
    ADD_FILTER_(NtCreateUserProcess,        LeNtCreateUserProcess,      this);
    ADD_FILTER_(NtInitializeNlsFiles,       LeNtInitializeNlsFiles,     this);
    ADD_FILTER_(NtQueryDefaultLocale,       LeNtQueryDefaultLocale,     this);
    ADD_FILTER_(NtQueryDefaultUILanguage,   LeNtQueryDefaultUILanguage, this);
    ADD_FILTER_(NtQueryInstallUILanguage,   LeNtQueryInstallUILanguage, this);
    //ADD_FILTER_(NtTerminateThread,          LeNtTerminateThread,        this);

    Mp::PATCH_MEMORY_DATA p[] =
    {
        Mp::FunctionCallVa(LdrInitNtContinue, LeLdrInitNtContinue, &HookStub.StubLdrInitNtContinue),
    };

    Mp::PatchMemory(p, countof(p));


    return STATUS_SUCCESS;
}

NTSTATUS LeGlobalData::UnHookNtdllRoutines()
{
    Mp::RestoreMemory(HookStub.StubLdrInitNtContinue);

    return 0;
}
