#if 1

#define AUTHOR_NAME "Amano"
#define SECTION_NAME "."AUTHOR_NAME

#define _WIN32_WINNT 0x601

#pragma comment(linker,"/ENTRY:main2")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text /MERGE:.text1=.text /SECTION:.idata,ERW")
#pragma comment(linker, "/SECTION:"SECTION_NAME",ERW /MERGE:.text="SECTION_NAME)
#pragma warning(disable:4995 4273)

#ifndef UNICODE
    #define UNICODE
#endif

#ifndef _UNICODE
    #define _UNICODE
#endif

#define  _DECL_DLLMAIN

#include "ml.cpp"

ML_OVERLOAD_NEW

#if defined(UNICODE)
    #define __WSTRING(str) L##str
    #define WSTRING(str) __WSTRING(str)
#else
    #define WSTRING(str) (str)
#endif


ULONG GetBitSetCount(ULONG Value)
{
    Value -= ((Value >> 1) & 0x55555555);
    Value  = (((Value >> 2) & 0x33333333) + (Value & 0x33333333));
    Value  = (((Value >> 4) + Value) & 0x0F0F0F0F);
    Value += (Value >> 8);
    Value += (Value>>16);
    Value &= 0x3F;

    return Value;
}

#if ML_X86

BOOL IsRunningInVMWare()
{
    BOOL Result;

    SEH_TRY
    {
        INLINE_ASM
        {
            mov     eax, 'VMXh';
            mov     ecx, 0xA;
            mov     edx, 'VX';
            in      eax, dx;
            sub     ebx, 'VMXh';
            sete    al;
            movzx   eax, al;
            mov     Result, eax;
        }
    }
    SEH_EXCEPT(EXCEPTION_EXECUTE_HANDLER)
    {
        Result = FALSE;
    }

    return Result;
}

#endif

VOID PrintLocaleDefaultAnsiCodePage()
{
    WCHAR Buffer[8];
    GetLocaleInfoW(GetUserDefaultLangID(), LOCALE_IDEFAULTANSICODEPAGE, Buffer, countof(Buffer));
    PrintConsole(L"%s\n", Buffer);
    PauseConsole();

    Ps::ExitProcess(0);
}

#include <vector>
#include <map>

using namespace std;

VOID setcpu(ULONG_PTR Percent, ULONG_PTR ProcessMask)
{
    HANDLE BusyThread;

    NtSetInformationProcess(CurrentProcess, ProcessAffinityMask, &ProcessMask, sizeof(ProcessMask));

    Ps::CreateThreadT(
        [](PVOID)
        {
            for (;;);
            return 0;
        },
        nullptr,
        TRUE,
        CurrentProcess,
        &BusyThread
    );

    ULONG_PTR BusyTime, IdleTime;

    Percent = ML_MAX(Percent, 0);
    Percent = ML_MIN(Percent, 100);
    BusyTime = Percent * 10;
    IdleTime = 1000 - BusyTime;

    LOOP_FOREVER
    {
        NtResumeThread(BusyThread, nullptr);
        WaitForSingleObject(BusyThread, BusyTime);
        NtSuspendThread(BusyThread, nullptr);
        Ps::Sleep(IdleTime);
    }
}

VOID setcpu2(ULONG_PTR Percent, ULONG_PTR ProcessMask)
{
    HANDLE BusyThread;

    NtSetInformationProcess(CurrentProcess, ProcessAffinityMask, &ProcessMask, sizeof(ProcessMask));

    ULONG_PTR BusyTime, IdleTime;

    Percent = ML_MAX(Percent, 0);
    Percent = ML_MIN(Percent, 100);
    BusyTime = Percent * 10;
    IdleTime = 1000 - BusyTime;

    LOOP_FOREVER
    {
        ULONG64 start = NtGetTickCount();

        while (NtGetTickCount() - start <= BusyTime);
        Ps::Sleep(IdleTime);
    }
}

#include "mlpython.h"

void test_void_void0()
{
    PrintConsole(L"%S\n", __FUNCTION__);
}

void FASTCALL test_void_uptr1(ULONG_PTR a)
{
    PrintConsole(L"%S: %Iu\n", __FUNCTION__, a);
}

void CDECL test_void_uptr2(ULONG_PTR a, ULONG_PTR b)
{
    PrintConsole(L"%S: %Iu, %Iu\n", __FUNCTION__, a, b);
}

ULONG NTAPI test_ulong_uptr3(ULONG_PTR a, ULONG_PTR b, ULONG_PTR c)
{
    return PrintConsole(L"%S: %Iu, %Iu, %Iu\n", __FUNCTION__, a, b, c);
}

struct test_class
{
    int dummy;
    int member;

    test_class(int m)
    {
        member = m;
    }

    static long static_func()
    {
        return 0;
    }

    void set_member(int m)
    {
        member = m;
    }

    long long_void()
    {
        return PrintConsole(L"%S, %u\n", __FUNCTION__, this->member);
    }

    VOID void_void()
    {
        PrintConsole(L"%S, %u\n", __FUNCTION__, this->member);
    }

    ml::String __repr__()
    {
        return L"FUCK";
    }
};

template<typename wchar_t*>
struct fuck
{
    ;
};

