#include "stdafx.h"

PyModuleDef PyInlineHookModule =
{
    PyModuleDef_HEAD_INIT,
    "PyInlineHook",
    "",
    -1,
};

PyMODINIT_FUNC PyInit_PyInlineHook()
{
    PyObject* Module;

    PyTypeObject *Type, Types[] =
    {
        PyInlineHook_Process_CreateType(),
    };

    Module = PyModule_Create(&PyInlineHookModule);
    if (Module == nullptr)
        return nullptr;

    FOR_EACH_ARRAY(Type, Types)
    {
        if (PyType_Ready(Type) < 0)
            break;

        PyAddRef((PyObject *)Type);
        PyModule_AddObject(Module, (Type)->tp_name, (PyObject *)(Type));
    }

    if (Type == &Types[countof(Types)])
        return Module;

    for (; Type != &Types[-1]; --Type)
    {
        PyRelease((PyObject *)Type);
    }

    PyRelease(Module);

    return nullptr;
}


BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    ml::MlInitialize();

    return TRUE;
}

BOOL WINAPI DllMain(PVOID BaseAddress, ULONG Reason, PVOID Reserved)
{
    switch (Reason)
    {
        case DLL_PROCESS_ATTACH:
            return Initialize(BaseAddress) || UnInitialize(BaseAddress);

        case DLL_PROCESS_DETACH:
            UnInitialize(BaseAddress);
            break;
    }

    return TRUE;
}
