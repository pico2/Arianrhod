#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")

#include "edao.h"
#include "SoundArc.h"
#include "MyLibrary.cpp"
#include "edao_vm.h"

#define ENABLE_LOG  0

#if !D3D9_VER
    #undef ENABLE_LOG
    #define ENABLE_LOG 0
#endif

void WriteLog(PCWSTR Format, ...)
{
#if ENABLE_LOG

    NtFileDisk log;
    WCHAR Buffer[0xFF0];

    log.CreateIfNotExist(L"log.txt");
    if (log.GetSize32() == 0)
    {
        ULONG BOM = BOM_UTF16_LE;
        log.Write(&BOM, 2);
    }

    log.Seek(0, FILE_END);

    log.Write(Buffer, vswprintf(Buffer, Format, (va_list)(&Format + 1)) * 2);
    log.Write(L"\r\n", 4);

#endif
}

#if !ENABLE_LOG
    #define WriteLog(...)
#endif
/*
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
*/

BOOL    Turbo;
ULONG   TurboCount;
WNDPROC WindowProc;

SHORT NTAPI AoGetKeyState(int VirtualKey)
{
    switch (VirtualKey)
    {
        case VK_SHIFT:
        case VK_LSHIFT:
            if (!Turbo)
                break;

            ++*EDAO::GlobalGetEDAO()->GetMap()->GetFrameNumber();

            return (SHORT)0xFFFF8001;
    }

    return GetKeyState(VirtualKey);
}

LRESULT NTAPI MainWndProc(HWND Window, UINT Message, WPARAM wParam, LPARAM lParam)
{
    FLOAT Delta;
    ULONG Index;

    enum { X = 0, Y = 1, Z = 2, Z2 = 42 };

    switch (Message)
    {
        case WM_KEYUP:
            switch (LOWORD(wParam))
            {
                case 'T':
                    Turbo ^= TRUE;
                    break;

                //case 'J':
                //    EDAO::GlobalGetEDAO()->JumpToMap();
                //    break;
            }
            break;

        case WM_KEYDOWN:
            switch (wParam & 0xFFFF)
            {
                case VK_NUMPAD4: Index = X; Delta = -1.f; goto CHANGE_CHR_COORD;
                case VK_NUMPAD6: Index = X; Delta = 1.f;  goto CHANGE_CHR_COORD;

                case VK_NUMPAD2: Index = Y; Delta = -1.f; goto CHANGE_CHR_COORD;
                case VK_NUMPAD8: Index = Y; Delta = 1.f;  goto CHANGE_CHR_COORD;

                case VK_NUMPAD7: Index = Z; Delta = 1.f;  goto CHANGE_CHR_COORD;
                case VK_NUMPAD9: Index = Z; Delta = -1.f;  goto CHANGE_CHR_COORD;

CHANGE_CHR_COORD:

                    //if (GetKeyState(VK_CONTROL) >= 0) break;

                    PFLOAT Coord = (PFLOAT)(*(PULONG_PTR)PtrAdd(EDAO::GlobalGetEDAO(), 0x78CB8 + 0x2BC) + 0x80);
                    Coord[Index] += Delta;
/*
                    switch (wParam & 0xFFFF)
                    {
                        case VK_NUMPAD7:
                        case VK_NUMPAD9:
                            Coord[Z2] += Delta;
                    }
*/
                    break;
            }
    }

    return WindowProc(Window, Message, wParam, lParam);
}

HWND WINAPI CreateWindowExCenterA(ULONG dwExStyle, LPCSTR lpClassName, LPCSTR lpWindowName, ULONG dwStyle, int X, int Y, int nWidth, int nHeight, HWND hWndParent, HMENU hMenu, HINSTANCE hInstance, LPVOID lpParam)
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

        WriteLog(L"pass1: %s", HookedPath);

        if (IsPathExists(HookedPath))
        {
            FileName = HookedPath;
            break;
        }

        CopyStruct(FileName, szPatch2, sizeof(szPatch2) - sizeof(*szPatch2));
        FileName = IsPathExists(HookedPath) ? HookedPath : OriginalPath;

        WriteLog(L"pass2: %s", HookedPath);
    }

    WriteLog(L"%d, %s -> %s", FileName == HookedPath, OriginalPath, HookedPath);

    return FileName;
}

