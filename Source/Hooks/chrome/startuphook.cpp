#pragma comment(linker,"/ENTRY:DllMain")
#pragma comment(linker,"/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker,"/SECTION:.Amano,ERW /MERGE:.text=.Amano")
#pragma comment(linker, "/EXPORT:WTSFreeMemory=_PWTSFreeMemory@4")
#pragma comment(linker, "/EXPORT:WTSQuerySessionInformationW=_PWTSQuerySessionInformationW@0")
#pragma comment(linker, "/EXPORT:WTSUnRegisterSessionNotification=_PWTSUnRegisterSessionNotification@4")
#pragma comment(linker, "/EXPORT:WTSRegisterSessionNotification=_PWTSRegisterSessionNotification@8")
#pragma comment(linker, "/EXPORT:WTSQueryUserToken=_PWTSQueryUserToken@8")

#include "MyLibrary.cpp"
#include <windowsx.h>
#include <WtsApi32.h>

#define KEY_FLAG_PRESSED    1

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
};

VOID SendKey(ULONG Modifier, ULONG VirtualKey, BOOL KeyDown)
{
    ULONG Flags, Count;
    INPUT inputs[4];

    Flags = KeyDown ? 0 : KEYEVENTF_KEYUP;

    Count = 0;
    ZeroMemory(inputs, sizeof(inputs));

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

    if (VirtualKey != 0)
    {
        inputs[Count].ki.wVk = VirtualKey;
        inputs[Count].ki.dwFlags = Flags;
        inputs[Count].type = INPUT_KEYBOARD;
        ++Count;
    }

    if (Count != 0)
        SendInput(Count, inputs, sizeof(inputs[0]));
}

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

BOOL TranslateKeyEvent(PMSG Msg, PBYTE KeyStateTable, BOOL KeyDown)
{
    if (KeyDown == FALSE)
        return FALSE;

    if (FindThreadFrame(TAG4('TRKE')) != nullptr)
        return FALSE;

    PKEY_MAP KeyMap;
    TEB_ACTIVE_FRAME filter(TAG4('TRKE'));

    filter.Push();

    FOR_EACH_ARRAY(KeyMap, KeyMapTable)
    {
        if (FLAG_ON(KeyMap->Original.Modifier, FCONTROL) != FLAG_ON(KeyStateTable[VK_CONTROL], KEY_FLAG_PRESSED))
            continue;

        if (FLAG_ON(KeyMap->Original.Modifier, FALT) != FLAG_ON(KeyStateTable[VK_MENU], KEY_FLAG_PRESSED))
            continue;

        if (FLAG_ON(KeyMap->Original.Modifier, FSHIFT) != FLAG_ON(KeyStateTable[VK_SHIFT], KEY_FLAG_PRESSED))
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

        // FOR_EACH_ARRAY(Key, KeyToRelease)
        // {
        //     if (*Key == 0)
        //         continue;

        //     SendKey(0, *Key, FALSE);
        // }

        SendKeyList(0, KeyToRelease, countof(KeyToRelease), FALSE);
        SendKey(KeyMap->Replacement.Modifier, KeyMap->Replacement.VirtualKey, TRUE);
        SendKey(KeyMap->Replacement.Modifier, KeyMap->Replacement.VirtualKey, FALSE);
        SendKeyList(0, KeyToRelease, countof(KeyToRelease), TRUE);

        // FOR_EACH_ARRAY(Key, KeyToRelease)
        // {
        //     if (*Key == 0)
        //         continue;

        //     SendKey(0, *Key, TRUE);
        // }

        return TRUE;
    }

    return FALSE;
}

