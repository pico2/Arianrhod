#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")

#pragma comment(linker, "/EXPORT:CreateXmlReader=_VaxCreateXmlReader@0")
#pragma comment(linker, "/EXPORT:CreateXmlReaderInputWithEncodingCodePage=_VaxCreateXmlReaderInputWithEncodingCodePage@0")
#pragma comment(linker, "/EXPORT:CreateXmlReaderInputWithEncodingName=_VaxCreateXmlReaderInputWithEncodingName@0")
#pragma comment(linker, "/EXPORT:CreateXmlWriter=_VaxCreateXmlWriter@0")
#pragma comment(linker, "/EXPORT:CreateXmlWriterOutputWithEncodingCodePage=_VaxCreateXmlWriterOutputWithEncodingCodePage@0")
#pragma comment(linker, "/EXPORT:CreateXmlWriterOutputWithEncodingName=_VaxCreateXmlWriterOutputWithEncodingName@0")

#include "ml.cpp"

using ml::String;

ML_OVERLOAD_NEW

API_POINTER(RtlGetFrame) StubCreateXmlReader;
API_POINTER(RtlGetFrame) StubCreateXmlReaderInputWithEncodingCodePage;
API_POINTER(RtlGetFrame) StubCreateXmlReaderInputWithEncodingName;
API_POINTER(RtlGetFrame) StubCreateXmlWriter;
API_POINTER(RtlGetFrame) StubCreateXmlWriterOutputWithEncodingCodePage;
API_POINTER(RtlGetFrame) StubCreateXmlWriterOutputWithEncodingName;

EXTC PVOID NTAPI VaxCreateXmlReader()
{
    return StubCreateXmlReader();
}

EXTC PVOID NTAPI VaxCreateXmlReaderInputWithEncodingCodePage()
{
    return StubCreateXmlReaderInputWithEncodingCodePage();
}

EXTC PVOID NTAPI VaxCreateXmlReaderInputWithEncodingName()
{
    return StubCreateXmlReaderInputWithEncodingName();
}

EXTC PVOID NTAPI VaxCreateXmlWriter()
{
    return StubCreateXmlWriter();
}

EXTC PVOID NTAPI VaxCreateXmlWriterOutputWithEncodingCodePage()
{
    return StubCreateXmlWriterOutputWithEncodingCodePage();
}

EXTC PVOID NTAPI VaxCreateXmlWriterOutputWithEncodingName()
{
    return StubCreateXmlWriterOutputWithEncodingName();
}

VOID VaxInitialize2(PLDR_MODULE vax, BOOL Force = FALSE);

BOOL NTAPI VaxDllMain(PVOID BaseAddress, ULONG Reason, PVOID Reserved)
{
    BOOL Success;
    PLDR_MODULE Self;
    PIMAGE_NT_HEADERS NtHeaders;

    Self = FindLdrModuleByHandle(BaseAddress);
    NtHeaders = ImageNtHeadersFast(BaseAddress);
    Self->EntryPoint = PtrAdd(BaseAddress, NtHeaders->OptionalHeader.AddressOfEntryPoint);

    Success = ((API_POINTER(VaxDllMain))Self->EntryPoint)(BaseAddress, Reason, Reserved);

    VaxInitialize2(Self, TRUE);

    return Success;
}

API_POINTER(LoadLibraryA) StubLoadLibraryA;

PVOID NTAPI VaxLoadLibraryA(PCSTR DllPath)
{
    static CHAR VaxDll[] = "VA_X.dll";

    ULONG_PTR Length;
    PVOID Base;

    Base = StubLoadLibraryA(DllPath);
    if (Base == nullptr)
        return Base;

    Length = StrLengthA(DllPath);
    if (Length < CONST_STRLEN(VaxDll))
        return Base;

    if (StrICompareA(VaxDll, &DllPath[Length - CONST_STRLEN(VaxDll)]) != 0)
        return Base;

    VaxInitialize2(FindLdrModuleByHandle(Base));

    return Base;
}

