ML_NAMESPACE_BEGIN(CF);

extern VOID (CDECL *CFRelease)(CFObjectRef Object);
extern VOID (CDECL *CFRetain)(CFObjectRef Object);

ML_NAMESPACE_END_(CF);


ML_NAMESPACE_BEGIN(AMD);

enum MOBILE_DEVICE_ERROR_CODE
{
    kAMDSuccess                                   = 0x00000000,
    kAMDUndefinedError                            = 0xE8000001,
    kAMDBadHeaderError                            = 0xE8000002,
    kAMDNoResourcesError                          = 0xE8000003,
    kAMDReadError                                 = 0xE8000004,
    kAMDWriteError                                = 0xE8000005,
    kAMDUnknownPacketError                        = 0xE8000006,
    kAMDInvalidArgumentError                      = 0xE8000007,
    kAMDNotFoundError                             = 0xE8000008,
    kAMDIsDirectoryError                          = 0xE8000009,
    kAMDPermissionError                           = 0xE800000A,
    kAMDNotConnectedError                         = 0xE800000B,
    kAMDTimeOutError                              = 0xE800000C,
    kAMDOverrunError                              = 0xE800000D,
    kAMDEOFError                                  = 0xE800000E,
    kAMDUnsupportedError                          = 0xE800000F,
    kAMDFileExistsError                           = 0xE8000010,
    kAMDBusyError                                 = 0xE8000011,
    kAMDCryptoError                               = 0xE8000012,
    kAMDInvalidResponseError                      = 0xE8000013,
    kAMDMissingKeyError                           = 0xE8000014,
    kAMDMissingValueError                         = 0xE8000015,
    kAMDGetProhibitedError                        = 0xE8000016,
    kAMDSetProhibitedError                        = 0xE8000017,
    kAMDRemoveProhibitedError                     = 0xE8000018,
    kAMDImmutableValueError                       = 0xE8000019,
    kAMDPasswordProtectedError                    = 0xE800001A,
    kAMDMissingHostIDError                        = 0xE800001B,
    kAMDInvalidHostIDError                        = 0xE800001C,
    kAMDSessionActiveError                        = 0xE800001D,
    kAMDSessionInactiveError                      = 0xE800001E,
    kAMDMissingSessionIDError                     = 0xE800001F,
    kAMDInvalidSessionIDError                     = 0xE8000020,
    kAMDMissingServiceError                       = 0xE8000021,
    kAMDInvalidServiceError                       = 0xE8000022,
    kAMDInvalidCheckinError                       = 0xE8000023,
    kAMDCheckinTimeoutError                       = 0xE8000024,
    kAMDMissingPairRecordError                    = 0xE8000025,
    kAMDInvalidActivationRecordError              = 0xE8000026,
    kAMDMissingActivationRecordError              = 0xE8000027,
    kAMDWrongDroidError                           = 0xE8000028,
    kAMDSUVerificationError                       = 0xE8000029,
    kAMDSUPatchError                              = 0xE800002A,
    kAMDSUFirmwareError                           = 0xE800002B,
    kAMDProvisioningProfileNotValid               = 0xE800002C,
    kAMDSendMessageError                          = 0xE800002D,
    kAMDReceiveMessageError                       = 0xE800002E,
    kAMDMissingOptionsError                       = 0xE800002F,
    kAMDMissingImageTypeError                     = 0xE8000030,
    kAMDDigestFailedError                         = 0xE8000031,
    kAMDStartServiceError                         = 0xE8000032,
    kAMDInvalidDiskImageError                     = 0xE8000033,
    kAMDMissingDigestError                        = 0xE8000034,
    kAMDMuxError                                  = 0xE8000035,
    kAMDApplicationAlreadyInstalledError          = 0xE8000036,
    kAMDApplicationMoveFailedError                = 0xE8000037,
    kAMDApplicationSINFCaptureFailedError         = 0xE8000038,
    kAMDApplicationSandboxFailedError             = 0xE8000039,
    kAMDApplicationVerificationFailedError        = 0xE800003A,
    kAMDArchiveDestructionFailedError             = 0xE800003B,
    kAMDBundleVerificationFailedError             = 0xE800003C,
    kAMDCarrierBundleCopyFailedError              = 0xE800003D,
    kAMDCarrierBundleDirectoryCreationFailedError = 0xE800003E,
    kAMDCarrierBundleMissingSupportedSIMsError    = 0xE800003F,
    kAMDCommCenterNotificationFailedError         = 0xE8000040,
    kAMDContainerCreationFailedError              = 0xE8000041,
    kAMDContainerP0wnFailedError                  = 0xE8000042,
    kAMDContainerRemovalFailedError               = 0xE8000043,
    kAMDEmbeddedProfileInstallFailedError         = 0xE8000044,
    kAMDErrorError                                = 0xE8000045,
    kAMDExecutableTwiddleFailedError              = 0xE8000046,
    kAMDExistenceCheckFailedError                 = 0xE8000047,
    kAMDInstallMapUpdateFailedError               = 0xE8000048,
    kAMDManifestCaptureFailedError                = 0xE8000049,
    kAMDMapGenerationFailedError                  = 0xE800004A,
    kAMDMissingBundleExecutableError              = 0xE800004B,
    kAMDMissingBundleIdentifierError              = 0xE800004C,
    kAMDMissingBundlePathError                    = 0xE800004D,
    kAMDMissingContainerError                     = 0xE800004E,
    kAMDNotificationFailedError                   = 0xE800004F,
    kAMDPackageExtractionFailedError              = 0xE8000050,
    kAMDPackageInspectionFailedError              = 0xE8000051,
    kAMDPackageMoveFailedError                    = 0xE8000052,
    kAMDPathConversionFailedError                 = 0xE8000053,
    kAMDRestoreContainerFailedError               = 0xE8000054,
    kAMDSeatbeltProfileRemovalFailedError         = 0xE8000055,
    kAMDStageCreationFailedError                  = 0xE8000056,
    kAMDSymlinkFailedError                        = 0xE8000057,
    kAMDiTunesArtworkCaptureFailedError           = 0xE8000058,
    kAMDiTunesMetadataCaptureFailedError          = 0xE8000059,
    kAMDAlreadyArchivedError                      = 0xE800005A,
    kAMDServiceLimitError                         = 0xE800005B,
    kAMDInvalidPairRecordError                    = 0xE800005C,
    kAMDServiceProhibitedError                    = 0xE800005D,
    kAMDCheckinSetupFailedError                   = 0xE800005E,
    kAMDCheckinConnectionFailedError              = 0xE800005F,
    kAMDCheckinReceiveFailedError                 = 0xE8000060,
    kAMDCheckinResponseFailedError                = 0xE8000061,
    kAMDCheckinSendFailedError                    = 0xE8000062,
    kAMDMuxCreateListenerError                    = 0xE8000063,
    kAMDMuxGetListenerError                       = 0xE8000064,
    kAMDMuxConnectError                           = 0xE8000065,
    kAMDUnknownCommandError                       = 0xE8000066,
    kAMDAPIInternalError                          = 0xE8000067,
    kAMDSavePairRecordFailedError                 = 0xE8000068,
    kAMDCheckinOutOfMemoryError                   = 0xE8000069,
    kAMDDeviceTooNewError                         = 0xE800006A,
    kAMDDeviceRefNoGood                           = 0xE800006B,
    kAMDCannotTranslateError                      = 0xE800006C,
    kAMDMobileImageMounterMissingImageSignature   = 0xE800006D,
    kAMDMobileImageMounterResponseCreationFailed  = 0xE800006E,
    kAMDMobileImageMounterMissingImageType        = 0xE800006F,
    kAMDMobileImageMounterMissingImagePath        = 0xE8000070,
    kAMDMobileImageMounterImageMapLoadFailed      = 0xE8000071,
    kAMDMobileImageMounterAlreadyMounted          = 0xE8000072,
    kAMDMobileImageMounterImageMoveFailed         = 0xE8000073,
    kAMDMobileImageMounterMountPathMissing        = 0xE8000074,
    kAMDMobileImageMounterMountPathNotEmpty       = 0xE8000075,
    kAMDMobileImageMounterImageMountFailed        = 0xE8000076,
    kAMDMobileImageMounterTrustCacheLoadFailed    = 0xE8000077,
    kAMDMobileImageMounterDigestFailed            = 0xE8000078,
    kAMDMobileImageMounterDigestCreationFailed    = 0xE8000079,
    kAMDMobileImageMounterImageVerificationFailed = 0xE800007A,
    kAMDMobileImageMounterImageInfoCreationFailed = 0xE800007B,
    kAMDMobileImageMounterImageMapStoreFailed     = 0xE800007C,
    kAMDBonjourSetupError                         = 0xE800007D,
    kAMDDeviceOSVersionTooLow                     = 0xE800007E,
    kAMDNoWifiSyncSupportError                    = 0xE800007F,
    kAMDDeviceFamilyNotSupported                  = 0xE8000080,
    kAMDEscrowLockedError                         = 0xE8000081,
    kAMDPairingProhibitedError                    = 0xE8000082,
    kAMDProhibitedBySupervision                   = 0xE8000083,
    kAMDDeviceDisconnectedError                   = 0xE8000084,
    kAMDTooBigError                               = 0xE8000085,
    kAMDPackagePatchFailedError                   = 0xE8000086,
    kAMDIncorrectArchitectureError                = 0xE8000087,
    kAMDPluginCopyFailedError                     = 0xE8000088,
    kAMDBreadcrumbFailedError                     = 0xE8000089,
    kAMDBreadcrumbUnlockError                     = 0xE800008A,
    kAMDGeoJSONCaptureFailedError                 = 0xE800008B,
    kAMDNewsstandArtworkCaptureFailedError        = 0xE800008C,
    kAMDMissingCommandError                       = 0xE800008D,
    kAMDNotEntitledError                          = 0xE800008E,
    kAMDMissingPackagePathError                   = 0xE800008F,
    kAMDMissingContainerPathError                 = 0xE8000090,
    kAMDMissingApplicationIdentifierError         = 0xE8000091,
    kAMDMissingAttributeValueError                = 0xE8000092,
    kAMDLookupFailedError                         = 0xE8000093,
    kAMDDictCreationFailedError                   = 0xE8000094,
    kAMDUserDeniedPairingError                    = 0xE8000095,
    kAMDPairingDialogResponsePendingError         = 0xE8000096,
    kAMDInstallProhibitedError                    = 0xE8000097,
    kAMDUninstallProhibitedError                  = 0xE8000098,
    kAMDFMiPProtectedError                        = 0xE8000099,
    kAMDMCProtected                               = 0xE800009A,
    kAMDMCChallengeRequired                       = 0xE800009B,
    kAMDMissingBundleVersionError                 = 0xE800009C,
    kAMDAppBlacklistedError                       = 0xE800009D,
};

