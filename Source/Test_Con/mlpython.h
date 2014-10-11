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
//               佛祖保佑         永无BUG
//
//
//

#include "ml.h"
#include <PythonHelper/PythonHelper.h>
#include <frameobject.h>

#define PYTHON_DLL              L"python34.dll"

#if !defined(PYTHON_PACKAGE_PATH)
    #define PYTHON_PACKAGE_PATH     L"python\\"
#endif

typedef LONG PYSTATUS;
#define PY_SUCCESS NT_SUCCESS
#define PY_FAILED NT_FAILED

#define PYCALL CDECL

#define PYCTOR INT (PYCALL*)

#define WRAP_CLASS_SUFFIX L"_WRAP_CLASS"


typedef enum
{
    PYSTATUS_SUCCESS = 0,

    PyStatusFirst = DEFINE_NTSTATUS(STATUS_SEVERITY_ERROR, 0x100),

    PYSTATUS_CREATE_MODULE_FAILED,
    PYSTATUS_IMPORT_MODULE_FAILED,
    PYSTATUS_CREATE_UNICODE_FAILED,
    PYSTATUS_CREATE_OBJECT_FAILED,
    PYSTATUS_GET_ATTR_FAILED,
    PYSTATUS_SET_ATTR_FAILED,
    PYSTATUS_NO_MEMORY,

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

template<>
struct PyTypeConverter<PVOID>
{
    static PyObject* FromNative(PVOID object)
    {
        return (PyObject *)object;
    }

    static PVOID ToNative(PyObject *object)
    {
        return object;
    }
};

template<>
struct PyTypeConverter<PyObject *>
{
    static PyObject* FromNative(PyObject *object)
    {
        if (object != nullptr)
            PyAddRef(object);
        return object;
    }

    static PyObject* ToNative(PyObject *object)
    {
        if (object != nullptr)
            PyAddRef(object);
        return object;
    }
};

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


template<>
struct PyTypeConverter<ml::ByteArray>
{
    static PyObject* FromNative(const ml::ByteArray &object)
    {
        return PyBytes_FromStringAndSize((PCHAR)object.GetData(), object.GetSize());
    }

    static ml::ByteArray ToNative(PyObject *object)
    {
        ml::ByteArray   bytes;
        Py_ssize_t      Size;
        PCHAR           Buffer;

        if (object == nullptr)
            return bytes;

        if (PyBytes_Check(object) != FALSE)
        {
            PyBytes_AsStringAndSize(object, &Buffer, &Size);
        }
        else if (PyByteArray_Check(object) != FALSE)
        {
            Size = PyByteArray_Size(object);
            Buffer = PyByteArray_AsString(object);
        }
        else
        {
            return bytes;
        }

        if (NT_SUCCESS(bytes.SetSize(Size)))
        {
            CopyMemory(bytes.GetData(), Buffer, Size);
            bytes.UpdateDataCount(Size);
        }

        return bytes;
    }
};

template<>
struct PyTypeConverter<ml::String>
{
    static PyObject* FromNative(const ml::String &object)
    {
        return PyUnicode_FromUnicode(object, object.GetCount());
    }

    static ml::String ToNative(PyObject *object)
    {
        ml::String text;
        Py_ssize_t size;
        Py_UNICODE *buffer;

        if (object == nullptr || PyUnicode_Check(object) == FALSE)
            return text;

        buffer = PyUnicode_AsUnicodeAndSize(object, &size);
        text.CopyFrom(buffer, size);

        return text;
    }
};

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

template<typename FUNC_OBJECT, typename FUNC_OBJ_CALLER = PyCallFuncObjectHelper<FUNC_OBJECT::NumberOfArguments>>
struct PyStaticFunctionHelper : public MlPyObjectBase
{
    typedef typename FUNC_OBJECT::FUNCTION_TYPE                     FUNC_TYPE;
    typedef PyStaticFunctionHelper<FUNC_OBJECT, FUNC_OBJ_CALLER>    SELF;
    typedef ml::String                                              String;

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
        *(FUNC_OBJECT **)&self->func = (FUNC_OBJECT *)PyTuple_GetItem(args, 0);
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
    PyObject* CallRoutine(PyObject* args)
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
        return FUNC_OBJ_CALLER::CallFuncObject<R, TYPE_OF(this->func), ARGS...>(this->func, args, 0);
    }
};


