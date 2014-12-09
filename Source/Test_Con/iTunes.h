#include "ml.h"

#define APPLE_APPLICATION_SUPPORT   L"C:\\Program Files (x86)\\Common Files\\Apple\\Apple Application Support"
#define MOBILE_DEVICE_SUPPORT       L"C:\\Program Files (x86)\\Common Files\\Apple\\Mobile Device Support"

#define INIT_STATIC_MEMBER(x) DECL_SELECTANY TYPE_OF(x) x = nullptr
#define LOAD_INTERFACE(_name) *(PVOID *)&_name = GetRoutineAddress(Module, #_name)
#define LOAD_INTERFACE_(_ptr, _name) *(PVOID *)&_ptr = GetRoutineAddress(Module, _name)

#define DECLARE_HANDLE_CHILD(_name, _parent) typedef struct _name##__ : public _parent##__ {} *_name

DECLARE_HANDLE(CFObjectRef);

DECLARE_HANDLE_CHILD(CFDataRef,         CFObjectRef);
DECLARE_HANDLE_CHILD(CFStringRef,       CFObjectRef);
DECLARE_HANDLE_CHILD(CFBooleanRef,      CFObjectRef);
DECLARE_HANDLE_CHILD(CFDictionary,      CFObjectRef);
DECLARE_HANDLE_CHILD(CFPropertyList,    CFDataRef);

typedef CFDataRef*      PCFDataRef;
typedef CFStringRef*    PCFStringRef;
typedef CFBooleanRef*   PCFBooleanRef;
typedef CFDictionary*   PCFDictionary;
typedef CFPropertyList* PCFPropertyList;

typedef LONG            CFTypeID;
typedef LONG            CFIndex;

typedef PVOID           ATH_CONNECTION;
typedef PVOID           AFC_CONNECTION, *PAFC_CONNECTION;

