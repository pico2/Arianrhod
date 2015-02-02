ML_NAMESPACE_BEGIN(CF);

extern VOID (CDECL *CFRelease)(CFObjectRef Object);
extern VOID (CDECL *CFRetain)(CFObjectRef Object);

ML_NAMESPACE_END_(CF);


ML_NAMESPACE_BEGIN(AMD);

#define AMDErrorMake(num) (0xe8000000 | (num))

enum MOBILE_DEVICE_ERROR_CODE
{
    kAMDSuccess                                     = 0x0,
    kAMDUndefinedError                              = AMDErrorMake(1),   //0xe8000001
    kAMDBadHeaderError                              = AMDErrorMake(2),   //0xe8000002
    kAMDNoResourcesError                            = AMDErrorMake(3),   //0xe8000003
    kAMDReadError                                   = AMDErrorMake(4),   //0xe8000004
    kAMDWriteError                                  = AMDErrorMake(5),   //0xe8000005
    kAMDUnknownPacketError                          = AMDErrorMake(6),   //0xe8000006
    kAMDInvalidArgumentError                        = AMDErrorMake(7),   //0xe8000007
    kAMDNotFoundError                               = AMDErrorMake(8),   //0xe8000008
    kAMDIsDirectoryError                            = AMDErrorMake(9),   //0xe8000009
    kAMDPermissionError                             = AMDErrorMake(10),  //0xe800000a
    kAMDNotConnectedError                           = AMDErrorMake(11),  //0xe800000b
    kAMDTimeOutError                                = AMDErrorMake(12),  //0xe800000c
    kAMDOverrunError                                = AMDErrorMake(13),  //0xe800000d
    kAMDEOFError                                    = AMDErrorMake(14),  //0xe800000e
    kAMDUnsupportedError                            = AMDErrorMake(15),  //0xe800000f
    kAMDFileExistsError                             = AMDErrorMake(16),  //0xe8000010
    kAMDBusyError                                   = AMDErrorMake(17),  //0xe8000011
    kAMDCryptoError                                 = AMDErrorMake(18),  //0xe8000012