void quick_sort(int *array, int count)
{
    int *left, *right, base;

    left = array;
    right = &array[count - 1];

    if (left > right)
        return;

    base = *left;

    while (left < right)
    {
        while (*right >= base && left < right)
            --right;

        while (*left <= base && left < right)
            ++left;

        if (left < right)
            Swap(*left, *right);
    }

    Swap(*array, *left);

    quick_sort(array, left - array);

    ++left;
    quick_sort(left, &array[count] - left);
}

//#define IMPORT_LIBLLDB 1

#include "iTunes/iTunes.h"
#include "lldb/API/LLDB.h"

#pragma comment(lib, "liblldb.lib")

using namespace lldb;

ForceInline VOID main2(LONG_PTR argc, PWSTR *argv)
{
    NTSTATUS Status;

    SBDebugger::Initialize();

    {
        SBDebugger dbg;

        dbg.SetCurrentPlatform("remote-ios");

        dbg.GetCommandInterpreter().GetProcess().IsValid();
    }

    SBDebugger::Terminate();

    Ps::ExitProcess(0);

    return;

#if 0

    ml::MlInitialize();

    LONG_PTR& a = argc;

    argc = 123;

    MlPython py;

    py.Initialize();

    py.Register(test_void_void0, L"test_void_void0")
      .Register(
        [&](ULONG_PTR a)
        {
            argc = a;
            return PrintConsole(L"%S: %d\n", __FUNCTION__, a);
        },
        L"test_void_uptr1"
    )
    .AddToModule(L"mlpy");

    py.Register(test_void_uptr2, L"test_void_uptr2")
      .Register(test_ulong_uptr3, L"test_void_uptr3")
      .AddToModule(L"mlpy");

    py.RegisterClass<test_class, VOID(int)>(L"test_class")
      .RegisterMethod(&test_class::set_member, L"set_member")
      .RegisterMethod(&test_class::long_void, L"long_void")
      .RegisterMethod(&test_class::void_void, L"void_void")
      .RegisterProperty(&test_class::member, L"member")
      .AddToModule(L"mlpy");

    MlPyObject func = py.Invoke<PyObject *>(L"fuck - Copy", L"getfunc");

    PrintConsole(L"%u\n", py.Invoke<ULONG>(func));

    auto ret = py.Invoke<ULONG>(L"fuck", L"main", 1, 2, 3, 4, 5);

    PrintConsole(L"ret = %u argc = %u\n", ret, argc);

    if (py.GetPyException().ErrorOccurred())
        PrintConsole(L"%s\n", py.GetPyException().Message);

#endif

    PauseConsole();

    return;

#if 0

    SC_HANDLE       ScManager, Service, Themes;
    SERVICE_STATUS  ServiceStatus;
    WCHAR           DriverPath[MAX_NTPATH];

    ScManager   = NULL;
    Service     = NULL;

    RtlWow64EnableFsRedirection(FALSE);
    ScManager = OpenSCManagerW(NULL, NULL, SC_MANAGER_CREATE_SERVICE);
    if (ScManager == NULL)
        return;

    PrintConsoleW(L"open scmgr\n");
    Status = STATUS_UNSUCCESSFUL;

    SCOPE_EXIT
    {
        if (Service != NULL)
        {
            if (!NT_SUCCESS(Status))
            {
                ControlService(Service, SERVICE_CONTROL_STOP, &ServiceStatus);
                DeleteService(Service);
            }
            CloseServiceHandle(Service);
        }

        if (ScManager != NULL)
            CloseServiceHandle(ScManager);

        PauseConsole();
        Nt_ExitProcess(0);
    }
    SCOPE_EXIT_END;

    Service = OpenServiceW(ScManager, BYPASS_UAC_SERVICE_NAME, SERVICE_ALL_ACCESS);

    PrintConsoleW(L"open svr\n");
    if (Service == NULL)
    {
        static WCHAR drv[] = BYPASS_UAC_DRIVER_NAME;
        CopyStruct(DriverPath + Nt_GetExeDirectory(DriverPath, countof(DriverPath)), drv, sizeof(drv));

        Service = CreateServiceW(
                        ScManager,
                        BYPASS_UAC_SERVICE_NAME,
                        BYPASS_UAC_SERVICE_NAME,
                        SERVICE_ALL_ACCESS,
                        SERVICE_KERNEL_DRIVER,
                        SERVICE_BOOT_START,
                        SERVICE_ERROR_IGNORE,
                        DriverPath,
                        NULL,
                        NULL,
                        NULL,
                        NULL,
                        NULL
                  );

        PrintConsoleW(L"create svr\n");
        if (Service == NULL)
            return;
    }

    if (!StartServiceW(Service, 0, NULL) && RtlGetLastWin32Error() != ERROR_SERVICE_ALREADY_RUNNING)
    {
        PrintConsoleW(L"lasterr %d\n", RtlGetLastWin32Error());
        return;
    }

    PrintConsoleW(L"start svr\n");
    Status = 0;

    return;

    NtFileDisk Device;

    Status = Device.OpenDevice(SHADOW_SYSCALL_DEVICE_SYMBOLIC);
    if (!NT_SUCCESS(Status))
        return;

    SS_PROBE_DEBUG_PORT Pdp;
    CONTEXT Context;
    ULONG_PTR CC;
    ULONG_PTR RemoteBase;
    HANDLE Thread;

    PROCESS_INFORMATION pi;

    if (!NT_SUCCESS(Nt_CreateProcess(NULL, Nt_CurrentPeb()->ProcessParameters->ImagePathName.Buffer, NULL, NULL, CREATE_SUSPENDED, NULL, &pi)))
        return;

    Context.ContextFlags = CONTEXT_ALL;
    NtGetContextThread(pi.hThread, &Context);

    RemoteBase = PtrSub(Context.Eax, PtrOffset(main2, &__ImageBase));

//    Nt_CreateThread((PVOID)(RemoteBase + PtrOffset(StubThread, &__ImageBase)), NULL, TRUE, pi.hProcess, &Thread);
//    Nt_WriteMemory(pi.hProcess, (PVOID)(Context.Esp + sizeof(PVOID)), &Thread, sizeof(Thread));
    Context.Eax = RemoteBase + PtrOffset(UnMapSectionThread, &__ImageBase);
    NtSetContextThread(pi.hThread, &Context);

    Pdp.DebugProcessId  = pi.dwProcessId;
    Pdp.DebugThreadId   = pi.dwThreadId;
    Pdp.UserContext     = &Context;

    Status = Device.DeviceIoControl(IOCTL_PROBE_DEBUG_PORT_ADDRESS, &Pdp, sizeof(Pdp), NULL, 0);
    PrintConsoleW(L"IOCTL_PROBE_DEBUG_PORT_ADDRESS: %08X\n", Status);

    NtTerminateProcess(pi.hProcess, 0);
    NtClose(pi.hProcess);
    NtClose(pi.hThread);

    PauseConsole();

    return;

#endif

#if 0
    INT   Height;
    HDC   hDC;
    HFONT hFont;
    BYTE  Buffer[0x5000];
    GLYPHMETRICS gm;
    MAT2 mat = { { 0, 1 }, { 0, 0 }, { 0, 0 }, { 0, 1 } };

    _wsetlocale(LC_CTYPE, L"");
    Height = 50;

#if 0
    ULONG BitsPerRow = 0x3E;
    PBYTE p = BitMap + sizeof(BitMap) - ROUND_UP(BitsPerRow / 8, 4);
    for (ULONG i = Height; i; --i)
    {
        PBYTE bak = p;
        for (ULONG j = BitsPerRow / 8; j; --j)
        {
            BYTE b = *p++;
            TEST_BIT(b, 7) ? printf("@") : printf(" ");
            TEST_BIT(b, 6) ? printf("@") : printf(" ");
            TEST_BIT(b, 5) ? printf("@") : printf(" ");
            TEST_BIT(b, 4) ? printf("@") : printf(" ");
            TEST_BIT(b, 3) ? printf("@") : printf(" ");
            TEST_BIT(b, 2) ? printf("@") : printf(" ");
            TEST_BIT(b, 1) ? printf("@") : printf(" ");
            TEST_BIT(b, 0) ? printf("@") : printf(" ");
        }
        p = bak - ROUND_UP(BitsPerRow / 8, 4);
        printf("#\n");
    }

//    return;

#endif

    hDC = CreateCompatibleDC(NULL);
    hFont = CreateFontW(
                Height,
                0,
                0,
                0,
                FW_NORMAL,
                0,
                0,
                0,
                GB2312_CHARSET,
                0,
                0,
                ANTIALIASED_QUALITY,
                FIXED_PITCH,
                L"ºÚÌå");
    SelectObject(hDC, hFont);
    WCHAR c = L'´ô';
    GetGlyphOutlineW(hDC, c, GGO_GRAY8_BITMAP, &gm, sizeof(Buffer), Buffer, &mat);

    INT nBytesPerLine;
    PBYTE pbBuffer = Buffer;

    printf(
        "Height             = %08X\n"
        "gmBlackBoxX        = %08X\n"
        "gmBlackBoxY        = %08X\n"
        "gmptGlyphOrigin.x  = %08X\n"
        "gmptGlyphOrigin.y  = %08X\n"
        "gmCellIncX         = %08X\n"
        "gmCellIncY         = %08X\n"
        "=========================\n",
        Height, gm.gmBlackBoxX, gm.gmBlackBoxY, gm.gmptGlyphOrigin.x, gm.gmptGlyphOrigin.y,
        gm.gmCellIncX, gm.gmCellIncY);

    nBytesPerLine = ROUND_UP(gm.gmBlackBoxX, sizeof(DWORD));

#if 0
    int nByteCount = ((gm.gmBlackBoxX +31) >> 5) << 2;
//    nByteCount = ROUND_UP(gm.gmBlackBoxX / 8, 8);
//    printf("%08X\n", nByteCount);

    PBYTE p1 = Buffer + (gm.gmBlackBoxY - 1) * nByteCount;
    p1 = Buffer;

    for (int i = ROUND_UP(gm.gmptGlyphOrigin.y, 32) / 8; i; --i)
        printf("\n");

    for ( int i = 0; i < gm.gmBlackBoxY; i++)
    {
        for (int j = gm.gmptGlyphOrigin.x; j; --j)
            printf(" ");

        PBYTE bak = p1;
        for (int j = 0; j < nByteCount; j++)
        {
            BYTE b;
            b = *p1++;
            TEST_BIT(b, 7) ? printf("@") : printf(" ");
            TEST_BIT(b, 6) ? printf("@") : printf(" ");
            TEST_BIT(b, 5) ? printf("@") : printf(" ");
            TEST_BIT(b, 4) ? printf("@") : printf(" ");
            TEST_BIT(b, 3) ? printf("@") : printf(" ");
            TEST_BIT(b, 2) ? printf("@") : printf(" ");
            TEST_BIT(b, 1) ? printf("@") : printf(" ");
            TEST_BIT(b, 0) ? printf("@") : printf(" ");
        }
//        p1 = bak - nByteCount;
        printf("#\n");
    }

    for (int i = (Height - gm.gmBlackBoxY) / 8; i; --i)
        printf("\n");

#else

    for (int j = 0; j != gm.gmBlackBoxY; ++j)
    {
        for (int i = 0; i != nBytesPerLine; ++i)
        {
            char c = *pbBuffer++;
            if (c > 31 && i < Height)
                printf("@");
            else
                printf(" ");
        }

        printf("#\n");
    }
#endif
#endif
    return;

/*
    HANDLE hFile, hMap;
    PBYTE  pbImage;
    PULONG_PTR pRVA;
    hFile = CreateFileW(
                name,
                GENERIC_READ|GENERIC_WRITE,
                FILE_SHARE_READ,
                NULL,
                OPEN_EXISTING,
                FILE_ATTRIBUTE_NORMAL,
                NULL);
    if (hFile == INVALID_HANDLE_VALUE)
        return;

    hMap = CreateFileMappingW(hFile, NULL, PAGE_READWRITE, 0, 0, NULL);
    CloseHandle(hFile);
    if (hMap == NULL)
        return;

    pbImage = (PBYTE)MapViewOfFile(hMap, FILE_MAP_READ|FILE_MAP_WRITE, 0, 0, 0);
    CloseHandle(hMap);
    if (pbImage == NULL)
        return;

    pRVA = (PULONG_PTR)(pbImage + 0x21440C);
    for (DWORD i = 266; i; --i)
    {
        if (*pRVA)
            *pRVA = *pRVA - 0x214400 + 0x21D000;
        else
            break;
        pRVA += 5;
    }

    UnmapViewOfFile(pbImage);
*/
}

