#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker, "/SECTION:.Amano,ERW /MERGE:.text=.Amano")
#pragma comment(linker, "/EXPORT:GetSaveFileNameW=COMDLG32.GetSaveFileNameW")
#pragma comment(linker, "/EXPORT:CommDlgExtendedError=COMDLG32.CommDlgExtendedError")
#pragma comment(linker, "/EXPORT:GetOpenFileNameW=COMDLG32.GetOpenFileNameW")

#include "MyLibrary.cpp"
#include "mlns.h"

#define ST_VERSION_AUTO 999

#define ST_VERSION ST_VERSION_AUTO

#if ST_VERSION == 2

    typedef WCHAR ACP_TEXT;
    ACP_TEXT Acp[10];

#elif ST_VERSION == 3

    typedef CHAR ACP_TEXT;
    ACP_TEXT Acp[10];

#endif

typedef struct
{
    PWSTR Begin;
    PWSTR End;

    ULONG_PTR Length()
    {
        return End - Begin;
    }

} SUBLIME_TEXT_WSTRING, *PSUBLIME_TEXT_WSTRING;

enum
{
    STCP_Hexadecimal    = 0x1D,
    STCP_UTF_16_BE      = 0x1E,
    STCP_UTF_16_BE_BOM  = 0x1F,
    STCP_UTF_16_LE      = 0x20,
    STCP_UTF_16_LE_BOM  = 0x21,
    STCP_UTF_8_LE_BOM   = 0x22,
    STCP_UTF_8_BOM      = 0x23,

#if ST_VERSION == ST_VERSION_AUTO

    STCP_ACP            = 1,

#else

    STCP_ACP            = ~0u,

#endif

};

ULONG (CDECL *StubUnicodeToACP)(ULONG CpIndex, PSUBLIME_TEXT_WSTRING Unicode, PSTR Ansi, LONG AnsiSize);


ULONG CDECL UnicodeToACP(ULONG CpIndex, PSUBLIME_TEXT_WSTRING Unicode, PSTR Ansi, LONG AnsiSize)
{
    if (CpIndex != STCP_ACP)
        return StubUnicodeToACP(CpIndex, Unicode, Ansi, AnsiSize);

    PSTR        AnsiBuffer;
    PWSTR       UnicodeBuffer;
    ULONG_PTR   Size, UnicodeSize;

    AnsiBuffer      = Ansi;
    UnicodeBuffer   = Unicode->Begin;
    UnicodeSize     = Unicode->Length();
    for (; UnicodeSize != 0 && AnsiSize > 0; AnsiSize -= Size, --UnicodeSize)
    {
        UnicodeToAnsi(AnsiBuffer, AnsiSize, UnicodeBuffer, 1, &Size);

        ++UnicodeBuffer;
        AnsiBuffer += Size;
    }

    Unicode->Begin = UnicodeBuffer;

    return AnsiBuffer - Ansi;
}

#if ST_VERSION != ST_VERSION_AUTO

PSUBLIME_TEXT_WSTRING (CDECL *StubGetEncodingByIndex)(PSUBLIME_TEXT_WSTRING Encoding, ULONG CpIndex);
ULONG (*StubACPToUnicode)();

PSUBLIME_TEXT_WSTRING CDECL GetEncodingByIndex(PSUBLIME_TEXT_WSTRING Encoding, ULONG CpIndex)
{
    if (CpIndex != STCP_ACP)
        return StubGetEncodingByIndex(Encoding, CpIndex);

    Encoding->Begin = (PWSTR)Acp;
    Encoding->End   = (PWSTR)(Acp + CONST_STRLEN(Acp));

    return Encoding;
}

LONG_PTR GetDefaultEncodingIndex()
{
    return STCP_ACP;
}

ULONG STDCALL ACPToUnicode(PSTR *Ansi, PSTR AnsiEnd, PWSTR *Unicode, ULONG CpIndex)
{
    if (CpIndex == STCP_ACP)
    {
        ULONG_PTR Length;

        Length = AnsiEnd - *Ansi;
        AnsiToUnicode(*Unicode, Length, *Ansi, Length, &Length);

        *Unicode    = PtrAdd(*Unicode, Length);
        *Ansi       = AnsiEnd;

        return Length;
    }

    return 0;
}

NAKED ULONG NakedACPToUnicode_2()
{
    INLINE_ASM
    {
        push    eax;
        push    eax;
        push    esi;
        push    ebx;
        push    edi;
        call    ACPToUnicode;
        pop     eax;
        add     esp, 4;
        jmp     StubACPToUnicode;
    }
}

NAKED ULONG NakedACPToUnicode_3()
{
    INLINE_ASM
    {
        push    ecx;
        push    ecx;
        push    edi;
        push    ebx;
        push    esi;
        call    ACPToUnicode;
        pop     ecx;
        add     esp, 4;
        jmp     StubACPToUnicode;
    }
}

