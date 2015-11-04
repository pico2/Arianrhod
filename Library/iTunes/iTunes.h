#ifndef _ITUNES_H_18d0eb7c_8df5_40e0_be11_6b0c5f2f3645_
#define _ITUNES_H_18d0eb7c_8df5_40e0_be11_6b0c5f2f3645_

#pragma warning(disable:4091)

#include "ml.h"
#include <Shlobj.h>

#define USE_ITUNES_MOBILE_DEVICE_DLL    0

#if ML_X86

    #if USE_ITUNES_MOBILE_DEVICE_DLL

        #define MOBILE_DEVICE_DLL   L"iTunesMobileDevice.dll"

    #else

        #define MOBILE_DEVICE_DLL   L"MobileDevice.dll"

    #endif

    #define APPLE_APPLICATION_SUPPORT   L"C:\\Program Files (x86)\\Common Files\\Apple\\Apple Application Support"
    #define MOBILE_DEVICE_SUPPORT       L"C:\\Program Files (x86)\\Common Files\\Apple\\Mobile Device Support"

#elif ML_AMD64

    #if USE_ITUNES_MOBILE_DEVICE_DLL

        #define MOBILE_DEVICE_DLL   L"iTunesMobileDevice.dll"

    #else

        #define MOBILE_DEVICE_DLL   L"MobileDevice64.dll"

    #endif

    #define APPLE_APPLICATION_SUPPORT   L"C:\\Program Files\\Common Files\\Apple\\Apple Application Support"
    #define MOBILE_DEVICE_SUPPORT       L"C:\\Program Files\\Common Files\\Apple\\Mobile Device Support"

#endif

#define INIT_STATIC_MEMBER(x) DECL_SELECTANY TYPE_OF(x) x = nullptr
#define LOAD_INTERFACE(_name) *(PVOID *)&_name = GetRoutineAddress(Module, #_name)
#define LOAD_INTERFACE_(_ptr, _name) *(PVOID *)&_ptr = GetRoutineAddress(Module, _name)

#define DECLARE_HANDLE_CHILD(_name, _parent) typedef struct _name##__ : public _parent##__ {} *_name

DECLARE_HANDLE(CFObjectRef);

typedef CFObjectRef CFPropertyListRef;

DECLARE_HANDLE_CHILD(CFRunLoopRef,              CFObjectRef);
DECLARE_HANDLE_CHILD(CFRunLoopSourceRef,        CFObjectRef);

DECLARE_HANDLE_CHILD(CFAllocatorRef,            CFObjectRef);
DECLARE_HANDLE_CHILD(CFNumberRef,               CFObjectRef);
DECLARE_HANDLE_CHILD(CFDataRef,                 CFObjectRef);
DECLARE_HANDLE_CHILD(CFMutableDataRef,          CFDataRef);
DECLARE_HANDLE_CHILD(CFStringRef,               CFObjectRef);
DECLARE_HANDLE_CHILD(CFBooleanRef,              CFObjectRef);
DECLARE_HANDLE_CHILD(CFArrayRef,                CFObjectRef);
DECLARE_HANDLE_CHILD(CFMutableArrayRef,         CFObjectRef);
DECLARE_HANDLE_CHILD(CFDictionaryRef,           CFObjectRef);
DECLARE_HANDLE_CHILD(CFMutableDictionaryRef,    CFDictionaryRef);
DECLARE_HANDLE_CHILD(CFServiceRef,              CFObjectRef);
DECLARE_HANDLE_CHILD(CFErrorRef,                CFObjectRef);

DECLARE_HANDLE_CHILD(AFCConnection,             CFObjectRef);
DECLARE_HANDLE_CHILD(AFCDirectory,              CFObjectRef);
// DECLARE_HANDLE_CHILD(AFCFileRef,                CFObjectRef);

typedef HANDLE64                    AFCFileRef;
typedef HANDLE64                    AFCHandle;

typedef CFDataRef*                  PCFDataRef;
typedef CFStringRef*                PCFStringRef;
typedef CFBooleanRef*               PCFBooleanRef;
typedef CFArrayRef*                 PCFArrayRef;
typedef CFMutableArrayRef*          PCFMutableArray;
typedef CFDictionaryRef*            PCFDictionaryRef;
typedef CFPropertyListRef*          PCFPropertyListRef;
typedef CFServiceRef*               PCFServiceRef;

typedef LONG_PTR                    CFTypeID;
typedef LONG_PTR                    CFIndex;
typedef LONG                        CFStringEncoding;
typedef ULONG                       CFHashCode;

typedef PVOID                       ATH_CONNECTION;

enum CFStringBuiltInEncodings
{
    kCFStringEncodingMacRoman      = 0,
    kCFStringEncodingWindowsLatin1 = 0x0500,
    kCFStringEncodingISOLatin1     = 0x0201,
    kCFStringEncodingNextStepLatin = 0x0B01,
    kCFStringEncodingASCII         = 0x0600,
    kCFStringEncodingUnicode       = 0x0100,
    kCFStringEncodingUTF8          = 0x08000100,
    kCFStringEncodingNonLossyASCII = 0x0BFF,

    kCFStringEncodingUTF16         = 0x0100,
    kCFStringEncodingUTF16BE       = 0x10000100,
    kCFStringEncodingUTF16LE       = 0x14000100,
    kCFStringEncodingUTF32         = 0x0c000100,
    kCFStringEncodingUTF32BE       = 0x18000100,
    kCFStringEncodingUTF32LE       = 0x1c000100,
};

ML_NAMESPACE_BEGIN(iTunesApi);

#include "MobileDevice.h"
#include "AirTrafficHost.h"
#include "CoreFoundation.h"
#include "AppleFileConduit.h"

inline NTSTATUS Initialize()
{
    using ml::String;

    if (AMD::AMDeviceNotificationSubscribe != nullptr)
        return STATUS_SUCCESS;

    WCHAR CommonFiles[MAX_NTPATH];

    SHGetFolderPathW(nullptr, IsWow64Process() ? CSIDL_PROGRAM_FILES_COMMONX86 : CSIDL_PROGRAM_FILES_COMMON, nullptr, SHGFP_TYPE_CURRENT, CommonFiles);

    String path = CommonFiles;

    path += L"\\Apple\\";

    Rtl::EnvironmentAppend(PUSTR(L"Path"), path + L"Apple Application Support");
    Rtl::EnvironmentAppend(PUSTR(L"Path"), path + L"Mobile Device Support");

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

#endif // _ITUNES_H_18d0eb7c_8df5_40e0_be11_6b0c5f2f3645_
