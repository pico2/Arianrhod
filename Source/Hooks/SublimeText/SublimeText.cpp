#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker, "/SECTION:.Amano,ERW /MERGE:.text=.Amano")
//#pragma comment(linker, "/EXPORT:GetSaveFileNameW=COMDLG32.GetSaveFileNameW")
//#pragma comment(linker, "/EXPORT:CommDlgExtendedError=COMDLG32.CommDlgExtendedError")
//#pragma comment(linker, "/EXPORT:GetOpenFileNameW=COMDLG32.GetOpenFileNameW")
#pragma comment(linker, "/EXPORT:MiniDumpWriteDump=_StMiniDumpWriteDump@28")

#include "ml.cpp"

ML_OVERLOAD_NEW

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

    STCP_ACP            = 1,
};

API_POINTER(MiniDumpWriteDump) DbghlpMiniDumpWriteDump;

VOID InitializeDbghelp()
{
    if (DbghlpMiniDumpWriteDump != nullptr)
        return;

    PVOID module;
    PLDR_MODULE self, dbghlp;
    ml::String path;

    Rtl::GetModuleDirectory(path, GetNtdllHandle());

    path += L"dbghelp.dll";

    module = Ldr::LoadDll(path);
    if (module == nullptr)
        return;

    *(PVOID *)&DbghlpMiniDumpWriteDump = GetRoutineAddress(module, "MiniDumpWriteDump");

    self = FindLdrModuleByHandle(&__ImageBase);
    dbghlp = FindLdrModuleByHandle(module);

    self->DllBase = dbghlp->DllBase;
    self->EntryPoint = dbghlp->EntryPoint;
    self->SizeOfImage = dbghlp->SizeOfImage;
}

EXTC
BOOL
NTAPI
StMiniDumpWriteDump(
    HANDLE                              hProcess,
    DWORD                               ProcessId,
    HANDLE                              hFile,
    MINIDUMP_TYPE                       DumpType,
    PMINIDUMP_EXCEPTION_INFORMATION     ExceptionParam,
    PMINIDUMP_USER_STREAM_INFORMATION   UserStreamParam,
    PMINIDUMP_CALLBACK_INFORMATION      CallbackParam
)
{
    InitializeDbghelp();

    if (DbghlpMiniDumpWriteDump != nullptr)
        return DbghlpMiniDumpWriteDump(hProcess, ProcessId, hFile, DumpType, ExceptionParam, UserStreamParam, CallbackParam);

    return FALSE;
}

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

