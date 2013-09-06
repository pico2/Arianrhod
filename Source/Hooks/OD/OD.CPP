#pragma comment(linker,"/ENTRY:DllMain")
#pragma comment(linker,"/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker,"/SECTION:.Amano,ERW /MERGE:.text=.Amano")
#pragma comment(lib, "ollydbg.lib")
#pragma comment(lib, "psapi.lib")

#include "OD.h"
#include "AntiDbgSysCallDbgee.h"
#include "AntiDbgSysCallDbger.h"
#include <Psapi.h>

#include "MyLibrary.cpp"
#include "HookPort.cpp"

OVERLOAD_CPP_NEW_WITH_HEAP(MemoryAllocator::GetGlobalHeap())

POD_HOOK_INFO g_Info;

PVOID       g_AntiAntiAttachBuffer, g_LoadSysHookBuffer;
BYTE        g_OldLdrInitializeThunkHeader[0x10];
BOOL        g_IsProcessOllyDbg, g_EnableSuperAntiDebug;
ULONG       g_AntiAntiAttachThreadId;

ULONG_PTR   g_ODBase;
PVOID       g_pvResKnown, g_pvResErrCode, g_pvResExceptions, g_pvResVXD;

BOOL (CDECL *WriteSettingsInt)(LPCSTR Key, LONG Value);
BOOL (CDECL *ReadSettingsInt)(LPCSTR Key, LONG DefaultValue);
VOID (CDECL *StubAddModuleToList)(t_module *Module);

TYPE_OF(GetProcAddress)     *StubOdGetProcAddress;
TYPE_OF(EnumProcessModules) *StubOdEnumProcessModules;

enum OllyDbgOperandType
{
    Type_Float  = 0x27,
    Type_Double = 0x28,
};

#pragma warning(push, 0)

ASM
HWND
WINAPI
OldCreateWindowExA(
    DWORD       ExStyle,
    LPCSTR      ClassName,
    LPCSTR      WindowName,
    DWORD       Style,
    int         X,
    int         Y,
    int         Width,
    int         Height,
    HWND        hWndParent,
    HMENU       hMenu,
    HINSTANCE   hInstance,
    LPVOID      Param
)
{
    ASM_DUMMY_AUTO();
}

ASM
VOID
CDECL
OldODSetcpu(
    ULONG ThreadId,
    ULONG AsmAddress,
    ULONG DumpAddress,
    ULONG StackAddress,
    ULONG Mode
)
{
    ASM_DUMMY_AUTO();
}

ASM ULONG CDECL OldODReadMemory(PVOID Buffer, ULONG Address, ULONG Size, LONG Mode)
{
    ASM_DUMMY_AUTO();
}

ASM INT CDECL OldDisasm(PBYTE src,ULONG srcsize,ULONG srcip,PBYTE srcdec, t_disasm *disasm,int disasmmode,ULONG threadid)
{
    ASM_DUMMY_AUTO();
}

ASM VOID CDECL OldGenerateUddPath(PCHAR pszModulePath, PCHAR pszUddPath)
{
    ASM_DUMMY_AUTO();
}

#pragma warning(pop)

VOID
CDECL
ODSetcpu(
    ULONG ThreadId,
    ULONG AsmAddress,
    ULONG DumpAddress,
    ULONG StackAddress,
    ULONG Mode
)
{
    DumpAddress += DumpAddress == 0 ? -1 : 0;
    return OldODSetcpu(ThreadId, AsmAddress, DumpAddress, StackAddress, Mode);
}

ULONG CDECL ODReadMemory(PVOID Buffer, ULONG Address, ULONG Size, LONG Mode)
{
    ULONG       BytesRead;
    NTSTATUS    Status;
    HANDLE      DebuggeeHandle;

    if (Address != NULL)
        goto DEFAULT_PROC;

    if (Size == 0 || Getstatus() == 0)
        return 0;

    DebuggeeHandle = (HANDLE)Plugingetvalue(VAL_HPROCESS);
    if (DebuggeeHandle == NULL)
        return 0;

    Status = NtReadVirtualMemory(DebuggeeHandle, (PVOID)Address, Buffer, Size, &BytesRead);
    if (!NT_SUCCESS(Status))
        return 0;

//    return BytesRead;

DEFAULT_PROC:

    return OldODReadMemory(Buffer, Address, Size, Mode);
}

INT
CDECL
DisplayFloat(
    PBYTE       src,
    ULONG       srcsize,
    ULONG       srcip,
    PBYTE       srcdec,
    t_disasm   *disasm,
    INT         disasmmode,
    ULONG       threadid
)
{
    INT     Result, Length2;
    CHAR    ValueBuffer[0x200], *p;
    CHAR    Value[0x20];

    Result = OldDisasm(src, srcsize, srcip, srcdec, disasm, disasmmode, threadid);

    if (disasm->cmdtype != (C_FLT | C_EXPL) ||
        Result != 6 ||
        disasm->indexed != 0 ||
        CHAR_UPPER(disasm->result[0]) != 'F')
    {
        return Result;
    }

#if 0
    AllocConsole();
    PrintConsoleW(
        L"ret     = %08X\n"
        L"address = %08X\n"
        L"cmdtype = %08X\n"
        L"memtype = %08X\n"
        L"result  = %S\n",
        Result,
        disasm->ip,
        disasm->cmdtype,
        disasm->memtype,
        disasm->result
    );

    return Result;
#endif

    switch (disasm->memtype)
    {
        case DEC_FLOAT4:
            Readmemory(&Value, disasm->adrconst, 4, MM_RESILENT);
            Length2 = Printfloat4(ValueBuffer, *(float *)Value) - 1;
            break;

        case DEC_FLOAT8:
            Readmemory(&Value, disasm->adrconst, 8, MM_RESILENT);
            Length2 = Printfloat8(ValueBuffer, *(double *)Value) - 1;
            break;

        case DEC_FLOAT10:
            Readmemory(&Value, disasm->adrconst, 10, MM_RESILENT);
            INLINE_ASM
            {
                sub     esp, 0xC;
                fld     tbyte ptr Value;
                fstp    tbyte ptr [esp];
                lea     eax, ValueBuffer;
                push    eax;
                call    dword ptr [Printfloat10];
                add     esp, 0x10;
                dec     eax;
                mov     Length2, eax;
            }
            break;

        default:
            return Result;
    }

    p = ValueBuffer + Length2;
    while (*p == '0')
        --p;
    if (*p == '.')
        ++p;
    *++p = 0;
    Quickinsertname(disasm->adrconst, NM_CONST, ValueBuffer);
    Mergequicknames();

    return Result;
}

VOID CDECL GenerateUddPath(PCHAR pszModulePath, PCHAR pszUddPathBuffer)
{
    PCHAR pszFileName;
    PCHAR pszUddPath;

    pszUddPath = (PCHAR)0xD396C + g_ODBase;

    pszFileName = findnamea(pszModulePath);
    sprintf(pszUddPathBuffer, "%s\\%s.udd", pszUddPath, pszFileName);
}

enum ECompareIndexType
{
    CMP_TYPE_FUNC_NAME,
    CMP_TYPE_FUNC_FLAG,
    CMP_TYPE_ERROR_CODE,
};

#define COMPARE_INFO_MAGIC  TAG4('CMPI')

struct COMPARE_INFO_FRAME : public TEB_ACTIVE_FRAME
{
    ULONG Type;
    PVOID Param;
};

typedef INT (CDECL *QSortCallback)(const void *, const void *);

INT CDECL CompareFunctionIndex(PULONG Offset1, PULONG Offset2)
{
    INT                 Result;
    LPWSTR              pFunc1, pFunc2;
    COMPARE_INFO_FRAME *pInfo;

    pInfo = (COMPARE_INFO_FRAME *)RtlGetFrame();
    while (pInfo->Context != COMPARE_INFO_MAGIC)
        pInfo = (COMPARE_INFO_FRAME *)pInfo->Previous;

    switch (pInfo->Type)
    {
        case CMP_TYPE_FUNC_NAME:
        {
            LPWSTR pParam1, pParam2;

            pFunc1 = (LPWSTR)((ULONG_PTR)pInfo->Param + *Offset1);
            pFunc2 = (LPWSTR)((ULONG_PTR)pInfo->Param + *Offset2);

            pParam1 = StrFindCharW(pFunc1, ':');
            pParam2 = StrFindCharW(pFunc2, ':');
            *pParam1 = 0;
            *pParam2 = 0;
            Result = StrCompareW(pFunc1, pFunc2);
            *pParam1 = ':';
            *pParam2 = ':';
        }
        break;

        case CMP_TYPE_FUNC_FLAG:
            pFunc1 = (LPWSTR)((ULONG_PTR)pInfo->Param + *Offset1 + 7 * sizeof(*pFunc1));
            pFunc2 = (LPWSTR)((ULONG_PTR)pInfo->Param + *Offset2 + 7 * sizeof(*pFunc2));
            Result = StrCompareW(pFunc1, pFunc2);
            break;

        default:
            return 0;
    }

    return Result < 0 ? -1 : Result > 0 ? 1 : 0;
}

typedef struct
{
    ULONG Value;
    ULONG Offset;
} ERROR_CODE_ENTRY;

INT CDECL CompareErrCodeIndex(ERROR_CODE_ENTRY &Entry1, ERROR_CODE_ENTRY &Entry2)
{
    return Entry1.Value < Entry2.Value ? -1 : Entry1.Value > Entry2.Value ? 1 : 0;
}

