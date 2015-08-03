ML_NAMESPACE_BEGIN(AFC);

enum AFC_ERROR_CODE
{
    kAFCSuccess              = 0x00000000,
    kAFCUndefinedError       = 0x00000001,
    kAFCBadHeaderError       = 0x00000002,
    kAFCNoResourcesError     = 0x00000003,
    kAFCReadError            = 0x00000004,
    kAFCWriteError           = 0x00000005,
    kAFCUnknownPacketError   = 0x00000006,
    kAFCInvalidArgumentError = 0x00000007,
    kAFCNotFoundError        = 0x00000008,
    kAFCIsDirectoryError     = 0x00000009,
    kAFCPermissionError      = 0x0000000A,
    kAFCNotConnectedError    = 0x0000000B,
    kAFCTimeOutError         = 0x0000000C,
    kAFCOverrunError         = 0x0000000D,
    kAFCEOFError             = 0x0000000E,
    kAFCUnsupportedError     = 0x0000000F,
    kAFCFileExistsError      = 0x00000010,
    kAFCBusyError            = 0x00000011,
    kAFCNoSpaceError         = 0x00000012,
    kAFCWouldBlockError      = 0x00000013,
    kAFCInputOutputError     = 0x00000014,
    kAFCInterruptedError     = 0x00000015,
    kAFCInProgressError      = 0x00000016,
    kAFCInternalError        = 0x00000017,
};

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
PCSTR
(CDECL
*AFCErrorString)(
    LONG_PTR AfcErrorCode
);

/* Opens a directory on the iPhone. Pass in a pointer in dir to be filled in.
* Note that this normally only accesses the iTunes sandbox/partition as the
* root, which is /var/root/Media. Pathnames are specified with '/' delimiters
* as in Unix style. Use UTF-8 to specify non-ASCII symbols in path.
*
* Returns:
*      MDERR_OK                if successful
*/

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
*AFCDirectoryCreate)(
    AFCConnection   Connection,
    PCSTR           Path
);


/* Acquires the next entry in a directory previously opened with
* AFCDirectoryOpen(). When dirent is filled with a NULL value, then the end
* of the directory has been reached. '.' and '..' will be returned as the
* first two entries in each directory except the root; you may want to skip
* over them.
*
* Returns:
*      MDERR_OK                if successful, even if no entries remain
*/

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCDirectoryRead)(
    AFCConnection   Connection,
    AFCDirectory    Directory,
    PCSTR*          DirectoryEntry
);

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCDirectoryClose)(
    AFCConnection   Connection,
    AFCDirectory    Directory
);

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCRemovePath)(
    AFCConnection   Connection,
    PCSTR           Path
);

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCRenamePath)(
    AFCConnection   Connection,
    PCSTR           OldPath,
    PCSTR           NewPath
);


/* Creates symbolic or hard link
     * linktype - int64: 1 means hard link, 2 - soft (symbolic) link
     * target - absolute or relative path to link target
     * linkname - absolute path where to create new link
*/

enum
{
    AFC_LINK_HARD_LINK  = 1,
    AFC_LINK_SOFT_LINK  = 2,
};

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCLinkPath)(
    AFCConnection   Connection,
    LONG64          LinkType,
    PCSTR           Target,
    PCSTR           Link
);

typedef struct
{
    PVOID       What[3];
    CFArrayRef  Array;
    ULONG       NumberOfKeys;

} AFCDictionary, *PAFCDictionary;


/* Opens dictionary describing specified file or directory (iTunes below 8.2 allowed using AFCGetFileInfo
 to get the same information)
*/

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCFileInfoOpen)(
    AFCConnection   Connection,
    PCSTR           Path,
    PAFCDictionary* Info
);


/* Reads next entry from dictionary. When last entry is read, function returns NULL in key argument
 Possible keys:
   "st_size":     val - size in bytes
   "st_blocks":   val - size in blocks
   "st_nlink":    val - number of hardlinks
   "st_ifmt":     val - "S_IFDIR" for folders
                      "S_IFLNK" for symlinks
   "LinkTarget":  val - path to symlink target
*/

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCKeyValueRead)(
    PAFCDictionary  Info,
    PCSTR*          Key,
    PCSTR*          Value
);

/*
    Closes dictionary
*/

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCKeyValueClose)(
    PAFCDictionary Info
);


/* Opens file for reading or writing without locking it in any way. afc_file_ref should not be shared between threads -
     * opening file in one thread and closing it in another will lead to possible crash.
* path - UTF-8 encoded absolute path to file
* mode 1 = read, mode 2 = write, mode 3 = read/write
* ref - receives file handle
*/

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCFileRefOpen)(
    AFCConnection   Connection,
    PCSTR           Path,
    ULONG64         Mode,
    AFCFileRef*     Handle
);

/*
    Reads specified amount (len) of bytes from file into buf.
    Puts actual count of read bytes into len on return
*/

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCFileRefRead)(
    AFCConnection   Connection,
    AFCFileRef      File,
    PVOID           Buffer,
    PULONG_PTR      Length
);

