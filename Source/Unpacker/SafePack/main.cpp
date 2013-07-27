#pragma comment(linker, "/ENTRY:main")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker, "/SECTION:.Amano,ERW /MERGE:.text=.Amano")

#include "SafePacker.h"
#include "MyLibrary.cpp"

ML_OVERLOAD_NEW

class SafePacker : public SafePackerImpl<SafePacker>
{
    ;
};

ForceInline Void main2(LONG_PTR argc, PWSTR *argv)
{
/*
    PRTL_USER_PROCESS_PARAMETERS UserProcessParameter;

    UserProcessParameter = (PRTL_USER_PROCESS_PARAMETERS)AllocateMemory(CurrentPeb()->ProcessParameters->MaximumLength + 4);
    CopyMemory(UserProcessParameter, CurrentPeb()->ProcessParameters, CurrentPeb()->ProcessParameters->Length);
    *(PULONG_PTR)PtrAdd(UserProcessParameter, UserProcessParameter->MaximumLength - 4) = -1;
    CurrentPeb()->ProcessParameters = UserProcessParameter;
*/
    if (--argc == 0)
        return;

    SafePacker sp;

    do
    {
        sp.Auto(*++argv);

    } while (--argc);
}

int __cdecl main(LONG_PTR argc, PWSTR *argv)
{
    getargsW(&argc, &argv);
    main2(argc, argv);
    ReleaseArgv(argv);
    Ps::ExitProcess(0);
}
