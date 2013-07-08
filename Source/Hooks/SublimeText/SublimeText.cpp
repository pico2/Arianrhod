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

    STCP_ACP            = ~0u,
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

    Nt_PatchMemory(p, countof(p), f, countof(f), GetExeModuleHandle());

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

    static CHAR WithEncodingString[] = " with encoding ";

    PVOID ACPToUnicodeStub, UnicodeToACPStub, WithEncodingStub;
    PLDR_MODULE module;

    ACPToUnicodeStub = NULL;
    UnicodeToACPStub = NULL;

    module = FindLdrModuleByHandle(NULL);

    {

        SEARCH_PATTERN_DATA Pattern[] =
        {
            ADD_PATTERN(DefaultEncodingStub1, 0, sizeof(DefaultEncodingStub1) + 7),
            ADD_PATTERN(DefaultEncodingStub2),
        };

        ACPToUnicodeStub = SearchPattern(Pattern, countof(Pattern), module->DllBase, module->SizeOfImage);
        if (ACPToUnicodeStub == NULL)
            return FALSE;
    }

    {
        SEARCH_PATTERN_DATA Pattern[] =
        {
            ADD_PATTERN(WithEncodingString),
        };

        WithEncodingStub = SearchPattern(Pattern, countof(Pattern), module->DllBase, module->SizeOfImage);
        if (WithEncodingStub == NULL)
            return FALSE;
    }

    {
        SEARCH_PATTERN_DATA Pattern[] =
        {
            ADD_PATTERN(&WithEncodingStub),
        };

        WithEncodingStub = SearchPattern(Pattern, countof(Pattern), module->DllBase, module->SizeOfImage);
        if (WithEncodingStub == NULL)
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

    MEMORY_FUNCTION_PATCH f[] =
    {
        INLINE_HOOK_CALL_NULL(PtrAdd(ACPToUnicodeStub, 0x1C), NakedACPToUnicode_3),
        INLINE_HOOK_JUMP_RVA(UnicodeToACPStub, UnicodeToACP, StubUnicodeToACP),
    };

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
