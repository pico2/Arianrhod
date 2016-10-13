#pragma comment(linker,"/ENTRY:DllMain")
#pragma comment(linker,"/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker,"/SECTION:.Amano,ERW /MERGE:.text=.Amano")
#pragma comment(linker, "/EXPORT:WTSFreeMemory=_PWTSFreeMemory@4")
#pragma comment(linker, "/EXPORT:WTSQuerySessionInformationW=_PWTSQuerySessionInformationW@0")
#pragma comment(linker, "/EXPORT:WTSUnRegisterSessionNotification=_PWTSUnRegisterSessionNotification@4")
#pragma comment(linker, "/EXPORT:WTSRegisterSessionNotification=_PWTSRegisterSessionNotification@8")
#pragma comment(linker, "/EXPORT:WTSQueryUserToken=_PWTSQueryUserToken@8")

#include "ml.cpp"
#include <windowsx.h>
#include <WtsApi32.h>

ML_OVERLOAD_NEW

LPWSTR g_pCmdLineW;
LPSTR  g_pCmdLineA;

API_POINTER(WTSFreeMemory)                      StubWTSFreeMemory;
API_POINTER(WTSQuerySessionInformationW)        StubWTSQuerySessionInformationW;
API_POINTER(WTSRegisterSessionNotification)     StubWTSRegisterSessionNotification;
API_POINTER(WTSUnRegisterSessionNotification)   StubWTSUnRegisterSessionNotification;
API_POINTER(LoadAcceleratorsW)                  StubLoadAcceleratorsW;
API_POINTER(WTSQueryUserToken)                  StubWTSQueryUserToken;
API_POINTER(PeekMessageW)                       StubPeekMessageW;

EXTC BOOL WINAPI PWTSQueryUserToken(ULONG SessionId, PHANDLE phToken)
{
    return StubWTSQueryUserToken(SessionId, phToken);
}

EXTC VOID WINAPI PWTSFreeMemory(PVOID Memory)
{
    return StubWTSFreeMemory(Memory);
}

EXTC BOOL WINAPI PWTSQuerySessionInformationW()
{
    return ((API_POINTER(PWTSQuerySessionInformationW))StubWTSQuerySessionInformationW)();
}

EXTC LONG WINAPI PWTSRegisterSessionNotification(HWND hWnd, DWORD Flags)
{
    return StubWTSRegisterSessionNotification(hWnd, Flags);
}

EXTC LONG WINAPI PWTSUnRegisterSessionNotification(HWND hWnd)
{
    return StubWTSUnRegisterSessionNotification(hWnd);
}

LPCWSTR MyGetCommandLineW()
{
    return g_pCmdLineW;
}

LPCSTR MyGetCommandLineA()
{
    return g_pCmdLineA;
}

#define KeyPressed(vk) (GetKeyState(vk) < 0)

typedef struct
{
    struct
    {
        ULONG Modifier;
        ULONG VirtualKey;
    } Original;

    struct
    {
        ULONG Modifier;
        ULONG VirtualKey;
    } Replacement;

} KEY_MAP, *PKEY_MAP;

KEY_MAP KeyMapTable[] =
{
    { { 0,      VK_F1   }, { FCONTROL,          VK_PRIOR    } },
    { { 0,      VK_F2   }, { FCONTROL,          VK_NEXT     } },
    { { 0,      VK_F4   }, { FCONTROL,          'W'         } },
    { { FALT,   'Z'     }, { FCONTROL | FSHIFT, 'T'         } },
    { { FALT,   'Q'     }, { FALT,              VK_HOME     } },
};

VOID SendKeyList(ULONG Modifier, PULONG VirtualKey, ULONG KeyCount, BOOL KeyDown)
{
    ULONG   Size, Flags, Count;
    PINPUT  inputs;

    Size = sizeof(*inputs) * (KeyCount + 3);
    inputs = (PINPUT)AllocStack(Size);

    Flags = KeyDown ? 0 : KEYEVENTF_KEYUP;

    Count = 0;
    ZeroMemory(inputs, Size);

    if (FLAG_ON(Modifier, FCONTROL))
    {
        inputs[Count].ki.wVk = VK_CONTROL;
        inputs[Count].ki.dwFlags = Flags;
        inputs[Count].type = INPUT_KEYBOARD;
        ++Count;
    }

    if (FLAG_ON(Modifier, FALT))
    {
        inputs[Count].ki.wVk = VK_MENU;
        inputs[Count].ki.dwFlags = Flags;
        inputs[Count].type = INPUT_KEYBOARD;
        ++Count;
    }

    if (FLAG_ON(Modifier, FSHIFT))
    {
        inputs[Count].ki.wVk = VK_SHIFT;
        inputs[Count].ki.dwFlags = Flags;
        inputs[Count].type = INPUT_KEYBOARD;
        ++Count;
    }

    FOR_EACH(VirtualKey, VirtualKey, KeyCount)
    {
        if (*VirtualKey == 0)
            continue;

        inputs[Count].ki.wVk = *VirtualKey;
        inputs[Count].ki.dwFlags = Flags;
        inputs[Count].type = INPUT_KEYBOARD;
        ++Count;
    }

    if (Count != 0)
        SendInput(Count, inputs, sizeof(inputs[0]));
}

