#pragma comment(linker, "/ENTRY:main")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text /MERGE:.text1=.text /SECTION:.idata,ERW")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")
#pragma comment(lib, "msi.lib")

#include "MyLibrary.cpp"
#include <comdef.h>
#include <Msi.h>

#define DebugLog(...) AllocConsole(), PrintConsole(__VA_ARGS__)

#pragma warning(push)
#pragma warning(disable:4005)
#define DebugLog(...)
#pragma warning(pop)

ML_NAMESPACE_BEGIN(MODI);

#include "MDIVWCTL.h"

BOOLEAN NTAPI EPMsoGimmeFile(ULONG Id, PWSTR Buffer, ULONG BufferCount, ULONG Flags);
PVOID NTAPI EPMsoLoadLibraryByName(PCSTR DllName);

SET_GUID(CLSID_MSPCORE_CreateImage, 0x863305F6, 0xE822, 0x4C08, 0x9b, 0xe1, 0xf1, 0xc7, 0xcf, 0xc9, 0x19, 0xaf);
SET_GUID(IID_MSPCORE_CreateImage, 0xA1943602, 0x8026, 0x4555, 0x95, 0x12, 0xdb, 0x1c, 0x2b, 0xd2, 0xca, 0x4b);

SET_GUID(CLSID_MSPCORE_OCR, 0x9D13E607, 0x106F, 0x4892, 0x8a, 0x83, 0xff, 0x98, 0x27, 0xc0, 0xa3, 0xd5);
SET_GUID(IID_MSPCORE_OCR, 0x5824B80C, 0x84C3, 0x4B51, 0x96, 0x97, 0x04, 0x22, 0x0d, 0x38, 0xd8, 0x9c);

SET_GUID(CLSID_MSPCORE_GetLayout, 0xE4425E53, 0x7859, 0x4889, 0xa3, 0xe8, 0x39, 0x00, 0x87, 0x7b, 0xb2, 0x41);
SET_GUID(IID_MSPCORE_GetLayout, 0x6FC9677E, 0x1123, 0x4F9D, 0xbf, 0x50, 0x72, 0xa4, 0x79, 0x84, 0xd6, 0x94);


API_POINTER(CoCreateInstance)               StubCoCreateInstance;
API_POINTER(LdrLoadDll)                     StubLdrLoadDll;
API_POINTER(EPMsoLoadLibraryByName)         StubEPMsoLoadLibraryByName;
API_POINTER(EPMsoGimmeFile)                 StubEPMsoGimmeFile;
API_POINTER(MsiProvideQualifiedComponentW)  StubMsiProvideQualifiedComponentW;

NTSTATUS GetSelfModulePath(ml::String &SelfPath)
{
    PLDR_MODULE     Self;
    UNICODE_STRING  SelfPathString;

    Self = FindLdrModuleByHandle(&__ImageBase);
    SelfPathString = Self->FullDllName;
    SelfPathString.Length -= Self->BaseDllName.Length;

    SelfPath = SelfPathString;

    return STATUS_SUCCESS;
}

NTSTATUS ModiGetObjectFromModule(PVOID Module, REFCLSID ClsId, REFIID IID, PVOID* Object)
{
    HRESULT                         hr;
    IClassFactory*                  factory;
    API_POINTER(DllGetClassObject)  GetClassObject;

    *(PVOID *)&GetClassObject = Ldr::GetRoutineAddress(Module, "DllGetClassObject");
    if (GetClassObject == nullptr)
        return STATUS_PROCEDURE_NOT_FOUND;

    hr = GetClassObject(ClsId, IID_IClassFactory, (PVOID *)&factory);
    FAIL_RETURN(hr);

    if (IID == IID_IClassFactory)
    {
        *Object = factory;
        return hr;
    }

    hr = factory->CreateInstance(nullptr, IID, Object);
    factory->Release();

    return hr;
}

