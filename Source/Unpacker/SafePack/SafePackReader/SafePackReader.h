#ifndef _SAFEPACKREADER_H_b1f323e8_670a_4883_8549_098b0c4596e4
#define _SAFEPACKREADER_H_b1f323e8_670a_4883_8549_098b0c4596e4

#include "UnpackerBase.h"
#include "../SafePacker.h"

typedef struct SAFE_PACK_READER_ENTRY : public UNPACKER_FILE_ENTRY_BASE
{
    //ULONG FileNameHash[4];

} SAFE_PACK_READER_ENTRY, *PSAFE_PACK_READER_ENTRY;

interface ISafePackReader
{
    virtual UPK_STATUS STDCALL Read(PVOID Buffer, ULONG_PTR Size, PLARGE_INTEGER BytesRead = nullptr) = 0;
    virtual UPK_STATUS STDCALL GetSize(PLARGE_INTEGER FileSize) = 0;
    virtual UPK_STATUS STDCALL GetPosition(PLARGE_INTEGER Position) = 0;
    virtual UPK_STATUS STDCALL Seek(LONG64 Offset, ULONG_PTR MoveMethod = FILE_BEGIN, PLARGE_INTEGER NewPosition = nullptr) = 0;
};

class SafePackReaderStreamDisk : public ISafePackReader
{
protected:
    LARGE_INTEGER   Size;
    LARGE_INTEGER   BeginOffset;
    NtFileDisk      File;

public:
    UPK_STATUS STDCALL Read(PVOID Buffer, ULONG_PTR Size, PLARGE_INTEGER BytesRead = nullptr)
    {
        return this->File.Read(Buffer, Size, BytesRead);
    }

    UPK_STATUS STDCALL GetSize(PLARGE_INTEGER Size)
    {
        Size->QuadPart = this->Size.QuadPart;
        return STATUS_SUCCESS;
    }

    UPK_STATUS STDCALL GetPosition(PLARGE_INTEGER Position)
    {
        NTSTATUS Status;

        Status = File.GetPosition(Position);
        if (NT_SUCCESS(Status))
            Position->QuadPart -= BeginOffset.QuadPart;

        return Status;
    }

    UPK_STATUS STDCALL Seek(LONG64 Offset, ULONG_PTR MoveMethod = FILE_BEGIN, PLARGE_INTEGER NewPosition = nullptr)
    {
        LARGE_INTEGER NewOffset;

        switch(MoveMethod)
        {
            case FILE_CURRENT:
                File.GetPosition(&NewOffset);
                NewOffset.QuadPart += Offset;
                break;

            case FILE_END:
                NewOffset.QuadPart = BeginOffset.QuadPart + Size.QuadPart + Offset;
                break;

            case FILE_BEGIN:
                NewOffset.QuadPart = BeginOffset.QuadPart + Offset;
                break;

            default:
                return STATUS_INVALID_PARAMETER_2;
        }

        if (NewOffset.QuadPart < BeginOffset.QuadPart ||
            NewOffset.QuadPart >= BeginOffset.QuadPart +  Size.QuadPart)
        {
            return STATUS_INVALID_PARAMETER_1;
        }

        File.Seek(NewOffset, FILE_BEGIN, NewPosition);

        return STATUS_SUCCESS;
    }

    static UPK_STATUS CreateStream(ISafePackReader *Reader, PSAFE_PACK_READER_ENTRY Entry)
    {
        return 0;
    }
};

class SafePackReaderBase
{
protected:

    UPK_STATUS
    DecryptPackHeader(
        PSAFE_PACK_HEADER Header
    )
    {
        return STATUS_NOT_IMPLEMENTED;
    }

    UPK_STATUS
    PreDecompressEntry(
        PSAFE_PACK_HEADER Header,
        PSAFE_PACK_BUFFER SourceBuffer
    )
    {
        return STATUS_NOT_IMPLEMENTED;
    }

    UPK_STATUS
    DecompressEntry(
        PSAFE_PACK_HEADER Header,
        PSAFE_PACK_BUFFER SourceBuffer,
        PSAFE_PACK_BUFFER DestinationBuffer
    )
    {
        return DecompressData(nullptr, SourceBuffer, DestinationBuffer);
    }

    UPK_STATUS
    PostDecompressEntry(
        PSAFE_PACK_HEADER Header,
        PSAFE_PACK_BUFFER SourceBuffer
    )
    {
        return STATUS_NOT_IMPLEMENTED;
    }

    UPK_STATUS
    PreDecompressData(
        PSAFE_PACK_READER_ENTRY FileInfo,
        PSAFE_PACK_BUFFER Buffer
    )
    {
        return STATUS_NOT_IMPLEMENTED;
    }

