#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text /MERGE:.text1=.text /SECTION:.idata,ERW")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")
#pragma comment(linker, "/EXPORT:GetFileVersionInfoW=VERSION.GetFileVersionInfoW")
#pragma comment(linker, "/EXPORT:GetFileVersionInfoSizeW=VERSION.GetFileVersionInfoSizeW")
#pragma comment(linker, "/EXPORT:VerQueryValueW=VERSION.VerQueryValueW")

#include "ml.cpp"

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

VOID (FASTCALL *StubPushDebList)(PVOID vec, PVOID, PVOID v1, PVOID v2, DEB_ENTRY*& Entry);
LONG (CDECL *StubFormatCheckboxXml)(PVOID str, PWSTR format, ULONG index);

VOID FASTCALL PushDebList(PVOID vec, PVOID, PVOID v1, PVOID v2, DEB_ENTRY*& Entry)
{
    if (StrCompareA(Entry->FileName.GetBuffer(), "Cydia") != 0)
    {
        //Entry->Selectable    = FALSE;
        Entry->SelectPrompt  = FALSE;
        Entry->Selected      = FALSE;
    }

    return StubPushDebList(vec, 0, v1, v2, Entry);
}

LONG CDECL FormatCheckboxXml(PVOID str, PWSTR format, ULONG index)
{
    if (index != 0)
    {
        return StubFormatCheckboxXml(str, ml::String(format).Replace(LR"(selected="true")", LR"(selected="false" enabled="false")"), index);
    }

    return StubFormatCheckboxXml(str, format, index);
}

BOOL CDECL IsJailbroken(HANDLE Device)
{
    RtlSetLastWin32Error(STATUS_UNSUCCESSFUL);
    return FALSE;
}

BOOL CDECL IsDeviceUnActivated(HANDLE Device)
{
    return FALSE;
}

PVOID NTAPI LoadTaiGDll(PCSTR)
{
    return LoadDll(L"TaiG.dll");
}

BOOL CDECL VerifyTaiGExe()
{
    return TRUE;
}

PVOID CDECL TgGetRoutine(PVOID BaseAddress, PVOID OrdinalOrName)
{
}

BOOL CDECL IsiTunesMobileAndAirTrafficHasBreakPoint()
{
    return FALSE;
}

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    using namespace Mp;

    LdrDisableThreadCalloutsForDll(BaseAddress);
    ml::MlInitialize();

    BaseAddress = LoadDll(L"TaiG.dll");

    {
        PATCH_MEMORY_DATA p[] =
        {
            MemoryPatchRva(0x00ull, 1, 0x9301),     // DebEntry->Selected = FALSE

            FunctionJumpRva(0x149A0, IsiTunesMobileAndAirTrafficHasBreakPoint),

            //FunctionJumpRva(0x35870, TgGetRoutine),
            //FunctionJumpRva(0x5CD0, VerifyTaiGExe),

            //FunctionJumpRva(0x11360, IsJailbroken),
            //FunctionCallRva(0x09357, PushDebList, &StubPushDebList),
            //FunctionJumpRva(0x145B0, IsDeviceUnActivated),
        };

        PatchMemory(p, countof(p), BaseAddress);
    }

    {
        PATCH_MEMORY_DATA p[] =
        {
            MemoryPatchRva(0x80, 1, 0x18D9B),       // jo

            FunctionCallRva(0x1500B, LoadTaiGDll),
            //FunctionCallRva(0x18BBC, FormatCheckboxXml, &StubFormatCheckboxXml),
        };

        PatchMemory(p, countof(p), GetExeModuleHandle());
    }

    return TRUE;
}

BOOL WINAPI DllMain(PVOID BaseAddress, ULONG Reason, PVOID Reserved)
{
    switch (Reason)
    {
        case DLL_PROCESS_ATTACH:
            return Initialize(BaseAddress) || UnInitialize(BaseAddress);

        case DLL_PROCESS_DETACH:
            UnInitialize(BaseAddress);
            break;
    }

    return TRUE;
}
