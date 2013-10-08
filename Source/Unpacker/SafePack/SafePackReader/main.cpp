#pragma comment(linker, "/ENTRY:main")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")

#include "MyLibrary.cpp"
#include "SafePackReader.h"

class SafePackReader : public SafePackReaderImpl<SafePackReader>
{
    ;
};

ForceInline Void main2(LONG_PTR argc, PWSTR *argv)
{
    if (--argc ==0)
        return;

    ++argv;

    SafePackReader spr;

    FOR_EACH(argv, argv, argc)
    {
        PSAFE_PACK_READER_ENTRY ent;

        spr.Open(*argv);
        ent = spr.Lookup(L"Vanguard Princess/Vanguard Princess.152.bmp");
        PrintConsoleW(L"%s\n", ent->FileName);
    }
}

int __cdecl main(LONG_PTR argc, PWSTR *argv)
{
    getargsW(&argc, &argv);
    main2(argc, argv);
    ReleaseArgv(argv);
    Ps::ExitProcess(0);
}