HANDLE
WINAPI
AoCreateFileA(
    LPCSTR                  lpFileName,
    ULONG                   dwDesiredAccess,
    ULONG                   dwShareMode,
    LPSECURITY_ATTRIBUTES   lpSecurityAttributes,
    ULONG                   dwCreationDisposition,
    ULONG                   dwFlagsAndAttributes,
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

LONG CDECL GetCampImage(PSTR Buffer, PCSTR Format, LONG ChrId)
{
    CHAR FullPath[MAX_NTPATH];

    sprintf(FullPath, "data/campimg/chrimg%02d.itp", ChrId);
    if (!AoIsFileExist(FullPath))
        ChrId = 9999;

    return sprintf(Buffer, Format, ChrId);
}

LONG CDECL GetBattleFace(PSTR Buffer, PCSTR Format, PCSTR DataPath, LONG ChrId)
{
    LONG_PTR Length;

    Length = sprintf(Buffer, Format, DataPath, ChrId);
    if (!AoIsFileExist(Buffer))
        Length = sprintf(Buffer, Format, DataPath, 9999);

    return Length;
}

LONG CDECL GetFieldAttackChr(PSTR Buffer, PCSTR Format, LONG ChrId)
{
    CHAR FullPath[MAX_NTPATH];

    sprintf(FullPath, "data/system/fachr%03d._bn", ChrId);
    if (!AoIsFileExist(FullPath))
        ChrId = 999;

    return sprintf(Buffer, Format, ChrId);
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

VOID NTAPI PrintOP(LONG sub, LONG offset, PBYTE base)
{
    //if (sub == 0) offset -= 4;

    if (offset == 0x1572)
        MessageBoxW(0,0,0,0);

    //AllocConsole();PrintConsoleA("%02X, %08X, %02X\n", sub, offset, base[offset]);
    WriteLog(L"%02X, %08X, %02X", sub, offset, base[offset]);
}

NAKED VOID xxx()
{
    INLINE_ASM
    {
        push    eax;
        push    edx;
        push    dword ptr [ecx + 2];
        and     dword ptr [esp], 0xFF;
        mov     al, byte ptr [eax+edx];
        mov     byte ptr [ebp-0x29], al;
        call    PrintOP;
        ret;
    }
}

// 90F793

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

        PATCH_MEMORY(0x00,      1, 0x653972),       // box height
        PATCH_MEMORY(0x00,      1, 0x653C31),       // monster height
        PATCH_MEMORY(0x00,      1, 0x655E64),       // actor height (mini map)

        PATCH_MEMORY(0xEB,      1,  0x2CAA98),      // enable shimmer when width > 1024
        PATCH_MEMORY(0xEB,      1,  0x2C33BE),      // enable blur when width > 1024
        PATCH_MEMORY(0xEB,      1,  0x2EFBB8),      // capture ?

        PATCH_MEMORY(0x00,      1,  0x55F6E1),      // ±¬Áé

        PATCH_MEMORY(0x1CEB,    2,  0x64ACFE),      // remove crappy mouse control @ PositionWindow

        // monster info
        PATCH_MEMORY(0xEB,      1,  0x626AC8),      // bypass check is enemy


        // buf fix
        PATCH_MEMORY(0xEB,      1,  0x60CC8F),      // burst energy
        PATCH_MEMORY(0x32,      1,  0x54FDA4),      // text length of menu item created by MenuCmd(1, x, x)

        //PATCH_MEMORY(0x00,  1,  0x5304C9),      // skip op Sleep

        // iat hook

#if !D3D9_VER

        PATCH_MEMORY(CreateWindowExCenterA, 4, 0x9D59E8),       // CreateWindowExA
        PATCH_MEMORY(AoGetKeyState,         4, 0x9D5A00),       // GetKeyState
        PATCH_MEMORY(AoCreateFileA,         4, 0x9D576C),       // CreateFileA

        PATCH_MEMORY(8 * sizeof(ULONG_PTR), 4, 0x403E92),       // fix WNDCLASS::cbWndExtra

#endif

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
        //INLINE_HOOK_CALL_RVA_NULL(0x51E1C7, xxx),

        // tweak

        //INLINE_HOOK_CALL_RVA_NULL(0x40492A, ShowExitMessageBox),
        INLINE_HOOK_CALL_RVA_NULL(0x3640A1, InitWarningItpTimeStamp),   // bypass show warning.itp
        INLINE_HOOK_CALL_RVA_NULL(0x3E2B42, EDAO::NakedLoadSaveDataThumb),
        INLINE_HOOK_CALL_RVA_NULL(0x465F08, EDAO::NakedSetSaveDataScrollStep),

        INLINE_HOOK_JUMP_RVA     (0x279AA3, METHOD_PTR(&EDAO::CheckItemEquipped), EDAO::StubCheckItemEquipped),
        INLINE_HOOK_CALL_RVA_NULL(0x5DE1D9, METHOD_PTR(&CBattle::NakedNoResistConditionUp)),

        INLINE_HOOK_CALL_RVA_NULL(0x5F690B, CBattle::FormatBattleChrAT),
        INLINE_HOOK_CALL_RVA_NULL(0x5B05C6, CBattle::ShowSkipCraftAnimeButton),


        INLINE_HOOK_JUMP_RVA_NULL(0x46B6A0, METHOD_PTR(&CSoundPlayer::GetSoundControlWindow)),
        INLINE_HOOK_JUMP         (EATLookupRoutineByHashPNoFix(FindLdrModuleByName(&WCS2US(L"USER32.dll"))->DllBase, USER32_SendMessageA), CSoundPlayer::StaticDispatchCtrlCode, CSoundPlayer::StubStaticDispatchCtrlCode),

        // bug fix

        INLINE_HOOK_CALL_RVA_NULL(0x5B1BE6, METHOD_PTR(&CBattleATBar::LookupReplaceAtBarEntry)),
        INLINE_HOOK_JUMP_RVA     (0x275DAE, METHOD_PTR(&CBattle::ExecuteActionScript), CBattle::StubExecuteActionScript),

        INLINE_HOOK_JUMP_RVA     (0x550C90, METHOD_PTR(&CScript::ScpSaveRestoreParty), CScript::StubScpSaveRestoreParty),

        // file redirection

        INLINE_HOOK_CALL_RVA_NULL(0x48C1EA, AoFindFirstFileA),
        INLINE_HOOK_CALL_RVA_NULL(0x48C206, ZwClose),
        INLINE_HOOK_CALL_RVA_NULL(0x4E6A0B, GetCampImage),
        INLINE_HOOK_CALL_RVA_NULL(0x5A05B4, GetBattleFace),
        INLINE_HOOK_CALL_RVA_NULL(0x2F9101, GetFieldAttackChr),

#if D3D9_VER

        INLINE_HOOK_JUMP_NULL(EATLookupRoutineByHashPNoFix(GetKernel32Handle(), KERNEL32_CreateFileA), AoCreateFileA),

#endif

        // custom format itp / itc

        //INLINE_HOOK_JUMP_RVA(0x273D24, METHOD_PTR(&EDAOFileStream::Uncompress), EDAOFileStream::StubUncompress),

        // hack for boss

        INLINE_HOOK_CALL_RVA_NULL(0x5D1ED5, METHOD_PTR(&CBattle::NakedAS8DDispatcher)),
        INLINE_HOOK_CALL_RVA_NULL(0x56F7C7, METHOD_PTR(&CBattle::NakedGetChrIdForSCraft)),
        INLINE_HOOK_CALL_RVA_NULL(0x5E027B, METHOD_PTR(&CBattle::NakedGetTurnVoiceChrId)),
        INLINE_HOOK_CALL_RVA_NULL(0x5E1015, METHOD_PTR(&CBattle::NakedGetRunawayVoiceChrId)),
        INLINE_HOOK_CALL_RVA_NULL(0x5E0CA3, METHOD_PTR(&CBattle::NakedGetReplySupportVoiceChrId)),
        INLINE_HOOK_CALL_RVA_NULL(0x5E09E0, METHOD_PTR(&CBattle::NakedGetTeamRushVoiceChrId)),
        INLINE_HOOK_CALL_RVA_NULL(0x5DFA21, METHOD_PTR(&CBattle::NakedGetUnderAttackVoiceChrId)),
        INLINE_HOOK_CALL_RVA_NULL(0x5E081E, METHOD_PTR(&CBattle::NakedGetUnderAttackVoiceChrId2)),
        INLINE_HOOK_CALL_RVA_NULL(0x5E062B, METHOD_PTR(&CBattle::NakedGetSBreakVoiceChrId)),
        INLINE_HOOK_CALL_RVA_NULL(0x5A3644, METHOD_PTR(&CBattle::NakedCopyMagicAndCraftData)),
        INLINE_HOOK_CALL_RVA_NULL(0x5A3814, METHOD_PTR(&CBattle::NakedOverWriteBattleStatusWithChrStatus)),
        INLINE_HOOK_CALL_RVA_NULL(0x578368, METHOD_PTR(&CBattle::NakedIsChrStatusNeedRefresh)),
        INLINE_HOOK_CALL_RVA_NULL(0x622C83, METHOD_PTR(&EDAO::NakedGetChrSBreak)),
        INLINE_HOOK_JUMP_RVA     (0x277776, METHOD_PTR(&CGlobal::GetMagicData), CGlobal::StubGetMagicData),
        INLINE_HOOK_JUMP_RVA     (0x274E18, METHOD_PTR(&CGlobal::GetMagicQueryTable), CGlobal::StubGetMagicQueryTable),
        INLINE_HOOK_JUMP_RVA     (0x2767E0, METHOD_PTR(&CGlobal::GetMagicDescription), CGlobal::StubGetMagicDescription),
        INLINE_HOOK_CALL_RVA_NULL(0x332B26, METHOD_PTR(&EDAO::GetStatusIcon)),
        INLINE_HOOK_CALL_RVA_NULL(0x4948B9, METHOD_PTR(&EDAO::GetCFace)),
        INLINE_HOOK_CALL_RVA_NULL(0x4948DF, METHOD_PTR(&EDAO::GetCFace)),
        INLINE_HOOK_CALL_RVA_NULL(0x4A7487, METHOD_PTR(&CActor::GetTeamAttackMemberId)),
        INLINE_HOOK_CALL_RVA_NULL(0x4A74A7, METHOD_PTR(&CActor::GetTeamAttackMemberId)),


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
        INLINE_HOOK_JUMP_RVA_NULL(0x5D3545, METHOD_PTR(&CBattle::NakedAS_8D_5F)), //Ê±¿Õ´ó±À»µ


        //INLINE_HOOK_JUMP_RVA(0x275755, METHOD_PTR(&EDAO::Fade), EDAO::StubFade),
        //INLINE_HOOK_CALL_RVA_NULL(0x601122, FadeInRate),
    };

#if 0
    RtlSetUnhandledExceptionFilter(
        [] (PEXCEPTION_POINTERS ExceptionPointers) -> LONG
    {
        ExceptionBox(L"crashed");
        CreateMiniDump(ExceptionPointers);
        return ExceptionContinueSearch;
    }
        );

#endif

    Nt_PatchMemory(p, countof(p), f, countof(f), GetExeModuleHandle());

    Turbo = TRUE;

    //Ldr::LoadDll(L"ed_ao_ex.dll");

    return TRUE;
}