LONG CDECL GetRegistrationType(PVOID p1, PVOID p2)
{
    return 0;
}

VOID VaxInitialize2(PLDR_MODULE vax, BOOL Force)
{
    using namespace Mp;

    if (Force == FALSE && FLAG_OFF(vax->Flags, LDRP_PROCESS_ATTACH_CALLED))
    {
        vax->EntryPoint = VaxDllMain;
        return;
    }

    // 1F159673     B8 E0070000          mov     eax, 0x7E0
    // 1F159678     66:3BC8              cmp     cx, ax
    // 1F15967B     76 0C                jbe     short 0x1F159689
    // 1F15967D     B9 DA070000          mov     ecx, 0x7DA
    //
    // mov     r32, const
    // cmp     r16, r16
    // jbe     short const
    // mov     r32, const


    PVOID Target = nullptr;

    LOOP_ONCE
    {
        Target = SearchPatternSafe(
                    L"B8 ?? 07 00 00 66 3B C8 76 0C B9 DA 07 00 00",
                    vax->DllBase,
                    vax->SizeOfImage
                );
        if (Target == nullptr)
            break;

        Target = ReverseSearchFunctionHeader(Target, 0x30);
        if (Target == nullptr)
            break;

        PATCH_MEMORY_DATA p[] =
        {
            Mp::FunctionJumpVa(Target, GetRegistrationType),
        };

        PatchMemory(p, countof(p));
    }

    if (Target == nullptr)
    {
        AllocConsole();
        PrintConsole(L"Can't find sig\n");
        return;
    }
}

VOID VaxInitialize()
{
    using namespace Mp;

    PLDR_MODULE vax;

    vax = FindLdrModuleByName(&USTR(L"VA_X.dll"));
    if (vax != nullptr)
    {
        VaxInitialize2(vax);
        return;
    }

    PATCH_MEMORY_DATA p[] =
    {
        Mp::FunctionJumpVa(LookupExportTable(GetKernel32Handle(), KERNEL32_LoadLibraryA), VaxLoadLibraryA, &StubLoadLibraryA),
    };

    PatchMemory(p, countof(p));
}

VOID XmlLiteInitialize()
{
    static PCSTR Names[] =
    {
        "CreateXmlReader",
        "CreateXmlReaderInputWithEncodingCodePage",
        "CreateXmlReaderInputWithEncodingName",
        "CreateXmlWriter",
        "CreateXmlWriterOutputWithEncodingCodePage",
        "CreateXmlWriterOutputWithEncodingName",
    };

    PVOID *Routines[] =
    {
        (PVOID *)&StubCreateXmlReader,
        (PVOID *)&StubCreateXmlReaderInputWithEncodingCodePage,
        (PVOID *)&StubCreateXmlReaderInputWithEncodingName,
        (PVOID *)&StubCreateXmlWriter,
        (PVOID *)&StubCreateXmlWriterOutputWithEncodingCodePage,
        (PVOID *)&StubCreateXmlWriterOutputWithEncodingName,
    };

    PVOID           module;
    NTSTATUS        Status;
    PLDR_MODULE     Self, Netapi32;
    UNICODE_STRING  SystemRoot;

    if (StubCreateXmlReader != nullptr)
        return;

    Status = Rtl::GetSystemDirectory(&SystemRoot);
    if (NT_FAILED(Status))
        return;

    module = Ldr::LoadDll(String(SystemRoot) + L"xmllite.dll");
    RtlFreeUnicodeString(&SystemRoot);

    LdrAddRefDll(LDR_ADDREF_DLL_PIN, module);

    for (LONG_PTR i = 0; i != countof(Names); ++i)
    {
        *Routines[i] = GetRoutineAddress(module, Names[i]);
    }
}

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    LdrDisableThreadCalloutsForDll(BaseAddress);
    ml::MlInitialize();

    VaxInitialize();
    XmlLiteInitialize();

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