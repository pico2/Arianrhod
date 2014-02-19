#pragma comment(linker, "/ENTRY:main")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text /MERGE:.text1=.text /SECTION:.idata,ERW")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")

#include "krkr2.h"
#include "zlib/zlib.h"
#include "MyLibrary.cpp"

ForceInline Void main2(LONG_PTR argc, PWSTR *argv)
{
    if (argc == 1)
        return;

    CKrkr2 rs;
    while (--argc)
        rs.Auto(*++argv);
}

int __cdecl main(LONG_PTR argc, PWSTR *argv)
{
    getargsW(&argc, &argv);
    main2(argc, argv);
    ReleaseArgv(argv);
    Ps::ExitProcess(0);
}