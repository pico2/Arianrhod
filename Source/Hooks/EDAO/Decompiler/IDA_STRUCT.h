#pragma pack(1)

typedef struct 
{
    BYTE    Dummy[0x7B8];

    PBYTE   Buffer;             // 0x07B8

    PVOID   Entry;              // 0x07BC
    PVOID   Entry1;             // 0x07C0
    PVOID   Entry2;             // 0x07C4
    PVOID   Entry3;             // 0x07C8
    PVOID   Entry4;             // 0x07CC
    PVOID   Entry5;             // 0x07D0

    PVOID   BufferBase;         // 0x07D4

} ED_AO_VM, *PED_AO_VM;
