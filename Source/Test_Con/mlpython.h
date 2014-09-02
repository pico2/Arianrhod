#ifndef _MLPYTHON_H_13f13917_f5da_49af_b443_052ccfc01ea9_
#define _MLPYTHON_H_13f13917_f5da_49af_b443_052ccfc01ea9_

/*++

    linker option:
        /DELAYLOAD:python34.dll

--*/


//
//                       _oo0oo_
//                      o8888888o
//                      88" . "88
//                      (| -_- |)
//                      0\  =  /0
//                    ___/`---'\___
//                  .' \\|     |// '.
//                 / \\|||  :  |||// \
//                / _||||| -:- |||||- \
//               |   | \\\  -  /// |   |
//               | \_|  ''\---/''  |_/ |
//               \  .-\__  '-'  ___/-. /
//             ___'. .'  /--.--\  `. .'___
//          ."" '<  `.___\_<|>_/___.' >' "".
//         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
//         \  \ `_.   \_ __\ /__ _/   .-` /  /
//     =====`-.____`.___ \_____/___.-`___.-'=====
//                       `=---='
//
//
//     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//               ·ð×æ±£ÓÓ         ÓÀÎÞBUG
//
//
//

#include "ml.h"
#include <PythonHelper/PythonHelper.h>

#define PYTHON_DLL              L"python34.dll"
#define PYTHON_PACKAGE_PATH     L"python\\"

typedef LONG PYSTATUS;
#define PY_SUCCESS NT_SUCCESS
#define PY_FAILED NT_FAILED

#define PYCALL CDECL

#define PYCTOR INT (PYCALL*)

#define WRAP_CLASS_SUFFIX L"_WRAP_CLASS"


typedef enum
{
    PyStatusFirst = DEFINE_NTSTATUS(STATUS_SEVERITY_ERROR, 0x100),

    PYSTATUS_CREATE_MODULE_FAILED,
    PYSTATUS_IMPORT_MODULE_FAILED,
    PYSTATUS_CREATE_UNICODE_FAILED,
    PYSTATUS_CREATE_OBJECT_FAILED,
    PYSTATUS_GET_ATTR_FAILED,
    PYSTATUS_SET_ATTR_FAILED,

    PyStatusLast,
};


//////////////////////////////////////////////////////////////////////////
// type traits
//////////////////////////////////////////////////////////////////////////

template<typename T>
struct PyTypeHelper
{
    typedef T           VALUE_TYPE;
    typedef T&          REF_TYPE;
    typedef const T&    CONST_REF_TYPE;
    VALUE_TYPE          value;
};

template<typename T>
struct PyTypeHelper<T&>
{
    typedef T           VALUE_TYPE;
    typedef T&          REF_TYPE;
    typedef const T&    CONST_REF_TYPE;
    VALUE_TYPE          value;
};

template<typename T>
struct PyTypeHelper<const T&>
{
    typedef T           VALUE_TYPE;
    typedef T&          REF_TYPE;
    typedef const T&    CONST_REF_TYPE;
    VALUE_TYPE          value;
};


//////////////////////////////////////////////////////////////////////////
// type converter
//////////////////////////////////////////////////////////////////////////

template<typename NATIVE_TYPE>
struct PyTypeConverter;

#define PY_INTEGER_CONVERTER_32(type) \
    template<> \
    struct PyTypeConverter<type> \
    { \
        static PyObject* FromNative(type ret) \
        { \
            return PyLong_FromLong((LONG)ret); \
        } \
 \
        static type ToNative(PyObject *obj) \
        { \
            if (obj == nullptr || PyLong_Check(obj) == 0) \
                return type(); \
            return (type)PyLong_AsLong(obj); \
        } \
    };

PY_INTEGER_CONVERTER_32(CHAR);
PY_INTEGER_CONVERTER_32(UCHAR);
PY_INTEGER_CONVERTER_32(SHORT);
PY_INTEGER_CONVERTER_32(USHORT);
PY_INTEGER_CONVERTER_32(INT32);
PY_INTEGER_CONVERTER_32(UINT32);
PY_INTEGER_CONVERTER_32(LONG);
PY_INTEGER_CONVERTER_32(ULONG);


#define PY_INTEGER_CONVERTER_64(type) \
    template<> \
    struct PyTypeConverter<type> \
    { \
        static PyObject* FromNative(type ret) \
        { \
            return PyLong_FromLongLong((LONG64)ret); \
        } \
 \
        static type ToNative(PyObject *obj) \
        { \
            if (obj == nullptr || PyLong_Check(obj) == 0) \
                return type(); \
            return (type)PyLong_AsUnsignedLongLong(obj); \
        } \
    };

PY_INTEGER_CONVERTER_64(LONG64);
PY_INTEGER_CONVERTER_64(ULONG64);