HRESULT
NTAPI
ModiCoCreateInstance(
    LPCLSID     ClsId,
    LPUNKNOWN   UnkOuter,
    ULONG       ClsContext,
    LPIID       IID,
    PVOID*      Object
)
{
    HRESULT hr;

    if (
        (*IID == IID_MSPCORE_CreateImage    && *ClsId == CLSID_MSPCORE_CreateImage) ||
        (*IID == IID_MSPCORE_OCR            && *ClsId == CLSID_MSPCORE_OCR)         ||
        (*IID == IID_MSPCORE_GetLayout      && *ClsId == CLSID_MSPCORE_GetLayout)   ||
        FALSE
       )
    {
        hr = ModiGetObjectFromModule(
                    Ldr::FindLdrModuleByName(&USTR(L"MSPCORE.DLL"))->DllBase,
                    *ClsId,
                    *IID,
                    Object
                );

        SUCCESS_RETURN(hr);
    }

    hr = StubCoCreateInstance(*ClsId, UnkOuter, ClsContext, *IID, Object);
/*
    PrintConsole(
        L"0x%08X, 0x%04X, 0x%04X, 0x%02X, 0x%02X, 0x%02X, 0x%02X, 0x%02X, 0x%02X, 0x%02X, 0x%02X\n"
        L"0x%08X, 0x%04X, 0x%04X, 0x%02X, 0x%02X, 0x%02X, 0x%02X, 0x%02X, 0x%02X, 0x%02X, 0x%02X\n",
        ClsId->Data1, ClsId->Data2, ClsId->Data3, ClsId->Data4[0], ClsId->Data4[1], ClsId->Data4[2], ClsId->Data4[3], ClsId->Data4[4], ClsId->Data4[5], ClsId->Data4[6], ClsId->Data4[7],
        IID->Data1, IID->Data2, IID->Data3, IID->Data4[0], IID->Data4[1], IID->Data4[2], IID->Data4[3], IID->Data4[4], IID->Data4[5], IID->Data4[6], IID->Data4[7]
    );

    if (SUCCEEDED(hr))
    {
        PrintConsole(L"%wZ\n", &FindLdrModuleByHandle(**(PVOID **)Object)->FullDllName);
    }

    PrintConsole(L"\n");
*/
    return hr;
}

NTSTATUS
NTAPI
ModiLdrLoadDll(
    PWSTR               PathToFile,
    PULONG              DllCharacteristics,
    PCUNICODE_STRING    ModuleFileName,
    PVOID*              DllHandle
)
{
    NTSTATUS Status;
    UNICODE_STRING Dll;

    Dll = *ModuleFileName;

    Dll.Buffer = findnamew(Dll.Buffer);
    Dll.Length -= PtrOffset(Dll.Buffer, ModuleFileName->Buffer);

    Status = StubLdrLoadDll(PathToFile, DllCharacteristics, &Dll, DllHandle);
    SUCCESS_RETURN(Status);

    return StubLdrLoadDll(PathToFile, DllCharacteristics, ModuleFileName, DllHandle);
}

PVOID NTAPI ModiEPMsoLoadLibraryByName(PCSTR DllName)
{
    PVOID Base;
    UNICODE_STRING Dll;

    Nls::AnsiToUnicodeString(&Dll, DllName);

    Base = Ldr::LoadDll(Dll.Buffer);
    RtlFreeUnicodeString(&Dll);

    if (Base != nullptr)
        return Base;

    return StubEPMsoLoadLibraryByName(DllName);
}

BOOLEAN NTAPI ModiEPMsoGimmeFile(ULONG Id, PWSTR Buffer, ULONG BufferCount, ULONG Flags)
{
    switch (Id)
    {
        case 0x190009:
        {
            ml::String XPAGE3C;
            ULONG_PTR Length;

            GetSelfModulePath(XPAGE3C);
            XPAGE3C += LR"(MODI\MODI\12.0\XPAGE3C.DLL)";

            Length = XPAGE3C.GetCount() + 1;

            CopyMemory(Buffer, XPAGE3C.GetBuffer(), ML_MIN(Length, BufferCount) * sizeof(Buffer[0]));

            return TRUE;
        }
    }

    return StubEPMsoGimmeFile(Id, Buffer, BufferCount, Flags);
}

