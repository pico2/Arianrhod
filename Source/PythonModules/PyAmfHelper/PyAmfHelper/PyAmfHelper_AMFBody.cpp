#include "Stdafx.h"

PyObject* PyAMFBody_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    PPyAmfHelper_AMFBody self;

    self = (PPyAmfHelper_AMFBody)type->tp_alloc(type, 0);
    if (self == nullptr)
        return *self;

    self->IsEmptyTarget             = TRUE;
    self->IgnoreResults             = FALSE;
    self->IsAuthenticationAction    = FALSE;

    self->Target    = (PyUnicodeObject *)PyUnicode_FromUnicode(L"", 0);
    self->Response  = (PyUnicodeObject *)PyUnicode_FromUnicode(L"", 0);
    self->Content   = (PyDictObject *)PyDict_New();

    return *self;
}

VOID PyAMFBody_dealloc(PPyAmfHelper_AMFBody self)
{
    PyRelease((PyObject *)self->Target);
    PyRelease((PyObject *)self->Response);
    PyRelease((PyObject *)self->Content);

    Py_TYPE(self)->tp_free(self);
}

PY_DEFINE_GET_BOOLEAN(PyAmfHelper_AMFBody, IsEmptyTarget);
PY_DEFINE_SET_BOOLEAN(PyAmfHelper_AMFBody, IsEmptyTarget);

PY_DEFINE_GET_BOOLEAN(PyAmfHelper_AMFBody, IsAuthenticationAction);
PY_DEFINE_SET_BOOLEAN(PyAmfHelper_AMFBody, IsAuthenticationAction);

PY_DEFINE_GET_BOOLEAN(PyAmfHelper_AMFBody, IgnoreResults);
PY_DEFINE_SET_BOOLEAN(PyAmfHelper_AMFBody, IgnoreResults);

PY_DEFINE_GET_OBJECT(PyAmfHelper_AMFBody,  Target);
PY_DEFINE_SET_OBJECT(PyAmfHelper_AMFBody,  Target, PyUnicode_Type);

PY_DEFINE_GET_OBJECT(PyAmfHelper_AMFBody,  Response);
PY_DEFINE_SET_OBJECT(PyAmfHelper_AMFBody,  Response, PyUnicode_Type);

PY_DEFINE_GET_OBJECT(PyAmfHelper_AMFBody,  Content);
PY_DEFINE_SET_OBJECT(PyAmfHelper_AMFBody,  Content, PyDict_Type);

PyGetSetDef PyAMFBody_GetSetList[] =
{
    PY_ADD_GET_SET(PyAmfHelper_AMFBody, IsEmptyTarget),
    PY_ADD_GET_SET(PyAmfHelper_AMFBody, IsAuthenticationAction),
    PY_ADD_GET_SET(PyAmfHelper_AMFBody, IgnoreResults),

    PY_ADD_GET_SET(PyAmfHelper_AMFBody, Target),
    PY_ADD_GET_SET(PyAmfHelper_AMFBody, Response),
    PY_ADD_GET_SET(PyAmfHelper_AMFBody, Content),

    { },
};

PyMemberDef PyAMFBody_Member[] =
{
    PY_ADD_MEMBER("Target",    T_OBJECT, FIELD_OFFSET(PyAmfHelper_AMFBody, Target),    0),
    PY_ADD_MEMBER("Response",  T_OBJECT, FIELD_OFFSET(PyAmfHelper_AMFBody, Response),  0),
    PY_ADD_MEMBER("Content",   T_OBJECT, FIELD_OFFSET(PyAmfHelper_AMFBody, Content),   0),
};

PyTypeObject PyAMFBody_Type =
{
    PyVarObject_HEAD_INIT(&PyType_Type, 0)
    "PyAMFBody",                                        /* tp_name */
    sizeof(PyAmfHelper_AMFBody),                        /* tp_size */
    0,                                                  /* tp_itemsize */
    (destructor)PyAMFBody_dealloc,                      /* tp_dealloc */
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
    "PyAMFBody Object",                                 /* tp_doc */
    0,                                                  /* tp_traverse */
    0,                                                  /* tp_clear */
    0,                                                  /* tp_richcompare */
    0,                                                  /* tp_weaklistoffset */
    0,                                                  /* tp_iter */
    0,                                                  /* tp_iternext */
    0,                                    /* tp_methods */
    0,                                                  /* tp_members */
    PyAMFBody_GetSetList,                               /* tp_getset */
    &PyBaseObject_Type,                                 /* tp_base */
    0,                                                  /* tp_dict */
    0,                                                  /* tp_descr_get */
    0,                                                  /* tp_descr_set */
    0,                                                  /* tp_dictoffset */
    0,                                                  /* tp_init */
    0,                                                  /* tp_alloc */
    PyAMFBody_new,                                      /* tp_new */
    PyObject_Del,                                       /* tp_free */
};
