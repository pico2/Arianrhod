#ifndef _SAFEPACKER_H_5447b095_7f6d_4794_a657_bd31b4450648
#define _SAFEPACKER_H_5447b095_7f6d_4794_a657_bd31b4450648

#include "UnpackerBase.h"
#include "aes.h"

#if !defined(SAFE_PACK_MAGIC)
    #define SAFE_PACK_MAGIC         TAG4('ARIA')
#endif

#if !defined(NRV2E_MAGIC)
    #define NRV2E_MAGIC             TAG4('NRV2')
#endif

#if !defined(LZNT1_MAGIC)
    #define LZNT1_MAGIC             TAG4('LZNT')
#endif

#if !defined(LZMA_MAGIC)
    #define LZMA_MAGIC              TAG4('LZMA')
#endif

#define DebugInfo(...) PrintConsole(__VA_ARGS__), PrintConsole(L"\n")

#define DEFAULT_COMPRESS_DATA   1
#define FILE_NAME_HASH_SIZE         (sizeof(ULONG) * 8)
#define FILE_NAME_SHORT_HASH_SIZE   (sizeof(ULONG) * 4)

#pragma pack(push, 1)

typedef struct
{
    PVOID           Buffer;
    ULONG           Flags;
    LARGE_INTEGER   Size;
    LARGE_INTEGER   Offset;

    VOID Initialize(PVOID Buffer = nullptr, ULONG Flags = 0, LONG64 Size = 0, LONG64 Offset = 0)
    {
        this->Buffer            = Buffer;
        this->Flags             = Flags;
        this->Size.QuadPart     = Size;
        this->Offset.QuadPart   = Offset;
    }

} SAFE_PACK_BUFFER, *PSAFE_PACK_BUFFER;

typedef struct
{
    ULONG           Magic;
    ULONG           HeaderSize;
    ULONG           Flags;
    ULONG           Reserve;
    LARGE_INTEGER   EntryOffset;
    LARGE_INTEGER   EntrySize;
    LARGE_INTEGER   LookupTableSize;
    LARGE_INTEGER   NumberOfFiles;

} SAFE_PACK_HEADER, *PSAFE_PACK_HEADER;

typedef struct
{
    ULONG           EntrySize;
    ULONG           Flags;
    LARGE_INTEGER   Offset;
    LARGE_INTEGER   FileSize;
    ULONG           Attributes;
    //LARGE_INTEGER   CreationTime;
    //LARGE_INTEGER   LastAccessTime;
    //LARGE_INTEGER   LastWriteTime;
    //ULONG           FileNameHash[4];
    UNICODE_STRING  FileName;
    WCHAR           Buffer[1];

} SAFE_PACK_ENTRY, *PSAFE_PACK_ENTRY;

typedef enum
{
    NoCompress,

    CompressMethodLZNT1     = 1,
    CompressMethodLZMA      = 2,
    CompressMethodNRV2E     = 3,

    CompressMethodUser      = 0x80000000,

} SafePackCompressMethodClass;

typedef struct
{
    ULONG           Magic;
    ULONG           Flags;
    ULONG           CompressMethod;
    LARGE_INTEGER   CompressedSize;
    LARGE_INTEGER   OriginalSize;

} SAFE_PACK_COMPRESSED_HEADER, *PSAFE_PACK_COMPRESSED_HEADER;

struct SAFE_PACK_ENTRY2 : public UNPACKER_FILE_ENTRY_BASE
{
    ULONG           UnicodeHash[FILE_NAME_HASH_SIZE / sizeof(ULONG)];
    LARGE_INTEGER   CreationTime;
    LARGE_INTEGER   LastAccessTime;
    LARGE_INTEGER   LastWriteTime;
};

typedef SAFE_PACK_ENTRY2 *PSAFE_PACK_ENTRY2;

#pragma pack(pop)

class SafePackerBase
{
public:
    static VOID EncryptHeader(PVOID Buffer, ULONG Size)
    {
        ULONG               Hash[8];
        aes_encrypt_ctx     AesContext;
        PIMAGE_DOS_HEADER   DosHeader;
        PIMAGE_NT_HEADERS   NtHeaders;

        DosHeader = (PIMAGE_DOS_HEADER)&__ImageBase;
        NtHeaders = (PIMAGE_NT_HEADERS)((ULONG_PTR)DosHeader + DosHeader->e_lfanew);
        sha256(IMAGE_FIRST_SECTION(NtHeaders)->Name, RTL_FIELD_SIZE(IMAGE_SECTION_HEADER, Name), Hash);
        aes_encrypt_key128(Hash, &AesContext);
        Encrypt(&AesContext, Buffer, Size, &Hash[4]);
    }