BOOL ReBuildErrorCode(LPCWSTR lpErrCodeFile, PVOID *ppvOutBuffer, PDWORD pOutSize)
{
    BOOL  Result;
    PVOID pvBuffer, pvBufIndex;
    ULONG FileSize;

    if (ppvOutBuffer == NULL)
        return FALSE;

    NtFileDisk file;
    MemoryAllocator mem;

    *ppvOutBuffer = NULL;

    if (pOutSize != NULL)
        *pOutSize = 0;

    if (!NT_SUCCESS(file.Open(lpErrCodeFile)))
        return FALSE;

    FileSize = file.GetSize32();
    pvBuffer = mem.Alloc(FileSize);
    if (pvBuffer == NULL)
        return FALSE;

    pvBufIndex = NULL;
    Result = FALSE;
    LOOP_ONCE
    {
        PBYTE  pbBufText;
        ULONG  IndexSize, TextSize, Length;
        LPWSTR pText, pTextEnd, pValue;
        ERROR_CODE_ENTRY *pErrCodeIndex;

        pvBufIndex = mem.Alloc(FileSize);
        if (pvBufIndex == NULL)
            break;

        if (!NT_SUCCESS(file.Read(pvBuffer)))
            break;

        pText = (LPWSTR)pvBuffer;
        if (*pText != BOM_UTF16_LE)
            break;

        ++pText;
        pTextEnd = (LPWSTR)((ULONG_PTR)pText + FileSize);
        if (pText >= pTextEnd)
            break;

        pbBufText     = (PBYTE)pvBuffer;
        pErrCodeIndex = (ERROR_CODE_ENTRY *)pvBufIndex;

        do
        {
            SizeT  LineSize = 0x10000;
            LPWSTR pPrevLine;

            pPrevLine = pText;
            pText = PeekLineW(pText, pTextEnd, NULL, &LineSize);
            if (pText == NULL)
                break;
            if (LineSize == 0)
                continue;

            pValue = StrFindCharW(pPrevLine, '=');
            if (pValue == NULL)
                continue;

            if (pText[0] != 0)
                pText[-1] = 0;
            *pValue++ = 0;
            pErrCodeIndex->Value  = StringToInt32HexW(pValue);
            pErrCodeIndex->Offset = pbBufText - (PBYTE)pvBuffer;
            Nt_UnicodeToAnsi((PCHAR)pbBufText, FileSize - (pbBufText - (PBYTE)pvBuffer), pPrevLine, -1, &Length);
            pbBufText += Length + 1;
            ++pErrCodeIndex;
        } while (pText < pTextEnd);

        PVOID pvOutBuffer;
        PBYTE pbOutBuffer;
        ULONG OutBufferSize;
//        CompareIndexInfo CmpInfo;

        IndexSize = (ULONG_PTR)pErrCodeIndex - (ULONG_PTR)pvBufIndex;
        TextSize  = pbBufText - (PBYTE)pvBuffer;
        OutBufferSize = IndexSize + TextSize;

        qsort(pvBufIndex, IndexSize / sizeof(ERROR_CODE_ENTRY), sizeof(ERROR_CODE_ENTRY), (QSortCallback)CompareErrCodeIndex);

//        CmpInfo.Type    = CMP_TYPE_ERROR_CODE;
//        CmpInfo.lpParam = pvBufIndex;
//        std::sort_with_param(
//            (ERROR_CODE_ENTRY *)pvBufIndex,
//            (ERROR_CODE_ENTRY *)pErrCodeIndex,
//            CompareErrCodeIndex,
//            &CmpInfo);

        pvOutBuffer = mem.Alloc(OutBufferSize);
        if (pvOutBuffer == NULL)
            break;

//        memset(pvOutBuffer, -2, OutBufferSize);
        *ppvOutBuffer = pvOutBuffer;
        pbOutBuffer = (PBYTE)pvOutBuffer;

        FileSize = Compress((PBYTE)pvBufIndex, IndexSize, pbOutBuffer + 8, OutBufferSize);
        *(PDWORD)pbOutBuffer = IndexSize / sizeof(*pErrCodeIndex);
        *(PDWORD)&pbOutBuffer[4] = FileSize;

        FileSize += 8;
        pbOutBuffer += FileSize;
        FileSize = Compress((PBYTE)pvBuffer, TextSize, pbOutBuffer + 8, OutBufferSize - FileSize);
        *(PDWORD)pbOutBuffer = TextSize;
        *(PDWORD)&pbOutBuffer[4] = FileSize;

        pbOutBuffer += FileSize + 8;
        FileSize = pbOutBuffer - (PBYTE)pvOutBuffer;
        if (pOutSize != NULL)
            *pOutSize = FileSize;

        *ppvOutBuffer = mem.ReAlloc(pvOutBuffer, FileSize);

        Result = TRUE;
    }

    mem.Free(pvBufIndex);
    mem.Free(pvBuffer);

    return Result;
}

BOOL ReBuildExceptions(LPCWSTR lpExceptionsFile, PVOID *ppvOutBuffer, PDWORD pOutSize)
{
    return ReBuildErrorCode(lpExceptionsFile, ppvOutBuffer, pOutSize);
}

BOOL ReBuildVxd(LPCWSTR lpVxdFile, PVOID *ppvOutBuffer, PDWORD pOutSize)
{
    return ReBuildErrorCode(lpVxdFile, ppvOutBuffer, pOutSize);
}

