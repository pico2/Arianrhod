ML_NAMESPACE_BEGIN(CF);

typedef ULONG CFOptionFlags;

// run loop

enum
{
    kCFRunLoopRunFinished      = 1,
    kCFRunLoopRunStopped       = 2,
    kCFRunLoopRunTimedOut      = 3,
    kCFRunLoopRunHandledSource = 4,
};

DECL_SELECTANY
VOID
(CDECL
*CFRunLoopRun)(
    VOID
);

DECL_SELECTANY
VOID
(CDECL
*CFRunLoopRunInMode)(
    CFStringRef Mode,
    DOUBLE      Seconds,
    BOOL        ReturnAfterSourceHandled
);

DECL_SELECTANY
CFRunLoopRef
(CDECL
*CFRunLoopGetCurrent)(
    VOID
);

DECL_SELECTANY
VOID
(CDECL
*CFRunLoopSourceInvalidate)(
    CFRunLoopSourceRef RunLoopSource
);

DECL_SELECTANY
VOID
(CDECL
*CFRunLoopAddSource)(
    CFRunLoopRef        RunLoop,
    CFRunLoopSourceRef  LoopSource,
    CFStringRef         RunLoopMode
);

DECL_SELECTANY
VOID
(CDECL
*CFRunLoopRemoveSource)(
    CFRunLoopRef        RunLoop,
    CFRunLoopSourceRef  LoopSource,
    CFStringRef         RunLoopMode
);

// type

DECL_SELECTANY CFTypeID (CDECL *CFGetTypeID)(CFObjectRef Object);
DECL_SELECTANY CFTypeID (CDECL *CFStringGetTypeID)();
DECL_SELECTANY CFTypeID (CDECL *CFDictionaryGetTypeID)();
DECL_SELECTANY CFTypeID (CDECL *CFArrayGetTypeID)();
DECL_SELECTANY CFTypeID (CDECL *CFNumberGetTypeID)();
DECL_SELECTANY CFTypeID (CDECL *CFDataGetTypeID)();
DECL_SELECTANY CFTypeID (CDECL *CFBooleanGetTypeID)();

// number

enum
{
    kCFNumberSInt8Type     = 1,
    kCFNumberSInt16Type    = 2,
    kCFNumberSInt32Type    = 3,
    kCFNumberSInt64Type    = 4,
    kCFNumberFloat32Type   = 5,
    kCFNumberFloat64Type   = 6,
    kCFNumberCharType      = 7,
    kCFNumberShortType     = 8,
    kCFNumberIntType       = 9,
    kCFNumberLongType      = 10,
    kCFNumberLongLongType  = 11,
    kCFNumberFloatType     = 12,
    kCFNumberDoubleType    = 13,
    kCFNumberCFIndexType   = 14,
    kCFNumberNSIntegerType = 15,
    kCFNumberCGFloatType   = 16,
    kCFNumberMaxType       = 16,
};

typedef ULONG CFNumberType;

DECL_SELECTANY
CFNumberRef
(CDECL
*CFNumberCreate)(
    CFAllocatorRef      Allocator,
    CFNumberType        Type,
    PVOID               ValuePtr
);

DECL_SELECTANY
CFIndex
(CDECL
*CFNumberGetByteSize)(
    CFNumberRef Number
);

DECL_SELECTANY
CFNumberType
(CDECL
*CFNumberGetType)(
    CFNumberRef Number
);

DECL_SELECTANY
BOOLEAN
(CDECL
*CFNumberGetValue)(
    CFNumberRef     Number,
    CFNumberType    Type,
    PVOID           ValuePtr
);

// data

DECL_SELECTANY
CFDataRef
(CDECL
*CFDataCreate)(
    CFAllocatorRef  Allocator,
    PVOID           Buffer,
    ULONG           Size
);

DECL_SELECTANY
CFMutableDataRef
(CDECL
*CFDataCreateMutable)(
    CFAllocatorRef  Allocator,
    CFIndex         Capacity
);

DECL_SELECTANY
VOID
(CDECL
*CFDataAppendBytes)(
    CFMutableDataRef    Data,
    PBYTE               Buffer,
    CFIndex             Length
);


DECL_SELECTANY CFIndex  (CDECL *CFDataGetLength)(CFDataRef Data);
DECL_SELECTANY PBYTE    (CDECL *CFDataGetBytePtr)(CFDataRef Data);

// property list

enum
{
   kCFPropertyListOpenStepFormat    = 1,
   kCFPropertyListXMLFormat_v1_0    = 100,
   kCFPropertyListBinaryFormat_v1_0 = 200,
};