//////////////////////////////////////////////////////////////////////////
// func helper
//////////////////////////////////////////////////////////////////////////

template<typename int>
struct PyCallStaticRoutineHelper
{
    template<typename R, typename FUNC_TYPE, typename ARG1, typename... FUNC_ARGS, typename... EXTRACTED_ARGS>
    ForceInline static R CallStaticRoutine(FUNC_TYPE func, PyObject *args, Py_ssize_t Index, EXTRACTED_ARGS... fargs)
    {
        return PyCallStaticRoutineHelper<sizeof...(FUNC_ARGS)>::CallStaticRoutine<R, FUNC_TYPE, FUNC_ARGS...>(
                   func,
                   args,
                   Index + 1,
                   fargs...,
                   PyTypeConverter<PyTypeHelper<ARG1>::VALUE_TYPE>::ToNative(PyTuple_GetItem(args, Index))
               );
    }
};

template<>
struct PyCallStaticRoutineHelper<0>
{
    template<typename R, typename FUNC_TYPE, typename... EXTRACTED_ARGS>
    ForceInline static R CallStaticRoutine(FUNC_TYPE func, PyObject *args, Py_ssize_t Index, EXTRACTED_ARGS... fargs)
    {
        return func(fargs...);
    }
};

template<typename T>
struct PyFunctionHelper
{
    static const ULONG_PTR NumberOfArguments = ml::Function<T>::NumberOfArguments;
    typedef typename ml::Function<T>::RET_TYPE RET_TYPE;

    template<typename R, typename... ARGS>
    static PyObject* CallRoutine(R(*func)(ARGS...), PyObject * args)
    {
        return PyTypeConverter<R>::FromNative(CallStaticRoutineImpl(func, args));
    }

    template<typename... ARGS>
    static PyObject* CallRoutine(VOID(*func)(ARGS...), PyObject * args)
    {
        CallStaticRoutineImpl(func, args);
        Py_RETURN_NONE;
    }

    template<typename R, typename... ARGS>
    static R CallStaticRoutineImpl(R(*func)(ARGS...), PyObject *args)
    {
        return PyCallStaticRoutineHelper<sizeof...(ARGS)>::CallStaticRoutine<R, TYPE_OF(func), ARGS...>(func, args, 0);
    }
};

template<typename T>
struct PyStaticFunctionHelper : public PyObjectBase
{
    typedef ml::String String;
    typedef PyStaticFunctionHelper<T> SELF;

    T func;

    PyStaticFunctionHelper()
    {
        func = nullptr;
    }

    static INT PYCALL InitObject(SELF *self, PyObject *args, PyObject *kwargs)
    {
        new (self)PyStaticFunctionHelper<T>();
        *(PVOID *)&self->func = (PVOID)PyLong_AsUnsignedLongLong(PyTuple_GetItem(args, 0));
        return 0;
    }

    static PyObject* PYCALL CallMethod(SELF *self, PyObject *args)
    {
        return self->CallMethodImpl(args);
    }

    ForceInline PyObject* CallMethodImpl(PyObject *args)
    {
        if (PyTuple_GET_SIZE(args) != PyFunctionHelper<T>::NumberOfArguments)
        {
            PyErr_SetString(
                PyExc_TypeError,
                String::Format(
                    L"function takes %d argument%s, but %d given",
                    PyFunctionHelper<T>::NumberOfArguments,
                    PyFunctionHelper<T>::NumberOfArguments > 1 ? L"s" : L"",
                    PyTuple_GET_SIZE(args)
                )
                .Encode(CP_UTF8)
            );

            return nullptr;
        }

        return PyFunctionHelper<T>::CallRoutine(this->func, args);
    }

    static PyObject* PYCALL AllocObject(PyTypeObject *type, PyObject *args, PyObject *kwargs)
    {
        return type->tp_alloc(type, 0);
    }

    static VOID PYCALL FreeObject(SELF *self)
    {
        Py_TYPE(self)->tp_free((PyObject*)self);
    }
};


