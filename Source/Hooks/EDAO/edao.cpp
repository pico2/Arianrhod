#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")

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

PWSTR
GetFileName(
    PWSTR   HookedPath,
    ULONG   HookedPathCount,
    PWSTR   OriginalPath,
    ULONG   OriginalCount,
    LPCSTR  InputFileName,
    BOOL    IsInputUnicode = FALSE
)
{
    ULONG_PTR   Length, AppPathLength;
    PWSTR       FileName;

    static WCHAR szDataPath[]   = L"data\\";
    static WCHAR szPatch[]      = L"patch\\\\";
    static WCHAR szPatch2[]     = L"patch2\\";

    if (IsInputUnicode)
    {
        StrCopyW(OriginalPath, (PWSTR)InputFileName);
    }
    else
    {
        AnsiToUnicode(OriginalPath, OriginalCount, (PSTR)InputFileName, -1);
    }

    PLDR_MODULE Module;

    Module = FindLdrModuleByHandle(NULL);
    AppPathLength = (Module->FullDllName.Length - Module->BaseDllName.Length) / sizeof(WCHAR);

    Length = RtlGetFullPathName_U(OriginalPath, HookedPathCount * sizeof(WCHAR), HookedPath, NULL);
    Length = Length / sizeof(WCHAR) + 1;
    FileName = HookedPath + AppPathLength;
    LOOP_ONCE
    {
        if (StrNICompareW(FileName, szDataPath, countof(szDataPath) - 1) ||
            StrNICompareW(Module->FullDllName.Buffer, HookedPath, AppPathLength))
        {
            FileName = OriginalPath;
            break;
        }

        FileName += countof(szDataPath) - 2;
        RtlMoveMemory(
            FileName + countof(szPatch) - countof(szDataPath),
            FileName,
            (Length - (FileName - HookedPath)) * sizeof(*FileName)
        );

        FileName -= countof(szDataPath) - 2;
        CopyStruct(FileName, szPatch, sizeof(szPatch) - sizeof(*szPatch));

        if (IsPathExists(HookedPath))
        {
            FileName = HookedPath;
            break;
        }

        CopyStruct(FileName, szPatch2, sizeof(szPatch2) - sizeof(*szPatch2));
        FileName = IsPathExists(HookedPath) ? HookedPath : OriginalPath;
    }

#if CONSOLE_DEBUG
    PrintConsoleW(L"%s\n", FileName);
#endif

    return FileName;
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
    WCHAR OriginalPath[MAX_NTPATH], HookedPath[MAX_NTPATH];

    return NtFileDisk::SimulateCreateFile(
                GetFileName(HookedPath, countof(HookedPath), OriginalPath, countof(OriginalPath), lpFileName),
                dwDesiredAccess,
                dwShareMode,
                lpSecurityAttributes,
                dwCreationDisposition,
                dwFlagsAndAttributes,
                hTemplateFile
           );
}

HANDLE NTAPI AoFindFirstFileA(PCSTR FileName, PWIN32_FIND_DATAA FindFileData)
{
    NTSTATUS        Status;
    HANDLE          FindHandle;
    WCHAR           OriginalPath[MAX_NTPATH], HookedPath[MAX_NTPATH];
    ML_FIND_DATA    FindData;

    Status = QueryFirstFile(
                    &FindHandle,
                    GetFileName(HookedPath, countof(HookedPath), OriginalPath, countof(OriginalPath), FileName),
                    &FindData
                );

    FindFileData->cFileName[0] = 0;

    if (NT_FAILED(Status))
        return NULL;

    UnicodeToAnsi(FindFileData->cFileName, countof(FindFileData->cFileName), FindData.FileName);

    return FindHandle;
}

BOOL AoIsFileExist(PCSTR FileName)
{
    WCHAR OriginalPath[MAX_NTPATH], HookedPath[MAX_NTPATH];

    if (GetFileName(HookedPath, countof(HookedPath), OriginalPath, countof(OriginalPath), FileName) == HookedPath)
        return TRUE;

    return IsPathExists(OriginalPath);
}

