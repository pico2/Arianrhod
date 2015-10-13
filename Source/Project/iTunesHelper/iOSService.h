#ifndef _IOSSERVICE_H_bbc67742_bda2_43ee_aa6d_d64e15255f9a_
#define _IOSSERVICE_H_bbc67742_bda2_43ee_aa6d_d64e15255f9a_

#include "iOSDevice.h"

using namespace iTunesApi::AMD;

class iOSDevice;
class iOSDeviceConnector;

ML_NAMESPACE_BEGIN(iOSServiceOptions)

enum
{
    CloseOnInvalidate   = 1 << 0,
    TimeoutConnection   = 1 << 1,
    UnlockEscrowBag     = 1 << 2,
    DirectSocket        = 1 << 3,
};

ML_NAMESPACE_END_(iOSServiceOptions)

class iOSService
{
public:
    iOSService(iOSDevice& Device) : Device(Device)
    {
    }

    ~iOSService()
    {
        this->Stop();
    }

    iOSService& operator=(const iOSService&) = delete;

    operator SOCKET()
    {
        return AMDServiceConnectionGetSocket(this->Service);
    }

    NTSTATUS Start(PCSTR ServiceName, ULONG_PTR Options = iOSServiceOptions::CloseOnInvalidate)
    {
        return Start(CFSTR(ServiceName));
    }

    NTSTATUS Start(const CFStringRef& ServiceName, ULONG_PTR OptionsFlags = iOSServiceOptions::CloseOnInvalidate)
    {
        NTSTATUS Status;
        CFServiceRef Service;

        iOSDeviceConnector conn(this->Device);

        if (conn.connected == FALSE)
            return conn.status;

        CFDict Options;

        if (FLAG_ON(OptionsFlags, iOSServiceOptions::CloseOnInvalidate))
            Options.SetValue(CFSTR("CloseOnInvalidate"), *kCFBooleanTrue);

        if (FLAG_ON(OptionsFlags, iOSServiceOptions::UnlockEscrowBag))
            Options.SetValue(CFSTR("UnlockEscrowBag"), *kCFBooleanTrue);

        if (FLAG_ON(OptionsFlags, iOSServiceOptions::TimeoutConnection))
            Options.SetValue(CFSTR("TimeoutConnection"), *kCFBooleanTrue);

        if (FLAG_ON(OptionsFlags, iOSServiceOptions::DirectSocket))
            Options.SetValue(CFSTR("DirectSocket"), *kCFBooleanTrue);

        Status = AMDeviceSecureStartService(this->Device, ServiceName, Options, &Service);
        if (Status != kAMDSuccess)
            return Status;

        this->Service = Service;
        return Status;
    }

    VOID Stop()
    {
        if (this->Service != nullptr)
        {
            AMDServiceConnectionInvalidate(this->Service);
            this->Service.~CFService();
        }
    }

    ULONG_PTR SendMessage(const CFDict& Message)
    {
        CFData data = Message.ToData();
        return SendMessage(data);
    }

    ULONG_PTR SendMessage(const CFList& Message)
    {
        CFData data = Message.ToData();
        return SendMessage(data);
    }

    ULONG_PTR SendMessage(const CFPropertyList& Message)
    {
        CFData data = CFObjectToBinaryData(Message);
        return SendMessage(data);
    }

    ULONG_PTR SendMessage(CFDataRef Message)
    {
        return SendMessage(CFDataGetBytePtr(Message), CFDataGetLength(Message));
    }

    NoInline ULONG_PTR SendMessage(PVOID Buffer, ULONG_PTR Size)
    {
        LONG BytesSent;
        ULONG_PTR SizeTotal;

        BytesSent = Bswap((LONG)Size);
        BytesSent = AMDServiceConnectionSend(this->Service, &BytesSent, 4);
        if (BytesSent != 4)
            return ~0u;

        return this->SendRawData(Buffer, Size);
    }

    NoInline ULONG_PTR SendRawData(PVOID Buffer, ULONG_PTR Size)
    {
        LONG BytesSent;
        ULONG_PTR SizeTotal;

        SizeTotal = Size;

        while (Size != 0)
        {
            BytesSent = AMDServiceConnectionSend(this->Service, Buffer, Size);
            if (BytesSent == -1 || BytesSent == 0)
                break;

            Size -= BytesSent;
            Buffer = PtrAdd(Buffer, BytesSent);
        }

        return SizeTotal;
    }

    NoInline CFPropertyListRef ReceiveMessage()
    {
        LONG MessageLength, ret;
        CFPropertyListRef xml;
        CFMutableDataRef data;

        ret = ReceiveRawMessage(&MessageLength, sizeof(MessageLength));
        if (ret != sizeof(MessageLength))
            return nullptr;

        MessageLength = Bswap(MessageLength);

        data = CFDataCreateMutable(nullptr, MessageLength);
        if (data == nullptr)
            return nullptr;

        BYTE Buffer[0x1000];

        while (MessageLength != 0)
        {
            ret = ReceiveRawMessage(Buffer, ML_MIN(MessageLength, sizeof(Buffer)));
            if (ret == 0 || ret == -1)
                break;

            MessageLength -= ret;
            CFDataAppendBytes(data, Buffer, ret);
        }

        xml = CFPropertyListCreateFromXMLData(nullptr, data, kCFPropertyListImmutable, nullptr);
        CFRelease(data);

        return xml;
    }

    ULONG_PTR ReceiveRawMessage(PVOID Buffer, ULONG_PTR Size)
    {
        return AMDServiceConnectionReceive(this->Service, Buffer, Size);
    }

protected:
    iOSDevice&  Device;
    CFService   Service;
};

#endif // _IOSSERVICE_H_bbc67742_bda2_43ee_aa6d_d64e15255f9a_