BOOL ReBuildFunctions(LPCWSTR lpPrototypeFile, LPCWSTR lpFlagsFile, PVOID *ppvOutBuffer, PDWORD pOutSize)
{
    PVOID       pvPrototype, pvFlags, pvIndex, pvPrototypeTextBuffer, pvFlagsTextBuffer;
    ULONG       PrototypeSize, FlagsSize, Length;
    ULONG       PrototypeTextSize, FlagsTextSize, PrototypeIndexSize, FlagsIndexSize;
    LPWSTR      pText, pTextEnd;

    if (ppvOutBuffer == NULL)
        return FALSE;

    NtFileDisk file;
    MemoryAllocator        mem;

    *ppvOutBuffer = NULL;
    if (pOutSize != NULL)
        *pOutSize = 0;

    pvPrototype           = NULL;
    pvFlags               = NULL;
    pvIndex               = NULL;
    pvPrototypeTextBuffer = NULL;
    pvFlagsTextBuffer     = NULL;

    LOOP_ONCE
    {
        if (!NT_SUCCESS(file.Open(lpFlagsFile)))
            break;

        FlagsSize = file.GetSize32();
        pvFlags   = mem.Alloc(FlagsSize);
        if (pvFlags == NULL)
            break;
        pvFlagsTextBuffer = mem.Alloc(FlagsSize);
        if (pvFlagsTextBuffer == NULL)
            break;

        file.Read(pvFlags);
        pText = (LPWSTR)pvFlags;
        if (*pText != BOM_UTF16_LE)
            break;

        if (!NT_SUCCESS(file.Open(lpPrototypeFile)))
            break;

        PrototypeSize = file.GetSize32();
        pvPrototype = mem.Alloc(PrototypeSize);
        if (pvPrototype == NULL)
            break;
        pvPrototypeTextBuffer = mem.Alloc(PrototypeSize);
        if (pvPrototypeTextBuffer == NULL)
            break;

        file.Read(pvPrototype);
        pText = (LPWSTR)pvPrototype;
        if (*pText != BOM_UTF16_LE)
            break;

        pvIndex = mem.Alloc(PrototypeSize + FlagsSize);
        if (pvIndex == NULL)
            break;

        pTextEnd = (LPWSTR)((ULONG_PTR)pText + PrototypeSize);
        ++pText;
        if (pText >= pTextEnd)
            break;

        SizeT  LineSize;
        ULONG  IndexCount;
        PDWORD pIndex;
        LPSTR  pOutText;
        LPWSTR pTextBegin;
        COMPARE_INFO_FRAME CmpInfo;

        pIndex = (PDWORD)pvIndex;
        pTextBegin = pText;

        {
            PDWORD pFuncNameIndex;
            LPWSTR pFunction, pParameter;

            pFuncNameIndex = pIndex;

            do
            {
                LineSize = 0x10000;
                pFunction = pText;
                pText = PeekLineW(pText, pTextEnd, NULL, &LineSize);
                if (pText == NULL)
                    break;
                if (LineSize == 0)
                    continue;

                if (*(PDWORD)pFunction == TAG2W('//'))
                    continue;

                pParameter = StrFindCharW(pFunction, ':');
                if (pParameter == NULL)
                    continue;

                for (INT32 Index = -1; pText[Index] == '\r' || pText[Index] == '\n'; --Index)
                    pText[Index] = 0;

                *pFuncNameIndex++ = (ULONG_PTR)pFunction - (ULONG_PTR)pTextBegin;

            } while (pText < pTextEnd);

            IndexCount = ((ULONG_PTR)pFuncNameIndex - (ULONG_PTR)pIndex) / sizeof(*pIndex);
        }

        if (IndexCount == 0)
            break;

        CmpInfo.Context = COMPARE_INFO_MAGIC;
        CmpInfo.Type    = CMP_TYPE_FUNC_NAME;
        CmpInfo.Param   = pTextBegin;
        RtlPushFrame(&CmpInfo);
        qsort(pIndex, IndexCount, sizeof(*pIndex), (QSortCallback)CompareFunctionIndex);
        RtlPopFrame(&CmpInfo);
//        std::sort_with_param(pIndex, pIndex + IndexCount, CompareFunctionIndex, &CmpInfo);

        pText = pTextBegin;
        pOutText = (LPSTR)pvPrototypeTextBuffer;

        do
        {
            LPWSTR pFunction, pParameter;

            pFunction = (LPWSTR)((ULONG_PTR)pText + *pIndex);
            pParameter = StrFindCharW(pFunction, ':');
            *pParameter++ = 0;

            *pIndex++ = (ULONG_PTR)pOutText - (ULONG_PTR)pvPrototypeTextBuffer;
            Nt_UnicodeToAnsi(pOutText, PrototypeSize - pIndex[-1], pFunction, -1, &Length);
            pOutText += Length + 1;
            *pOutText++ = 0;
            Nt_UnicodeToAnsi(pOutText, PrototypeSize - pIndex[-1], pParameter, -1, &Length);
            pOutText += Length + 1;
        } while (--IndexCount);

        PrototypeIndexSize = (ULONG_PTR)pIndex - (ULONG_PTR)pvIndex;
        PrototypeTextSize  = (ULONG_PTR)pOutText - (ULONG_PTR)pvPrototypeTextBuffer;

        pText    = (LPWSTR)pvFlags + 1;
        pTextEnd = (LPWSTR)((ULONG_PTR)pvFlags + FlagsSize);
        if (pText >= pTextEnd)
            break;

        pTextBegin = pText;
        enum
        {
            STATUS_GET_FLAG_NAME,
            STATUS_GET_FLAG_VALUE,
            STATUS_GET_FLAG_END,
        };

        ULONG Status = STATUS_GET_FLAG_NAME;

        {
            PDWORD pFlagsIndex;
            LPWSTR pFlagName;

            pFlagsIndex = pIndex;

            do
            {
                LineSize = 0x10000;
                pFlagName = pText;
                pText = PeekLineW(pText, pTextEnd, NULL, &LineSize);
                if (pText == NULL)
                    break;
                if (LineSize == 0)
                    continue;

                if (*(PDWORD)pFlagName == TAG2W('//'))
                    continue;

                for (INT32 Index = -1; pText[Index] == '\r' || pText[Index] == '\n'; --Index)
                    pText[Index] = 0;

                if (Status == STATUS_GET_FLAG_NAME)
                {
                    if (StrNICompareW(pFlagName, L"@Flags=", 7))
                        continue;

                    *pFlagsIndex++ = (ULONG_PTR)pFlagName - (ULONG_PTR)pTextBegin;
                }
                else if (Status == STATUS_GET_FLAG_VALUE)
                {
                    if (!StrNICompareW(pFlagName, L"@End", 4))
                    {
                        Status = STATUS_GET_FLAG_NAME;
                        continue;
                    }
                }

            } while (pText < pTextEnd);

            IndexCount = ((ULONG_PTR)pFlagsIndex - (ULONG_PTR)pIndex) / sizeof(*pIndex);
        }

        if (IndexCount == 0)
            break;

        CmpInfo.Context = COMPARE_INFO_MAGIC;
        CmpInfo.Type    = CMP_TYPE_FUNC_FLAG;
        CmpInfo.Param   = pTextBegin;
        RtlPushFrame(&CmpInfo);
        qsort(pIndex, IndexCount, sizeof(*pIndex), (QSortCallback)CompareFunctionIndex);
        RtlPopFrame(&CmpInfo);
//        std::sort_with_param(pIndex, pIndex + IndexCount, CompareFunctionIndex, &CmpInfo);

        pOutText = (LPSTR)pvFlagsTextBuffer;

        do
        {
            LPWSTR pFlagText, pFlagValue;

            pFlagText = pText;
            pFlagText = (LPWSTR)((ULONG_PTR)pTextBegin + *pIndex);
            Status = STATUS_GET_FLAG_NAME;

            while (pFlagText < pTextEnd)
            {
                switch (*pFlagText)
                {
                    case 0:
                    case '\n':
                    case '\r':
                        ++pFlagText;
                        continue;
                }

                if (Status == STATUS_GET_FLAG_NAME)
                {
                    if (StrNICompareW(pFlagText, L"@Flags=", 7))
                        goto CONTINUE_LOOP;

                    Status = STATUS_GET_FLAG_VALUE;
                    *pIndex++ = (ULONG_PTR)pOutText - (ULONG_PTR)pvFlagsTextBuffer;
                    pFlagText += 7;
                    Nt_UnicodeToAnsi(pOutText, FlagsSize - pIndex[-1], pFlagText, -1, &Length);
                    pOutText += Length + 1;
                }
                else if (Status == STATUS_GET_FLAG_VALUE)
                {
                    UINT32 ByteCode;
                    if (!StrNICompareW(pFlagText, L"@End", 4))
                    {
                        Status = STATUS_GET_FLAG_NAME;
                        *pOutText++ = 0;
                        break;
                    }

                    ByteCode = StringToInt32HexW(pFlagText);
                    *pOutText++ = (CHAR)ByteCode;
                    pFlagValue = StrFindCharW(pFlagText, ',');
                    if (pFlagValue == NULL)
                        goto CONTINUE_LOOP;

                    pFlagText = pFlagValue;
                    if (ByteCode != 0x01 && ByteCode != 0x0A && ByteCode != 0x17)
                    {
                        *(PDWORD)pOutText = StringToInt32HexW(++pFlagText);
                        pOutText += 4;
                        pFlagValue = StrFindCharW(pFlagText, ',');
                        if (pFlagValue == NULL)
                            goto CONTINUE_LOOP;

                        pFlagText = pFlagValue;
                    }

                    Nt_UnicodeToAnsi(pOutText, FlagsSize - pIndex[-1], ++pFlagText, -1, &Length);
                    pOutText += Length + 1;
                }
CONTINUE_LOOP:
                pFlagText += StrLengthW(pFlagText);
            }

        } while (--IndexCount);

        FlagsIndexSize = (ULONG_PTR)pIndex - (ULONG_PTR)pvIndex - PrototypeIndexSize;
        FlagsTextSize  = (ULONG_PTR)pOutText - (ULONG_PTR)pvFlagsTextBuffer;

        PVOID pvOutBuffer;
        PBYTE pbOutBuffer;
        ULONG FileSize, CompSize, OutBufferSize;

        OutBufferSize = PrototypeIndexSize + PrototypeTextSize + FlagsIndexSize + FlagsTextSize;
        OutBufferSize *= 4;
        pvOutBuffer = mem.Alloc(OutBufferSize + 8 * 4);
        if (pvOutBuffer == NULL)
            break;

        pbOutBuffer   = (PBYTE)pvOutBuffer;
        *ppvOutBuffer = pbOutBuffer;
        FileSize      = 0;

        CompSize = Compress((PBYTE)pvIndex, PrototypeIndexSize, pbOutBuffer + 8, OutBufferSize - 8);
        *(PDWORD)pbOutBuffer = PrototypeIndexSize / sizeof(PrototypeIndexSize);
        *(PDWORD)&pbOutBuffer[4] = CompSize;

        CompSize    += 8;
        FileSize    += CompSize;
        pbOutBuffer += CompSize;
        CompSize = Compress((PBYTE)pvPrototypeTextBuffer, PrototypeTextSize, pbOutBuffer + 8, OutBufferSize - FileSize);
        *(PDWORD)pbOutBuffer = PrototypeTextSize;
        *(PDWORD)&pbOutBuffer[4] = CompSize;

        CompSize    += 8;
        FileSize    += CompSize;
        pbOutBuffer += CompSize;
        CompSize = Compress((PBYTE)pvIndex + PrototypeIndexSize, FlagsIndexSize, pbOutBuffer + 8, OutBufferSize - FileSize);
        *(PDWORD)pbOutBuffer = FlagsIndexSize / sizeof(FlagsIndexSize);
        *(PDWORD)&pbOutBuffer[4] = CompSize;

        CompSize    += 8;
        FileSize    += CompSize;
        pbOutBuffer += CompSize;
        CompSize = Compress((PBYTE)pvFlagsTextBuffer, FlagsTextSize, pbOutBuffer + 8, OutBufferSize - FileSize);
        *(PDWORD)pbOutBuffer = FlagsTextSize;
        *(PDWORD)&pbOutBuffer[4] = CompSize;

        FileSize += CompSize + 8;
        if (pOutSize != NULL)
            *pOutSize = FileSize;

        *ppvOutBuffer = mem.ReAlloc(pvOutBuffer, FileSize);

    }

    mem.Free(pvIndex);
    mem.Free(pvFlags);
    mem.Free(pvPrototype);
    mem.Free(pvPrototypeTextBuffer);
    mem.Free(pvFlagsTextBuffer);

    return TRUE;
}

#define HRES_UNKNOWN  (HRSRC)0x00000000
#define HRES_KNOWN    (HRSRC)0xFFFFFFFF
#define HRES_ERRCODE  (HRSRC)0xFFFFFFFE
#define HRES_EXCEPTNS (HRSRC)0xFFFFFFFD
#define HRES_VXD      (HRSRC)0xFFFFFFFC

HRSRC GetResourceType(LPCSTR lpName)
{
    switch (HashAPI(lpName))
    {
        case 0x10AE55F3:    // RES_KNOWN
            if (g_pvResKnown != NULL)
                return HRES_KNOWN;
            break;

        case 0xC999B32A:    // RES_ERRCODE
            if (g_pvResErrCode != NULL)
                return HRES_ERRCODE;
            break;

        case 0x7606B6C2:    // RES_EXCEPTNS
            if (g_pvResExceptions != NULL)
                return HRES_EXCEPTNS;
            break;

        case 0x5D2FAF4F:    // RES_VXD
            if (g_pvResVXD != NULL)
                return HRES_VXD;
            break;
    }

    return HRES_UNKNOWN;
}

HRSRC WINAPI MyFindResourceA(HMODULE hModule, LPCSTR lpName, LPCSTR lpType)
{
    HRSRC hResource;

    LOOP_ONCE
    {
        if (hModule != NULL)
            break;

        if (StrCompareA(lpType, "KNOWNRESTYPE"))
            break;

        hResource = GetResourceType(lpName);
        if (hResource != HRES_UNKNOWN)
            return hResource;

    }

    return FindResourceA(hModule, lpName, lpType);
}

HGLOBAL WINAPI MyLoadResource(HMODULE hModule, HRSRC hResInfo)
{
    if (hModule == 0)
    {
/*
        if (hResInfo == HRES_KNOWN    ||
            hResInfo == HRES_ERRCODE  ||
            hResInfo == HRES_EXCEPTNS ||
            hResInfo == HRES_VXD)
        {
            return (HGLOBAL)hResInfo;
        }
*/

        switch ((ULONG_PTR)hResInfo)
        {
            case HRES_KNOWN:
            case HRES_ERRCODE:
            case HRES_EXCEPTNS:
            case HRES_VXD:
                return (HGLOBAL)hResInfo;
        }

    }

    return LoadResource(hModule, hResInfo);
}