template<typename BASE_CLASS, typename CTOR>
struct PyNativeClassHelper : public MlPyObjectBase
{
    typedef PyNativeClassHelper<BASE_CLASS, CTOR> SELF;
    typedef ml::String String;

    BASE_CLASS *object;

    PyNativeClassHelper()
    {
        this->object = nullptr;
    }

    ~PyNativeClassHelper()
    {
        SafeDeleteT(this->object);
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

    static INT PYCALL InitObject(SELF *self, PyObject *args, PyObject *kwargs)
    {
        new (self)SELF();

        CTOR* ctor = nullptr;

        self->object = self->InitClassObject(args, ctor);

        IF_EXIST(BASE_CLASS::self)
        {
            self->object->self = (PyObject *)self;
        }

        return self->object == nullptr ? -1 : 0;
    }

    template<typename R, typename... ARGS>
    BASE_CLASS* InitClassObject(PyObject *args, R(*ctor)(ARGS...))
    {
        static const ULONG_PTR NumberOfArguments = sizeof...(ARGS);
        if (PyTuple_GET_SIZE(args) != NumberOfArguments)
        {
            PyErr_SetString(
                PyExc_TypeError,
                String::Format(
                    L"'%S' takes %d argument%s, but %d given",
                    Py_TYPE(this)->tp_name, NumberOfArguments, NumberOfArguments > 1 ? L"s" : L"", PyTuple_GET_SIZE(args)
                )
                .Encode(CP_UTF8)
            );

            return nullptr;
        }

        auto lambda = [](ARGS... args)
        {
            return new BASE_CLASS(args...);
        };

        return PyCallFuncObjectHelper<sizeof...(ARGS)>::CallFuncObject<BASE_CLASS*, TYPE_OF(&lambda), ARGS...>(&lambda, args, 0);
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

    MlPyObject(const ml::String& str)
    {
        this->object = PyUnicode_FromUnicode(str, str.GetCount());
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

struct MlPyTypeObject : public PyTypeObject
{
    MlPyTypeObject()
    {
        this->tp_name = nullptr;
    }

    MlPyTypeObject(PyTypeObject *that)
    {
        CopyStruct((PyTypeObject *)this, that, sizeof(*that));
        this->tp_name = nullptr;
    }

    ~MlPyTypeObject()
    {
        SafeDeleteT(this->tp_name);
    }
};

struct MlPyMethodDef : public PyMethodDef
{
    MlPyMethodDef()
    {
        this->ml_name = nullptr;
    }

    MlPyMethodDef(PyMethodDef *that)
    {
        CopyStruct((PyMethodDef *)this, that, sizeof(*that));
        this->ml_name = nullptr;
    }

    ~MlPyMethodDef()
    {
        SafeDeleteT(this->ml_name);
    }
};

struct MlPyGetSetDef : public PyGetSetDef
{
    MlPyGetSetDef()
    {
        this->name = nullptr;
        this->doc = nullptr;
    }

    MlPyGetSetDef(PyGetSetDef *that)
    {
        CopyStruct((PyGetSetDef *)this, that, sizeof(*that));
        this->name = nullptr;
        this->doc = nullptr;
    }

    ~MlPyGetSetDef()
    {
        SafeDeleteT(this->name);
        SafeDeleteT(this->doc);
    }
};

struct MlWrapperBase : public wrapperbase
{
    PyCFunction method;

    MlWrapperBase()
    {
        this->name = nullptr;
        this->doc = nullptr;
        this->method = nullptr;
    }

    MlWrapperBase(wrapperbase *that)
    {
        CopyStruct((PyMethodDef *)this, that, sizeof(*that));
        this->name = nullptr;
        this->doc = nullptr;
        this->method = nullptr;
    }

    ~MlWrapperBase()
    {
        SafeDeleteT(this->name);
        SafeDeleteT(this->doc);
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
        ULONG_PTR   TypeSize;
        PyCFunction Native;
        initproc    ctor;
        destructor  dtor;
        newfunc     alloc;
        PVOID       Address;
        String      Name;
        String      Doc;
        ULONG_PTR   Flags;

        PY_STATIC_FUNCTION()
        {
            Flags = 0;
        }
    };

    MlPythonException                   PyException;
    GrowableArray<PY_STATIC_FUNCTION>   RegisteredFunctions;
    GrowableArray<MlPyTypeObject>       RegisteredTypeObjects;
    GrowableArray<MlWrapperBase>        RegisteredWrappers;
    GrowableArray<MlPyGetSetDef>        RegisteredGetSets;

public:
    MlPython()
    {
        ml::MlInitialize();
    }

    ~MlPython()
    {
        ;
    }

    VOID Initialize()
    {
        if (Py_IsInitialized() == FALSE)
        {
            InitializePackage();
            Py_Initialize();
        }
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
        return PYSTATUS_SUCCESS;
    }

    PYSTATUS RunString(const String& code)
    {
        PyRun_SimpleString(code.Encode(CP_UTF8));
        return PYSTATUS_SUCCESS;
    }

    template<typename T>
    PYSTATUS GetGlobalVariable(const String& ModuleName, const String& VariableName, T& Output)
    {
        MlPyObject value;

        value = GetModuleAttr(ModuleName, VariableName);
        if (value == nullptr)
            return PYSTATUS_GET_ATTR_FAILED;

        Output = PyTypeConverter<PyTypeHelper<T>::VALUE_TYPE>::ToNative(value);

        return PYSTATUS_SUCCESS;
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

            status = PyObject_SetAttr(module, name, value) == 0 ? PYSTATUS_SUCCESS : PYSTATUS_SET_ATTR_FAILED;
        }

        return status;
    }

    template<typename T>
    NoInline MlPython& Register(T func, const String& FunctionName, const String& Doc = L"")
    {
        PY_STATIC_FUNCTION f;

        typedef ml::Function<T>                                     LAMBDA_OR_FUNCTION;
        typedef ml::Function<LAMBDA_OR_FUNCTION::FUNCTION_TYPE>     FUNCTION;

        *(FUNCTION **)&f.Address = new FUNCTION(func);

        f.Name      = FunctionName;
        f.Doc       = Doc;
        f.TypeSize  = sizeof(PyStaticFunctionHelper<FUNCTION>);
        f.Native    = (PyCFunction)PyStaticFunctionHelper<FUNCTION>::CallMethod;
        f.dtor      = (destructor)PyStaticFunctionHelper<FUNCTION>::FreeObject;
        f.ctor      = (initproc)PyStaticFunctionHelper<FUNCTION>::InitObject;
        f.alloc      = PyStaticFunctionHelper<FUNCTION>::AllocObject;

        this->RegisteredFunctions.Add(f);

        return *this;
    }

    struct REGISTER_CLASS_HELPER
    {
        struct CLASS_PROPERTY_HELPER
        {
            getter      get;
            setter      set;
            ULONG_PTR   offset;
            String      Name;
            String      Doc;
        };

        ULONG_PTR   TypeSize;
        initproc    ctor;
        destructor  dtor;
        newfunc     alloc;
        String      Name;
        String      Doc;

        MlPython*   thiz;

        GrowableArray<PY_STATIC_FUNCTION> Methods;
        GrowableArray<CLASS_PROPERTY_HELPER> Properties;

        REGISTER_CLASS_HELPER(MlPython* py = nullptr) : thiz(py)
        {
        }

        template<typename T>
        NoInline REGISTER_CLASS_HELPER& RegisterMethodHelper(T func, const String& MethodName, const String& Doc = L"")
        {
            PY_STATIC_FUNCTION f;

            typedef ml::Function<PyCFunction> FUNC;

            *(FUNC **)&f.Address = new FUNC(func);

            f.Name      = MethodName;
            f.Doc       = Doc;

            this->Methods.Add(f);

            return *this;
        }

        template<typename CLASS, typename R, typename... ARGS>
        NoInline REGISTER_CLASS_HELPER& RegisterMethod(R(CLASS::*method)(ARGS...), const String& MethodName, const String& Doc = L"")
        {
            typedef PyNativeClassHelper<CLASS, VOID()> FAKE_CLASS;

            auto Invoker = [=](PyObject *self, PyObject *args) -> PyObject*
            {
                auto Invoker2 = [=] (ARGS... args)
                {
                    FAKE_CLASS *thiz = (FAKE_CLASS *)self;
                    return (thiz->object->*method)(args...);
                };

                return PyTypeConverter<R>::FromNative(
                            PyCallFuncObjectHelper<sizeof...(ARGS)>::CallFuncObject<R, TYPE_OF(&Invoker2), ARGS...>(&Invoker2, args, 0)
                        );
            };

            return this->RegisterMethodHelper(Invoker, MethodName, Doc);
        }

        template<typename CLASS, typename... ARGS>
        NoInline REGISTER_CLASS_HELPER& RegisterMethod(VOID(CLASS::*method)(ARGS...), const String& MethodName, const String& Doc = L"")
        {
            typedef PyNativeClassHelper<CLASS, VOID()> FAKE_CLASS;

            auto Invoker = [=](PyObject *self, PyObject *args) -> PyObject*
            {
                auto Invoker2 = [=](ARGS... args)
                {
                    FAKE_CLASS *thiz = (FAKE_CLASS *)self;
                    return (thiz->object->*method)(args...);
                };

                PyCallFuncObjectHelper<sizeof...(ARGS)>::CallFuncObject<VOID, TYPE_OF(&Invoker2), ARGS...>(&Invoker2, args, 0);
                Py_RETURN_NONE;
            };

            return this->RegisterMethodHelper(Invoker, MethodName, Doc);
        }

        template<typename CLASS, typename R>
        NoInline REGISTER_CLASS_HELPER& RegisterProperty(R CLASS::*member, const String& PropertyName, const String& Doc = L"", BOOL ReadOnly = FALSE)
        {
            typedef PyNativeClassHelper<CLASS, VOID()> FAKE_CLASS;

            auto getter = [](PyObject *self, PVOID Closure) -> PyObject*
            {
                R CLASS::*member;
                FAKE_CLASS *thiz = (FAKE_CLASS *)self;

                *(PVOID *)&member = Closure;

                return PyTypeConverter<R>::FromNative(thiz->object->*member);
            };

            auto setter = [](PyObject *self, PyObject *value, PVOID Closure) -> int
            {
                R CLASS::*member;
                FAKE_CLASS *thiz = (FAKE_CLASS *)self;

                *(PVOID *)&member = Closure;
                thiz->object->*member = PyTypeConverter<R>::ToNative(value);

                return 0;
            };

            this->Properties.Add(CLASS_PROPERTY_HELPER());

            auto &last = this->Properties.GetLast();

            last.Name = PropertyName;
            last.Doc = Doc;
            last.get = getter;
            last.set = setter;

            *(TYPE_OF(&member))&last.offset = member;

            return *this;
        }

        template<typename... ARGS>
        ForceInline PYSTATUS AddToModule(ARGS... args)
        {
            return thiz->AddToModule(args...);
        }
    };

    GrowableArray<REGISTER_CLASS_HELPER> RegisteredClasses;

    template<typename CLASS, typename CTOR>
    REGISTER_CLASS_HELPER& RegisterClass(const String& ClassName, const String& ClassDoc = L"")
    {
        this->RegisteredClasses.Add(REGISTER_CLASS_HELPER(this));

        REGISTER_CLASS_HELPER& cls = this->RegisteredClasses.GetLast();

        cls.Name        = ClassName;
        cls.Doc         = ClassDoc;
        cls.TypeSize    = sizeof       (PyNativeClassHelper<CLASS, CTOR>);
        cls.dtor        = (destructor)  PyNativeClassHelper<CLASS, CTOR>::FreeObject;
        cls.ctor        = (initproc)    PyNativeClassHelper<CLASS, CTOR>::InitObject;
        cls.alloc       =               PyNativeClassHelper<CLASS, CTOR>::AllocObject;

        return cls;
    }

    NoInline PYSTATUS AddToModule(const String& ModuleName/*, const String& Doc = L""*/)
    {
        PYSTATUS    status;
        PyObject*   Module;

        Module = PyImport_AddModuleObject(MlPyObject(PyUnicode_FromUnicode(ModuleName, ModuleName.GetCount())));
        if (Module == nullptr)
            return PYSTATUS_CREATE_MODULE_FAILED;

        status = this->InitFunctions(Module, ModuleName);
        status = PY_SUCCESS(status) ? this->InitClass(Module, ModuleName) : status;

        this->RegisteredFunctions.RemoveAll();
        this->RegisteredClasses.RemoveAll();

        return status;
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

    template<typename RET_TYPE, typename... ARGS>
    NoInline RET_TYPE Invoke(PyObject *object, ARGS... args)
    {
        MlPyObject retval = InvokeInternal(object, L"", args...);
        return PyTypeConverter<PyTypeHelper<RET_TYPE>::VALUE_TYPE>::ToNative(retval);
    }

protected:

    template<typename RET_TYPE>
    struct PyInvokePyHelper
    {
        template<typename... ARGS>
        ForceInline static RET_TYPE Invoke(MlPython* This, const String& ModuleName, const String& FunctionName, ARGS... args)
        {
            MlPyObject retval = This->InvokeModuleMethod(ModuleName, FunctionName, args...);
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
            MlPyObject retval = This->InvokeModuleMethod(ModuleName, FunctionName, args...);
        }
    };

    template<typename... ARGS>
    NoInline PyObject* InvokeModuleMethod(const String& ModuleName, const String& FunctionName, ARGS... args)
    {
        MlPyObject module, tuple, func, value;
        PyCodeObject* code;

        module = Import(ModuleName);
        if (module == nullptr)
        {
            this->SetPyException(String::Format(L"No module named '%s'", ModuleName), PyExc_ImportError);
            return nullptr;
        }

        if (PyErr_Occurred())
        {
            CapturePyException();
            return nullptr;
        }

        func = PyObject_GetAttr(module, MlPyObject(FunctionName));
        if (func == nullptr)
        {
            this->SetPyException(String::Format(L"'%s' object has no attribute '%s'", ModuleName, FunctionName), PyExc_AttributeError);
            return nullptr;
        }

        return InvokeInternal(func, FunctionName, args...);
    }

    template<typename... ARGS>
    NoInline PyObject* InvokeInternal(PyObject *callable, const String& FunctionName, ARGS... args)
    {
        BOOL                InvalidNumberOfArguments;
        PYSTATUS            status;
        MlPyObject          tuple, value;
        PyCodeObject*       code;

        if (PyCallable_Check(callable) == FALSE)
        {
            this->SetPyException(String::Format(L"'%S' object is not callable", callable != nullptr ? Py_TYPE(callable)->tp_name : (PSTR)callable));
            return nullptr;
        }

        code = nullptr;
        InvalidNumberOfArguments = FALSE;
        if (PyFunction_Check(callable))
        {
            code = (PyCodeObject *)PyFunction_GET_CODE(callable);
        }
        else if (PyMethod_Check(callable))
        {
            code = (PyCodeObject *)PyFunction_GET_CODE(PyMethod_GET_FUNCTION(callable));
        }

        if (code != nullptr)
        {
            InvalidNumberOfArguments = FLAG_OFF(code->co_flags, CO_VARARGS | CO_VARKEYWORDS) && code->co_argcount != sizeof...(ARGS);
        }

        if (InvalidNumberOfArguments)
        {
            this->SetPyException(
                String::Format(
                    L"'%S' takes %d argument%s, but %d given",
                    PyEval_GetFuncName(callable),
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

        value = PyObject_CallObject(callable, tuple);
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
        return PYSTATUS_SUCCESS;
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

    NoInline PYSTATUS InitFunctions(PyObject* Module, const String& ModuleName)
    {
        for (auto &func : this->RegisteredFunctions)
        {
            BOOL Success = FALSE;

            PyTypeObject wraptype =
            {
                PyVarObject_HEAD_INIT(&PyType_Type, 0)
                nullptr,                                            /* tp_name */
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
                nullptr,                                            /* tp_methods */
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

            auto& type = this->AddType(&wraptype, func.Name + WRAP_CLASS_SUFFIX);

            LOOP_ONCE
            {
                MlPyObject args, obj, method;

                if (PyType_Ready(&type) != 0)
                    break;

                PyMethodDef methoddef = PY_ADD_METHOD(nullptr, func.Native, METH_VARARGS);

                PyAddRef((PyObject *)&type);

                AddMethod(&type, &methoddef, func.Name, func.Doc);
                //MlPyObject wrapper = CreateWrapper(Py_TYPE(Module), &methoddef, func.Name, func.Doc);
                //PyObject_SetAttr(Module, MlPyObject(func.Name), wrapper);
                //break;

                //if (PyModule_AddObject(Module, type.tp_name, (PyObject *)&type) != 0)
                //    break;

                args = Py_BuildValue("(Ou)", func.Address, func.Name);
                if (args == nullptr)
                    break;

                obj = PyObject_CallObject((PyObject *)&type, args);
                if (obj == nullptr)
                    break;

                MlPyObject name = PyUnicode_FromUnicode(func.Name, func.Name.GetCount());

                method = PyObject_GetAttr(obj, name);
                if (method == nullptr)
                    break;

                if (PyObject_SetAttr(Module, name, method) != 0)
                    break;

                Success = TRUE;
            }
        }

        this->RegisteredFunctions.RemoveAll();

        return PYSTATUS_SUCCESS;
    }

    NoInline PYSTATUS InitClass(PyObject* Module, const String& ModuleName)
    {
        for (auto &cls : this->RegisteredClasses)
        {
            BOOL Success = FALSE;

            PyTypeObject classtype =
            {
                PyVarObject_HEAD_INIT(&PyType_Type, 0)
                nullptr,                                            /* tp_name */
                cls.TypeSize,                                       /* tp_size */
                0,                                                  /* tp_itemsize */
                cls.dtor,                                           /* tp_dealloc */
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
                nullptr,                                            /* tp_doc */
                nullptr,                                            /* tp_traverse */
                nullptr,                                            /* tp_clear */
                nullptr,                                            /* tp_richcompare */
                0,                                                  /* tp_weaklistoffset */
                nullptr,                                            /* tp_iter */
                nullptr,                                            /* tp_iternext */
                nullptr,                                            /* tp_methods */
                nullptr,                                            /* tp_members */
                nullptr,                                            /* tp_getset */
                &PyBaseObject_Type,                                 /* tp_base */
                nullptr,                                            /* tp_dict */
                nullptr,                                            /* tp_descr_get */
                nullptr,                                            /* tp_descr_set */
                0,                                                  /* tp_dictoffset */
                cls.ctor,                                           /* tp_init */
                nullptr,                                            /* tp_alloc */
                cls.alloc,                                          /* tp_new */
                nullptr,                                            /* tp_free */
            };

            auto& type = this->AddType(&classtype, cls.Name, cls.Doc);

            PyAddRef((PyObject *)&type);
            if (PyType_Ready(&type) != 0)
                continue;

            Success = TRUE;

            for (auto &method : cls.Methods)
            {
                auto caller = [](PyObject *self, PyObject *args, PVOID wrapped) -> PyObject*
                {
                    typedef ml::Function<PyCFunction> FUNC;
                    return (*(FUNC *)((MlWrapperBase *)wrapped)->method)(self, args);
                };

                PyMethodDef meth = PY_ADD_METHOD(nullptr, method.Address, METH_VARARGS);
                AddMethod(&type, &meth, method.Name, method.Doc, caller);
            }

            for (auto &prop : cls.Properties)
            {
                PyGetSetDef getset = { nullptr, prop.get, prop.set, nullptr, (PVOID)prop.offset };
                AddGetSet(&type, &getset, prop.Name, prop.Doc);
            }

            if (Success == FALSE)
                continue;

            if (PyModule_AddObject(Module, cls.Name.Encode(CP_UTF8), (PyObject *)&type) != 0)
                break;
        }

        this->RegisteredClasses.RemoveAll();

        return PYSTATUS_SUCCESS;
    }

    NoInline MlPyTypeObject& AddType(PyTypeObject *Type, const String& TypeName, const String& TypeDoc = L"")
    {
        this->RegisteredTypeObjects.Add(Type);

        auto &last = this->RegisteredTypeObjects.GetLast();

        StringToAnsi(*(PSTR*)&last.tp_name, TypeName);
        StringToAnsi(*(PSTR*)&last.tp_doc, TypeDoc);

        return last;
    }

    NoInline PYSTATUS AddMethod(PyTypeObject *Type, PyMethodDef *Method, const String& MethodName, const String& Doc, wrapperfunc WrapperCaller = nullptr)
    {
        MlPyObject wrapper = CreateWrapper(Type, Method->ml_meth, MethodName, Doc, WrapperCaller);

        if (wrapper == nullptr)
            return PYSTATUS_CREATE_OBJECT_FAILED;

        PyDict_SetItem(Type->tp_dict, MlPyObject(MethodName), wrapper);

        return PYSTATUS_SUCCESS;
    }

    NoInline PYSTATUS AddGetSet(PyTypeObject *Type, PyGetSetDef *GetSet, const String& PropertyName, const String& Doc)
    {
        MlPyObject name = PropertyName;

        if (PyDict_GetItem(Type->tp_dict, name))
            return PYSTATUS_SUCCESS;

        this->RegisteredGetSets.Add(GetSet);

        auto& gsp = this->RegisteredGetSets.GetLast();

        StringToAnsi(gsp.name, PropertyName);
        StringToAnsi(gsp.doc, Doc);

        MlPyObject descr = PyDescr_NewGetSet(Type, &gsp);

        PyDict_SetItem(Type->tp_dict, MlPyObject(PropertyName), descr);

        return PYSTATUS_SUCCESS;
    }

    PyObject* CreateWrapper(PyTypeObject *Type, PyCFunction Method, const String& MethodName, const String& Doc, wrapperfunc WrapperCaller = nullptr)
    {
        auto caller = [](PyObject *self, PyObject *args, PVOID wrapped) -> PyObject*
        {
            return ((MlWrapperBase *)wrapped)->method(self, args);
        };

        wrapperbase wrapper =
        {
            nullptr,
            0,
            nullptr,
            WrapperCaller == nullptr ? caller : WrapperCaller,
            nullptr,
            0,
            nullptr,
        };

        this->RegisteredWrappers.Add(&wrapper);

        auto &last = this->RegisteredWrappers.GetLast();
        last.method = Method;

        StringToAnsi(last.name, MethodName);
        StringToAnsi(last.doc, Doc);

        return PyDescr_NewWrapper(Type, &last, &last);
    }

    NoInline static VOID StringToAnsi(PSTR &ansi, const String& str)
    {
        if (!str)
        {
            ansi = "";
            return;
        }

        const auto &doc = str.Encode(CP_UTF8);

        ansi = new CHAR[doc.GetSize()];
        if (ansi != nullptr)
        {
            CopyMemory(ansi, doc.GetData(), doc.GetSize());
        }
        else
        {
            ansi = "ansi out of memory";
        }
    }

    NoInline static VOID DestroyAnsi(PSTR &ansi)
    {
        SafeDeleteT(ansi);
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

        return PYSTATUS_SUCCESS;
    }
};

#endif // _MLPYTHON_H_13f13917_f5da_49af_b443_052ccfc01ea9_
