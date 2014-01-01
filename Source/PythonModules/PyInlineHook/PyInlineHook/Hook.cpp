#include "stdafx.h"

typedef struct PY_INLINE_HOOK_HOOK :public PyObjectBase
{

} PY_INLINE_HOOK_HOOK, *PPY_INLINE_HOOK_HOOK;


PyObject* PyInlineHook_Hook_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    PPY_INLINE_HOOK_HOOK self;

    self = (PPY_INLINE_HOOK_HOOK)type->tp_alloc(type, 0);
    if (self == nullptr)
        return *self;

    new (self) PY_INLINE_HOOK_HOOK;

    return *self;
}

VOID PyInlineHook_Hook_dealloc(PPY_INLINE_HOOK_HOOK self)
{
    Py_TYPE(self)->tp_free(self);
}

/************************************************************************
  methods
  ************************************************************************/

PyObject* PyInlineHook_Hook_Patch(PyObject *self, PyObject *args, PyObject *kwargs)
{
    PyObject *PyAddress, *PyLength;
    PVOID64 Address;
    ULONG64 Length;

    static PSTR kwlist[] = { "Address", "Length", nullptr };

    if (PyArg_ParseTupleAndKeywords(args, kwargs, "KK", kwlist, &PyAddress, &PyLength) == FALSE)
        return nullptr;

    Py_RETURN_NONE;
}

PyObject* PyInlineHook_Hook_Restore(PyObject *self, PyObject *args, PyObject *kwargs)
{
    PyObject *PyAddress, *PyLength, *PyBuffer;
    PVOID64 Address;
    ULONG64 Length;
    PBYTE   Buffer;

    static PSTR kwlist[] = { "Address", "Length", "Buffer", nullptr };

    if (PyArg_ParseTupleAndKeywords(args, kwargs, "KK", kwlist, &PyAddress, &PyLength, &PyBuffer) == FALSE)
        return nullptr;

    Py_RETURN_NONE;
}


PyTypeObject PyInlineHook_Hook_CreateType()
{
    static PyMethodDef PyInlineHook_Hook_Methods[] =
    {
        PY_ADD_METHOD("Patch",      PyInlineHook_Hook_Patch,    METH_VARARGS | METH_KEYWORDS),
        PY_ADD_METHOD("Restore",    PyInlineHook_Hook_Restore,  METH_VARARGS | METH_KEYWORDS),

        PY_ADD_METHOD_END
    };

    PyTypeObject PyInlineHook_Hook_Type =
    {
        PyVarObject_HEAD_INIT(&PyType_Type, 0)
        "PyInlineHook.Hook",                                /* tp_name */
        sizeof(PY_INLINE_HOOK_HOOK),                        /* tp_size */
        0,                                                  /* tp_itemsize */
        (destructor)PyInlineHook_Hook_dealloc,              /* tp_dealloc */
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
        "PyInlineHook.Hook Object",                         /* tp_doc */
        0,                                                  /* tp_traverse */
        0,                                                  /* tp_clear */
        0,                                                  /* tp_richcompare */
        0,                                                  /* tp_weaklistoffset */
        0,                                                  /* tp_iter */
        0,                                                  /* tp_iternext */
        PyInlineHook_Hook_Methods,                          /* tp_methods */
        0,                                                  /* tp_members */
        0,                                                  /* tp_getset */
        &PyBaseObject_Type,                                 /* tp_base */
        0,                                                  /* tp_dict */
        0,                                                  /* tp_descr_get */
        0,                                                  /* tp_descr_set */
        0,                                                  /* tp_dictoffset */
        0,                                                  /* tp_init */
        0,                                                  /* tp_alloc */
        PyInlineHook_Hook_new,                              /* tp_new */
        PyObject_Del,                                       /* tp_free */
    };

    return PyInlineHook_Hook_Type;
}