typedef struct
{

} IOS_DEVICE, *PIOS_DEVICE;

struct NOTIFICATION_OBJECT;

typedef struct
{
    PIOS_DEVICE             Device;
    ULONG                   State;
    NOTIFICATION_OBJECT*    Notification;

    enum
    {
        STATE_CONNECT       = 1,
        STATE_DISCONNECT    = 2,
        STATE_UNSUBSCRIBE   = 3,
    };

} DEVICE_CONNECTION_INFO, *PDEVICE_CONNECTION_INFO;

typedef VOID (CDECL *ON_DEVICE_CONNECTION_CHANGED)(PDEVICE_CONNECTION_INFO, PVOID UserData);

typedef struct NOTIFICATION_OBJECT
{
    ULONG                           Mode;
    CFArrayRef                      Array;
    CFObjectRef                     USBListener;
    CFRunLoopSourceRef              RunLoopSource;
    USHORT                          Flags;
    ON_DEVICE_CONNECTION_CHANGED    Callback;
    PVOID                           CallbackContext;

} NOTIFICATION_OBJECT, *PNOTIFICATION_OBJECT;



/*  Registers a notification with the current run loop. The callback gets
*  copied into the notification struct, as well as being registered with the
*  current run loop. Cookie gets copied into cookie in the same.
*  (Cookie is a user info parameter that gets passed as an arg to
*  the callback) unused0 and unused1 are both 0 when iTunes calls this.
*
*  Never try to acces directly or copy contents of dev and subscription fields
*  in am_device_notification_callback_info. Treat them as abstract handles.
*  When done with connection use AMDeviceRelease to free resources allocated for am_device.
*
*  Returns:
*      MDERR_OK            if successful
*      MDERR_SYSCALL       if CFRunLoopAddSource() failed
*      MDERR_OUT_OF_MEMORY if we ran out of memory
*/