#else // auto

ULONG STDCALL ACPToUnicode(PSTR *Ansi, PSTR AnsiEnd, PWSTR *Unicode, PLONG CpIndex)
{
    ULONG_PTR Length;

    --*Ansi;

    Length = AnsiEnd - *Ansi;
    AnsiToUnicode(*Unicode, Length, *Ansi, Length, &Length);

    *Unicode    = PtrAdd(*Unicode, Length);
    *Ansi       = AnsiEnd;
    *CpIndex    = STCP_ACP;

    return 0;
}

NAKED ULONG NakedACPToUnicode_3()
{
    INLINE_ASM
    {
        push    edx;            // PULONG   CpIndex
        push    edi;            // PWSTR*   Unicode
        push    ebx;            // PCSTR    End
        push    esi;            // PCSTR*   Buffer
        call    ACPToUnicode;
        ret;
    }
}

NTSTATUS CDECL StCalcRegKey()
{
    return STATUS_SUCCESS;
}

BOOL (CDECL *StubIsUnicodeEncoding)(ULONG CpIndex);

BOOL CDECL IsUnicodeEncoding(ULONG CpIndex)
{
    return CpIndex == STCP_ACP || StubIsUnicodeEncoding(CpIndex);
}

BOOL
NTAPI
StReplaceFile(
    PCWSTR  ReplacedFileName,
    PCWSTR  ReplacementFileName,
    PCWSTR  BackupFileName,
    ULONG   ReplaceFlags,
    PVOID   Exclude,
    PVOID   Reserved
)
{
    NTSTATUS Status;

    Status = Io::MoveFile(ReplacementFileName, ReplacedFileName);
    BaseSetLastNTError(Status);

    return NT_SUCCESS(Status);
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

                if (Buffer[-10] == 0x68)
                {
                    Buffer -= 10;
                }
                else if (Buffer[-7] == 0x6A)
                {
                    Buffer -= 7;
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

#endif // ST_VERSION_AUTO

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    LdrDisableThreadCalloutsForDll(BaseAddress);

#if ST_VERSION == 2

    MEMORY_PATCH p[] =
    {
        PATCH_MEMORY(STCP_ACP,  sizeof(STCP_ACP),   0x15DD14),
        PATCH_MEMORY(0x01B0,    2,                  0x0CC775),
    };

    MEMORY_FUNCTION_PATCH f[] =
    {
        INLINE_HOOK_JUMP_RVA(0x15D760, GetEncodingByIndex, StubGetEncodingByIndex),
        INLINE_HOOK_JUMP_RVA(0x15E880, UnicodeToACP, StubUnicodeToACP),
        PATCH_FUNCTION(CALL, AUTO_DISASMP | FORCE_JUMP_BACK, 0x15DE51, NakedACPToUnicode_2, 0, &StubACPToUnicode),
    };

    swprintf(Acp, L"ACP %d", CurrentPeb()->AnsiCodePageData[1]);

    Nt_PatchMemory(p, countof(p), f, countof(f), GetExeModuleHandle());

#elif ST_VERSION == 3

    MEMORY_PATCH p[] =
    {
        PATCH_MEMORY(0xC033, 2, 0x08D63C),
    };

    MEMORY_FUNCTION_PATCH f[] =
    {
        INLINE_HOOK_CALL_RVA_NULL(0x0C2F1A, GetDefaultEncodingIndex),

        INLINE_HOOK_JUMP_RVA(0x0C35CC, GetEncodingByIndex, StubGetEncodingByIndex),
        INLINE_HOOK_JUMP_RVA(0x0C33DB, UnicodeToACP, StubUnicodeToACP),

        PATCH_FUNCTION(CALL, AUTO_DISASMP | FORCE_JUMP_BACK, 0x0C2FCA, NakedACPToUnicode_3, 0, &StubACPToUnicode),
    };

    sprintf(Acp, "ACP %d", CurrentPeb()->AnsiCodePageData[1]);

    Nt_PatchMemory(p, countof(p), f, 0*countof(f), GetExeModuleHandle());

#elif ST_VERSION == ST_VERSION_AUTO

    static BYTE DefaultEncodingStub1[] =
    {
        0x8b, 0x06, 0x8a, 0x08, 0x40, 0x89, 0x06, 0x8b, 0x02, 0x0f, 0xb6, 0xd1
    };

    static BYTE DefaultEncodingStub2[] =
    {
        0x8b, 0x0f, 0x66, 0x8b, 0x04, 0x50, 0x8b, 0x55, 0x08, 0x66, 0x89, 0x01, 0x83, 0x07, 0x02, 0x39,
        0x1e, 0x72, 0xda
    };

    static CHAR RegisterKey[] = "30819D300D06092A864886F70D010101050003818B0030818702818100D87BA24562F7C5D14A0CFB12B9740C195C6BDC7E6D6EC92BAC0EB29D59E1D9AE67890C2B88C3ABDCAFFE7D4A33DCC1BFBE531A251CEF0C923F06BE79B2328559ACFEE986D5E15E4D1766EA56C4E10657FA74DB0977C3FB7582B78CD47BB2C7F9B252B4A9463D15F6AE6EE9237D54C5481BF3E0B09920190BCFB31E5BE509C33B020111";
    static CHAR CheckEncodingWhenSave[] = "Not all characters are representable in ";
    static CHAR WithEncodingString[] = " with encoding ";

    PVOID ACPToUnicodeStub, UnicodeToACPStub, WithEncodingStub;
    PVOID CalcRegKey;
    PVOID NotAllCharactersRepresentable, IsUnicodeEncodingAddress;

    PLDR_MODULE module;

    ACPToUnicodeStub = nullptr;
    UnicodeToACPStub = nullptr;

    module = FindLdrModuleByHandle(nullptr);

    CalcRegKey = SearchStringAndReverseSearchHeader(module->DllBase, RegisterKey, sizeof(RegisterKey), 0x30);

    {

        SEARCH_PATTERN_DATA Pattern[] =
        {
            ADD_PATTERN(DefaultEncodingStub1, 0, sizeof(DefaultEncodingStub1) + 7),
            ADD_PATTERN(DefaultEncodingStub2),
        };

        ACPToUnicodeStub = SearchPattern(Pattern, countof(Pattern), module->DllBase, module->SizeOfImage);
        if (ACPToUnicodeStub == nullptr)
            return FALSE;
    }

    {
        SEARCH_PATTERN_DATA Pattern[] =
        {
            ADD_PATTERN(WithEncodingString),
        };

        WithEncodingStub = SearchPattern(Pattern, countof(Pattern), module->DllBase, module->SizeOfImage);
        if (WithEncodingStub == nullptr)
            return FALSE;
    }

    {
        SEARCH_PATTERN_DATA Pattern[] =
        {
            ADD_PATTERN(&WithEncodingStub),
        };

        WithEncodingStub = SearchPattern(Pattern, countof(Pattern), module->DllBase, module->SizeOfImage);
        if (WithEncodingStub == nullptr)
            return FALSE;
    }

    BOOL MagicFound = FALSE;

    WithEncodingStub = PtrAdd(WithEncodingStub, 4);
    for (LONG_PTR Size = 0x200; Size > 0; )
    {
        ULONG_PTR Len;

        if (*(PULONG)PtrAdd(WithEncodingStub, 2) == 0x40000)
        {
            MagicFound = TRUE;
        }
        else if (MagicFound) switch (*(PBYTE)WithEncodingStub)
        {
            case CALL:
                Size = 0;
                UnicodeToACPStub = GetCallDestination(WithEncodingStub);
                continue;
        }

        Len = GetOpCodeSize(WithEncodingStub);
        WithEncodingStub = PtrAdd(WithEncodingStub, Len);
        Size -= Len;
        if (Size <= 0)
            return FALSE;
    }

    {
        NotAllCharactersRepresentable = SearchStringAndReverseSearchHeader(module->DllBase, CheckEncodingWhenSave, sizeof(CheckEncodingWhenSave), 0x120);
        if (NotAllCharactersRepresentable == nullptr)
            return FALSE;

        ULONG_PTR NumberOfCall = 0;

        IsUnicodeEncodingAddress = nullptr;
        WalkOpCodeT(NotAllCharactersRepresentable, 0x70,
            WalkOpCodeM(Buffer, OpLength, Ret)
            {
                if (Buffer[0] == CALL && ++NumberOfCall == 2)
                {
                    IsUnicodeEncodingAddress = GetCallDestination(Buffer);
                    return STATUS_SUCCESS;
                }

                return STATUS_NOT_FOUND;
            }
        );

        if (IsUnicodeEncodingAddress == nullptr)
            return FALSE;
    }

    MEMORY_FUNCTION_PATCH f[] =
    {
        INLINE_HOOK_CALL_NULL(PtrAdd(ACPToUnicodeStub, 0x1C), NakedACPToUnicode_3),
        INLINE_HOOK_JUMP(UnicodeToACPStub, UnicodeToACP, StubUnicodeToACP),
        INLINE_HOOK_JUMP_NULL(CalcRegKey, StCalcRegKey),
        INLINE_HOOK_JUMP(IsUnicodeEncodingAddress, IsUnicodeEncoding, StubIsUnicodeEncoding)
    };

    PVOID addr = StReplaceFile;
    WriteProtectMemory(CurrentProcess, PtrAdd(module->DllBase, IATLookupRoutineRVAByHashNoFix(module->DllBase, KERNEL32_ReplaceFileW)), &addr, sizeof(addr));

    Nt_PatchMemory(0, 0, f, countof(f));

#endif

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