VOID SendKey(ULONG Modifier, ULONG VirtualKey, BOOL KeyDown)
{
    SendKeyList(Modifier, &VirtualKey, 1, KeyDown);
}

BOOL TranslateKeyEvent(PMSG Msg, BOOL KeyDown)
{
    if (KeyDown == FALSE)
        return FALSE;

    if (FindThreadFrame(TAG4('TRKE')) != nullptr)
        return FALSE;

    PKEY_MAP KeyMap;
    TEB_ACTIVE_FRAME filter(TAG4('TRKE'));

    filter.Push();

    BOOL CtrlPressed, AltPressed, ShiftPressed;

    CtrlPressed = KeyPressed(VK_CONTROL);
    AltPressed = KeyPressed(VK_MENU);
    ShiftPressed = KeyPressed(VK_SHIFT);

    FOR_EACH_ARRAY(KeyMap, KeyMapTable)
    {
        if (FLAG_ON(KeyMap->Original.Modifier, FCONTROL) != CtrlPressed)
            continue;

        if (FLAG_ON(KeyMap->Original.Modifier, FALT) != AltPressed)
            continue;

        if (FLAG_ON(KeyMap->Original.Modifier, FSHIFT) != ShiftPressed)
            continue;

        if ((BYTE)Msg->wParam != KeyMap->Original.VirtualKey)
            continue;

        ULONG KeyToRelease[3], CtrlKeys[3];
        PULONG Key;

        ZeroMemory(KeyToRelease, sizeof(KeyToRelease));
        ZeroMemory(CtrlKeys, sizeof(CtrlKeys));

        if (FLAG_ON(KeyMap->Original.Modifier, FCONTROL))
            KeyToRelease[0] = VK_CONTROL;

        if (FLAG_ON(KeyMap->Original.Modifier, FALT))
            KeyToRelease[1] = VK_MENU;

        if (FLAG_ON(KeyMap->Original.Modifier, FSHIFT))
            KeyToRelease[2] = VK_SHIFT;

        if (FLAG_ON(KeyMap->Replacement.Modifier, FCONTROL))
            CtrlKeys[0] = VK_CONTROL;

        if (FLAG_ON(KeyMap->Replacement.Modifier, FALT))
            CtrlKeys[1] = VK_MENU;

        if (FLAG_ON(KeyMap->Replacement.Modifier, FSHIFT))
            CtrlKeys[2] = VK_SHIFT;

        SendKeyList(0, KeyToRelease, countof(KeyToRelease), FALSE);
        SendKey(KeyMap->Replacement.Modifier, KeyMap->Replacement.VirtualKey, TRUE);
        SendKey(KeyMap->Replacement.Modifier, KeyMap->Replacement.VirtualKey, FALSE);
        SendKeyList(0, KeyToRelease, countof(KeyToRelease), TRUE);

        return TRUE;
    }

    return FALSE;
}