/*
    Writes specified amount (len) of bytes from buf into file.
*/

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCFileRefWrite)(
    AFCConnection   Connection,
    AFCFileRef      File,
    PVOID           Buffer,
    ULONG64         Length
);

/*
    Gets the current position of a file pointer into offset argument.
*/

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCFileRefTell)(
    AFCConnection   Connection,
    AFCFileRef      File,
    PULONG64        Offset
);


/* Moves the file pointer to a specified location.
* offset - Number of bytes from origin (int64)
* origin - 0 = from beginning, 1 = from current position, 2 = from end
*/

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCFileRefSeek)(
    AFCConnection   Connection,
    AFCFileRef      File,
    ULONG64         Offset,
    LONG            Origin
);


/*
    Truncates a file at the specified offset
*/
DECL_SELECTANY
NTSTATUS
(CDECL
*AFCFileRefSetFileSize)(
    AFCConnection   Connection,
    AFCFileRef      Handle,
    ULONG64         Size
);


/** Lock operation flags */
enum AFC_LOCK_OPERATION
{
    AFC_LOCK_SHARED    = 1 | 4, /**< shared lock */
    AFC_LOCK_EXCLUSIVE = 2 | 4, /**< exclusive lock */
    AFC_LOCK_UNLOCK    = 8 | 4, /**< unlock */
};

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCFileRefLock)(
    AFCConnection   Connection,
    AFCFileRef      Handle,
    BOOLEAN         ExclusiveLock
);

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCFileRefUnlock)(
    AFCConnection   Connection,
    AFCFileRef      Handle
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
    ULONG_PTR       Length
);

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCReadData)(
    AFCConnection   Connection,
    PVOID           Buffer,
    ULONG_PTR       Length
);

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCReadPacket)(
    AFCConnection   Connection,
    PBYTE*          PacketHeader,
    PBYTE*          PacketBody,
    PULONG          PacketSize
);


/* Opens an Apple File Connection. You must start the appropriate service
* first with AMDeviceStartService(). In iTunes, io_timeout is 0.
*
* Returns:
*      MDERR_OK                if successful
*      MDERR_AFC_OUT_OF_MEMORY if malloc() failed
*/

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
    ULONG_PTR       Timeout
);


/* Returns the context field of the given AFC connection. */

DECL_SELECTANY
PVOID
(CDECL
*AFCConnectionGetContext)(
    AFCConnection Connection
);

DECL_SELECTANY
VOID
(CDECL
*AFCConnectionSetContext)(
    AFCConnection   Connection,
    PVOID           Context
);

DECL_SELECTANY
PVOID
(CDECL
*AFCConnectionGetSecureContext)(
    AFCConnection Connection
);

DECL_SELECTANY
VOID
(CDECL
*AFCConnectionSetSecureContext)(
    AFCConnection   Connection,
    PVOID           Context
);


/* Closes the given AFC connection. */

DECL_SELECTANY
NTSTATUS
(CDECL
*AFCConnectionClose)(
    AFCConnection Connection
);


inline NTSTATUS Initialize()
{
    PVOID Module = LoadDll(MOBILE_DEVICE_DLL);

    LOAD_INTERFACE(AFCErrorString);

    LOAD_INTERFACE(AFCConnectionOpen);
    LOAD_INTERFACE(AFCConnectionCreate);
    LOAD_INTERFACE(AFCConnectionGetContext);
    LOAD_INTERFACE(AFCConnectionSetContext);
    LOAD_INTERFACE(AFCConnectionGetSecureContext);
    LOAD_INTERFACE(AFCConnectionSetSecureContext);
    LOAD_INTERFACE(AFCConnectionClose);

    LOAD_INTERFACE(AFCDirectoryOpen);
    LOAD_INTERFACE(AFCDirectoryCreate);
    LOAD_INTERFACE(AFCDirectoryRead);
    LOAD_INTERFACE(AFCDirectoryClose);

    LOAD_INTERFACE(AFCRemovePath);
    LOAD_INTERFACE(AFCRenamePath);
    LOAD_INTERFACE(AFCLinkPath);

    LOAD_INTERFACE(AFCFileInfoOpen);
    LOAD_INTERFACE(AFCKeyValueRead);
    LOAD_INTERFACE(AFCKeyValueClose);

    LOAD_INTERFACE(AFCFileRefOpen);
    LOAD_INTERFACE(AFCFileRefRead);
    LOAD_INTERFACE(AFCFileRefWrite);
    LOAD_INTERFACE(AFCFileRefTell);
    LOAD_INTERFACE(AFCFileRefSetFileSize);
    LOAD_INTERFACE(AFCFileRefLock);
    LOAD_INTERFACE(AFCFileRefUnlock);
    LOAD_INTERFACE(AFCFileRefClose);

    LOAD_INTERFACE(AFCSendData);
    LOAD_INTERFACE(AFCReadData);

    return STATUS_SUCCESS;
}

ML_NAMESPACE_END_(AFC);
