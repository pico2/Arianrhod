#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")

#include "edao.h"
#include "SoundArc.h"
#include "MyLibrary.cpp"
#include "edao_vm.h"

#define ENABLE_LOG  0
#define DEBUG_DISABLE_PATCH 0

#if !D3D9_VER
    #undef ENABLE_LOG
    #define ENABLE_LOG 0
#endif

BOOL WINAPI DllMain(PVOID BaseAddress, ULONG Reason, PVOID Reserved);

TYPE_OF(&NtOpenFile)            StubNtOpenFile;
TYPE_OF(&NtCreateFile)          StubNtCreateFile;
TYPE_OF(&NtQueryAttributesFile) StubNtQueryAttributesFile;


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
WNDPROC WindowProc;

SHORT NTAPI AoGetKeyState(int VirtualKey)
{
    switch (VirtualKey)
    {
        case VK_LSHIFT:
            VirtualKey = VK_SHIFT;

        case VK_SHIFT:

            if (!Turbo)
                break;

            ++*EDAO::GlobalGetEDAO()->GetMap()->GetFrameNumber();

            return (SHORT)0xFFFF8001;
    }

    return GetKeyState(VirtualKey);
}

LRESULT NTAPI MainWndProc(HWND Window, UINT Message, WPARAM wParam, LPARAM lParam)
{
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
    }

    return WindowProc(Window, Message, wParam, lParam);
}

VOID ChangeMainWindowProc(HWND GameWindow)
{
    if (GameWindow != nullptr)
        WindowProc = (WNDPROC)SetWindowLongPtrA(GameWindow, GWL_WNDPROC, (LONG_PTR)MainWndProc);
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
    ChangeMainWindowProc(Window);

    return Window;
}


typedef struct
{
    UNICODE_STRING Original;
    UNICODE_STRING Redirected;

} FILE_REDIRECT_ENTRY, *PFILE_REDIRECT_ENTRY;

PFILE_REDIRECT_ENTRY GlobalRedirectEntry;

#define REDIRECT_PATH(orig, redir) { RTL_CONSTANT_STRING(orig), RTL_CONSTANT_STRING(redir) }


NTSTATUS InitializeRedirectEntry()
{
    NTSTATUS                Status;
    UNICODE_STRING          ExePath;
    PLDR_MODULE             Module;
    PWSTR                   Buffer;
    ULONG_PTR               Length;
    PFILE_REDIRECT_ENTRY    Entry, RedirectEntry;

    static FILE_REDIRECT_ENTRY RedirectSubDirectory[] =
    {
        REDIRECT_PATH(L"data\\", L"patch\\"),
        REDIRECT_PATH(L"data\\", L"patch2\\"),
    };

    Module = FindLdrModuleByHandle(nullptr);
    Status = NtFileDisk::QueryFullNtPath(Module->FullDllName.Buffer, &ExePath);
    FAIL_RETURN(Status);

    RedirectEntry = (PFILE_REDIRECT_ENTRY)AllocateMemoryP((countof(RedirectSubDirectory) + 1) * sizeof(*RedirectEntry), HEAP_ZERO_MEMORY);
    if (RedirectEntry == nullptr)
    {
        RtlFreeUnicodeString(&ExePath);
        return STATUS_NO_MEMORY;
    }

    GlobalRedirectEntry = RedirectEntry;

    ExePath.Length -= Module->BaseDllName.Length;
    Length = 0;
    FOR_EACH(Entry, RedirectSubDirectory, countof(RedirectSubDirectory))
    {
        Length = ML_MAX(Entry->Original.Length, ML_MAX(Entry->Redirected.Length, Length));
    }

    Length += ExePath.Length;

    Buffer = (PWSTR)AllocStack(Length + sizeof(WCHAR));

    FOR_EACH(Entry, RedirectSubDirectory, countof(RedirectSubDirectory))
    {
        CopyMemory(Buffer, ExePath.Buffer, ExePath.Length);
        CopyMemory(PtrAdd(Buffer, ExePath.Length), Entry->Original.Buffer, Entry->Original.Length);
        *PtrAdd(Buffer, ExePath.Length + Entry->Original.Length) = 0;
        RtlCreateUnicodeString(&RedirectEntry->Original, Buffer);

        CopyMemory(PtrAdd(Buffer, ExePath.Length), Entry->Redirected.Buffer, Entry->Redirected.Length);
        *PtrAdd(Buffer, ExePath.Length + Entry->Redirected.Length) = 0;
        RtlCreateUnicodeString(&RedirectEntry->Redirected, Buffer);

        ++RedirectEntry;
    }

    return STATUS_SUCCESS;
}