LONG CDECL GetCampImage(PSTR Buffer, PCSTR Format, LONG ChrIndex)
{
    CHAR FullPath[MAX_NTPATH];

    sprintf(FullPath, "data/campimg/chrimg%02d.itp", ChrIndex);
    if (!AoIsFileExist(FullPath))
        ChrIndex = 9999;

    return sprintf(Buffer, "chrimg%02d", ChrIndex);
}

LONG CDECL GetBattleFace(PSTR Buffer, PCSTR Format, PCSTR DataPath, LONG ChrIndex)
{
    LONG_PTR Length;

    Length = sprintf(Buffer, "%sbattle/itp/bface%03d.itp", DataPath, ChrIndex);
    if (!AoIsFileExist(Buffer))
        Length = sprintf(Buffer, "%sbattle/itp/bface%03d.itp", DataPath, 9999);

    return Length;
}

LONG NTAPI ShowExitMessageBox(HWND hWnd, PCSTR Text, PCSTR Caption, UINT Type)
{
    ULONG_PTR   Length;
    PSTR        Buffer;

    Length = StrLengthA(Text) + 1;
    Buffer = (PSTR)AllocStack(Length + 3);

    *(PULONG)&Buffer[0] = TAG3('#5C');
    CopyMemory(Buffer + 3, Text, Length);

    return EDAO::GlobalGetEDAO()->AoMessageBox(Buffer) == TRUE ? IDYES : IDNO;
}

// [0xC29988]+78f84

LONG64 InitWarningItpTimeStamp()
{
    return -1;
}

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

#define METHOD_PTR(_method) PtrAdd((PVOID)NULL, _method)

#include "xxoo.cpp"

