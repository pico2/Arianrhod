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
#include <frameobject.h>

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
struct PyCallFuncObjectHelper
{
    template<typename R, typename FUNC_TYPE, typename ARG1, typename... FUNC_ARGS, typename... EXTRACTED_ARGS>
    ForceInline static R CallFuncObject(FUNC_TYPE func, PyObject *args, Py_ssize_t Index, EXTRACTED_ARGS... fargs)
    {
        return PyCallFuncObjectHelper<sizeof...(FUNC_ARGS)>::CallFuncObject<R, FUNC_TYPE, FUNC_ARGS...>(
                   func,
                   args,
                   Index + 1,
                   fargs...,
                   PyTypeConverter<PyTypeHelper<ARG1>::VALUE_TYPE>::ToNative(PyTuple_GetItem(args, Index))
               );
    }
};

template<>
struct PyCallFuncObjectHelper<0>
{
    template<typename R, typename FUNC_TYPE, typename... EXTRACTED_ARGS>
    ForceInline static R CallFuncObject(FUNC_TYPE func, PyObject *args, Py_ssize_t Index, EXTRACTED_ARGS... fargs)
    {
        return (*func)(fargs...);
    }
};

template<typename T>
struct PyFunctionTraits
{
    typedef ml::Function<T> FUNCTION_OBJECT;

    static const ULONG_PTR NumberOfArguments = FUNCTION_OBJECT::NumberOfArguments;

    typedef typename FUNCTION_OBJECT::RET_TYPE          RET_TYPE;
    typedef typename FUNCTION_OBJECT::FUNCTION_TYPE     FUNCTION_TYPE;
};

struct MlPyObjectBase : public PyObjectBase
{
    PyMethodDef*    Methods;
    PyTypeObject*   SelfType;

    MlPyObjectBase()
    {
        this->Methods = nullptr;
        this->SelfType = nullptr;
    }

    ~MlPyObjectBase()
    {
        SafeDeleteArrayT(this->Methods);
        SafeDeleteT(this->SelfType);
    }
};

template<typename FUNC_OBJECT>
struct PyStaticFunctionHelper : public MlPyObjectBase
{
    typedef typename FUNC_OBJECT::FUNCTION_TYPE FUNC_TYPE;
    typedef ml::String String;
    typedef PyStaticFunctionHelper<FUNC_OBJECT> SELF;

    static const ULONG_PTR NumberOfArguments = FUNC_OBJECT::NumberOfArguments;

    FUNC_OBJECT* func;
    String Name;

    PyStaticFunctionHelper(PCWSTR FunctionName) : Name(FunctionName)
    {
        func = nullptr;
    }

    static INT PYCALL InitObject(SELF *self, PyObject *args, PyObject *kwargs)
    {
        new (self) SELF(PyUnicode_AsUnicode(PyTuple_GetItem(args, 1)));
        *(FUNC_OBJECT **)&self->func = (FUNC_OBJECT *)(ULONG_PTR)PyLong_AsUnsignedLongLong(PyTuple_GetItem(args, 0));
        return 0;
    }

    static PyObject* PYCALL AllocObject(PyTypeObject *type, PyObject *args, PyObject *kwargs)
    {
        return type->tp_alloc(type, 0);
    }

    static VOID PYCALL FreeObject(SELF *self)
    {
        self->~SELF();
        Py_TYPE(self)->tp_free((PyObject*)self);
    }

    static PyObject* PYCALL CallMethod(SELF *self, PyObject *args)
    {
        return self->CallMethodImpl(args);
    }

    ForceInline PyObject* CallMethodImpl(PyObject *args)
    {
        if (PyTuple_GET_SIZE(args) != NumberOfArguments)
        {
            PyErr_SetString(
                PyExc_TypeError,
                String::Format(
                    L"'%s' takes %d argument%s, but %d given",
                    this->Name, NumberOfArguments, NumberOfArguments > 1 ? L"s" : L"", PyTuple_GET_SIZE(args)
                )
                .Encode(CP_UTF8)
            );

            return nullptr;
        }

        return CallRoutine<FUNC_OBJECT::RET_TYPE>(args);
    }

    template<typename RET_TYPE>
    PyObject* CallRoutine(PyObject * args)
    {
        FUNC_TYPE *f = nullptr;
        return PyTypeConverter<RET_TYPE>::FromNative(CallStaticRoutineImpl<RET_TYPE>(args, f));
    }

    template<>
    PyObject* CallRoutine<VOID>(PyObject * args)
    {
        FUNC_TYPE *f = nullptr;
        CallStaticRoutineImpl<VOID>(args, f);
        Py_RETURN_NONE;
    }

    template<typename R, typename... ARGS>
    R CallStaticRoutineImpl(PyObject *args, R(*)(ARGS...))
    {
        return PyCallFuncObjectHelper<NumberOfArguments>::CallFuncObject<R, TYPE_OF(this->func), ARGS...>(this->func, args, 0);
    }
};


