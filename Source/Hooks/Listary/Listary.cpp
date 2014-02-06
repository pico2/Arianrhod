#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text /MERGE:.text1=.text /SECTION:.idata,ERW")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")
#pragma comment(linker, "/EXPORT:AlphaBlend=_MSIMG32_AlphaBlend@44")
#pragma comment(linker, "/EXPORT:GradientFill=GDI32.GdiGradientFill")
#pragma comment(linker, "/EXPORT:TransparentBlt=GDI32.GdiTransparentBlt")

#include "MyLibrary.cpp"

API_POINTER(AlphaBlend) StubAlphaBlend;

EXTC
BOOL
NTAPI
MSIMG32_AlphaBlend(
    HDC hdcDest,
    int xoriginDest,
    int yoriginDest,
    int wDest,
    int hDest,
    HDC hdcSrc,
    int xoriginSrc,
    int yoriginSrc,
    int wSrc,
    int hSrc,
    BLENDFUNCTION ftn
)
{
    return StubAlphaBlend(hdcDest, xoriginDest, yoriginDest, wDest, hDest, hdcSrc, xoriginSrc, yoriginSrc, wSrc, hSrc, ftn);
}

PVOID SearchStringReference(PLDR_MODULE Module, PVOID String, ULONG_PTR SizeInBytes, ULONG_PTR BeginOffset = 0)
{
    PVOID StringValue, StringReference;

    SEARCH_PATTERN_DATA Str[] =
    {
        ADD_PATTERN_(String, SizeInBytes),
    };

    StringValue = SearchPattern(Str, countof(Str), Module->DllBase, Module->SizeOfImage);
    if (StringValue == nullptr)
        return nullptr;

    SEARCH_PATTERN_DATA Stub[] =
    {
        ADD_PATTERN(&StringValue),
    };

    StringReference = SearchPattern(Stub, countof(Stub), PtrAdd(Module->DllBase, BeginOffset), PtrSub(Module->SizeOfImage, BeginOffset));
    if (StringReference == nullptr)
        return nullptr;

    return StringReference;
}

PVOID ReverseSearchFunctionHeader(PVOID Start, ULONG_PTR Length)
{
    PBYTE Buffer;

    Buffer = (PBYTE)Start;

    for (; Length != 0; --Buffer, --Length)
    {
        switch (Buffer[0])
        {
            case CALL:
                // push    local_var_size
                // mov     eax, exception_handler
                // call    _SEH_prolog

                if (Buffer[-5] != 0xB8)
                    continue;

                if (Buffer[-7] == 0x6A)
                {
                    Buffer -= 7;
                }
                else if (Buffer[-10] == 0x68)
                {
                    Buffer -= 10;
                }
                else
                {
                    continue;
                }

                break;

            case 0x55:
                if (Buffer[1] != 0x8B || Buffer[2] != 0xEC)
                    continue;

                // push ebp
                // mov ebp, esp

                break;

            default:
                continue;
        }

        return Buffer;
    }

    return nullptr;
}

PVOID
SearchStringAndReverseSearchHeader(
    PVOID       ImageBase,
    PVOID       BytesSequence,
    ULONG_PTR   SizeInBytes,
    ULONG_PTR   SearchRange
)
{
    PVOID       StringReference;
    PLDR_MODULE Module;

    Module = FindLdrModuleByHandle(ImageBase);

    StringReference = SearchStringReference(Module, BytesSequence, SizeInBytes);
    if (StringReference == nullptr)
        return IMAGE_INVALID_VA;

    StringReference = ReverseSearchFunctionHeader(PtrAdd(StringReference, 4), SearchRange);

    return StringReference == nullptr ? IMAGE_INVALID_VA : StringReference;
}

PVOID (FASTCALL *StubGetLicenseManager)(PVOID This);

