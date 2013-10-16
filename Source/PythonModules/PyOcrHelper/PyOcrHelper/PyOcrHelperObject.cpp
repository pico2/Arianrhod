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

HANDLE CreateSection()
{
    NTSTATUS            Status;
    WCHAR               SectionNameBuffer[MAX_NTPATH];
    OBJECT_ATTRIBUTES   ObjectAttributes;
    UNICODE_STRING      BaseNamedObjectsName;
    HANDLE              SectionHandle, BaseNamedObjects;
    ULONG_PTR           SessionId;
    LARGE_INTEGER       MaximumSize;

    SessionId = GetSessionId(CurrentProcess);
    if (SessionId == INVALID_SESSION_ID)
        return nullptr;

    BaseNamedObjectsName.Length         = (USHORT)swprintf(SectionNameBuffer, L"\\Sessions\\%d\\BaseNamedObjects", SessionId) * sizeof(WCHAR);
    BaseNamedObjectsName.MaximumLength  = BaseNamedObjectsName.Length;
    BaseNamedObjectsName.Buffer         = SectionNameBuffer;

    InitializeObjectAttributes(&ObjectAttributes, &BaseNamedObjectsName, OBJ_CASE_INSENSITIVE, nullptr, nullptr);
    Status = NtOpenDirectoryObject(&BaseNamedObjects, DIRECTORY_ALL_ACCESS, &ObjectAttributes);
    if (NT_FAILED(Status))
        return nullptr;

    InitializeObjectAttributes(&ObjectAttributes, nullptr, OBJ_INHERIT, nullptr, nullptr);

    MaximumSize.QuadPart = 0x1000;
    Status = NtCreateSection(
                &SectionHandle,
                SECTION_ALL_ACCESS,
                &ObjectAttributes,
                &MaximumSize,
                PAGE_READWRITE,
                SEC_COMMIT,
                nullptr
            );

    NtClose(BaseNamedObjects);

    if (NT_FAILED(Status))
        return nullptr;

    return SectionHandle;
}

NTSTATUS InvokeOcrHelper(const ml::String &CmdLine, ml::String &OcrResult)
{
    NTSTATUS            Status;
    HANDLE              StdoutRead, StdoutWrite, StdoutWrite2;
    SECURITY_ATTRIBUTES PipeAttributes;
    STARTUPINFOW        StartupInfo;
    PROCESS_INFORMATION ProcessInfo;
    WCHAR               Buffer[0x1000];
    LARGE_INTEGER       BytesRead, TimeOut;

    PipeAttributes.nLength = sizeof(PipeAttributes);
    PipeAttributes.bInheritHandle = FALSE;
    PipeAttributes.lpSecurityDescriptor = nullptr;

    //FAIL_RETURN(Io::CreateNamedPipe(&StdoutRead, &StdoutWrite, nullptr, &PipeAttributes));
    //FAIL_RETURN(Io::CreateNamedPipe(&StdinRead, &StdinWrite, nullptr, &PipeAttributes));
    CreatePipe(&StdoutRead, &StdoutWrite, &PipeAttributes, 0);

    NtDuplicateObject(CurrentProcess, StdoutWrite, CurrentProcess, &StdoutWrite2, 0, OBJ_INHERIT, DUPLICATE_SAME_ACCESS);

    PrintConsole(L"%p\n", StdoutWrite);

    ZeroMemory(&StartupInfo, sizeof(StartupInfo));
    StartupInfo.cb          = sizeof(StartupInfo);
    StartupInfo.dwFlags     = STARTF_USESTDHANDLES;
    StartupInfo.hStdOutput  = StdoutWrite2;
    StartupInfo.wShowWindow = SW_HIDE;

    Status = Ps::CreateProcessW(
                nullptr,
                String::Format(L"%s %s", CmdLine, L"STD_OUTPUT_IS_PIPE"),
                nullptr,
                0,
                &StartupInfo,
                &ProcessInfo
            );
    if (NT_FAILED(Status))
    {
        NtClose(StdoutRead);
        NtClose(StdoutWrite);

        return Status;
    }

    NtWaitForSingleObject(ProcessInfo.hProcess, FALSE, nullptr);
    NtClose(ProcessInfo.hProcess);
    NtClose(ProcessInfo.hThread);

    FormatTimeOut(&TimeOut, 1);

    ULONG aval;

    while (PeekNamedPipe(StdoutRead, nullptr, 0, nullptr, &aval, nullptr) != FALSE && aval != 0)
    {
        ReadFile(StdoutRead, Buffer, aval, &BytesRead.LowPart, nullptr);

        *PtrAdd(Buffer, BytesRead.LowPart) = 0;
        OcrResult += Buffer;
        PrintConsole(L"%s\n", OcrResult);
    }

    NtClose(StdoutRead);
    NtClose(StdoutWrite);
    NtClose(StdoutWrite2);

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
