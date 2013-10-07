/* Minimal main program -- everything is loaded from the library */

#if defined(__cplusplus)
extern "C" {
#endif

#include "Python.h"
#include <Windows.h>

#if defined(__cplusplus)
}
#endif
//#include <locale.h>

#ifdef __FreeBSD__
#include <floatingpoint.h>
#endif

//#include "../Modules/getbuildinfo.c"

#ifdef MS_WINDOWS

#pragma comment(linker, "/ENTRY:main")

#define ML_DISABLE_THIRD_LIB 1

#include "MyLibrary.cpp"

VOID AppendPackage()
{
    PLDR_MODULE Self;
    UNICODE_STRING SelfPath;

    static WCHAR PythonZip[] = L"python.zip";

    ml::MlInitialize();

    //Py_IgnoreEnvironmentFlag = TRUE;
    //Py_NoSiteFlag = TRUE;
    Py_DontWriteBytecodeFlag = TRUE;
    //Py_NoUserSiteDirectory = TRUE;

    Self = FindLdrModuleByHandle(nullptr);

    SelfPath = Self->FullDllName;
    SelfPath.Length -= Self->BaseDllName.Length;

    Py_SetPath(ml::String::Format(
        L"%wZ;%wZ%s;%wZ%s\\site-packages;%wZlib;%wZDLLs;%wZUserSite",
        &SelfPath,                      // exe path
        &SelfPath, PythonZip,           // ./python.zip
        &SelfPath, PythonZip,           // ./python.zip/site-packages
        &SelfPath,                      // ./lib
        &SelfPath,                      // ./DLLs
        &SelfPath                       // ./UserSite
    ));

    ml::String      PathEnv, UserSite;
    PWSTR           EnvBuffer;
    ULONG_PTR       Length;
    UNICODE_STRING  Env;

    Length = CurrentPeb()->ProcessParameters->EnvironmentSize;
    EnvBuffer = (PWSTR)AllocStack(Length);
    RtlInitEmptyString(&Env, EnvBuffer, Length);

    RtlExpandEnvironmentStrings_U(nullptr, &USTR(L"%Path%"), &Env, nullptr);

    UserSite = SelfPath;
    UserSite += L"UserSite";
    PathEnv = Env;
    PathEnv += ';';

    EnumDirectoryFiles(
        nullptr, L"*.*", 0, UserSite, nullptr,
        [] (PVOID Buffer, PWIN32_FIND_DATAW FindData, ULONG_PTR Context) -> LONG
        {
            ml::String *PathEnv = (ml::String *)Context;

            if (FLAG_OFF(FindData->dwFileAttributes, FILE_ATTRIBUTE_DIRECTORY))
                return 0;

            (*PathEnv) += FindData->cFileName;
            (*PathEnv) += ';';

            return 0;
        },
        (ULONG_PTR)&PathEnv,
        EDF_PROCDIR | EDF_BEFORE
    );

    RtlSetEnvironmentVariable(nullptr, &USTR(L"Path"), PathEnv);
}

ForceInline int main2(LONG_PTR argc, PWSTR *argv)
{
    AppendPackage();
    return Py_Main(argc, argv);
}

int __cdecl main(LONG_PTR argc, PWSTR *argv)
{
    getargsW(&argc, &argv);
    main2(argc, argv);
    ReleaseArgv(argv);
    Ps::ExitProcess(0);
}

#else

int
main(int argc, char **argv)
{
    wchar_t **argv_copy;
    /* We need a second copy, as Python might modify the first one. */
    wchar_t **argv_copy2;
    int i, res;
    char *oldloc;
#ifdef __FreeBSD__
    fp_except_t m;
#endif

    argv_copy = (wchar_t **)PyMem_RawMalloc(sizeof(wchar_t*) * (argc+1));
    argv_copy2 = (wchar_t **)PyMem_RawMalloc(sizeof(wchar_t*) * (argc+1));
    if (!argv_copy || !argv_copy2) {
        fprintf(stderr, "out of memory\n");
        return 1;
    }

    /* 754 requires that FP exceptions run in "no stop" mode by default,
     * and until C vendors implement C99's ways to control FP exceptions,
     * Python requires non-stop mode.  Alas, some platforms enable FP
     * exceptions by default.  Here we disable them.
     */
#ifdef __FreeBSD__
    m = fpgetmask();
    fpsetmask(m & ~FP_X_OFL);
#endif

    oldloc = _PyMem_RawStrdup(setlocale(LC_ALL, NULL));
    if (!oldloc) {
        fprintf(stderr, "out of memory\n");
        return 1;
    }

    setlocale(LC_ALL, "");
    for (i = 0; i < argc; i++) {
        argv_copy[i] = _Py_char2wchar(argv[i], NULL);
        if (!argv_copy[i]) {
            PyMem_RawFree(oldloc);
            fprintf(stderr, "Fatal Python error: "
                            "unable to decode the command line argument #%i\n",
                            i + 1);
            return 1;
        }
        argv_copy2[i] = argv_copy[i];
    }
    argv_copy2[argc] = argv_copy[argc] = NULL;

    setlocale(LC_ALL, oldloc);
    PyMem_RawFree(oldloc);
    res = Py_Main(argc, argv_copy);
    for (i = 0; i < argc; i++) {
        PyMem_RawFree(argv_copy2[i]);
    }
    PyMem_RawFree(argv_copy);
    PyMem_RawFree(argv_copy2);
    return res;
}
#endif