PVOID FASTCALL GetLicenseManager(PVOID This)
{
    typedef struct
    {
        union
        {
            WCHAR SmallBuffer[8];
            PWSTR Buffer;
        };

        ULONG Length;
        ULONG MaximumLength;

        PWSTR GetBuffer()
        {
            return Length > countof(SmallBuffer) ? Buffer : SmallBuffer;
        }

    } LISTARY_STRING, *PLISTARY_STRING;

    typedef struct
    {
        CHAR    UserNameLower[100];
        ULONG   UserNameLength;             // 0x64
        CHAR    RegCode[0x60];              // 0x68
        ULONG   Crc32;                      // 0xC8
        ULONG   Hash;                       // 0xCC
        ULONG   Sum;                        // 0xD0

    } LICENSE_DATA, *PLICENSE_DATA;

    typedef struct
    {
        PVOID x;
        BOOL Initialized;       // BOOLEAN
        LISTARY_STRING Email;
        LISTARY_STRING Name;
        LISTARY_STRING RegCode;
        PLICENSE_DATA LicenseData;

    } LICENSE_MANAGER, *PLICENSE_MANAGER;
    
    static LICENSE_DATA LicenseData;

    ULONG_PTR           Data;
    PSTR                Buffer;
    PWSTR               BufferW;
    PLICENSE_MANAGER    Manager;
    
    Manager = *(PLICENSE_MANAGER *)PtrAdd(This, 0x24);
    if (Manager != nullptr)
        return Manager;

    StubGetLicenseManager(This);

    Manager = *(PLICENSE_MANAGER *)PtrAdd(This, 0x24);
    Manager->LicenseData = &LicenseData;

    Buffer = LicenseData.UserNameLower;
    FOR_EACH(BufferW, L"东方姑娘", CONST_STRLEN(L"东方姑娘"))
    {
        *Buffer++ = CHAR_LOWER(*BufferW);
    }

    LicenseData.UserNameLength = Buffer - LicenseData.UserNameLower;

    LicenseData.Crc32 = RtlComputeCrc32(
                            RtlComputeCrc32(
                                RtlComputeCrc32(
                                    0,
                                    LicenseData.UserNameLower,
                                    LicenseData.UserNameLength
                                ),
                                "Listary",
                                CONST_STRLEN("Listary")
                            ),
                            LicenseData.RegCode,
                            sizeof(LicenseData.RegCode)
                        );

    Data = 0;
    FOR_EACH(Buffer, LicenseData.UserNameLower, LicenseData.UserNameLength)
    {
        Data = Data * 0x2B + (LONG)*Buffer;
    }

    LicenseData.Hash = Data;

    Data = 0;
    FOR_EACH(Buffer, LicenseData.UserNameLower, LicenseData.UserNameLength)
    {
        ULONG_PTR And;
        Data <<= 4;
        Data += (LONG)*Buffer;
        And = Data & 0xF0000000;
        if (And != 0)
        {
            Data ^= (And >> 0x18) ^ And;
        }
    }

    LicenseData.Sum = Data;

    return Manager;
}

PVOID SearchGetLicenseManager(PVOID ImageBase)
{
    static CHAR String[] = "no_pro";
    return SearchStringAndReverseSearchHeader(ImageBase, String, sizeof(String), 0xB0);
}

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    LdrDisableThreadCalloutsForDll(BaseAddress);
    ml::MlInitialize();

    {
        ml::String SystemDirectory;

        Rtl::GetModuleDirectory(SystemDirectory, GetNtdllHandle());

        *(PVOID *)&StubAlphaBlend = GetRoutineAddress(Ldr::LoadDll(SystemDirectory + L"msimg32.dll"), "AlphaBlend");
    }

    PVOID GetLicenseManagerAddress;

    BaseAddress = GetExeModuleHandle();
    if (RtlEqualUnicodeString(&FindLdrModuleByHandle(nullptr)->BaseDllName, &USTR(L"Listary.exe"), TRUE) == FALSE)
        return TRUE;

    GetLicenseManagerAddress = SearchGetLicenseManager(BaseAddress);

    MEMORY_FUNCTION_PATCH f[] =
    {
        INLINE_HOOK_JUMP(GetLicenseManagerAddress, GetLicenseManager, StubGetLicenseManager),
    };

    Nt_PatchMemory(nullptr, 0, f, countof(f));

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
