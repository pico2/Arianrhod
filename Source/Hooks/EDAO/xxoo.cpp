
NAKED VOID NakedArianrhodRefreshSy()
{
    INLINE_ASM
    {
        mov dword ptr ds:[eax+0x60],ecx;
        push 1;
        mov ecx,dword ptr ss:[ebp+0x8];
        push ecx;
        mov ecx,dword ptr ss:[ebp-0x8];
        add ecx,0x103148;
        mov eax, 0x00679E45;
        call eax;
        test eax,eax
            je lable2
            mov ecx,dword ptr ss:[ebp-0x44];
        mov dword ptr ds:[eax+0x60],ecx;
lable2: 
        push 0x9B1C4D;
        retn;
    }
}
