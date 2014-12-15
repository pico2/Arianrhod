#include "Stdafx.h"
#include "PyAmfHelperObject.h"

/************************************************************************
native funtions
************************************************************************/

PyObject* PyAMFSerializer_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    PPyAmfHelper_AMFSerializer self;

    self = (PPyAmfHelper_AMFSerializer)type->tp_alloc(type, 0);
    if (self == nullptr)
        return *self;

    return *self;
}

VOID PyAMFSerializer_dealloc(PPyAmfHelper_AMFSerializer self)
{
    Py_TYPE(self)->tp_free(self);
}

PyObject* PyAMFSerializer_WriteMessage(PyObject *self, PyObject *args, PyObject *kwargs)
{
    return PyAMFSerializer_WriteMessage_Managed(self, args, kwargs);
}

PyMethodDef PyAMFSerializer_Methods[] =
{
    PY_ADD_METHOD("WriteMessage", PyAMFSerializer_WriteMessage, METH_VARARGS | METH_KEYWORDS),

    PY_ADD_METHOD_END
};

PyTypeObject PyAMFSerializer_Type =
{
    PyVarObject_HEAD_INIT(&PyType_Type, 0)
    "PyAMFSerializer",                                  /* tp_name */
    sizeof(PyAmfHelper_AMFSerializer),                  /* tp_size */
    0,                                                  /* tp_itemsize */
    (destructor)PyAMFSerializer_dealloc,                /* tp_dealloc */
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
    "PyAMFSerializer Object",                           /* tp_doc */
    0,                                                  /* tp_traverse */
    0,                                                  /* tp_clear */
    0,                                                  /* tp_richcompare */
    0,                                                  /* tp_weaklistoffset */
    0,                                                  /* tp_iter */
    0,                                                  /* tp_iternext */
    PyAMFSerializer_Methods,                            /* tp_methods */
    0,                                                  /* tp_members */
    0,                                                  /* tp_getset */
    &PyBaseObject_Type,                                 /* tp_base */
    0,                                                  /* tp_dict */
    0,                                                  /* tp_descr_get */
    0,                                                  /* tp_descr_set */
    0,                                                  /* tp_dictoffset */
    0,                                                  /* tp_init */
    0,                                                  /* tp_alloc */
    PyAMFSerializer_new,                                /* tp_new */
    PyObject_Del,                                       /* tp_free */
};