    static VOID DecryptHeader(PVOID Buffer, ULONG Size)
    {
        ULONG               Hash[8];
        aes_encrypt_ctx     AesContext;
        PIMAGE_DOS_HEADER   DosHeader;
        PIMAGE_NT_HEADERS   NtHeaders;

        DosHeader = (PIMAGE_DOS_HEADER)&__ImageBase;
        NtHeaders = (PIMAGE_NT_HEADERS)((ULONG_PTR)DosHeader + DosHeader->e_lfanew);
        sha256(IMAGE_FIRST_SECTION(NtHeaders)->Name, RTL_FIELD_SIZE(IMAGE_SECTION_HEADER, Name), Hash);
        aes_encrypt_key128(Hash, &AesContext);
        Decrypt(&AesContext, Buffer, Size, &Hash[4]);
    }

    static VOID Encrypt(aes_encrypt_ctx *AesContext, PVOID Buffer, ULONG Size, PULONG Key)
    {
        ULONG   Mod16Buffer[4], KeyLocal[4];
        PULONG  Data;

        Data = (PULONG)Buffer;
        CopyStruct(KeyLocal, Key, sizeof(KeyLocal));
        for (ULONG SizeMod16 = Size / 16; SizeMod16; --SizeMod16)
        {
            aes_encrypt(KeyLocal, KeyLocal, AesContext);

            Data[0] ^= KeyLocal[0];
            Data[1] ^= KeyLocal[1];
            Data[2] ^= KeyLocal[2];
            Data[3] ^= KeyLocal[3];

            CopyStruct(KeyLocal, Data, sizeof(KeyLocal));

            Data += 4;
        }

        Size %= 16;
        if (Size == 0)
            return;

        CopyMemory(Mod16Buffer, Data, Size);
        aes_encrypt(KeyLocal, KeyLocal, AesContext);

        Mod16Buffer[0] ^= KeyLocal[0];
        Mod16Buffer[1] ^= KeyLocal[1];
        Mod16Buffer[2] ^= KeyLocal[2];
        Mod16Buffer[3] ^= KeyLocal[3];

        CopyMemory(Data, Mod16Buffer, Size);
    }

    static VOID Decrypt(aes_encrypt_ctx *AesContext, PVOID Buffer, ULONG Size, PULONG Key)
    {
        ULONG   Mod16Buffer[4], KeyLocal[4];
        PULONG  Data;

        Data = (PULONG)Buffer;
        CopyStruct(KeyLocal, Key, sizeof(KeyLocal));
        for (ULONG SizeMod16 = Size / 16; SizeMod16; --SizeMod16)
        {
            aes_encrypt(KeyLocal, KeyLocal, AesContext);

            Swap(Data[0], KeyLocal[0]);
            Swap(Data[1], KeyLocal[1]);
            Swap(Data[2], KeyLocal[2]);
            Swap(Data[3], KeyLocal[3]);

            Data[0] ^= KeyLocal[0];
            Data[1] ^= KeyLocal[1];
            Data[2] ^= KeyLocal[2];
            Data[3] ^= KeyLocal[3];

            Data += 4;
        }

        Size %= 16;
        if (Size == 0)
            return;

        CopyMemory(Mod16Buffer, Data, Size);
        aes_encrypt(KeyLocal, KeyLocal, AesContext);

        Mod16Buffer[0] ^= KeyLocal[0];
        Mod16Buffer[1] ^= KeyLocal[1];
        Mod16Buffer[2] ^= KeyLocal[2];
        Mod16Buffer[3] ^= KeyLocal[3];

        CopyMemory(Data, Mod16Buffer, Size);
    }

    UPK_STATUS
    PreCompressData(
        PSAFE_PACK_ENTRY2 FileInfo,
        PSAFE_PACK_BUFFER Buffer
    )
    {
        return STATUS_NOT_IMPLEMENTED;
    }

