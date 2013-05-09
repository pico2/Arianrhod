#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")
#pragma comment(linker, "/EXPORT:Direct3DCreate9=d3d9.Direct3DCreate9")

#include "edao.h"
#include "MyLibrary.cpp"
#include "edao_vm.h"

VOID THISCALL EDAO::Fade(ULONG Param1, ULONG Param2, ULONG Param3, ULONG Param4, ULONG Param5, ULONG Param6)
{
    if (GetAsyncKeyState(VK_LSHIFT) >= 0)
        (this->*StubFade)(Param1, Param2, Param3, Param4, Param5, Param6);
}

float Rate = 200.f;
float fuck = 0.17f;

NAKED VOID FadeInRate()
{
    INLINE_ASM
    {
        //fld     dword ptr [eax+0x40];
        fld     fuck;
        fmul    Rate;
        ret;
    }
}

BOOL    Turbo;
WNDPROC WindowProc;

SHORT NTAPI AoGetKeyState(int VirtualKey)
{
    switch (VirtualKey)
    {
        case VK_SHIFT:
        case VK_LSHIFT:
            if (Turbo)
                return (SHORT)0xFFFF8001;

            break;
    }

    return GetKeyState(VirtualKey);
}

LRESULT NTAPI MainWndProc(HWND Window, UINT Message, WPARAM wParam, LPARAM lParam)
{
    switch (Message)
    {
        case WM_KEYUP:
            switch (wParam & 0xFFFF)
            {
                case 'T':
                    Turbo ^= TRUE;
                    break;
            }
    }

    return WindowProc(Window, Message, wParam, lParam);
}

HWND WINAPI CreateWindowExCenterA(DWORD dwExStyle, LPCSTR lpClassName, LPCSTR lpWindowName, DWORD dwStyle, int X, int Y, int nWidth, int nHeight, HWND hWndParent, HMENU hMenu, HINSTANCE hInstance, LPVOID lpParam)
{
    HWND    Window;
    RECT    rcWordArea;
    ULONG   Length;
    PWSTR   pszClassName, pszWindowName;

    Length = StrLengthA(lpClassName) + 1;
    pszClassName = (PWSTR)AllocStack(Length * sizeof(WCHAR));
    AnsiToUnicode(pszClassName, Length, lpClassName, Length);

    Length = StrLengthA(lpWindowName) + 1;
    pszWindowName = (PWSTR)AllocStack(Length * sizeof(WCHAR));
    AnsiToUnicode(pszWindowName, Length, lpWindowName, Length);

    if (SystemParametersInfoW(SPI_GETWORKAREA, 0, &rcWordArea, 0))
    {
        X = ((rcWordArea.right - rcWordArea.left) - nWidth) / 2;
        Y = ((rcWordArea.bottom - rcWordArea.top) - nHeight) / 2;
    }

    Window = CreateWindowExW(dwExStyle, pszClassName, pszWindowName, dwStyle, X, Y, nWidth, nHeight, hWndParent, hMenu, hInstance, lpParam);

    if (Window != NULL)
        WindowProc = (WNDPROC)SetWindowLongPtrA(Window, GWL_WNDPROC, (LONG_PTR)MainWndProc);

    return Window;
}



PWCHAR
GetFileName(
    PWCHAR  pszHooked,
    ULONG   HookedBufferCount,
    PWCHAR  pszOriginal,
    ULONG   OriginalCount,
    LPCSTR  lpFileName,
    BOOL    IsInputUnicode = FALSE
)
{
    ULONG   Length, AppPathLength;
    PWCHAR  pszFileName;

    static WCHAR szDataPath[]   = L"data\\";
    static WCHAR szPatch[]      = L"patch\\";

    if (IsInputUnicode)
    {
        StrCopyW(pszOriginal, (LPWSTR)lpFileName);
    }
    else
    {
        AnsiToUnicode(pszOriginal, OriginalCount, (PCHAR)lpFileName, -1);
    }

    PLDR_MODULE Module;

    Module = FindLdrModuleByHandle(NULL);
    AppPathLength = (Module->FullDllName.Length - Module->BaseDllName.Length) / sizeof(WCHAR);

    Length = RtlGetFullPathName_U(pszOriginal, HookedBufferCount * sizeof(WCHAR), pszHooked, NULL);
    Length = Length / sizeof(WCHAR) + 1;
    pszFileName = pszHooked + AppPathLength;
    LOOP_ONCE
    {
        if (StrNICompareW(pszFileName, szDataPath, countof(szDataPath) - 1) ||
            StrNICompareW(Module->FullDllName.Buffer, pszHooked, AppPathLength))
        {
            pszFileName = pszOriginal;
            break;
        }

        pszFileName += countof(szDataPath) - 2;
        RtlMoveMemory(
            pszFileName + countof(szPatch) - countof(szDataPath),
            pszFileName,
            (Length - (pszFileName - pszHooked)) * sizeof(*pszFileName)
        );

        pszFileName -= countof(szDataPath) - 2;
        CopyStruct(pszFileName, szPatch, sizeof(szPatch) - sizeof(*szPatch));

        pszFileName = IsPathExists(pszHooked) ? pszHooked : pszOriginal;
    }

#if CONSOLE_DEBUG
    PrintConsoleW(L"%s\n", pszFileName);
#endif

    return pszFileName;
}

