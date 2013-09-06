#ifndef _OD_H_5bacdc5e_0bc6_44b1_b606_84e1831e76c7_
#define _OD_H_5bacdc5e_0bc6_44b1_b606_84e1831e76c7_

#include "MyLibraryUser.h"
#include "Plugin.h"
#include "HookPort.h"
#include "../../Drivers/AntiAntiKernelDebug/ShadowSysCall.h"

#define SUPER_ANTI_DEBUG_KEY    "SuperAntiDebug"
#define ULTRA_ANTI_DEBUG_KEY    "UltraAntiDebug"

typedef struct
{
    BOOL        Enabled;
    NtFileDisk  Device;
    NtFileDisk  Log;

} SHADOW_SYSTEM_CALL_DEVICE, *PSHADOW_SYSTEM_CALL_DEVICE;

typedef struct OD_HOOK_INFO
{
    struct
    {
        BOOLEAN DriverLoaded    : 1;
    };

    HANDLE MainThreadId;
    ULONG_PTR ThemesPid;

    SHADOW_SYSTEM_CALL_DEVICE SsDevice;

    ANSI_STRING SystemDirectoryWow64;
    ANSI_STRING SystemDirectory64;

    OD_HOOK_INFO()
    {
        ZeroMemory(this, sizeof(*this));
    }

    ~OD_HOOK_INFO()
    {
        RtlFreeAnsiString(&SystemDirectoryWow64);
        RtlFreeAnsiString(&SystemDirectory64);
    }

} OD_HOOK_INFO, *POD_HOOK_INFO;

#pragma pack(1)

#pragma pack()

#endif // _OD_H_5bacdc5e_0bc6_44b1_b606_84e1831e76c7_