int CDECL main(Long_Ptr argc, TChar **argv)
{
//    MyLib_Initialize();
//    my_initterm(&__xi_a, &__xi_z);
//    my_initterm(&__xc_a, &__xc_z);
    getargs(&argc, &argv);
    main2(argc, argv);

//    MyLib_UnInitialize();

    Ps::ExitProcess(0);
}

#if 0
Void FASTCALL ExtractSubtitles(Int argc, PWChar *argv)
{
    UInt32 cur;
    WChar path[MAX_PATH];
    HANDLE hPipeRead, hPipeWrite;
    STARTUPINFOW si;
    PROCESS_INFORMATION pi;
    SECURITY_ATTRIBUTES sa;

    if (argc < 2)
        return;
/*
    cur = GetModuleFileNameW(0, path, countof(path));
    while (path[--cur] != '\\');
    path[++cur] = 0;
*/

    _wsetlocale(LC_CTYPE, L"");

    sa.nLength = sizeof(sa);
    sa.lpSecurityDescriptor = NULL;
    sa.bInheritHandle = True;

    ZeroMemory(&si, sizeof(si));
    si.cb = sizeof(si);

    wcscpy(path, L"G:\\x\\mkvtoolnix\\mkvinfo.exe");
    cur = wcslen(path);
    for (Int i = 1; i != argc; ++i)
    {
        if (CreatePipe(&hPipeRead, &hPipeWrite, &sa, 0x2000) == False)
        {
            PrintError(GetLastError());
            continue;
        }

        si.dwFlags = STARTF_USESTDHANDLES;
        si.hStdOutput = hPipeWrite;
        swprintf(path + cur, L" \"%s\"", *++argv);
        if (CreateProcessW(NULL, path, NULL, NULL, True, 0, NULL, NULL, &si, &pi) == False)
        {
            PrintError(GetLastError());
            CloseHandle(hPipeWrite);
            CloseHandle(hPipeRead);
            continue;
        }

        WaitForSingleObjectEx(pi.hProcess, INFINITE, False);
        CloseHandle(pi.hProcess);
        CloseHandle(pi.hThread);
        CloseHandle(hPipeWrite);

        PChar pBuf, p1;
        DWORD dwRead, dwAvail;

        if (PeekNamedPipe(hPipeRead, 0, 0, NULL, &dwAvail, NULL))
        {
            pBuf = (PChar)malloc(dwAvail + 4);
            p1 = pBuf;
            ReadFile(hPipeRead, pBuf, dwAvail, &dwRead, NULL);
            *(PUInt32)&pBuf[dwRead] = 0;

            UInt32 count, n;
            PChar psubid, p;
            WChar cmd[MAX_PATH * 3];

            n = 0;
            count = swprintf(cmd, L"%s\"%s\" ", L"G:\\x\\mkvtoolnix\\mkvextract.exe tracks ", *argv);
            rmextw(*argv);
            while (psubid = strstr(pBuf, "Track type: subtitles"))
            {
                p = pBuf;
                pBuf = psubid + 1;
                psubid = StrRStrIA(p, psubid, "Track number:");
                if (psubid == NULL)
                    continue;

                if (sscanf(psubid, "Track number: %u", &dwRead) != 1)
                    continue;

                PCWChar fmt, param;
                static WChar *lang[] = { L"sc", L"tc", L"jp" };

                count += swprintf(cmd + count, L"%u:\"%s.", dwRead, *argv);

                if (n >= 0 && n < countof(lang))
                {
                    fmt = L"%s.ass\" ";
                    param = lang[n];
                }
                else
                {
                    fmt = L"%u.ass\" ";
                    param = (PCWChar)n;
                }

                count += swprintf(cmd + count, fmt, param);
                ++n;
            }

            si.dwFlags = 0;
            if (n && CreateProcessW(NULL, cmd, 0, 0, 0, 0, 0, 0, &si, &pi))
            {
                WaitForSingleObjectEx(pi.hProcess, INFINITE, False);
                CloseHandle(pi.hThread);
                CloseHandle(pi.hProcess);
            }

            free(p1);
        }

        CloseHandle(hPipeRead);
    }
}