//////////////////////////////////////////////////////////////////////////
// mlpy
//////////////////////////////////////////////////////////////////////////

struct MlPythonException
{
    MlPythonException() {}

    MlPythonException(const MlPythonException&) = delete;
    MlPythonException& operator=(const MlPythonException&) = delete;

    VOID Clear()
    {
        this->Message = L"";
    }

    VOID SetMessage(PCWSTR Message)
    {
        this->Message = Message;
    }

    BOOL ErrorOccurred() const
    {
        return this->Message.GetCount() != 0;
    }

    ml::String Message;
};

class MlPyObject
{
protected:
    PyObject *object;

public:
    MlPyObject(PyObject* object = nullptr)
    {
        this->object = object;
    }

    NoInline ~MlPyObject()
    {
        PyRelease(object);
    }

    MlPyObject(const MlPyObject&) = delete;
    MlPyObject& operator=(const MlPyObject&) = delete;

    MlPyObject& operator=(PyObject *object)
    {
        this->~MlPyObject();
        this->object = object;
        return *this;
    }

    operator PyObject*()
    {
        return object;
    }

    PyObject** operator&()
    {
        return &object;
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

    struct REGISTER_CLASS_HELPER
    {
        ULONG_PTR   ArgsCount;
        ULONG_PTR   TypeSize;
        PyCFunction Native;
        initproc    ctor;
        destructor  dtor;
        newfunc     alloc;
        PVOID       CtorAddress;
        String      Name;
        String      Doc;

        GrowableArray<PY_STATIC_FUNCTION> ClassMethods;
    };

    MlPythonException PyException;
    GrowableArray<PY_STATIC_FUNCTION> RegisteredFunctions;
    GrowableArray<REGISTER_CLASS_HELPER> RegisteredClasses;

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

    const MlPythonException& GetPyException() const
    {
        return this->PyException;
    }

    NoInline const MlPythonException& CapturePyException()
    {
        MlPyObject Type, Value, TraceBack, FormatException, StringJoin, ExceptionList, ExceptionInfo;

        this->PyException.Clear();

        PyErr_Fetch(&Type, &Value, &TraceBack);
        PyErr_NormalizeException(&Type, &Value, &TraceBack);

        LOOP_ONCE
        {
            FormatException = GetModuleAttr(L"traceback", L"format_exception");
            BREAK_IF(FormatException == nullptr);

            if (TraceBack == nullptr)
            {
                TraceBack = Py_None;
                PyAddRef(TraceBack);
            }

            ExceptionList = PyObject_CallFunction(FormatException, "OOOi", Type, Value, TraceBack, 20);
            BREAK_IF(ExceptionList == nullptr);

            ExceptionInfo = PyUnicode_Join(MlPyObject(PyUnicode_FromUnicode(L"", 0)), ExceptionList);
            BREAK_IF(ExceptionInfo == nullptr);

            this->PyException.SetMessage(PyUnicode_AsUnicode(ExceptionInfo));
        }

        return this->PyException;
    }

    NoInline const MlPythonException& SetPyException(const String& ErrorMessage, PyObject *ExceptionType = PyExc_TypeError)
    {
        PyErr_SetString(ExceptionType, ErrorMessage.Encode(CP_UTF8));
        return this->CapturePyException();
    }

    NoInline const MlPythonException& SetPyException(PCSTR Utf8ErrorMessage, PyObject *ExceptionType = PyExc_TypeError)
    {
        PyErr_SetString(ExceptionType, Utf8ErrorMessage);
        return this->CapturePyException();
    }


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
        MlPyObject value;

        value = GetModuleAttr(ModuleName, VariableName);
        if (value == nullptr)
            return PYSTATUS_GET_ATTR_FAILED;

        Output = PyTypeConverter<PyTypeHelper<T>::VALUE_TYPE>::ToNative(value);

        return STATUS_SUCCESS;
    }

    template<typename T>
    PYSTATUS SetGlobalVariable(const String& ModuleName, const String& VariableName, const T& Value)
    {
        MlPyObject  module, name, value;
        PYSTATUS    status;

        module = Import(ModuleName);
        if (module == nullptr)
            return PYSTATUS_IMPORT_MODULE_FAILED;

        status = STATUS_UNSUCCESSFUL;

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

        return status;
    }