LPVOID WINAPI MyLockResource(HGLOBAL hResData)
{
    HRSRC hResInfo = (HRSRC)hResData;

    if (hResInfo == HRES_KNOWN)
        return g_pvResKnown;
    else if (hResInfo == HRES_EXCEPTNS)
        return g_pvResExceptions;
    else if (hResInfo == HRES_ERRCODE)
        return g_pvResErrCode;
    else if (hResInfo == HRES_VXD)
        return g_pvResVXD;

    return LockResource(hResData);
}

VOID RefreshFunctionInfo()
{
    WCHAR CurrentDirectory[MAX_NTPATH];

    MemoryAllocator::FreeMemory(g_pvResErrCode);
    MemoryAllocator::FreeMemory(g_pvResExceptions);
    MemoryAllocator::FreeMemory(g_pvResVXD);
    MemoryAllocator::FreeMemory(g_pvResKnown);

    Nt_GetCurrentDirectory(countof(CurrentDirectory), CurrentDirectory);
    Nt_SetExeDirectoryAsCurrent();

    ReBuildErrorCode (L"info\\RES_ERRCODE.txt",  &g_pvResErrCode, NULL);
    ReBuildExceptions(L"info\\RES_EXCEPTNS.txt", &g_pvResExceptions, NULL);
    ReBuildVxd       (L"info\\RES_VXD.txt",      &g_pvResVXD, NULL);
    ReBuildFunctions (L"info\\RES_KNOWN_PROTOTYPE.txt", L"info\\RES_KNOWN_FLAG.txt", &g_pvResKnown, NULL);

    Nt_SetCurrentDirectory(CurrentDirectory);
}

BOOL STDCALL BackupExe(LPSTR ExistingFileName, LPSTR NewFileName)
{
    WCHAR Exist[MAX_NTPATH], New[MAX_NTPATH];

    Nt_AnsiToUnicode(Exist, countof(Exist), ExistingFileName);
    Nt_AnsiToUnicode(New, countof(New), NewFileName);

    return Nt_IsPathExists(New) || NT_SUCCESS(Nt_MoveFile(Exist, New));
}

NTSTATUS ModifyModuleBase(PVOID DestinationModule)
{
    NTSTATUS            Status;
    PLDR_MODULE         OdModule;
    UNICODE_STRING      str;
    BYTE                PeHeader[0x1000];
    PIMAGE_DOS_HEADER   DosHeader;
    PIMAGE_NT_HEADERS   NtHeaders;

    RTL_CONST_STRING(str, L"OllyDbg.exe");

    if (Nt_FindLdrModuleByName(&str) != NULL)
        return STATUS_SUCCESS;

    CopyMemory(PeHeader, &__ImageBase, sizeof(PeHeader));

    DosHeader = (PIMAGE_DOS_HEADER)PeHeader;
    NtHeaders = (PIMAGE_NT_HEADERS)PtrAdd(DosHeader, DosHeader->e_lfanew);

    ZeroMemory(NtHeaders->OptionalHeader.DataDirectory, sizeof(NtHeaders->OptionalHeader.DataDirectory));

    NtHeaders->OptionalHeader.AddressOfEntryPoint = NULL;
    NtHeaders->OptionalHeader.SizeOfImage = sizeof(PeHeader);
    NtHeaders->FileHeader.NumberOfSections = 0;

    SET_FLAG(NtHeaders->FileHeader.Characteristics, IMAGE_FILE_RELOCS_STRIPPED);
    CLEAR_FLAG(NtHeaders->FileHeader.Characteristics, IMAGE_FILE_DLL);

    Status = LoadDllFromMemory(PeHeader, sizeof(PeHeader), &str, NULL, LMD_MAPPED_DLL);
    if (!NT_SUCCESS(Status))
        return Status;

    OdModule = Nt_FindLdrModuleByName(&str);
    if (OdModule == NULL)
        return STATUS_UNSUCCESSFUL;

    OdModule->DllBase = DestinationModule;
    OdModule->EntryPoint = NULL;

    return STATUS_SUCCESS;
}

ULONG GetHookSysCallDllPath(PWCHAR FullPath, ULONG Count)
{
//    ULONG Size;
//    static WCHAR DllFileName[] = L"HookSyscall.dll";

    return Nt_GetModuleFileName((HMODULE)&__ImageBase, FullPath, Count);

//    Size = RtlGetExecuteDirectoryW(FullPath, Count);
//    CopyStruct(FullPath + Size, DllFileName, sizeof(DllFileName));
//    Size += CONST_STRLEN(DllFileName);
//    return Size;
}

ASM BOOL STDCALL OldODDebugActiveProcess(ULONG /* ProcessId */)
{
    ASM_DUMMY_AUTO();
}

typedef struct
{
    PVOID           NtTerminateThread;
    PVOID           pfLdrLoadDll;
    UNICODE_STRING  DllPath;
//    WCHAR           Buffer[1];
} REMOTE_LOAD_DLL_INFO;

ASM VOID LoadSysCallHookDll()
{
    INLINE_ASM
    {
        call    SELF_LOCATE;
SELF_LOCATE:
        pop     ecx;
        lea     ecx, [ecx + 14];
        push    ecx;
        xor     eax, eax;
        push    dword ptr fs:[eax];
        mov     dword ptr fs:[eax], esp;
        __emit  0xCC;

        call    SELF_LOCATE2;
SELF_LOCATE2:
        pop     esi;
        and     esi, not (MEMORY_PAGE_SIZE - 1);
        lodsd;
        mov     ebx, eax;
        lodsd;
        xor     ecx, ecx;
        push    eax;    // sub esp, 4
        push    esp;    // pModuleHandle
        push    esi;    // ModuleFileName
        push    ecx;    // Flags
        push    ecx;    // PathToFile
        call    eax;    // LdrLoadDll
//        pop     eax;    // add esp, 4;

EXIT_THREAD:
//        push    0;
        push    -2;
        call    ebx;
        jmp     EXIT_THREAD;
    }
}

ASM VOID LoadSysCallHookDllEnd() { ASM_UNIQUE() }

NTSTATUS LoadSysCallHookDllAfterAttach(HANDLE ProcessHandle)
{
    WCHAR                   DllPath[MAX_PATH];
    BYTE                    JumpOpCode[0x10];
    ULONG                   Size, OldProtect;
    NTSTATUS                Status;
    PVOID                   BaseAddress, AntiAntiAttachBuffer, BaseLdrInitializeThunk;
    REMOTE_LOAD_DLL_INFO    LoadInfo;
    HANDLE                  ThreadHandle;
    CLIENT_ID               ClientID;

    if (g_AntiAntiAttachBuffer != NULL)
    {
        Size = 0;
        Nt_FreeMemory(ProcessHandle, g_AntiAntiAttachBuffer);
        g_AntiAntiAttachBuffer = NULL;
    }

    BaseLdrInitializeThunk = LdrInitializeThunk;
    BaseAddress = BaseLdrInitializeThunk;
    Status = Nt_ReadMemory(ProcessHandle, BaseAddress, JumpOpCode, 5);
    if (!NT_SUCCESS(Status))
        return Status;

    CopyStruct(g_OldLdrInitializeThunkHeader, JumpOpCode, 5);

//    if (JumpOpCode[0] != JUMP)
    {
        BaseAddress = NULL;
        Status = Nt_AllocateMemory(ProcessHandle, &BaseAddress, MEMORY_PAGE_SIZE);
        if (!NT_SUCCESS(Status))
            return Status;

        AntiAntiAttachBuffer    = BaseAddress;
        g_AntiAntiAttachBuffer  = BaseAddress;
    }
//    else
    {
//        AntiAntiAttachBuffer = (PVOID)(*(PULONG_PTR)&JumpOpCode[1] + (ULONG_PTR)BaseLdrInitializeThunk + 5);
    }

    LoadInfo.NtTerminateThread    = NtTerminateThread;
    LoadInfo.pfLdrLoadDll           = LdrLoadDll;
    LoadInfo.DllPath.Buffer         = (PWCHAR)((ULONG_PTR)AntiAntiAttachBuffer + sizeof(LoadInfo));

    Size = GetHookSysCallDllPath(DllPath, countof(DllPath));
    Size *= sizeof(WCHAR);

    LoadInfo.DllPath.Length         = (USHORT)Size;
    LoadInfo.DllPath.MaximumLength  = (USHORT)(Size += 2);

    Status = Nt_WriteMemory(ProcessHandle, AntiAntiAttachBuffer, &LoadInfo, sizeof(LoadInfo));
    if (!NT_SUCCESS(Status))
        return Status;

    *(PULONG_PTR)&AntiAntiAttachBuffer += sizeof(LoadInfo);

    Status = Nt_WriteMemory(ProcessHandle, AntiAntiAttachBuffer, DllPath, Size);
    if (!NT_SUCCESS(Status))
        return Status;

    *(PULONG_PTR)&AntiAntiAttachBuffer += Size;

    Size = (ULONG_PTR)LoadSysCallHookDllEnd - (ULONG_PTR)LoadSysCallHookDll;
    Status = Nt_WriteMemory(ProcessHandle, AntiAntiAttachBuffer, LoadSysCallHookDll, Size);
    if (!NT_SUCCESS(Status))
        return Status;

    BaseAddress = BaseLdrInitializeThunk;
    Status = Nt_ProtectMemory(ProcessHandle, BaseAddress, 5, PAGE_EXECUTE_READWRITE, &OldProtect);
    if (!NT_SUCCESS(Status))
        return Status;

    Status = RtlCreateUserThread(
                ProcessHandle,
                NULL,
                FALSE,
                0,
                0,
                0x4000,
                AntiAntiAttachBuffer,
                NULL,
                &ThreadHandle,
                &ClientID
             );
    if (NT_SUCCESS(Status))
    {
        NtClose(ThreadHandle);
        g_AntiAntiAttachThreadId = (ULONG_PTR)ClientID.UniqueThread;
    }
    else
        return Status;

    JumpOpCode[0] = JUMP;
    *(PULONG_PTR)&JumpOpCode[1] = (ULONG_PTR)(AntiAntiAttachBuffer) - ((ULONG_PTR)BaseAddress + 5);
    Status = Nt_WriteMemory(ProcessHandle, BaseAddress, JumpOpCode, 5);
    if (OldProtect != PAGE_EXECUTE_READWRITE)
    {
        Nt_ProtectMemory(ProcessHandle, BaseAddress, 5, OldProtect, &OldProtect);
    }

    return Status;
}