BOOL NTAPI ChromePeekMessageW(LPMSG lpMsg, HWND hWnd, UINT wMsgFilterMin, UINT wMsgFilterMax, UINT wRemoveMsg)
{
    BOOL        Success, forward;
    LONG        X, Y, WheelDistance, fwKeys;
    INPUT       inputs[2];
    POINT       point;

    static LONG LastDelta;

    static BYTE KeyStateTable[256];

    Success = StubPeekMessageW(lpMsg, hWnd, wMsgFilterMin, wMsgFilterMax, wRemoveMsg);
    if (Success == FALSE)
        return Success;

    switch (lpMsg->message)
    {
        case WM_MOUSEWHEEL:
            //static int n = 0;

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

            //if (Y > GetSystemMetrics(SM_CYCAPTION))
            if (Y > (IsMaximized(lpMsg->hwnd) ? 30 : 50))
                break;

            forward = WheelDistance > 0;
            SendKey(FCONTROL, forward ? VK_PRIOR : VK_NEXT, TRUE);
            SendKey(FCONTROL, forward ? VK_PRIOR : VK_NEXT, FALSE);

            // inputs[0].type = INPUT_KEYBOARD;
            // inputs[0].ki.wVk = VK_CONTROL;
            // inputs[0].ki.wScan = 0;
            // inputs[0].ki.time = 0;
            // inputs[0].ki.dwFlags = 0;
            // inputs[0].ki.dwExtraInfo = 0;
            // inputs[1].type = INPUT_KEYBOARD;
            // inputs[1].ki.wVk = forward ? VK_PRIOR : VK_NEXT;
            // inputs[1].ki.wScan = 0;
            // inputs[1].ki.time = 0;
            // inputs[1].ki.dwFlags = KEYEVENTF_EXTENDEDKEY;
            // inputs[1].ki.dwExtraInfo = 0;
            // SendInput(2, inputs, sizeof(*inputs));

            // inputs[0].ki.dwFlags |= KEYEVENTF_KEYUP;
            // inputs[1].ki.dwFlags |= KEYEVENTF_KEYUP;
            // Swap(inputs[0], inputs[1]);
            // SendInput(2, inputs, sizeof(*inputs));

            break;

        case WM_SYSKEYDOWN:
        case WM_KEYDOWN:
            SET_FLAG(KeyStateTable[(BYTE)lpMsg->wParam], KEY_FLAG_PRESSED);
            Success = !TranslateKeyEvent(lpMsg, KeyStateTable, TRUE);
            break;

        case WM_SYSKEYUP:
        case WM_KEYUP:
            CLEAR_FLAG(KeyStateTable[(BYTE)lpMsg->wParam], KEY_FLAG_PRESSED);
            Success = !TranslateKeyEvent(lpMsg, KeyStateTable, FALSE);
            break;
    }

    return Success;
}

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    PVOID   hModule;
    SizeT   Length, Length2;
    LPWSTR  lpCmdLineW, pCmdLine;
    WChar   end, szCmdLine[MAX_PATH + 40];

    static WChar AddCmdLineHeadW[] = L" --user-data-dir=\"";
    static WChar AddCmdLineTailW[] = L"UserData\" --purge-memory-button";

    LdrDisableThreadCalloutsForDll(BaseAddress);

    Length = Nt_GetSystemDirectory(szCmdLine, countof(szCmdLine));
    CopyStruct(szCmdLine + Length, L"wtsapi32.dll", sizeof(L"wtsapi32.dll"));
    hModule = Ldr::LoadDll(szCmdLine);

    *(PVOID *)&StubWTSFreeMemory                    = GetRoutineAddress(hModule, "WTSFreeMemory");
    *(PVOID *)&StubWTSQuerySessionInformationW      = GetRoutineAddress(hModule, "WTSQuerySessionInformationW");
    *(PVOID *)&StubWTSUnRegisterSessionNotification = GetRoutineAddress(hModule, "WTSUnRegisterSessionNotification");
    *(PVOID *)&StubWTSRegisterSessionNotification   = GetRoutineAddress(hModule, "WTSRegisterSessionNotification");
    *(PVOID *)&StubWTSQueryUserToken                = GetRoutineAddress(hModule, "WTSQueryUserToken");

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

    hModule = Nt_GetModuleHandle(L"chrome.dll");

    Mp::PATCH_MEMORY_DATA p[] =
    {
        Mp::FunctionJumpVa(::GetCommandLineW,   MyGetCommandLineW),
        Mp::FunctionJumpVa(::GetCommandLineA,   MyGetCommandLineA),

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