NTSTATUS GetRedirectedFileName(PUNICODE_STRING OriginalFile, PUNICODE_STRING RedirectedFile)
{
    ULONG_PTR               Length, BufferLength;
    PWSTR                   Buffer;
    NTSTATUS                Status;
    UNICODE_STRING          SubFilePath, Redirected, OriginalPath;
    OBJECT_ATTRIBUTES       oa;
    FILE_BASIC_INFORMATION  FileBasic;
    PFILE_REDIRECT_ENTRY    Entry;

    RtlInitEmptyString(RedirectedFile);

    Entry = GlobalRedirectEntry;
    if (Entry == nullptr)
        return STATUS_FLT_NOT_INITIALIZED;

    if (OriginalFile == nullptr || OriginalFile->Buffer == nullptr)
    {
        return STATUS_INVALID_PARAMETER;
    }

    Status = NtFileDisk::QueryFullNtPath(OriginalFile->Buffer, &OriginalPath);
    FAIL_RETURN(Status);

    BufferLength = MAX_NTPATH * sizeof(WCHAR);
    Buffer = (PWSTR)AllocStack(BufferLength);
    SubFilePath = OriginalPath;

    FOR_EACH(Entry, Entry, ~0u)
    {
        if (Entry->Original.Buffer == nullptr)
            return STATUS_NO_MATCH;

        if (OriginalPath.Length <= Entry->Original.Length)
            continue;

        SubFilePath.Length = Entry->Original.Length;
        if (!RtlEqualUnicodeString(&SubFilePath, &Entry->Original, TRUE))
            continue;

        Length = Entry->Redirected.Length + OriginalPath.Length - SubFilePath.Length + sizeof(WCHAR);
        if (Length > BufferLength)
        {
            Buffer = (PWSTR)AllocStack(Length - BufferLength);
            BufferLength = Length;
        }

        Length = OriginalPath.Length - SubFilePath.Length;

        CopyMemory(Buffer, Entry->Redirected.Buffer, Entry->Redirected.Length);
        CopyMemory(PtrAdd(Buffer, Entry->Redirected.Length), PtrAdd(OriginalPath.Buffer, SubFilePath.Length), Length);
        Length += Entry->Redirected.Length;
        *PtrAdd(Buffer, Length) = 0;

        Redirected.Length           = (USHORT)Length;
        Redirected.MaximumLength    = Redirected.Length;
        Redirected.Buffer           = Buffer;

        InitializeObjectAttributes(&oa, &Redirected, OBJ_CASE_INSENSITIVE, nullptr, 0);
        Status = StubNtQueryAttributesFile(&oa, &FileBasic);
        if (
            NT_SUCCESS(Status) &&
            FileBasic.FileAttributes != INVALID_FILE_ATTRIBUTES &&
            FLAG_OFF(FileBasic.FileAttributes, FILE_ATTRIBUTE_DIRECTORY)
           )
        {
            Status = RtlDuplicateUnicodeString(RTL_DUPSTR_ADD_NULL, &Redirected, RedirectedFile);
            if (NT_SUCCESS(Status))
                break;
        }
    }

    RtlFreeUnicodeString(&OriginalPath);

    return STATUS_SUCCESS;
}

NTSTATUS
NTAPI
AoOpenFile(
    PHANDLE             FileHandle,
    ACCESS_MASK         DesiredAccess,
    POBJECT_ATTRIBUTES  ObjectAttributes,
    PIO_STATUS_BLOCK    IoStatusBlock,
    ULONG               ShareAccess,
    ULONG               OpenOptions
)
{
    NTSTATUS            Status;
    OBJECT_ATTRIBUTES   LocalObjectAttributes;
    UNICODE_STRING      Redirected;

    RtlInitEmptyString(&Redirected);

    LOOP_ONCE
    {
        if (ObjectAttributes == nullptr)
            break;

        Status = GetRedirectedFileName(ObjectAttributes->ObjectName, &Redirected);
        FAIL_BREAK(Status);

        LocalObjectAttributes               = *ObjectAttributes;
        LocalObjectAttributes.ObjectName    = &Redirected;
        LocalObjectAttributes.RootDirectory = nullptr;

        CLEAR_FLAG(LocalObjectAttributes.Attributes, OBJ_INHERIT);

        ObjectAttributes = &LocalObjectAttributes;
    }

    Status = StubNtOpenFile(FileHandle, DesiredAccess, ObjectAttributes, IoStatusBlock, ShareAccess, OpenOptions);

    RtlFreeUnicodeString(&Redirected);

    return Status;
}

