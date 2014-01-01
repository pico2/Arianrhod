#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")
#pragma comment(linker, "/EXPORT:__TrackMouseEvent=COMCTL32._TrackMouseEvent")

#include "MyLibrary.cpp"
#include "Vector.hpp"
#include "HandleTable.cpp"

ML_OVERLOAD_NEW

typedef struct
{
    PCSTR   ScriptName;
    PVOID   Dummy[7];
    PULONG  OpBuffer;

} SCRIPT_OBJECT, *PSCRIPT_OBJECT;

typedef struct TEXT_NODE
{
    ULONG   Offset;
    ULONG   Length;
    CHAR    Text[1];

    TEXT_NODE* Next()
    {
        return PtrAdd(this, ROUND_UP(this->Length, 4) + FIELD_OFFSET(TEXT_NODE, Text));
    }

} *PTEXT_NODE;

typedef ml::GrowableArray<PTEXT_NODE> TextNodeList;

MlHandleTable *g_TextTable;
PVOID g_TextBuffer;

ULONG FASTCALL GetStringOffset(PSCRIPT_OBJECT Script, ULONG OpIndex, PCSTR StringBuffer)
{
    ULONG                   Offset, Hash;
    PTEXT_NODE*             TextNode;
    TextNodeList*           NodeList;
    PML_HANDLE_TABLE_ENTRY  NodeListHandle;

    Offset = Script->OpBuffer[OpIndex];
    if (Script->ScriptName == NULL)
        return Offset;

    Hash = HashAPILower(Script->ScriptName);
    //AllocConsole();PrintConsoleW(L"%08X, %S\n", Hash, Script->ScriptName);

    LOOP_ONCE
    {
        NodeListHandle = g_TextTable->Lookup(Hash);
        if (NodeListHandle == NULL)
            break;

        NodeList = (TextNodeList *)NodeListHandle->Handle;
        if (NodeList == NULL)
            break;

        TextNode = BinarySearch(NodeList->GetData(), NodeList->GetData() + NodeList->GetSize(), Offset,
                        [] (PTEXT_NODE* ValuePtr, ULONG Value, ULONG Context)
                        {
                            return (*ValuePtr)->Offset == Value ? 0 : (*ValuePtr)->Offset < Value ? -1 : 1;
                        },
                        0
                    );

        if (TextNode == NULL)
            break;

        Offset = PtrOffset((*TextNode)->Text, StringBuffer);
    }

    return Offset;
}

NAKED ULONG NakedGetStringOffset()
{
    INLINE_ASM
    {
        mov     ecx, ebx;
        mov     edx, esi;
        push    dword ptr [ebp-40h];
        call    GetStringOffset;
        ret;
    }
}

NTSTATUS InitTextTable()
{
    PVOID           Buffer;
    PBYTE           Begin, End;
    ULONG_PTR       Size;
    NTSTATUS        Status;
    NtFileDisk      TextFile;
    MlHandleTable*  TextTable;

    SetExeDirectoryAsCurrent();

    TextTable = new MlHandleTable;
    if (TextTable == NULL)
        return STATUS_NO_MEMORY;

    g_TextTable = TextTable;

    if (TextTable->Create() == NULL)
        return STATUS_NO_MEMORY;

    Status = TextFile.Open(L"lang.cs.bin");
    FAIL_RETURN(Status);

    Size = TextFile.GetSize32();
    Buffer = AllocateMemoryP(Size);
    if (Buffer == NULL)
        return STATUS_NO_MEMORY;

    g_TextBuffer = Buffer;

    Status = TextFile.Read(Buffer, Size);
    FAIL_RETURN(Status);

    Begin   = (PBYTE)Buffer;
    End     = Begin + Size;

    while (Begin < End)
    {
        TextNodeList*           NodeList;
        PTEXT_NODE              TextNode;
        PML_HANDLE_TABLE_ENTRY  Entry;

        Entry = TextTable->Insert(*(PULONG)Begin);
        if (Entry == NULL)
            return STATUS_NO_MEMORY;

        NodeList = new TextNodeList;
        if (NodeList == NULL)
            return STATUS_NO_MEMORY;

        Entry->Handle = NodeList;

        Begin += sizeof(ULONG);
        TextNode = (PTEXT_NODE)(Begin + sizeof(ULONG));

        for (ULONG_PTR Count = *(PULONG)Begin; Count; TextNode = TextNode->Next(), --Count)
        {
            NodeList->Add(TextNode);
        }

        Begin = (PBYTE)TextNode;
    }

    return STATUS_SUCCESS;
}

TYPE_OF(CreateFontW)* StubCreateFontW;

