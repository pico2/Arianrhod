ML_NAMESPACE_BEGIN(AFC);

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
    *AFCFileRefRead)(
        AFCConnection   Connection,
        AFCFileRef      File,
        PVOID           Buffer,
        PULONG          Length
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
    LONG
    (CDECL
    *AFCSendData)(
        AFCConnection   Connection,
        PVOID           Buffer,
        LONG            Length
    );

    DECL_SELECTANY
    LONG
    (CDECL
    *AFCReadData)(
        AFCConnection   Connection,
        PVOID           Buffer,
        LONG            Length
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

        LOAD_INTERFACE(AFCDirectoryOpen);
        LOAD_INTERFACE(AFCDirectoryRead);
        LOAD_INTERFACE(AFCDirectoryClose);
        LOAD_INTERFACE(AFCRemovePath);
        LOAD_INTERFACE(AFCRenamePath);
        LOAD_INTERFACE(AFCFileInfoOpen);
        LOAD_INTERFACE(AFCFileRefRead);
        LOAD_INTERFACE(AFCFileRefTell);
        LOAD_INTERFACE(AFCSendData);
        LOAD_INTERFACE(AFCReadData);
        LOAD_INTERFACE(AFCConnectionClose);

        return STATUS_SUCCESS;
    }

ML_NAMESPACE_END_(AFC);