DECL_SELECTANY
NTSTATUS
(CDECL
*AMDeviceNotificationSubscribe)(
    ON_DEVICE_CONNECTION_CHANGED    OnDeviceConnectionChanged,
    LONG,
    ULONG                           Mode,
    PVOID                           UserData,
    PNOTIFICATION_OBJECT*           Notification
);


/* Unregisters notifications. Buggy (iTunes 8.2): if you subscribe, unsubscribe and subscribe again, arriving
   notifications will contain cookie and subscription from 1st call to subscribe, not the 2nd one. iTunes
   calls this function only once on exit.
*/
DECL_SELECTANY
NTSTATUS
(CDECL
*AMDeviceNotificationUnsubscribe)(
    PNOTIFICATION_OBJECT Notification
);

/* Decrements reference counter and, if nothing left, releases resources hold
* by connection, invalidates  pointer to device
*/

DECL_SELECTANY
VOID
(CDECL
*AMDeviceRelease)(
    PIOS_DEVICE Device
);

/*
    Returns device_id field of am_device structure
*/

DECL_SELECTANY
NTSTATUS
(CDECL
*AMDeviceGetConnectionID)(
    PIOS_DEVICE Device
);


/*
    Returns serial field of am_device structure
*/

DECL_SELECTANY
CFStringRef
(CDECL
*AMDeviceCopyDeviceIdentifier)(
    PIOS_DEVICE Device
);


