#include "PyOcrHelper.h"

typedef struct PyOcrHelper : public PyObjectBase
{

} PyOcrHelper, *PPyOcrHelper;


PyObject* PyOcrHelper_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    PPyOcrHelper self;

    self = (PPyOcrHelper)type->tp_alloc(type, 0);
    if (self == nullptr)
        return *self;

    return *self;
}

VOID PyOcrHelper_dealloc(PPyOcrHelper self)
{
    Py_TYPE(self)->tp_free(self);
}

NTSTATUS InvokeOcrHelper(const ml::String &CmdLine, ml::String &OcrResult)
{
    NTSTATUS            Status;
    HANDLE              PipeRead, PipeWrite;
    SECURITY_ATTRIBUTES PipeAttributes;
    STARTUPINFOW        StartupInfo;
    PROCESS_INFORMATION ProcessInfo;
    WCHAR               Buffer[0x1000];
    LARGE_INTEGER       BytesRead;

    PipeAttributes.nLength = sizeof(PipeAttributes);
    PipeAttributes.bInheritHandle = TRUE;
    PipeAttributes.lpSecurityDescriptor = nullptr;

    //FAIL_RETURN(Io::CreateNamedPipe(&PipeRead, &PipeWrite, nullptr, &PipeAttributes));
    CreatePipe(&PipeRead, &PipeWrite, &PipeAttributes, 0);

    PrintConsole(L"%p\n", PipeWrite);

    ZeroMemory(&StartupInfo, sizeof(StartupInfo));
    StartupInfo.cb          = sizeof(StartupInfo);
    StartupInfo.dwFlags     = STARTF_USESTDHANDLES | STARTF_USESHOWWINDOW;
    StartupInfo.hStdInput   = PipeWrite;
    StartupInfo.hStdOutput  = PipeWrite;
    StartupInfo.hStdError   = PipeWrite;
    StartupInfo.wShowWindow = SW_HIDE;

    Status = Ps::CreateProcessW(nullptr, CmdLine, nullptr, 0, &StartupInfo, &ProcessInfo);
    if (NT_FAILED(Status))
    {
        NtClose(PipeRead);
        NtClose(PipeWrite);

        return Status;
    }

    NtWaitForSingleObject(ProcessInfo.hProcess, FALSE, nullptr);
    NtClose(ProcessInfo.hProcess);
    NtClose(ProcessInfo.hThread);

    while (NT_SUCCESS(NtFileDisk::Read(PipeRead, Buffer, sizeof(Buffer), &BytesRead)))
    {
        *PtrAdd(Buffer, BytesRead.QuadPart) = 0;
        OcrResult += Buffer;
    }

    NtClose(PipeRead);
    NtClose(PipeWrite);

    return STATUS_SUCCESS;
}

PyObject* PyOcrHelper_Ocr(PyObject *self, PyObject *args, PyObject *kwargs)
{
    NTSTATUS        Status;
    PyObject*       PyTiffPath;
    PCWSTR          TiffPath;
    UNICODE_STRING  SelfPath;
    PLDR_MODULE     Self;

    static PSTR kwlist[] = { "TiffPath", nullptr };

    if (PyArg_ParseTupleAndKeywords(args, kwargs, "O", kwlist, &PyTiffPath) == FALSE)
        return nullptr;

    PyAddRef(PyTiffPath);

    TiffPath = PyUnicode_AsUnicode(PyTiffPath);

    ml::String CmdLine, OcrResult;

    Self = FindLdrModuleByHandle(&__ImageBase);

    SelfPath = Self->FullDllName;
    SelfPath.Length -= Self->BaseDllName.Length;

    CmdLine = ml::String::Format(L"\"%wZModiOcrHelper.exe\" \"%s\"", &SelfPath, TiffPath);
    PyRelease(PyTiffPath);

    Status = InvokeOcrHelper(CmdLine, OcrResult);

    if (NT_FAILED(Status))
    {
        Py_RETURN_NONE;
    }

    return PyUnicode_FromUnicode(OcrResult, OcrResult.GetCount());
}


PyMethodDef PyOcrHelper_Methods[] =
{
    PY_ADD_METHOD("Ocr", PyOcrHelper_Ocr, METH_VARARGS | METH_KEYWORDS),

    PY_ADD_METHOD_END
};


PyTypeObject PyOcrHelper_Type =
{
    PyVarObject_HEAD_INIT(&PyType_Type, 0)
    "PyOcrHelper",                                      /* tp_name */
    sizeof(PyOcrHelper),                                /* tp_size */
    0,                                                  /* tp_itemsize */
    (destructor)PyOcrHelper_dealloc,                    /* tp_dealloc */
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
    "PyOcrHelper Object",                               /* tp_doc */
    0,                                                  /* tp_traverse */
    0,                                                  /* tp_clear */
    0,                                                  /* tp_richcompare */
    0,                                                  /* tp_weaklistoffset */
    0,                                                  /* tp_iter */
    0,                                                  /* tp_iternext */
    PyOcrHelper_Methods,                                /* tp_methods */
    0,                                                  /* tp_members */
    0,                                                  /* tp_getset */
    &PyBaseObject_Type,                                 /* tp_base */
    0,                                                  /* tp_dict */
    0,                                                  /* tp_descr_get */
    0,                                                  /* tp_descr_set */
    0,                                                  /* tp_dictoffset */
    0,                                                  /* tp_init */
    0,                                                  /* tp_alloc */
    PyOcrHelper_new,                                    /* tp_new */
    PyObject_Del,                                       /* tp_free */
};


PyModuleDef PyOcrHelperModule =
{
    PyModuleDef_HEAD_INIT,
    PY_OCR_HELPER_MODULE,
    "",
    -1,
};

PyMODINIT_FUNC PyInit_PyOcrHelper()
{
    PyObject* Module;

    PyTypeObject **Type, *Types[] =
    {
        &PyOcrHelper_Type,
    };

    Module = PyModule_Create(&PyOcrHelperModule);
    if (Module == nullptr)
        return nullptr;

    FOR_EACH_ARRAY(Type, Types)
    {
        if (PyType_Ready(*Type) < 0)
            break;

        PyAddRef((PyObject *)*Type);
        PyModule_AddObject(Module, (*Type)->tp_name, (PyObject *)(*Type));
    }

    if (Type == &Types[countof(Types)])
        return Module;

    for (; Type != &Types[-1]; --Type)
    {
        PyRelease((PyObject *)*Type);
    }

    PyRelease(Module);

    return nullptr;
}