    UPK_STATUS
    CompressData(
        PSAFE_PACK_ENTRY2 FileInfo,
        PSAFE_PACK_BUFFER SourceBuffer,
        PSAFE_PACK_BUFFER DestinationBuffer,
        ULONG_PTR         CompressionFormatAndEngine = COMPRESSION_FORMAT_LZNT1 | COMPRESSION_ENGINE_STANDARD
    )
    {

#if !DEFAULT_COMPRESS_DATA

        UNREFERENCED_PARAMETER(FileInfo);
        return STATUS_COMPRESSION_DISABLED;

#else

        NTSTATUS                        Status;
        ULONG                           CompressBufferWorkSpaceSize;
        ULONG                           CompressFragmentWorkSpaceSize;
        PVOID                           WorkSpace;
        PSAFE_PACK_COMPRESSED_HEADER    Header;

        if (SourceBuffer->Size.HighPart != 0)
            return STATUS_COMPRESSION_DISABLED;

        if (DestinationBuffer->Size.QuadPart < SourceBuffer->Size.QuadPart * 2)
        {
            DestinationBuffer->Size.QuadPart = SourceBuffer->Size.QuadPart * 2;
            return STATUS_BUFFER_TOO_SMALL;
        }

        Status = RtlGetCompressionWorkSpaceSize(
                    CompressionFormatAndEngine,
                    &CompressBufferWorkSpaceSize,
                    &CompressFragmentWorkSpaceSize
                );

        if (NT_FAILED(Status))
        {
            return STATUS_COMPRESSION_DISABLED;
        }

        WorkSpace = AllocStack(CompressBufferWorkSpaceSize + CompressFragmentWorkSpaceSize);

        Header = (PSAFE_PACK_COMPRESSED_HEADER)DestinationBuffer->Buffer;

        Status = RtlCompressBuffer(
                    CompressionFormatAndEngine,
                    SourceBuffer->Buffer,
                    SourceBuffer->Size.LowPart,
                    Header + 1,
                    DestinationBuffer->Size.LowPart,
                    CompressFragmentWorkSpaceSize,
                    &DestinationBuffer->Size.LowPart,
                    WorkSpace
                );

        if (NT_FAILED(Status))
        {
            return STATUS_COMPRESSION_DISABLED;
        }

        DestinationBuffer->Size.HighPart = 0;

        if (DestinationBuffer->Size.LowPart + sizeof(*Header) >= SourceBuffer->Size.LowPart)
        {
            return STATUS_COMPRESSION_DISABLED;
        }

        Header->Magic                     = LZNT1_MAGIC;
        Header->Flags                     = 0;
        Header->CompressMethod            = CompressMethodLZNT1;
        Header->OriginalSize.QuadPart     = SourceBuffer->Size.QuadPart;
        Header->CompressedSize.QuadPart   = DestinationBuffer->Size.QuadPart;

        DestinationBuffer->Size.QuadPart += sizeof(*Header);

        return STATUS_SUCCESS;

#endif

    }

    UPK_STATUS
    PostCompressData(
        PSAFE_PACK_ENTRY2 FileInfo,
        PSAFE_PACK_BUFFER Buffer
    )
    {

        return STATUS_NOT_IMPLEMENTED;
/*
        aes_encrypt_ctx AesContext;

        aes_encrypt_key128(&FileInfo->UnicodeHash[4], &AesContext);
        Encrypt(&AesContext, Buffer->Buffer, Buffer->Size.LowPart, FileInfo->UnicodeHash);

        return STATUS_SUCCESS;
*/
    }

    UPK_STATUS
    FinalizeEntrySize(
        PSAFE_PACK_ENTRY Entry
    )
    {
        return STATUS_NOT_IMPLEMENTED;
    }

    UPK_STATUS
    GetEntryLookupData(
        PTRIE_BYTES_ENTRY BytesEntry,
        PSAFE_PACK_ENTRY2 FileInfo
    )
    {
        ml::String FileNameLower = FileInfo->FileName.ToLower();

        BytesEntry->SizeInBytes = FileNameLower.GetCount() * sizeof(WCHAR);

        BytesEntry->Data = AllocateMemoryP(BytesEntry->SizeInBytes);
        if (BytesEntry->Data == nullptr)
            return STATUS_NO_MEMORY;

        CopyMemory(BytesEntry->Data, FileNameLower.GetBuffer(), BytesEntry->SizeInBytes);

        return STATUS_SUCCESS;
    }

