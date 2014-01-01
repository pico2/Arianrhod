#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")
#pragma comment(linker, "/EXPORT:Direct3DCreate9=d3d9.Direct3DCreate9")

#include "th135.h"
#include "MyLibrary.cpp"
#include "mlns.h"

PTH135_PAKCN    g_Pak;
PWSTR           g_PakcnPath;

PTH135_PAKCN_ENTRY LookupFileEntry(ULONG Hash)
{
    PTH135_PAKCN_ENTRY Entry;

    Entry = BinarySearch(g_Pak->Entry, g_Pak->Entry + g_Pak->Count, Hash,
                [] (PTH135_PAKCN_ENTRY Entry, ULONG Hash, ULONG_PTR) -> LONG_PTR
                {
                    return Entry->Hash < Hash ? -1 : Entry->Hash > Hash ? 1 : 0;
                },
                0
            );

    return Entry;
}

BOOLEAN FASTCALL PakFileObject::OpenFileInPak(PVOID PakFile, PCSTR FileName)
{
    BOOL                Success;
    PTH135_PAKCN_ENTRY  Entry;

    INLINE_ASM mov PakFile, eax;

    LOOP_ONCE
    {
        INLINE_ASM
        {
            mov     eax, PakFile;
            mov     ecx, this;
            push    FileName;
            call    StubOpenFileInPak;
            movzx   eax, al;
            mov     Success, eax;
        }

        if (!Success)
            break;

        Entry = LookupFileEntry(this->FileInfo.Hash);
        if (Entry == NULL)
            break;

        //this->FileInfo.DecKeyIndex   = 0;
        //this->FileInfo.Hash          = Entry->Hash;
        this->FileInfo.Offset        = Entry->Offset;
        this->FileInfo.Size          = Entry->Size;

        CopyStruct(this->FileInfo.DecryptKey, Entry->Key, sizeof(Entry->Key));
        *(PULONG)&this->FileInfo.DecryptKeyPad = *(PULONG)&Entry->Key[0];

        //this->BufferSize     = 0;
        //this->Size           = 0;
        //this->CurrentOffset  = 0;

        ZwClose(this->FileHandle);
        NtFileDisk::Open(&this->FileHandle, g_PakcnPath);
        NtFileDisk::Seek(this->FileHandle, Entry->Offset, FILE_BEGIN);
    }

    return Success;
}

HFONT WINAPI ThCreateFontA(int cHeight, int cWidth, int cEscapement, int cOrientation, int cWeight, DWORD bItalic, DWORD bUnderline, DWORD bStrikeOut, DWORD iCharSet, DWORD iOutPrecision, DWORD iClipPrecision, DWORD iQuality, DWORD iPitchAndFamily, PCSTR pszFaceName)
{
    return CreateFontW(cHeight, cWidth, cEscapement, cOrientation, cWeight, bItalic, bUnderline, bStrikeOut, GB2312_CHARSET, iOutPrecision, iClipPrecision, iQuality, iPitchAndFamily, L"黑体");
}

BOOL UnInitialize(PVOID BaseAddress)
{
    FreeMemoryP(g_Pak);
    FreeMemoryP(g_PakcnPath);

    g_Pak = NULL;
    g_PakcnPath = NULL;

    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    ml::MlInitialize();

    LdrDisableThreadCalloutsForDll(BaseAddress);

    NTSTATUS Status;

    Status = STATUS_SUCCESS;

    LOOP_ONCE
    {
        NtFileDisk      Pak;
        PLDR_MODULE     ExeModule;
        PWSTR           PakcnPath;
        ULONG           Length;
        PTH135_PAKCN    PakBuffer;

        ExeModule = FindLdrModuleByHandle(NULL);

        Length = ExeModule->FullDllName.Length;
        PakcnPath = (PWSTR)AllocateMemoryP(Length + sizeof(PakcnPath));
        Length -= ExeModule->BaseDllName.Length;

        if (PakcnPath == NULL)
        {
            Status = STATUS_NO_MEMORY;
            break;
        }

        g_PakcnPath = PakcnPath;

        swprintf(PakcnPath, L"%.*s%s", Length / sizeof(WCHAR), ExeModule->FullDllName.Buffer, L"th135cn.pak");

        Status = Pak.Open(PakcnPath);
        FAIL_BREAK(Status);

        Status = Pak.Read(&Length, sizeof(PakBuffer->Count));
        FAIL_BREAK(Status);

        Length = (Length * sizeof(PakBuffer->Entry[0])) + sizeof(*PakBuffer) - sizeof(PakBuffer->Entry);

        PakBuffer = (PTH135_PAKCN)AllocateMemoryP(Length);
        if (PakBuffer == NULL)
        {
            Status = STATUS_NO_MEMORY;
            break;
        }

        g_Pak = PakBuffer;

        Pak.Rewind();

        Status = Pak.Read(PakBuffer, Length);
        FAIL_BREAK(Status);

        qsort(PakBuffer->Entry, PakBuffer->Count, sizeof(PakBuffer->Entry),
            [] (const void *entry1, const void *entry2) -> int
            {
                PTH135_PAKCN_ENTRY ent1, ent2;

                ent1 = (PTH135_PAKCN_ENTRY)entry1;
                ent2 = (PTH135_PAKCN_ENTRY)entry2;

                return ent1->Hash < ent2->Hash ? -1 : ent1->Hash > ent2->Hash ? 1 : 0;
            }
        );
    }

    if (NT_FAILED(Status))
    {
        UnInitialize(BaseAddress);
        return TRUE;
    }

    BaseAddress = Ldr::GetExeModuleHandle();

    MEMORY_PATCH p[] =
    {
        PATCH_MEMORY("东方心绮楼",      4, 0x1CB00),
        PATCH_MEMORY(ThCreateFontA,     4, IATLookupRoutineRVAByHashNoFix(BaseAddress, GDI32_CreateFontA)),
    };

    MEMORY_FUNCTION_PATCH f[] =
    {
        INLINE_HOOK_JUMP_RVA(0x174D0, METHOD_PTR(PakFileObject::OpenFileInPak),  PakFileObject::StubOpenFileInPak),
    };

    Nt_PatchMemory(p, countof(p), f, countof(f), BaseAddress);

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
