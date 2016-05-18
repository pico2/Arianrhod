#include "iTunesHelper.h"

PVOID
SearchSignatureAndReverseSearchHeader(
    PVOID       ImageBase,
    PVOID       BytesSequence,
    ULONG_PTR   SizeInBytes,
    ULONG_PTR   SearchRange
)
{
    PVOID Found;
    SEARCH_PATTERN_DATA pattern[] =
    {
        ADD_PATTERN_(BytesSequence, SizeInBytes),
    };

    Found = SearchPattern(pattern, countof(pattern), ImageBase, ImageNtHeaders(ImageBase)->OptionalHeader.SizeOfImage);
    if (Found == nullptr)
        return nullptr;

    Found = ReverseSearchFunctionHeader(Found, SearchRange);

    return Found;
}

PVOID search_freeSessionData(PVOID itunes)
{
    static BYTE sig[] =
    {
        0x81, 0xF1, 0x11, 0x1B, 0xE4, 0x1C,  // xor     ecx, 1CE41B11h
        0x69, 0xD1, 0xE5, 0xB0, 0x77, 0x3C,  // imul    edx, ecx, 3C77B0E5h
    };

    return SearchSignatureAndReverseSearchHeader(itunes, sig, sizeof(sig), 0x30);
}

PVOID search_kbsyncCreateSession(PVOID itunes)
{
    static BYTE sig[] =
    {
        0x83, 0xC4, 0x10,                       // add esp, 0x10
        0x81, 0xFE, 0x57, 0x5B, 0xFF, 0xFF,     // cmp esi, 0xFFFF5B57
    };

    PBYTE Found;
    SEARCH_PATTERN_DATA pattern[] =
    {
        ADD_PATTERN(sig),
    };

    Found = (PBYTE)SearchPattern(pattern, countof(pattern), itunes, ImageNtHeaders(itunes)->OptionalHeader.SizeOfImage);
    if (Found == nullptr)
        return nullptr;

    if (Found[-7] != 0xE8)
        return nullptr;

    return GetCallDestination(&Found[-7]);
}

PVOID search_kbsyncValidate(PVOID itunes)
{
    /*
        .text:104BA480 E8 DB 62 BD FF       call    kbsyncValidate
        .text:104BA485 83 C4 04             add     esp, 4
        .text:104BA488 3D 57 5B FF FF       cmp     eax, 0FFFF5B57h
    */

    PVOID Found;

    Found = SearchPatternSafe(L"E8 ?? ?? ?? ?? 83 C4 04 3D 57 5B FF FF", itunes, ImageNtHeaders(itunes)->OptionalHeader.SizeOfImage);
    if (Found == nullptr)
        return nullptr;

    return GetCallDestination(Found);
}

PVOID search_kbsyncInitSomething(PVOID itunes)
{
    /*
        .text:10CB27AA E8 A1 15 3E FF       call    kbsyncInitSomething
        .text:10CB27AF 83 C4 0C             add     esp, 0Ch
        .text:10CB27B2 3D A3 5B FF FF       cmp     eax, 0FFFF5BA3h
    */

    PVOID Found;

    Found = SearchPatternSafe(L"E8 ?? ?? ?? ?? 83 C4 0C 3D A3 5B FF FF", itunes, ImageNtHeaders(itunes)->OptionalHeader.SizeOfImage);
    if (Found == nullptr)
        return nullptr;

    return GetCallDestination(Found);
}

