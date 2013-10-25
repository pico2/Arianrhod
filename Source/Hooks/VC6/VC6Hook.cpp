#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")

#include "MyLibrary.cpp"


VOID FASTCALL WriteLinkerTempFile(PVOID This, PVOID, PSTR Text)
{
    PWSTR Unicode;
    ULONG  Length;
    FILE  *fp;

    Length = StrLengthA(Text);
    if (*(PULONG)Text == TAG4('@ech'))
    {
        Unicode = (PWSTR)Text;
    }
    else
    {
        Unicode = (PWSTR)AllocStack(Length * 2 + 2);
        *(PUSHORT)Unicode = BOM_UTF16_LE;
        Length = MultiByteToWideChar(CP_GB2312, 0, Text, Length, Unicode + 1, Length);
        Length = Length * 2 + 2;
    }

    fp = *(PTR_OF(fp))PtrAdd(This, 0x10);
    _setmode(_fileno(fp), _O_BINARY);
    fwrite(Unicode, Length, 1, fp);
}

VOID FASTCALL DelayInitialize(PVOID devshl)
{
    MEMORY_FUNCTION_PATCH f[] =
    {
        INLINE_HOOK_CALL_RVA_NULL(0xE160, WriteLinkerTempFile),
    };

    Nt_PatchMemory(NULL, 0, f, countof(f), devshl);
}

ASM VOID LoadDevBldFinished()
{
    INLINE_ASM
    {
        mov  ecx, [esp + 4];
        push eax;
        call DelayInitialize
        pop  eax;
        test eax, eax;
        ret  0x10;
    }
}

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    setlocale(LC_ALL, ".936");

    PLDR_MODULE devshl;

    MEMORY_FUNCTION_PATCH f[] =
    {
        INLINE_HOOK_CALL_RVA_NULL(0x380DB, LoadDevBldFinished),
    };

    devshl = FindLdrModuleByHandle(L"devshl.dll");

    Nt_PatchMemory(NULL, 0, f, countof(f), devshl->DllBase);

    PVOID mfc42 = Ldr::LoadDll(L"MFC42.dll");

    PVOID mbscmp = PtrAdd(mfc42, IATLookupRoutineRVAByHashNoFix(mfc42, CONST_STRHASH("_mbscmp")));
    PVOID orig;

    orig = EATLookupRoutineByHashPNoFix(Ldr::LoadDll(L"msvcrt.dll"), CONST_STRHASH("_mbscmp"));

    Mm::WriteProtectMemory(CurrentProcess, mbscmp, &orig, sizeof(orig));

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
