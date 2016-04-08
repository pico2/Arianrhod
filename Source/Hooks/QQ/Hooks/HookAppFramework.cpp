#include "Hooks.h"

NTSTATUS (FASTCALL *StubAppFramework_RemoveRevokedMsg)(PVOID self, PVOID, ULONG flags);

NTSTATUS FASTCALL AppFramework_RemoveRevokedMsg(PVOID self, PVOID, ULONG flags)
{
/*
    BOOL fromSelf = flags != 0x80000000;

    AllocConsole();
    ShowWindow(GetConsoleWindow(), SW_SHOW);
    PrintConsole(L"flags = 0x%08X\n", flags);

    if (fromSelf)
        return StubAppFramework_RemoveRevokedMsg(self, nullptr, flags);
*/
    return STATUS_SUCCESS;
}

PVOID SearchAppFramework_RemoveRevokedMsg(PVOID ImageBase)
{
    static CHAR String[] = "nMsgIndex";

    return SearchStringAndReverseSearchHeader(ImageBase, String, sizeof(String) - sizeof(String[0]), 0x50);
}

NTSTATUS HookAppFramework(PVOID BaseAddress)
{
    /************************************************************************
        67B8983B   |> \8D45 80             lea     eax, [local.32]
        67B8983E   |.  50                  push    eax
        67B8983F   |.  897D 80             mov     [local.32], edi
        67B89842   |.  FF15 D805C967       call    dword ptr [<&Common.Util::Data::CreateTXData>]    ;  Common.Util::Data::CreateTXData
        67B89848   |.  59                  pop     ecx
        67B89849   |.  8D85 64FFFFFF       lea     eax, [local.39]
        67B8984F   |.  50                  push    eax
        67B89850   |.  51                  push    ecx
        67B89851   |.  8D85 74FFFFFF       lea     eax, [local.35]
        67B89857   |.  8BCC                mov     ecx, esp
        67B89859   |.  50                  push    eax
        67B8985A   |.  89BD 64FFFFFF       mov     [local.39], edi
        67B89860   |.  FF15 1806C967       call    dword ptr [<&Common.CTXStringW::CTXStringW>]      ;  Common.CTXStringW::CTXStringW
        67B89866   |.  6A FF               push    -0x1
        67B89868   |.  FF15 6C01C967       call    dword ptr [<&AFUtil.Util::AFChatSession::CreateMs>;  AFUtil.Util::AFChatSession::CreateMsgTipPack
        67B8986E   |.  83C4 0C             add     esp, 0xC
        67B89871   |.  85C0                test    eax, eax
        67B89873   |.  0F84 35010000       je      0x67B899AE
        67B89879   |.  39BD 64FFFFFF       cmp     [local.39], edi
        67B8987F   |.  0F84 29010000       je      0x67B899AE
        67B89885   |.  57                  push    edi
        67B89886   |.  FF75 F8             push    [local.2]
        67B89889   |.  FFB5 64FFFFFF       push    [local.39]
        67B8988F   |.  FF15 2809C967       call    dword ptr [<&KernelUtil.Util::Msg::SetMsgTime>]   ;  KernelUt.Util::Msg::SetMsgTime
        67B89895   |.  FFB5 70FFFFFF       push    [local.36]
        67B8989B   |.  FFB5 64FFFFFF       push    [local.39]
        67B898A1   |.  FF15 2409C967       call    dword ptr [<&KernelUtil.Util::Msg::SetMsgRand32>] ;  KernelUt.Util::Msg::SetMsgRand32
        67B898A7   |.  8B45 80             mov     eax, [local.32]
        67B898AA   |.  8B08                mov     ecx, dword ptr [eax]
        67B898AC   |.  83C4 14             add     esp, 0x14
        67B898AF   |.  FFB5 64FFFFFF       push    [local.39]
        67B898B5   |.  68 304FC967         push    0x67C94F30
        67B898BA   |.  68 403EC967         push    0x67C93E40                                        ;  ASCII "iMsgPack"
        67B898BF   |.  50                  push    eax
        67B898C0   |.  FF91 58010000       call    dword ptr [ecx+0x158]
        67B898C6   |.  8B45 80             mov     eax, [local.32]
        67B898C9   |.  8B08                mov     ecx, dword ptr [eax]
        67B898CB   |.  68 06020000         push    0x206
        67B898D0   |.  68 F83FC967         push    0x67C93FF8                                        ;  ASCII "dwShowType"
        67B898D5   |.  50                  push    eax
        67B898D6   |.  FF91 18010000       call    dword ptr [ecx+0x118]
        67B898DC   |.  8B45 80             mov     eax, [local.32]
        67B898DF   |.  8B08                mov     ecx, dword ptr [eax]
        67B898E1   |.  6A 03               push    0x3
        67B898E3   |.  68 B03EC967         push    0x67C93EB0                                        ;  ASCII "nInsertLocation"
        67B898E8   |.  50                  push    eax
        67B898E9   |.  FF91 20010000       call    dword ptr [ecx+0x120]
        67B898EF   |.  8B85 68FFFFFF       mov     eax, [local.38]
        67B898F5   |.  8D55 88             lea     edx, [local.30]
        67B898F8   |.  52                  push    edx
        67B898F9   |.  BE E03FC967         mov     esi, 0x67C93FE0                                   ;  ASCII "dwMsgCookie"
        67B898FE   |.  56                  push    esi
        67B898FF   |.  897D 88             mov     [local.30], edi
        67B89902   |.  8B08                mov     ecx, dword ptr [eax]
        67B89904   |.  50                  push    eax
        67B89905   |.  FF51 48             call    dword ptr [ecx+0x48]
        67B89908   |.  85C0                test    eax, eax
        67B8990A       79 36               jns     short 0x67B89942
        67B8990C   |>  8D8D 64FFFFFF       lea     ecx, [local.39]
        67B89912   |.  E8 77A90A00         call    0x67C3428E
        67B89917   |.  8D4D 80             lea     ecx, [local.32]
        67B8991A   |.  E8 6FA90A00         call    0x67C3428E
        67B8991F   |.  8D8D 6CFFFFFF       lea     ecx, [local.37]
        67B89925   |.  E8 64A90A00         call    0x67C3428E
        67B8992A   |.  8D8D 68FFFFFF       lea     ecx, [local.38]
        67B89930   |.  E8 59A90A00         call    0x67C3428E
        67B89935   |.  8D4D 84             lea     ecx, [local.31]
        67B89938   |.  E8 51A90A00         call    0x67C3428E
        67B8993D   |.^ E9 50FBFFFF         jmp     0x67B89492
        67B89942   |>  FF75 88             push    [local.30]                                        ;  removeMsg
        67B89945   |.  8B8D 60FFFFFF       mov     ecx, [local.40]
        67B8994B       E8 5088FFFF         call    <removeMsg>
        67B89950   |.  FF75 88             push    [local.30]
        67B89953   |.  8B45 80             mov     eax, [local.32]
        67B89956   |.  8B08                mov     ecx, dword ptr [eax]
        67B89958   |.  56                  push    esi
        67B89959   |.  50                  push    eax
        67B8995A   |.  FF91 18010000       call    dword ptr [ecx+0x118]
        67B89960   |.  FFB5 4CFFFFFF       push    [local.45]
        67B89966   |.  8B45 80             mov     eax, [local.32]
        67B89969   |.  8B08                mov     ecx, dword ptr [eax]
        67B8996B   |.  68 D86EC967         push    0x67C96ED8                                        ;  ASCII "uInsertDetailPos"
        67B89970   |.  50                  push    eax
        67B89971   |.  FF91 18010000       call    dword ptr [ecx+0x118]
        67B89977   |.  8B85 24FFFFFF       mov     eax, [local.55]
        67B8997D   |.  40                  inc     eax
        67B8997E   |.  3B85 50FFFFFF       cmp     eax, [local.44]
        67B89984       75 03               jnz     short 0x67B89989
        67B89986   |.  33FF                xor     edi, edi
        67B89988       47                  inc     edi
        67B89989   |>  8B45 80             mov     eax, [local.32]
        67B8998C   |.  8B08                mov     ecx, dword ptr [eax]
        67B8998E   |.  57                  push    edi
        67B8998F   |.  68 5471C967         push    0x67C97154                                        ;  ASCII "bBreakMsgFlowMerge"
        67B89994   |.  50                  push    eax
        67B89995   |.  FF91 F0000000       call    dword ptr [ecx+0xF0]
        67B8999B   |.  FF75 80             push    [local.32]
        67B8999E   |.  8B8D 60FFFFFF       mov     ecx, [local.40]
        67B899A4   |.  E8 1BE4FFFF         call    <showRevokeTip>                                   ;  <--

    ************************************************************************/

    Mp::PATCH_MEMORY_DATA Function_AppFramework[] =
    {
        Mp::FunctionJumpVa(SearchAppFramework_RemoveRevokedMsg(BaseAddress), AppFramework_RemoveRevokedMsg, &StubAppFramework_RemoveRevokedMsg),
    };

    return Mp::PatchMemory(Function_AppFramework, countof(Function_AppFramework), BaseAddress);
}
