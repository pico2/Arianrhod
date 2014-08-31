#ifndef _MLPYTHON_H_13f13917_f5da_49af_b443_052ccfc01ea9_
#define _MLPYTHON_H_13f13917_f5da_49af_b443_052ccfc01ea9_

/*++


--*/

#include "ml.h"
#include <PythonHelper/PythonHelper.h>

#define PYTHON_DLL              L"python34.dll"
#define PYTHON_PACKAGE_PATH     L"python\\"

typedef LONG PYSTATUS;


template<typename T>
struct FunctionTraits
{
    static const ULONG_PTR NumberOfArguments = ml::Function<T>::NumberOfArguments;
};


class MlPython
{
protected:
    typedef ml::String String;
    typedef PCSTR PY_FUNCTION_NAME;
    typedef PCSTR PY_DOC_STRING;

    typedef struct
    {
        ULONG_PTR   NumberOfArguments;
        PyCFunction NativeFunction;

    } PY_STATIC_METHOD;

public:
    MlPython()
    {
        ml::MlInitialize();

        if (Py_IsInitialized() == FALSE)
        {
            InitializePackage();
            Py_Initialize();
        }
    }

    ~MlPython()
    {
        ;
    }

    PYSTATUS RunString(PCSTR code)
    {
        PyRun_SimpleString(code);
        return STATUS_SUCCESS;
    }

    PYSTATUS RunString(const String& code)
    {
        PyRun_SimpleString(code.Encode(CP_ACP));
        return STATUS_SUCCESS;
    }

    template<class T>
    MlPython& Register(T func, PY_FUNCTION_NAME FunctionName, PY_DOC_STRING Doc = "")
    {
        return *this;
    }

    PYSTATUS InitModule()
    {
        GrowableArray<PyMethodDef> RegisteredMethods;
    }

protected:
    PYSTATUS InitializePackage()
    {
        PLDR_MODULE Self;
        UNICODE_STRING SelfPath;

        static WCHAR PythonZip[] = L"python.zip";

        //Py_IgnoreEnvironmentFlag = TRUE;
        //Py_NoSiteFlag = TRUE;
        Py_DontWriteBytecodeFlag = TRUE;
        //Py_NoUserSiteDirectory = TRUE;

        Self = FindLdrModuleByName(&USTR(PYTHON_DLL));
        if (Self == nullptr)
            return STATUS_DLL_NOT_FOUND;

        SelfPath = Self->FullDllName;
        SelfPath.Length -= Self->BaseDllName.Length;

        Py_SetPath(String::Format(
            L"%wZ%s;%wZ%s%s;%wZ%s%s\\site-packages;%wZ%slib;%wZ%sDLLs;%wZ%sUserSite",
            &SelfPath, PYTHON_PACKAGE_PATH,                      // exe path
            &SelfPath, PYTHON_PACKAGE_PATH, PythonZip,           // ./python.zip
            &SelfPath, PYTHON_PACKAGE_PATH, PythonZip,           // ./python.zip/site-packages
            &SelfPath, PYTHON_PACKAGE_PATH,                      // ./lib
            &SelfPath, PYTHON_PACKAGE_PATH,                      // ./DLLs
            &SelfPath, PYTHON_PACKAGE_PATH                       // ./UserSite
        ));

        String          PathEnv, UserSite;
        PWSTR           EnvBuffer;
        ULONG           Length;
        UNICODE_STRING  Path;

        RtlInitEmptyString(&Path);
        RtlExpandEnvironmentStrings_U(nullptr, &USTR(L"%Path%"), &Path, &Length);

        EnvBuffer = (PWSTR)AllocStack(Length);
        RtlInitEmptyString(&Path, EnvBuffer, Length);

        RtlExpandEnvironmentStrings_U(nullptr, &USTR(L"%Path%"), &Path, nullptr);

        UserSite = SelfPath;
        UserSite += PYTHON_PACKAGE_PATH;
        UserSite + L"UserSite";

        PathEnv = Path;
        PathEnv += ';';
        PathEnv += SelfPath;
        PathEnv += L"DLLs;";

        EnumDirectoryFiles(
            nullptr, L"*.*", 0, UserSite, nullptr,
            [] (PVOID Buffer, PWIN32_FIND_DATAW FindData, ULONG_PTR Context) -> LONG
            {
                String *PathEnv = (String *)Context;

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

        return STATUS_SUCCESS;
    }

private:
    MlPython(const MlPython&);
    MlPython& operator=(const MlPython&);
};

#endif // _MLPYTHON_H_13f13917_f5da_49af_b443_052ccfc01ea9_