BOOL NTAPI ChromePeekMessageW(LPMSG lpMsg, HWND hWnd, UINT wMsgFilterMin, UINT wMsgFilterMax, UINT wRemoveMsg)
{
    BOOL        Success, forward;
    LONG        X, Y, WheelDistance, fwKeys, vPixelsPerMm;
    POINT       point;

    static LONG LastDelta;

    Success = StubPeekMessageW(lpMsg, hWnd, wMsgFilterMin, wMsgFilterMax, wRemoveMsg);
    if (Success == FALSE || wRemoveMsg != PM_REMOVE)
        return Success;

    switch (lpMsg->message)
    {
        case WM_MOUSEWHEEL:
            //static int n = 0;
            if (lpMsg->hwnd == nullptr || GetParent(lpMsg->hwnd) != nullptr)
                break;

            fwKeys = GET_KEYSTATE_WPARAM(lpMsg->wParam);

            if (fwKeys != 0)
            {
                LastDelta = 0;
                break;
            }

            WheelDistance = GET_WHEEL_DELTA_WPARAM(lpMsg->wParam) / WHEEL_DELTA;
            LastDelta += ML_MAX(WheelDistance, 1);

            //AllocConsole();
            //PrintConsole(L"%04d: %d, %d\n", ++n, WheelDistance, LastDelta);
            if (abs(LastDelta) < 2)
                break;

            LastDelta = 0;

            point.x = GET_X_LPARAM(lpMsg->lParam);
            point.y = GET_Y_LPARAM(lpMsg->lParam);

            ScreenToClient(lpMsg->hwnd, &point);

            X = point.x;
            Y = point.y;
            //PrintConsole(L"%d, %d\n", X, Y);

            {
                HDC screen = GetDC(nullptr);
                vPixelsPerMm = GetDeviceCaps(screen, LOGPIXELSY) / 25;
                ReleaseDC(nullptr, screen);
            }

            //if (Y > GetSystemMetrics(SM_CYCAPTION))
            if (Y > (IsMaximized(lpMsg->hwnd) ? (10 * vPixelsPerMm) : (12 * vPixelsPerMm)))
                break;

            forward = WheelDistance > 0;
            SendKey(FCONTROL, forward ? VK_PRIOR : VK_NEXT, TRUE);
            SendKey(FCONTROL, forward ? VK_PRIOR : VK_NEXT, FALSE);
            break;

        case WM_SYSKEYDOWN:
        case WM_KEYDOWN:
            Success = !TranslateKeyEvent(lpMsg, TRUE);
            break;

        case WM_SYSKEYUP:
        case WM_KEYUP:
            Success = !TranslateKeyEvent(lpMsg, FALSE);
            break;
    }

    return Success;
}

VOID FuckDisableNewAvatarMenu(PLDR_MODULE chrome)
{
    using namespace Mp;

    static CHAR text[] = "disable-new-avatar-menu";

    PVOID push, firstCall, secondCall;

    push = SearchStringReference(chrome, text, sizeof(text));
    if (push == nullptr)
        return;

    push = PtrAdd(push, sizeof(push));
    firstCall = nullptr;
    secondCall = nullptr;

    WalkOpCodeT(push, 0x14,
        WalkOpCodeM(Buffer, OpLength, Ret)
        {
            switch (Buffer[0])
            {
                case CALL:
                    if (firstCall == nullptr)
                    {
                        firstCall = Buffer;
                        break;
                    }

                    secondCall = Buffer;
                    return STATUS_SUCCESS;
            }

            return STATUS_NOT_FOUND;
        }
    );

    if (secondCall == nullptr)
        return;

    auto fuckit = [](PCSTR) -> BOOL
    {
        return TRUE;
    };

    PATCH_MEMORY_DATA p[] =
    {
        FunctionCallVa(secondCall, (BOOL(NTAPI*)(PCSTR))fuckit),
    };

    PatchMemory(p, countof(p), chrome->DllBase);
}

VOID FuckExtensionDeveloperModeWarning(PLDR_MODULE chrome)
{
    using namespace Mp;

    PBYTE push;

    push = (PBYTE)SearchPatternSafe(L"84 C0 74 04 B0 01 ?? C3 E8 ?? ?? ?? ?? 83 F8 03 7D", chrome->DllBase, chrome->SizeOfImage);
    if (push == nullptr)
        return;

    PATCH_MEMORY_DATA p[] =
    {
        MemoryPatchVa(0ull, 1, push + 5),
    };

    PatchMemory(p, countof(p), chrome->DllBase);

/*
    static CHAR text[] = "ExtensionDeveloperModeWarning";

    push = (PBYTE)SearchStringReference(chrome, text, sizeof(text));
    if (push == IMAGE_INVALID_VA)
        return;

    --push;

    for (LONG_PTR length = 0x20; length > 0; --push, --length)
    {
        if ((*(PULONG)push & 0x00FFFFFF) != 0x00C301B0)
            continue;

        PATCH_MEMORY_DATA p[] =
        {
            MemoryPatchVa(0ull, 1, push + 1),
        };

        PatchMemory(p, countof(p), chrome->DllBase);
        break;
    }
*/
}

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    using namespace Mp;

    PLDR_MODULE module;
    SizeT       Length, Length2;
    LPWSTR      lpCmdLineW, pCmdLine;
    WChar       end, szCmdLine[MAX_PATH + 40];

    static WChar AddCmdLineHeadW[] = L" --user-data-dir=\"";
    static WChar AddCmdLineTailW[] = L"UserData\" --purge-memory-button";

    LdrDisableThreadCalloutsForDll(BaseAddress);

    Length = Nt_GetSystemDirectory(szCmdLine, countof(szCmdLine));
    CopyStruct(szCmdLine + Length, L"wtsapi32.dll", sizeof(L"wtsapi32.dll"));
    BaseAddress = Ldr::LoadDll(szCmdLine);

    *(PVOID *)&StubWTSFreeMemory                    = GetRoutineAddress(BaseAddress, "WTSFreeMemory");
    *(PVOID *)&StubWTSQuerySessionInformationW      = GetRoutineAddress(BaseAddress, "WTSQuerySessionInformationW");
    *(PVOID *)&StubWTSUnRegisterSessionNotification = GetRoutineAddress(BaseAddress, "WTSUnRegisterSessionNotification");
    *(PVOID *)&StubWTSRegisterSessionNotification   = GetRoutineAddress(BaseAddress, "WTSRegisterSessionNotification");
    *(PVOID *)&StubWTSQueryUserToken                = GetRoutineAddress(BaseAddress, "WTSQueryUserToken");