    UPK_STATUS
    FreeEntryLookupData(
        PTRIE_BYTES_ENTRY BytesEntry
    )
    {
        FreeMemoryP(BytesEntry->Data);
        return STATUS_SUCCESS;
    }

    UPK_STATUS
    PreCompressEntry(
        PSAFE_PACK_HEADER Header,
        PSAFE_PACK_BUFFER SourceBuffer
    )
    {
        UNREFERENCED_PARAMETER(Header);
        UNREFERENCED_PARAMETER(SourceBuffer);

        return STATUS_NOT_IMPLEMENTED;
    }

    UPK_STATUS
    CompressEntry(
        PSAFE_PACK_HEADER Header,
        PSAFE_PACK_BUFFER SourceBuffer,
        PSAFE_PACK_BUFFER DestinationBuffer
    )
    {
        UNREFERENCED_PARAMETER(Header);
        return CompressData(nullptr, SourceBuffer, DestinationBuffer);
    }

    UPK_STATUS
    PostCompressEntry(
        PSAFE_PACK_HEADER Header,
        PSAFE_PACK_BUFFER SourceBuffer
    )
    {
        UNREFERENCED_PARAMETER(Header);
        return STATUS_NOT_IMPLEMENTED;

        //EncryptHeader(SourceBuffer->Buffer, SourceBuffer->Size.LowPart);
        //return STATUS_SUCCESS;
    }

    UPK_STATUS
    EncryptPackHeader(
        PSAFE_PACK_HEADER   Header,
        ULONG_PTR           HeaderSize
    )
    {
        return STATUS_NOT_IMPLEMENTED;
/*
        SET_FLAG(Header->Flags, UNPACKER_ENTRY_ENCRYPTED);
        EncryptHeader(Header, Header->HeaderSize);

        return STATUS_SUCCESS;
*/
    }

    ULONG_PTR GetHeaderMagic()
    {
        return SAFE_PACK_MAGIC;
    }

protected:
    static LARGE_INTEGER FileTimeToLargeInteger(FILETIME FileTime)
    {
        LARGE_INTEGER Large;

        Large.LowPart   = FileTime.dwLowDateTime;
        Large.HighPart  = FileTime.dwHighDateTime;

        return Large;
    }

    static
    LONG
    STDCALL
    EnumDirCallback(
        PSAFE_PACK_ENTRY2   Entry,
        PWIN32_FIND_DATAW   FindData,
        ULONG_PTR           Context
    )
    {
        ULONG   Length;

        Length = StrLengthW(FindData->cFileName + Context);

        Entry->Attributes       = FindData->dwFileAttributes;
        Entry->CreationTime     = FileTimeToLargeInteger(FindData->ftCreationTime);
        Entry->LastAccessTime   = FileTimeToLargeInteger(FindData->ftLastAccessTime);
        Entry->LastWriteTime    = FileTimeToLargeInteger(FindData->ftLastWriteTime);
        Entry->Size.LowPart     = FindData->nFileSizeLow;
        Entry->Size.HighPart    = FindData->nFileSizeHigh;
        Entry->Flags            = 0;

        HashFileName(Entry->UnicodeHash, FindData->cFileName + Context, Length);

        Entry->SetFileName(FindData->cFileName + Context);

        return 1;
    }
/*
    static INT CDECL SortEntry(PSAFE_PACK_ENTRY Entry1, PSAFE_PACK_ENTRY Entry2)
    {
        ULONG  Count;
        PULONG Hash1, Hash2;

        Hash1 = Entry1->FileNameHash;
        Hash2 = Entry2->FileNameHash;
        Count = countof(Entry1->FileNameHash);

        do
        {
            if (*Hash1 < *Hash2)
                return -1;
            else if (*Hash1 > *Hash2)
                return 1;

            ++Hash1;
            ++Hash2;

        } while (--Count);

        return 0;
    }
*/
public:

    static VOID HashFileNameShort(PULONG Hash, PCWSTR FileName, ULONG_PTR Length)
    {
        ULONG LongHash[FILE_NAME_HASH_SIZE / sizeof(ULONG)];

        HashFileName(LongHash, FileName, Length);

        Hash[0]  = LongHash[0] ^ LongHash[4];
        Hash[1]  = LongHash[1] ^ LongHash[5];
        Hash[2]  = LongHash[2] ^ LongHash[6];
        Hash[3]  = LongHash[3] ^ LongHash[7];
    }