HANDLE
WINAPI
AoCreateFileA(
    LPCSTR                  lpFileName,
    DWORD                   dwDesiredAccess,
    DWORD                   dwShareMode,
    LPSECURITY_ATTRIBUTES   lpSecurityAttributes,
    DWORD                   dwCreationDisposition,
    DWORD                   dwFlagsAndAttributes,
    HANDLE                  hTemplateFile
)
{
    WCHAR szFile[MAX_NTPATH], szFullPath[MAX_NTPATH];

    return NtFileDisk::SimulateCreateFile(
                GetFileName(szFullPath, countof(szFullPath), szFile, countof(szFile), lpFileName),
                dwDesiredAccess,
                dwShareMode,
                lpSecurityAttributes,
                dwCreationDisposition,
                dwFlagsAndAttributes,
                hTemplateFile
           );
}

// [0xC29988]+78f84

LONG64 InitWarningItpTimeStamp()
{
    return -1;
}

BOOL EDAO::CheckItemEquipped(ULONG ItemId, PULONG EquippedIndex)
{
    switch (ItemId)
    {
        case 0xB7:  // ú—Ä¿
        case 0xB8:  // ÌìÑÛ
        case 0xBB:  // Ì½Öª
            if (EquippedIndex != NULL)
                *EquippedIndex = 0;

            return TRUE;
    }

    return (this->*StubCheckItemEquipped)(ItemId, EquippedIndex);
}

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

#define METHOD_PTR(_method) PtrAdd((PVOID)NULL, _method)

BOOL Initialize(PVOID BaseAddress)
{
    SetExeDirectoryAsCurrent();

    MEMORY_PATCH p[] =
    {
        PATCH_MEMORY(0xEB,      1, 0x2C15B7),    // bypass CGlobal::SetStatusDataForChecking
        PATCH_MEMORY(0x06,      1, 0x410731),    // win
        PATCH_MEMORY(0x06,      1, 0x410AD1),    // win
        PATCH_MEMORY(0x01,      1, 0x40991D),    // cpu
        PATCH_MEMORY(0x91,      1, 0x2F9EE3),    // one hit
        PATCH_MEMORY(VK_SHIFT,  4, 0x4098BA),    // GetKeyState(VK_SHIFT)

        PATCH_MEMORY(CreateWindowExCenterA, 4, 0x9D59E8),       // CreateWindowExA
        PATCH_MEMORY(AoGetKeyState,         4, 0x9D5A00),       // GetKeyState
        PATCH_MEMORY(AoCreateFileA,         4, 0x9D576C),       // CreateFileA
    };

    MEMORY_FUNCTION_PATCH f[] =
    {
        // crack

        INLINE_HOOK_JUMP_RVA_NULL(0x27969D, METHOD_PTR(&CBattle::USE_ATTACK_FOR_CHECKING)),
        INLINE_HOOK_JUMP_RVA_NULL(0x279553, METHOD_PTR(&CBattle::USE_MAGIC_FOR_CHECKING)),
        INLINE_HOOK_JUMP_RVA_NULL(0x275DF4, METHOD_PTR(&CBattle::USE_CRAFT_FOR_CHECKING)),
        INLINE_HOOK_JUMP_RVA_NULL(0x272AB9, METHOD_PTR(&CBattle::USE_SCRAFT_FOR_CHECKING)),

        INLINE_HOOK_JUMP_RVA_NULL(0x279986, METHOD_PTR(&CSSaveData::SaveData2SystemData)),
        INLINE_HOOK_JUMP_RVA_NULL(0x279FA8, METHOD_PTR(&CSSaveData::SystemData2SaveData)),

        // tweak

        INLINE_HOOK_CALL_RVA_NULL(0x3640A1, InitWarningItpTimeStamp),   // bypass show warning.itp
        INLINE_HOOK_JUMP_RVA(0x279AA3, METHOD_PTR(&EDAO::CheckItemEquipped), EDAO::StubCheckItemEquipped),

        // custom format itp / itc

        INLINE_HOOK_JUMP_RVA(0x273D24, METHOD_PTR(&EDAOFileStream::Uncompress), EDAOFileStream::StubUncompress),

        //INLINE_HOOK_JUMP_RVA(0x275755, METHOD_PTR(&EDAO::Fade), EDAO::StubFade),
        //INLINE_HOOK_CALL_RVA_NULL(0x601122, FadeInRate),
    };

    Nt_PatchMemory(p, countof(p), f, countof(f), GetExeModuleHandle());

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
