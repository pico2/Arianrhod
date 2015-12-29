#ifndef _IOS_H_651f444c_14a4_4602_81a3_03a3237daa65_
#define _IOS_H_651f444c_14a4_4602_81a3_03a3237daa65_

#include "iTunes/iTunes.h"

using ml::ByteArray;
using ml::String;

#if 1
    #define DebugLog(...) (PrintConsole(L"[%S:%d] ", __FUNCTION__, __LINE__), PrintConsole(__VA_ARGS__), PrintConsole(L"\n"))
#else
    #define DebugLog(...)
#endif

using namespace iTunesApi::CF;

CFDataRef CFObjectToBinaryData(const CFObjectRef object);

class CFObjectBase
{
    ;
};

template<class T>
class CFObjectT : public CFObjectBase
{
public:
    CFObjectT(T object = nullptr)
    {
        this->object = object;
    }

    ~CFObjectT()
    {
        if (this->object != nullptr)
        {
            iTunesApi::CF::CFRelease(this->object);
            this->object = nullptr;
        }
    }

    CFObjectT(const CFObjectT& that)
    {
        this->object = that.object;
        if (object != nullptr)
            CFRetain(object);
    }

    operator T() const
    {
        return this->object;
    }

    CFObjectT& operator=(T object)
    {
        this->~CFObjectT();
        this->object = object;
        return *this;
    }

    CFObjectT& operator=(const CFObjectT& that)
    {
        this->~CFObjectT();
        this->object = that.object;
        CFRetain(this->object);
        return *this;
    }

    CFTypeID GetTypeID()
    {
        return CFGetTypeID(object);
    }

    static PVOID GetTypeFromTypeId(CFTypeID id)
    {
        static PCSTR TypeIdRoutines[] =
        {
            "CFMessagePortGetTypeID",
            "CFDateFormatterGetTypeID",
            "CFTimeZoneGetTypeID",
            "CFAttributedStringGetTypeID",
            "CFArrayGetTypeID",
            "CFAllocatorGetTypeID",
            "CFNumberGetTypeID",
            "CFNullGetTypeID",
            "CFRunLoopSourceGetTypeID",
            "CFNotificationCenterGetTypeID",
            "CFPlugInInstanceGetTypeID",
            "CFRunLoopGetTypeID",
            "CFURLGetTypeID",
            "CFWriteStreamGetTypeID",
            "CFUUIDGetTypeID",
            "CFBooleanGetTypeID",
            "CFTreeGetTypeID",
            "CFXMLParserGetTypeID",
            "CFURLEnumeratorGetTypeID",
            "CFRunLoopTimerGetTypeID",
            "CFRunArrayGetTypeID",
            "CFRunLoopObserverGetTypeID",
            "CFBinaryHeapGetTypeID",
            "CFSocketGetTypeID",
            "CFDataGetTypeID",
            "CFDateGetTypeID",
            "CFNumberFormatterGetTypeID",
            "CFPlugInGetTypeID",
            "CFSetGetTypeID",
            "CFReadStreamGetTypeID",
            "CFStorageGetTypeID",
            "_CFKeyedArchiverUIDGetTypeID",
            "CFWindowsNamedPipeGetTypeID",
            "CFStringGetTypeID",
            "CFErrorGetTypeID",
            "CFCharacterSetGetTypeID",
            "CFTypeGetTypeID",
            "CFBitVectorGetTypeID",
            "CFCalendarGetTypeID",
            "CFDictionaryGetTypeID",
            "CFXMLNodeGetTypeID",
            "CFBundleGetTypeID",
            "CFBagGetTypeID",
            "CFLocaleGetTypeID",
        };

        TYPE_OF(CFStringGetTypeID) GetTypeID;
        PVOID Base = FindLdrModuleByName(PUSTR(L"CoreFoundation.dll"))->DllBase;

        for (int i = 0; i != countof(TypeIdRoutines); ++i)
        {
            *(PVOID *)&GetTypeID = GetRoutineAddress(Base, TypeIdRoutines[i]);
            if (GetTypeID() == id)
                return GetTypeID;
        }

        return nullptr;
    }

    String ToString()
    {
        CFTypeID TypeId = GetTypeID();

        if (TypeId == CFStringGetTypeID())
        {
            return ((CFString *)this)->ToString();
        }
        else if (TypeId == CFBooleanGetTypeID())
        {
            return ((CFBoolean *)this)->ToString();
        }
        else if (TypeId == CFNumberGetTypeID())
        {
            return ((CFNumber *)this)->ToString();
        }
        else if (TypeId == CFDataGetTypeID())
        {
            return ((CFData *)this)->ToString();
        }

        return L"<UNKNOWN TYPE>";
    }

    ULONG64 ToULong64()
    {
        ULONG64 v = 0;
        CFNumberGetValue((CFNumberRef)object, kCFNumberLongLongType, &v);
        return v;
    }

protected:
    T object;
};

/*++

    string

--*/