BOOL Initialize(PVOID BaseAddress)
{
    ml::MlInitialize();

    LdrDisableThreadCalloutsForDll(BaseAddress);

    SetExeDirectoryAsCurrent();

    static DOUBLE DefaultDistance = 0.f;

    BYTE PushActorDistance[6] = { 0xDD, 0x05 };

    *(DOUBLE **)&PushActorDistance[2] = &DefaultDistance;

    MEMORY_PATCH p[] =
    {
        PATCH_MEMORY(0xEB,      1, 0x2C15B7),    // bypass CGlobal::SetStatusDataForChecking
        PATCH_MEMORY(0x06,      1, 0x410731),    // win
        PATCH_MEMORY(0x06,      1, 0x410AD1),    // win
        PATCH_MEMORY(0x01,      1, 0x40991D),    // cpu
        PATCH_MEMORY(0x91,      1, 0x2F9EE3),    // one hit
        PATCH_MEMORY(VK_SHIFT,  4, 0x4098BA),    // GetKeyState(VK_SHIFT)
        PATCH_MEMORY(0x3FEB,    2, 0x452FD1),    // bypass savedata checksum
        PATCH_MEMORY(0x20000,   4, 0x4E71B2),    // chrimg max buffer size

        // debug AT

        PATCH_MEMORY(0x49EB,    2, 0x5F668D),    // disable orig at
        PATCH_MEMORY(0x81,      1, 0x5F66D9),    // disable orig at
        PATCH_MEMORY(0x80,      1, 0x5F68A4),    // force show debug at
        PATCH_MEMORY(0x2C,      1, 0x5F693D),    // debug at pos.X advance

        // tweak

        PATCH_MEMORY(PushActorDistance, sizeof(PushActorDistance), 0x6538EF),
        PATCH_MEMORY(PushActorDistance, sizeof(PushActorDistance), 0x653BBE),

        PATCH_MEMORY(0x00, 1, 0x55F6E1),        // ±¨¡È

        // monster info
        PATCH_MEMORY(0xEB,      1, 0x626AC8),    // bypass check is enemy

        // iat hook

        PATCH_MEMORY(CreateWindowExCenterA, 4, 0x9D59E8),       // CreateWindowExA
        PATCH_MEMORY(AoGetKeyState,         4, 0x9D5A00),       // GetKeyState
        PATCH_MEMORY(AoCreateFileA,         4, 0x9D576C),       // CreateFileA
    };

    MEMORY_FUNCTION_PATCH f[] =
    {
        // crack

#if !D3D9_VER

        INLINE_HOOK_JUMP_RVA_NULL(0x27969D, METHOD_PTR(&CBattle::SetSelectedAttack)),
        INLINE_HOOK_JUMP_RVA_NULL(0x275DF4, METHOD_PTR(&CBattle::SetSelectedCraft)),
        INLINE_HOOK_JUMP_RVA_NULL(0x272AB9, METHOD_PTR(&CBattle::SetSelectedSCraft)),

        INLINE_HOOK_JUMP_RVA_NULL(0x279986, METHOD_PTR(&CSSaveData::SaveData2SystemData)),
        INLINE_HOOK_JUMP_RVA_NULL(0x279FA8, METHOD_PTR(&CSSaveData::SystemData2SaveData)),

#endif // D3D9_VER

        INLINE_HOOK_JUMP_RVA_NULL(0x279553, METHOD_PTR(&CBattle::SetSelectedMagic)),

        // tweak

        //INLINE_HOOK_CALL_RVA_NULL(0x40492A, ShowExitMessageBox),
        INLINE_HOOK_CALL_RVA_NULL(0x3640A1, InitWarningItpTimeStamp),   // bypass show warning.itp
        INLINE_HOOK_JUMP_RVA     (0x279AA3, METHOD_PTR(&EDAO::CheckItemEquipped), EDAO::StubCheckItemEquipped),
        INLINE_HOOK_CALL_RVA_NULL(0x5F690B, CBattle::FormatBattleChrAT),
        INLINE_HOOK_CALL_RVA_NULL(0x5B05C6, CBattle::ShowSkipCraftAnimeButton),

        // bug fix

        INLINE_HOOK_CALL_RVA_NULL(0x5B1BE6, METHOD_PTR(&CBattleATBar::LookupReplaceAtBarEntry)),

        // file redirection

        INLINE_HOOK_CALL_RVA_NULL(0x48C1EA, AoFindFirstFileA),
        INLINE_HOOK_CALL_RVA_NULL(0x48C206, NtClose),
        INLINE_HOOK_CALL_RVA_NULL(0x4E6A0B, GetCampImage),
        INLINE_HOOK_CALL_RVA_NULL(0x4E6AE4, GetCampImage),
        INLINE_HOOK_CALL_RVA_NULL(0x5A05B4, GetBattleFace),

        // custom format itp / itc

        INLINE_HOOK_JUMP_RVA(0x273D24, METHOD_PTR(&EDAOFileStream::Uncompress), EDAOFileStream::StubUncompress),

        // hack for boss

        INLINE_HOOK_CALL_RVA_NULL(0x56F7C7, METHOD_PTR(&CBattle::NakedGetChrIdForSCraft)),
        INLINE_HOOK_CALL_RVA_NULL(0x5E027B, METHOD_PTR(&CBattle::NakedGetTurnVoiceChrId)),
        INLINE_HOOK_CALL_RVA_NULL(0x5E1015, METHOD_PTR(&CBattle::NakedGetRunawayVoiceChrId)),
        INLINE_HOOK_CALL_RVA_NULL(0x5E0CA3, METHOD_PTR(&CBattle::NakedGetReplySupportVoiceChrId)),
        INLINE_HOOK_CALL_RVA_NULL(0x5E09E0, METHOD_PTR(&CBattle::NakedGetTeamRushVoiceChrId)),
        INLINE_HOOK_CALL_RVA_NULL(0x5E062B, METHOD_PTR(&CBattle::NakedGetSBreakVoiceChrId)),
        INLINE_HOOK_CALL_RVA_NULL(0x5A3644, METHOD_PTR(&CBattle::NakedCopyMagicAndCraftData)),
        INLINE_HOOK_CALL_RVA_NULL(0x5A3814, METHOD_PTR(&CBattle::NakedOverWriteBattleStatusWithChrStatus)),
        INLINE_HOOK_CALL_RVA_NULL(0x578368, METHOD_PTR(&CBattle::NakedIsChrStatusNeedRefresh)),
        INLINE_HOOK_CALL_RVA_NULL(0x622C83, METHOD_PTR(&EDAO::NakedGetChrSBreak)),
        INLINE_HOOK_JUMP_RVA     (0x277776, METHOD_PTR(&CGlobal::GetMagicData), CGlobal::StubGetMagicData),
        INLINE_HOOK_JUMP_RVA     (0x274E18, METHOD_PTR(&CGlobal::GetMagicQueryTable), CGlobal::StubGetMagicQueryTable),
        INLINE_HOOK_JUMP_RVA     (0x2767E0, METHOD_PTR(&CGlobal::GetMagicDescription), CGlobal::StubGetMagicDescription),


        // inherit custom flags

        INLINE_HOOK_CALL_RVA_NULL(0x358457, METHOD_PTR(&CScript::NakedInheritSaveData)),


        // enemy sbreak

        INLINE_HOOK_CALL_RVA_NULL(0x56526F, METHOD_PTR(&CBattle::NakedGetBattleState)),
        INLINE_HOOK_JUMP_RVA     (0x599100, METHOD_PTR(&CBattle::SetCurrentActionChrInfo), CBattle::StubSetCurrentActionChrInfo),
        INLINE_HOOK_CALL_RVA_NULL(0x591C3A, METHOD_PTR(&CBattle::NakedEnemyThinkAction)),


        // monster info box

        INLINE_HOOK_CALL_RVA_NULL(0x626AEA, METHOD_PTR(&CBattleInfoBox::SetMonsterInfoBoxSize)),
        INLINE_HOOK_JUMP_RVA     (0x27AC8C, METHOD_PTR(&CBattleInfoBox::DrawMonsterStatus), CBattleInfoBox::StubDrawMonsterStatus),


        // acgn

        INLINE_HOOK_JUMP_RVA     (0x275EFD, METHOD_PTR(&CBattle::LoadMSFile), CBattle::StubLoadMSFile),	//it3
        INLINE_HOOK_JUMP_RVA_NULL(0x5D3545, METHOD_PTR(&CBattle::NakedAS_8D_5F)), // ±ø’¥Û±¿ªµ


        //INLINE_HOOK_JUMP_RVA(0x275755, METHOD_PTR(&EDAO::Fade), EDAO::StubFade),
        //INLINE_HOOK_CALL_RVA_NULL(0x601122, FadeInRate),
    };

    Nt_PatchMemory(p, countof(p), f, countof(f), GetExeModuleHandle());

    return TRUE;
}