NTSTATUS
NTAPI
AoCreateFile(
    PHANDLE             FileHandle,
    ACCESS_MASK         DesiredAccess,
    POBJECT_ATTRIBUTES  ObjectAttributes,
    PIO_STATUS_BLOCK    IoStatusBlock,
    PLARGE_INTEGER      AllocationSize,
    ULONG               FileAttributes,
    ULONG               ShareAccess,
    ULONG               CreateDisposition,
    ULONG               CreateOptions,
    PVOID               EaBuffer,
    ULONG               EaLength
)
{
    NTSTATUS            Status;
    UNICODE_STRING      RedirectedFile;
    OBJECT_ATTRIBUTES   LocalObjectAttributes;

    RtlInitEmptyString(&RedirectedFile);

    if (ObjectAttributes != nullptr)
    {
        if (NT_SUCCESS(GetRedirectedFileName(ObjectAttributes->ObjectName, &RedirectedFile)))
        {
            LocalObjectAttributes               = *ObjectAttributes;
            LocalObjectAttributes.ObjectName    = &RedirectedFile;
            LocalObjectAttributes.RootDirectory = nullptr;

            CLEAR_FLAG(LocalObjectAttributes.Attributes, OBJ_INHERIT);

            ObjectAttributes = &LocalObjectAttributes;
        }
    }

    Status = StubNtCreateFile(
                FileHandle,
                DesiredAccess,
                ObjectAttributes,
                IoStatusBlock,
                AllocationSize,
                FileAttributes,
                ShareAccess,
                CreateDisposition,
                CreateOptions,
                EaBuffer,
                EaLength
            );

    RtlFreeUnicodeString(&RedirectedFile);

    return Status;
}

NTSTATUS
NTAPI
AoQueryAttributesFile(
    POBJECT_ATTRIBUTES      ObjectAttributes,
    PFILE_BASIC_INFORMATION FileInformation
)
{
    NTSTATUS            Status;
    OBJECT_ATTRIBUTES   LocalObjectAttributes;
    UNICODE_STRING      Redirected;

    RtlInitEmptyString(&Redirected);

    LOOP_ONCE
    {
        if (ObjectAttributes == nullptr)
            break;

        Status = GetRedirectedFileName(ObjectAttributes->ObjectName, &Redirected);
        FAIL_BREAK(Status);

        LocalObjectAttributes               = *ObjectAttributes;
        LocalObjectAttributes.ObjectName    = &Redirected;
        LocalObjectAttributes.RootDirectory = nullptr;

        CLEAR_FLAG(LocalObjectAttributes.Attributes, OBJ_INHERIT);

        ObjectAttributes = &LocalObjectAttributes;
    }

    Status = StubNtQueryAttributesFile(ObjectAttributes, FileInformation);

    RtlFreeUnicodeString(&Redirected);

    return Status;
}

HANDLE NTAPI AoFindFirstFileA(PCSTR FileName, PWIN32_FIND_DATAA FindFileData)
{
    NTSTATUS        Status;
    HANDLE          FindHandle;
    ML_FIND_DATA    FindData;
    UNICODE_STRING  FileToFind, RedirectedFile;

    Status = AnsiToUnicodeString(&FileToFind, FileName);
    if (NT_FAILED(Status))
        return nullptr;

    Status = GetRedirectedFileName(&FileToFind, &RedirectedFile);
    Status = QueryFirstFile(
                    &FindHandle,
                    NT_SUCCESS(Status) ? RedirectedFile.Buffer : FileToFind.Buffer,
                    &FindData
                );

    RtlFreeUnicodeString(&FileToFind);
    RtlFreeUnicodeString(&RedirectedFile);

    FindFileData->cFileName[0] = 0;

    if (NT_FAILED(Status))
        return nullptr;

    UnicodeToAnsi(FindFileData->cFileName, countof(FindFileData->cFileName), FindData.FileName);

    return FindHandle;
}

