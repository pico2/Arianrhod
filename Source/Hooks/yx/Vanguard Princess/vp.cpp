#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")
#pragma comment(linker, "/EXPORT:DirectDrawCreate=DDRAW.DirectDrawCreate")

#include "MyLibrary.cpp"
#include "../../../Unpacker/SafePack/SafePackReader/SafePackReader.h"

ML_OVERLOAD_NEW


#undef  DebugPrint
#define DebugPrint(...)

#if 0

#undef  DebugPrint
#define DebugPrint(...) AllocConsole(), PrintConsoleW(__VA_ARGS__), PrintConsoleW(L"\n")

#endif


class VPPackReader : public SafePackReaderImpl<VPPackReader> {};

VPPackReader *Pack;


#define IMAGE_HAS_PALETTE   0x00000001

typedef struct
{
    PVOID Buffer;
    ULONG Width;
    ULONG Height;
    ULONG Flags;
    ULONG CompressedSize;

} VP_IMAGE_ENTRY, *PVP_IMAGE_ENTRY;

LONG CDECL sprintf_vp_kgt(PSTR Buffer, PCSTR Format, PCSTR CommandLine)
{
    ULONG_PTR       Length;
    PLDR_MODULE     ExeModule;

    ExeModule = FindLdrModuleByHandle(nullptr);

    UnicodeToAnsi(Buffer, 0x100, ExeModule->FullDllName.Buffer, (ExeModule->FullDllName.Length - ExeModule->BaseDllName.Length) / sizeof(WCHAR), &Length);

    CopyStruct(&Buffer[Length], "Vanguard Princess.KGT", sizeof("Vanguard Princess.KGT"));

    return 0;
}

NTSTATUS FASTCALL ReadPack(HANDLE FileHandle, ULONG_PTR NumberOfImages, PVP_IMAGE_ENTRY ImageEntry)
{
    PVOID                   ImageBuffer;
    ULONG_PTR               ImageSize, Index, Length;
    NTSTATUS                Status;
    UNICODE_STRING          DosPath;
    WCHAR                   Buffer[MAX_NTPATH];
    PWSTR                   FileName;
    PSAFE_PACK_READER_ENTRY Entry;
    UNPACKER_FILE_INFO      FileInfo;
    PIMAGE_BITMAP_HEADER    BmpHeader;

    Status = QueryDosPathFromHandle(&DosPath, FileHandle);
    FAIL_RETURN(Status);

    FileName = findnamew(DosPath.Buffer);
    *findextw(FileName) = 0;

    FileName = Buffer + swprintf(Buffer, L"%s\\%s.", FileName, FileName);
    Length = FileName - Buffer;

    RtlFreeUnicodeString(&DosPath);

    Index = ~0u;

    FOR_EACH(ImageEntry, ImageEntry, NumberOfImages)
    {
        ++Index;

        ImageSize = ImageEntry->CompressedSize;
        if (ImageSize == 0)
            ImageSize = ImageEntry->Width * ImageEntry->Height + (FLAG_ON(ImageEntry->Flags, IMAGE_HAS_PALETTE) ? 0x400 : 0);

        if (ImageSize == 0)
            continue;

        Entry = Pack->Lookup(Buffer, Length + swprintf(FileName, L"%d.bmp", Index));
        if (Entry == nullptr)
            continue;

        DebugPrint(L"%s", Entry->FileName);

        Status = Pack->GetFileData(&FileInfo, Entry);
        FAIL_CONTINUE(Status);

        BmpHeader = (PIMAGE_BITMAP_HEADER)FileInfo.BinaryData.Buffer;

        ImageSize = BmpHeader->Info.Width * BmpHeader->Info.Height + 0x400;

        ImageBuffer = GlobalAlloc(GMEM_FIXED, ImageSize);

        if (ImageBuffer != nullptr)
        {
            GlobalFree(ImageEntry->Buffer);

            ImageEntry->Buffer = ImageBuffer;
            ImageEntry->CompressedSize = 0;
            SET_FLAG(ImageEntry->Flags, IMAGE_HAS_PALETTE);

            CopyMemory(ImageBuffer, BmpHeader + 1, 0x400);

            PBYTE Source, Destination;
            LONG  Stride, Pitch;

            Pitch = BmpHeader->Info.Width;

            Source      = (PBYTE)PtrAdd(BmpHeader, BmpHeader->RawOffset);
            Destination = (PBYTE)ImageBuffer + 0x400;
            Stride      = (Pitch + 3) & ~3;

            Source += Stride * BmpHeader->Info.Height;

            for (LONG_PTR Height = BmpHeader->Info.Height; Height; --Height)
            {
                Source -= Stride;
                CopyMemory(Destination, Source, Pitch);
                Destination += Pitch;
            }

            //if (PtrOffset(Destination, ImageBuffer) > ImageSize) _asm int 3;
        }

        Pack->FreeFileData(&FileInfo);
    }

    return 0;
}

NAKED VOID NakedReadPack()
{
    INLINE_ASM
    {
        mov     edi, [esp + 20h];
        mov     edx, [esp + 2Ch];
        push    edi;
        mov     ecx, ebx;
        call    ReadPack

        mov     edi, dword ptr ds:[41C088h];
        ret;
    }
}

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    ml::MlInitialize();

    MEMORY_FUNCTION_PATCH f[] =
    {
        INLINE_HOOK_CALL_RVA_NULL(0x037ED, NakedReadPack),
        INLINE_HOOK_CALL_RVA_NULL(0x09AE0, sprintf_vp_kgt),
    };

    SetExeDirectoryAsCurrent();

    Pack = new VPPackReader();
    Pack->Open(L"vp.pack");

    Nt_PatchMemory(nullptr, 0, f, countof(f), GetExeModuleHandle());

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
