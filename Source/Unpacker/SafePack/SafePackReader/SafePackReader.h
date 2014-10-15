#ifndef _SAFEPACKREADER_H_b1f323e8_670a_4883_8549_098b0c4596e4
#define _SAFEPACKREADER_H_b1f323e8_670a_4883_8549_098b0c4596e4

#include "UnpackerBase.h"
#include "../SafePacker.h"

typedef struct SAFE_PACK_READER_ENTRY : public UNPACKER_FILE_ENTRY_BASE
{
    ULONG Context[8];

} SAFE_PACK_READER_ENTRY, *PSAFE_PACK_READER_ENTRY;

interface ISafePackReader
{
    virtual STDCALL ~ISafePackReader() {};
    virtual LONG STDCALL AddRef() = 0;
    virtual LONG STDCALL Release() = 0;

    virtual UPK_STATUS STDCALL Read(PVOID Buffer, ULONG_PTR Size, PLARGE_INTEGER BytesRead = nullptr) = 0;
    virtual UPK_STATUS STDCALL GetSize(PLARGE_INTEGER FileSize) = 0;
    virtual UPK_STATUS STDCALL GetPosition(PLARGE_INTEGER Position) = 0;
    virtual UPK_STATUS STDCALL Seek(LONG64 Offset, ULONG_PTR MoveMethod = FILE_BEGIN, PLARGE_INTEGER NewPosition = nullptr) = 0;
};

class SafePackReaderStreamBase : public ISafePackReader
{
protected:
    LONG RefCount;

public:
    SafePackReaderStreamBase()
    {
        this->RefCount = 1;
    }

    virtual LONG STDCALL AddRef()
    {
        return ++RefCount;
    }

    virtual LONG STDCALL Release()
    {
        LONG Ref = --this->RefCount;
        if (Ref == 0)
            delete this;
        return Ref;
    }
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
        UPK_STATUS Status;

        Status = File.GetPosition(Position);
        if (UPK_SUCCESS(Status))
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

    UPK_STATUS STDCALL Release()
    {
        delete this;
        return STATUS_SUCCESS;
    }

    static UPK_STATUS CreateStream(ISafePackReader **Reader, PSAFE_PACK_READER_ENTRY Entry)
    {
        return 0;
    }
};

class SafePackReaderBase
{
protected:

    UPK_STATUS
    DecryptPackHeader(
        PSAFE_PACK_HEADER   Header,
        ULONG_PTR           HeaderSize
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

    UPK_STATUS FillEntryFromPackEntry(PSAFE_PACK_READER_ENTRY Entry, PSAFE_PACK_ENTRY PackEntry, PVOID PackEntryBase)
    {
        PackEntry->FileName.Buffer = PtrAdd(PackEntry->FileName.Buffer, PackEntryBase);

        Entry->Size.QuadPart    = PackEntry->FileSize.QuadPart;
        Entry->Offset.QuadPart  = PackEntry->Offset.QuadPart;
        Entry->Attributes       = PackEntry->Attributes;
        Entry->Flags            = PackEntry->Flags;

        Entry->SetFileName(&PackEntry->FileName);

        return STATUS_SUCCESS;
    }

    UPK_STATUS
    PreDecompressData(
        PSAFE_PACK_READER_ENTRY FileInfo,
        PSAFE_PACK_BUFFER       Buffer
    )
    {
        return STATUS_SUCCESS;
    }

    UPK_STATUS
    DecompressData(
        PSAFE_PACK_READER_ENTRY FileInfo,
        PSAFE_PACK_BUFFER       SourceBuffer,
        PSAFE_PACK_BUFFER       DestinationBuffer,
        ULONG_PTR               CompressionFormatAndEngine = COMPRESSION_FORMAT_LZNT1 | COMPRESSION_ENGINE_STANDARD
    )
    {

#if !DEFAULT_COMPRESS_DATA

        return STATUS_NOT_IMPLEMENTED;

#else

        UPK_STATUS                      Status;
        PSAFE_PACK_COMPRESSED_HEADER    Header;

        Header = (PSAFE_PACK_COMPRESSED_HEADER)SourceBuffer->Buffer;

        if ((Header->Magic * 2) != (LZNT1_MAGIC * 2) || Header->CompressMethod != CompressMethodLZNT1)
            return STATUS_UNSUPPORTED_COMPRESSION;

        if (Header->OriginalSize.HighPart != 0)
            return STATUS_BAD_COMPRESSION_BUFFER;

        if (DestinationBuffer->Size.QuadPart < Header->OriginalSize.QuadPart)
        {
            DestinationBuffer->Size.QuadPart = Header->OriginalSize.QuadPart;
            return STATUS_BUFFER_TOO_SMALL;
        }

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
        PSAFE_PACK_BUFFER       Buffer
    )
    {
        return STATUS_SUCCESS;
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
    ml::String FileName;

public:
    HANDLE GetHandle()
    {
        return this->File;
    }

    UPK_STATUS Open(PCWSTR FileName)
    {
        UPK_STATUS          Status;
        SAFE_PACK_HEADER    HeaderBuffer;
        PSAFE_PACK_HEADER   Header;
        BaseType*           This;

        This = GetTopClass();

        Status = File.Open(FileName);
        FAIL_RETURN(Status);

        this->FileName = FileName;

        Status = File.Read(&HeaderBuffer, sizeof(HeaderBuffer));
        FAIL_RETURN(Status);

        This->DecryptPackHeader(&HeaderBuffer, sizeof(HeaderBuffer));
        FAIL_RETURN(Status);

        if (((HeaderBuffer.Magic * 2) ^ (This->GetHeaderMagic() * 2)) != 0)
            return STATUS_INVALID_IMAGE_FORMAT;

        if (HeaderBuffer.HeaderSize < sizeof(HeaderBuffer))
            return STATUS_INFO_LENGTH_MISMATCH;

        if (HeaderBuffer.HeaderSize != sizeof(HeaderBuffer))
        {
            File.Rewind();

            Header = (PSAFE_PACK_HEADER)AllocStack(HeaderBuffer.HeaderSize);
            Status = File.Read(Header, HeaderBuffer.HeaderSize);
            FAIL_RETURN(Status);

            This->DecryptPackHeader(Header, HeaderBuffer.HeaderSize);
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

        DestinationBuffer.Initialize(PackEntry, 0, EntrySize);
        Status = This->PostDecompressEntry(Header, &SourceBuffer);
        if (Status != STATUS_NOT_IMPLEMENTED)
            FAIL_RETURN(Status);

        --Entry;

        for (ULONG_PTR NumberOfFiles = Header->NumberOfFiles.QuadPart;
             NumberOfFiles != 0 && PackEntry < PackEntryEnd;
             PackEntry = PtrAdd(PackEntry, PackEntry->EntrySize), --NumberOfFiles)
        {
            ++Entry;
            This->FillEntryFromPackEntry(Entry, PackEntry, EntryBuffer);
            ++m_Index.FileCount.QuadPart;
        }

        if (PackEntry >= PackEntryEnd)
            return STATUS_INFO_LENGTH_MISMATCH;

        Status = LookupTable.Initialize(PackEntry, Header->LookupTableSize.QuadPart);

        return Status;
    }

    NoInline PSAFE_PACK_READER_ENTRY Lookup(PVOID LookupData, ULONG_PTR SizeInBytes)
    {
        NODE_CONTEXT        Index;
        TRIE_BYTES_ENTRY    Bytes;
        NTSTATUS            Status;

        Bytes.Data = LookupData;
        Bytes.SizeInBytes = SizeInBytes;

        Status = this->LookupTable.Lookup(&Bytes, &Index);
        if (UPK_FAILED(Status))
            return nullptr;

        return (PSAFE_PACK_READER_ENTRY)PtrAdd(m_Index.Entry, Index * m_Index.EntrySize);
    }

    NoInline PSAFE_PACK_READER_ENTRY Lookup(PCWSTR FileName, ULONG_PTR Length)
    {
        PWSTR Buffer;

        Buffer = (PWSTR)AllocStack(Length * sizeof(FileName[0]));

        for (ULONG_PTR Count = Length; Count != 0; --Count)
        {
            WCHAR ch = *FileName++;

            switch (ch)
            {
                case '/':
                    ch = '\\';
                    break;

                default:
                    ch = CHAR_UPPER(ch);
                    break;
            }

            *Buffer++ = ch;
        }

        Buffer -= Length;
        return GetTopClass()->Lookup((PVOID)Buffer, Length * sizeof(FileName[0]));
    }

    PSAFE_PACK_READER_ENTRY Lookup(PCWSTR FileName)
    {
        return GetTopClass()->Lookup(FileName, StrLengthW(FileName));
    }

    PSAFE_PACK_READER_ENTRY Lookup(PCUNICODE_STRING FileName)
    {
        return GetTopClass()->Lookup(FileName->Buffer, FileName->Length);
    }

protected:
    class PackMemoryStream : public SafePackReaderStreamBase
    {
    protected:
        NtFileMemory            File;
        BaseType*               Pack;
        PSAFE_PACK_READER_ENTRY Entry;

    public:
        PackMemoryStream(PVOID Buffer, ULONG_PTR Size, BaseType* Pack, PSAFE_PACK_READER_ENTRY Entry, NTSTATUS &Status)
        {
            Status = File.Open(Buffer, Size);
            this->Pack = Pack;
            this->Entry = Entry;
        }

        virtual UPK_STATUS STDCALL Read(PVOID Buffer, ULONG_PTR Size, PLARGE_INTEGER BytesRead = nullptr)
        {
            UPK_STATUS          Status;
            SAFE_PACK_BUFFER    DestinationBuffer;

            Status = this->File.Read(Buffer, Size, BytesRead);
            FAIL_RETURN(Status);

            DestinationBuffer.Initialize(Buffer, 0, BytesRead->QuadPart, this->File.GetPosition32());
            //Status = this->Pack->PreDecompressData(this->Entry, &DestinationBuffer);
            //Status = this->Pack->PostDecompressData(this->Entry, &DestinationBuffer);

            return Status;
        }

        virtual UPK_STATUS STDCALL GetSize(PLARGE_INTEGER FileSize)
        {
            FileSize->QuadPart = this->File.GetSize64();
            return STATUS_SUCCESS;
        }

        virtual UPK_STATUS STDCALL GetPosition(PLARGE_INTEGER Position)
        {
            Position->QuadPart = this->File.GetPosition32();
            return STATUS_SUCCESS;
        }

        virtual UPK_STATUS STDCALL Seek(LONG64 Offset, ULONG_PTR MoveMethod = FILE_BEGIN, PLARGE_INTEGER NewPosition = nullptr)
        {
            return this->File.Seek(Offset, MoveMethod, NewPosition);
        }
    };

    class PackFileStream : public SafePackReaderStreamBase
    {
    protected:
        NtFileDisk              File;
        BaseType*               Pack;
        PSAFE_PACK_READER_ENTRY Entry;

    public:
        PackFileStream(PCWSTR FileName, BaseType* Pack, PSAFE_PACK_READER_ENTRY Entry, NTSTATUS &Status)
        {
            Status = this->File.Open(FileName);
            Status = NT_SUCCESS(Status) && this->File.Seek(Entry->Offset, FILE_BEGIN);
            this->Pack = Pack;
            this->Entry = Entry;
        }

        virtual UPK_STATUS STDCALL Read(PVOID Buffer, ULONG_PTR Size, PLARGE_INTEGER BytesRead = nullptr)
        {
            UPK_STATUS          Status;
            LARGE_INTEGER       Position, LocalBytesRead;
            SAFE_PACK_BUFFER    DestinationBuffer;

            Status = this->GetPosition(&Position);
            FAIL_RETURN(Status);

            Size = ML_MIN(Size, this->Entry->Size.QuadPart - Position.QuadPart);

            Status = this->File.Read(Buffer, Size, &LocalBytesRead);
            FAIL_RETURN(Status);

            if (BytesRead != nullptr)
                BytesRead->QuadPart = LocalBytesRead.QuadPart;

            DestinationBuffer.Initialize(Buffer, 0, LocalBytesRead.QuadPart, Position.QuadPart);
            Status = this->Pack->PreDecompressData(this->Entry, &DestinationBuffer);
            Status = this->Pack->PostDecompressData(this->Entry, &DestinationBuffer);

            return Status;
        }

        virtual UPK_STATUS STDCALL GetSize(PLARGE_INTEGER FileSize)
        {
            FileSize->QuadPart = this->Entry->Size.QuadPart;
            return STATUS_SUCCESS;
        }

        virtual UPK_STATUS STDCALL GetPosition(PLARGE_INTEGER Position)
        {
            Position->QuadPart = this->File.GetCurrentPos64() - this->Entry->Offset.QuadPart;
            return STATUS_SUCCESS;
        }

        virtual UPK_STATUS STDCALL Seek(LONG64 Offset, ULONG_PTR MoveMethod = FILE_BEGIN, PLARGE_INTEGER NewPosition = nullptr)
        {
            LARGE_INTEGER NewOffset;

            switch(MoveMethod)
            {
                case FILE_CURRENT:
                    NewOffset.QuadPart = this->File.GetCurrentPos64() + Offset;
                    break;

                case FILE_END:
                    NewOffset.QuadPart = this->Entry->Offset.QuadPart + this->Entry->Size.QuadPart + Offset;
                    break;

                case FILE_BEGIN:
                    NewOffset.QuadPart = this->Entry->Offset.QuadPart + Offset;
                    break;

                default:
                    return STATUS_INVALID_PARAMETER_2;
            }

            if (NewOffset.QuadPart < this->Entry->Offset.QuadPart)
                return STATUS_INVALID_PARAMETER;

            if (NewPosition != nullptr)
                NewPosition->QuadPart = NewOffset.QuadPart - this->Entry->Offset.QuadPart;

            return this->File.Seek(NewOffset, FILE_BEGIN);
        }
    };

public:
    UPK_STATUS
    GetFileStream(
        ISafePackReader**           Stream,
        PUNPACKER_FILE_ENTRY_BASE   BaseEntry,
        ULONG                       Flags = 0
    )
    {
        UPK_STATUS              Status;
        PSAFE_PACK_READER_ENTRY Entry;
        SAFE_PACK_BUFFER        SourceBuffer, DestinationBuffer;

        *Stream = nullptr;
        Entry = (PSAFE_PACK_READER_ENTRY)BaseEntry;

        if (FLAG_OFF(Entry->Flags, UNPACKER_ENTRY_COMPRESSED))
        {
            Status = STATUS_UNSUCCESSFUL;

            *Stream = new PackFileStream(this->FileName, GetTopClass(), Entry, Status);
            if (*Stream == nullptr)
                return STATUS_NO_MEMORY;

            if (NT_FAILED(Status))
            {
                (*Stream)->Release();
                *Stream = nullptr;
                return Status;
            }
        }
        else
        {
            UNPACKER_FILE_INFO FileInfo;

            Status = GetTopClass()->GetFileData(&FileInfo, Entry, Flags);
            FAIL_RETURN(Status);

            *Stream = new PackMemoryStream(FileInfo.BinaryData.Buffer, FileInfo.BinaryData.Size.QuadPart, GetTopClass(), Entry, Status);
            if (*Stream == nullptr)
                return STATUS_NO_MEMORY;

            if (NT_FAILED(Status))
            {
                (*Stream)->Release();
                *Stream = nullptr;
                return Status;
            }
        }

        return STATUS_SUCCESS;
    }

    UPK_STATUS
    GetFileData(
        PUNPACKER_FILE_INFO         FileInfo,
        PUNPACKER_FILE_ENTRY_BASE   BaseEntry,
        ULONG                       Flags = 0
    )
    {
        PVOID                   Buffer;
        UPK_STATUS              Status;
        PSAFE_PACK_READER_ENTRY Entry;
        SAFE_PACK_BUFFER        SourceBuffer, DestinationBuffer;

        Entry = (PSAFE_PACK_READER_ENTRY)BaseEntry;

        Status = File.Seek(Entry->Offset.QuadPart);
        FAIL_RETURN(Status);

        if (FLAG_ON(Entry->Flags, UNPACKER_ENTRY_COMPRESSED))
        {
            Buffer = AllocateMemory(Entry->Size.QuadPart);
            if (Buffer == nullptr)
                return STATUS_NO_MEMORY;

            Status = File.Read(Buffer, Entry->Size.QuadPart);
            if (UPK_FAILED(Status))
            {
                FreeMemory(Buffer);
                return Status;
            }

            SourceBuffer.Initialize(Buffer, 0, Entry->Size.QuadPart);

            Status = DecompressBlock(Entry, &SourceBuffer, &DestinationBuffer);

            FreeMemory(Buffer);
            FAIL_RETURN(Status);

            Status = AllocateFileData(FileInfo, DestinationBuffer.Size.QuadPart, UnpackerFileBinary);
            if (UPK_SUCCESS(Status))
                CopyMemory(FileInfo->BinaryData.Buffer, DestinationBuffer.Buffer, DestinationBuffer.Size.QuadPart);

            FreeMemory(DestinationBuffer.Buffer);
        }
        else
        {
            Status = AllocateFileData(FileInfo, Entry->Size.QuadPart, UnpackerFileBinary);
            FAIL_RETURN(Status);

            Status = File.Read(FileInfo->BinaryData.Buffer, Entry->Size.QuadPart);
            if (UPK_SUCCESS(Status))
            {
                SAFE_PACK_BUFFER DestinationBuffer;
                DestinationBuffer.Initialize(FileInfo->BinaryData.Buffer, 0, Entry->Size.QuadPart, 0);
                Status = GetTopClass()->PreDecompressData(Entry, &DestinationBuffer);
                Status = GetTopClass()->PostDecompressData(Entry, &DestinationBuffer);
                Status = Status == STATUS_NOT_IMPLEMENTED ? STATUS_SUCCESS : Status;
            }

            if (UPK_FAILED(Status))
            {
                FreeFileData(FileInfo);
                return Status;
            }
        }

        return Status;
    }

protected:

    NoInline
    UPK_STATUS
    DecompressBlock(
        PSAFE_PACK_READER_ENTRY FileInfo,
        PSAFE_PACK_BUFFER       SourceBuffer,
        PSAFE_PACK_BUFFER       DestinationBuffer
    )
    {
        PVOID       Buffer;
        UPK_STATUS  Status;
        BaseType*   This;

        This = GetTopClass();

        DestinationBuffer->Initialize();

        Status = This->PreDecompressData(FileInfo, SourceBuffer);
        if (Status != STATUS_NOT_IMPLEMENTED && UPK_FAILED(Status))
            return Status;

        Buffer = nullptr;

        LOOP_FOREVER
        {
            DestinationBuffer->Buffer = Buffer;
            Status = This->DecompressData(FileInfo, SourceBuffer, DestinationBuffer);
            if (Status != STATUS_BUFFER_TOO_SMALL)
                break;

            Buffer = ReAllocateMemory(Buffer, DestinationBuffer->Size.QuadPart);
            if (Buffer == nullptr)
            {
                Status = STATUS_INSUFFICIENT_RESOURCES;
                return Status;
            }
        }

        if (Status != STATUS_NOT_IMPLEMENTED && UPK_FAILED(Status))
        {
            FreeMemory(DestinationBuffer->Buffer);
            return Status;
        }

        Status = This->PostDecompressData(FileInfo, DestinationBuffer);

        if (Status == STATUS_NOT_IMPLEMENTED)
            Status = STATUS_SUCCESS;

        if (UPK_FAILED(Status))
            FreeMemory(DestinationBuffer->Buffer);

        return Status;
    }
};

#endif // _SAFEPACKREADER_H_b1f323e8_670a_4883_8549_098b0c4596e4