    template<typename T>
    NoInline MlPython& Register(T func, const String& FunctionName, const String& Doc = L"")
    {
        PY_STATIC_FUNCTION f;

        typedef ml::Function<T>                                     LAMBDA_OR_FUNCTION;
        typedef ml::Function<LAMBDA_OR_FUNCTION::FUNCTION_TYPE>     FUNCTION;
        typedef FUNCTION::FUNCTION_TYPE                             FUNCTION_TYPE;

        *(FUNCTION **)&f.Address = new FUNCTION(func);

        f.Name      = FunctionName;
        f.Doc       = Doc;
        f.ArgsCount = FUNCTION::NumberOfArguments;
        f.TypeSize  = sizeof(PyStaticFunctionHelper<FUNCTION>);
        f.Native    = (PyCFunction)PyStaticFunctionHelper<FUNCTION>::CallMethod;
        f.dtor      = (destructor)PyStaticFunctionHelper<FUNCTION>::FreeObject;
        f.ctor      = (initproc)PyStaticFunctionHelper<FUNCTION>::InitObject;
        f.alloc      = PyStaticFunctionHelper<FUNCTION>::AllocObject;

        this->RegisteredFunctions.Add(f);

        return *this;
    }

    template<typename CLASS, typename CTOR>
    REGISTER_CLASS_HELPER& RegisterClass(const String& ClassName, const String& ClassDoc = L"")
    {
        this->RegisteredClasses.Add(REGISTER_CLASS_HELPER());

        REGISTER_CLASS_HELPER& cls = this->RegisteredClasses.GetLast();

        return cls;
    }

    NoInline PYSTATUS InitModule(const String& ModuleName/*, const String& Doc = L""*/)
    {
        PyObject *Module;

        Module = PyImport_AddModuleObject(MlPyObject(PyUnicode_FromUnicode(ModuleName, ModuleName.GetCount())));
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

    static PyObject* GetModuleAttr(const String& ModuleName, const String& AttrName)
    {
        PyObject *module, *name, *attr;

        module = Import(ModuleName);
        if (module == nullptr)
            return nullptr;

        attr = nullptr;
        name = PyUnicode_FromUnicode(AttrName, AttrName.GetCount());
        if (name != nullptr)
        {
            attr = PyObject_GetAttr(module, name);
        }

        PyRelease(name);
        PyRelease(module);

        return attr;
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
            MlPyObject retval = This->InvokeInternal(ModuleName, FunctionName, args...);
            RET_TYPE ret = PyTypeConverter<PyTypeHelper<RET_TYPE>::VALUE_TYPE>::ToNative(retval);
            return ret;
        }
    };

    template<>
    struct PyInvokePyHelper<VOID>
    {
        template<typename... ARGS>
        ForceInline static VOID Invoke(MlPython* This, const String& ModuleName, const String& FunctionName, ARGS... args)
        {
            MlPyObject retval = This->InvokeInternal(ModuleName, FunctionName, args...);
        }
    };

    template<typename... ARGS>
    NoInline PyObject* InvokeInternal(const String& ModuleName, const String& FunctionName, ARGS... args)
    {
        PYSTATUS status;
        MlPyObject module, tuple, func, value;
        PyCodeObject* code;

        module = Import(ModuleName);
        if (module == nullptr)
        {
            this->SetPyException(String::Format(L"No module named '%s'", ModuleName), PyExc_ImportError);
            return nullptr;
        }

        func = PyObject_GetAttr(module, MlPyObject(PyUnicode_FromUnicode(FunctionName, FunctionName.GetCount())));
        if (func == nullptr)
        {
            this->SetPyException(String::Format(L"'%s' object has no attribute '%s'", ModuleName, FunctionName), PyExc_AttributeError);
            return nullptr;
        }

        code = (PyCodeObject *)PyFunction_GET_CODE((PyObject *)func);
        if (code->co_argcount != sizeof...(ARGS))
        {
            this->SetPyException(
                String::Format(
                    L"'%s' takes %d argument%s, but %d given",
                    FunctionName,
                    code->co_argcount,
                    code->co_argcount > 1 ? L"s" : L"",
                    sizeof...(ARGS)
                )
            );

            return nullptr;
        }

        tuple = PyTuple_New(sizeof...(ARGS));
        if (tuple == nullptr)
        {
            this->SetPyException("Create Tuple failed", PyExc_MemoryError);
            return nullptr;
        }

        status = BuildPyArgs(tuple, 0, args...);
        if (PY_FAILED(status))
        {
            this->SetPyException("Build python args failed", PyExc_MemoryError);
            return nullptr;
        }

        value = PyObject_CallObject(func, tuple);
        if (PyErr_Occurred())
        {
            CapturePyException();
        }
        else
        {
            this->PyException.Clear();
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

            BOOL Success = FALSE;

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
                MlPyObject args, obj, method;

                if (methods == nullptr || methoswrapclass == nullptr)
                    break;

                if (PyType_Ready(methoswrapclass) != 0)
                    break;

                PyAddRef((PyObject *)methoswrapclass);
                if (PyModule_AddObject(Module, methoswrapclass->tp_name, (PyObject *)methoswrapclass) != 0)
                    break;

                args = Py_BuildValue("(Ku)", (ULONG64)func.Address, func.Name);
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

                ((MlPyObjectBase *)(PyObject *)obj)->Methods = methods;
                ((MlPyObjectBase *)(PyObject *)obj)->SelfType = methoswrapclass;

                Success = TRUE;
            }

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
