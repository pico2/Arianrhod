#pragma comment(linker, "/ENTRY:main")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text /MERGE:.text1=.text /SECTION:.idata,ERW")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")
#pragma comment(lib, "Shlwapi.lib")

#include <MyLibrary.cpp>

Void GetRandomName(IN OUT LPWSTR lpFileName)
{
    LPWSTR lpName = findnamew(lpFileName);

    do
    {
        swprintf(lpName, L"%X%X.%X", GetRandom32(), GetRandom32(), GetRandom32());
    } while (GetFileAttributesW(lpFileName) != -1);
}

Void _DeleteFile(LPWSTR lpFileName)
{
    DWORD  dwSize, dwWritten;
    HANDLE hFile, hMap, hHeap;
    PBYTE  pbFile, pbBuffer;
    WCHAR  szTempName[MAX_PATH];

    wprintf(L"Deleting \"%s\" ... ", lpFileName);
    hHeap = GetProcessHeap();
//    SetFileAttributesW(lpFileName, FILE_ATTRIBUTE_NORMAL);
    hFile = CreateFileW(lpFileName,
        GENERIC_READ|GENERIC_WRITE|FILE_ALL_ACCESS,
        0,
        NULL,
        OPEN_EXISTING,
        FILE_ATTRIBUTE_NORMAL|FILE_ATTRIBUTE_HIDDEN|FILE_ATTRIBUTE_SYSTEM|FILE_FLAG_WRITE_THROUGH,
        NULL);
    if (hFile == INVALID_HANDLE_VALUE)
    {
        printf("failed\n");
        return;
    }

    dwSize = GetFileSize(hFile, NULL);
    if (dwSize) if (dwSize < 30 * 1024 * 1024)
    {
        pbBuffer = (PBYTE)HeapAlloc(hHeap, 0, dwSize);
        memset(pbBuffer, -1, dwSize);
        WriteFile(hFile, pbBuffer, dwSize, &dwWritten, NULL);
        HeapFree(hHeap, 0, pbBuffer);
        FlushFileBuffers(hFile);
    }
    else
    {
        hMap = CreateFileMappingW(hFile, NULL, PAGE_READWRITE, 0, dwSize, NULL);
        if (hMap)
        {
            if (dwSize > 100 * 1024 * 1024)
            {
                //dwSize = 100 * 1024 * 1024;
            }

            pbFile = (PBYTE)MapViewOfFile(hMap, FILE_MAP_WRITE, 0, 0, dwSize);
            CloseHandle(hMap);
            if (pbFile)
            {
                memset(pbFile, -1, dwSize);
                UnmapViewOfFile(pbFile);
                FlushFileBuffers(hFile);
            }
        }
    }
    CloseHandle(hFile);

    lstrcpyW(szTempName, lpFileName);
    GetRandomName(szTempName);
    lpFileName = MoveFileExW(lpFileName, szTempName, 0) ? szTempName : lpFileName;
    printf("%s\n", DeleteFileW(lpFileName) ? "OK" : "failed");
}

Void DeleteFolder(LPWSTR lpPath, LPWIN32_FIND_DATAW pWfd)
{
    LPWSTR lpEnd;
    HANDLE hFind;

    if (GetFileAttributesW(lpPath) == -1)
        return;

    lpEnd = lpPath + lstrlenW(lpPath);
    lstrcpyW(lpEnd, L"\\*.*");

    hFind = FindFirstFileW(lpPath, pWfd);
    if (hFind != INVALID_HANDLE_VALUE)
    {
        do
        {
            if (!lstrcmpW(pWfd->cFileName, L".") || !lstrcmpW(pWfd->cFileName, L".."))
                continue;

            lstrcpyW(lpEnd + 1, pWfd->cFileName);
            if (pWfd->dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY)
            {
                DeleteFolder(lpPath, pWfd);
            }
            else
            {
                _DeleteFile(lpPath);
            }
        } while (FindNextFileW(hFind, pWfd));
        FindClose(hFind);
    }

    *lpEnd = 0;
    lstrcpyW(pWfd->cFileName, lpPath);
    GetRandomName(pWfd->cFileName);
    lpEnd = MoveFileExW(lpPath, pWfd->cFileName, 0) ? pWfd->cFileName : lpPath;
    wprintf(L"Removing \"%s\" ... ", lpPath);
    printf("%s\n", RemoveDirectoryW(lpEnd) ? "OK" : "failed");
}

void ForceInline main2(int argc, wchar_t **argv)
{
    LPWSTR lpFileName;
    WCHAR  szPath[MAX_PATH];
    HANDLE hFind;
    WIN32_FIND_DATAW wfd;

    setlocale(LC_CTYPE, "");
    for (int i = 1; i != argc; ++i)
    {
        hFind = FindFirstFileW(argv[i], &wfd);
        if (hFind == INVALID_HANDLE_VALUE)
            continue;

        lstrcpyW(szPath, argv[i]);
        lpFileName = findnamew(szPath);

        do
        {
            if (!lstrcmpW(wfd.cFileName, L".") || !lstrcmpW(wfd.cFileName, L".."))
                continue;

            lstrcpyW(lpFileName, wfd.cFileName);

            if (wfd.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY)
                DeleteFolder(szPath, &wfd);
            else
                _DeleteFile(szPath);
        } while (FindNextFileW(hFind, &wfd));

        FindClose(hFind);
    }
}

int __cdecl main(LONG_PTR argc, PWSTR *argv)
{
    getargsW(&argc, &argv);
    main2(argc, argv);
    ReleaseArgv(argv);
    Ps::ExitProcess(0);
}
