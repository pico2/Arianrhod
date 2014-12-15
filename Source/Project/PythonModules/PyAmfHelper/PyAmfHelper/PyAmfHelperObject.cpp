#include "Stdafx.h"

#pragma warning(push)
#pragma warning(disable:4127)

NoInline VOID PyAddRef(PyObject *Object)
{
    Py_XINCREF(Object);
}

NoInline VOID PyRelease(PyObject *Object)
{
    Py_XDECREF(Object);
}

#pragma warning(pop)


PyModuleDef PyAmfHelperModule =
{
    PyModuleDef_HEAD_INIT,
    PY_AMF_HELPER_MODULE,
    "",
    -1,
};

PyMODINIT_FUNC PyInit_PyAmfHelper()
{
    PyObject* Module;

    PyTypeObject **Type, *Types[] =
    {
        &PyAMFSerializer_Type,
        &PyAMFDeserializer_Type,
    };

    Module = PyModule_Create(&PyAmfHelperModule);
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