UINT
NTAPI
ModiMsiProvideQualifiedComponentW(
    PCWSTR  Category,
    PCWSTR  Qualifier,
    ULONG   InstallMode,
    PWSTR   PathBuffer,
    PULONG  PathBufferCount
)
{
    UNICODE_STRING CategoryString, QualifierString;

    static UNICODE_STRING MsoCategory = RTL_CONSTANT_STRING(L"{0683AB16-DB61-43C0-B0EB-CA72D348DFF5}");
    static UNICODE_STRING Components = RTL_CONSTANT_STRING(L"vUpAVS.}X%!!!!!MKKSkOCR_2052<\0");

    RtlInitUnicodeString(&CategoryString, Category);
    RtlInitUnicodeString(&QualifierString, Qualifier);

    LOOP_ONCE
    {
        if (RtlEqualUnicodeString(&CategoryString, &MsoCategory, TRUE) == FALSE)
            break;

        if (
            RtlEqualUnicodeString(&QualifierString, &USTR(L"9"), TRUE) ||
            RtlEqualUnicodeString(&QualifierString, &USTR(L"2052"), TRUE)
           )
        {
            ULONG_PTR   Length;
            ml::String  SCCODE;

            GetSelfModulePath(SCCODE);

            SCCODE += LR"(MODI\MODI\12.0\SCCODE.UNI)";

            Length = SCCODE.GetCount() + 1;
            if (PathBuffer != nullptr)
            {
                CopyMemory(PathBuffer, SCCODE.GetBuffer(), ML_MIN(Length, *PathBufferCount) * sizeof(PathBuffer[0]));
            }

            *PathBufferCount = Length;

            return ERROR_SUCCESS;
        }
    }

    return StubMsiProvideQualifiedComponentW(Category, Qualifier, InstallMode, PathBuffer, PathBufferCount);
}

NTSTATUS HookModuleIAT(PVOID Module, ULONG ApiHash, PVOID NewRoutine, PVOID* OriginalRoutine)
{
    PVOID       IAT, LocalOriginalRoutine;
    ULONG       Protect;
    NTSTATUS    Status;

    IAT = (PVOID)IATLookupRoutineRVAByHashNoFix(Module, ApiHash);
    if (IAT == (PVOID)IMAGE_INVALID_RVA)
        return STATUS_NOT_FOUND;

    IAT = PtrAdd(Module, IAT);

    Status = Mm::ProtectVirtualMemory(IAT, sizeof(IAT), PAGE_EXECUTE_READWRITE, &Protect);
    FAIL_RETURN(Status);

    LocalOriginalRoutine = _InterlockedExchangePointer(IAT, NewRoutine);

    Mm::ProtectVirtualMemory(IAT, sizeof(IAT), Protect);

    if (OriginalRoutine != nullptr)
        *OriginalRoutine = LocalOriginalRoutine;

    return STATUS_SUCCESS;
}

NTSTATUS AppendModiPathToPath(ml::String &SelfPath)
{
    PWSTR           EnvBuffer;
    ULONG           Length;
    UNICODE_STRING  Path;
    ml::String      PathEnv;

    Length = 0;
    RtlInitEmptyString(&Path);
    RtlExpandEnvironmentStrings_U(nullptr, &USTR(L"%Path%"), &Path, &Length);
    if (Length == 0)
        return STATUS_UNSUCCESSFUL;

    EnvBuffer = (PWSTR)AllocStack(Length);
    RtlInitEmptyString(&Path, EnvBuffer, Length);

    FAIL_RETURN(RtlExpandEnvironmentStrings_U(nullptr, &USTR(L"%Path%"), &Path, nullptr));

    PathEnv = SelfPath + L"MODI\\MODI\\12.0;";
    PathEnv += SelfPath + L"MODI\\OFFICE12;";
    PathEnv += Path;

    return RtlSetEnvironmentVariable(nullptr, &USTR(L"Path"), PathEnv);
}