#if 0

    lpCmdLineW = Ps::GetCommandLine();

    Length = StrLengthW(lpCmdLineW);

    pCmdLine = szCmdLine;
    StrCopyW(pCmdLine, AddCmdLineHeadW);
    pCmdLine += countof(AddCmdLineHeadW) - 1;
    pCmdLine += Nt_GetExeDirectory(pCmdLine, countof(szCmdLine) - (pCmdLine - szCmdLine));
    StrCopyW(pCmdLine, AddCmdLineTailW);
    pCmdLine += countof(AddCmdLineTailW);
    Length2 = pCmdLine - szCmdLine;

    g_pCmdLineW = (PWChar)AllocateMemory(Length * 2 + Length2 * 2 + 2);

    pCmdLine = lpCmdLineW;
    end = *pCmdLine++ == '\"' ? '\"' : ' ';
    while (*pCmdLine && *pCmdLine != end) ++pCmdLine;
    ++pCmdLine;
/*
    if (*++pCmdLine)
    {
        while (*pCmdLine == ' ' || *pCmdLine == '\t') ++pCmdLine;
    }
*/
    end = *pCmdLine;
    *pCmdLine = 0;
    StrCopyW(g_pCmdLineW, lpCmdLineW);
    *pCmdLine = end;

    lpCmdLineW = g_pCmdLineW + (pCmdLine - lpCmdLineW);
    StrCopyW(lpCmdLineW, szCmdLine);
    lpCmdLineW += Length2 - 1;
    StrCopyW(lpCmdLineW, pCmdLine);

    Length = StrLengthW(g_pCmdLineW);
    g_pCmdLineA = (PChar)AllocateMemory(Length * 2);
    UnicodeToAnsi(g_pCmdLineA, Length * 2, g_pCmdLineW, -1);

#endif

    PVOID DllNotificationCookie;

    module = FindLdrModuleByHandle(nullptr);

    if (RtlEqualUnicodeString(&module->BaseDllName, PUSTR(L"360AP.exe"), TRUE))
    {
        auto nop = [](ULONG) -> ULONG
        {
            return 1;
        };

        PATCH_MEMORY_DATA p[] =
        {
            MemoryPatchVa((ULONG64)(API_POINTER(SetThreadExecutionState)(nop)), sizeof(PVOID), LookupImportTable(module->DllBase, "kernel32.dll", KERNEL32_SetThreadExecutionState)),
        };

        PatchMemory(p, countof(p), nullptr);

        return TRUE;
    }

    LdrRegisterDllNotification(0,
        [] (ULONG NotificationReason, PCLDR_DLL_NOTIFICATION_DATA NotificationData, PVOID Context)
        {
            if (NotificationReason != LDR_DLL_NOTIFICATION_REASON_LOADED)
                return;

            if (RtlEqualUnicodeString(NotificationData->Loaded.BaseDllName, PUSTR(L"chrome.dll"), FALSE) == FALSE)
                return;

            PLDR_MODULE chrome = FindLdrModuleByHandle(NotificationData->Loaded.DllBase);

            FuckDisableNewAvatarMenu(chrome);
            FuckExtensionDeveloperModeWarning(chrome);
        },
        nullptr,
        &DllNotificationCookie
    );

    Mp::PATCH_MEMORY_DATA p[] =
    {
        //Mp::FunctionJumpVa(::GetCommandLineW,   MyGetCommandLineW),
        //Mp::FunctionJumpVa(::GetCommandLineA,   MyGetCommandLineA),

        //Mp::FunctionJumpVa(LoadAcceleratorsW,   MyLoadAcceleratorsW,    &StubLoadAcceleratorsW),
        Mp::FunctionJumpVa(PeekMessageW,        ChromePeekMessageW,     &StubPeekMessageW),
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