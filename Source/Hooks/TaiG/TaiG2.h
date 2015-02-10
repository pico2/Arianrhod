#ifndef _TAIG2_H_4ec3cd5a_8227_47ed_a9aa_256432b5034d_
#define _TAIG2_H_4ec3cd5a_8227_47ed_a9aa_256432b5034d_

#include <Ws2spi.h>
#include "ml.h"
#include "D:\Desktop\Source\Test_Con\iTunes\iTunes.h"

typedef struct
{
    ULONG _;

    union
    {
        CHAR SmallBuffer[0x10];
        PSTR Buffer;
    };

    ULONG Length;
    ULONG MaximumLength;

    PSTR GetBuffer()
    {
        return Length > countof(SmallBuffer) - 1 ? Buffer : SmallBuffer;
    }

} STL_STRING, *PSTL_STRING;

typedef struct  // 0xA0
{
    PVOID _;                            // 0x00

    STL_STRING  UniqueDeviceId;         // 0x08
    STL_STRING  DeviceName;             // 0x20
    STL_STRING  ProductVersion;         // 0x3C
    STL_STRING  DeviceClass;            // 0x58
    STL_STRING  ProductType;            // 0x74

    ULONG64     ProductVersionValue;    // 0x90     int.int.int.int

    BOOLEAN     What;                   // 0x98
    BOOLEAN     PasswordProtected;      // 0x99
    BOOLEAN     Jailbroken;             // 0x9A
    BOOLEAN     UnActivate;             // 0x9B

    ULONG       Padded;                 // 0x9C

} IOS_DEVICE, *PIOS_DEVICE;

typedef struct
{
    STL_STRING FileName;
    STL_STRING FileVersion;
    STL_STRING FileText;

    BOOLEAN Selectable;
    BOOLEAN SelectPrompt;
    BOOLEAN Selected;

} DEB_ENTRY, *PDEB_ENTRY;

extern PVOID TaiGBase;

LONG CDECL TGAFCSendData(AFCConnection Connection, PVOID Buffer, LONG Length);
LONG CDECL TGAFCReadData(AFCConnection Connection, PVOID Buffer, LONG Length);
LONG CDECL TGAMDServiceConnectionSend(CFServiceRef Connection, PVOID Data, ULONG Length);
LONG CDECL TGAMDServiceConnectionReceive(CFServiceRef Connection, PVOID Buffer, ULONG Length);

#endif // _TAIG2_H_4ec3cd5a_8227_47ed_a9aa_256432b5034d_