ASM
BOOL
STDCALL
OldODCreateProcessA(
    LPCSTR                  /* lpApplicationName */,
    LPSTR                   /* lpCommandLine */,
    LPSECURITY_ATTRIBUTES   /* lpProcessAttributes */,
    LPSECURITY_ATTRIBUTES   /* lpThreadAttributes */,
    BOOL                    /* bInheritHandles */,
    ULONG                   /* dwCreationFlags */,
    LPVOID                  /* lpEnvironment */,
    LPCSTR                  /* lpCurrentDirectory */,
    LPSTARTUPINFOA          /* lpStartupInfo */,
    LPPROCESS_INFORMATION   /* lpProcessInformation */
)
{
    ASM_DUMMY_AUTO();
}

ASM PVOID LoadExternDll2()
{
    INLINE_ASM
    {
        push eax;               // ret addr
        pushad;
        pushfd;
        call SELF_LOCALIZATION;
SELF_LOCALIZATION:
        pop  esi;
        and  esi, 0xFFFF0000;
        lodsd;
        mov  [esp+0x24], eax;   // ret addr
        lodsd;
        xor  ecx, ecx;
        push ecx;
        push esp;               // pModuleHandle
        push esi;               // ModuleFileName
        push ecx;               // Flags
        push ecx;               // PathToFile
        call eax;               // LdrLoadDll
        pop  eax;               // pop ModuleHandle
        xchg eax, esi;
        and  eax, 0FFFF0000h;
        and  dword ptr [eax], 0;
        popfd;
        popad;
        ret;
    }
}

ASM VOID LoadExternDllEnd2() { ASM_UNIQUE() }

typedef struct
{
    ULONG           ReturnAddr;
    PVOID           pfLdrLoadDll;
    UNICODE_STRING  ModuleFileName;
} INJECT_DLL_CURRENT_THREAD2;

NTSTATUS LoadSysCallHookDll_CP(HANDLE hProcess, HANDLE hThread)
{
    NTSTATUS    Status;
    PVOID       pvBuffer, OriginalEip;
    ULONG       Length;
    WCHAR       DllPath[MAX_PATH];
    CONTEXT     ThreadContext;
    INJECT_DLL_CURRENT_THREAD2 inj;

    pvBuffer = NULL;

    ThreadContext.ContextFlags = CONTEXT_CONTROL;
    Status = NtGetContextThread(hThread, &ThreadContext);
    if (!NT_SUCCESS(Status))
        return Status;

    OriginalEip = (PVOID)ThreadContext.Eip;

    Length = GetHookSysCallDllPath(DllPath, countof(DllPath));

    LOOP_ONCE
    {
        Status = Nt_AllocateMemory(hProcess, &pvBuffer, MEMORY_PAGE_SIZE);
        if (!NT_SUCCESS(Status))
            break;

        Length *= sizeof(WCHAR);
        inj.pfLdrLoadDll = LdrLoadDll;
        inj.ReturnAddr   = ThreadContext.Eip;
        inj.ModuleFileName.Length = (USHORT)Length;
        inj.ModuleFileName.MaximumLength = (USHORT)(Length + sizeof(WCHAR));
        inj.ModuleFileName.Buffer = (LPWSTR)((ULONG_PTR)pvBuffer + sizeof(inj));
        Status = Nt_WriteMemory(hProcess, pvBuffer, &inj, sizeof(inj));
        if (!NT_SUCCESS(Status))
            break;

        Length += sizeof(WCHAR);
        Status = Nt_WriteMemory(hProcess, (PVOID)((ULONG_PTR)pvBuffer + sizeof(inj)), DllPath, Length);
        if (!NT_SUCCESS(Status))
            break;

        ThreadContext.Eip = (ULONG_PTR)pvBuffer + sizeof(inj) + Length;
        Length = (ULONG_PTR)LoadExternDllEnd2 - (ULONG_PTR)LoadExternDll2;
        Status = Nt_WriteMemory(hProcess, (PVOID)ThreadContext.Eip, LoadExternDll2, Length);
        if (!NT_SUCCESS(Status))
            break;

        Status = NtSetContextThread(hThread, &ThreadContext);
        if (NT_SUCCESS(Status))
            break;

        LARGE_INTEGER TimeOut;

        FormatTimeOut(&TimeOut, 100);
        for (ULONG Retry = 3; Retry; --Retry)
        {
            Status = NtSetContextThread(hThread, &ThreadContext);
            if (NT_SUCCESS(Status))
                break;

            NtDelayExecution(FALSE, &TimeOut);
        }
    }

    if (!NT_SUCCESS(Status))
    {
        ThreadContext.Eip = (ULONG_PTR)OriginalEip;
        NtSetContextThread(hThread, &ThreadContext);
        Nt_FreeMemory(hProcess, pvBuffer);
    }
    else
    {
        g_LoadSysHookBuffer = pvBuffer;
    }

    return Status;
}

VOID SetDebuggeeInformation(ULONG_PTR ProcessId, BOOL Set = TRUE)
{
    NtFileDisk Device;

    if (NT_SUCCESS(Device.OpenDevice(SHADOW_SYSCALL_DEVICE_SYMBOLIC)))
    {
        SS_PROCESS_OBJECT obj;

        obj.Debuggee = Set;
        obj.ProcessId = ProcessId;

        Device.DeviceIoControl(IOCTL_SET_PROCESS_INFO, &obj, sizeof(obj), NULL, 0);
    }
}

BOOL
STDCALL
ODCreateProcessA(
    LPCSTR                  ApplicationName,
    LPSTR                   CommandLine,
    LPSECURITY_ATTRIBUTES   ProcessAttributes,
    LPSECURITY_ATTRIBUTES   ThreadAttributes,
    BOOL                    InheritHandles,
    ULONG                   CreationFlags,
    LPVOID                  Environment,
    LPCSTR                  CurrentDirectory,
    LPSTARTUPINFOA          StartupInfo,
    LPPROCESS_INFORMATION   ProcessInformation
)
{
    BOOL                Result;
    WCHAR               Buffer[0x100];
    ULONG               DebugFlags;
    NTSTATUS            Status;
    TEB_ACTIVE_FRAME    filter;
    HANDLE              DebugObject, DebuggeeProcess;

    filter.Context = CREATE_EXPLORER_CHILD_PROCESS_MAGIC;

    CLEAR_FLAG(CreationFlags, DEBUG_PROCESS | DEBUG_ONLY_THIS_PROCESS);

    DebugFlags = 0;
    NtSetInformationProcess(NtCurrentProcess(), ProcessDebugFlags, &DebugFlags, sizeof(DebugFlags));

    RtlPushFrame(&filter);
    Result = OldODCreateProcessA(ApplicationName, CommandLine, ProcessAttributes, ThreadAttributes, InheritHandles, CreationFlags | CREATE_SUSPENDED, Environment, CurrentDirectory, StartupInfo, ProcessInformation);
    RtlPopFrame(&filter);

    if (!Result)
        return Result;

    SetDebuggeeInformation(ProcessInformation->dwProcessId);
    Nt_DebugActiveProcess(ProcessInformation->dwProcessId);

    if (!g_EnableSuperAntiDebug)
    {
        if (!FLAG_ON(CreationFlags, CREATE_SUSPENDED))
            NtResumeProcess(ProcessInformation->hProcess);

        return Result;
    }

    do
    {
        Status = LoadSysCallHookDll_CP(ProcessInformation->hProcess, ProcessInformation->hThread);
        if (NT_SUCCESS(Status))
            break;

        swprintf(Buffer, L"LoadSysCallHookDll_CP failed, Status = %08X, retry ?", Status);
    } while (MessageBoxW(NULL, Buffer, NULL, MB_ICONASTERISK | MB_OKCANCEL) == MB_OK);

    if (!FLAG_ON(CreationFlags, CREATE_SUSPENDED))
        NtResumeProcess(ProcessInformation->hProcess);

    return TRUE;
}

NTSTATUS AttachToActiveProccess(ULONG ProcessId)
{
    HANDLE      DebugObject, DebuggeeProcess;
    NTSTATUS    Status;

    Status = DbgUiConnectToDbg();
    if (!NT_SUCCESS(Status))
        return Status;

    DebuggeeProcess = ProcessIdToHandle(ProcessId);
    if (DebuggeeProcess == NULL)
        return STATUS_UNSUCCESSFUL;

    SetDebuggeeInformation(ProcessId);

    DebugObject = DbgUiGetThreadDebugObject();
    Status = STATUS_SUCCESS;
    LOOP_ONCE
    {
        Status = NtDebugActiveProcess(DebuggeeProcess, DebugObject);
        if (!NT_SUCCESS(Status))
            break;

        Status = LoadSysCallHookDllAfterAttach(DebuggeeProcess);
    }

    if (!NT_SUCCESS(Status))
    {
        NtRemoveProcessDebug(DebuggeeProcess, DebugObject);
        SetDebuggeeInformation(ProcessId, FALSE);
    }

    NtClose(DebuggeeProcess);

    return Status;
}

BOOL STDCALL ODDebugActiveProcess(ULONG ProcessId)
{
    if (g_EnableSuperAntiDebug)
    {
        if (NT_SUCCESS(AttachToActiveProccess(ProcessId)))
            return TRUE;
    }

    return OldODDebugActiveProcess(ProcessId);
}

VOID ResetDebuggeeInfoWorker()
{
    g_LoadSysHookBuffer = NULL;
    g_AntiAntiAttachBuffer = NULL;
}

ASM VOID OldResetDebuggeeInfo()
{
    ASM_DUMMY_AUTO();
}