enum CFPropertyListMutabilityOptions
{
    kCFPropertyListImmutable                  = 0,
    kCFPropertyListMutableContainers          = 1,
    kCFPropertyListMutableContainersAndLeaves = 2,
};

typedef ULONG CFPropertyListFormat;

DECL_SELECTANY
CFDataRef
(CDECL
*CFPropertyListCreateXMLData)(
    CFAllocatorRef      Allocator,
    CFPropertyListRef   PropertyList
);

DECL_SELECTANY
CFDataRef
(CDECL
*CFPropertyListCreateData)(
    CFAllocatorRef          Allocator,
    CFPropertyListRef       PropertyList,
    CFPropertyListFormat    Format,
    CFOptionFlags           Options,
    CFErrorRef*             Error
);

DECL_SELECTANY
CFPropertyListRef
(CDECL
*CFPropertyListCreateFromXMLData)(
    CFAllocatorRef  Allocator,
    CFDataRef       XmlData,
    CFOptionFlags   MutabilityOption,
    CFStringRef*    ErrorString
);

DECL_SELECTANY
CFPropertyListRef
(CDECL
*CFPropertyListCreateWithData)(
    CFAllocatorRef          Allocator,
    CFDataRef               XmlData,
    CFOptionFlags           Options,
    CFPropertyListFormat*   Format,
    CFErrorRef*             Error
);


// dict

typedef const void* (CDECL *CFDictionaryRetainCallBack) ( CFAllocatorRef allocator, const void *value );
typedef void (CDECL *CFDictionaryReleaseCallBack) ( CFAllocatorRef allocator, const void *value );
typedef CFStringRef (CDECL *CFDictionaryCopyDescriptionCallBack)( const void *value );
typedef BOOLEAN (CDECL *CFDictionaryEqualCallBack) ( const void *value1, const void *value2 );
typedef CFHashCode (CDECL *CFDictionaryHashCallBack) ( const void *value );

struct CFDictionaryKeyCallBacks
{
    CFIndex                             version;
    CFDictionaryRetainCallBack          retain;
    CFDictionaryReleaseCallBack         release;
    CFDictionaryCopyDescriptionCallBack copyDescription;
    CFDictionaryEqualCallBack           equal;
    CFDictionaryHashCallBack            hash;
};

struct CFDictionaryValueCallBacks
{
    CFIndex                             version;
    CFDictionaryRetainCallBack          retain;
    CFDictionaryReleaseCallBack         release;
    CFDictionaryCopyDescriptionCallBack copyDescription;
    CFDictionaryEqualCallBack           equal;
};


DECL_SELECTANY CFDictionaryKeyCallBacks*    kCFCopyStringDictionaryKeyCallBacks;
DECL_SELECTANY CFDictionaryKeyCallBacks*    kCFTypeDictionaryKeyCallBacks;
DECL_SELECTANY CFDictionaryValueCallBacks*  kCFTypeDictionaryValueCallBacks;

DECL_SELECTANY
CFDictionaryRef
(CDECL
*CFDictionaryCreate)(
    CFAllocatorRef              Allocator,
    CFObjectRef*                Keys,
    CFObjectRef*                Values,
    CFIndex                     NumberofValues,
    CFDictionaryKeyCallBacks*   KeyCallBacks,
    CFDictionaryValueCallBacks* ValueCallBacks
);

DECL_SELECTANY
CFMutableDictionaryRef
(CDECL
*CFDictionaryCreateMutable)(
    CFAllocatorRef  Allocator,
    CFIndex         Capacity,
    PVOID           KeyCallBacks,
    PVOID           ValueCallBacks
);

DECL_SELECTANY
VOID
(CDECL
*CFDictionaryAddValue)(
    CFMutableDictionaryRef  Dict,
    CFObjectRef             Key,
    CFObjectRef             Value
);

DECL_SELECTANY
VOID
(CDECL
*CFDictionarySetValue)(
    CFMutableDictionaryRef  Dict,
    CFObjectRef             Key,
    CFObjectRef             Value
);

DECL_SELECTANY
PVOID
(CDECL
*CFDictionaryGetValue)(
    CFDictionaryRef Dict,
    PVOID           Key
); 

// array

typedef const void *(CDECL *CFArrayRetainCallBack) ( CFAllocatorRef allocator, const void *value );
typedef void (CDECL *CFArrayReleaseCallBack) ( CFAllocatorRef allocator, const void *value );
typedef CFStringRef (CDECL *CFArrayCopyDescriptionCallBack) ( const void *value );
typedef BOOLEAN (CDECL *CFArrayEqualCallBack)(PVOID value1, PVOID value2);