    /* Lockdown errors overlap in this range */
    kAMDInvalidResponseError                        = AMDErrorMake(19),  //0xe8000013
    kAMDMissingKeyError                             = AMDErrorMake(20),  //0xe8000014
    kAMDMissingValueError                           = AMDErrorMake(21),  //0xe8000015
    kAMDGetProhibitedError                          = AMDErrorMake(22),  //0xe8000016
    kAMDSetProhibitedError                          = AMDErrorMake(23),  //0xe8000017
    kAMDRemoveProhibitedError                       = AMDErrorMake(24),  //0xe8000018
    kAMDImmutableValueError                         = AMDErrorMake(25),  //0xe8000019
    kAMDPasswordProtectedError                      = AMDErrorMake(26),  //0xe800001a
    kAMDMissingHostIDError                          = AMDErrorMake(27),  //0xe800001b
    kAMDInvalidHostIDError                          = AMDErrorMake(28),  //0xe800001c
    kAMDSessionActiveError                          = AMDErrorMake(29),  //0xe800001d
    kAMDSessionInactiveError                        = AMDErrorMake(30),  //0xe800001e
    kAMDMissingSessionIDError                       = AMDErrorMake(31),  //0xe800001f
    kAMDInvalidSessionIDError                       = AMDErrorMake(32),  //0xe8000020
    kAMDMissingServiceError                         = AMDErrorMake(33),  //0xe8000021
    kAMDInvalidServiceError                         = AMDErrorMake(34),  //0xe8000022
    kAMDInvalidCheckinError                         = AMDErrorMake(35),  //0xe8000023
    kAMDCheckinTimeoutError                         = AMDErrorMake(36),  //0xe8000024
    kAMDMissingPairRecordError                      = AMDErrorMake(37),  //0xe8000025
    kAMDInvalidActivationRecordError                = AMDErrorMake(38),  //0xe8000026
    kAMDMissingActivationRecordError                = AMDErrorMake(39),  //0xe8000027
    kAMDWrongDroidError                             = AMDErrorMake(40),  //0xe8000028
    kAMDSUVerificationError                         = AMDErrorMake(41),  //0xe8000029
    kAMDSUPatchError                                = AMDErrorMake(42),  //0xe800002a
    kAMDSUFirmwareError                             = AMDErrorMake(43),  //0xe800002b
    kAMDProvisioningProfileNotValid                 = AMDErrorMake(44),  //0xe800002c
    kAMDSendMessageError                            = AMDErrorMake(45),  //0xe800002d
    kAMDReceiveMessageError                         = AMDErrorMake(46),  //0xe800002e
    kAMDMissingOptionsError                         = AMDErrorMake(47),  //0xe800002f
    kAMDMissingImageTypeError                       = AMDErrorMake(48),  //0xe8000030
    kAMDDigestFailedError                           = AMDErrorMake(49),  //0xe8000031
    kAMDStartServiceError                           = AMDErrorMake(50),  //0xe8000032
    kAMDInvalidDiskImageError                       = AMDErrorMake(51),  //0xe8000033
    kAMDMissingDigestError                          = AMDErrorMake(52),  //0xe8000034
    kAMDMuxError                                    = AMDErrorMake(53),  //0xe8000035
    kAMDApplicationAlreadyInstalledError            = AMDErrorMake(54),  //0xe8000036
    kAMDApplicationMoveFailedError                  = AMDErrorMake(55),  //0xe8000037
    kAMDApplicationSINFCaptureFailedError           = AMDErrorMake(56),  //0xe8000038
    kAMDApplicationSandboxFailedError               = AMDErrorMake(57),  //0xe8000039
    kAMDApplicationVerificationFailedError          = AMDErrorMake(58),  //0xe800003a
    kAMDArchiveDestructionFailedError               = AMDErrorMake(59),  //0xe800003b
    kAMDBundleVerificationFailedError               = AMDErrorMake(60),  //0xe800003c
    kAMDCarrierBundleCopyFailedError                = AMDErrorMake(61),  //0xe800003d
    kAMDCarrierBundleDirectoryCreationFailedError   = AMDErrorMake(62),  //0xe800003e
    kAMDCarrierBundleMissingSupportedSIMsError      = AMDErrorMake(63),  //0xe800003f
    kAMDCommCenterNotificationFailedError           = AMDErrorMake(64),  //0xe8000040
    kAMDContainerCreationFailedError                = AMDErrorMake(65),  //0xe8000041
    kAMDContainerP0wnFailedError                    = AMDErrorMake(66),  //0xe8000042
    kAMDContainerRemovalFailedError                 = AMDErrorMake(67),  //0xe8000043
    kAMDEmbeddedProfileInstallFailedError           = AMDErrorMake(68),  //0xe8000044
    kAMDErrorError                                  = AMDErrorMake(69),  //0xe8000045
    kAMDExecutableTwiddleFailedError                = AMDErrorMake(70),  //0xe8000046
    kAMDExistenceCheckFailedError                   = AMDErrorMake(71),  //0xe8000047
    kAMDInstallMapUpdateFailedError                 = AMDErrorMake(72),  //0xe8000048
    kAMDManifestCaptureFailedError                  = AMDErrorMake(73),  //0xe8000049
    kAMDMapGenerationFailedError                    = AMDErrorMake(74),  //0xe800004a
    kAMDMissingBundleExecutableError                = AMDErrorMake(75),  //0xe800004b
    kAMDMissingBundleIdentifierError                = AMDErrorMake(76),  //0xe800004c
    kAMDMissingBundlePathError                      = AMDErrorMake(77),  //0xe800004d
    kAMDMissingContainerError                       = AMDErrorMake(78),  //0xe800004e
    kAMDNotificationFailedError                     = AMDErrorMake(79),  //0xe800004f
    kAMDPackageExtractionFailedError                = AMDErrorMake(80),  //0xe8000050
    kAMDPackageInspectionFailedError                = AMDErrorMake(81),  //0xe8000051
    kAMDPackageMoveFailedError                      = AMDErrorMake(82),  //0xe8000052
    kAMDPathConversionFailedError                   = AMDErrorMake(83),  //0xe8000053
    kAMDRestoreContainerFailedError                 = AMDErrorMake(84),  //0xe8000054
    kAMDSeatbeltProfileRemovalFailedError           = AMDErrorMake(85),  //0xe8000055
    kAMDStageCreationFailedError                    = AMDErrorMake(86),  //0xe8000056
    kAMDSymlinkFailedError                          = AMDErrorMake(87),  //0xe8000057
    kAMDiTunesArtworkCaptureFailedError             = AMDErrorMake(88),  //0xe8000058
    kAMDiTunesMetadataCaptureFailedError            = AMDErrorMake(89),  //0xe8000059
    kAMDAlreadyArchivedError                        = AMDErrorMake(90),  //0xe800005a
    kAMDServiceLimitError                           = AMDErrorMake(91),  //0xe800005b
    kAMDInvalidPairRecordError                      = AMDErrorMake(92),  //0xe800005c
    kAMDServiceProhibitedError                      = AMDErrorMake(93),  //0xe800005d
    kAMDCheckinSetupFailedError                     = AMDErrorMake(94),  //0xe800005e
    kAMDCheckinConnectionFailedError                = AMDErrorMake(95),  //0xe800005f
    kAMDCheckinReceiveFailedError                   = AMDErrorMake(96),  //0xe8000060
    kAMDCheckinResponseFailedError                  = AMDErrorMake(97),  //0xe8000061
    kAMDCheckinSendFailedError                      = AMDErrorMake(98),  //0xe8000062
    kAMDMuxCreateListenerError                      = AMDErrorMake(99),  //0xe8000063
    kAMDMuxGetListenerError                         = AMDErrorMake(100), //0xe8000064
    kAMDMuxConnectError                             = AMDErrorMake(101), //0xe8000065
    kAMDUnknownCommandError                         = AMDErrorMake(102), //0xe8000066
    kAMDAPIInternalError                            = AMDErrorMake(103), //0xe8000067
    kAMDSavePairRecordFailedError                   = AMDErrorMake(104), //0xe8000068
    kAMDCheckinOutOfMemoryError                     = AMDErrorMake(105), //0xe8000069
    kAMDDeviceTooNewError                           = AMDErrorMake(106), //0xe800006a
    kAMDDeviceRefNoGood                             = AMDErrorMake(107), //0xe800006b
    kAMDCannotTranslateError                        = AMDErrorMake(108), //0xe800006c
    kAMDMobileImageMounterMissingImageSignature     = AMDErrorMake(109), //0xe800006d
    kAMDMobileImageMounterResponseCreationFailed    = AMDErrorMake(110), //0xe800006e
    kAMDMobileImageMounterMissingImageType          = AMDErrorMake(111), //0xe800006f
    kAMDMobileImageMounterMissingImagePath          = AMDErrorMake(112), //0xe8000070
    kAMDMobileImageMounterImageMapLoadFailed        = AMDErrorMake(113), //0xe8000071
    kAMDMobileImageMounterAlreadyMounted            = AMDErrorMake(114), //0xe8000072
    kAMDMobileImageMounterImageMoveFailed           = AMDErrorMake(115), //0xe8000073
    kAMDMobileImageMounterMountPathMissing          = AMDErrorMake(116), //0xe8000074
    kAMDMobileImageMounterMountPathNotEmpty         = AMDErrorMake(117), //0xe8000075
    kAMDMobileImageMounterImageMountFailed          = AMDErrorMake(118), //0xe8000076
    kAMDMobileImageMounterTrustCacheLoadFailed      = AMDErrorMake(119), //0xe8000077
    kAMDMobileImageMounterDigestFailed              = AMDErrorMake(120), //0xe8000078
    kAMDMobileImageMounterDigestCreationFailed      = AMDErrorMake(121), //0xe8000079
    kAMDMobileImageMounterImageVerificationFailed   = AMDErrorMake(122), //0xe800007a
    kAMDMobileImageMounterImageInfoCreationFailed   = AMDErrorMake(123), //0xe800007b
    kAMDMobileImageMounterImageMapStoreFailed       = AMDErrorMake(124), //0xe800007c
    kAMDBonjourSetupError                           = AMDErrorMake(125), //0xe800007d
    kAMDDeviceOSVersionTooLow                       = AMDErrorMake(126), //0xe800007e
    kAMDNoWifiSyncSupportError                      = AMDErrorMake(127), //0xe800007f
    kAMDDeviceFamilyNotSupported                    = AMDErrorMake(128), //0xe8000080
    kAMDEscrowLockedError                           = AMDErrorMake(129), //0xe8000081
    kAMDPairingProhibitedError                      = AMDErrorMake(130), //0xe8000082
    kAMDProhibitedBySupervision                     = AMDErrorMake(131), //0xe8000083
    kAMDDeviceDisconnectedError                     = AMDErrorMake(132), //0xe8000084
    kAMDTooBigError                                 = AMDErrorMake(133), //0xe8000085
    kAMDPackagePatchFailedError                     = AMDErrorMake(134), //0xe8000086
    kAMDIncorrectArchitectureError                  = AMDErrorMake(135), //0xe8000087
    kAMDPluginCopyFailedError                       = AMDErrorMake(136), //0xe8000088
    kAMDBreadcrumbFailedError                       = AMDErrorMake(137), //0xe8000089
    kAMDBreadcrumbUnlockError                       = AMDErrorMake(138), //0xe800008a
    kAMDGeoJSONCaptureFailedError                   = AMDErrorMake(139), //0xe800008b
    kAMDNewsstandArtworkCaptureFailedError          = AMDErrorMake(140), //0xe800008c
    kAMDMissingCommandError                         = AMDErrorMake(141), //0xe800008d
    kAMDNotEntitledError                            = AMDErrorMake(142), //0xe800008e
    kAMDMissingPackagePathError                     = AMDErrorMake(143), //0xe800008f
    kAMDMissingContainerPathError                   = AMDErrorMake(144), //0xe8000090
    kAMDMissingApplicationIdentifierError           = AMDErrorMake(145), //0xe8000091
    kAMDMissingAttributeValueError                  = AMDErrorMake(146), //0xe8000092
    kAMDLookupFailedError                           = AMDErrorMake(147), //0xe8000093
    kAMDDictCreationFailedError                     = AMDErrorMake(148), //0xe8000094
    kAMDUserDeniedPairingError                      = AMDErrorMake(149), //0xe8000095
    kAMDPairingDialogResponsePendingError           = AMDErrorMake(150), //0xe8000096
    kAMDInstallProhibitedError                      = AMDErrorMake(151), //0xe8000097
    kAMDUninstallProhibitedError                    = AMDErrorMake(152), //0xe8000098
    kAMDFMiPProtectedError                          = AMDErrorMake(153), //0xe8000099
    kAMDMCProtected                                 = AMDErrorMake(154), //0xe800009a
    kAMDMCChallengeRequired                         = AMDErrorMake(155), //0xe800009b
    kAMDMissingBundleVersionError                   = AMDErrorMake(156), //0xe800009c
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
        STATE_DETACH        = 3,
    };

} DEVICE_CONNECTION_INFO, *PDEVICE_CONNECTION_INFO;

