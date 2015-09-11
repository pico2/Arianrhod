ML_NAMESPACE_BEGIN(ATH);

DECL_SELECTANY
ATH_CONNECTION
(CDECL
*ATHostConnectionCreateWithLibrary)(
    CFStringRef LibraryID,
    CFStringRef Udid,
    CFStringRef ATHPath
);

DECL_SELECTANY
NTSTATUS
(CDECL
*ATHostConnectionSendPowerAssertion)(
    ATH_CONNECTION  Connection,
    CFBooleanRef    Enabled
);

DECL_SELECTANY
NTSTATUS
(CDECL
*ATHostConnectionSendSyncRequest)(
    ATH_CONNECTION  Connection,
    CFArrayRef      Dataclasses,
    CFDictionaryRef DataclassAnchors,
    CFDictionaryRef HostInfo
);

DECL_SELECTANY
NTSTATUS
(CDECL
*ATHostConnectionSendMetadataSyncFinished)(
    ATH_CONNECTION  Connection,
    CFDictionaryRef Dataclasses,
    CFDictionaryRef DataclassAnchors
);

DECL_SELECTANY
NTSTATUS
(CDECL
*ATHostConnectionSendSyncFailed)(
    ATH_CONNECTION  Connection,
    NTSTATUS        nErrorCode
);

DECL_SELECTANY
NTSTATUS
(CDECL
*ATHostConnectionSendHostInfo)(
    ATH_CONNECTION  Connection,
    CFDictionaryRef HostInfo
);

DECL_SELECTANY
CFPropertyListRef
(CDECL
*ATHostConnectionReadMessage)(
    ATH_CONNECTION Connection
);

DECL_SELECTANY
VOID
(CDECL
*ATHostConnectionRetain)(
    ATH_CONNECTION Connection
);

DECL_SELECTANY
VOID
(CDECL
*ATHostConnectionRelease)(
    ATH_CONNECTION Connection
);

DECL_SELECTANY
VOID
(CDECL
*ATHostConnectionDestroy)(
    ATH_CONNECTION Connection
);

DECL_SELECTANY
NTSTATUS
(CDECL
*ATHostConnectionSendAssetCompleted)(
    ATH_CONNECTION  Connection,
    PVOID           cfstrParam1,
    PVOID           cfstrParam2,
    PVOID           cfstrParam3
);

DECL_SELECTANY
ULONG
(CDECL
*ATHostConnectionGetGrappaSessionId)(
    ATH_CONNECTION Connection
);

DECL_SELECTANY
NTSTATUS
(CDECL
*ATHostConnectionSendFileBegin)(
    ATH_CONNECTION  Connection,
    PVOID           cfstrParam1,
    PVOID           cfstrParam2,
    UINT64          cfstrParam3,
    UINT64          cfstrParam4
);

DECL_SELECTANY
NTSTATUS
(CDECL
*ATHostConnectionSendFileProgress)(
    ATH_CONNECTION  Connection,
    PVOID           cfstrParam1,
    PVOID           cfstrParam2,
    double          nParam3,
    double          nParam4
);

DECL_SELECTANY
NTSTATUS
(CDECL
*ATHostConnectionSendFileError)(
    ATH_CONNECTION  Connection,
    PVOID           cfstrParam1,
    PVOID           cfstrParam2,
    NTSTATUS        nErrorCode
);

DECL_SELECTANY
NTSTATUS
(CDECL
*ATHostConnectionSendPing)(
    ATH_CONNECTION Connection
);

DECL_SELECTANY
NTSTATUS
(CDECL
*ATHostConnectionSendMessage)(
    ATH_CONNECTION  Connection,
    PVOID           cfstrParam1
);

DECL_SELECTANY
CFStringRef
(CDECL
*ATCFMessageGetName)(
    CFPropertyListRef Message
);

DECL_SELECTANY
CFDictionaryRef
(CDECL
*ATCFMessageGetParam)(
    CFPropertyListRef Message
);

inline NTSTATUS Initialize()
{
    // SetDllDirectoryW(MOBILE_DEVICE_SUPPORT);

    PVOID Module = LoadDll(L"AirTrafficHost.dll");

    LOAD_INTERFACE(ATHostConnectionCreateWithLibrary);
    LOAD_INTERFACE(ATHostConnectionSendPowerAssertion);
    LOAD_INTERFACE(ATHostConnectionSendSyncRequest);
    LOAD_INTERFACE(ATHostConnectionSendHostInfo);
    LOAD_INTERFACE(ATHostConnectionReadMessage);
    LOAD_INTERFACE(ATHostConnectionRetain);
    LOAD_INTERFACE(ATHostConnectionRelease);
    LOAD_INTERFACE(ATHostConnectionSendMetadataSyncFinished);
    LOAD_INTERFACE(ATHostConnectionDestroy);
    LOAD_INTERFACE(ATHostConnectionSendAssetCompleted);
    LOAD_INTERFACE(ATHostConnectionGetGrappaSessionId);
    LOAD_INTERFACE(ATHostConnectionSendFileBegin);
    LOAD_INTERFACE(ATHostConnectionSendFileProgress);
    LOAD_INTERFACE(ATHostConnectionSendFileError);
    LOAD_INTERFACE(ATHostConnectionSendSyncFailed);
    LOAD_INTERFACE(ATHostConnectionSendPing);
    LOAD_INTERFACE(ATHostConnectionSendMessage);

    LOAD_INTERFACE(ATCFMessageGetName);
    LOAD_INTERFACE(ATCFMessageGetParam);

    return STATUS_SUCCESS;
}

ML_NAMESPACE_END_(ATH);
