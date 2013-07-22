#ifndef _SAFEPACKREADER_H_b1f323e8_670a_4883_8549_098b0c4596e4
#define _SAFEPACKREADER_H_b1f323e8_670a_4883_8549_098b0c4596e4

#include "UnpackerBase.h"
#include "../SafePacker.h"

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
        PSAFE_PACK_ENTRY2 FileInfo,
        PSAFE_PACK_BUFFER Buffer
    )
    {
        return STATUS_NOT_IMPLEMENTED;
    }

    UPK_STATUS
    DecompressData(
        PSAFE_PACK_ENTRY2 FileInfo,
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
                    SourceBuffer->Buffer,
                    SourceBuffer->Size.LowPart,
                    &DestinationBuffer->Size.LowPart
                );

        FAIL_RETURN(Status);

        DestinationBuffer->Size.HighPart = 0;

        return STATUS_SUCCESS;

#endif

    }

    UPK_STATUS
    PostDecompressData(
        PSAFE_PACK_ENTRY2 FileInfo,
        PSAFE_PACK_BUFFER Buffer
    )
    {
        return STATUS_NOT_IMPLEMENTED;
    }
};

template<typename BaseType>
class SafePackReaderImpl : public UnpackerImpl<BaseType>, public SafePackReaderBase
{
protected:
    NtFileDisk File;

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
        PSAFE_PACK_ENTRY2               Entry;
        SAFE_PACK_BUFFER                SourceBuffer, DestinationBuffer;
        PSAFE_PACK_COMPRESSED_HEADER    CompressHeader;
        BaseType*                       This;

        This = GetTopClass();

        m_Index.EntrySize = sizeof(*Entry);

        Entry = (PSAFE_PACK_ENTRY2)AllocateEntry(Header->NumberOfFiles);
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

        return Status;
    }


protected:

    UPK_STATUS
    DecompressBlock(
        PSAFE_PACK_ENTRY2 FileInfo,
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