PVOID search_kbsyncGetData(PVOID itunes)
{
    /*
        .text:10CB6294 8D 4D F0             lea     ecx, [ebp+var_10]
        .text:10CB6297 51                   push    ecx
        .text:10CB6298 8D 4D FC             lea     ecx, [ebp+var_4]
        .text:10CB629B 51                   push    ecx
        .text:10CB629C FF 75 F8             push    [ebp+var_8]
        .text:10CB629F 50                   push    eax
        .text:10CB62A0 FF 75 0C             push    [ebp+arg_4]
        .text:10CB62A3 FF 75 08             push    [ebp+arg_0]
        .text:10CB62A6 FF 75 F4             push    [ebp+var_C]
        .text:10CB62A9 E8 D2 6C 36 FF       call    kbsyncGetData
        .text:10CB62AE 83 C4 1C             add     esp, 1Ch
    */

    PVOID Found;

    Found = SearchPatternSafe(L"8D 4D F0 51 8D 4D FC 51 FF 75 F8 50 FF 75 0C FF 75 08 FF 75 F4 E8 ?? ?? ?? ?? 83 C4 1C 85 C0", itunes, ImageNtHeaders(itunes)->OptionalHeader.SizeOfImage);
    if (Found == nullptr)
        return nullptr;

    return GetCallDestination(PtrAdd(Found, 0x15));
}

PVOID search_kbsyncImport(PVOID itunes)
{
    /*
        .text:104BA468 E8 E3 51 BA FF       call    kbsyncImport
        .text:104BA46D 83 C4 0C             add     esp, 0Ch
        .text:104BA470 3D EF 5B FF FF       cmp     eax, 0FFFF5BEFh
    */

    PVOID Found;

    Found = SearchPatternSafe(L"E8 ?? ?? ?? ?? 83 C4 0C 3D EF 5B FF FF", itunes, ImageNtHeaders(itunes)->OptionalHeader.SizeOfImage);
    if (Found == nullptr)
        return nullptr;

    return GetCallDestination(Found);
}

//
// sap
//

PVOID search_sapCreateSession(PVOID itunes)
{
    /*
        .text:10ED4518 E8 83 1A 19 FF           call    sapCreateSession
        .text:10ED451D 8B F8                    mov     edi, eax
        .text:10ED451F 83 C4 08                 add     esp, 8
        .text:10ED4522 81 FF 58 5A FF FF        cmp     edi, 0FFFF5A58h
    */

    PVOID Found;

    Found = SearchPatternSafe(L"E8 ?? ?? ?? ?? 8B F8 83 C4 08 81 FF 58 5A FF FF", itunes, ImageNtHeaders(itunes)->OptionalHeader.SizeOfImage);
    if (Found == nullptr)
        return nullptr;

    return GetCallDestination(Found);
}

NTSTATUS search_sapCreateSession_sapExchangeData_sapCloseSession_getDeviceId(PVOID itunes, iTunesRoutines* routines)
{
    /*
        .text:10ED4518 E8 83 1A 19 FF           call    sapCreateSession
        .text:10ED451D 8B F8                    mov     edi, eax
        .text:10ED451F 83 C4 08                 add     esp, 8
        .text:10ED4522 81 FF 58 5A FF FF        cmp     edi, 0FFFF5A58h
    */

    PVOID Found;

    Found = SearchPatternSafe(L"E8 ?? ?? ?? ?? 8B F8 83 C4 08 81 FF 58 5A FF FF", itunes, ImageNtHeaders(itunes)->OptionalHeader.SizeOfImage);
    if (Found == nullptr)
        return STATUS_NOT_FOUND;

    *(PVOID *)&routines->sapCreateSession = GetCallDestination(Found);

    Found = ReverseSearchFunctionHeader(Found, 0x50);
    if (Found == nullptr)
        return STATUS_NOT_FOUND;

    ULONG_PTR CallIndex = 0;

    WalkOpCodeT(Found, 0x500,
        WalkOpCodeM(Buffer, OpLength, Ret)
        {
            switch (Buffer[0])
            {
                case 0xC2:
                case 0xC3:
                    return STATUS_SUCCESS;

                case 0xE8:
                    switch (CallIndex++)
                    {
                        case 0:
                            *(PVOID *)&routines->sapCloseSession = GetCallDestination(Buffer);
                            break;

                        case 1:
                            *(PVOID *)&routines->getDeviceId = GetCallDestination(Buffer);
                            break;

                        case 2:
                        case 4:
                            if ((PVOID)routines->sapCreateSession != GetCallDestination(Buffer))
                                DebugBreakPoint();

                            break;

                        case 3:
                            break;

                        case 5:
                            *(PVOID *)&routines->sapExchangeData = GetCallDestination(Buffer);
                            break;

                        default:
                            return STATUS_SUCCESS;
                    }

                    break;
            }

            return STATUS_VALIDATE_CONTINUE;
        }
    );

    if (routines->sapExchangeData == nullptr)
        return STATUS_NOT_FOUND;

    if (routines->sapCreateSession == nullptr)
        return STATUS_NOT_FOUND;

    if (routines->sapCloseSession == nullptr)
        return STATUS_NOT_FOUND;

    if (routines->getDeviceId == nullptr)
        return STATUS_NOT_FOUND;

    return STATUS_SUCCESS;
}

