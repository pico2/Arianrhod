#include "Hooks.h"

using namespace Mp;

API_POINTER(free)           msvcrX0_free;
API_POINTER(SetWindowPos)   StubSetWindowPos;
API_POINTER(ShowWindow)     StubShowWindow;
API_POINTER(PostMessageW)   StubPostMessageW;

BOOL IsWindowMessageBox(HWND hWnd)
{
    WCHAR Title[0x200];

    GetWindowTextW(hWnd, Title, countof(Title));

    return wcsstr(Title, L" - ЯћЯЂКазг") != nullptr;
}

BOOL
NTAPI
QqSetWindowPos(
    HWND    hWnd,
    HWND    hWndInsertAfter,
    int     X,
    int     Y,
    int     cx,
    int     cy,
    UINT    Flags
)
{
#define GROUP_WIDTH     722
#define GROUP_HEIGHT    671
#define BUDDY_WIDTH     506
#define BUDDY_HEIGHT    507

#if 0

    AllocConsole();
    ShowWindow(GetConsoleWindow(), SW_SHOW);
    PrintConsoleW(L"%d, %d\n", cx, cy);

    if (0)
    {
        FILE *fp;

        fp = fopen("D:\\desktop\\qqlog.txt", "ab");
        fprintf(fp, "%d, %d\r\n", cx, cy);
        fclose(fp);
    }

#endif

    enum
    {
        UnknownWindow,
        BuddyWindow,
        GroupWindow,
        DiscussWindow,
        MessageBox,
        Qq64,
    };

    auto GetWindowType = [] (HWND hWnd, INT cx, INT cy)
    {
        BOOL IsMessageBox;
        PSIZE Size;

        static SIZE BuddySize[] =
        {
            { 553, 526 },
        };

        static SIZE GroupSize[] =
        {
            { 614, 546 },
            { 603, 527 },
            { 623, 546 },
            { 599, 524 },
            { 598, 522 },
        };

        static SIZE DiscussSize[] =
        {
            { 567, 545 },
            { 556, 526 },
            { 571, 545 },
        };

        IsMessageBox = IsWindowMessageBox(hWnd);
        if (IsMessageBox)
            return MessageBox;

        FOR_EACH_ARRAY(Size, BuddySize)
        {
            if (Size->cx == cx && Size->cy == cy)
                return BuddyWindow;
        }

        FOR_EACH_ARRAY(Size, GroupSize)
        {
            if (Size->cx == cx && Size->cy == cy)
                return GroupWindow;
        }

        FOR_EACH_ARRAY(Size, DiscussSize)
        {
            if (Size->cx == cx && Size->cy == cy)
                return DiscussWindow;
        }

        return UnknownWindow;
    };

    ULONG WindowType = GetWindowType(hWnd, cx, cy);

    static HWND LastChatFrame;

    if (WindowType == UnknownWindow)
    {
        if (Flags == 0x15 &&
            cx == -1 &&
            cy == -1 &&
            X != -1 &&
            Y != -1 &&
            hWndInsertAfter == HWND_TOP
           )
        {
            LastChatFrame = hWnd;
        }
        else if (Flags == 0x214 &&
                 hWndInsertAfter == HWND_TOP &&
                 X != -1 &&
                 Y != -1 &&
                 cx != -1 &&
                 cy != -1
                )
        {
            if (LastChatFrame != nullptr && LastChatFrame == hWnd)
            {
                WindowType = Qq64;
            }
        }
        else if (Flags == 0x214 &&
                 hWndInsertAfter == HWND_TOP &&
                 X == -1 &&
                 Y == -1 &&
                 cx != -1 &&
                 cy != -1
                )
        {
            LastChatFrame = hWnd;
        }

        if (hWnd != LastChatFrame)
            LastChatFrame = nullptr;
    }

    if (WindowType != UnknownWindow)
    {
        RECT WorkArea;

        SystemParametersInfoW(SPI_GETWORKAREA, 0, &WorkArea, 0);

        int width, height;

        switch (WindowType)
        {
            case MessageBox:
                cx = (WorkArea.right - WorkArea.left) * 80 / 100;
                cy = (WorkArea.bottom - WorkArea.top) * 90 / 100;
                break;

            case BuddyWindow:
                //cx = BUDDY_WIDTH;
                //cy = BUDDY_HEIGHT;
                break;

            case GroupWindow:
            case DiscussWindow:
                cx = GROUP_WIDTH;
                cy = GROUP_HEIGHT;
                break;
        }

        width = cx;
        height = cy;

        X = ((WorkArea.right - WorkArea.left) - width) / 2;
        Y = ((WorkArea.bottom - WorkArea.top) - height) / 2;

        //X = Y = 0;

        //CLEAR_FLAG(Flags, SWP_NOSIZE | SWP_NOMOVE);
    }

    return StubSetWindowPos(hWnd, hWndInsertAfter, X, Y, cx, cy, Flags);
}

BOOL NTAPI QqShowWindow(HWND hWnd, int CmdShow)
{
    if (IsWindowMessageBox(hWnd))
        QqSetWindowPos(hWnd, nullptr, 0, 0, 0, 0, 0);

    return StubShowWindow(hWnd, CmdShow);
}

BOOL NTAPI QqPostMessageW(HWND hWnd, UINT Message, WPARAM wParam, LPARAM lParam)
{
    switch (Message)
    {
        case 0x7E9:
        case 0x7EA:
        case 0x7EB:
        case 0x7EC:
            if (wParam > 0x10000 && msvcrX0_free != nullptr)
                msvcrX0_free((PVOID)wParam);

            return TRUE;
    }

    return StubPostMessageW(hWnd, Message, wParam, lParam);
}

NTSTATUS HookUser32(PVOID BaseAddress)
{
    PLDR_MODULE crt;
    PUNICODE_STRING crtname;

    static UNICODE_STRING msvcrt[] =
    {
        RTL_CONSTANT_STRING(L"msvcr80.dll"),
        RTL_CONSTANT_STRING(L"msvcr90.dll"),
        RTL_CONSTANT_STRING(L"msvcr100.dll"),
        RTL_CONSTANT_STRING(L"msvcr110.dll"),
    };

    FOR_EACH_ARRAY(crtname, msvcrt)
    {
        crt = FindLdrModuleByName(crtname);
        if (crt == nullptr)
            continue;

        *(PVOID *)&msvcrX0_free = GetRoutineAddress(crt->DllBase, "free");
        break;
    }

    PATCH_MEMORY_DATA Function_user32[] =
    {
        FunctionJumpVa(LookupExportTable(BaseAddress, USER32_SetWindowPos), QqSetWindowPos, &StubSetWindowPos),
        //FunctionJumpVa(LookupExportTable(BaseAddress, USER32_PostMessageW), QqPostMessageW, &StubPostMessageW)
    };

    return PatchMemory(Function_user32, countof(Function_user32), BaseAddress);
}