//////////////////////////////////////////////////////////////////////////
// mlpy
//////////////////////////////////////////////////////////////////////////

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

    template<typename T>
    PYSTATUS GetGlobalVariable(const String& ModuleName, const String& VariableName, T& Output)
    {
        PyObject *module, *name, *value;
        PYSTATUS status;

        module = Import(ModuleName);
        if (module == nullptr)
            return PYSTATUS_IMPORT_MODULE_FAILED;

        status = STATUS_UNSUCCESSFUL;

        name = nullptr;
        value = nullptr;

        LOOP_ONCE
        {
            name = PyUnicode_FromUnicode(VariableName, VariableName.GetCount());
            if (name == nullptr)
            {
                status = PYSTATUS_CREATE_UNICODE_FAILED;
                break;
            }

            value = PyObject_GetAttr(module, name);
            if (value == nullptr)
            {
                status = PYSTATUS_GET_ATTR_FAILED;
                break;
            }

            Output = PyTypeConverter<PyTypeHelper<T>::VALUE_TYPE>::ToNative(value);
            status = STATUS_SUCCESS;
        }

        PyRelease(name);
        PyRelease(value);
        PyRelease(module);

        return status;
    }

    template<typename T>
    PYSTATUS SetGlobalVariable(const String& ModuleName, const String& VariableName, const T& Value)
    {
        PyObject *module, *name, *value;
        PYSTATUS status;

        module = Import(ModuleName);
        if (module == nullptr)
            return PYSTATUS_IMPORT_MODULE_FAILED;

        status = STATUS_UNSUCCESSFUL;

        name = nullptr;
        value = nullptr;

        LOOP_ONCE
        {
            name = PyUnicode_FromUnicode(VariableName, VariableName.GetCount());
            if (name == nullptr)
            {
                status = PYSTATUS_CREATE_UNICODE_FAILED;
                break;
            }

            value = PyTypeConverter<PyTypeHelper<T>::VALUE_TYPE>::FromNative(Value);
            if (value == nullptr)
            {
                status = PYSTATUS_CREATE_OBJECT_FAILED;
                break;
            }

            status = PyObject_SetAttr(module, name, value) == 0 ? STATUS_SUCCESS : PYSTATUS_SET_ATTR_FAILED;
        }

        PyRelease(name);
        PyRelease(value);
        PyRelease(module);

        return status;
    }

    template<class T>
    NoInline MlPython& Register(T func, const String& FunctionName, const String& Doc = L"")
    {
        PY_STATIC_FUNCTION f;

        *(T *)&f.Address = func;

        f.Name      = FunctionName;
        f.Doc       = Doc;
        f.ArgsCount = PyFunctionHelper<T>::NumberOfArguments;
        f.TypeSize  = sizeof(PyStaticFunctionHelper<T>);
        f.Native    = (PyCFunction)PyStaticFunctionHelper<T>::CallMethod;
        f.dtor      = (destructor)PyStaticFunctionHelper<T>::FreeObject;
        f.ctor      = (initproc)PyStaticFunctionHelper<T>::InitObject;
        f.alloc      = PyStaticFunctionHelper<T>::AllocObject;

        this->RegisteredFunctions.Add(f);

        return *this;
    }

    NoInline PYSTATUS InitModule(const String& ModuleName/*, const String& Doc = L""*/)
    {
        PyObject* Module;
        auto& ModuleNameAnsi = ModuleName.Encode(CP_UTF8);
        //auto& DocAnsi = Doc.Encode(CP_UTF8);

        Module = PyImport_AddModule(ModuleNameAnsi);
        if (Module == nullptr)
            return PYSTATUS_CREATE_MODULE_FAILED;

        FAIL_RETURN(this->InitFunctions(Module, ModuleName));

        return STATUS_SUCCESS;
    }

    static PyObject* Import(const String& ModuleName)
    {
        PyObject *name, *module;

        name = PyUnicode_FromUnicode(ModuleName, ModuleName.GetCount());
        if (name == nullptr)
            return nullptr;

        module = PyImport_Import(name);
        PyRelease(name);

        return module;
    }

    template<typename RET_TYPE, typename... ARGS>
    NoInline RET_TYPE Invoke(const String& ModuleName, const String& FunctionName, ARGS... args)
    {
        return PyInvokePyHelper<RET_TYPE>::Invoke(this, ModuleName, FunctionName, args...);
    }