VOID ResetDebuggeeInfo()
{
    OldResetDebuggeeInfo();
    ResetDebuggeeInfoWorker();

    g_EnableSuperAntiDebug = ReadSettingsInt(SUPER_ANTI_DEBUG_KEY, -1);
    if (g_EnableSuperAntiDebug == -1)
        WriteSettingsInt(SUPER_ANTI_DEBUG_KEY, TRUE);

    POD_HOOK_INFO Info = g_Info;

    if (Info->DriverLoaded)
        Info->SsDevice.Enabled = ReadSettingsInt(ULTRA_ANTI_DEBUG_KEY, TRUE);
}

ASM VOID CDECL OldCallPluginMainLoop(LPDEBUG_EVENT /* DebugEvent */)
{
    ASM_DUMMY_AUTO();
}

VOID RestoreLdrInitThunk(ULONG_PTR ProcessId)
{
    HANDLE Process;
    ULONG OldProtect;
    PVOID BaseLdrInitializeThunk;

    if (g_OldLdrInitializeThunkHeader[0] == 0)
        return;

    Process = ProcessIdToHandle(ProcessId);
    if (Process == NULL)
        return;

    BaseLdrInitializeThunk = LdrInitializeThunk;
    Nt_ProtectMemory(Process, BaseLdrInitializeThunk, 5, PAGE_EXECUTE_READWRITE, &OldProtect);
    Nt_WriteMemory(Process, BaseLdrInitializeThunk, g_OldLdrInitializeThunkHeader, 5);

    if (OldProtect != PAGE_EXECUTE_READWRITE)
    {
        Nt_ProtectMemory(Process, BaseLdrInitializeThunk, 5, OldProtect, &OldProtect);
    }

    NtClose(Process);

    g_OldLdrInitializeThunkHeader[0] = 0;
}

VOID CDECL CallPluginMainLoop(LPDEBUG_EVENT DebugEvent)
{
    OldCallPluginMainLoop(DebugEvent);

#if 1

    if (DebugEvent == NULL)
        return;

    ULONG       OldProtect;
    NTSTATUS    Status;
    HANDLE      ProcessHandle, ThreadHandle;
    CONTEXT     Context;

    switch (DebugEvent->dwDebugEventCode)
    {
        case EXIT_THREAD_DEBUG_EVENT:
            if (g_AntiAntiAttachBuffer == NULL || DebugEvent->dwThreadId != g_AntiAntiAttachThreadId)
                break;

            ProcessHandle = ProcessIdToHandle(DebugEvent->dwProcessId);
            if (ProcessHandle == NULL)
                return;

            RestoreLdrInitThunk(DebugEvent->dwProcessId);

            Nt_FreeMemory(ProcessHandle, g_AntiAntiAttachBuffer);
            g_AntiAntiAttachBuffer = NULL;
            g_AntiAntiAttachThreadId = 0;

            NtClose(ProcessHandle);
            break;

        case EXCEPTION_DEBUG_EVENT:
            if (DebugEvent->u.Exception.ExceptionRecord.ExceptionCode != STATUS_SINGLE_STEP)
                break;

            if (g_AntiAntiAttachBuffer != NULL)
                RestoreLdrInitThunk(DebugEvent->dwProcessId);

            if (g_LoadSysHookBuffer == NULL)
                break;

            ThreadHandle = ThreadIdToHandle(DebugEvent->dwThreadId);
            if (ThreadHandle == NULL)
                break;

            Context.ContextFlags = CONTEXT_CONTROL;
            Status = NtGetContextThread(ThreadHandle, &Context);
            NtClose(ThreadHandle);
            if (!NT_SUCCESS(Status))
                break;

            if ((ULONG_PTR)Context.Eip >= (ULONG_PTR)g_LoadSysHookBuffer &&
                (ULONG_PTR)Context.Eip <= (ULONG_PTR)g_LoadSysHookBuffer + MEMORY_PAGE_SIZE)
            {
                break;
            }

            ProcessHandle = ProcessIdToHandle(DebugEvent->dwProcessId);
            if (ProcessHandle == NULL)
                break;

            Status = Nt_ReadMemory(ProcessHandle, g_LoadSysHookBuffer, &OldProtect, 4);
            if (NT_SUCCESS(Status) && OldProtect == 0)
            {
                Nt_FreeMemory(ProcessHandle, g_LoadSysHookBuffer);
                g_LoadSysHookBuffer = NULL;
            }

            NtClose(ProcessHandle);
            break;

        case EXIT_PROCESS_DEBUG_EVENT:
            ResetDebuggeeInfoWorker();
            break;
    }

#endif
}

WNDPROC g_OldWndProc;

BOOL OnKey(HWND hWnd, ULONG VirtualKey, BOOL IsKeyDown, INT RepeatCount, ULONG KeyFlags)
{
    LONG        Flags, Mode;
    ULONG_PTR   Address, TheadId;
    t_thread   *ThreadInfo;
    enum
    {
        FLAG_DISASM     = 0x00000001,
        FLAG_DUMP       = 0x00000002,

        FLAG_FOLLOW_EIP = 0x20000000,

        FLAG_CONTROL_MASK   = 0xF0000000,
    };

    UNREFERENCED_PARAMETER(hWnd);
    UNREFERENCED_PARAMETER(RepeatCount);
    UNREFERENCED_PARAMETER(KeyFlags);

    if (!IsKeyDown || VirtualKey == '8')
        return FALSE;

    //  ']}' for US
    if (VirtualKey == VK_OEM_6 &&
        GetKeyState(VK_CONTROL) < 0 &&
        GetKeyState(VK_MENU) < 0
       )
    {
        RefreshFunctionInfo();
        return TRUE;
    }

    if (Getstatus() == 0)
        return FALSE;

    Flags   = 0;
    Mode    = 0;

    if (GetKeyState(VK_CONTROL) < 0)
    {
        SET_FLAG(Flags, FLAG_DUMP);
        SET_FLAG(Mode, CPU_DUMPHIST);
    }
    if (GetKeyState(VK_SHIFT) < 0)
    {
        SET_FLAG(Flags, FLAG_DISASM);
        SET_FLAG(Mode, CPU_ASMHIST);
    }
/*
    switch (VirtualKey)
    {
        case '9':
            if (!FLAG_ON(Flags, FLAG_DISASM))
                break;
            NO_BREAK;

        case VK_MULTIPLY:
            SET_FLAG(Flags, FLAG_FOLLOW_EIP);
            break;
    }
*/
    if (Flags == 0)
        return FALSE;
/*
    if (FLAG_ON(Flags, FLAG_CONTROL_MASK))
    {
        CallWindowProcA(
            g_OldWndProc,
            hWnd,
            WM_CHAR,
            -1, MAKELPARAM(RepeatCount, KeyFlags)
        );

        return TRUE;
    }
*/
    if (VirtualKey < '1' || VirtualKey > '9')
        return FALSE;

    TheadId = Getcputhreadid();
    ThreadInfo = Findthread(TheadId);
    if (ThreadInfo == NULL)
        return FALSE;

    if (VirtualKey == '9')
    {
        Address = ThreadInfo->reg.r[7];
    }
    else
    {
        Address = ThreadInfo->reg.r[VirtualKey - '1'];
    }

    if (Findmemory(Address) == NULL)
        return FALSE;

    OldODSetcpu(
        NULL,
        FLAG_ON(Flags, FLAG_DISASM) ? Address : 0,
        FLAG_ON(Flags, FLAG_DUMP) ? Address : -1,
        0,
        Mode | CPU_NOFOCUS
    );

    return FALSE;
}

LRESULT WINAPI ODWindowProcA(HWND hWnd, ULONG Message, WPARAM wParam, LPARAM lParam)
{
    switch (Message)
    {
        case WM_KEYDOWN:
        case WM_KEYUP:
            if (OnKey(hWnd, wParam, Message == WM_KEYDOWN, (SHORT)LOWORD(lParam), (ULONG)HIWORD(lParam)))
                return 0;
            break;
    }

    return CallWindowProcA(g_OldWndProc, hWnd, Message, wParam, lParam);
}

HWND
WINAPI
MyCreateWindowExA(
    DWORD       ExStyle,
    LPCSTR      ClassName,
    LPCSTR      WindowName,
    DWORD       Style,
    int         X,
    int         Y,
    int         Width,
    int         Height,
    HWND        hWndParent,
    HMENU       hMenu,
    HINSTANCE   hInstance,
    LPVOID      Param
)
{
    HWND hWnd;

    hWnd = OldCreateWindowExA(
                ExStyle,
                ClassName,
                WindowName,
                Style,
                X,
                Y,
                Width,
                Height,
                hWndParent,
                hMenu,
                hInstance,
                Param
           );
    if (hWnd != NULL)
    {
        g_OldWndProc = (WNDPROC)SetWindowLongPtrA(hWnd, GWLP_WNDPROC, (LONG_PTR)ODWindowProcA);
    }

    return hWnd;
}

WCHAR SystemDirectory[MAX_NTPATH];

VOID CDECL AddModuleToList(t_module *Module)
{
    ULONG_PTR Length;
    POD_HOOK_INFO Info = g_Info;

    Length = Info->SystemDirectory64.Length;
    if (!StrNICompareA(Info->SystemDirectory64.Buffer, Module->path, Length))
    {
        if (!StrICompareA(Module->path + Length, "ntdll.dll"))
        {
            return;
        }
    }
    else
    {
        Length = Info->SystemDirectoryWow64.Length;
        if (!StrNICompareA(Info->SystemDirectoryWow64.Buffer, Module->path, Length))
        {
            if (!StrICompareA(Module->path + Length, "ntdll.dll"))
            {
                CopyStruct(Module->name, "ntdll", 6);
            }
        }
    }

    StubAddModuleToList(Module);
    if (Module->codebase == NULL) LOOP_ONCE
    {
        NTSTATUS    Status;
        HANDLE      Process;
        PVOID       Address;

        IMAGE_DOS_HEADER DosHeader;
        IMAGE_NT_HEADERS NtHeaders;

        Process = (HANDLE)Plugingetvalue(VAL_HPROCESS);

        Address = (PVOID)Module->base;

        Status = Nt_ReadMemory(Process, Address, &DosHeader, sizeof(DosHeader));
        FAIL_BREAK(Status);

        Status = Nt_ReadMemory(Process, PtrAdd(Address, DosHeader.e_lfanew), &NtHeaders, sizeof(NtHeaders));
        FAIL_BREAK(Status);

        Module->codebase = PtrAdd(NtHeaders.OptionalHeader.BaseOfCode, Address);
        Module->codesize = PtrAdd(NtHeaders.OptionalHeader.SizeOfCode, Address);
        Module->origcodesize = PtrAdd(NtHeaders.OptionalHeader.BaseOfCode, Address);
    }
}