    static VOID HashFileName(PVOID Hash, PCWSTR FileName, ULONG_PTR Length)
    {
        PWSTR Buffer, Text;

        Length *= sizeof(WCHAR);

        Buffer = (PWSTR)AllocStack(Length);
        CopyMemory(Buffer, FileName, Length);

        FOR_EACH(Text, Buffer, Length / sizeof(WCHAR))
        {
            switch (*Text)
            {
                case '/':
                    *Text = '\\';
                    break;

                default:
                    *Text = CHAR_UPPER(*Text);
                    break;
            }
        }

        sha256(Buffer, Length, Hash);
    }
};

template<class BaseType>
class SafePackerImpl : public UnpackerImpl<BaseType>, public SafePackerBase
{
public:
    UPK_STATUS
    Pack(
        PCWSTR          InputPath,
        PCWSTR          OutputFile   = nullptr,
        PLARGE_INTEGER  PackedFiles  = nullptr,
        ULONG           Flags        = 0
    );
};

template<class BaseType>
UPK_STATUS
SafePackerImpl<BaseType>::
Pack(
    PCWSTR          InputPath,
    PCWSTR          OutputFile  /* = NULL */,
    PLARGE_INTEGER  PackedFiles /* = NULL */,
    ULONG           Flags       /* = 0 */
)
{
    UPK_STATUS          Status;
    WCHAR               PackPath[MAX_NTPATH], *FileName;
    ULONG_PTR           Length, PackedFileNumber;
    ULONG_PTR           BufferSize, CompressedBufferSize, FileSize;
    ULONG_PTR           EntrySize, WriteSize;
    PVOID               FileBuffer, Buffer, Compressed, WriteBuffer;
    SAFE_PACK_BUFFER    SourceBuffer, DestinationBuffer;
    SAFE_PACK_HEADER    Header;
    PSAFE_PACK_ENTRY    EntryBase, Entry;
    PSAFE_PACK_ENTRY2   FileList, FileListBase;
    LARGE_INTEGER       FileNumber, DataOffset;
    BaseType           *This;

    if (Flags != 0)
        return STATUS_INVALID_PARAMETER;

    This                = GetTopClass();
    Buffer              = nullptr;
    Compressed          = nullptr;
    PackedFileNumber    = 0;

    if (PackedFiles != nullptr)
        PackedFiles->QuadPart = 0;

    Length = StrLengthW(InputPath);

    DebugInfo(L"");

    Status = STATUS_UNSUCCESSFUL;
    if (
        !EnumDirectoryFiles(
            (PVOID *)&FileListBase,
            L"*.*",
            sizeof(*FileListBase),
            InputPath,
            &FileNumber,
            (EnumDirectoryFilesCallBackRoutine)EnumDirCallback,
            Length + (InputPath[Length - 1] != '\\'),
            EDF_SUBDIR | EDF_BEFORE)
       )
    {
        DebugInfo(L"Enum failed");
        return Status;
    }

    DebugInfo(L"FileNumber %I64d", FileNumber.QuadPart);

    NtFileDisk          pack, file;
    Trie                EntryLookupTable;
    TRIE_BYTES_ENTRY    BytesEntry;

    EntrySize = (ULONG_PTR)FileNumber.QuadPart;
    EntrySize = EntrySize * (sizeof(*Entry) - sizeof(Entry->Buffer) + MAX_NTPATH * sizeof(WCHAR));
    EntryBase = (PSAFE_PACK_ENTRY)AllocateMemory(EntrySize, HEAP_ZERO_MEMORY);
    if (EntryBase == nullptr)
    {
        DebugInfo(L"AllocateMemory(%d) failed", EntrySize);
        Status = STATUS_NO_MEMORY;
        goto CLEAN_UP;
    }

    Status = EntryLookupTable.InitializeRootNode();
    if (NT_FAILED(Status))
    {
        DebugInfo(L"InitializeRootNode failed");
        goto CLEAN_UP;
    }

    if (OutputFile == nullptr)
    {
        CopyMemory(PackPath, InputPath, Length * sizeof(WCHAR));
        Length -= PackPath[Length - 1] == '\\';
        *(PULONG64)&PackPath[Length + 0] = TAG4W('.pac');
        *(PULONG)&PackPath[Length + 4] = 'k';
    }
    else
    {
        Length = StrLengthW(OutputFile);
        CopyMemory(PackPath, OutputFile, (Length + 1) * sizeof(WCHAR));
        do
        {
            if (PackPath[Length] == '\\' || PackPath[Length] == '/')
                break;
        } while (--Length);
    }

    Status = pack.Create(PackPath);
    if (!NT_SUCCESS(Status))
    {
        DebugInfo(L"create %s failed: %08X", PackPath, Status);
        goto CLEAN_UP;
    }

    Header.Magic                = This->GetHeaderMagic();
    Header.HeaderSize           = sizeof(Header);
    Header.Flags                = 0;
    Header.EntryOffset.QuadPart = 0;
    Header.EntrySize.QuadPart   = 0;
    DataOffset.QuadPart         = Header.HeaderSize;

    Status = pack.Seek(DataOffset, FILE_BEGIN);
    if (!NT_SUCCESS(Status))
    {
        DebugInfo(L"Seek %s failed: %08X", PackPath, Status);
        goto CLEAN_UP;
    }

    FileName = PackPath + Length;
    if (Length != 0)
        *FileName++ = '\\';

    BufferSize              = 0;
    CompressedBufferSize    = 0;
    Entry                   = EntryBase;
    FileList                = FileListBase;

    for (LARGE_INTEGER Count = FileNumber; Count.QuadPart; ++FileList, --Count.QuadPart)
    {
        DebugInfo(FileList->FileName);

        if (PtrOffset(Entry, EntryBase) > EntrySize)
        {
            ULONG_PTR Offset = PtrOffset(Entry, EntryBase);
            EntrySize = Offset * 3 / 2;
            EntryBase = (PSAFE_PACK_ENTRY)ReAllocateMemory(EntryBase, EntrySize);
            if (EntryBase == nullptr)
            {
                Status = STATUS_NO_MEMORY;
                goto CLEAN_UP;
            }

            Entry = PtrAdd(EntryBase, Offset);
        }

        Length = FileList->GetFileNameLength() * sizeof(WCHAR);

        Entry->Flags            = Flags;
        //Entry->CreationTime     = FileList->CreationTime;
        //Entry->LastAccessTime   = FileList->LastAccessTime;
        //Entry->LastWriteTime    = FileList->LastWriteTime;
        //Entry->FileNameHash[0]  = FileList->UnicodeHash[0] ^ FileList->UnicodeHash[4];
        //Entry->FileNameHash[1]  = FileList->UnicodeHash[1] ^ FileList->UnicodeHash[5];
        //Entry->FileNameHash[2]  = FileList->UnicodeHash[2] ^ FileList->UnicodeHash[6];
        //Entry->FileNameHash[3]  = FileList->UnicodeHash[3] ^ FileList->UnicodeHash[7];
        Entry->Attributes       = FileList->Attributes;

        if (FLAG_ON(Entry->Attributes, FILE_ATTRIBUTE_DIRECTORY))
        {
            Entry->Offset.QuadPart = DataOffset.QuadPart + GetRandom32Range(0x100, 0x200);
            Entry->FileSize.QuadPart = DataOffset.QuadPart + GetRandom32Range(0x200, 0x300);
            goto PACK_NEXT_FILE;
            // continue;
        }

        CopyMemory(FileName, FileList->GetFileName(), Length + sizeof(WCHAR));

        Status = file.Open(PackPath);
        if (NT_FAILED(Status))
        {
            DebugInfo(L"open %s failed: %08X", PackPath, Status);
            continue;
        }

        FileSize = file.GetSize32();
        if (FileSize > BufferSize)
        {
            BufferSize = FileSize;
            Buffer = ReAllocateMemory(Buffer, BufferSize);
            if (Buffer == nullptr)
            {
                Status = STATUS_INSUFFICIENT_RESOURCES;
                goto CLEAN_UP;
            }
        }

        Status = file.Read(Buffer, FileSize);
        if (!NT_SUCCESS(Status))
        {
            DebugInfo(L"Read %s failed: %08X", PackPath, Status);
            goto CLEAN_UP;
        }

        Entry->Offset.QuadPart      = DataOffset.QuadPart;
        Entry->FileSize.QuadPart    = FileList->Size.QuadPart;
        FileList->Offset.QuadPart   = Entry->Offset.QuadPart;

        SourceBuffer.Initialize(Buffer, Flags, FileSize, 0);
        Status = This->PreCompressData(FileList, &SourceBuffer);
        if (Status == STATUS_NOT_IMPLEMENTED)
        {
            ;
        }
        else if (!NT_SUCCESS(Status))
        {
            continue;
        }
        else
        {
            SET_FLAG(Entry->Flags, UNPACKER_ENTRY_ENCRYPTED);
        }

        if (FileSize * 2 > CompressedBufferSize)
        {
            CompressedBufferSize = FileSize * 2;
            Compressed = ReAllocateMemory(Compressed, CompressedBufferSize);
            if (Compressed == nullptr)
            {
                Status = STATUS_INSUFFICIENT_RESOURCES;
                goto CLEAN_UP;
            }
        }

        FileBuffer = Buffer;

        SourceBuffer.Initialize(Buffer, Flags, FileSize, 0);
        DestinationBuffer.Initialize(nullptr, Flags, CompressedBufferSize, 0);

        LOOP_FOREVER
        {
            DestinationBuffer.Buffer = Compressed;
            Status = This->CompressData(FileList, &SourceBuffer, &DestinationBuffer);
            if (Status != STATUS_BUFFER_TOO_SMALL)
                break;

            CompressedBufferSize = (ULONG_PTR)DestinationBuffer.Size.QuadPart;
            Compressed = ReAllocateMemory(Compressed, CompressedBufferSize);
            if (Compressed == nullptr)
            {
                Status = STATUS_INSUFFICIENT_RESOURCES;
                goto CLEAN_UP;
            }
        }

        WriteBuffer = nullptr;
        WriteSize = (ULONG_PTR)-1;

        if (Status == STATUS_COMPRESSION_DISABLED || Status == STATUS_NOT_IMPLEMENTED)
        {
            WriteBuffer = SourceBuffer.Buffer;
            WriteSize   = (ULONG_PTR)SourceBuffer.Size.QuadPart;
        }
        else if (!NT_SUCCESS(Status))
        {
            ;
        }
        else
        {
            SET_FLAG(Entry->Flags, UNPACKER_ENTRY_COMPRESSED);

            Entry->FileSize.QuadPart = DestinationBuffer.Size.QuadPart;

            WriteBuffer = DestinationBuffer.Buffer;
            WriteSize   = (ULONG_PTR)DestinationBuffer.Size.QuadPart;
        }

        SourceBuffer.Initialize(WriteBuffer, Flags, WriteSize, 0);
        Status = This->PostCompressData(FileList, &SourceBuffer);
        if (!NT_SUCCESS(Status))
        {
            ;
        }
        else
        {
            SET_FLAG(Entry->Flags, UNPACKER_ENTRY_ENCRYPTED);
        }

        Status = pack.Write(WriteBuffer, WriteSize);
        if (!NT_SUCCESS(Status))
        {
            DebugInfo(L"write %s failed: %08X", PackPath, Status);
            goto CLEAN_UP;
        }

        DataOffset.QuadPart += WriteSize;

PACK_NEXT_FILE:

        CopyMemory(Entry->Buffer, FileList->GetFileName(), Length);

        Entry->FileName.Buffer          = PtrSub(Entry->Buffer, EntryBase);
        Entry->FileName.Length          = (USHORT)Length;
        Entry->FileName.MaximumLength   = (USHORT)Length + sizeof(WCHAR);
        Entry->EntrySize                = sizeof(*Entry) - sizeof(Entry->Buffer) + Entry->FileName.MaximumLength;

        Status = This->FinalizeEntrySize(Entry);
        if (Status != STATUS_NOT_IMPLEMENTED && NT_FAILED(Status))
            continue;

        Entry->EntrySize = ROUND_UP(Entry->EntrySize, 16);
        Entry = PtrAdd(Entry, Entry->EntrySize);

        BytesEntry.Context = (NODE_CONTEXT)PackedFileNumber;

        Status = This->GetEntryLookupData(&BytesEntry, FileList);
        if (NT_FAILED(Status))
        {
            DebugInfo(L"GetEntryLookupData failed");
            goto CLEAN_UP;
        }

        Status = EntryLookupTable.InsertBytesEntry(&BytesEntry);

        This->FreeEntryLookupData(&BytesEntry);

        if (NT_FAILED(Status))
        {
            DebugInfo(L"GetEntryLookupData failed");
            goto CLEAN_UP;
        }

        ++PackedFileNumber;
    }

    DebugInfo(L"compress entry");

    Header.EntrySize.QuadPart       = PtrOffset(Entry, EntryBase);
    Header.EntryOffset.QuadPart     = pack.GetCurrentPos64();
    Header.NumberOfFiles.QuadPart   = PackedFileNumber;

    {
        ULONG_PTR   Offset, CompactSize;
        PVOID       Compact;

        Status = EntryLookupTable.BuildCompactTree(&Compact, &CompactSize);
        if (NT_FAILED(Status))
            goto CLEAN_UP;

        Offset = ROUND_UP((ULONG_PTR)Header.EntrySize.QuadPart, 16);

        Header.LookupTableSize.QuadPart = CompactSize;

        if (Header.LookupTableSize.QuadPart + Offset > EntrySize)
        {
            EntrySize = Header.LookupTableSize.QuadPart + Offset;
            EntryBase = (PSAFE_PACK_ENTRY)ReAllocateMemory(EntryBase, EntrySize);
            if (EntryBase == nullptr)
            {
                FreeMemoryP(Compact);
                Status = STATUS_NO_MEMORY;
                goto CLEAN_UP;
            }

            Entry = PtrAdd(EntryBase, Offset);
        }

        CopyMemory(Entry, Compact, CompactSize);

        Header.EntrySize.QuadPart += CompactSize;

        FreeMemoryP(Compact);
    }

    SourceBuffer.Initialize(EntryBase, Flags, Header.EntrySize.QuadPart, 0);
    Status = This->PreCompressEntry(&Header, &SourceBuffer);

    SourceBuffer.Initialize(EntryBase, Flags, Header.EntrySize.QuadPart, 0);
    DestinationBuffer.Initialize(Compressed, Flags, CompressedBufferSize, 0);

    LOOP_FOREVER
    {
        DestinationBuffer.Buffer = Compressed;
        Status = This->CompressEntry(&Header, &SourceBuffer, &DestinationBuffer);
        if (Status != STATUS_BUFFER_TOO_SMALL)
            break;

        CompressedBufferSize = (ULONG_PTR)DestinationBuffer.Size.QuadPart;
        Compressed = ReAllocateMemory(Compressed, CompressedBufferSize);
        if (Compressed == nullptr)
        {
            Status = STATUS_INSUFFICIENT_RESOURCES;
            goto CLEAN_UP;
        }
    }

    if (Status == STATUS_COMPRESSION_DISABLED || Status == STATUS_NOT_IMPLEMENTED)
    {
        WriteBuffer = EntryBase;
        WriteSize   = (ULONG_PTR)Header.EntrySize.QuadPart;
    }
    else if (!NT_SUCCESS(Status))
    {
        goto CLEAN_UP;
    }
    else
    {
        SET_FLAG(Header.Flags, UNPACKER_ENTRY_COMPRESSED);

        WriteBuffer = DestinationBuffer.Buffer;
        WriteSize   = (ULONG_PTR)DestinationBuffer.Size.QuadPart;
    }

    SourceBuffer.Initialize(WriteBuffer, Flags, WriteSize, 0);
    Status = This->PostCompressEntry(&Header, &SourceBuffer);

    pack.Seek(0ll, FILE_END);
    Status = pack.Write(WriteBuffer, WriteSize);
    if (!NT_SUCCESS(Status))
        goto CLEAN_UP;

    Header.EntrySize.QuadPart = WriteSize;

    This->EncryptPackHeader(&Header, sizeof(Header));
    pack.Seek(0ll, FILE_BEGIN);
    Status = pack.Write(&Header, sizeof(Header));

CLEAN_UP:

    EnumDirectoryFilesFree(FileListBase);
    FreeMemory(EntryBase);
    FreeMemory(Buffer);
    FreeMemory(Compressed);

    if (UPK_SUCCESS(Status) && PackedFiles != nullptr)
        PackedFiles->QuadPart = PackedFileNumber;

    return Status;
}


#endif // _SAFEPACKER_H_5447b095_7f6d_4794_a657_bd31b4450648