NTSTATUS InitializeModi()
{
    PVOID           MSPCORE, MDIVWCTL, MSPGIMME;
    ml::String      SelfPath;
    UNICODE_STRING  WorkingDirectory;

    GetSelfModulePath(SelfPath);
    AppendModiPathToPath(SelfPath);

    GetWorkingDirectory(&WorkingDirectory);
    SetWorkingDirectory((PUNICODE_STRING)(SelfPath + L"MODI\\MODI\\12.0\\"));

    MDIVWCTL = Ldr::LoadDll(L"MDIVWCTL.DLL");
    MSPGIMME = Ldr::LoadDll(L"MSPGIMME.DLL");
    MSPCORE = Ldr::LoadDll(L"MSPCORE.DLL");

    SetWorkingDirectory(&WorkingDirectory);
    RtlFreeUnicodeString(&WorkingDirectory);

    if (MDIVWCTL == nullptr || MSPGIMME == nullptr || MSPCORE == nullptr)
    {
        Ldr::UnloadDll(MDIVWCTL);
        Ldr::UnloadDll(MSPGIMME);
        Ldr::UnloadDll(MSPCORE);

        return STATUS_DLL_NOT_FOUND;
    }

    MEMORY_FUNCTION_PATCH f[] =
    {
        INLINE_HOOK_JUMP(CoCreateInstance,              ModiCoCreateInstance,   StubCoCreateInstance),
        INLINE_HOOK_JUMP(LdrLoadDll,                    ModiLdrLoadDll,         StubLdrLoadDll),
        INLINE_HOOK_JUMP(MsiProvideQualifiedComponentW, ModiMsiProvideQualifiedComponentW,  StubMsiProvideQualifiedComponentW),

        EAT_HOOK_JUMP(MSPGIMME, "EPMsoLoadLibraryByName",   ModiEPMsoLoadLibraryByName, StubEPMsoLoadLibraryByName),
        EAT_HOOK_JUMP(MSPGIMME, "EPMsoGimmeFile",           ModiEPMsoGimmeFile,         StubEPMsoGimmeFile),
    };

    Nt_PatchMemory(0, 0, f, countof(f));

    CoInitialize(nullptr);

    return STATUS_SUCCESS;
}

NTSTATUS UnInitializeModi()
{
    CoUninitialize();
    return STATUS_SUCCESS;
}