BOOL
WINAPI
OdEnumProcessModules(
    HANDLE      Process,
    HMODULE*    Modules,
    ULONG       cb,
    PULONG      Needed
)
{
    BOOL        Success;
    ULONG_PTR   Size1, Size2, Size, Need;
    HMODULE     *List1, *List2;
    PULONG_PTR  List, L, L2;

    Size1 = 0x200 * sizeof(*List1);
    List1 = (HMODULE *)AllocStack(Size1);

    LOOP_FOREVER
    {
        Success = EnumProcessModules(Process, List1, Size1, &Need);
        if (!Success)
            break;

        if (Need <= Size1)
        {
            Size1 = Need;
            break;
        }

        List1 = (HMODULE *)AllocStack(Need - Size1);
        Size1 = Need;
    }

    if (!Success)
        Size1 = 0;

    Size2 = 0x200 * sizeof(*List2);
    List2 = (HMODULE *)AllocStack(Size2);

    LOOP_FOREVER
    {
        Success = StubOdEnumProcessModules(Process, List2, Size2, &Need);
        if (!Success)
            break;

        if (Need <= Size2)
        {
            Size2 = Need;
            break;
        }

        List2 = (HMODULE *)AllocStack(Need - Size2);
        Size2 = Need;
    }

    if (!Success)
        Size2 = 0;

    Size = Size1 + Size2;
    if (Size == 0)
        return FALSE;

#if 0

    if (Modules != NULL)
    {
        CopyMemory(Modules, List1, MY_MIN(Size1, cb));

        if (cb <= Size1)
            return TRUE;

        cb -= Size1;
        CopyMemory(PtrAdd(Modules, Size1), List2, MY_MIN(Size2, cb));
    }

    if (Needed != NULL)
        *Needed = Size;

    return TRUE;

#else

    List = (PULONG_PTR)AllocStack(Size);
    CopyMemory(List, List1, Size1);
    CopyMemory(PtrAdd(List, Size1), List2, Size2);

    for (ULONG_PTR i = Size / sizeof(*List); i; --i)
        for (ULONG_PTR j = 0; j != i - 1; ++j)
            if (List[j] > List[j + 1])
                Swap(List[j], List[j + 1]);

    L = List;
    L2 = L + 1;
    for (LONG_PTR Count = Size / sizeof(*List) - 1; Count; --Count)
    {
        if (*L != *L2)
            *++L = *L2;

        ++L2;
    }

    Size = PtrOffset(L + 1, List);
    if (Modules != NULL)
    {
        CopyMemory(Modules, List, MY_MIN(Size, cb));
    }

    if (Needed != NULL)
        *Needed = Size;

    return TRUE;
#endif
}

ULONG
WINAPI
OdGetModuleFileNameEx(
    HANDLE  Process,
    PVOID   Module,
    LPSTR   FileName,
    ULONG   Size
)
{
    ULONG_PTR   Length, NameLength;
    NTSTATUS    Status;
    WCHAR       DeviceName[MAX_NTPATH];
    MEMORY_MAPPED_FILENAME_INFORMATION2 ModulePath;

//    if (OdGetModuleFileNameEx != NULL) return GetModuleFileNameExA(Process, (HMODULE)Module, FileName, Size);

    if (Size < 3 || FileName == NULL)
        return GetModuleFileNameExA(Process, (HMODULE)Module, FileName, Size);

    if (Module == NULL)
        Module = Nt_GetExeModuleHandle();

    Status = NtQueryVirtualMemory(Process, Module, MemoryMappedFilenameInformation, &ModulePath, sizeof(ModulePath), &Length);
    if (!NT_SUCCESS(Status))
        return GetModuleFileNameExA(Process, (HMODULE)Module, FileName, Size);

    WCHAR DosPath[4];

    *(PULONG)&DosPath[0] = TAG2W('A:');
    *(PULONG)&DosPath[2] = 0;

    for (ULONG_PTR Count = 'Z' - 'A' + 1; Count; ++DosPath[0], --Count)
    {
        PWSTR BackSlash;

        Length = Nt_QueryDosDevice(DosPath, DeviceName, countof(DeviceName));
        if (Length == 0)
            continue;

        if (RtlCompareMemory(ModulePath.Name.Buffer, DeviceName, Length * sizeof(WCHAR)) !=  Length * sizeof(WCHAR))
            continue;

        FileName[0] = DosPath[0];
        FileName[1] = DosPath[1];
        FileName[2] = '\\';

        Nt_UnicodeToAnsi(
            FileName + 3,
            Size - 3,
            ModulePath.Name.Buffer + Length,
            ModulePath.Name.Length / sizeof(WCHAR) - Length,
            &Length
        );

        return Length / sizeof(WCHAR);
    }

    return GetModuleFileNameExA(Process, (HMODULE)Module, FileName, Size);
}

PVOID WINAPI OdGetProcAddress(HMODULE Module, PCSTR ProcName)
{
    if (PtrAnd(ProcName, 0xFFFF0000) != 0)
    switch (HashAPI(ProcName))
    {
        case PSAPI_GetModuleFileNameExA: return OdGetModuleFileNameEx;

        case PSAPI_EnumProcessModules:
            *(PVOID *)&StubOdEnumProcessModules = StubOdGetProcAddress(Module, ProcName);
            return OdEnumProcessModules;
    }

    return StubOdGetProcAddress(Module, ProcName);
}

BOOL IsProcessOllyDbg(PVOID BaseAddress)
{
    PBYTE Base = (PBYTE)BaseAddress;

    if (*(PULONG)(Base + 0x208) != 0x40B10868   ||
        *(Base + 0x77DCE)       != 0xE8         ||
        *(Base + 0x77958)       != 0xE8)
    {
        return FALSE;
    }

    return TRUE;
}

NTSTATUS InitializeDriver(POD_HOOK_INFO Info)
{
    NTSTATUS        Status;
    SERVICE_STATUS  ServiceStatus;
    SC_HANDLE       ScManager, Service;
    WCHAR           DriverPath[MAX_NTPATH];

    Status      = STATUS_UNSUCCESSFUL;
    ScManager   = NULL;
    Service     = NULL;

    ScManager = OpenSCManagerW(NULL, NULL, SC_MANAGER_CREATE_SERVICE);
    if (ScManager == NULL)
        return STATUS_UNSUCCESSFUL;

    SCOPE_EXIT
    {
        if (Service != NULL)
            CloseServiceHandle(Service);

        if (ScManager != NULL)
            CloseServiceHandle(ScManager);

    } SCOPE_EXIT_END;

    Service = OpenServiceW(ScManager, SHADOW_SYSCALL_SERVICE_NAME, SERVICE_ALL_ACCESS);
    if (Service != NULL)
    {
        if (!StartServiceW(Service, 0, NULL) && RtlGetLastWin32Error() != ERROR_SERVICE_ALREADY_RUNNING)
            ControlService(Service, SERVICE_CONTROL_CONTINUE, &ServiceStatus);

        Status = STATUS_SUCCESS;
        return Status;
    }

    CopyStruct(DriverPath + Nt_GetExeDirectory(DriverPath, countof(DriverPath)), SHADOW_SYSCALL_DRIVER_NAME, sizeof(L"Test_Drv.sys"));

    Service = CreateServiceW(
                    ScManager,
                    SHADOW_SYSCALL_SERVICE_NAME,
                    SHADOW_SYSCALL_SERVICE_NAME,
                    SERVICE_ALL_ACCESS,
                    SERVICE_KERNEL_DRIVER,
                    SERVICE_DEMAND_START,
                    SERVICE_ERROR_IGNORE,
                    DriverPath,
                    NULL,
                    NULL,
                    NULL,
                    NULL,
                    NULL
              );

    if (Service == NULL)
        return STATUS_UNSUCCESSFUL;

    if (StartServiceW(Service, 0, NULL))
        Status = STATUS_SUCCESS;

    return Status;
}

VOID
NTAPI
SetThemesAccessAnyApc(
    POD_HOOK_INFO   Info,
    ULONG_PTR       ProcessId,
    BOOL            Create
)
{
    if (!Create)
    {
        if (ProcessId == Info->ThemesPid)
            Info->ThemesPid = 0;

        return;
    }

    NTSTATUS    Status;
    SC_HANDLE   ScManager, Themes;
    NtFileDisk  Device;

    if (Info->ThemesPid != 0)
        return;

    Status = Device.OpenDevice(SHADOW_SYSCALL_DEVICE_SYMBOLIC);
    if (!NT_SUCCESS(Status))
        return;

    ScManager = OpenSCManagerW(NULL, NULL, SC_MANAGER_CREATE_SERVICE);
    if (ScManager == NULL)
        return;

    Themes = OpenServiceW(ScManager, L"Themes", SERVICE_ALL_ACCESS);
    if (Themes == NULL)
    {
        CloseServiceHandle(ScManager);
        return;
    }

    ULONG Needed;
    SERVICE_STATUS_PROCESS ServiceProcess;

    if (QueryServiceStatusEx(Themes, SC_STATUS_PROCESS_INFO, (PBYTE)&ServiceProcess, sizeof(ServiceProcess), &Needed) &&
        (ProcessId == 0 || ProcessId == ServiceProcess.dwProcessId))
    {
        SS_PROCESS_OBJECT obj;

        Info->ThemesPid = ServiceProcess.dwProcessId;
        obj.ProcessId   = ServiceProcess.dwProcessId;
        obj.AccessAny   = TRUE;

        Device.DeviceIoControl(IOCTL_SET_PROCESS_INFO, &obj, sizeof(obj), NULL, 0);
    }

    CloseServiceHandle(Themes);
    CloseServiceHandle(ScManager);
}

