NAKED VOID CBattle::USE_SCRAFT_FOR_CHECKING()
{
    INLINE_ASM
    {
        push    ebp
        mov     ebp, esp
        sub     esp, 0xD8
        push    ebx
        push    esi
        push    edi
        //push    ecx
        //lea     edi, dword ptr [ebp-0xD8]
        //mov     ecx, 0x36
        //mov     eax, 0xCCCCCCCC
        //rep     stos dword ptr es:[edi]
        //pop     ecx
        mov     dword ptr [ebp-0x8], ecx
        mov     eax, 0x4
        mov     ecx, dword ptr [ebp+0x8]
        mov     word ptr [ecx+0x172], ax
        mov     eax, dword ptr [ebp+0x8]
        mov     cx, word ptr [ebp+0xC]
        mov     word ptr [eax+0x17E], cx
        mov     eax, dword ptr [ebp+0x10]
        imul    eax, eax, 0x18
        mov     ecx, dword ptr [ebp+0x8]
        lea     edx, dword ptr [ecx+eax+0xE64];
        mov     dword ptr [ebp-0x14], edx
        mov     eax, dword ptr [ebp+0x8]
        mov     cx, word ptr [ebp+0x10]
        mov     word ptr [eax+0x182], cx
        mov     eax, dword ptr [ebp+0x8]
        mov     cx, word ptr [ebp+0xC]
        mov     word ptr [eax+0xF24], cx;
        mov     eax, dword ptr [ebp+0x8]
        mov     ecx, dword ptr [ebp-0x14]
        mov     dl, byte ptr [ecx+0x4]
        mov     byte ptr [eax+0xF26], dl;
        mov     eax, dword ptr [ebp+0x8]
        mov     ecx, dword ptr [ebp-0x14]
        mov     dl, byte ptr [ecx+0x5]
        mov     byte ptr [eax+0xF27], dl;
        pop     edi
        pop     esi
        pop     ebx
        mov     esp, ebp
        pop     ebp
        ret     0xC
    }
}

NAKED VOID CBattle::USE_CRAFT_FOR_CHECKING()
{
    INLINE_ASM
    {
        push    ebp
        mov     ebp, esp
        sub     esp, 0xD8
        push    ebx
        push    esi
        push    edi
        //push    ecx
        //lea     edi, dword ptr [ebp-0xD8]
        //mov     ecx, 0x36
        //mov     eax, 0xCCCCCCCC
        //rep     stos dword ptr es:[edi]
        //pop     ecx
        mov     dword ptr [ebp-0x8], ecx
        mov     eax, 0x3
        mov     ecx, dword ptr [ebp+0x8]
        mov     word ptr [ecx+0x172], ax
        mov     eax, dword ptr [ebp+0x8]
        mov     cx, word ptr [ebp+0xC]
        mov     word ptr [eax+0x17E], cx
        mov     eax, dword ptr [ebp+0x10]
        imul    eax, eax, 0x18
        mov     ecx, dword ptr [ebp+0x8]
        lea     edx, dword ptr [ecx+eax+0xCFC];
        mov     dword ptr [ebp-0x14], edx
        mov     eax, dword ptr [ebp+0x8]
        mov     cx, word ptr [ebp+0x10]
        mov     word ptr [eax+0x182], cx
        mov     eax, dword ptr [ebp+0x8]
        mov     cx, word ptr [ebp+0xC]
        mov     word ptr [eax+0xF24], cx;
        mov     eax, dword ptr [ebp+0x8]
        mov     ecx, dword ptr [ebp-0x14]
        mov     dl, byte ptr [ecx+0x4]
        mov     byte ptr [eax+0xF26], dl;
        mov     eax, dword ptr [ebp+0x8]
        mov     ecx, dword ptr [ebp-0x14]
        mov     dl, byte ptr [ecx+0x5]
        mov     byte ptr [eax+0xF27], dl;
        pop     edi
        pop     esi
        pop     ebx
        mov     esp, ebp
        pop     ebp
        ret     0xC
    }
}

NAKED VOID CBattle::USE_MAGIC_FOR_CHECKING()
{
    INLINE_ASM
    {
        push    ebp
        mov     ebp, esp
        sub     esp, 0xCC
        push    ebx
        push    esi
        push    edi
        //push    ecx
        //lea     edi, dword ptr [ebp-0xCC]
        //mov     ecx, 0x33
        //mov     eax, 0xCCCCCCCC
        //rep     stos dword ptr es:[edi]
        //pop     ecx
        mov     dword ptr [ebp-0x8], ecx
        mov     eax, 0x2
        mov     ecx, dword ptr [ebp+0x8]
        mov     word ptr [ecx+0x172], ax
        mov     eax, dword ptr [ebp+0x8]
        mov     cx, word ptr [ebp+0xC]
        mov     word ptr [eax+0x17E], cx
        mov     eax, dword ptr [ebp+0x8]
        mov     cx, word ptr [ebp+0x10]
        mov     word ptr [eax+0x182], cx
        mov     eax, dword ptr [ebp+0x8]
        mov     cx, word ptr [ebp+0xC]
        mov     word ptr [eax+0xF24], cx;
        mov     eax, dword ptr [ebp+0x8]
        mov     byte ptr [eax+0xF26], 0x6;
        mov     eax, dword ptr [ebp+0x8]
        mov     byte ptr [eax+0xF27], 0x7;
        pop     edi
        pop     esi
        pop     ebx
        mov     esp, ebp
        pop     ebp
        ret     0xC
    }
}