NTSTATUS CDECL StCalcRegKey(PVOID arg1, PVOID arg2, PVOID arg3, PVOID arg4)
{
    return arg2 != nullptr ? 1 : STATUS_SUCCESS;
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
    ULONG_PTR   Attributes;
    NTSTATUS    Status;

    Status = Io::QueryFileAttributesEx(ReplacedFileName, &Attributes);
    if (Status == STATUS_OBJECT_NAME_NOT_FOUND)
    {
        Attributes = FILE_ATTRIBUTE_NORMAL;
    }
    else if (NT_FAILED(Status))
    {
        BaseSetLastNTError(Status);
        return FALSE;
    }

    Status = Io::MoveFile(ReplacementFileName, ReplacedFileName, TRUE);
    BaseSetLastNTError(Status);
    if (NT_SUCCESS(Status))
    {
        Io::ApplyFileAttributes(ReplacedFileName, Attributes);
    }

    return NT_SUCCESS(Status);
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

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    using namespace Mp;

    LdrDisableThreadCalloutsForDll(BaseAddress);
    ml::MlInitialize();

    //static CHAR RegisterKey[] = "30819D300D06092A864886F70D010101050003818B0030818702818100D87BA24562F7C5D14A0CFB12B9740C195C6BDC7E6D6EC92BAC0EB29D59E1D9AE67890C2B88C3ABDCAFFE7D4A33DCC1BFBE531A251CEF0C923F06BE79B2328559ACFEE986D5E15E4D1766EA56C4E10657FA74DB0977C3FB7582B78CD47BB2C7F9B252B4A9463D15F6AE6EE9237D54C5481BF3E0B09920190BCFB31E5BE509C33B020111";
    static CHAR RegisterKey[] = "EA7E";
    static CHAR CheckEncodingWhenSave[] = "Not all characters are representable in ";

    PVOID ACPToUnicodeStub, UnicodeToACPStub, WithEncodingStub;
    PVOID CalcRegKey;
    PVOID NotAllCharactersRepresentable, IsUnicodeEncodingAddress;

    PLDR_MODULE module;

    ACPToUnicodeStub = nullptr;
    UnicodeToACPStub = nullptr;

    module = FindLdrModuleByHandle(nullptr);

    CalcRegKey = SearchStringAndReverseSearchHeader(module->DllBase, RegisterKey, sizeof(RegisterKey), 0xC0);

#if 0

    {
        /*++

            0028189F   |> /8B06               /mov     eax, dword ptr [esi]
            002818A1   |. |8A08               |mov     cl, byte ptr [eax]
            002818A3   |. |40                 |inc     eax
            002818A4   |. |8906               |mov     dword ptr [esi], eax
            002818A6   |. |8B02               |mov     eax, dword ptr [edx]
            002818A8   |. |0FB6D1             |movzx   edx, cl
            002818AB   |. |8B0485 00F45A00    |mov     eax, dword ptr [eax*4+0x5AF400]    ?? ?? ?? ?? ?? ?? ??
            002818B2   |. |8B0F               |mov     ecx, dword ptr [edi]
            002818B4   |. |66:8B0450          |mov     ax, word ptr [eax+edx*2]
            002818B8   |. |8B55 08            |mov     edx, [arg.1]
            002818BB   |. |66:8901            |mov     word ptr [ecx], ax
            002818BE   |. |8307 02            |add     dword ptr [edi], 0x2
            002818C1   |> |391E                cmp     dword ptr [esi], ebx
            002818C3   |.^\72 DA              \jb      short 0x28189F

            001C1DBB   |> /8B06                /mov     eax, dword ptr [esi]
            001C1DBD   |. |8A08                |mov     cl, byte ptr [eax]
            001C1DBF   |. |40                  |inc     eax
            001C1DC0   |. |8906                |mov     dword ptr [esi], eax
            001C1DC2   |. |8B02                |mov     eax, dword ptr [edx]
            001C1DC4   |. |0FB6C9              |movzx   ecx, cl
            001C1DC7   |. |8B0485 F8FD5100     |mov     eax, dword ptr [eax*4+0x51FDF8]
            001C1DCE   |. |0FB70C48            |movzx   ecx, word ptr [eax+ecx*2]
            001C1DD2   |. |8B07                |mov     eax, dword ptr [edi]
            001C1DD4   |. |8908                |mov     dword ptr [eax], ecx
            001C1DD6   |. |8307 04             |add     dword ptr [edi], 0x4
            001C1DD9   |> |391E                 cmp     dword ptr [esi], ebx
            001C1DDB   |.^\72 DE               \jb      short 0x1C1DBB
        --*/

        ACPToUnicodeStub = SearchPatternSafe(
                                L"8B 06 8A 08 40 89 06 8B 02 0F B6 D1 ?? ?? ?? ?? ?? ?? ?? 8B 0F 66 8B 04 50 8B 55 08 66 89 01 83 07 02 39 1E 72 DA",
                                module->DllBase,
                                module->SizeOfImage
                            );

        if (ACPToUnicodeStub == nullptr)
            ACPToUnicodeStub = SearchPatternSafe(
                                L"8B 06 8A 08 40 89 06 8B 02 0F B6 C9 ?? ?? ?? ?? ?? ?? ?? 0F B7 0C 48 8B 07 89 08 83 07 04 39 1E 72 DE",
                                module->DllBase,
                                module->SizeOfImage
                            );

        if (ACPToUnicodeStub == nullptr)
            return FALSE;
    }

    {

        /*++
          00281CE9   |.  83FE 22            cmp     esi, 0x22
          00281CEC   |.  74 7E              je      short 0x281D6C
          00281CEE   |.  83FE 23            cmp     esi, 0x23
          00281CF1   |.  74 79              je      short 0x281D6C
          00281CF3   |.  83FE 1D            cmp     esi, 0x1D
          00281CF6   |.  75 6D              jnz     short 0x281D65
          00281CF8   |.  8B4D 0C            mov     ecx, [arg.2]
        --*/

        UnicodeToACPStub = SearchPatternSafe(L"83 ?? 22 74 ?? 83 ?? 23 74 ?? 83 ?? 1D 75 ??", module->DllBase, module->SizeOfImage);
        if (UnicodeToACPStub == nullptr)
            return FALSE;

        UnicodeToACPStub = ReverseSearchFunctionHeader(UnicodeToACPStub, 0x90);
        if (UnicodeToACPStub == nullptr)
            return FALSE;
    }

    {
        IsUnicodeEncodingAddress = SearchPatternSafe(L"83 ?? 1B 76 ?? 83 ?? 1D 74 ?? 33 C0", module->DllBase, module->SizeOfImage);
        if (IsUnicodeEncodingAddress != nullptr)
            IsUnicodeEncodingAddress = ReverseSearchFunctionHeader(IsUnicodeEncodingAddress, 0x10);

        if (IsUnicodeEncodingAddress == nullptr)
            return FALSE;
    }

#endif

    PATCH_MEMORY_DATA f[] =
    {
        //FunctionCallVa(PtrAdd(ACPToUnicodeStub, 0x1C), NakedACPToUnicode_3),
        //FunctionJumpVa(UnicodeToACPStub, UnicodeToACP, &StubUnicodeToACP),
        FunctionJumpVa(CalcRegKey, StCalcRegKey),
        //FunctionJumpVa(IsUnicodeEncodingAddress, IsUnicodeEncoding, &StubIsUnicodeEncoding)
    };

    PVOID addr = StReplaceFile;
    WriteProtectMemory(CurrentProcess, PtrAdd(module->DllBase, IATLookupRoutineRVAByHashNoFix(module->DllBase, KERNEL32_ReplaceFileW)), &addr, sizeof(addr));

    PatchMemory(f, countof(f), nullptr);

    SetExeDirectoryAsCurrent();
    EnumDirectoryFiles(nullptr, L"*.*", 0, L"Data\\Packages\\User\\Fonts", nullptr, 
        [](PVOID, PWIN32_FIND_DATAW FindData, ULONG_PTR) -> LONG
        {
            AddFontResourceExW(FindData->cFileName, FR_PRIVATE, nullptr);
            return 0;
        },
        0,
        0
    );

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