BOOL InitOllyDbg(PVOID OdBaseAddrses)
{
    BOOL            Success, bEnable, Wow64;
    NTSTATUS        Status;
    PVOID           OllyDbgModule;
    UNICODE_STRING  ODFileName;
    POD_HOOK_INFO   Info;
    UNICODE_STRING  SystemRoot;
    WCHAR           SystemDirectory[MAX_NTPATH];

    Info = NULL;
    Success = FALSE;

//    RtlWow64EnableFsRedirection(FALSE);

    Info = new OD_HOOK_INFO;
    if (Info == NULL)
        return FALSE;

    Wow64 = Nt_IsWow64Process(NtCurrentProcess());

    if (!Wow64) LOOP_ONCE
    {
        SetThemesAccessAnyApc(Info, 0, TRUE);

        NtFileDisk Device;

        Status = Device.OpenDevice(SHADOW_SYSCALL_DEVICE_SYMBOLIC);
        FAIL_BREAK(Status);

        SS_CREATE_PROCESS_NOTIFY notify;

        notify.Context          = Info;
        notify.NotifyRoutine    = SetThemesAccessAnyApc;
        notify.ThreadId         = (HANDLE)Nt_GetCurrentThreadId();
        Info->MainThreadId      = notify.ThreadId;

        Device.DeviceIoControl(IOCTL_REGISTER_CREATE_PROCESS, &notify, sizeof(notify), NULL, 0);

        SS_PROCESS_OBJECT obj;

        obj.ProcessId = Nt_GetCurrentProcessId();
        obj.Flags = 0;
        obj.ShadowSystemCall = TRUE;
        obj.DenyAccess = TRUE;
        obj.AccessAny = TRUE;
        Status = Device.DeviceIoControl(IOCTL_SET_PROCESS_INFO, &obj, sizeof(obj), NULL, 0);
    }

    InstallHookPort();

    ADD_FILTER_(NtCreateProcess, OdCreateProcess);
    ADD_FILTER_(NtCreateProcessEx, OdCreateProcessEx);
    ADD_FILTER_(NtCreateUserProcess, OdCreateUserProcess);

    g_Info = Info;

    SystemRoot = WCharToUnicodeString(SystemDirectory, Nt_GetSystemDirectory64(SystemDirectory, countof(SystemDirectory)));
    RtlUnicodeStringToAnsiString(&Info->SystemDirectory64, &SystemRoot, TRUE);

    SystemRoot = WCharToUnicodeString(SystemDirectory, Nt_GetSystemDirectory(SystemDirectory, countof(SystemDirectory)));
    RtlUnicodeStringToAnsiString(&Info->SystemDirectoryWow64, &SystemRoot, TRUE);

    Nt_SetExeDirectoryAsCurrent();

    RTL_CONST_STRING(ODFileName, L"OllyDbg.exe");
    Status = LdrGetDllHandle(NULL, 0, &ODFileName, (PVOID *)&OllyDbgModule);
    if (!NT_SUCCESS(Status) || OllyDbgModule == NULL)
    {
        ModifyModuleBase(OdBaseAddrses);
    }

    MEMORY_PATCH p[] =
    {
//        PATCH_MEMORY(0xFF,              1, 0x200BF),    // follow eip: * -> 0xFF
        PATCH_MEMORY(0x44EB,            2, 0x1ED54),    // The byte you are pointing at lies outside the executable code of any known module.
        PATCH_MEMORY(0x41EB,            2, 0x23DEA),    // same
        PATCH_MEMORY(0x03,              1, 0x6C211),    // choose font
        PATCH_MEMORY(0x7FEB,            2, 0x195AE),
        PATCH_MEMORY(0xEB,              1, 0x776D0),    // bypass "Is dll" warning
        PATCH_MEMORY(TAG3('%s>'),       4, 0xC76C9),    // remove CONST. prefix format
        PATCH_MEMORY(0x00,              1, 0xC76CE),    // remove const. prefix
        PATCH_MEMORY(0x00,              1, 0xC76D4),    // remove CONST. prefix
        PATCH_MEMORY(0xFF,              1, 0x2DA1E),    // display NULL memory in dump
        PATCH_MEMORY(0xFF,              1, 0x2DA64),    // display NULL memory in dump
        PATCH_MEMORY(0x00,              1, 0x61327),    // display NULL memory in dump
        PATCH_MEMORY(0xEB,              1, 0x61A57),    // display NULL memory in dump
        PATCH_MEMORY(0x00,              4, 0x2EA0A),    // wow64 EFlags Interrupt Enable Flag bit
        PATCH_MEMORY(MyFindResourceA,   4, IATLookupRoutineRVAByEntry(OdBaseAddrses, FindResourceA)),
        PATCH_MEMORY(MyLoadResource,    4, IATLookupRoutineRVAByEntry(OdBaseAddrses, LoadResource)),
        PATCH_MEMORY(MyLockResource,    4, IATLookupRoutineRVAByEntry(OdBaseAddrses, LockResource)),
    };

    MEMORY_FUNCTION_PATCH f[] =
    {
        PATCH_FUNCTION(CALL, FIRST_CALL_TO_JUMP, 0x35E63, MyCreateWindowExA,    0, OldCreateWindowExA),
        PATCH_FUNCTION(JUMP, AUTO_DISASM, 0xAEFD0, ODCreateProcessA,     0, OldODCreateProcessA),
        PATCH_FUNCTION(JUMP, AUTO_DISASM, 0xAEFD6, ODDebugActiveProcess, 0, OldODDebugActiveProcess),

        PATCH_FUNCTION(JUMP, AUTO_DISASM, 0x6130C, ODReadMemory,    0, OldODReadMemory),
        PATCH_FUNCTION(JUMP, AUTO_DISASM, 0x2D618, ODSetcpu,        0, OldODSetcpu),

        PATCH_FUNCTION(CALL, 0, 0x4D905, BackupExe),
        PATCH_FUNCTION(JUMP, 0, 0x5B314, GenerateUddPath),
        PATCH_FUNCTION(JUMP, 0, 0x15F48, DisplayFloat,          4, OldDisasm),
        PATCH_FUNCTION(JUMP, 0, 0x96C48, ResetDebuggeeInfo,     4, OldResetDebuggeeInfo),
        PATCH_FUNCTION(JUMP, 0, 0x96B4C, CallPluginMainLoop,    0, OldCallPluginMainLoop),

        INLINE_HOOK_CALL_RVA(Wow64 ? 0x5F7E6 : IMAGE_INVALID_RVA, AddModuleToList, StubAddModuleToList),
        INLINE_HOOK_JUMP_RVA(0xAF090, OdGetProcAddress, StubOdGetProcAddress),
    };

    *(PULONG_PTR)&WriteSettingsInt  = (ULONG_PTR)OdBaseAddrses + 0x2E25C;
    *(PULONG_PTR)&ReadSettingsInt   = (ULONG_PTR)OdBaseAddrses + 0x2E294;
    g_ODBase = (ULONG_PTR)OdBaseAddrses;

    Nt_PatchMemory(p, countof(p), f, countof(f), OdBaseAddrses);

    RefreshFunctionInfo();

    RtlAdjustPrivilege(SE_DEBUG_PRIVILEGE, TRUE, FALSE, (PBOOLEAN)&bEnable);

    return TRUE;
}

BOOL InitSysCallHook()
{
    InstallHookPort();

    ADD_FILTER(NtQueryInformationProcess);
    ADD_FILTER(NtSetInformationThread);
    ADD_FILTER(NtClose);
    ADD_FILTER(NtYieldExecution);
//    ADD_FILTER(NtOpenProcess);

//    AllocConsole();

    return TRUE;
}

BOOL Initialize(PVOID BaseAddress)
{
    PVOID hModule;

    LdrDisableThreadCalloutsForDll(BaseAddress);

    if (MemoryAllocator::CreateGlobalHeap() == NULL)
        return FALSE;

    hModule = Nt_GetExeModuleHandle();

    g_IsProcessOllyDbg = IsProcessOllyDbg(hModule);
    return g_IsProcessOllyDbg ? InitOllyDbg(hModule) : InitSysCallHook();
}

BOOL UnInitialize(PVOID BaseAddress)
{
    POD_HOOK_INFO Info;

    if (g_IsProcessOllyDbg)
    {
        MemoryAllocator::FreeMemory(g_pvResKnown);
        MemoryAllocator::FreeMemory(g_pvResErrCode);
        MemoryAllocator::FreeMemory(g_pvResExceptions);
        MemoryAllocator::FreeMemory(g_pvResVXD);

        UnInstallHookPort();

        Info = g_Info;

        if (Info != NULL && Info->MainThreadId != NULL)
        {
            NTSTATUS    Status;
            NtFileDisk  Device;

            Status = Device.OpenDevice(SHADOW_SYSCALL_DEVICE_SYMBOLIC);
            if (NT_SUCCESS(Status))
            {
                SS_CREATE_PROCESS_NOTIFY notify;

                notify.Context = NULL;
                notify.NotifyRoutine = NULL;
                notify.ThreadId = Info->MainThreadId;

                Device.DeviceIoControl(IOCTL_REGISTER_CREATE_PROCESS, &notify, sizeof(notify), NULL, 0);
            }
        }

        delete Info;

        MemoryAllocator::DestroyGlobalHeap();
    }
    else
    {
        UnInstallHookPort();
    }

    return FALSE;
}

BOOL WINAPI DllMain(PVOID BaseAddress, ULONG Reason, PVOID Reserved)
{
    switch (Reason)
    {
        case DLL_PROCESS_ATTACH:
            if (Nt_FindThreadFrameByContext(LOAD_MEM_DLL_INFO_MAGIC) != NULL)
                break;

            return Initialize(BaseAddress) || UnInitialize(BaseAddress);

        case DLL_PROCESS_DETACH:
            UnInitialize(BaseAddress);
            break;
    }

    return TRUE;
}
