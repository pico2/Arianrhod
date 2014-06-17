#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text /MERGE:.text1=.text /SECTION:.idata,ERW")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")
#pragma comment(linker, "/EXPORT:CharNextExA=USER32.CharNextExA")

#include "MyLibrary.cpp"

Void AnsiWin32FindDataToUnicode(LPWIN32_FIND_DATAW pwfdW, LPWIN32_FIND_DATAA pwfdA)
{
    pwfdA->dwFileAttributes = pwfdW->dwFileAttributes;
    pwfdA->ftCreationTime   = pwfdW->ftCreationTime;
    pwfdA->ftLastAccessTime = pwfdW->ftLastAccessTime;
    pwfdA->ftLastWriteTime  = pwfdW->ftLastWriteTime;
    pwfdA->nFileSizeHigh    = pwfdW->nFileSizeHigh;
    pwfdA->nFileSizeLow     = pwfdW->nFileSizeLow;
    pwfdA->dwReserved0      = pwfdW->dwReserved0;
    pwfdA->dwReserved1      = pwfdW->dwReserved1;

    WideCharToMultiByte(CP_ACP, 0, pwfdW->cFileName, -1, pwfdA->cFileName, sizeof(pwfdA->cFileName), 0, 0);
}

HANDLE NTAPI CabFindFirstFileA(PCSTR FileName, PWIN32_FIND_DATAA FindFileData)
{
    HANDLE find;
    UNICODE_STRING name;
    WIN32_FIND_DATAW fd;

    AnsiToUnicodeString(&name, FileName);

    find = FindFirstFileW(name.Buffer, &fd);
    RtlFreeUnicodeString(&name);

    if (find == INVALID_HANDLE_VALUE)
        return find;

    FindFileData->dwFileAttributes  = fd.dwFileAttributes;
    FindFileData->ftCreationTime    = fd.ftCreationTime;
    FindFileData->ftLastAccessTime  = fd.ftLastAccessTime;
    FindFileData->ftLastWriteTime   = fd.ftLastWriteTime;
    FindFileData->nFileSizeHigh     = fd.nFileSizeHigh;
    FindFileData->nFileSizeLow      = fd.nFileSizeLow;
    FindFileData->dwReserved0       = fd.dwReserved0;
    FindFileData->dwReserved1       = fd.dwReserved1;

    UnicodeToAnsi(FindFileData->cFileName, sizeof(FindFileData->cFileName), fd.cFileName);
    UnicodeToAnsi(FindFileData->cAlternateFileName, sizeof(FindFileData->cAlternateFileName), fd.cAlternateFileName);

    return find;
}

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    LdrDisableThreadCalloutsForDll(BaseAddress);
    ml::MlInitialize();

    Mp::PATCH_MEMORY_DATA p[] =
    {
        Mp::FunctionJumpVa(LookupExportTable(LoadDll(L"KERNELBASE.dll"), KERNEL32_FindFirstFileA), CabFindFirstFileA),
    };

    Mp::PatchMemory(p, countof(p));

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