ML_NAMESPACE_BEGIN(iTunesApi)

    ML_NAMESPACE_BEGIN(CF);

        // type

        DECL_SELECTANY CFTypeID (CDECL *CFGetTypeID)(CFObjectRef Object);
        DECL_SELECTANY CFTypeID (CDECL *CFStringGetTypeID)();
        DECL_SELECTANY CFTypeID (CDECL *CFDictionaryGetTypeID)();


        // data

        DECL_SELECTANY
        CFDataRef
        (CDECL
        *CFDataCreate)(
            PVOID Allocator,
            PBYTE Buffer,
            ULONG Size
        );

        DECL_SELECTANY
        CFPropertyList
        (CDECL
        *CFPropertyListCreateXMLData)(
            PVOID           Allocator,
            CFDictionary    PropertyList
        );

        DECL_SELECTANY CFIndex  (CDECL *CFDataGetLength)(CFDataRef Data);
        DECL_SELECTANY PBYTE    (CDECL *CFDataGetBytePtr)(CFDataRef Data);


        // string

        DECL_SELECTANY CFStringRef (CDECL *CFStringMakeConstantString)(PCSTR String);
        DECL_SELECTANY CFIndex  (CDECL *CFStringGetLength)(CFStringRef String);
        DECL_SELECTANY
        BOOL
        (CDECL
        *CFStringGetCString)(
            CFStringRef String,
            PSTR        Buffer,
            ULONG       BufferSize,
            ULONG       Encoding
        );


        // object

        DECL_SELECTANY VOID (CDECL *CFRelease)(CFObjectRef Object);


        // boolean

        DECL_SELECTANY PCFBooleanRef kCFBooleanTrue;
        DECL_SELECTANY PCFBooleanRef kCFBooleanFalse;

        inline NTSTATUS Initialize()
        {
            PVOID Module = LoadDll(L"CoreFoundation.dll");

            LOAD_INTERFACE(CFPropertyListCreateXMLData);

            LOAD_INTERFACE(CFGetTypeID);
            LOAD_INTERFACE(CFStringGetTypeID);
            LOAD_INTERFACE(CFDictionaryGetTypeID);

            LOAD_INTERFACE(CFDataGetLength);
            LOAD_INTERFACE(CFDataGetBytePtr);

            LOAD_INTERFACE_(CFStringMakeConstantString, "__CFStringMakeConstantString");
            LOAD_INTERFACE(CFStringGetCString);
            LOAD_INTERFACE(CFStringGetLength);

            LOAD_INTERFACE(CFRelease);

            LOAD_INTERFACE(kCFBooleanTrue);
            LOAD_INTERFACE(kCFBooleanFalse);

            return STATUS_SUCCESS;
        }

    ML_NAMESPACE_END_(CF);

    ML_NAMESPACE_BEGIN(ATH);

        DECL_SELECTANY
        ATH_CONNECTION
        (CDECL
        *ATHostConnectionCreateWithLibrary)(
            CFStringRef LibraryID,
            CFStringRef Uuid,
            ULONG       Unknown0
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
            PVOID           cfarrayParam1,
            PVOID           cfmudictParam2,
            CFDictionary    HostInfo
        );

        DECL_SELECTANY
        NTSTATUS
        (CDECL
        *ATHostConnectionSendHostInfo)(
            ATH_CONNECTION  Connection,
            CFDictionary    Dict
        );

        DECL_SELECTANY
        CFDictionary
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
        NTSTATUS
        (CDECL
        *ATHostConnectionSendMetadataSyncFinished)(
            ATH_CONNECTION  Connection,
            PVOID           cfmudictParam1,
            PVOID           cfmudictParam2
        );

        DECL_SELECTANY
        NTSTATUS
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
        *ATHostConnectionSendSyncFailed)(
            ATH_CONNECTION  Connection,
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

        inline NTSTATUS Initialize()
        {
            SetDllDirectoryW(MOBILE_DEVICE_SUPPORT);

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

            return STATUS_SUCCESS;
        }

    ML_NAMESPACE_END_(ATH);

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

        typedef VOID (CDECL *ON_DEVICE_CONNECTION_CHANGED)(PDEVICE_CONNECTION_INFO);

        DECL_SELECTANY
        NTSTATUS
        (CDECL
        *AMDeviceNotificationSubscribe)(
            ON_DEVICE_CONNECTION_CHANGED *OnDeviceConnectionChanged,
            LONG,
            LONG,
            LONG,
            PHANDLE Device
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

        DECL_SELECTANY
        NTSTATUS
        (CDECL
        *AMDeviceSecureStartService)(
            HANDLE          Device,
            CFStringRef     ServiceName,
            LONG            Option,
            PAFC_CONNECTION Connection
        );

        DECL_SELECTANY SOCKET (CDECL *AMDServiceConnectionGetSocket)(AFC_CONNECTION Connection);
        DECL_SELECTANY PVOID (CDECL *AMDServiceConnectionGetSecureIOContext)(AFC_CONNECTION Connection);

        inline NTSTATUS Initialize()
        {
            SetDllDirectoryW(MOBILE_DEVICE_SUPPORT);

            PVOID Module = LoadDll(L"iTunesMobileDevice.dll");

            LOAD_INTERFACE(AMDeviceNotificationSubscribe);
            LOAD_INTERFACE(AMDeviceSecureStartService);
            LOAD_INTERFACE(AMDServiceConnectionGetSocket);
            LOAD_INTERFACE(AMDServiceConnectionGetSecureIOContext);

            return STATUS_SUCCESS;
        }

    ML_NAMESPACE_END_(AMD);

    inline NTSTATUS Initialize()
    {
        SetDllDirectoryW(APPLE_APPLICATION_SUPPORT);

        LoadDll(L"pthreadVC2.dll");
        LoadDll(L"CoreFoundation.dll");
        LoadDll(L"CFNetwork.dll");

        CF::Initialize();
        ATH::Initialize();
        AMD::Initialize();

        return STATUS_SUCCESS;
    }

ML_NAMESPACE_END_(iTunesApi);