inline String CFObjectT<CFStringRef>::ToString()
{
    CFIndex Length;
    PWSTR   Buffer;

    Length = iTunesApi::CF::CFStringGetLength(*this) + 1;
    Length *= sizeof(*Buffer);
    Buffer = (PWSTR)AllocStack(Length);
    iTunesApi::CF::CFStringGetCString(*this, Buffer, Length, kCFStringEncodingUTF16LE);

    Buffer[(Length - 1) / sizeof(*Buffer)] = 0;

    return String(Buffer);
}

/*++

    boolean

--*/

inline String CFObjectT<CFBooleanRef>::ToString()
{
    return CFBooleanGetValue(*this) ? L"True" : L"False";
}

/*++

    number

--*/

inline String CFObjectT<CFNumberRef>::ToString()
{
    WCHAR buffer[100];
    ULONG64 value = 0;
    float   fvalue = 0.0;
    double  dvalue = 0.0;

    CFNumberType type = CFNumberGetType((CFNumberRef)this->object);

    switch (type)
    {
        case kCFNumberSInt8Type:
        case kCFNumberSInt16Type:
        case kCFNumberSInt32Type:
        case kCFNumberSInt64Type:
            CFNumberGetValue((CFNumberRef)this->object, type, &value);
            swprintf(buffer, L"%I64d", value);
            break;

        case kCFNumberFloat32Type:
        case kCFNumberFloatType:
            CFNumberGetValue((CFNumberRef)this->object, type, &fvalue);
            swprintf(buffer, L"%lf", fvalue);
            break;

        case kCFNumberFloat64Type:
        case kCFNumberDoubleType:
            CFNumberGetValue((CFNumberRef)this->object, type, &dvalue);
            swprintf(buffer, L"%lf", dvalue);
            break;

        case kCFNumberCharType:
        case kCFNumberShortType:
        case kCFNumberIntType:
        case kCFNumberLongType:
        case kCFNumberLongLongType:
        case kCFNumberCFIndexType:
            CFNumberGetValue((CFNumberRef)this->object, type, &value);
            swprintf(buffer, L"%I64u", value);
            break;
    }

    return String(buffer);
}

/*++

    object

--*/

inline String CFObjectT<CFDataRef>::ToString()
{
    String ret;
    CFIndex Length = CFDataGetLength(*this);
    PBYTE Buffer = CFDataGetBytePtr(*this);

    for (; Length; ++Buffer, --Length)
    {
        ret += String::Format(L"%02X ", Buffer[0]);
    }

    return ret.Strip();
}

typedef CFObjectT<CFObjectRef>              CFObject;
typedef CFObjectT<CFDataRef>                CFData;
typedef CFObjectT<CFMutableDataRef>         CFMutableData;
typedef CFObjectT<CFNumberRef>              CFNumber;
typedef CFObjectT<CFStringRef>              CFString;
typedef CFObjectT<CFBooleanRef>             CFBoolean;
typedef CFObjectT<CFServiceRef>             CFService;
typedef CFObjectT<CFArrayRef>               CFArray;
typedef CFObjectT<CFMutableArrayRef>        CFMutableArray;
typedef CFObjectT<CFDictionaryRef>          CFDictionary;
typedef CFObjectT<CFMutableDictionaryRef>   CFMutableDictionary;
typedef CFObjectT<CFPropertyListRef>        CFPropertyList;


class iOSDevice;

class iOSDeviceConnector
{
public:
    iOSDeviceConnector(iOSDevice& device);
    ~iOSDeviceConnector();

    iOSDeviceConnector& operator=(const iOSDeviceConnector&) = delete;

public:
    BOOL connected;
    NTSTATUS status;

protected:
    iOSDevice& device;
};

class CFDict
{
public:
    CFDict();
    ~CFDict();

    CFDict(const CFDict&) = delete;

    operator CFDictionaryRef() const
    {
        return (CFDictionaryRef)this->dict;
    }

    operator CFMutableDictionaryRef() const
    {
        return (CFMutableDictionaryRef)this->dict;
    }

    operator CFPropertyListRef() const
    {
        return (CFPropertyListRef)(CFDictionaryRef)this->dict;
    }

    VOID SetValue(const String& Key, const String& Value);
    VOID SetValue(const String& Key, CFObjectRef Value);
    VOID SetValue(CFObjectRef Key, CFObjectRef Value);

    CFDataRef ToData() const;

protected:
    CFMutableDictionary dict;
};

class CFList
{
public:
    CFList();
    ~CFList();

    VOID Clear();

    CFList& operator<<(INT32 value);
    CFList& operator<<(INT64 value);
    CFList& operator<<(PCSTR value);
    CFList& operator<<(const String& value);
    CFList& operator<<(LONG value);
    CFList& operator<<(CFObjectRef object);

    CFDataRef ToData() const;

    operator CFObjectRef() const
    {
        return (CFObjectRef)this->array;
    }

    operator CFArrayRef() const
    {
        return (CFArrayRef)(CFMutableArrayRef)this->array;
    }

    operator CFMutableArrayRef() const
    {
        return (CFMutableArrayRef)this->array;
    }

    VOID AppendValue(CFObjectRef object)
    {
        iTunesApi::CF::CFArrayAppendValue(this->array, object);
    }

protected:
    CFMutableArray array;
};

#endif // _IOS_H_651f444c_14a4_4602_81a3_03a3237daa65_
