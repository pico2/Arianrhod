#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")
#pragma comment(linker, "/EXPORT:__TrackMouseEvent=COMCTL32._TrackMouseEvent")

#include "MyLibrary.cpp"
#include "Vector.hpp"
#include "HandleTable.cpp"

OVERLOAD_CPP_NEW_WITH_HEAP(MemoryAllocator::GetGlobalHeap())

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

    MEMORY_FUNCTION_PATCH f[] =
    {
        INLINE_HOOK_CALL_RVA_NULL(0x5891C, NakedGetStringOffset),
    };

    Nt_PatchMemory(NULL, 0, f, countof(f), GetExeModuleHandle());

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
