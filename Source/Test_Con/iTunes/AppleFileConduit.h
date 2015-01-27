ML_NAMESPACE_BEGIN(AFC);

enum AFC_FILE_MODE
{
    // Flags for afc_file_open
    AFC_FOPEN_RDONLY   = 0x00000001,    // < r   O_RDONLY
    AFC_FOPEN_RW       = 0x00000002,    // < r+  O_RDWR   | O_CREAT
    AFC_FOPEN_WRONLY   = 0x00000003,    // < w   O_WRONLY | O_CREAT  | O_TRUNC
    AFC_FOPEN_WR       = 0x00000004,    // < w+  O_RDWR   | O_CREAT  | O_TRUNC
    AFC_FOPEN_APPEND   = 0x00000005,    // < a   O_WRONLY | O_APPEND | O_CREAT
    AFC_FOPEN_RDAPPEND = 0x00000006,    // < a+  O_RDWR   | O_APPEND | O_CREAT
};

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCDirectoryOpen)(
    AFCConnection   Connection,
    PCSTR           Path,
    AFCDirectory*   Directory
);

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCDirectoryRead)(
    AFCConnection   Connection,
    AFCDirectory*   Directory,
    PCSTR*          DirectoryEntry
);

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCDirectoryClose)(
    AFCConnection   Connection,
    AFCDirectory*   Directory
);

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCRemovePath)(
    AFCConnection   Connection,
    PCSTR           DirectoryName
);

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCRenamePath)(
    AFCConnection   Connection,
    PCSTR           OldPath,
    PCSTR           NewPath
);

typedef struct
{
    PVOID       What[3];
    CFArrayRef  Array;
    ULONG       NumberOfKeys;

} AFCDictionary, *PAFCDictionary;

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCFileInfoOpen)(
    AFCConnection   Connection,
    PCSTR           Path,
    PAFCDictionary* Info
);

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCFileRefOpen)(
    AFCConnection   Connection,
    PCSTR           Path,
    AFC_FILE_MODE   Mode,
    ULONG           Timeout,
    AFCFileRef*     Handle
);

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCFileRefRead)(
    AFCConnection   Connection,
    AFCFileRef      File,
    PVOID           Buffer,
    PULONG          Length
);

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCFileRefWrite)(
    AFCConnection   Connection,
    AFCFileRef      File,
    PVOID           Buffer,
    ULONG           Length
);

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCFileRefTell)(
    AFCConnection   Connection,
    AFCFileRef      File,
    PULONG64        Offset
);

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCFileRefSeek)(
    AFCConnection   Connection,
    AFCFileRef      File,
    PULONG64        Offset
);

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCFileRefClose)(
    AFCConnection   Connection,
    AFCFileRef      Handle
);

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCSendData)(
    AFCConnection   Connection,
    PVOID           Buffer,
    LONG            Length
);

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCReadData)(
    AFCConnection   Connection,
    PVOID           Buffer,
    LONG            Length
);

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCConnectionOpen)(
    SOCKET          ServiceSocket,
    ULONG           Timeout,
    AFCConnection*  Connection
);

DECL_SELECTANY
AFCConnection
(CDECL
*AFCConnectionCreate)(
    CFAllocatorRef  Allocator,
    SOCKET          ServiceSocket,
    PVOID           Unknown1,
    PVOID           Unknown2,
    ULONG           Timeout
);

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCConnectionSetSecureContext)(
    AFCConnection   Connection,
    PVOID           Context
);

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCConnectionClose)(
    AFCConnection Connection
);


inline NTSTATUS Initialize()
{
    // SetDllDirectoryW(MOBILE_DEVICE_SUPPORT);

    PVOID Module = LoadDll(L"iTunesMobileDevice.dll");

    LOAD_INTERFACE(AFCConnectionOpen);
    LOAD_INTERFACE(AFCConnectionCreate);
    LOAD_INTERFACE(AFCConnectionSetSecureContext);
    LOAD_INTERFACE(AFCConnectionClose);

    LOAD_INTERFACE(AFCDirectoryOpen);
    LOAD_INTERFACE(AFCDirectoryRead);
    LOAD_INTERFACE(AFCDirectoryClose);

    LOAD_INTERFACE(AFCRemovePath);
    LOAD_INTERFACE(AFCRenamePath);

    LOAD_INTERFACE(AFCFileInfoOpen);

    LOAD_INTERFACE(AFCFileRefOpen);
    LOAD_INTERFACE(AFCFileRefRead);
    LOAD_INTERFACE(AFCFileRefWrite);
    LOAD_INTERFACE(AFCFileRefTell);
    LOAD_INTERFACE(AFCFileRefClose);

    LOAD_INTERFACE(AFCSendData);
    LOAD_INTERFACE(AFCReadData);

    return STATUS_SUCCESS;
}

ML_NAMESPACE_END_(AFC);
