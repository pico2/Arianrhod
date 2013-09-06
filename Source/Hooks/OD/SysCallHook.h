#ifndef _SYSCALLHOOK_H_4422eab3_99d6_4a37_9f4f_ea45031f9439
#define _SYSCALLHOOK_H_4422eab3_99d6_4a37_9f4f_ea45031f9439

#include "pragma_once.h"
#include <Windows.h>
#include "my_headers.h"

#pragma comment(lib, "undoc_ntdll.lib")

#define MAX_SERVICE_INDEX   0x300
#define SYSCALL_FILTER_FLAG_ENABLE  0x00000001
#define KI_FAST_SYSTEM_CALL_MASK    TAG4('NANA')

#define DISABLE_HOOK(_info) CLEAR_FLAG(_info->Flags, SYSCALL_FILTER_FLAG_ENABLE)
#define ENABLE_HOOK(_info) SET_FLAG(_info->Flags, SYSCALL_FILTER_FLAG_ENABLE)

#define ADD_FUNCTION(routine) AddFunctionToTable(&g_HashTable, SYSCALL_##routine, Hook##routine)
#define DEL_FUNCTION(routine) RemoveFunctionFromTable(&g_HashTable, SYSCALL_##routine)

enum
{
    PASS_THROUGH        = 0,
    BYPASS_SYSCALL      = 1,
    CALL_AFTER_RETURN   = 2,
};

_MY_C_HEAD_

#pragma pack(1)

typedef struct SYSCALL_FILTER_ENTRY
{
    PVOID               ProxyFunction;
    ULONG               Flags;
    ULONG               ArgumentSize;
    PVOID               FunctionName;
    ULONG               ServiceIndex;
    PCRITICAL_SECTION   FilterLock;
    PVOID               ReturnOpAddress;
    PVOID               Reserve4;
} SYSCALL_FILTER_ENTRY;

typedef struct
{
    ULONG Hash;
    SYSCALL_FILTER_ENTRY *Entry;
} HASH_TABLE_ENTRY;

typedef struct
{
    ULONG Count;
    HASH_TABLE_ENTRY *Entry;
} SYSCALL_FILTER_HASH_TABLE;

#pragma pack()

extern SYSCALL_FILTER_ENTRY        *g_pSysCallFilters;
extern SYSCALL_FILTER_HASH_TABLE    g_HashTable;
extern ULONG                        g_ExplorerPID;

NTSTATUS InstallSyscallHook();
NTSTATUS UnInstallSyscallHook();
NTSTATUS RemoveFunctionFromTable(SYSCALL_FILTER_HASH_TABLE *HashTable, ULONG Hash);
NTSTATUS AddFunctionToTable(SYSCALL_FILTER_HASH_TABLE *HashTable, ULONG Hash, PVOID Routine);

NTSTATUS
CDECL
CallSystemCall(
    SYSCALL_FILTER_ENTRY   *FilterInfo,
    PBOOL                   BypassType,
    ...
);

_MY_C_TAIL_