protected:

    template<typename RET_TYPE>
    struct PyInvokePyHelper
    {
        template<typename... ARGS>
        ForceInline static RET_TYPE Invoke(MlPython* This, const String& ModuleName, const String& FunctionName, ARGS... args)
        {
            PyObject* retval = This->InvokeInternal(ModuleName, FunctionName, args...);
            RET_TYPE ret = PyTypeConverter<PyTypeHelper<RET_TYPE>::VALUE_TYPE>::ToNative(retval);
            PyRelease(retval);
            return ret;
        }
    };

    template<>
    struct PyInvokePyHelper<VOID>
    {
        template<typename... ARGS>
        ForceInline static VOID Invoke(MlPython* This, const String& ModuleName, const String& FunctionName, ARGS... args)
        {
            PyObject* retval = This->InvokeInternal(ModuleName, FunctionName, args...);
            PyRelease(retval);
        }
    };

    template<typename... ARGS>
    NoInline PyObject* InvokeInternal(const String& ModuleName, const String& FunctionName, ARGS... args)
    {
        PYSTATUS status;
        PyObject* tuple;
        PyObject* module;
        PyObject* func;
        PyObject* name;
        PyObject* value;
        PyCodeObject* code;

        status = STATUS_UNSUCCESSFUL;

        tuple   = nullptr;
        module  = nullptr;
        func    = nullptr;
        name    = nullptr;
        value   = nullptr;

        SCOPE_EXIT
        {
            PyRelease(tuple);
            PyRelease(module);
            PyRelease(func);
            PyRelease(name);
            PyRelease(value);
        }
        SCOPE_EXIT_END;

        module = Import(ModuleName);
        if (module == nullptr)
            return value;

        name = PyUnicode_FromUnicode(FunctionName, FunctionName.GetCount());
        if (name == nullptr)
            return value;

        func = PyObject_GetAttr(module, name);
        if (func == nullptr)
            return value;

        code = (PyCodeObject *)PyFunction_GET_CODE(func);
        if (code->co_argcount != sizeof...(ARGS))
        {   
            PyErr_SetString(
                PyExc_TypeError,
                String::Format(
                    L"function takes %d argument%s, but %d given",
                    code->co_argcount,
                    code->co_argcount > 1 ? L"s" : L"",
                    sizeof...(ARGS)
                )
                .Encode(CP_UTF8)
            );

            return nullptr;
        }

        tuple = PyTuple_New(sizeof...(ARGS));
        if (tuple == nullptr)
            return value;

        status = BuildPyArgs(tuple, 0, args...);
        if (PY_FAILED(status))
            return value;

        value = PyObject_CallObject(func, tuple);
        if (PyErr_Occurred())
        {
            PyErr_Clear();
        }

        if (value != nullptr)
            PyAddRef(value);

        return value;
    }

    ForceInline PYSTATUS BuildPyArgs(PyObject *tuple, Py_ssize_t Index)
    {
        return STATUS_SUCCESS;
    }

    template<typename T, typename... REST>
    ForceInline PYSTATUS BuildPyArgs(PyObject *tuple, Py_ssize_t Index, T arg, REST... rest)
    {
        PyObject *obj = PyTypeConverter<PyTypeHelper<T>::VALUE_TYPE>::FromNative(arg);
        if (obj == nullptr)
            return PYSTATUS_CREATE_OBJECT_FAILED;

        PyTuple_SetItem(tuple, Index, obj);
        PyRelease(obj);

        return BuildPyArgs(tuple, Index + 1, rest...);
    }

    PYSTATUS InitFunctions(PyObject* Module, const String& ModuleName)
    {
        for (auto &func : this->RegisteredFunctions)
        {
            auto &name = func.Name.Encode(CP_UTF8);
            auto &type = (func.Name + WRAP_CLASS_SUFFIX).Encode(CP_UTF8);

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
                nullptr,                                            /* tp_print */
                nullptr,                                            /* tp_getattr */
                nullptr,                                            /* tp_setattr */
                nullptr,                                            /* tp_reserved */
                nullptr,                                            /* tp_repr */
                nullptr,                                            /* tp_as_number */
                nullptr,                                            /* tp_as_sequence */
                nullptr,                                            /* tp_as_mapping */
                nullptr,                                            /* tp_hash*/
                nullptr,                                            /* tp_call*/
                nullptr,                                            /* tp_str */
                PyObject_GenericGetAttr,                            /* tp_getattro */
                nullptr,                                            /* tp_setattro */
                nullptr,                                            /* tp_as_buffer */
                Py_TPFLAGS_DEFAULT,                                 /* tp_flags */
                "",                                                 /* tp_doc */
                nullptr,                                            /* tp_traverse */
                nullptr,                                            /* tp_clear */
                nullptr,                                            /* tp_richcompare */
                0,                                                  /* tp_weaklistoffset */
                nullptr,                                            /* tp_iter */
                nullptr,                                            /* tp_iternext */
                methods,                                            /* tp_methods */
                nullptr,                                            /* tp_members */
                nullptr,                                            /* tp_getset */
                &PyBaseObject_Type,                                 /* tp_base */
                nullptr,                                            /* tp_dict */
                nullptr,                                            /* tp_descr_get */
                nullptr,                                            /* tp_descr_set */
                0,                                                  /* tp_dictoffset */
                func.ctor,                                          /* tp_init */
                nullptr,                                            /* tp_alloc */
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
            &SelfPath, PYTHON_PACKAGE_PATH,                      // ./python
            &SelfPath, PYTHON_PACKAGE_PATH, PythonZip,           // ./python/python.zip
            &SelfPath, PYTHON_PACKAGE_PATH, PythonZip,           // ./python/python.zip/site-packages
            &SelfPath, PYTHON_PACKAGE_PATH,                      // ./python/lib
            &SelfPath, PYTHON_PACKAGE_PATH,                      // ./python/DLLs
            &SelfPath, PYTHON_PACKAGE_PATH                       // ./python/UserSite
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