struct CFArrayCallBacks
{
    CFIndex                         version;
    CFArrayRetainCallBack           retain;
    CFArrayReleaseCallBack          release;
    CFArrayCopyDescriptionCallBack  copyDescription;
    CFArrayEqualCallBack            equal;
};

DECL_SELECTANY CFArrayCallBacks*    kCFTypeArrayCallBacks;

DECL_SELECTANY
CFArrayRef
(CDECL
*CFArrayCreate)(
    CFAllocatorRef          Allocator,
    PVOID*                  Values,
    CFIndex                 NumberOfValues,
    CFArrayCallBacks*       Callbacks
);

DECL_SELECTANY
CFMutableArrayRef
(CDECL
*CFArrayCreateMutable)(
    CFAllocatorRef          Allocator,
    CFIndex                 Capacity,
    CFArrayCallBacks*       Callbacks
);

DECL_SELECTANY
CFIndex
(CDECL
*CFArrayGetCount)(
    CFArrayRef Array
);

DECL_SELECTANY
PVOID
(CDECL
*CFArrayGetValueAtIndex)(
    CFArrayRef  Array,
    CFIndex     Index
);

DECL_SELECTANY
VOID
(CDECL
*CFArrayAppendValue)(
    CFMutableArrayRef   Array,
    PVOID               Value
);

DECL_SELECTANY
VOID
(CDECL
*CFArrayInsertValueAtIndex)(
    CFMutableArrayRef   Array,
    CFIndex             Index,
    PVOID               Value
);

DECL_SELECTANY
VOID
(CDECL
*CFArrayRemoveAllValues)(
    CFMutableArrayRef Array
);

DECL_SELECTANY
VOID
(CDECL
*CFArrayRemoveValueAtIndex)(
    CFMutableArrayRef   Array,
    CFIndex             Index
);

DECL_SELECTANY
VOID
(CDECL
*CFArraySetValueAtIndex)(
    CFMutableArrayRef   Array,
    CFIndex             Index,
    PVOID               Value
);


// string

DECL_SELECTANY
CFStringRef
(CDECL
*CFStringCreateWithCString)(
    CFAllocatorRef      Allocator,
    PCSTR               String,
    CFStringEncoding    Encoding
);

template<class T>
inline CFStringRef CFSTR(T s)
{
    return (s) ? iTunesApi::CF::CFStringMakeConstantString(s) : nullptr;
}

// #define CFSTR(s) ((s) ? iTunesApi::CF::CFStringMakeConstantString(s) : nullptr)

DECL_SELECTANY CFStringRef (CDECL *CFStringMakeConstantString)(PCSTR String);
DECL_SELECTANY CFIndex  (CDECL *CFStringGetLength)(CFStringRef String);

DECL_SELECTANY
BOOL
(CDECL
*CFStringGetCString)(
    CFStringRef         String,
    PVOID               Buffer,
    CFIndex             BufferSize,
    CFStringEncoding    Encoding
);

DECL_SELECTANY
PVOID
(CDECL
*CFStringGetCStringPtr)(
    CFStringRef         String,
    CFStringEncoding    Encoding
);

enum
{
    kCFCompareCaseInsensitive      = 1,
    kCFCompareBackwards            = 4,
    kCFCompareAnchored             = 8,
    kCFCompareNonliteral           = 16,
    kCFCompareLocalized            = 32,
    kCFCompareNumerically          = 64,
    kCFCompareDiacriticInsensitive = 128,
    kCFCompareWidthInsensitive     = 256,
    kCFCompareForcedOrdering       = 512,
};

typedef CFOptionFlags CFStringCompareFlags;

enum CFComparisonResult
{
    kCFCompareLessThan    = -1,
    kCFCompareEqualTo     = 0,
    kCFCompareGreaterThan = 1,
};

DECL_SELECTANY
CFComparisonResult
(CDECL
*CFStringCompare)(
    CFStringRef             String1,
    CFStringRef             String2,
    CFStringCompareFlags    CompareOptions
);

// object

DECL_SELECTANY VOID (CDECL *CFRetain)(CFObjectRef Object);
DECL_SELECTANY VOID (CDECL *CFRelease)(CFObjectRef Object);
DECL_SELECTANY BOOLEAN (CDECL *CFEqual)(CFObjectRef Object1, CFObjectRef Object2);


