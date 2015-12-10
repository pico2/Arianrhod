#ifndef _IOSDEVICE_H_a5ab90f6_e409_4429_87f3_992d1da0d339_
#define _IOSDEVICE_H_a5ab90f6_e409_4429_87f3_992d1da0d339_

#include "iOS.h"

using namespace iTunesApi::AMD;
using namespace iTunesApi::CF;
using ml::String;

class iTunesHelper;

class iOSDevice
{
public:
    iOSDevice(PIOS_DEVICE Device)
    {
        //CFRetain(Device);
        this->Device = Device;
        this->ConnectCount = 0;
        this->SessionCount = 0;
    }

    ~iOSDevice()
    {
        //CFRelease(this->Device);
    }

    operator PIOS_DEVICE()
    {
        return this->Device;
    }

    /*++

        device connection

    --*/

    NoInline NTSTATUS ConnectDevice()
    {
        BOOL        Connected;
        NTSTATUS    Status;

        if (++this->ConnectCount != 1)
            return kAMDSuccess;

        Connected = FALSE;

        LOOP_ONCE
        {
            Status = AMDeviceConnect(this->Device);
            if (Status != kAMDSuccess)
                break;

            Connected = TRUE;

            AMDeviceIsPaired(this->Device);
            if (Status != kAMDSuccess)
                break;

            Status = AMDeviceValidatePairing(this->Device);
            if (Status != kAMDSuccess)
            {
                CFObjectRef ExtendedPairingErrors = CFSTR("ExtendedPairingErrors");
                CFDictionary dict = CFDictionaryCreate(nullptr, &ExtendedPairingErrors, (CFObjectRef *)kCFBooleanTrue, 1, kCFTypeDictionaryKeyCallBacks, kCFTypeDictionaryValueCallBacks);

                Status = AMDevicePairWithOptions(this->Device, dict);

                if (Status != kAMDSuccess)
                    break;

                Status = AMDeviceValidatePairing(this->Device);
            }

            if (Status != kAMDSuccess)
                break;

            Status = StartSession();
            if (Status != kAMDSuccess)
            {
                break;
            }
        }

        if (Status != kAMDSuccess)
        {
            if (Connected != FALSE)
                AMDeviceDisconnect(this->Device);

            --this->ConnectCount;
            DebugLog(L"ConnectDevice failed: %p", Status);
        }

        return Status;
    }

    NoInline NTSTATUS DisconnectDevice()
    {
        if (--this->ConnectCount != 0)
            return kAMDSuccess;

        StopSession();
        AMDeviceDisconnect(this->Device);

        return kAMDSuccess;
    }

    NTSTATUS StartSession()
    {
        if (++this->SessionCount != 1)
        {
            return kAMDSuccess;
        }

        NTSTATUS status = AMDeviceStartSession(*this);
        this->SessionCount = status == kAMDSuccess ? this->SessionCount : 0;
        return status;
    }

    NTSTATUS StopSession()
    {
        if (--this->SessionCount != 0)
        {
            return kAMDSuccess;
        }

        return AMDeviceStopSession(*this);
    }

    /*++

        device info

    --*/

    CFObject GetDeviceValue(PCSTR Key, PCSTR Domain = nullptr)
    {
        iOSDeviceConnector conn(*this);

        if (conn.connected == FALSE)
            return nullptr;

        return AMDeviceCopyValue(this->Device, CFSTR(Domain), CFSTR(Key));
    }

    String GetDeviceValueString(PCSTR Key, PCSTR Domain = nullptr)
    {
        CFObject Value = GetDeviceValue(Key, Domain);
        if (Value == nullptr)
            return L"";

        return Value.ToString();
    }

    NTSTATUS IsJailbroken();

    NTSTATUS IsActivated()
    {
        iOSDeviceConnector conn(*this);

        if (conn.connected == FALSE)
            return conn.status;

        return GetDeviceValueString("ActivationState") == L"Activated" ? kAMDSuccess : kAMDMissingActivationRecordError;
    }

    BOOL IsPasswordProtected()
    {
        return FALSE;
    }

    NTSTATUS Restart();

    NTSTATUS AuthorizeDsids(iTunesHelper* helper, PCSTR SCInfoPath, GrowableArray<ULONG64>& DsidToAuth, GrowableArray<ULONG64>& DsidAuthed);

#define DefineStringPropertyGetter(prop, ...) NoInline String Get##prop() { return GetDeviceValueString(#prop, __VA_ARGS__); }
#define DefineObjectPropertyGetter(prop, ...) NoInline CFObject Get##prop() { return GetDeviceValue(#prop, __VA_ARGS__); }
#define DefineDataPropertyGetter(prop, ...) NoInline CFData Get##prop() { return *(CFData *)&GetDeviceValue(#prop, __VA_ARGS__); }

    DefineStringPropertyGetter(CPUArchitecture);
    DefineStringPropertyGetter(DeviceName);
    DefineStringPropertyGetter(DeviceClass);      // iPhone iPad iPod ...
    DefineStringPropertyGetter(ActivationState);
    DefineStringPropertyGetter(ProductType);
    DefineStringPropertyGetter(DeviceColor);
    DefineStringPropertyGetter(ModelNumber);
    DefineStringPropertyGetter(RegionInfo);
    DefineStringPropertyGetter(SerialNumber);
    DefineStringPropertyGetter(ProductVersion);
    DefineStringPropertyGetter(PhoneNumber);
    DefineStringPropertyGetter(UniqueDeviceID);
    DefineDataPropertyGetter  (UniqueDeviceIDData);
    DefineStringPropertyGetter(BasebandVersion);
    DefineStringPropertyGetter(BasebandBootloaderVersion);
    DefineObjectPropertyGetter(FairPlayCertificate,     "com.apple.mobile.iTunes");
    DefineObjectPropertyGetter(FairPlayDeviceType,      "com.apple.mobile.iTunes");
    DefineStringPropertyGetter(FairPlayGUID,            "com.apple.mobile.iTunes");
    DefineObjectPropertyGetter(KeyTypeSupportVersion,   "com.apple.mobile.iTunes");

protected:
    PIOS_DEVICE Device;
    ULONG_PTR   ConnectCount;
    ULONG_PTR   SessionCount;
};

#endif // _IOSDEVICE_H_a5ab90f6_e409_4429_87f3_992d1da0d339_