#endif





#if 0



// #include "JsonParser.h"

HANDLE g_hHeap;

typedef struct
{
    TYPE_OF(NtWaitForSingleObject)  *NtWaitForSingleObject;
    TYPE_OF(DeleteFileW)            *DeleteFileW;
    TYPE_OF(NtTerminateProcess)     *NtTerminateProcess;
    TYPE_OF(NtClose)                *NtClose;

    HANDLE ProcessHandle;
    WCHAR  FullPath[1];

} DELETE_SELF_INFO, *PDELETE_SELF_INFO;

#if !ML_AMD64

VOID FASTCALL DeleteSelfImpl(PDELETE_SELF_INFO dsi)
{
    INLINE_ASM
    {
        call SELF_LOCATE;
SELF_LOCATE:
        pop eax;
        and eax, not (MEMORY_PAGE_SIZE - 1);
        mov dsi, eax;
    }

    dsi->NtWaitForSingleObject(dsi->ProcessHandle, FALSE, NULL);
    dsi->NtClose(dsi->ProcessHandle);
    dsi->DeleteFileW(dsi->FullPath);
    dsi->NtTerminateProcess(NtCurrentProcess(), 0);
}

ASM VOID DeleteSelfImplEnd() {}

VOID DeleteSelf()
{
    NTSTATUS            Status;
    ULONG               Length;
    WCHAR               path[MAX_PATH];
    STARTUPINFOW        si;
    PROCESS_INFORMATION pi;
    DELETE_SELF_INFO    dsi, *pdsi;
    CONTEXT             Context;
    PVOID               FuncAddress;

    CopyStruct(path + Nt_GetSystemDirectory(path, countof(path)), L"\\cmd.exe", sizeof(L"\\cmd.exe"));
    ZeroMemory(&si, sizeof(si));
    si.cb = sizeof(si);

//    pi.hProcess = NtCurrentProcess();
//    pi.hThread = NtCurrentThread();
    Status = Nt_CreateProcess(NULL, path, NULL, CREATE_SUSPENDED, NULL, &pi);
    if (!NT_SUCCESS(Status))
        return;

    pdsi = NULL;
    Status = Nt_AllocateMemory(pi.hProcess, (PVOID *)&pdsi, 0x1000);

    NtDuplicateObject(
        NtCurrentProcess(),
        NtCurrentProcess(),
        pi.hProcess,
        &dsi.ProcessHandle,
        0,
        FALSE,
        DUPLICATE_SAME_ACCESS
    );

    dsi.NtWaitForSingleObject   = NtWaitForSingleObject;
    dsi.DeleteFileW             = DeleteFileW;
    dsi.NtTerminateProcess      = NtTerminateProcess;
    dsi.NtClose                 = NtClose;

    Nt_WriteMemory(pi.hProcess, pdsi, &dsi, sizeof(dsi), (PSIZE_T)&Length);
    Length = Nt_GetModuleFileName(NULL, path, countof(path));
    Nt_WriteMemory(pi.hProcess, pdsi->FullPath, path, (Length + 1) * sizeof(WCHAR), (PSIZE_T)&Length);

    FuncAddress = (PBYTE)&pdsi->FullPath + Length;
    Nt_WriteMemory(
        pi.hProcess,
        FuncAddress,
        DeleteSelfImpl,
        (ULONG_PTR)DeleteSelfImplEnd - (ULONG_PTR)DeleteSelfImpl,
        (PSIZE_T)&Length
    );

    Context.ContextFlags = CONTEXT_CONTROL;
    NtGetContextThread(pi.hThread, &Context);
    Context.Eip = (ULONG_PTR)FuncAddress;
    Context.Ecx = (ULONG_PTR)pdsi;
    NtSetContextThread(pi.hThread, &Context);

    NtResumeThread(pi.hThread, NULL);
    NtClose(pi.hProcess);
    NtClose(pi.hThread);
}