/*  Connects to the iPhone. Pass in the am_device structure that the
*  notification callback will give to you.
*
*  Returns:
*      MDERR_OK                if successfully connected
*      MDERR_SYSCALL           if setsockopt() failed
*      MDERR_QUERY_FAILED      if the daemon query failed
*      MDERR_INVALID_ARGUMENT  if USBMuxConnectByPort returned 0xffffffff
*/

DECL_SELECTANY
NTSTATUS
(CDECL
*AMDeviceConnect)(
    PIOS_DEVICE Device
);

DECL_SELECTANY
NTSTATUS
(CDECL
*AMDeviceDisconnect)(
    PIOS_DEVICE Device
);

/*
    Increments reference counter
*/
DECL_SELECTANY
VOID
(CDECL
*AMDeviceRetain)(
    PIOS_DEVICE Device
);


/*  Calls PairingRecordPath() on the given device, than tests whether the path
*  which that function returns exists. During the initial connect, the path
*  returned by that function is '/', and so this returns 1.
*
*  Returns:
*      0   if the path did not exist
*      1   if it did
*/

DECL_SELECTANY
BOOL
(CDECL
*AMDevicePair)(
    PIOS_DEVICE Device
);

DECL_SELECTANY
BOOL
(CDECL
*AMDeviceIsPaired)(
    PIOS_DEVICE Device
);


