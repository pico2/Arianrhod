#include "stdafx.h"
#include "iOS.h"
#include "iOSDevice.h"

using namespace iTunesApi::CF;
using ml::String;

//
// iOSDeviceConnector
//

iOSDeviceConnector::iOSDeviceConnector(iOSDevice& device) : device(device)
{
    status = device.ConnectDevice();
    connected = status == kAMDSuccess;
}

iOSDeviceConnector::~iOSDeviceConnector()
{
    if (connected != FALSE)
        this->device.DisconnectDevice();
}


//
//
//

CFDataRef CFObjectToBinaryData(const CFObjectRef object)
{
    return CFPropertyListCreateData(
                nullptr,
                object,
                kCFPropertyListBinaryFormat_v1_0,
                0,
                nullptr
            );
}

//
// CFDict
//

CFDict::CFDict() : dict(CFDictionaryCreateMutable(nullptr, 0, kCFTypeDictionaryKeyCallBacks, kCFTypeDictionaryValueCallBacks))
{
    ;
}

CFDict::~CFDict()
{
    ;
}

VOID CFDict::SetValue(const String& Key, const String& Value)
{
    CFDictionarySetValue(this->dict, CFSTR(Key.Encode(CP_UTF8)), CFSTR(Value.Encode(CP_UTF8)));
}

VOID CFDict::SetValue(const ml::String& Key, CFObjectRef Value)
{
    CFDictionarySetValue(this->dict, CFSTR(Key.Encode(CP_UTF8)), Value);
}

VOID CFDict::SetValue(CFObjectRef Key, CFObjectRef Value)
{
    CFDictionarySetValue(this->dict, Key, Value);
}

CFDataRef CFDict::ToData() const
{
    return CFObjectToBinaryData(*this);
}


//
// CFList
//

CFList::CFList() : array(CFArrayCreateMutable(nullptr, 0, kCFTypeArrayCallBacks))
{
}

CFList::~CFList()
{
    ;
}

VOID CFList::Clear()
{
    CFArrayRemoveAllValues(*this);
}

CFList& CFList::operator<<(INT32 value)
{
    AppendValue(CFObject(CFNumberCreate(nullptr, kCFNumberSInt32Type, &value)));
    return *this;
}

CFList& CFList::operator<<(INT64 value)
{
    AppendValue(CFObject(CFNumberCreate(nullptr, kCFNumberSInt64Type, &value)));
    return *this;
}

CFList& CFList::operator<<(LONG value)
{
    AppendValue(CFObject(CFNumberCreate(nullptr, kCFNumberLongType, &value)));
    return *this;
}

CFList& CFList::operator<<(PCSTR value)
{
    AppendValue(CFSTR(value));
    return *this;
}

CFList& CFList::operator<<(const ml::String& value)
{
    AppendValue(CFSTR(value.Encode(CP_UTF8)));
    return *this;
}

CFList& CFList::operator<<(CFObjectRef object)
{
    AppendValue(object);
    return *this;
}

CFDataRef CFList::ToData() const
{
    return CFObjectToBinaryData(*this);
}