#endif // x86

#if 0

#include "json-c/json.h"
#include "json-c/json_object_private.h"

#include "E:/Desktop/Source/GUI/Celestial Globe/Internal/CG_Script.h"

#define CG_SCRIPT_CONFIG_ROOT_TAG       L"CoreConfig"
#define CG_SCRIPT_CONFIG_UI_MODULE      L"UIModule"
#define CG_SCRIPT_CONFIG_IMAGE_PLUGIN   L"ImagePlugin"
#define CG_SCRIPT_CONFIG_CATEGORY       L"Category"
#define CG_SCRIPT_CONFIG_CATEGORY_LIST  L"List"

#define CG_SCRIPT_GAMELIST_ROOT_TAG     L"GameList"

#define PARSE_SCRIPT_CHECK_BUFFER_SIZE(size, info) \
            if ((size) < sizeof(info)) \
                return STATUS_BUFFER_TOO_SMALL

CGSTATUS
ParseCoreConfig(
    JSON_OBJECT            *Script,
    CG_SCRIPT_CORE_CONFIG  *CoreConfig,
    ULONG                   InfoSize
)
{
    CGSTATUS     Status;
    JSON_OBJECT *Object, *CategoryObject, *CategoryItem;
    CG_GAME_CATEGORY_ENTRY *CategoryEntry;

    PARSE_SCRIPT_CHECK_BUFFER_SIZE(InfoSize, CoreConfig);

    ZeroMemory(CoreConfig, sizeof(*CoreConfig));
    CoreConfig->ScriptType = CG_SCRIPT_TYPE_CONFIG;

    Status = STATUS_SUCCESS;
    Object = Script->Value.Object.Object;
    for (ULONG Count = Script->Value.Object.Count; Count; ++Object, --Count)
    {
        if (!StrICompareW(Object->Name.Buffer, CG_SCRIPT_CONFIG_CATEGORY))
        {
            if (Object->Type != JSON_TYPE_OBJECT)
            {
                Status = STATUS_UNSUCCESSFUL;
                break;
            }

            CoreConfig->Category.Count = Object->Value.Object.Count;
            CategoryEntry = (CG_GAME_CATEGORY_ENTRY *)malloc(sizeof(*CategoryEntry) * CoreConfig->Category.Count);
            if (CategoryEntry == NULL)
            {
                Status = STATUS_NO_MEMORY;
                break;
            }

            CoreConfig->Category.pCategory = CategoryEntry;

            CategoryObject = Object->Value.Object.Object;
            for (ULONG Count = Object->Value.Object.Count; Count; --Count)
            {
                if (CategoryObject->Type != JSON_TYPE_OBJECT)
                    continue;

                CategoryItem = CategoryObject->Value.Object.Object;
                RtlCreateUnicodeString(&CategoryEntry->Name, CategoryObject->Name.Buffer);
                for (ULONG ItemCount = CategoryObject->Value.Object.Count; ItemCount; --ItemCount)
                {
                    if (!StrICompareW(CategoryItem->Name.Buffer, CG_SCRIPT_CONFIG_CATEGORY_LIST))
                    {
                        if (CategoryItem->Type != JSON_TYPE_STRING)
                            continue;

                        RtlCreateUnicodeString(
                            &CategoryEntry->ScriptPath,
                            CategoryItem->Value.String.Buffer
                        );
                    }
                }

                ++CategoryObject;
                ++CategoryEntry;
            }
        }
        else if (!StrICompareW(Object->Name.Buffer, CG_SCRIPT_CONFIG_UI_MODULE))
        {
            RtlCreateUnicodeString(&CoreConfig->UIModule, Object->Value.String.Buffer);
        }
    }

    return Status;
}