// boolean

DECL_SELECTANY PCFBooleanRef    kCFBooleanTrue;
DECL_SELECTANY PCFBooleanRef    kCFBooleanFalse;
DECL_SELECTANY CFStringRef*     kCFRunLoopDefaultMode;
DECL_SELECTANY CFStringRef*     kCFRunLoopCommonModes;

DECL_SELECTANY BOOLEAN (CDECL *CFBooleanGetValue)(CFObjectRef Object);

inline NTSTATUS Initialize()
{
    PVOID Module = LoadDll(L"CoreFoundation.dll");

    LOAD_INTERFACE(CFRunLoopRun);
    LOAD_INTERFACE(CFRunLoopRunInMode);
    LOAD_INTERFACE(CFRunLoopGetCurrent);
    LOAD_INTERFACE(CFRunLoopSourceInvalidate);
    LOAD_INTERFACE(CFRunLoopAddSource);
    LOAD_INTERFACE(CFRunLoopRemoveSource);

    LOAD_INTERFACE(CFPropertyListCreateXMLData);
    LOAD_INTERFACE(CFPropertyListCreateData);
    LOAD_INTERFACE(CFPropertyListCreateFromXMLData);
    LOAD_INTERFACE(CFPropertyListCreateWithData);

    LOAD_INTERFACE(CFGetTypeID);
    LOAD_INTERFACE(CFStringGetTypeID);
    LOAD_INTERFACE(CFDictionaryGetTypeID);
    LOAD_INTERFACE(CFArrayGetTypeID);
    LOAD_INTERFACE(CFNumberGetTypeID);
    LOAD_INTERFACE(CFDataGetTypeID);
    LOAD_INTERFACE(CFBooleanGetTypeID);

    LOAD_INTERFACE(CFNumberCreate);
    LOAD_INTERFACE(CFNumberGetByteSize);
    LOAD_INTERFACE(CFNumberGetType);
    LOAD_INTERFACE(CFNumberGetValue);

    LOAD_INTERFACE(CFDataCreate);
    LOAD_INTERFACE(CFDataCreateMutable);
    LOAD_INTERFACE(CFDataAppendBytes);
    LOAD_INTERFACE(CFDataGetLength);
    LOAD_INTERFACE(CFDataGetBytePtr);

    LOAD_INTERFACE(kCFCopyStringDictionaryKeyCallBacks);
    LOAD_INTERFACE(kCFTypeDictionaryKeyCallBacks);
    LOAD_INTERFACE(kCFTypeDictionaryValueCallBacks);
    LOAD_INTERFACE(CFDictionaryCreate);
    LOAD_INTERFACE(CFDictionaryCreateMutable);
    LOAD_INTERFACE(CFDictionaryAddValue);
    LOAD_INTERFACE(CFDictionarySetValue);
    LOAD_INTERFACE(CFDictionaryGetValue);

    LOAD_INTERFACE(kCFTypeArrayCallBacks);
    LOAD_INTERFACE(CFArrayCreate);
    LOAD_INTERFACE(CFArrayCreateMutable);
    LOAD_INTERFACE(CFArrayGetCount);
    LOAD_INTERFACE(CFArrayGetValueAtIndex);
    LOAD_INTERFACE(CFArrayAppendValue);
    LOAD_INTERFACE(CFArrayInsertValueAtIndex);
    LOAD_INTERFACE(CFArrayRemoveAllValues);
    LOAD_INTERFACE(CFArrayRemoveValueAtIndex);
    LOAD_INTERFACE(CFArraySetValueAtIndex);

    LOAD_INTERFACE(CFStringCreateWithCString);
    LOAD_INTERFACE_(CFStringMakeConstantString, "__CFStringMakeConstantString");
    LOAD_INTERFACE(CFStringGetCString);
    LOAD_INTERFACE(CFStringGetCStringPtr);
    LOAD_INTERFACE(CFStringCompare);
    LOAD_INTERFACE(CFStringGetLength);

    LOAD_INTERFACE(CFRetain);
    LOAD_INTERFACE(CFRelease);
    LOAD_INTERFACE(CFEqual);

    LOAD_INTERFACE(kCFBooleanTrue);
    LOAD_INTERFACE(kCFBooleanFalse);
    LOAD_INTERFACE(CFBooleanGetValue);

    LOAD_INTERFACE(kCFRunLoopDefaultMode);
    LOAD_INTERFACE(kCFRunLoopCommonModes);

    return STATUS_SUCCESS;
}

ML_NAMESPACE_END_(CF);
