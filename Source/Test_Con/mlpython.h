#ifndef _MLPYTHON_H_13f13917_f5da_49af_b443_052ccfc01ea9_
#define _MLPYTHON_H_13f13917_f5da_49af_b443_052ccfc01ea9_

/*++

    linker option:
        /DELAYLOAD:python34.dll

--*/

#include "ml.h"
#include <PythonHelper/PythonHelper.h>

#define PYTHON_DLL              L"python34.dll"
#define PYTHON_PACKAGE_PATH     L"python\\"

typedef LONG PYSTATUS;
#define PY_SUCCESS NT_SUCCESS
#define PY_FAILED NT_FAILED

#define PYCALL CDECL

#define PYCTOR INT (PYCALL*)


typedef enum
{
    PyStatusFirst = DEFINE_NTSTATUS(STATUS_SEVERITY_ERROR, 0x100),

    PYSTATUS_CREATE_MODULE_FAILED,

    PyStatusLast,
};


template<typename NATIVE_TYPE>
struct PyTypeConverter;

template<typename T>
struct PyFunctionTraits
{
    static const ULONG_PTR NumberOfArguments = ml::Function<T>::NumberOfArguments;
    typedef typename ml::Function<T>::RET_TYPE RET_TYPE;

    template<typename R, typename... ARGS>
    static PyObject* CallRoutine(R(*func)(ARGS...), PyObject *args)
    {
        func(sizeof...(ARGS));
        Py_RETURN_NONE;
    }
};


template<typename T>
struct PyStaticFunctionHelper : public PyObjectBase
{
    typedef ml::String String;
    typedef PyStaticFunctionHelper<T> SELF;

    //T *object;
    T func;

    PyStaticFunctionHelper()
    {
        func = nullptr;
    }

    template<typename T>
    struct CtorHelper;

    template<typename R, typename... ARGS>
    struct CtorHelper<R (PYCALL*)(ARGS...)>
    {
        static INT PYCALL InitObject(SELF *self, PyObject *args, PyObject *kwargs)
        {
            new (self) PyStaticFunctionHelper<T>();
            *(PVOID *)&self->func = (PVOID)PyLong_AsUnsignedLongLong(PyTuple_GetItem(args, 0));
            return 0;
        }
    };

    template<typename R, typename... ARGS>
    struct CtorHelper<R PYCALL(ARGS...)>
    {
        static INT PYCALL InitObject(SELF *self, PyObject *args, PyObject *kwargs)
        {
            new (self)PyStaticFunctionHelper<T>();
            *(PVOID *)&self->func = (PVOID)PyLong_AsUnsignedLongLong(PyTuple_GetItem(args, 0));
            return 0;
        }
    };

    static PyObject* PYCALL CallMethod(SELF *self, PyObject *args)
    {
        return self->CallMethodImpl(args);
    }

    PyObject* CallMethodImpl(PyObject *args)
    {
        if (PyTuple_GET_SIZE(args) != PyFunctionTraits<T>::NumberOfArguments)
        {
            PyErr_SetString(
                PyExc_TypeError,
                String::Format(
                    L"function takes %d argument%s, but %d given",
                    PyFunctionTraits<T>::NumberOfArguments,
                    PyFunctionTraits<T>::NumberOfArguments > 1 ? L"s" : L"",
                    PyTuple_GET_SIZE(args)
                )
                .Encode(CP_UTF8)
            );

            return nullptr;
        }

        PrintConsole(L"%S\n", __FUNCTION__);

        return PyFunctionTraits<T>::CallRoutine(this->func, args);
    }

    static PyObject* PYCALL AllocObject(PyTypeObject *type, PyObject *args, PyObject *kwargs)
    {
        return type->tp_alloc(type, 0);
    }

    static VOID PYCALL FreeObject(SELF *self)
    {
        self->ob_base.ob_type->tp_free((PyObject*)self);
    }
};

class MlPython
{
protected:
    typedef ml::String String;
    typedef PCSTR PY_FUNCTION_NAME;
    typedef PCSTR PY_DOC_STRING;
    typedef PCSTR PY_MODULE_NAME;

    struct PY_STATIC_FUNCTION
    {
        ULONG_PTR   ArgsCount;
        ULONG_PTR   TypeSize;
        PyCFunction Native;
        initproc    ctor;
        destructor  dtor;
        newfunc     alloc;
        PVOID       Address;
        String      Name;
        String      Doc;
    };

    GrowableArray<PY_STATIC_FUNCTION> RegisteredFunctions;

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

    MlPython(const MlPython&) = delete;
    MlPython& operator=(const MlPython&) = delete;

    PYSTATUS RunString(PCSTR code)
    {
        PyRun_SimpleString(code);
        return STATUS_SUCCESS;
    }

    PYSTATUS RunString(const String& code)
    {
        PyRun_SimpleString(code.Encode(CP_UTF8));
        return STATUS_SUCCESS;
    }