CGSTATUS FreeScript(CG_SCRIPT_BASE *ScriptInfo)
{
    union
    {
        CG_SCRIPT_BASE          *Base;
        CG_SCRIPT_CORE_CONFIG   *CoreConfig;
        CG_SCRIPT_PLUGIN        *Plugin;
    };

    CGSTATUS Status;
    CG_GAME_CATEGORY_ENTRY *pCategory;

    Status = STATUS_SUCCESS;
    Base = ScriptInfo;
    switch (Base->ScriptType)
    {
        case CG_SCRIPT_TYPE_CONFIG:
            RtlFreeUnicodeString(&CoreConfig->UIModule);
            RtlFreeUnicodeString(&CoreConfig->ImagePlugin);

            pCategory = CoreConfig->Category.pCategory;
            for (ULONG Count = CoreConfig->Category.Count; Count; ++pCategory, --Count)
            {
                RtlFreeUnicodeString(&pCategory->Name);
                RtlFreeUnicodeString(&pCategory->ScriptPath);
            }

            free(CoreConfig->Category.pCategory);
            break;
    }

    ZeroMemory(CoreConfig, sizeof(*CoreConfig));

    return Status;
}

CGSTATUS
ParseScript(
    PVOID           Script,
    ULONG           ScriptSize,
    CG_SCRIPT_BASE *ScriptInfo,
    ULONG           InfoSize
)
{
    CGSTATUS    Status;
    JSON_OBJECT Object, *ScriptObject;
    CJsonParser JsonParser;

    Status = JsonParser.Parse(Script, ScriptSize, &Object);
    if (!CG_SUCCESS(Status))
        return Status;

    Status = STATUS_UNSUCCESSFUL;
    LOOP_ONCE
    {
        if (Object.Type != JSON_TYPE_OBJECT ||
            Object.Value.Object.Count < 1   ||
            Object.Value.Object.Object->Type != JSON_TYPE_OBJECT)
        {
            break;
        }

        ScriptObject = Object.Value.Object.Object;
        if (!StrICompare(ScriptObject->Name.Buffer, CG_SCRIPT_CONFIG_ROOT_TAG))
        {
            Status = ParseCoreConfig(ScriptObject, (CG_SCRIPT_CORE_CONFIG *)ScriptInfo, InfoSize);
        }
        else if (StrICompareW(ScriptObject->Name.Buffer, CG_SCRIPT_GAMELIST_ROOT_TAG))
        {
            ;
        }
    }

    JsonParser.Destroy(&Object);
    if (!CG_SUCCESS(Status))
        FreeScript(ScriptInfo);

    return Status;
}

