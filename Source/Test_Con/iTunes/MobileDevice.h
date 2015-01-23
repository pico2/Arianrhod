ML_NAMESPACE_BEGIN(AMD);

    typedef struct
    {
        HANDLE  Device;
        ULONG   State;

        enum
        {
            STATE_CONNECT       = 1,
            STATE_DISCONNECT    = 2,
            STATE_UNKNOW        = 3,
        };

    } DEVICE_CONNECTION_INFO, *PDEVICE_CONNECTION_INFO;

    typedef VOID (CDECL *ON_DEVICE_CONNECTION_CHANGED)(PDEVICE_CONNECTION_INFO, PVOID UserData);

    DECL_SELECTANY
    NTSTATUS
    (CDECL
    *AMDeviceNotificationSubscribe)(
        ON_DEVICE_CONNECTION_CHANGED OnDeviceConnectionChanged,
        LONG,
        LONG,
        PVOID UserData,
        PHANDLE Device
    );

    DECL_SELECTANY NTSTATUS (CDECL *AMDeviceRetain)(HANDLE Device);
    DECL_SELECTANY NTSTATUS (CDECL *AMDeviceIsPaired)(HANDLE Device);
    DECL_SELECTANY NTSTATUS (CDECL *AMDeviceValidatePairing)(HANDLE Device);
    DECL_SELECTANY NTSTATUS (CDECL *AMDeviceStartSession)(HANDLE Device);
    DECL_SELECTANY NTSTATUS (CDECL *AMDeviceStopSession)(HANDLE Device);
    DECL_SELECTANY NTSTATUS (CDECL *AMDeviceConnect)(HANDLE Device);
    DECL_SELECTANY NTSTATUS (CDECL *AMDeviceDisconnect)(HANDLE Device);


    /*++

        ServiceName:
            com.apple.mobile.installation_proxy
            com.apple.mobile.notification_proxy
            com.apple.afc
            com.apple.afc2
            com.apple.mobile.diagnostics_relay
            com.apple.mobile.screenshotr

    --*/

    DECL_SELECTANY
    NTSTATUS
    (CDECL
    *AMDeviceSecureStartService)(
        HANDLE                  Device,
        CFStringRef             ServiceName,
        LONG                    Option,
        PCFServiceConnection    Connection
    );

    DECL_SELECTANY SOCKET (CDECL *AMDServiceConnectionGetSocket)(CFServiceConnection Connection);
    DECL_SELECTANY PVOID (CDECL *AMDServiceConnectionGetSecureIOContext)(CFServiceConnection Connection);

    DECL_SELECTANY LONG (CDECL *AMDServiceConnectionSend)(CFServiceConnection Connection, PVOID Buffer, ULONG Length);
    DECL_SELECTANY LONG (CDECL *AMDServiceConnectionReceive)(CFServiceConnection Connection, PVOID Buffer, ULONG Length);

    DECL_SELECTANY VOID (CDECL *AMDServiceConnectionInvalidate)(CFServiceConnection Connection);

    inline NTSTATUS Initialize()
    {
        // SetDllDirectoryW(MOBILE_DEVICE_SUPPORT);

        PVOID Module = LoadDll(L"iTunesMobileDevice.dll");

        LOAD_INTERFACE(AMDeviceNotificationSubscribe);

        LOAD_INTERFACE(AMDeviceRetain);
        LOAD_INTERFACE(AMDeviceIsPaired);
        LOAD_INTERFACE(AMDeviceValidatePairing);
        LOAD_INTERFACE(AMDeviceStartSession);
        LOAD_INTERFACE(AMDeviceStopSession);
        LOAD_INTERFACE(AMDeviceConnect);
        LOAD_INTERFACE(AMDeviceDisconnect);

        LOAD_INTERFACE(AMDeviceSecureStartService);
        LOAD_INTERFACE(AMDServiceConnectionGetSocket);
        LOAD_INTERFACE(AMDServiceConnectionGetSecureIOContext);
        LOAD_INTERFACE(AMDServiceConnectionSend);
        LOAD_INTERFACE(AMDServiceConnectionReceive);
        LOAD_INTERFACE(AMDServiceConnectionInvalidate);

        return STATUS_SUCCESS;
    }

ML_NAMESPACE_END_(AMD);