typedef VOID (CDECL *ON_DEVICE_CONNECTION_CHANGED)(PDEVICE_CONNECTION_INFO, PVOID UserData);

typedef struct NOTIFICATION_OBJECT
{
    LONG                            Mode;
    CFArrayRef                      Array;
    CFObjectRef                     USBListener;
    CFRunLoopSourceRef              RunLoopSource;
    ULONG                           Flags;
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
    LONG,
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
CFStringRef
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
   */

DECL_SELECTANY
NTSTATUS
(CDECL
*AMDeviceSecureStartService)(
    PIOS_DEVICE             Device,
    CFStringRef             ServiceName,
    LONG                    Option,
    PCFServiceRef           Service
);

DECL_SELECTANY SOCKET (CDECL *AMDServiceConnectionGetSocket)(CFServiceRef Service);
DECL_SELECTANY PVOID (CDECL *AMDServiceConnectionGetSecureIOContext)(CFServiceRef Service);

DECL_SELECTANY LONG (CDECL *AMDServiceConnectionSend)(CFServiceRef Service, PVOID Buffer, ULONG Length);
DECL_SELECTANY LONG (CDECL *AMDServiceConnectionReceive)(CFServiceRef Service, PVOID Buffer, ULONG Length);

DECL_SELECTANY VOID (CDECL *AMDServiceConnectionInvalidate)(CFServiceRef Service);


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

inline NTSTATUS Initialize()
{
    // SetDllDirectoryW(MOBILE_DEVICE_SUPPORT);

#if USE_ITUNES_MOBILE_DEVICE_DLL

    PVOID Module = LoadDll(L"iTunesMobileDevice.dll");

    LOAD_INTERFACE(AMDeviceRetain);
    LOAD_INTERFACE(AMDeviceRelease);

#else

    PVOID Module = LoadDll(L"MobileDevice.dll");

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

    return STATUS_SUCCESS;
}

ML_NAMESPACE_END_(AMD);
