#pragma comment(linker, "/ENTRY:main")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text /MERGE:.text1=.text /SECTION:.idata,ERW")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")

#include "ml.cpp"
#include "../Hooker/PyHooker.cpp"

ML_OVERLOAD_NEW

VOID test(PyHooker *hooker)
{
    hooker->Initialize();
    hooker->LoadPyFile();

    //hooker->PyHookFunction(NtClose, 0);

    for (ULONG_PTR i = 1; i != 0; --i)
        NtClose(0);
}

ForceInline VOID main2(LONG_PTR argc, PWSTR *argv)
{
    PyHooker *hooker;

    ml::MlInitialize();

    hooker = PyHooker::GetInstance();

    ULONG64 beg, end;

    beg = NtGetTickCount();

    test(hooker);

    end = NtGetTickCount();

    printf("%fs\n", (end - beg) / 1024.f);

    hooker->Release();
}

int __cdecl main(LONG_PTR argc, PWSTR *argv)
{
    getargsW(&argc, &argv);
    main2(argc, argv);
    ReleaseArgv(argv);
    Ps::ExitProcess(0);
}