BOOL AoIsFileExist(PCSTR FileName)
{
    BOOL            Exists;
    NTSTATUS        Status;
    UNICODE_STRING  FileToCheck;

    Status = AnsiToUnicodeString(&FileToCheck, FileName);
    if (NT_FAILED(Status))
        return FALSE;

    Exists = IsPathExists(FileToCheck.Buffer);

    RtlFreeUnicodeString(&FileToCheck);

    return Exists;
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

    InitializeRedirectEntry();


    static DOUBLE DefaultDistance = 0.f;

    BYTE PushActorDistance[6] = { 0xDD, 0x05 };

    *(DOUBLE **)&PushActorDistance[2] = &DefaultDistance;

    MEMORY_PATCH p[] =
    {
        PATCH_MEMORY(0xEB,      1, 0x2C15B7),    // bypass CGlobal::SetStatusDataForChecking

#if !DEBUG_DISABLE_PATCH

        PATCH_MEMORY(0x06,      1, 0x410731),    // win
        PATCH_MEMORY(0x06,      1, 0x410AD1),    // win
        PATCH_MEMORY(0x01,      1, 0x40991D),    // cpu
        PATCH_MEMORY(0x91,      1, 0x2F9EE3),    // one hit
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

        // monster info
        PATCH_MEMORY(0xEB,      1,  0x626AC8),      // bypass check is enemy


        // buf fix
        PATCH_MEMORY(0xEB,      1,  0x60CC8F),      // burst energy
        PATCH_MEMORY(0x32,      1,  0x54FDA4),      // text length of menu item created by MenuCmd(1, x, x)
        // PATCH_MEMORY(0x37,      1,  0x5006B8),      // dead lock while exiting

        //PATCH_MEMORY(0x00,  1,  0x5304C9),      // skip op Sleep

        // iat hook

        PATCH_MEMORY(AoGetKeyState,         4, 0x9D5A00),       // GetKeyState

#if !D3D9_VER

        PATCH_MEMORY(0x1CEB,                2, 0x64ACFE),       // remove crappy mouse control @ PositionWindow
        PATCH_MEMORY(0x00,                  4, 0x329851),       // disable foolish get joy stick pos
        PATCH_MEMORY(CreateWindowExCenterA, 4, 0x9D59E8),       // CreateWindowExA
        PATCH_MEMORY(8 * sizeof(ULONG_PTR), 4, 0x403E92),       // fix WNDCLASS::cbWndExtra

#endif

#endif // DEBUG_DISABLE_PATCH

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

#if !DEBUG_DISABLE_PATCH

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

        INLINE_HOOK_CALL_RVA     (0x328C77, METHOD_PTR(&CInput::HandleMainInterfaceInputState), CInput::StubHandleMainInterfaceInputState),

        // bug fix

        INLINE_HOOK_CALL_RVA_NULL(0x5B1BE6, METHOD_PTR(&CBattleATBar::LookupReplaceAtBarEntry)),
        INLINE_HOOK_JUMP_RVA     (0x275DAE, METHOD_PTR(&CBattle::ExecuteActionScript), CBattle::StubExecuteActionScript),
        INLINE_HOOK_JUMP_RVA     (0x550C90, METHOD_PTR(&CScript::ScpSaveRestoreParty), CScript::StubScpSaveRestoreParty),

        INLINE_HOOK_CALL_RVA_NULL(0x6A58FF, CMiniGame::HorrorHouse_GetMonsterPosition),


        // file redirection

        INLINE_HOOK_JUMP         (ZwOpenFile,               AoOpenFile,             StubNtOpenFile),
        INLINE_HOOK_JUMP         (ZwCreateFile,             AoCreateFile,           StubNtCreateFile),
        INLINE_HOOK_JUMP         (ZwQueryAttributesFile,    AoQueryAttributesFile,  StubNtQueryAttributesFile),
        INLINE_HOOK_CALL_RVA_NULL(0x48C1EA,                 AoFindFirstFileA),
        INLINE_HOOK_CALL_RVA_NULL(0x48C206,                 ZwClose),
        INLINE_HOOK_CALL_RVA_NULL(0x4E6A0B,                 EDAO::GetCampImage),
        INLINE_HOOK_CALL_RVA_NULL(0x5A05B4,                 EDAO::GetBattleFace),
        INLINE_HOOK_CALL_RVA_NULL(0x2F9101,                 EDAO::GetFieldAttackChr),
        INLINE_HOOK_CALL_RVA_NULL(0x4948B9,                 METHOD_PTR(&EDAO::GetCFace)),
        INLINE_HOOK_CALL_RVA_NULL(0x4948DF,                 METHOD_PTR(&EDAO::GetCFace)),


        // custom format itp / itc
        //INLINE_HOOK_JUMP_RVA(0x273D24, METHOD_PTR(&EDAOFileStream::Uncompress), EDAOFileStream::StubUncompress),


        // hack for boss

        INLINE_HOOK_CALL_RVA_NULL(0x5D1ED5, METHOD_PTR(&CBattle::   NakedAS8DDispatcher)),
        INLINE_HOOK_CALL_RVA_NULL(0x56F7C7, METHOD_PTR(&CBattle::   NakedGetChrIdForSCraft)),
        INLINE_HOOK_CALL_RVA_NULL(0x5E027B, METHOD_PTR(&CBattle::   NakedGetTurnVoiceChrId)),
        INLINE_HOOK_CALL_RVA_NULL(0x5E1015, METHOD_PTR(&CBattle::   NakedGetRunawayVoiceChrId)),
        INLINE_HOOK_CALL_RVA_NULL(0x5E0CA3, METHOD_PTR(&CBattle::   NakedGetReplySupportVoiceChrId)),
        INLINE_HOOK_CALL_RVA_NULL(0x5E09E0, METHOD_PTR(&CBattle::   NakedGetTeamRushVoiceChrId)),
        INLINE_HOOK_CALL_RVA_NULL(0x5DFA1B, METHOD_PTR(&CBattle::   NakedGetUnderAttackVoiceChrId)),
        INLINE_HOOK_CALL_RVA_NULL(0x5E081E, METHOD_PTR(&CBattle::   NakedGetUnderAttackVoiceChrId2)),
        INLINE_HOOK_CALL_RVA_NULL(0x5E062B, METHOD_PTR(&CBattle::   NakedGetSBreakVoiceChrId)),
        INLINE_HOOK_CALL_RVA_NULL(0x5A3644, METHOD_PTR(&CBattle::   NakedCopyMagicAndCraftData)),
        INLINE_HOOK_CALL_RVA_NULL(0x5A3814, METHOD_PTR(&CBattle::   NakedOverWriteBattleStatusWithChrStatus)),
        INLINE_HOOK_CALL_RVA_NULL(0x578368, METHOD_PTR(&CBattle::   NakedIsChrStatusNeedRefresh)),
        INLINE_HOOK_CALL_RVA_NULL(0x622C83, METHOD_PTR(&EDAO::      NakedGetChrSBreak)),
        INLINE_HOOK_JUMP_RVA     (0x277776, METHOD_PTR(&CGlobal::   GetMagicData),          CGlobal::StubGetMagicData),
        INLINE_HOOK_JUMP_RVA     (0x274E18, METHOD_PTR(&CGlobal::   GetMagicQueryTable),    CGlobal::StubGetMagicQueryTable),
        INLINE_HOOK_JUMP_RVA     (0x2767E0, METHOD_PTR(&CGlobal::   GetMagicDescription),   CGlobal::StubGetMagicDescription),
        INLINE_HOOK_CALL_RVA_NULL(0x332B26, METHOD_PTR(&EDAO::      GetStatusIcon)),
        INLINE_HOOK_CALL_RVA_NULL(0x2F82B8, METHOD_PTR(&EDAO::      GetLeaderChangeVoice)),
        INLINE_HOOK_CALL_RVA_NULL(0x4A7487, METHOD_PTR(&CSSaveData::GetTeamAttackMemberId)),
        INLINE_HOOK_CALL_RVA_NULL(0x4A74A7, METHOD_PTR(&CSSaveData::GetTeamAttackMemberId)),


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

#endif // DEBUG_DISABLE_PATCH

    };

    Nt_PatchMemory(p, countof(p), f, countof(f), GetExeModuleHandle());

    Turbo = TRUE;

#if D3D9_VER

    Ldr::LoadDll(L"ed_ao_ex.dll");

#endif

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