NAKED VOID CBattle::USE_ATTACK_FOR_CHECKING()
{
    INLINE_ASM
    {
        push    ebp
        mov     ebp, esp
        sub     esp, 0xCC
        push    ebx
        push    esi
        push    edi
        //push    ecx
        //lea     edi, dword ptr [ebp-0xCC]
        //mov     ecx, 0x33
        //mov     eax, 0xCCCCCCCC
        //rep     stos dword ptr es:[edi]
        //pop     ecx
        mov     dword ptr [ebp-0x8], ecx
        xor     eax, eax
        mov     ecx, dword ptr [ebp+0x8]
        mov     word ptr [ecx+0x172], ax
        mov     eax, dword ptr [ebp+0x8]
        mov     ecx, dword ptr [ebp+0x8]
        mov     dx, word ptr [ecx+0x56A];
        mov     word ptr [eax+0x17E], dx
        mov     eax, 0xFFFF
        mov     ecx, dword ptr [ebp+0x8]
        mov     word ptr [ecx+0x182], ax
        mov     eax, dword ptr [ebp+0x8]
        mov     ecx, dword ptr [ebp+0x8]
        mov     dl, byte ptr [ecx+0x569];
        mov     byte ptr [eax+0xF27], dl;
        mov     eax, dword ptr [ebp+0x8]
        mov     ecx, dword ptr [ebp+0x8]
        mov     dl, byte ptr [ecx+0x568];
        mov     byte ptr [eax+0xF26], dl;
        mov     eax, dword ptr [ebp+0x8]
        mov     ecx, dword ptr [ebp+0x8]
        mov     dx, word ptr [ecx+0x56A];
        mov     word ptr [eax+0xF24], dx;
        pop     edi
        pop     esi
        pop     ebx
        mov     esp, ebp
        pop     ebp
        ret     0x4
    }
}


NAKED VOID CSSaveData::SaveData2SystemData()
{
    INLINE_ASM
    {
        push    ebp
        mov     ebp, esp
        sub     esp, 0xD8
        push    ebx
        push    esi
        push    edi
        //push    ecx
        //lea     edi, dword ptr [ebp-0xD8]
        //mov     ecx, 0x36
        //mov     eax, 0xCCCCCCCC
        //rep     stos dword ptr es:[edi]
        //pop     ecx
        mov     dword ptr [ebp-0x8], ecx
        cmp     dword ptr [ebp+0x8], 0x0
        jnz L016
        jmp L071
L016:
        mov     eax, dword ptr ds:[0xC29988];
        mov     dword ptr [ebp-0x14], eax
        push    0x504
        push    0x0
        mov     eax, dword ptr [ebp+0x8]
        push    eax
        call    memset
        add     esp, 0xC
        push    0x8
        mov     eax, dword ptr [ebp-0x14]
        add     eax, 0x81C7C;
        push    eax
        mov     ecx, dword ptr [ebp+0x8]
        add     ecx, 0x4C4
        push    ecx
        call    memcpy
        add     esp, 0xC
        push    0x4C4
        mov     eax, dword ptr [ebp-0x14]
        add     eax, 0x817AC;
        push    eax
        mov     ecx, dword ptr [ebp+0x8]
        push    ecx
        call    memcpy
        add     esp, 0xC
        mov     eax, dword ptr [ebp+0x8]
        mov     ecx, dword ptr [ebp-0x14]
        mov     edx, dword ptr [ecx+0x81C84];
        mov     dword ptr [eax+0x4D0], edx
        mov     eax, dword ptr [ebp+0x8]
        mov     ecx, dword ptr [ebp-0x14]
        mov     edx, dword ptr [ecx+0xA70C4];
        mov     dword ptr [eax+0x4CC], edx
        mov     eax, dword ptr [ebp+0x8]
        mov     ecx, dword ptr [ebp-0x14]
        mov     edx, dword ptr [ecx+0x81C88];
        mov     dword ptr [eax+0x4D8], edx
        mov     eax, dword ptr [ebp+0x8]
        mov     ecx, dword ptr [ebp-0x14]
        mov     edx, dword ptr [eax+0x4DC]
        cmp     edx, dword ptr [ecx+0x38D28];   // ??
        jge L062
        mov     eax, dword ptr [ebp+0x8]
        mov     ecx, dword ptr [ebp-0x14]
        mov     edx, dword ptr [ecx+0x38D28];   // ??
        mov     dword ptr [eax+0x4DC], edx
L062:
        mov     eax, dword ptr [ebp+0x8]
        mov     ecx, dword ptr [ebp-0x14]
        mov     edx, dword ptr [eax+0x4DC]
        cmp     edx, dword ptr [ecx+0xA70C0];
        jge L071
        mov     eax, dword ptr [ebp+0x8]
        mov     ecx, dword ptr [ebp-0x14]
        mov     edx, dword ptr [ecx+0xA70C0];
        mov     dword ptr [eax+0x4DC], edx
L071:
        pop     edi
        pop     esi
        pop     ebx
        add     esp, 0xD8
        mov     esp, ebp
        pop     ebp
        ret     0x4

    }
}