    UPK_STATUS
    DecompressData(
        PSAFE_PACK_READER_ENTRY FileInfo,
        PSAFE_PACK_BUFFER SourceBuffer,
        PSAFE_PACK_BUFFER DestinationBuffer
    )
    {

#if !DEFAULT_COMPRESS_DATA

        return STATUS_COMPRESSION_DISABLED;

#else

        NTSTATUS                        Status;
        ULONG                           CompressionFormatAndEngine;
        PSAFE_PACK_COMPRESSED_HEADER    Header;

        Header = (PSAFE_PACK_COMPRESSED_HEADER)SourceBuffer->Buffer;

        if (Header->CompressMethod != CompressMethodLZNT1)
            return STATUS_UNSUPPORTED_COMPRESSION;

        if (Header->OriginalSize.HighPart != 0)
            return STATUS_BAD_COMPRESSION_BUFFER;

        if (DestinationBuffer->Size.QuadPart < Header->OriginalSize.QuadPart)
        {
            DestinationBuffer->Size.QuadPart = Header->OriginalSize.QuadPart;
            return STATUS_BUFFER_TOO_SMALL;
        }


        CompressionFormatAndEngine = COMPRESSION_FORMAT_LZNT1 | COMPRESSION_ENGINE_MAXIMUM;

        Status = RtlDecompressBuffer(
                    CompressionFormatAndEngine,
                    DestinationBuffer->Buffer,
                    DestinationBuffer->Size.LowPart,
                    Header + 1,
                    Header->CompressedSize.LowPart,
                    &DestinationBuffer->Size.LowPart
                );

        FAIL_RETURN(Status);

        DestinationBuffer->Size.HighPart = 0;

        return STATUS_SUCCESS;

#endif

    }

    UPK_STATUS
    PostDecompressData(
        PSAFE_PACK_READER_ENTRY FileInfo,
        PSAFE_PACK_BUFFER Buffer
    )
    {
        return STATUS_NOT_IMPLEMENTED;
    }

    ULONG_PTR GetHeaderMagic()
    {
        return SAFE_PACK_MAGIC;
    }
};

template<typename BaseType>
class SafePackReaderImpl : public UnpackerImpl<BaseType>, public SafePackReaderBase
{
protected:
    NtFileDisk File;
    //ml::GrowableArray<PSAFE_PACK_READER_ENTRY> LookupTable;
    CompactTrie LookupTable;

public:

    UPK_STATUS Open(PCWSTR FileName)
    {
        UPK_STATUS          Status;
        SAFE_PACK_HEADER    HeaderBuffer;
        PSAFE_PACK_HEADER   Header;
        BaseType*           This;

        This = GetTopClass();

        Status = File.Open(FileName);
        FAIL_RETURN(Status);

        Status = File.Read(&HeaderBuffer, sizeof(HeaderBuffer));
        FAIL_RETURN(Status);

        This->DecryptPackHeader(&HeaderBuffer);
        FAIL_RETURN(Status);

        if (HeaderBuffer.Magic != This->GetHeaderMagic())
            return STATUS_INVALID_IMAGE_FORMAT;

        if (HeaderBuffer.HeaderSize < sizeof(HeaderBuffer))
            return STATUS_INFO_LENGTH_MISMATCH;

        if (HeaderBuffer.HeaderSize != sizeof(HeaderBuffer))
        {
            File.Rewind();

            Header = (PSAFE_PACK_HEADER)AllocStack(HeaderBuffer.HeaderSize);
            Status = File.Read(Header, HeaderBuffer.HeaderSize);
            FAIL_RETURN(Status);

            This->DecryptPackHeader(Header);
            FAIL_RETURN(Status);
        }
        else
        {
            Header = &HeaderBuffer;
        }

        Status = InitializeEntry(Header);

        return Status;
    }

