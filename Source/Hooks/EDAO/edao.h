#ifndef _EDAO_H_5c8a3013_4334_4138_9413_3d0209da878e_
#define _EDAO_H_5c8a3013_4334_4138_9413_3d0209da878e_

#include "MyLibrary.h"

class EDAO
{
public:
    VOID THISCALL Fade(ULONG Param1, ULONG Param2, ULONG Param3, ULONG Param4, ULONG Param5, ULONG Param6);
    BOOL THISCALL CheckItemEquipped(ULONG ItemId, PULONG EquippedIndex);

    static TYPE_OF(&EDAO::Fade)                 StubFade;
    static TYPE_OF(&EDAO::CheckItemEquipped)    StubCheckItemEquipped;
};

DECL_SELECTANY TYPE_OF(EDAO::StubFade) EDAO::StubFade = NULL;
DECL_SELECTANY TYPE_OF(EDAO::StubCheckItemEquipped) EDAO::StubCheckItemEquipped = NULL;

class CBattle
{
public:
    VOID USE_ATTACK_FOR_CHECKING();
    VOID USE_MAGIC_FOR_CHECKING();
    VOID USE_CRAFT_FOR_CHECKING();
    VOID USE_SCRAFT_FOR_CHECKING();
};

class CSSaveData
{
public:
    VOID SaveData2SystemData();
    VOID SystemData2SaveData();
};


#define UCL_COMPRESS_MAGIC TAG4('UCL4')

#pragma pack(1)

typedef struct
{
    ULONG Magic;
    ULONG CompressedSize;

} UCL_COMPRESS_HEADER;

#pragma pack()

class EDAOFileStream
{
public:
    ULONG THISCALL Read(PVOID Buffer, ULONG Size, ULONG Count = 1, ULONG Unknown = 0, ULONG Unknown2 = 0)
    {
        TYPE_OF(&EDAOFileStream::Read) StubRead;

        *(PVOID *)&StubRead = (PVOID)0x6725AA;

        return (this->*StubRead)(Buffer, Size, Count, Unknown, Unknown2);
    }

    BOOL THISCALL Seek(LONG Offset, ULONG SeekMethod)
    {
        TYPE_OF(&EDAOFileStream::Seek) StubSeek;

        *(PVOID *)&StubSeek = (PVOID)0x675787;
        return (this->*StubSeek)(Offset, SeekMethod);
    }

    ULONG THISCALL Uncompress(PVOID Output, ULONG BlockSize, ULONG BlockCount)
    {
        LONG_PTR            BytesRead;
        PVOID               Buffer;
        UCL_COMPRESS_HEADER Header;

        static PVOID        StaticBuffer;
        static ULONG_PTR    StaticBufferSize;

        ULONG pos = m_Position;

        BytesRead = Read(&Header, sizeof(Header));
        if (BytesRead != sizeof(Header) || Header.Magic != UCL_COMPRESS_MAGIC)
        {
            Seek(-BytesRead, SEEK_CUR);
            m_Position = pos;

            return (this->*StubUncompress)(Output, BlockSize, BlockCount);
        }

        Buffer = StaticBuffer;
        if (Header.CompressedSize > StaticBufferSize)
        {
            StaticBufferSize = Header.CompressedSize;
            Buffer = ReAllocateMemoryP(Buffer, StaticBufferSize);
            StaticBuffer = Buffer;
        }

        if (Buffer == NULL)
            return 0;

        Read(Buffer, Header.CompressedSize);

        UCL_NRV2E_Decompress(Buffer, Header.CompressedSize, Output, &BlockSize);

        return BlockSize;
    }

    static TYPE_OF(&EDAOFileStream::Uncompress) StubUncompress;

    CHAR    m_FileName[0x24];   // 0x00
    ULONG   m_Position;         // 0x24
    ULONG   m_Size;             // 0x28
    DUMMY_STRUCT(0x54);         // 0x2C
    BYTE    m_BufferIndex;
    BYTE    m_BufferFlags;
};

DECL_SELECTANY TYPE_OF(EDAOFileStream::StubUncompress) EDAOFileStream::StubUncompress = NULL;


#endif // _EDAO_H_5c8a3013_4334_4138_9413_3d0209da878e_