/*  iTunes calls this function immediately after testing whether the device is
*  paired. It creates a pairing file and establishes a Lockdown connection.
*
*  Returns:
*      MDERR_OK                if successful
*      MDERR_INVALID_ARGUMENT  if the supplied device is null
*      MDERR_DICT_NOT_LOADED   if the load_dict() call failed
*/

DECL_SELECTANY
NTSTATUS
(CDECL
*AMDeviceValidatePairing)(
    PIOS_DEVICE Device
);

DECL_SELECTANY
NTSTATUS
(CDECL
*AMDevicePairWithOptions)(
    PIOS_DEVICE     Device,
    CFDictionaryRef Record
);

/*  Creates a Lockdown session and adjusts the device structure appropriately
*  to indicate that the session has been started. iTunes calls this function
*  after validating pairing.
*
*  Returns:
*      MDERR_OK                if successful
*      MDERR_INVALID_ARGUMENT  if the Lockdown conn has not been established
*      MDERR_DICT_NOT_LOADED   if the load_dict() call failed
*/

DECL_SELECTANY
NTSTATUS
(CDECL
*AMDeviceStartSession)(
    PIOS_DEVICE Device
);


/* Stops a session. You should do this before accessing services.
*
* Returns:
*      MDERR_OK                if successful
*      MDERR_INVALID_ARGUMENT  if the Lockdown conn has not been established
*/

DECL_SELECTANY
NTSTATUS
(CDECL
*AMDeviceStopSession)(
    PIOS_DEVICE Device
);



/* Reads various device settings. One of domain or cfstring arguments should be NULL.
    *
    * Possible values for cfstring:
    * ActivationState
    * ActivationStateAcknowledged
    * BasebandBootloaderVersion
    * BasebandVersion
    * BluetoothAddress
    * BuildVersion
    * CPUArchitecture
    * DeviceCertificate
    * DeviceClass
    * DeviceName
    * DevicePublicKey
    * FirmwareVersion
    * HostAttached
    * IntegratedCircuitCardIdentity
    * InternationalMobileEquipmentIdentity
    * InternationalMobileSubscriberIdentity
    * ModelNumber
    * PhoneNumber
    * ProductType
    * ProductVersion
    * ProtocolVersion
    * RegionInfo
    * SBLockdownEverRegisteredKey
    * SIMStatus
    * SerialNumber
    * SomebodySetTimeZone
    * TimeIntervalSince1970
    * TimeZone
    * TimeZoneOffsetFromUTC
    * TrustedHostAttached
    * UniqueDeviceID
    * Uses24HourClock
    * WiFiAddress
    * iTunesHasConnected
    *
    * Possible values for domain:
    * com.apple.mobile.battery
*/

DECL_SELECTANY
CFObjectRef
(CDECL
*AMDeviceCopyValue)(
    PIOS_DEVICE Device,
    CFStringRef Domain,
    CFStringRef Key
);


/*++

    ServiceName:
        com.apple.mobile.installation_proxy
        com.apple.mobile.notification_proxy
        com.apple.afc
        com.apple.afc2
        com.apple.mobile.diagnostics_relay
        com.apple.mobile.screenshotr

--*/

/* Starts a service and returns a socket file descriptor that can be used in order to further
* access the service. You should stop the session and disconnect before using
* the service. iTunes calls this function after starting a session. It starts
* the service and the SSL connection. service_name should be one of the AMSVC_*
* constants.
*
* Returns:
*      MDERR_OK                if successful
*      MDERR_SYSCALL           if the setsockopt() call failed
*      MDERR_INVALID_ARGUMENT  if the Lockdown conn has not been established
*
* Possible values for Options:
*     CloseOnInvalidate:    Boolean
*     TimeoutConnection:    Boolean
*     UnlockEscrowBag:      Boolean
*     DirectSocket:         Boolean
*
*/

