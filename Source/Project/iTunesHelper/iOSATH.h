#ifndef _IOSATH_H_ec5ebc03_fefc_45a0_b243_30b71dfc1411_
#define _IOSATH_H_ec5ebc03_fefc_45a0_b243_30b71dfc1411_

#include "iOSDevice.h"
#include "iOSAFC.h"

class iOSATH
{
public:
    iOSATH(iOSDevice &device);
    ~iOSATH();

    operator ATH_CONNECTION() const
    {
        return this->Connection;
    }

public:
    NTSTATUS Connect();
    NTSTATUS Disconnect();

    ULONG GetGrappaSessionId();

    NTSTATUS SendPowerAssertion(BOOL Enabled);
    NTSTATUS Ping();
    NTSTATUS SendSyncRequest();
    NTSTATUS SendSyncFinished();

protected:
    String GetLibraryID();

    ULONG ReadMessageThread();

    VOID HandleInstalledAssets(CFPropertyList Message);
    VOID HandleSyncAllowed(CFPropertyList Message);
    VOID HandleRequestingSync(CFPropertyList Message);
    VOID HandleReadyForSync(CFPropertyList Message);
    VOID HandleSyncFinished(CFPropertyList Message);
    VOID HandleSyncFailed(CFPropertyList Message);

    static ULONG NTAPI StaticReadMessageThread(PVOID thiz)
    {
        return ((iOSATH *)thiz)->ReadMessageThread();
    }

protected:
    iOSDevice&      device;
    ATH_CONNECTION  Connection;
    CFString        LibraryID;

    HANDLE ReadThreadHandle;
    volatile BOOL Exiting;

public:
    union
    {
        volatile ULONG64 Flags;

        struct
        {
            volatile BOOLEAN SyncAllowed : 1;
            volatile BOOLEAN ReadyForSync : 1;
            volatile BOOLEAN SyncFinished : 1;
            volatile BOOLEAN SyncFailed : 1;
            volatile BOOLEAN ConnectionBroken : 1;
        };
    };
};

#endif // _IOSATH_H_ec5ebc03_fefc_45a0_b243_30b71dfc1411_