PVOID search_sapCreatePrimeSignature(PVOID itunes)
{
    /*
        .text:109324AE 6A 00                    push    0
        .text:109324B0 6A 00                    push    0
        .text:109324B2 6A 64                    push    64h
        .text:109324B4 FF 76 24                 push    dword ptr [esi+24h]
        .text:109324B7 E8 84 0A 70 FF           call    sapCreatePrimeSignature
        .text:109324BC 83 C4 18                 add     esp, 18h
        .text:109324BF 8B F8                    mov     edi, eax
        .text:109324C1 81 3E 6B 63 6F 6C        cmp     dword ptr [esi], 6C6F636Bh
    */

    PVOID Found;

    Found = SearchPatternSafe(L"6A 00 6A 00 6A 64 FF 76 24 E8 ?? ?? ?? ?? 83 C4 18 8B F8 81 3E 6B 63 6F 6C", itunes, ImageNtHeaders(itunes)->OptionalHeader.SizeOfImage);
    if (Found == nullptr)
        return nullptr;

    return GetCallDestination(PtrAdd(Found, 9));
}

PVOID search_sapVerifyPrimeSignature(PVOID itunes)
{
    /*
        mov     eax, X-Apple-ActionSignature
        ...
        call    ds:CFHTTPMessageCopyHeaderFieldValue
        ...
        call    sapVerifyPrimeSignature_0
            .text:109326A7 56                   push    esi
            .text:109326A8 FF 15 C8 F6 4C 11    call    ds:CFDataGetLength
            .text:109326AE 56                   push    esi
            .text:109326AF 8B F8                mov     edi, eax
            .text:109326B1 FF 15 90 F7 4C 11    call    ds:CFDataGetBytePtr
            .text:109326B7 83 C4 08             add     esp, 8
            .text:109326BA 8B CB                mov     ecx, ebx
            .text:109326BC 6A 00                push    0
            .text:109326BE 6A 00                push    0
            .text:109326C0 57                   push    edi
            .text:109326C1 50                   push    eax
            .text:109326C2 E8 A9 FE FF FF       call    sapVerifyPrimeSignature_1
                call sapVerifyPrimeSignature
    */
}

NTSTATUS iTunesRoutines::searchRoutines(PVOID itunes)
{
    *(PVOID *)&this->freeSessionData        = search_freeSessionData(itunes);
    // *(PVOID *)&this->kbsyncCreateSession    = search_kbsyncCreateSession(itunes);
    // *(PVOID *)&this->kbsyncValidate         = search_kbsyncValidate(itunes);
    // *(PVOID *)&this->kbsyncInitSomething    = search_kbsyncInitSomething(itunes);
    // *(PVOID *)&this->kbsyncGetData          = search_kbsyncGetData(itunes);
    // *(PVOID *)&this->kbsyncImport           = search_kbsyncImport(itunes);

    search_sapCreateSession_sapExchangeData_sapCloseSession_getDeviceId(itunes, this);
    *(PVOID *)&this->sapCreatePrimeSignature    = search_sapCreatePrimeSignature(itunes);

    return STATUS_NOT_IMPLEMENTED;
}