    template<class T>
    NoInline MlPython& Register(T func, const String& FunctionName, const String& Doc = L"")
    {
        PY_STATIC_FUNCTION f;

        *(T *)&f.Address = func;

        f.Name      = FunctionName;
        f.Doc       = Doc;
        f.ArgsCount = PyFunctionTraits<T>::NumberOfArguments;
        f.TypeSize  = sizeof(PyStaticFunctionHelper<T>);
        f.Native    = (PyCFunction)PyStaticFunctionHelper<T>::CallMethod;
        f.dtor      = (destructor)PyStaticFunctionHelper<T>::FreeObject;
        f.ctor      = (initproc)PyStaticFunctionHelper<T>::CtorHelper<PYCTOR(ULONG64)>::InitObject;
        f.alloc      = PyStaticFunctionHelper<T>::AllocObject;

        this->RegisteredFunctions.Add(f);

        return *this;
    }

    NoInline PYSTATUS InitModule(const String& ModuleName, const String& Doc = L"")
    {
        PyObject* Module;
        auto& ModuleNameAnsi = ModuleName.Encode(CP_UTF8);
        auto& DocAnsi = Doc.Encode(CP_UTF8);

        PyModuleDef ModuleDef =
        {
            PyModuleDef_HEAD_INIT,
            ModuleNameAnsi,
            DocAnsi,
            -1,
        };

        //Module = PyModule_Create(&ModuleDef);
        Module = PyImport_AddModule(ModuleNameAnsi);
        if (Module == nullptr)
            return PYSTATUS_CREATE_MODULE_FAILED;

        FAIL_RETURN(this->InitFunctions(Module, ModuleName, Doc));

        return STATUS_SUCCESS;
    }

protected:
    PYSTATUS InitFunctions(PyObject* Module, const String& ModuleName, const String& Doc = L"")
    {
        for (auto &func : this->RegisteredFunctions)
        {
            auto &name = func.Name.Encode(CP_UTF8);
            auto &type = (func.Name + L"_wrapclass").Encode(CP_UTF8);

            BOOL Success;
            PyObject *args, *obj, *method;

            args    = nullptr;
            obj     = nullptr;
            method  = nullptr;
            Success = FALSE;

            PyMethodDef localmethods[] =
            {
                PY_ADD_METHOD(name, func.Native, METH_VARARGS | METH_KEYWORDS),
                PY_ADD_METHOD_END
            };

            PyMethodDef *methods = new PyMethodDef[countof(localmethods)];
            if (methods != nullptr)
            {
                CopyStruct(methods, localmethods, sizeof(localmethods));
            }

            PyTypeObject *methoswrapclass = new PyTypeObject
            {
                PyVarObject_HEAD_INIT(&PyType_Type, 0)
                type,                                               /* tp_name */
                func.TypeSize,                                      /* tp_size */
                0,                                                  /* tp_itemsize */
                func.dtor,                                          /* tp_dealloc */
                0,                                                  /* tp_print */
                0,                                                  /* tp_getattr */
                0,                                                  /* tp_setattr */
                0,                                                  /* tp_reserved */
                0,                                                  /* tp_repr */
                0,                                                  /* tp_as_number */
                0,                                                  /* tp_as_sequence */
                0,                                                  /* tp_as_mapping */
                0,                                                  /* tp_hash*/
                0,                                                  /* tp_call*/
                0,                                                  /* tp_str */
                PyObject_GenericGetAttr,                            /* tp_getattro */
                0,                                                  /* tp_setattro */
                0,                                                  /* tp_as_buffer */
                Py_TPFLAGS_DEFAULT,                                 /* tp_flags */
                "",                                                 /* tp_doc */
                0,                                                  /* tp_traverse */
                0,                                                  /* tp_clear */
                0,                                                  /* tp_richcompare */
                0,                                                  /* tp_weaklistoffset */
                0,                                                  /* tp_iter */
                0,                                                  /* tp_iternext */
                methods,                                            /* tp_methods */
                0,                                                  /* tp_members */
                0,                                                  /* tp_getset */
                &PyBaseObject_Type,                                 /* tp_base */
                0,                                                  /* tp_dict */
                0,                                                  /* tp_descr_get */
                0,                                                  /* tp_descr_set */
                0,                                                  /* tp_dictoffset */
                func.ctor,                                          /* tp_init */
                0,                                                  /* tp_alloc */
                func.alloc,                                         /* tp_new */
                nullptr,                                            /* tp_free */
            };

            LOOP_ONCE
            {
                if (methods == nullptr || methoswrapclass == nullptr)
                    break;

                if (PyType_Ready(methoswrapclass) != 0)
                    break;

                PyAddRef((PyObject *)methoswrapclass);
                if (PyModule_AddObject(Module, methoswrapclass->tp_name, (PyObject *)methoswrapclass) != 0)
                    break;

                args = Py_BuildValue("(K)", (ULONG64)func.Address);
                if (args == nullptr)
                    break;

                obj = PyObject_CallObject((PyObject *)methoswrapclass, args);
                if (obj == nullptr)
                    break;

                method = PyObject_GetAttrString(obj, name);
                if (method == nullptr)
                    break;

                if (PyObject_SetAttrString(Module, name, method) != 0)
                    break;

                Success = TRUE;
            }

            PyRelease(args);
            PyRelease(method);
            PyRelease(obj);

            if (Success == FALSE)
            {
                delete[] methods;
                delete methoswrapclass;
            }
        }

        this->RegisteredFunctions.RemoveAll();

        return STATUS_SUCCESS;
    }

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
};

#endif // _MLPYTHON_H_13f13917_f5da_49af_b443_052ccfc01ea9_