BOOL WINAPI DllMain(PVOID BaseAddress, ULONG Reason, PVOID Reserved)
{
    //PrintConsoleW(L"%d", FIELD_OFFSET(MONSTER_STATUS, SummonCount));

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
#pragma comment(linker, "/EXPORT:DirectInput8Create=_Arianrhod_DirectInput8Create@20")

NoInline BOOL IsCodeDecompressed()
{
    SEH_TRY
    {
        static ULONG Signature[] =
        {
		    0xe9003ffa, 0x0024ca08, 0x0e8a03e9, 0x78cee900,
            0xf9e90025, 0xe900276e, 0x00225f64, 0x0c354fe9,
            0x54dae900, 0xb5e90025, 0xe900033e, 0x004ebe90
        };

        return RtlCompareMemory((PVOID)0x672020, Signature, sizeof(Signature)) == sizeof(Signature);
    }
    SEH_EXCEPT(EXCEPTION_EXECUTE_HANDLER)
    {
        return FALSE;
    }
}

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

#if ENABLE_LOG
    {
        NtFileDisk f;
        f.Create(L"log.txt");
    }
#endif

    WriteLog(L"%08X\n", _ReturnAddress());

    if (IsCodeDecompressed())
    {
        DllMain(&__ImageBase, DLL_PROCESS_ATTACH, 0);
    }

    return Direct3DCreate9(SDKVersion);
}

