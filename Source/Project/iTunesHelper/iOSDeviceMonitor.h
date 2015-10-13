#ifndef _IOSDEVICEMONITOR_H_cd193acc_3081_4abc_953d_083ddf2b08ac_
#define _IOSDEVICEMONITOR_H_cd193acc_3081_4abc_953d_083ddf2b08ac_

#include "iOS.h"

using namespace iTunesApi::AMD;
using namespace iTunesApi::CF;
using ml::String;

class iOSDeviceMonitor
{
public:
    iOSDeviceMonitor()
    {
        this->Notification = nullptr;
        this->MainThreadId = CurrentTid();
        this->MainThread = TidToHandle(this->MainThreadId);
    }

    ~iOSDeviceMonitor()
    {
        this->NotificationUnsubscribe();
        NtClose(this->MainThread);
    }

    /*++

        notification

    --*/

    NTSTATUS WaitForDeviceConnectionChanged(ULONG Timeout = INFINITE)
    {
        NTSTATUS Status;
        LARGE_INTEGER Interval;

        if (Timeout == 0)
            return NtTestAlert();

        FormatTimeOut(&Interval, Timeout);
        Status = NtDelayExecution(TRUE, &Interval);

        return Status == STATUS_USER_APC ? STATUS_SUCCESS : STATUS_TIMEOUT;
    }

    static ULONG NTAPI USBListenerThread(HANDLE NotificationHandle)
    {
        PNOTIFICATION_OBJECT Object = (PNOTIFICATION_OBJECT)NotificationHandle;

        CFRetain(Object->RunLoopSource);

        CFRunLoopAddSource(CFRunLoopGetCurrent(), Object->RunLoopSource, *kCFRunLoopCommonModes);
        CFRunLoopRun();

        return 0;
    }

    NoInline NTSTATUS NotificationSubscribe(ON_DEVICE_CONNECTION_CHANGED Callback, PVOID Context)
    {
        NTSTATUS Status;

        NotificationUnsubscribe();

        auto cb = [] (PDEVICE_CONNECTION_INFO Info, PVOID UserData) -> VOID
        {
            return ((iOSDeviceMonitor *)UserData)->DeviceConnectionChanged(Info);
        };

        this->NotificationRoutine = Callback;
        this->NotificationContext = Context;

        Status = AMDeviceNotificationSubscribe(cb, 0, 0, this, &this->Notification);
        if (Status != kAMDSuccess)
            return Status;

#if !USE_ITUNES_MOBILE_DEVICE_DLL

        CFRunLoopRemoveSource(CFRunLoopGetCurrent(), ((PNOTIFICATION_OBJECT)this->Notification)->RunLoopSource, *kCFRunLoopCommonModes);

        Status = Ps::CreateThread(USBListenerThread, this->Notification);
        if (NT_FAILED(Status))
            this->NotificationUnsubscribe();

#endif

        return Status;
    }

    NoInline VOID NotificationUnsubscribe()
    {
        if (this->Notification != nullptr)
        {
            AMDeviceNotificationUnsubscribe(this->Notification);
            this->Notification = nullptr;
            this->NotificationRoutine = nullptr;
        }
    }

    VOID DeviceConnectionChanged(PDEVICE_CONNECTION_INFO Info)
    {
        if (this->NotificationRoutine == nullptr)
            return;

        if (CurrentTid() == this->MainThreadId)
        {
            return this->DeviceConnectionChangedApc(Info);
        }

        auto apc = [] (PVOID self, PVOID info, PVOID Context3)
        {
            PDEVICE_CONNECTION_INFO Info = (PDEVICE_CONNECTION_INFO)info;
            ((iOSDeviceMonitor *)self)->DeviceConnectionChangedApc(Info);
            delete Info;
        };

        NTSTATUS Status;
        PDEVICE_CONNECTION_INFO Captured = new DEVICE_CONNECTION_INFO(*Info);

        Status = NtQueueApcThread(this->MainThread, apc, this, Captured, nullptr);
        if (NT_FAILED(Status))
            delete Captured;
    }

    VOID DeviceConnectionChangedApc(PDEVICE_CONNECTION_INFO Info)
    {
        this->NotificationRoutine(Info, this->NotificationContext);
    }

protected:
    ULONG_PTR                       MainThreadId;
    HANDLE                          MainThread;

    PNOTIFICATION_OBJECT            Notification;
    ON_DEVICE_CONNECTION_CHANGED    NotificationRoutine;
    PVOID                           NotificationContext;
};

#endif // _IOSDEVICEMONITOR_H_cd193acc_3081_4abc_953d_083ddf2b08ac_