#endif

#if 0

#define _JUNK_CODE(label, junk_bytes) \
            label: INLINE_ASM push label + 0xC3654321 + 0xE + junk_bytes \
            INLINE_ASM sub  dword ptr [esp], 0xC3654321 - junk_bytes + 4 \
            INLINE_ASM __emit 0xEB INLINE_ASM __emit 0xFD \
            INLINE_ASM __emit 0x28

#define JUNK_CODE() _JUNK_CODE(MAKE_UNIQUE_NAME(__COUNTER__), 1)

PCHAR SkipSpace(PCHAR p, BOOL Forward)
{
    ULONG delta = Forward ? 1 : -1;

    while (*p == ' ' || *p == '\t')
        p += delta;

    return p;
}

VOID AntiDllInject()
{
    ULONG Version, ClientLoadDllIndex;

    Version = 500;
    switch (Version)
    {
        case 500:
            ClientLoadDllIndex = 0x40;
            break;

        case 501:
        case 600:
            ClientLoadDllIndex = 0x42;
            break;

        case 601:
            ClientLoadDllIndex = 0x41;
            break;

        default:
            return;
    }
}

#define HANDLE_INDEX_MASK 0xFC000000u

template<class HandleType>
class HandleTableManager
{
protected:
    RTL_HANDLE_TABLE m_HandleTable;

    const static ULONG m_kHandleSize = sizeof(HandleType);

public:
    HandleTableManager()
    {
        ZeroMemory(&m_HandleTable, sizeof(m_HandleTable));
    }

    HandleTableManager(ULONG MaximumHandleCount)
    {
        Initialize(MaximumHandleCount);
    }

    ~HandleTableManager()
    {
        RtlDestroyHandleTable(&m_HandleTable);
    }

    VOID Initialize(ULONG MaximumHandleCount)
    {
        RtlInitializeHandleTable(
            MaximumHandleCount * m_kHandleSize,
            m_kHandleSize,
            &m_HandleTable
        );
    }

    HANDLE AllocateHandle(PRTL_HANDLE_TABLE_ENTRY *Object = NULL)
    {
        ULONG_PTR Handle;
        PRTL_HANDLE_TABLE_ENTRY Entry;

        if (Object != NULL)
            *Object = NULL;

        Entry = RtlAllocateHandle(&m_HandleTable, &Handle);
        if (Entry == NULL)
            return NULL;

        SET_FLAG(Entry->Flags, RTL_HANDLE_VALID);

        if (Object != NULL)
            *Object = Entry;

        return GetHandleByIndex(Handle);
    }

    BOOL ReferenceObjectByHandle(HANDLE Handle, HandleType **Object)
    {
        return IsValidHandle(Handle, (PVOID *)Object);
    }

    BOOL FreeHandle(HandleType *Object)
    {
        if (!RtlIsValidHandle(&m_HandleTable, (PRTL_HANDLE_TABLE_ENTRY)Object))
            return FALSE;

        return RtlFreeHandle(&m_HandleTable, (PRTL_HANDLE_TABLE_ENTRY)Object);
    }

    BOOL FreeHandle(HANDLE Handle)
    {
        HandleType *Object;

        if (!ReferenceObjectByHandle(Handle, &Object))
            return FALSE;

        return FreeHandle(Object);
    }

protected:
    BOOL IsValidHandle(HANDLE Handle, PVOID *Object = NULL)
    {
        ULONG_PTR Index;

        if (Handle == NULL || PtrAnd(Handle, 3) != 0)
            return FALSE;

        Index = GetIndexByHandle(Handle);

        return IsValidIndexHandle(Index, Object);
    }

    BOOL IsValidIndexHandle(ULONG_PTR Index, PVOID *Object = NULL)
    {
        PRTL_HANDLE_TABLE_ENTRY Entry;

        if (Object == NULL)
            Object = (PVOID *)&Entry;

        return RtlIsValidIndexHandle(&m_HandleTable, Index, (PRTL_HANDLE_TABLE_ENTRY *)Object);
    }

    ULONG_PTR GetIndexByHandle(HANDLE Handle)
    {
        return (ULONG_PTR)Handle / 4 - 1;
    }

    HANDLE GetHandleByIndex(ULONG_PTR Index)
    {
        return (HANDLE)(++Index * 4);
    }
};

struct HANDLE_OBJECT
{
    enum HandleObjectTypeClass
    {
        ObjectFile,
    };

    ULONG RefCount;
    ULONG Flags;        // HANDLE_FLAG_PROTECT_FROM_CLOSE
    ULONG ObjectType;

    union
    {
        struct
        {
            UNICODE_STRING  FileName;
            LARGE_INTEGER   FileSize;
            LARGE_INTEGER   CurrentPosition;
        } FileObject;

    } Data;

    HANDLE_OBJECT()
    {
        RefCount    = 1;
        Flags       = 0;
    }

    ULONG AddRef()
    {
        return _InterlockedIncrement((PLONG)&RefCount);
    }

    ULONG Release()
    {
        ULONG Ref;

        Ref = _InterlockedDecrement((PLONG)&RefCount);
        if (Ref == 0)
            delete this;

        return Ref;
    }
};