NTSTATUS OcrTiff(PCWSTR TiffFile, ml::String &ResultText)
{
    PVOID               MDIVWCTL;
    HRESULT             hr;
    BSTR                tif, text;
    IClassFactory*      factory;
    MODI::IDocument*    doc;
    MODI::IImages*      imgs;
    MODI::IImage*       img;
    MODI::ILayout*      layout;
    MODI::IWords*       words;
    MODI::IWord*        word;
    LONG                wordcount;

    factory = nullptr;
    doc     = nullptr;
    imgs    = nullptr;
    img     = nullptr;
    layout  = nullptr;
    words   = nullptr;
    word    = nullptr;

    ResultText = L"";

    LOOP_ONCE
    {
        hr = ModiGetObjectFromModule(
                FindLdrModuleByName(&USTR(L"MDIVWCTL.DLL"))->DllBase,
                MODI::CLSID_Document,
                IID_IDocument,
                (PVOID *)&doc
            );

        FAIL_BREAK(hr);

        tif = SysAllocString(TiffFile);
        hr = doc->Create(tif);
        SysFreeString(tif);
        FAIL_BREAK(hr);

        DebugLog(L"ocr\n");

        hr = doc->OCR(MODI::miLANG_CHINESE_SIMPLIFIED, TRUE, TRUE);
        FAIL_BREAK(hr);

        DebugLog(L"get_Images\n");

        hr = doc->get_Images(&imgs);
        FAIL_BREAK(hr);

        imgs->get_Count(&wordcount);
        DebugLog(L"imgs count = %d\n", wordcount);

        DebugLog(L"imgs->get_Item\n");

        hr = imgs->get_Item(0, (IDispatch**)&img);
        FAIL_BREAK(hr);

        DebugLog(L"img->get_Layout\n");

        hr = img->get_Layout(&layout);
        FAIL_BREAK(hr);

        DebugLog(L"layout->get_Words\n");

        hr = layout->get_Words(&words);
        FAIL_BREAK(hr);

        DebugLog(L"words->get_Count\n");

        hr = words->get_Count(&wordcount);
        FAIL_BREAK(hr);

        DebugLog(L"loop\n");

        for (LONG_PTR Index = 0; Index != wordcount; ++Index)
        {
            hr = words->get_Item(Index, (IDispatch **)&word);
            FAIL_BREAK(hr);

            hr = word->get_Text(&text);
            FAIL_BREAK(hr);

            ResultText += text;
            SysFreeString(text);

            SafeReleaseT(word);
        }

        FAIL_BREAK(hr);
    }

    SafeReleaseT(factory);
    SafeReleaseT(doc);
    SafeReleaseT(imgs);
    SafeReleaseT(img);
    SafeReleaseT(layout);
    SafeReleaseT(words);
    SafeReleaseT(word);

    return hr;
}

ML_NAMESPACE_END_(MODI)

ForceInline Void main2(LongPtr argc, TChar **argv)
{
    ml::MlInitialize();

    //ExceptionBox(ml::String::Format(L"%p, %p", CurrentPeb()->ProcessParameters->StandardOutput, GetStdHandle(STD_OUTPUT_HANDLE)));

    if (argc < 2)
    {
        return;
    }

    NTSTATUS Status;

    Status = MODI::InitializeModi();
    if (NT_FAILED(Status))
    {
        return;
    }

    ml::String ret;

    if (argc > 2)
    {
        WCHAR Tiff[0x1000];
        HANDLE StandardIntput, StandardError, ParentProcess;
        LARGE_INTEGER BytesRead, Timeout;

        StandardIntput = CurrentPeb()->ProcessParameters->StandardInput;
        StandardError = CurrentPeb()->ProcessParameters->StandardError;

        FormatTimeOut(&Timeout, 1);

        ParentProcess = PidToHandle(StringToInt64W(argv[1]));

        LOOP_FOREVER
        {
            if (ParentProcess != nullptr)
            {
                Status = NtWaitForSingleObject(ParentProcess, FALSE, &Timeout);
                if (Status != STATUS_TIMEOUT)
                {
                    NtClose(ParentProcess);
                    break;
                }
            }

            Status = NtFileDisk::Read(StandardIntput, Tiff, sizeof(Tiff), &BytesRead);
            if (NT_FAILED(Status))
            {
                Ps::Sleep(1);
                continue;
            }

            *PtrAdd(Tiff, BytesRead.QuadPart) = 0;

            Status = MODI::OcrTiff(Tiff, ret);

            BytesRead.QuadPart = ret.GetSize();
            NtFileDisk::Write(StandardError, &BytesRead.QuadPart, 8);
            if (BytesRead.QuadPart != 0)
                NtFileDisk::Write(StandardError, ret.GetBuffer(), BytesRead.QuadPart);
        }
    }
    else
    {
        MODI::OcrTiff(argv[1], ret);
        PrintConsole(L"%s", ret);
    }

    MODI::UnInitializeModi();

    return;
}

int __cdecl main(LONG_PTR argc, PWSTR *argv)
{
    getargsW(&argc, &argv);
    main2(argc, argv);
    ReleaseArgv(argv);
    Ps::ExitProcess(0);
}
