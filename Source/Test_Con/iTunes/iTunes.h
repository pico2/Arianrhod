#include "ml.h"

#define APPLE_APPLICATION_SUPPORT   L"C:\\Program Files (x86)\\Common Files\\Apple\\Apple Application Support"
#define MOBILE_DEVICE_SUPPORT       L"C:\\Program Files (x86)\\Common Files\\Apple\\Mobile Device Support"

#define INIT_STATIC_MEMBER(x) DECL_SELECTANY TYPE_OF(x) x = nullptr
#define LOAD_INTERFACE(_name) *(PVOID *)&_name = GetRoutineAddress(Module, #_name)
#define LOAD_INTERFACE_(_ptr, _name) *(PVOID *)&_ptr = GetRoutineAddress(Module, _name)

#define DECLARE_HANDLE_CHILD(_name, _parent) typedef struct _name##__ : public _parent##__ {} *_name

DECLARE_HANDLE(CFObjectRef);

DECLARE_HANDLE_CHILD(CFDataRef,                 CFObjectRef);
DECLARE_HANDLE_CHILD(CFStringRef,               CFObjectRef);
DECLARE_HANDLE_CHILD(CFBooleanRef,              CFObjectRef);
DECLARE_HANDLE_CHILD(CFArrayRef,                CFObjectRef);
DECLARE_HANDLE_CHILD(CFMutableArrayRef,         CFObjectRef);
DECLARE_HANDLE_CHILD(CFDictionaryRef,           CFObjectRef);
DECLARE_HANDLE_CHILD(CFPropertyListRef,         CFDictionaryRef);
DECLARE_HANDLE_CHILD(CFServiceConnection,       CFObjectRef);

DECLARE_HANDLE_CHILD(AFCConnection,             CFObjectRef);
DECLARE_HANDLE_CHILD(AFCDirectory,              CFObjectRef);
DECLARE_HANDLE_CHILD(AFCFileRef,                CFObjectRef);

typedef CFDataRef*                  PCFDataRef;
typedef CFStringRef*                PCFStringRef;
typedef CFBooleanRef*               PCFBooleanRef;
typedef CFArrayRef*                 PCFArrayRef;
typedef CFMutableArrayRef*          PCFMutableArray;
typedef CFDictionaryRef*            PCFDictionaryRef;
typedef CFPropertyListRef*          PCFPropertyListRef;
typedef CFServiceConnection*        PCFServiceConnection;

typedef LONG            CFTypeID;
typedef LONG            CFIndex;

typedef PVOID           ATH_CONNECTION;

ML_NAMESPACE_BEGIN(iTunesApi)

#include "MobileDevice.h"
#include "AirTrafficHost.h"
#include "CoreFoundation.h"
#include "AppleFileConduit.h"

    inline NTSTATUS Initialize()
    {
        // SetDllDirectoryW(APPLE_APPLICATION_SUPPORT);

        Rtl::EnvironmentAppend(&USTR(L"Path"), &USTR(APPLE_APPLICATION_SUPPORT));
        Rtl::EnvironmentAppend(&USTR(L"Path"), &USTR(MOBILE_DEVICE_SUPPORT));

        LoadDll(L"pthreadVC2.dll");
        LoadDll(L"CoreFoundation.dll");
        LoadDll(L"CFNetwork.dll");

        CF::Initialize();
        ATH::Initialize();
        AMD::Initialize();
        AFC::Initialize();

        return STATUS_SUCCESS;
    }

ML_NAMESPACE_END_(iTunesApi);