DECL_SELECTANY
NTSTATUS
(CDECL
*AMDeviceSecureStartService)(
    PIOS_DEVICE             Device,
    CFStringRef             ServiceName,
    CFDictionaryRef         Options,
    PCFServiceRef           Service
);

DECL_SELECTANY
SOCKET
(CDECL
*AMDServiceConnectionGetSocket)(
    CFServiceRef Service
);

DECL_SELECTANY
PVOID
(CDECL
*AMDServiceConnectionGetSecureIOContext)(
    CFServiceRef Service
);

DECL_SELECTANY
LONG
(CDECL
*AMDServiceConnectionSend)(
    CFServiceRef    Service,
    PVOID           Buffer,
    ULONG           Length
);

DECL_SELECTANY
LONG
(CDECL
*AMDServiceConnectionReceive)(
    CFServiceRef    Service,
    PVOID           Buffer,
    ULONG           Length
);


DECL_SELECTANY
VOID
(CDECL
*AMDServiceConnectionInvalidate)(
    CFServiceRef Service
);


DECL_SELECTANY
NTSTATUS
(CDECL
*AMDeviceActivate)(
    PIOS_DEVICE     Device,
    CFDictionaryRef dict
);

DECL_SELECTANY
NTSTATUS
(CDECL
*AMDeviceDeactivate)(
    PIOS_DEVICE Device
);

DECL_SELECTANY
NTSTATUS
(CDECL
*AMDeviceRemoveValue)(
    PIOS_DEVICE Device,
    CFStringRef Domain,
    CFStringRef Key
);

DECL_SELECTANY
PCSTR
(CDECL
*AMDErrorString)(
    NTSTATUS ErrorCode
);

inline NTSTATUS Initialize()
{
    PVOID Module = LoadDll(MOBILE_DEVICE_DLL);

#if USE_ITUNES_MOBILE_DEVICE_DLL

    LOAD_INTERFACE(AMDeviceRetain);
    LOAD_INTERFACE(AMDeviceRelease);

#else

    AMDeviceRelease = [] (PIOS_DEVICE Device)
    {
        if (Device != nullptr)
            CF::CFRelease((CFObjectRef)Device);
    };

    AMDeviceRetain = [] (PIOS_DEVICE Device)
    {
        if (Device != nullptr)
            CF::CFRetain((CFObjectRef)Device);
    };

#endif

    LOAD_INTERFACE(AMDeviceNotificationSubscribe);
    LOAD_INTERFACE(AMDeviceNotificationUnsubscribe);
    LOAD_INTERFACE(AMDeviceGetConnectionID);

    LOAD_INTERFACE(AMDevicePair);
    LOAD_INTERFACE(AMDeviceIsPaired);
    LOAD_INTERFACE(AMDeviceValidatePairing);
    LOAD_INTERFACE(AMDevicePairWithOptions);
    LOAD_INTERFACE(AMDeviceStartSession);
    LOAD_INTERFACE(AMDeviceStopSession);
    LOAD_INTERFACE(AMDeviceConnect);
    LOAD_INTERFACE(AMDeviceDisconnect);

    LOAD_INTERFACE(AMDeviceCopyValue);

    LOAD_INTERFACE(AMDeviceSecureStartService);
    LOAD_INTERFACE(AMDServiceConnectionGetSocket);
    LOAD_INTERFACE(AMDServiceConnectionGetSecureIOContext);
    LOAD_INTERFACE(AMDServiceConnectionSend);
    LOAD_INTERFACE(AMDServiceConnectionReceive);
    LOAD_INTERFACE(AMDServiceConnectionInvalidate);

    LOAD_INTERFACE(AMDeviceDeactivate);
    LOAD_INTERFACE(AMDeviceActivate);
    LOAD_INTERFACE(AMDeviceRemoveValue);

    LOAD_INTERFACE(AMDErrorString);

    return STATUS_SUCCESS;
}

ML_NAMESPACE_END_(AMD);
