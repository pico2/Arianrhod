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

NAKED VOID FadeInRate()
{
    INLINE_ASM
    {
        fld     dword ptr [eax+0x40];
        fmul    Rate;
        ret;
    }
}

HWND WINAPI CreateWindowExCenterA(DWORD dwExStyle, LPCSTR lpClassName, LPCSTR lpWindowName, DWORD dwStyle, int X, int Y, int nWidth, int nHeight, HWND hWndParent, HMENU hMenu, HINSTANCE hInstance, LPVOID lpParam)
{
    RECT    rcWordArea;
    ULONG   Length;
    PWSTR  pszClassName, pszWindowName;

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

    return CreateWindowExW(dwExStyle, pszClassName, pszWindowName, dwStyle, X, Y, nWidth, nHeight, hWndParent, hMenu, hInstance, lpParam);
}

LONG64 InitWarningItpTimeStamp()
{
    return -1;
}

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

#define METHOD_PTR(_method) PtrAdd((PVOID)NULL, _method)

BOOL Initialize(PVOID BaseAddress)
{
    MEMORY_PATCH p[] =
    {
        PATCH_MEMORY(0xEB, 1, 0x2C15B7),    // bypass CGlobal::SetStatusDataForChecking
        PATCH_MEMORY(0x06, 1, 0x410731),    // win
        PATCH_MEMORY(0x06, 1, 0x410AD1),    // win
        PATCH_MEMORY(0x01, 1, 0x40991D),    // cpu

        PATCH_MEMORY(CreateWindowExCenterA, 4, 0x9D59E8),       // CreateWindowExA
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