NAKED VOID CSSaveData::SystemData2SaveData()
{
    INLINE_ASM
    {
        push    ebp
        mov     ebp, esp
        sub     esp, 0xF0
        push    ebx
        push    esi
        push    edi
        //push    ecx
        //lea     edi, dword ptr [ebp-0xF0]
        //mov     ecx, 0x3C
        //mov     eax, 0xCCCCCCCC
        //rep     stos dword ptr es:[edi]
        //pop     ecx
        mov     dword ptr [ebp-0x8], ecx
        cmp     dword ptr [ebp+0x8], 0x0
        jnz L016
        jmp L081
L016:
        mov     eax, dword ptr ds:[0xC29988];
        mov     dword ptr [ebp-0x14], eax
        mov     eax, dword ptr [ebp-0x14]
        movzx   ecx, byte ptr [eax+0x81C69];
        mov     dword ptr [ebp-0x20], ecx
        mov     eax, dword ptr [ebp-0x14]
        movzx   ecx, byte ptr [eax+0x81C68];
        mov     dword ptr [ebp-0x2C], ecx
        push    0x8
        mov     eax, dword ptr [ebp+0x8]
        add     eax, 0x4C4
        push    eax
        mov     ecx, dword ptr [ebp-0x14]
        add     ecx, 0x81C7C;
        push    ecx
        call    memcpy
        add     esp, 0xC
        push    0x4C4
        mov     eax, dword ptr [ebp+0x8]
        push    eax
        mov     ecx, dword ptr [ebp-0x14]
        add     ecx, 0x817AC;
        push    ecx
        call    memcpy
        add     esp, 0xC
        mov     eax, dword ptr [ebp-0x14]
        mov     cl, byte ptr [ebp-0x20]
        mov     byte ptr [eax+0x81C69], cl;
        mov     eax, dword ptr [ebp-0x14]
        mov     cl, byte ptr [ebp-0x20]
        mov     byte ptr [eax+0x81C34], cl;
        mov     eax, dword ptr [ebp-0x14]
        mov     cl, byte ptr [ebp-0x2C]
        mov     byte ptr [eax+0x81C68], cl;
        mov     eax, dword ptr [ebp-0x14]
        mov     cl, byte ptr [ebp-0x2C]
        mov     byte ptr [eax+0x81C33], cl;
        mov     eax, dword ptr [ebp-0x14]
        mov     ecx, dword ptr [ebp+0x8]
        mov     edx, dword ptr [ecx+0x4D0]
        mov     dword ptr [eax+0x81C84], edx;
        mov     eax, dword ptr [ebp-0x14]
        mov     ecx, dword ptr [ebp+0x8]
        mov     edx, dword ptr [ecx+0x4CC]
        mov     dword ptr [eax+0xA70C4], edx;
        mov     eax, dword ptr [ebp-0x14]
        mov     ecx, dword ptr [ebp+0x8]
        mov     edx, dword ptr [ecx+0x4D8]
        mov     dword ptr [eax+0x81C88], edx
        mov     eax, dword ptr [ebp-0x14]
        movzx   ecx, byte ptr [eax+0x81C69];
        push    ecx
        mov     ecx, dword ptr [ebp-0x14]
        add     ecx, 0x3A628;
        mov     eax, 0x67AA70;
        call    eax;
        mov     eax, dword ptr [ebp-0x14]
        movzx   ecx, byte ptr [eax+0x81C68];
        push    ecx
        mov     ecx, dword ptr [ebp-0x14]
        add     ecx, 0x3A578;
        mov     eax, 0x673257;
        call    eax;
        mov     eax, dword ptr [ebp-0x14]
        mov     ecx, dword ptr [ebp+0x8]
        mov     edx, dword ptr [ecx+0x4DC]
        mov     dword ptr [eax+0xA70C0], edx;
L081:
        pop     edi
        pop     esi
        pop     ebx
        add     esp, 0xF0
        mov     esp, ebp
        pop     ebp
        ret     0x4

    }
}