HFONT NTAPI GlobalCreateFontW(_In_ int cHeight, _In_ int cWidth, _In_ int cEscapement, _In_ int cOrientation, _In_ int cWeight, _In_ DWORD bItalic, _In_ DWORD bUnderline, _In_ DWORD bStrikeOut, _In_ DWORD iCharSet, _In_ DWORD iOutPrecision, _In_ DWORD iClipPrecision, _In_ DWORD iQuality, _In_ DWORD iPitchAndFamily, _In_opt_ LPCWSTR pszFaceName)
{
    int newh;

    newh = cHeight;

    AllocConsole();
    PrintConsoleW(L"2: %03d -> %03d\n", cHeight, newh);

    newh = 12;

    return StubCreateFontW(newh, cWidth, cEscapement, cOrientation, cWeight, bItalic, bUnderline, bStrikeOut, iCharSet, iOutPrecision, iClipPrecision, iQuality, iPitchAndFamily, L"ºÚÌå");
}

HFONT NTAPI gCreateFontW(_In_ int cHeight, _In_ int cWidth, _In_ int cEscapement, _In_ int cOrientation, _In_ int cWeight, _In_ DWORD bItalic, _In_ DWORD bUnderline, _In_ DWORD bStrikeOut, _In_ DWORD iCharSet, _In_ DWORD iOutPrecision, _In_ DWORD iClipPrecision, _In_ DWORD iQuality, _In_ DWORD iPitchAndFamily, _In_opt_ LPCWSTR pszFaceName)
{
    int newh;

    newh = cHeight;

    // if (newh > 70)      newh /= 6;
    // if (newh > 50) newh /= 4;
    //if (newh > 30) newh /= 3;
    //if (newh > 30) newh = newh * 2 / 5;
    //else if (newh > 20) newh = newh * 2 / 3;

    if (newh > 30) newh -= 10;
    else if (newh > 20) newh -= 5;

    //AllocConsole();PrintConsoleW(L"%03d -> %03d\n", cHeight, newh);

    return CreateFontW(
                newh,
                cWidth,
                cEscapement,
                cOrientation,
                cWeight,
                bItalic,
                bUnderline,
                bStrikeOut,
                iCharSet,
                iOutPrecision,
                iClipPrecision,
                iQuality,
                iPitchAndFamily,
                pszFaceName
            );
}

NAKED ULONG FindCachedChar()
{
    INLINE_ASM
    {
        lea     esi, dword ptr [edi+eax*4+54h];
        cmp     eax, 80h;
        jb      ANSI_CHAR;
        or      dword ptr [esi], -1;
        xor     eax, eax;

ANSI_CHAR:

        ret;
    }
}

int (CDECL *stub_zlib_uncompress)(PVOID Output, PULONG OutputSize, PVOID Input, ULONG InputSize);

int CDECL zlib_uncompress(PVOID Output, PULONG OutputSize, PVOID Input, ULONG InputSize)
{
    int     ret;
    ULONG   StartIndex;
    PVOID   Start, StackFrame, Ebp;

    ret = stub_zlib_uncompress(Output, OutputSize, Input, InputSize);
    if (ret != 0)
        return ret;

    if (zlib_uncompress == NULL)
        StackFrame = AllocStack(16);

    StackFrame = PtrSub(_AddressOfReturnAddress(), sizeof(PVOID));
    Ebp = *(PVOID *)StackFrame;

    StartIndex = *(PULONG)PtrSub(Ebp, 0x14);

    if (StartIndex >= 0x80)
    {
        FillMemory(Output, *OutputSize, 0xFF);
    }
    else
    {
        Start = (PULONG)Output - StartIndex + 0x80;
        FillMemory(Start, *OutputSize - PtrOffset(Start, Output), 0xFF);
    }

    return ret;
}

BOOL UnInitialize(PVOID BaseAddress)
{
/*
    FreeMemoryP(g_TextBuffer);

    if (g_TextTable != NULL)
    {
        g_TextTable->Destroy(
            HandleTableDestroyM(Entry, Count, Context)
            {
                for (; Count; ++Entry, --Count)
                    delete (TextNodeList *)Entry->Handle;

                return 0;
            }
        );

        SafeDeleteT(g_TextTable);
    }
*/
    ml::MlUnInitialize();

    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    ml::MlInitialize();

    LdrDisableThreadCalloutsForDll(BaseAddress);

    if (NT_FAILED(InitTextTable()))
        return TRUE;

    MEMORY_PATCH p[] =
    {
        PATCH_MEMORY(gCreateFontW, 4, 0x166044),
        //PATCH_MEMORY(0x75FF0E, 4, 0x78744),
    };

    MEMORY_FUNCTION_PATCH f[] =
    {
        INLINE_HOOK_CALL_RVA_NULL(0x5891C, NakedGetStringOffset),
        // INLINE_HOOK_CALL_RVA_NULL(0x7873F, FindCachedChar),
        INLINE_HOOK_CALL_RVA(0x7790D, zlib_uncompress, stub_zlib_uncompress),

        //INLINE_HOOK_JUMP(CreateFontW, GlobalCreateFontW, StubCreateFontW),
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