BOOL WINAPI DllMain(PVOID BaseAddress, ULONG Reason, PVOID Reserved)
{
    //PrintConsoleW(L"%d", FIELD_OFFSET(MONSTER_STATUS, Equipment));

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

#if !D3D9_VER

#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/EXPORT:Direct3DCreate9=d3d9.Direct3DCreate9")

#else // D3D9_VER

#include <d3d9.h>
#pragma comment(linker, "/EXPORT:Direct3DCreate9=_Arianrhod_Direct3DCreate9@4")

EXTC IDirect3D9* STDCALL Arianrhod_Direct3DCreate9(UINT SDKVersion)
{
    static TYPE_OF(Arianrhod_Direct3DCreate9) *Direct3DCreate9;

    if (Direct3DCreate9 == NULL)
    {
        ULONG           Length;
        NTSTATUS        Status;
        PVOID           d3d9;
        WCHAR           D3D9Path[MAX_NTPATH];

        Length = Nt_GetSystemDirectory(D3D9Path, countof(D3D9Path));
        CopyStruct(D3D9Path + Length, L"d3d9.dll", sizeof(L"d3d9.dll"));

        d3d9 = Ldr::LoadDll(D3D9Path);
        if (d3d9 == NULL)
            return NULL;

        LdrAddRefDll(GET_MODULE_HANDLE_EX_FLAG_PIN, d3d9);

        *(PVOID *)&Direct3DCreate9 = GetRoutineAddress(d3d9, "Direct3DCreate9");
        if (Direct3DCreate9 == NULL)
            return NULL;

    }

    if ((ULONG_PTR)_ReturnAddress() == 0x8055F5)
    {
        DllMain(&__ImageBase, DLL_PROCESS_ATTACH, 0);
    }

    return Direct3DCreate9(SDKVersion);
}

#endif
