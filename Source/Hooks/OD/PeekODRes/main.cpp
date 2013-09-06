#pragma comment(linker,"/ENTRY:main")
#pragma comment(linker,"/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker,"/SECTION:.Amano,ERW /MERGE:.text=.Amano")

#include <Windows.h>
#include "my_headers.h"
#include "Mem.cpp"

DWORD ProcessPrototype(LPCWSTR lpFileName)
{
    CMem  mem;
    PBYTE pbTextOffset, pbText;
    DWORD IndexSize, TextSize;
    PDWORD pOffset;
    LPSTR  lpFuncName, lpParameter;
    CFileDisk file;
    WCHAR szFile[0x10000];

    lstrcpyW(szFile, lpFileName);
    rmextw(szFile);
    lstrcatW(szFile, L".index");
    if (!file.Open(szFile))
        return 0;

    IndexSize = file.GetSize();
    pbTextOffset = (PBYTE)mem.Alloc(IndexSize);
    if (pbTextOffset == NULL)
        return 0;

    file.Read(pbTextOffset);

    rmextw(szFile);
    lstrcatW(szFile, L".text");
    if (!file.Open(szFile))
    {
        mem.Free(pbTextOffset);
        return 0;
    }

    TextSize = file.GetSize();
    pbText = (PBYTE)mem.Alloc(TextSize);
    if (pbText == NULL)
    {
        mem.Free(pbTextOffset);
        return 0;
    }

    file.Read(pbText);

    rmextw(szFile);
    lstrcatW(szFile, L".txt");
    if (file.Create(szFile))
    {

        TextSize = BOM_UTF16_LE;
        file.Write(&TextSize, 2);
        pOffset = (PDWORD)pbTextOffset;
        for (DWORD Index = IndexSize / sizeof(Index); Index; --Index)
        {
            LPWSTR lpBuffer = szFile;

            lpFuncName = (LPSTR)((ULONG_PTR)pbText + *pOffset++);
            lpParameter = lpFuncName + StrLengthA(lpFuncName) + 2;

            lpBuffer += MultiByteToWideChar(CP_ACP, 0, lpFuncName, -1, lpBuffer, countof(szFile) - (lpBuffer - szFile));
            lpBuffer[-1] = ':';
            lpBuffer += MultiByteToWideChar(CP_ACP, 0, lpParameter, -1, lpBuffer, countof(szFile) - (lpBuffer - szFile));
            *(PUINT32)&lpBuffer[-1] = TAG2W('\n\r');
            ++lpBuffer;
            if (!file.Write(szFile, ((ULONG_PTR)lpBuffer - (ULONG_PTR)szFile)))
                break;
        }
    }

    mem.Free(pbTextOffset);
    mem.Free(pbText);

    return IndexSize / sizeof(IndexSize);
}

DWORD ProcessFlags(LPCWSTR lpFileName)
{
    CMem  mem;
    PBYTE pbTextOffset, pbText;
    DWORD IndexSize, TextSize;
    PDWORD pOffset;
    LPSTR  lpText;
    CFileDisk file;
    WCHAR szFile[0x10000];

    lstrcpyW(szFile, lpFileName);
    rmextw(szFile);
    lstrcatW(szFile, L".index");
    if (!file.Open(szFile))
        return 0;

    IndexSize = file.GetSize();
    pbTextOffset = (PBYTE)mem.Alloc(IndexSize);
    if (pbTextOffset == NULL)
        return 0;

    file.Read(pbTextOffset);

    rmextw(szFile);
    lstrcatW(szFile, L".text");
    if (!file.Open(szFile))
    {
        mem.Free(pbTextOffset);
        return 0;
    }

    TextSize = file.GetSize();
    pbText = (PBYTE)mem.Alloc(TextSize);
    if (pbText == NULL)
    {
        mem.Free(pbTextOffset);
        return 0;
    }

    file.Read(pbText);

    rmextw(szFile);
    lstrcatW(szFile, L".txt");
    if (file.Create(szFile))
    {
        TextSize = BOM_UTF16_LE;
        file.Write(&TextSize, 2);
        pOffset = (PDWORD)pbTextOffset;
        for (DWORD Index = IndexSize / sizeof(Index); Index; --Index)
        {
            LPWSTR lpBuffer;
            DWORD Length, ch;
            enum
            {
                BYTE_CODE_FLAG      = 0x07,
                BYTE_CODE_FLAG2     = 0x0F,
                BYTE_CODE_NOP       = 0x1A,
                BYTE_CODE_SKIP_TEXT = 0x0A,
            };

            lpText = (LPSTR)((ULONG_PTR)pbText + *pOffset++);

            lpBuffer = szFile;
            lpBuffer += swprintf(lpBuffer, L"@Flags=", lpText);
            lpBuffer += MultiByteToWideChar(CP_ACP, 0, lpText, -1, lpBuffer, countof(szFile) - (lpBuffer - szFile));
            --lpBuffer;
            lpBuffer += swprintf(lpBuffer, L"\r\n");
            lpText += StrLengthA(lpText) + 1;
            while (*lpText)
            {
                Length = 0;
                switch (ch = *lpText)
                {
                    case 0x07:
                    case 0x0F:
                    case 0x10:
                        Length = swprintf(lpBuffer, L"%02X,%08X,", *(PUINT8)lpText, *(PUINT32)&lpText[1]);
                        lpBuffer += Length;
                        lpBuffer += MultiByteToWideChar(CP_ACP, 0, lpText + 5, -1, lpBuffer, countof(szFile) - (lpBuffer - szFile));
                        --lpBuffer;
                        Length = swprintf(lpBuffer, L"\r\n");
                        lpText += StrLengthA(lpText + 5) + 1 + 5;
                        break;
/*
                    case 0x02:
                        lpText += 5;
                        break;
*/
                    case 0x01:
                    case 0x17:
                    case 0x0A:
//                        Length = wsprintfA(lpBuffer, "%02X,%s\r\n", *(PUINT8)lpText, lpText + 1);
                        lpBuffer += swprintf(lpBuffer, L"%02X,", *(PUINT8)lpText);
                        lpBuffer += MultiByteToWideChar(CP_ACP, 0, lpText + 1, -1, lpBuffer, countof(szFile) - (lpBuffer - szFile));
                        --lpBuffer;
                        Length = swprintf(lpBuffer, L"\r\n");
                        lpText += StrLengthA(lpText + 1) + 1 + 1;
                        break;
/*
                    case 0x0A:
                    case 0x10:
                        lpText += 5;
                        lpText += StrLengthA(lpText) + 1;
                        break;
*/
                    case 0x04: case 0x05: case 0x06: case 0x08:
                    case 0x09: case 0x0B: case 0x0C: case 0x0D:
                    case 0x0E: /*case 0x11: */case 0x12: case 0x13:
                    case 0x14: case 0x15: case 0x16: case 0x18:
                    case 0x1A:
                        Length = swprintf(lpBuffer, L"%02X\r\n", *(PUINT8)lpText);
                        ++lpText;
                        break;

                    case 0x02:
                    case 0x03:
                    case 0x11:
                    case 0x19:
                        Length = swprintf(lpBuffer, L"%02X,%08X\r\n", *(PUINT8)lpText, *(PUINT32)&lpText[1]);
                        NO_BREAK;
//                    case 0x11:
                        lpText += 1 + 4;
                        break;

                    default:
                        printf("%02X @ %p: unknown byte code, attach me please\n", ch, lpText);
                        getch();
                }

                lpBuffer += Length;
            }

            if (lpBuffer != szFile)
                lpBuffer += swprintf(lpBuffer, L"@End\r\n\r\n");

            if (!file.Write(szFile, (lpBuffer - szFile) * 2))
                break;
        }
    }

    mem.Free(pbTextOffset);
    mem.Free(pbText);

    return IndexSize / sizeof(IndexSize);
}