DECL_ALIGN(8) struct HANDLE_ENTRY : public RTL_HANDLE_TABLE_ENTRY
{
    HANDLE_OBJECT *Object;
};

typedef enum
{
    RTMP_HEADER_LENGTH_12   = 0,
    RTMP_HEADER_LENGTH_8    = 1,
    RTMP_HEADER_LENGTH_4    = 2,
    RTMP_HEADER_LENGTH_1    = 3,

} RtmpHeaderLengthClass;

DECL_ALIGN(1) struct RTMP_HEADER
{
    union
    {
        struct
        {
            BYTE Type   : 6;
            BYTE Length : 2;
        };

        ULONG TimeStamp;
    };

    BYTE  AMFSize[3];
    BYTE  AMFType;
    ULONG StreamID;

    ULONG GetType()
    {
        return Type;
    }

    ULONG GetLength()
    {
        BYTE RtmpLengthMap[] = { 12, 8, 4, 1 };

        return Length > countof(RtmpLengthMap) ? -1 : RtmpLengthMap[Length];
    }

    ULONG GetLengthRaw()
    {
        return Length;
    }

    ULONG GetTimeStamp()
    {
        return Bswap(TimeStamp >> 8);
    }

    ULONG GetAMFSize()
    {
        ULONG Size = *(PULONG)AMFSize & 0xFFFFFF;

        return ((Size & 0xFF) << 16) | (Size & 0x0000FF00) | (Size >> 16);
    }

    ULONG GetAMFType()
    {
        return AMFType;
    }

    ULONG GetStreamID()
    {
        return Bswap(StreamID);
    }

    PVOID GetAMFData()
    {
        return PtrAdd((PVOID)this, GetLength());
    }
};

typedef enum
{
    AMF_TYPE_NUMBER         = 0x00,
    AMF_TYPE_BOOLEAN        = 0x01,
    AMF_TYPE_STRING         = 0x02,
    AMF_TYPE_OBJECT         = 0x03,
    AMF_TYPE_MOVIECLIP      = 0x04 ,
    AMF_TYPE_NULL           = 0x05,
    AMF_TYPE_UNDEFINED      = 0x06,
    AMF_TYPE_REFERENCE      = 0x07,
    AMF_TYPE_ECMA_ARRAY     = 0x08,
    AMF_TYPE_END_OF_OBJECT  = 0x09,
    AMF_TYPE_ARRAY          = 0x0A,
    AMF_TYPE_DATE           = 0x0B,
    AMF_TYPE_LONG_STRING    = 0x0C,
    AMF_TYPE_UNSUPPORTED    = 0x0D,
    AMF_TYPE_RECORDSET      = 0x0E,
    AMF_TYPE_XML            = 0x0F,
    AMF_TYPE_TYPED_OBJECT   = 0x10,
    AMF_TYPE_AMF3_OBJECT    = 0x11,

} AmfTypeClass;

#endif

#endif



















/*

void CPUUsage()
{
    SYSTEM_PERFORMANCE_INFORMATION SysPerfInfo;
    SYSTEM_TIME_INFORMATION SysTimeInfo;
    SYSTEM_BASIC_INFORMATION SysBaseInfo;
    DOUBLE dbIdleTime;
    LONG64 dbSystemTime;
    LONG status;
    LARGE_INTEGER liOldIdleTime = {0,0};
    LARGE_INTEGER liOldSystemTime = {0,0};

    // get number of processors in the system
    status = NtQuerySystemInformation(SystemBasicInformation,
        &SysBaseInfo, sizeof(SysBaseInfo), NULL);

    printf("CPU Usage\n");
    while(!_kbhit())
    {
        // get new system time
        NtQuerySystemInformation(SystemTimeInformation, &SysTimeInfo, sizeof(SysTimeInfo), 0);
        // get new CPU'sname idle time
        NtQuerySystemInformation(SystemPerformanceInformation,
            &SysPerfInfo, sizeof(SysPerfInfo), NULL);

        // if it'sname a first call-skip it
        if (liOldIdleTime.QuadPart != 0)
        {
            // CurrentValue = NewValue - OldValue
            dbIdleTime   = (DOUBLE)SysPerfInfo.liIdleTime.QuadPart - liOldIdleTime.QuadPart;
            dbSystemTime = SysTimeInfo.liKeSystemTime.QuadPart - liOldSystemTime.QuadPart;

            // CurrentCpuIdle = IdleTime / SystemTime
            dbIdleTime = dbIdleTime / dbSystemTime;

            // CurrentCpuUsage% = 100 - (CurrentCpuIdle * 100) / NumberOfProcessors
            dbIdleTime = 100.0 - dbIdleTime * 100.0 / SysBaseInfo.bKeNumberProcessors + 0.5;

            printf("%d%%             \r",(UINT)dbIdleTime);
        }

        // store new CPU'sname idle and system time
        liOldIdleTime = SysPerfInfo.liIdleTime;
        liOldSystemTime = SysTimeInfo.liKeSystemTime;

        // wait one second
        Sleep(1000);
    }
    printf("\n");
}
*/
// & > ^ > |


#else // global

#pragma comment(linker, "/ENTRY:main")

#include <Windows.h>
#include <functional>

NTSTATUS NTAPI NtClose2(HANDLE Handle);

NTSTATUS __cdecl main(HANDLE)
{
    std::function<decltype(NtClose2)> fuck = main;
}

#endif