EXTC
HRESULT
STDCALL
Arianrhod_DirectInput8Create(
    HINSTANCE   hinst,
    ULONG       Version,
    REFIID      riidltf,
    PVOID*      ppvOut,
    LPUNKNOWN   punkOuter
)
{
    static TYPE_OF(Arianrhod_DirectInput8Create) *DirectInput8Create;

    if (DirectInput8Create == NULL)
    {
        ULONG       Length;
        NTSTATUS    Status;
        PVOID       dinput8;
        WCHAR       DInput8Path[MAX_NTPATH];

        Length = Nt_GetSystemDirectory(DInput8Path, countof(DInput8Path));
        CopyStruct(DInput8Path + Length, L"dinput8.dll", sizeof(L"dinput8.dll"));

        dinput8 = Ldr::LoadDll(DInput8Path);
        if (dinput8 == NULL)
            return NULL;

        LdrAddRefDll(GET_MODULE_HANDLE_EX_FLAG_PIN, dinput8);

        *(PVOID *)&DirectInput8Create = GetRoutineAddress(dinput8, "DirectInput8Create");
        if (DirectInput8Create == NULL)
            return NULL;
    }

#if ENABLE_LOG
    {
        NtFileDisk f;
        f.Create(L"log.txt");
    }
#endif

    WriteLog(L"%08X\n", _ReturnAddress());

    if (IsCodeDecompressed())
    {
        static BOOL Hooked = FALSE;

        if (!Hooked)
        {
            DllMain(&__ImageBase, DLL_PROCESS_ATTACH, 0);
            Hooked = TRUE;
        }
    }

    return DirectInput8Create(hinst, Version, riidltf, ppvOut, punkOuter);
}

#endif