#define SYSCALL_ZwAcceptConnectPort                                         0x3E0DE6AD
#define SYSCALL_ZwAccessCheck                                               0x147B768E
#define SYSCALL_ZwAccessCheckAndAuditAlarm                                  0x4EFE5E3B
#define SYSCALL_ZwAccessCheckByType                                         0x3E3DAFFE
#define SYSCALL_ZwAccessCheckByTypeAndAuditAlarm                            0xC34CBE6F
#define SYSCALL_ZwAccessCheckByTypeResultList                               0xC9E5DC56
#define SYSCALL_ZwAccessCheckByTypeResultListAndAuditAlarm                  0x73ABEF80
#define SYSCALL_ZwAccessCheckByTypeResultListAndAuditAlarmByHandle          0x2DEC7785
#define SYSCALL_ZwAddAtom                                                   0x6E5DDA27
#define SYSCALL_ZwAddBootEntry                                              0xD0E5C004
#define SYSCALL_ZwAddDriverEntry                                            0x37F5DF59
#define SYSCALL_ZwAdjustGroupsToken                                         0xC5EA783F
#define SYSCALL_ZwAdjustPrivilegesToken                                     0x0A72F800
#define SYSCALL_ZwAlertResumeThread                                         0x4DDCA233
#define SYSCALL_ZwAlertThread                                               0xAF2AFDCF
#define SYSCALL_ZwAllocateLocallyUniqueId                                   0x189C8D77
#define SYSCALL_ZwAllocateReserveObject                                     0x452B9B22
#define SYSCALL_ZwAllocateUserPhysicalPages                                 0x4661E797
#define SYSCALL_ZwAllocateUuids                                             0xA217368F
#define SYSCALL_ZwAllocateVirtualMemory                                     0x977DFFAF
#define SYSCALL_ZwAlpcAcceptConnectPort                                     0x08E34AA9
#define SYSCALL_ZwAlpcCancelMessage                                         0x233FD0FF
#define SYSCALL_ZwAlpcConnectPort                                           0xD69C1C03
#define SYSCALL_ZwAlpcCreatePort                                            0x47DEDBC4
#define SYSCALL_ZwAlpcCreatePortSection                                     0x8017EC7B
#define SYSCALL_ZwAlpcCreateResourceReserve                                 0x9405A716
#define SYSCALL_ZwAlpcCreateSectionView                                     0x81882C7A
#define SYSCALL_ZwAlpcCreateSecurityContext                                 0x2AFD388E
#define SYSCALL_ZwAlpcDeletePortSection                                     0x8250E4C3
#define SYSCALL_ZwAlpcDeleteResourceReserve                                 0x1F858366
#define SYSCALL_ZwAlpcDeleteSectionView                                     0x83CF24C2
#define SYSCALL_ZwAlpcDeleteSecurityContext                                 0xA17D1CFE
#define SYSCALL_ZwAlpcDisconnectPort                                        0x432390B2
#define SYSCALL_ZwAlpcImpersonateClientOfPort                               0x6C041D89
#define SYSCALL_ZwAlpcOpenSenderProcess                                     0xF1B8AE22
#define SYSCALL_ZwAlpcOpenSenderThread                                      0x6B2F035A
#define SYSCALL_ZwAlpcQueryInformation                                      0xCAEBC263
#define SYSCALL_ZwAlpcQueryInformationMessage                               0x9D78C73D
#define SYSCALL_ZwAlpcRevokeSecurityContext                                 0xE162759F
#define SYSCALL_ZwAlpcSendWaitReceivePort                                   0x902A78E8
#define SYSCALL_ZwAlpcSetInformation                                        0x9256441C
#define SYSCALL_ZwApphelpCacheControl                                       0xC80D29DD
#define SYSCALL_ZwAreMappedFilesTheSame                                     0x5265B41A
#define SYSCALL_ZwAssignProcessToJobObject                                  0x4B3A6A01
#define SYSCALL_ZwCallbackReturn                                            0xCBF25EAE
#define SYSCALL_ZwCancelIoFile                                              0xF707F576
#define SYSCALL_ZwCancelIoFileEx                                            0xDBD4BFAD
#define SYSCALL_ZwCancelSynchronousIoFile                                   0xB78BE27A
#define SYSCALL_ZwCancelTimer                                               0x054E3B21
#define SYSCALL_ZwClearEvent                                                0xB008D64E
#define SYSCALL_ZwClose                                                     0xB828D68A
#define SYSCALL_ZwCloseObjectAuditAlarm                                     0x361FAC01
#define SYSCALL_ZwCommitComplete                                            0x6BC307DE
#define SYSCALL_ZwCommitEnlistment                                          0x707481D5
#define SYSCALL_ZwCommitTransaction                                         0xB759CB8E
#define SYSCALL_ZwCompactKeys                                               0xBE8CA93E
#define SYSCALL_ZwCompareTokens                                             0x2A53BBE9
#define SYSCALL_ZwCompleteConnectPort                                       0x46690796
#define SYSCALL_ZwCompressKey                                               0x06FBF538
#define SYSCALL_ZwConnectPort                                               0x668CC7B9
#define SYSCALL_ZwContinue                                                  0xAC15233A
#define SYSCALL_ZwCreateDebugObject                                         0x8FA5DF61
#define SYSCALL_ZwCreateDirectoryObject                                     0xA41BBA61
#define SYSCALL_ZwCreateEnlistment                                          0xB73A1191
#define SYSCALL_ZwCreateEvent                                               0x363B1FB5
#define SYSCALL_ZwCreateEventPair                                           0x7F5E6BC2
#define SYSCALL_ZwCreateFile                                                0x82089053
#define SYSCALL_ZwCreateIoCompletion                                        0xC736032E
#define SYSCALL_ZwCreateJobObject                                           0xA63EF986
#define SYSCALL_ZwCreateJobSet                                              0x9664852D
#define SYSCALL_ZwCreateKey                                                 0xB5B59051
#define SYSCALL_ZwCreateKeyTransacted                                       0x02512246
#define SYSCALL_ZwCreateKeyedEvent                                          0x1DE9173F
#define SYSCALL_ZwCreateMailslotFile                                        0x3363791B
#define SYSCALL_ZwCreateMutant                                              0x5FC5EE23
#define SYSCALL_ZwCreateNamedPipeFile                                       0xA833C690
#define SYSCALL_ZwCreatePagingFile                                          0xDCAA4B3A
#define SYSCALL_ZwCreatePort                                                0x9A0B5B42
#define SYSCALL_ZwCreatePrivateNamespace                                    0x895754C9
#define SYSCALL_ZwCreateProcess                                             0x9073CA85
#define SYSCALL_ZwCreateProcessEx                                           0x16496F52
#define SYSCALL_ZwCreateProfile                                             0xA0702813
#define SYSCALL_ZwCreateProfileEx                                           0x4E8960D8
#define SYSCALL_ZwCreateResourceManager                                     0x01936BE3
#define SYSCALL_ZwCreateSection                                             0xA0B08136
#define SYSCALL_ZwCreateSemaphore                                           0xDF1F01CB
#define SYSCALL_ZwCreateSymbolicLinkObject                                  0x9EB2214C
#define SYSCALL_ZwCreateThread                                              0x4E140D01
#define SYSCALL_ZwCreateThreadEx                                            0x0530F04C
#define SYSCALL_ZwCreateTimer                                               0x172A7033
#define SYSCALL_ZwCreateToken                                               0x0F2A732F
#define SYSCALL_ZwCreateTransaction                                         0x65515367
#define SYSCALL_ZwCreateTransactionManager                                  0xA1D55AAA
#define SYSCALL_ZwCreateUserProcess                                         0xB5BA1CD8
#define SYSCALL_ZwCreateWaitablePort                                        0xBA7E2A0C
#define SYSCALL_ZwCreateWorkerFactory                                       0x319CDED2
#define SYSCALL_ZwDebugActiveProcess                                        0x17DFB7D9
#define SYSCALL_ZwDebugContinue                                             0xFF475CB6
#define SYSCALL_ZwDelayExecution                                            0x219254F8
#define SYSCALL_ZwDeleteAtom                                                0xBEE9E4DB
#define SYSCALL_ZwDeleteBootEntry                                           0x718DBDFD
#define SYSCALL_ZwDeleteDriverEntry                                         0xD1707EAE
#define SYSCALL_ZwDeleteFile                                                0xCAE98753
#define SYSCALL_ZwDeleteKey                                                 0x0DB7D759
#define SYSCALL_ZwDeleteObjectAuditAlarm                                    0x967B566A
#define SYSCALL_ZwDeletePrivateNamespace                                    0x8DD945B9
#define SYSCALL_ZwDeleteValueKey                                            0xD8323C60
#define SYSCALL_ZwDeviceIoControlFile                                       0x1C311055
#define SYSCALL_ZwDisableLastKnownGood                                      0x5D92A3AE
#define SYSCALL_ZwDisplayString                                             0xF3E7BA0B
#define SYSCALL_ZwDrawText                                                  0xB823DDB5
#define SYSCALL_ZwDuplicateObject                                           0x2F399CF3
#define SYSCALL_ZwDuplicateToken                                            0xE1897F41
#define SYSCALL_ZwEnableLastKnownGood                                       0xE4A6117D
#define SYSCALL_ZwEnumerateBootEntries                                      0xD05749F4
#define SYSCALL_ZwEnumerateDriverEntries                                    0x3ADF16F4
#define SYSCALL_ZwEnumerateKey                                              0x7DD24A86
#define SYSCALL_ZwEnumerateSystemEnvironmentValuesEx                        0x7B5D9A07
#define SYSCALL_ZwEnumerateTransactionObject                                0x73079549
#define SYSCALL_ZwEnumerateValueKey                                         0x38F907DE
#define SYSCALL_ZwExtendSection                                             0xC8359B72
#define SYSCALL_ZwFilterToken                                               0xA44E3A15
#define SYSCALL_ZwFindAtom                                                  0xED17F732
#define SYSCALL_ZwFlushBuffersFile                                          0xF6C76CB7
#define SYSCALL_ZwFlushInstallUILanguage                                    0x1E74232C
#define SYSCALL_ZwFlushInstructionCache                                     0x4178B1D8
#define SYSCALL_ZwFlushKey                                                  0x1067E390
#define SYSCALL_ZwFlushProcessWriteBuffers                                  0x9DB39F29
#define SYSCALL_ZwFlushVirtualMemory                                        0x2D5C8D0C
#define SYSCALL_ZwFlushWriteBuffer                                          0x5A465394
#define SYSCALL_ZwFreeUserPhysicalPages                                     0x8FBACF2A
#define SYSCALL_ZwFreeVirtualMemory                                         0x25F62332
#define SYSCALL_ZwFreezeRegistry                                            0x74355377
#define SYSCALL_ZwFreezeTransactions                                        0x8B6CF0D9
#define SYSCALL_ZwFsControlFile                                             0x798822B1
#define SYSCALL_ZwGetContextThread                                          0x35111741
#define SYSCALL_ZwGetCurrentProcessorNumber                                 0xC293EAFF
#define SYSCALL_ZwGetDevicePowerState                                       0x21A3E39D
#define SYSCALL_ZwGetMUIRegistryInfo                                        0x656CF931
#define SYSCALL_ZwGetNextProcess                                            0x73B0A4FB
#define SYSCALL_ZwGetNextThread                                             0x3DE3131A
#define SYSCALL_ZwGetNlsSectionPtr                                          0xED823959
#define SYSCALL_ZwGetNotificationResourceManager                            0xF1D925AF
#define SYSCALL_ZwGetPlugPlayEvent                                          0xA5A40066
#define SYSCALL_ZwGetWriteWatch                                             0xF1334DF4
#define SYSCALL_ZwImpersonateAnonymousToken                                 0x964767C5
#define SYSCALL_ZwImpersonateClientOfPort                                   0xC7051032
#define SYSCALL_ZwImpersonateThread                                         0xE3241813
#define SYSCALL_ZwInitializeNlsFiles                                        0xCB6EFDF5
#define SYSCALL_ZwInitializeRegistry                                        0x499E50D7
#define SYSCALL_ZwInitiatePowerAction                                       0x265B4CA4
#define SYSCALL_ZwIsProcessInJob                                            0x2489E599
#define SYSCALL_ZwIsSystemResumeAutomatic                                   0xF0DB68C8
#define SYSCALL_ZwIsUILanguageComitted                                      0x2E61AB25
#define SYSCALL_ZwListenPort                                                0x2B5E0060
#define SYSCALL_ZwLoadDriver                                                0xDE98FAA4
#define SYSCALL_ZwLoadKey                                                   0x920FC8A5
#define SYSCALL_ZwLoadKey2                                                  0xF914B273
#define SYSCALL_ZwLoadKeyEx                                                 0x96409F5A
#define SYSCALL_ZwLockFile                                                  0xC9E614A0
#define SYSCALL_ZwLockProductActivationKeys                                 0x25C66B61
#define SYSCALL_ZwLockRegistryKey                                           0x4CFF67E5
#define SYSCALL_ZwLockVirtualMemory                                         0x247C3FDA
#define SYSCALL_ZwMakePermanentObject                                       0xC02D49EF
#define SYSCALL_ZwMakeTemporaryObject                                       0xD2A08DD6
#define SYSCALL_ZwMapCMFModule                                              0xC4CA447F
#define SYSCALL_ZwMapUserPhysicalPages                                      0xB060DC2E
#define SYSCALL_ZwMapUserPhysicalPagesScatter                               0xA38B5C54
#define SYSCALL_ZwMapViewOfSection                                          0xA4CA3654
#define SYSCALL_ZwModifyBootEntry                                           0xF04BA9B5
#define SYSCALL_ZwModifyDriverEntry                                         0xF37766FF
#define SYSCALL_ZwNotifyChangeDirectoryFile                                 0x258B34AF
#define SYSCALL_ZwNotifyChangeKey                                           0x36AACD00
#define SYSCALL_ZwNotifyChangeMultipleKeys                                  0x78E6A430
#define SYSCALL_ZwNotifyChangeSession                                       0x74A8B343
#define SYSCALL_ZwOpenDirectoryObject                                       0x066413BD
#define SYSCALL_ZwOpenEnlistment                                            0xE605C57F
#define SYSCALL_ZwOpenEvent                                                 0x1EA4F5C2
#define SYSCALL_ZwOpenEventPair                                             0xD82CE23C
#define SYSCALL_ZwOpenFile                                                  0xD1B1D4AC
#define SYSCALL_ZwOpenIoCompletion                                          0x7E72FC7D
#define SYSCALL_ZwOpenJobObject                                             0x014C7078
#define SYSCALL_ZwOpenKey                                                   0x924F0D9B
#define SYSCALL_ZwOpenKeyEx                                                 0x6E419C4E
#define SYSCALL_ZwOpenKeyTransacted                                         0x9DBB556E
#define SYSCALL_ZwOpenKeyTransactedEx                                       0xBA7E4D2D
#define SYSCALL_ZwOpenKeyedEvent                                            0x4CD6C3D1
#define SYSCALL_ZwOpenMutant                                                0xA28B0B30
#define SYSCALL_ZwOpenObjectAuditAlarm                                      0x67CED355
#define SYSCALL_ZwOpenPrivateNamespace                                      0x7C6CC086
#define SYSCALL_ZwOpenProcess                                               0x4CD1B52C
#define SYSCALL_ZwOpenProcessToken                                          0x30EFFDB7
#define SYSCALL_ZwOpenProcessTokenEx                                        0xDCCB1F8E
#define SYSCALL_ZwOpenResourceManager                                       0xA3ECC23F
#define SYSCALL_ZwOpenSection                                               0x7C12FE9F
#define SYSCALL_ZwOpenSemaphore                                             0x786D8835
#define SYSCALL_ZwOpenSession                                               0x7D12FD1F
#define SYSCALL_ZwOpenSymbolicLinkObject                                    0xA166CF1D
#define SYSCALL_ZwOpenThread                                                0xB35AE812
#define SYSCALL_ZwOpenThreadToken                                           0xCFF947CA
#define SYSCALL_ZwOpenThreadTokenEx                                         0x2B374567
#define SYSCALL_ZwOpenTimer                                                 0x3FB59A44
#define SYSCALL_ZwOpenTransaction                                           0x9FCC9940
#define SYSCALL_ZwOpenTransactionManager                                    0x9E01B4FB
#define SYSCALL_ZwPlugPlayControl                                           0x4F14214F
#define SYSCALL_ZwPowerInformation                                          0xDC4FD11F
#define SYSCALL_ZwPrePrepareComplete                                        0xEC1E291C
#define SYSCALL_ZwPrePrepareEnlistment                                      0x7A6BF56E
#define SYSCALL_ZwPrepareComplete                                           0xC137F586
#define SYSCALL_ZwPrepareEnlistment                                         0x12DF521C
#define SYSCALL_ZwPrivilegeCheck                                            0x88F1DBAC
#define SYSCALL_ZwPrivilegeObjectAuditAlarm                                 0x2776184F
#define SYSCALL_ZwPrivilegedServiceAuditAlarm                               0x3FD9A100
#define SYSCALL_ZwPropagationComplete                                       0xF5619130
#define SYSCALL_ZwPropagationFailed                                         0x2B257776
#define SYSCALL_ZwProtectVirtualMemory                                      0x0CF0A6F9
#define SYSCALL_ZwPulseEvent                                                0xFA6C4F60
#define SYSCALL_ZwQueryAttributesFile                                       0xC39E005C
#define SYSCALL_ZwQueryBootEntryOrder                                       0x49D3306A
#define SYSCALL_ZwQueryBootOptions                                          0x6BB5129D
#define SYSCALL_ZwQueryDebugFilterState                                     0x9F6240B4
#define SYSCALL_ZwQueryDefaultLocale                                        0xBF0668C1
#define SYSCALL_ZwQueryDefaultUILanguage                                    0x73170C87
#define SYSCALL_ZwQueryDirectoryFile                                        0x5EE6AC6D
#define SYSCALL_ZwQueryDirectoryObject                                      0xB5C7F9D7
#define SYSCALL_ZwQueryDriverEntryOrder                                     0xBAE4B765
#define SYSCALL_ZwQueryEaFile                                               0x9C9807AC
#define SYSCALL_ZwQueryEvent                                                0xB24C0F58
#define SYSCALL_ZwQueryFullAttributesFile                                   0xBEA71B4E
#define SYSCALL_ZwQueryInformationAtom                                      0x81676C4B
#define SYSCALL_ZwQueryInformationEnlistment                                0x50DE0C4A
#define SYSCALL_ZwQueryInformationFile                                      0xF5670FC3
#define SYSCALL_ZwQueryInformationJobObject                                 0x48E1C6A6
#define SYSCALL_ZwQueryInformationPort                                      0xED64C4D2
#define SYSCALL_ZwQueryInformationProcess                                   0x27BC02BE
#define SYSCALL_ZwQueryInformationResourceManager                           0xCE5B5054
#define SYSCALL_ZwQueryInformationThread                                    0x0FC9B37F
#define SYSCALL_ZwQueryInformationToken                                     0xFCD87DC2
#define SYSCALL_ZwQueryInformationTransaction                               0xE6EA2F9B
#define SYSCALL_ZwQueryInformationTransactionManager                        0x45C8814D
#define SYSCALL_ZwQueryInformationWorkerFactory                             0xC3923321
#define SYSCALL_ZwQueryInstallUILanguage                                    0x365A26BE
#define SYSCALL_ZwQueryIntervalProfile                                      0x161C5FF8
#define SYSCALL_ZwQueryIoCompletion                                         0xAB15BBA9
#define SYSCALL_ZwQueryKey                                                  0xA871AB30
#define SYSCALL_ZwQueryLicenseValue                                         0xA024BB28
#define SYSCALL_ZwQueryMultipleValueKey                                     0x31A67D85
#define SYSCALL_ZwQueryMutant                                               0xBDD85EAD
#define SYSCALL_ZwQueryObject                                               0xACA9F1A9
#define SYSCALL_ZwQueryOpenSubKeys                                          0x9130E9A3
#define SYSCALL_ZwQueryOpenSubKeysEx                                        0x8E4C63DE
#define SYSCALL_ZwQueryPerformanceCounter                                   0xE8B732F3
#define SYSCALL_ZwQueryPortInformationProcess                               0x99B7B08F
#define SYSCALL_ZwQueryQuotaInformationFile                                 0xA55AA91B
#define SYSCALL_ZwQuerySection                                              0x16A15D75
#define SYSCALL_ZwQuerySecurityAttributesToken                              0xC88332C0
#define SYSCALL_ZwQuerySecurityObject                                       0xE9E71904
#define SYSCALL_ZwQuerySemaphore                                            0xD1C746BA
#define SYSCALL_ZwQuerySymbolicLinkObject                                   0x7093FA44
#define SYSCALL_ZwQuerySystemEnvironmentValue                               0x26047B84
#define SYSCALL_ZwQuerySystemEnvironmentValueEx                             0x1090B196
#define SYSCALL_ZwQuerySystemInformation                                    0x4945491E
#define SYSCALL_ZwQuerySystemInformationEx                                  0x792DB55C
#define SYSCALL_ZwQuerySystemTime                                           0x74831BF7
#define SYSCALL_ZwQueryTimer                                                0x935D60DE
#define SYSCALL_ZwQueryTimerResolution                                      0x7C73FCCE
#define SYSCALL_ZwQueryValueKey                                             0x93BEC4B3
#define SYSCALL_ZwQueryVirtualMemory                                        0xCD05AF8E
#define SYSCALL_ZwQueryVolumeInformationFile                                0x1EE14B20
#define SYSCALL_ZwQueueApcThread                                            0x53C6B9CD
#define SYSCALL_ZwQueueApcThreadEx                                          0x3547BA9F
#define SYSCALL_ZwRaiseException                                            0x624178BC
#define SYSCALL_ZwRaiseHardError                                            0xC51536A2
#define SYSCALL_ZwReadFile                                                  0x391494A4
#define SYSCALL_ZwReadFileScatter                                           0xF7C0FE10
#define SYSCALL_ZwReadOnlyEnlistment                                        0x6FA598F0
#define SYSCALL_ZwReadRequestData                                           0x231F5B73
#define SYSCALL_ZwReadVirtualMemory                                         0x24E2218A
#define SYSCALL_ZwRecoverEnlistment                                         0x6356ECF9
#define SYSCALL_ZwRecoverResourceManager                                    0xA94A9132
#define SYSCALL_ZwRecoverTransactionManager                                 0xCD28327E
#define SYSCALL_ZwRegisterProtocolAddressInformation                        0x26BD8786
#define SYSCALL_ZwRegisterThreadTerminatePort                               0x8041B9A1
#define SYSCALL_ZwReleaseKeyedEvent                                         0xBA4EFE0A
#define SYSCALL_ZwReleaseMutant                                             0x2156B459
#define SYSCALL_ZwReleaseSemaphore                                          0x96B23CF4
#define SYSCALL_ZwReleaseWorkerFactoryWorker                                0xBBFCE147
#define SYSCALL_ZwRemoveIoCompletion                                        0xE4A1076C
#define SYSCALL_ZwRemoveIoCompletionEx                                      0xB39A2465
#define SYSCALL_ZwRemoveProcessDebug                                        0x8F3E03AF
#define SYSCALL_ZwRenameKey                                                 0x0C274151
#define SYSCALL_ZwRenameTransactionManager                                  0x6D43D2AF
#define SYSCALL_ZwReplaceKey                                                0xA04AF6E5
#define SYSCALL_ZwReplacePartitionUnit                                      0x215EF893
#define SYSCALL_ZwReplyPort                                                 0x9D623BC6
#define SYSCALL_ZwReplyWaitReceivePort                                      0x32C71862
#define SYSCALL_ZwReplyWaitReceivePortEx                                    0x88C3BC19
#define SYSCALL_ZwReplyWaitReplyPort                                        0x9B569685
#define SYSCALL_ZwRequestPort                                               0xBFCCD8DD
#define SYSCALL_ZwRequestWaitReplyPort                                      0xF832C359
#define SYSCALL_ZwResetEvent                                                0x0229DF42
#define SYSCALL_ZwResetWriteWatch                                           0xB3696A4F
#define SYSCALL_ZwRestoreKey                                                0xB95CF6F9
#define SYSCALL_ZwResumeProcess                                             0x82F853DC
#define SYSCALL_ZwResumeThread                                              0x84DC995D
#define SYSCALL_ZwRollbackComplete                                          0x1CF3C6A5
#define SYSCALL_ZwRollbackEnlistment                                        0x9DA842D0
#define SYSCALL_ZwRollbackTransaction                                       0x2F397635
#define SYSCALL_ZwRollforwardTransactionManager                             0xDC450EDD
#define SYSCALL_ZwSaveKey                                                   0x93780839
#define SYSCALL_ZwSaveKeyEx                                                 0xE6454058
#define SYSCALL_ZwSaveMergedKeys                                            0x060D0579
#define SYSCALL_ZwSecureConnectPort                                         0x1E17469D
#define SYSCALL_ZwSerializeBoot                                             0xF1D58F4F
#define SYSCALL_ZwSetBootEntryOrder                                         0x31251972
#define SYSCALL_ZwSetBootOptions                                            0x5B44FECF
#define SYSCALL_ZwSetContextThread                                          0x351117E1
#define SYSCALL_ZwSetDebugFilterState                                       0xFE819810
#define SYSCALL_ZwSetDefaultHardErrorPort                                   0xC42BEC94
#define SYSCALL_ZwSetDefaultLocale                                          0xF7C5AF70
#define SYSCALL_ZwSetDefaultUILanguage                                      0x080380BB
#define SYSCALL_ZwSetDriverEntryOrder                                       0xDB076FC1
#define SYSCALL_ZwSetEaFile                                                 0x84E0F185
#define SYSCALL_ZwSetEvent                                                  0x0304CC9F
#define SYSCALL_ZwSetEventBoostPriority                                     0x052CF216
#define SYSCALL_ZwSetHighEventPair                                          0xE75766A7
#define SYSCALL_ZwSetHighWaitLowEventPair                                   0x3B72C7F7
#define SYSCALL_ZwSetInformationDebugObject                                 0xFA37BBE5
#define SYSCALL_ZwSetInformationEnlistment                                  0x9319BD02
#define SYSCALL_ZwSetInformationFile                                        0x304400DD
#define SYSCALL_ZwSetInformationJobObject                                   0xC2A7D89B
#define SYSCALL_ZwSetInformationKey                                         0x31C00235
#define SYSCALL_ZwSetInformationObject                                      0x747D7365
#define SYSCALL_ZwSetInformationProcess                                     0xB63B8DDC
#define SYSCALL_ZwSetInformationResourceManager                             0x49D432C5
#define SYSCALL_ZwSetInformationThread                                      0x74DD3F43
#define SYSCALL_ZwSetInformationToken                                       0x9D3BA566
#define SYSCALL_ZwSetInformationTransaction                                 0x10C337E3
#define SYSCALL_ZwSetInformationTransactionManager                          0x8279C98E
#define SYSCALL_ZwSetInformationWorkerFactory                               0x204A9740
#define SYSCALL_ZwSetIntervalProfile                                        0xD33F50E6
#define SYSCALL_ZwSetIoCompletion                                           0x969FFDB7
#define SYSCALL_ZwSetIoCompletionEx                                         0xDE52DF8E
#define SYSCALL_ZwSetLdtEntries                                             0x2C6FD278
#define SYSCALL_ZwSetLowEventPair                                           0x6908C5AF
#define SYSCALL_ZwSetLowWaitHighEventPair                                   0xF8BF6466
#define SYSCALL_ZwSetQuotaInformationFile                                   0x2F1CB726
#define SYSCALL_ZwSetSecurityObject                                         0x9111301C
#define SYSCALL_ZwSetSystemEnvironmentValue                                 0xD02D63FC
#define SYSCALL_ZwSetSystemEnvironmentValueEx                               0xF34815F7
#define SYSCALL_ZwSetSystemInformation                                      0x3251C522
#define SYSCALL_ZwSetSystemPowerState                                       0xF6A0B904
#define SYSCALL_ZwSetSystemTime                                             0x16129C78
#define SYSCALL_ZwSetThreadExecutionState                                   0xAE1A1962
#define SYSCALL_ZwSetTimer                                                  0x2215A319
#define SYSCALL_ZwSetTimerEx                                                0x6480F6F4
#define SYSCALL_ZwSetTimerResolution                                        0xB950F3D0
#define SYSCALL_ZwSetUuidSeed                                               0x96CA3C7C
#define SYSCALL_ZwSetValueKey                                               0x37DF276B
#define SYSCALL_ZwSetVolumeInformationFile                                  0xDD26FA68
#define SYSCALL_ZwShutdownSystem                                            0xFEFD534F
#define SYSCALL_ZwShutdownWorkerFactory                                     0x7E331024
#define SYSCALL_ZwSignalAndWaitForSingleObject                              0x871600D5
#define SYSCALL_ZwSinglePhaseReject                                         0x3CA550D2
#define SYSCALL_ZwStartProfile                                              0x7EE0F454
#define SYSCALL_ZwStopProfile                                               0x8C525DCA
#define SYSCALL_ZwSuspendProcess                                            0xF3B31A02
#define SYSCALL_ZwSuspendThread                                             0xCA2F1307
#define SYSCALL_ZwSystemDebugControl                                        0x7AE77BB0
#define SYSCALL_ZwTerminateJobObject                                        0xB08013A4
#define SYSCALL_ZwTerminateProcess                                          0x3FC94200
#define SYSCALL_ZwTerminateThread                                           0x0A3970D5
#define SYSCALL_ZwTestAlert                                                 0xB6E2E3F6
#define SYSCALL_ZwThawRegistry                                              0x3A8DFB93
#define SYSCALL_ZwThawTransactions                                          0x05281B53
#define SYSCALL_ZwTraceControl                                              0x9AF7CC7F
#define SYSCALL_ZwTraceEvent                                                0x92E84860
#define SYSCALL_ZwTranslateFilePath                                         0x74E73BAE
#define SYSCALL_ZwUmsThreadYield                                            0x797CAFA8
#define SYSCALL_ZwUnloadDriver                                              0xAA9FCEC7
#define SYSCALL_ZwUnloadKey                                                 0x54E7C6CD
#define SYSCALL_ZwUnloadKey2                                                0xF8D9AAAE
#define SYSCALL_ZwUnloadKeyEx                                               0x355B3F63
#define SYSCALL_ZwUnlockFile                                                0xC82B0C7D
#define SYSCALL_ZwUnlockVirtualMemory                                       0x3FDC0679
#define SYSCALL_ZwUnmapViewOfSection                                        0x69D2EB55
#define SYSCALL_ZwVdmControl                                                0xAC107F6C
#define SYSCALL_ZwWaitForDebugEvent                                         0x12E1DC72
#define SYSCALL_ZwWaitForKeyedEvent                                         0xCB05DC74
#define SYSCALL_ZwWaitForMultipleObjects                                    0x4B85F002
#define SYSCALL_ZwWaitForMultipleObjects32                                  0x092877F2
#define SYSCALL_ZwWaitForSingleObject                                       0xD5B47747
#define SYSCALL_ZwWaitForWorkViaWorkerFactory                               0x4E5669E0
#define SYSCALL_ZwWaitHighEventPair                                         0x44760F32
#define SYSCALL_ZwWaitLowEventPair                                          0x25A5DCA4
#define SYSCALL_ZwWorkerFactoryWorkerReady                                  0xACEFA1BF
#define SYSCALL_ZwWow64CallFunction64                                       0x008E9DF5
#define SYSCALL_ZwWow64CsrAllocateCaptureBuffer                             0x61A8224E
#define SYSCALL_ZwWow64CsrAllocateMessagePointer                            0x023E216F
#define SYSCALL_ZwWow64CsrCaptureMessageBuffer                              0x873EA761
#define SYSCALL_ZwWow64CsrCaptureMessageString                              0xBB2FCD56
#define SYSCALL_ZwWow64CsrClientCallServer                                  0x308F952D
#define SYSCALL_ZwWow64CsrClientConnectToServer                             0x8F8029B2
#define SYSCALL_ZwWow64CsrFreeCaptureBuffer                                 0xDF755713
#define SYSCALL_ZwWow64CsrGetProcessId                                      0xAF22546D
#define SYSCALL_ZwWow64CsrIdentifyAlertableThread                           0x470FCA7E
#define SYSCALL_ZwWow64CsrVerifyRegion                                      0x67EBA705
#define SYSCALL_ZwWow64DebuggerCall                                         0x0AC012C5
#define SYSCALL_ZwWow64GetCurrentProcessorNumberEx                          0x93B77445
#define SYSCALL_ZwWow64GetNativeSystemInformation                           0x374B4462
#define SYSCALL_ZwWow64InterlockedPopEntrySList                             0x12A47C28
#define SYSCALL_ZwWow64QueryInformationProcess64                            0xD5FED5A5
#define SYSCALL_ZwWow64QueryVirtualMemory64                                 0xAD81A447
#define SYSCALL_ZwWow64ReadVirtualMemory64                                  0xBEF9FD29
#define SYSCALL_ZwWow64WriteVirtualMemory64                                 0x2E87B8A6
#define SYSCALL_ZwWriteFile                                                 0x3CA7B5E7
#define SYSCALL_ZwWriteFileGather                                           0x4B6555D4
#define SYSCALL_ZwWriteRequestData                                          0x3B32C279
#define SYSCALL_ZwWriteVirtualMemory                                        0x0C8297EE
#define SYSCALL_ZwYieldExecution                                            0xE236EECC

#endif // _SYSCALLHOOK_H_4422eab3_99d6_4a37_9f4f_ea45031f9439