    UPK_STATUS InitializeEntry(PSAFE_PACK_HEADER Header)
    {
        UPK_STATUS                      Status;
        PVOID                           EntryBuffer;
        ULONG_PTR                       EntrySize;
        PSAFE_PACK_ENTRY                PackEntry, PackEntryEnd;
        PSAFE_PACK_READER_ENTRY         Entry;
        SAFE_PACK_BUFFER                SourceBuffer, DestinationBuffer;
        PSAFE_PACK_COMPRESSED_HEADER    CompressHeader;
        BaseType*                       This;

        This = GetTopClass();

        m_Index.EntrySize = sizeof(*Entry);

        Entry = (PSAFE_PACK_READER_ENTRY)AllocateEntry(Header->NumberOfFiles.QuadPart);
        if (Entry == nullptr)
            return STATUS_NO_MEMORY;

        Status = File.Seek(Header->EntryOffset);
        FAIL_RETURN(Status);

        EntryBuffer = AllocateMemory(Header->EntrySize.QuadPart);
        if (EntryBuffer == nullptr)
            return STATUS_NO_MEMORY;

        SCOPE_EXIT
        {
            FreeMemory(EntryBuffer);
        }
        SCOPE_EXIT_END;

        Status = File.Read(EntryBuffer, Header->EntrySize.QuadPart);
        FAIL_RETURN(Status);

        SourceBuffer.Initialize(EntryBuffer, 0, Header->EntrySize.QuadPart);

        Status = This->PreDecompressEntry(Header, &SourceBuffer);
        if (Status != STATUS_NOT_IMPLEMENTED)
            FAIL_RETURN(Status);

        if (FLAG_ON(Header->Flags, UNPACKER_ENTRY_COMPRESSED))
        {
            CompressHeader = (PSAFE_PACK_COMPRESSED_HEADER)EntryBuffer;

            DestinationBuffer.Buffer = AllocateMemory(CompressHeader->OriginalSize.QuadPart);
            if (DestinationBuffer.Buffer == nullptr)
                return STATUS_NO_MEMORY;

            DestinationBuffer.Size.QuadPart = CompressHeader->OriginalSize.QuadPart;

            Status = This->DecompressEntry(Header, &SourceBuffer, &DestinationBuffer);
            FAIL_RETURN(Status);

            FreeMemory(EntryBuffer);

            EntryBuffer = DestinationBuffer.Buffer;
            EntrySize = DestinationBuffer.Size.QuadPart;
        }
        else
        {
            EntrySize = Header->EntrySize.QuadPart;
        }

        PackEntry = (PSAFE_PACK_ENTRY)EntryBuffer;
        PackEntryEnd = PtrAdd(PackEntry, EntrySize);

        --Entry;

        for (ULONG_PTR NumberOfFiles = Header->NumberOfFiles.QuadPart; 
             NumberOfFiles != 0 && PackEntry < PackEntryEnd;
             PackEntry = PtrAdd(PackEntry, PackEntry->EntrySize), --NumberOfFiles)
        {
            ++Entry;

            PackEntry->FileName.Buffer = PtrAdd(PackEntry->FileName.Buffer, EntryBuffer);

            Entry->Size.QuadPart    = PackEntry->FileSize.QuadPart;
            Entry->Offset.QuadPart  = PackEntry->Offset.QuadPart;
            Entry->Attributes       = PackEntry->Attributes;
            Entry->Flags            = PackEntry->Flags;

            Entry->SetFileName(&PackEntry->FileName);

            ++m_Index.FileCount.QuadPart;
        }

        if (PackEntry >= PackEntryEnd)
            return STATUS_INFO_LENGTH_MISMATCH;

        Status = LookupTable.Initialize(PackEntry, Header->LookupTableSize.QuadPart);

        return Status;
    }

    NoInline PSAFE_PACK_READER_ENTRY Lookup(PCWSTR FileName, ULONG_PTR Length)
    {
        NODE_CONTEXT        Index;
        NTSTATUS            Status;
        TRIE_BYTES_ENTRY    Bytes = { (PVOID)FileName, Length * sizeof(FileName[0]) };

        Status = this->LookupTable.Lookup(&Bytes, &Index);
        if (NT_FAILED(Status))
            return nullptr;

        return (PSAFE_PACK_READER_ENTRY)PtrAdd(m_Index.Entry, Index * m_Index.EntrySize);
    }

    PSAFE_PACK_READER_ENTRY Lookup(PCWSTR FileName)
    {
        return Lookup(FileName, StrLengthW(FileName) * sizeof(FileName[0]));
    }

    PSAFE_PACK_READER_ENTRY Lookup(PCUNICODE_STRING FileName)
    {
        return Lookup(FileName->Buffer, FileName->Length);
    }

protected:

    UPK_STATUS
    DecompressBlock(
        PSAFE_PACK_READER_ENTRY FileInfo,
        PSAFE_PACK_BUFFER SourceBuffer,
        PSAFE_PACK_BUFFER DestinationBuffer
    )
    {
        UPK_STATUS  Status;
        BaseType*   This;

        This = GetTopClass();

        DestinationBuffer->Initialize();

        LOOP_FOREVER
        {
            DestinationBuffer.Buffer = Compressed;
            Status = This->DecompressData(FileInfo, &SourceBuffer, &DestinationBuffer);
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
    }
};

#endif // _SAFEPACKREADER_H_b1f323e8_670a_4883_8549_098b0c4596e4