DWORD ProcessErrorCodeAndExceptions(LPCWSTR lpFileName)
{
    CMem  mem;
    PBYTE pbTextOffset, pbText;
    DWORD IndexSize, TextSize;
    LPSTR  lpName;
    CFileDisk file;
    WCHAR szFile[0x2000];
    struct _tagErrorCodeIndex
    {
        UINT32 Value;
        UINT32 Offset;
    } *pErrorCodeIndex;

    lstrcpyW(szFile, lpFileName);
    rmextw(szFile);
    lstrcatW(szFile, L".index");
    if (!file.Open(szFile))
        return 0;

    IndexSize = file.GetSize();
    pbTextOffset = (PBYTE)mem.Alloc(IndexSize);
    if (pbTextOffset == NULL)
        return 0;

    file.Read(pbTextOffset);

    rmextw(szFile);
    lstrcatW(szFile, L".text");
    if (!file.Open(szFile))
    {
        mem.Free(pbTextOffset);
        return 0;
    }

    TextSize = file.GetSize();
    pbText = (PBYTE)mem.Alloc(TextSize);
    if (pbText == NULL)
    {
        mem.Free(pbTextOffset);
        return 0;
    }

    file.Read(pbText);

    rmextw(szFile);
    lstrcatW(szFile, L".txt");
    if (file.Create(szFile))
    {
        TextSize = BOM_UTF16_LE;
        file.Write(&TextSize, 2);
        pErrorCodeIndex = (struct _tagErrorCodeIndex *)pbTextOffset;
        for (DWORD Index = IndexSize / sizeof(*pErrorCodeIndex); Index; --Index)
        {
            LPWSTR lpBuffer = szFile;

            lpName = (LPSTR)((ULONG_PTR)pbText + pErrorCodeIndex->Offset);

            lpBuffer += MultiByteToWideChar(CP_ACP, 0, lpName, -1, lpBuffer, countof(szFile) - (lpBuffer - szFile));
            lpBuffer[-1] = '=';
            lpBuffer += swprintf(lpBuffer, L"%08X\r\n", pErrorCodeIndex->Value);
            if (!file.Write(szFile, ((ULONG_PTR)lpBuffer - (ULONG_PTR)szFile)))
                break;

            ++pErrorCodeIndex;
        }
    }

    mem.Free(pbTextOffset);
    mem.Free(pbText);

    return IndexSize / sizeof(IndexSize);
}

ForceInline Void main2(Int argc, WChar **argv)
{
    if (argc-- == 1)
        return;
    do
    {
        LPCWSTR lpPath = *++argv;
        LPCWSTR lpFileName = findnamew(lpPath);

        if (!StrNICompareW(lpFileName, L"RES_KNOWN_PROTOTYPE", 19))
            ProcessPrototype(lpPath);
        else if (!StrNICompareW(lpFileName, L"RES_KNOWN_FLAG", 14))
            ProcessFlags(lpPath);
        else if (!StrNICompareW(lpFileName, L"RES_EXCEPTNS", 12))
            ProcessErrorCodeAndExceptions(lpPath);
        else if (!StrNICompareW(lpFileName, L"RES_ERRCODE", 11))
            ProcessErrorCodeAndExceptions(lpPath);
        else if (!StrNICompareW(lpFileName, L"RES_VXD", 7))
            ProcessErrorCodeAndExceptions(lpPath);

    } while (--argc);
}

void __cdecl main(Int argc, WChar **argv)
{
    getargsW(&argc, &argv);
    main2(argc, argv);
    exit(0);
}