#include "Stdafx.h"
#include "PyAmfHelperObject.h"

using namespace FluorineFx;
using namespace FluorineFx::AMF3;
using namespace FluorineFx::IO;
using namespace System;
using namespace System::IO;
using namespace System::Reflection;
using namespace System::Runtime::InteropServices;
using namespace System::Collections::Generic;

/************************************************************************
managed function
************************************************************************/

Object^ PyObjectToObject(PyObject *pyobj);

Object^ PyArrayToArrayT(API_POINTER(PyList_GetItem) GetItem, PyObject *pyarray, Py_ssize_t Size)
{
    PyObject *item;
    ArrayCollection ^arr = gcnew ArrayCollection();

    for (Py_ssize_t Index = 0; Index != Size; ++Index)
    {
        item = GetItem(pyarray, Index);
        arr->Add(PyObjectToObject(item));
    }

    return arr;
}

Object^ PyListToArray(PyObject *pyarray)
{
    return PyArrayToArrayT(PyList_GetItem, pyarray, PyList_Size(pyarray));
}

Object^ PyTupleToArray(PyObject *pyarray)
{
    return PyArrayToArrayT(PyTuple_GetItem, pyarray, PyTuple_Size(pyarray));
}

Object^ PyDictToDictionary(PyObject *pydict)
{
    ASObject^ object;
    PyObject *Key, *Value;
    Py_ssize_t Position;

    object = gcnew ASObject();

    Position = 0;
    while (PyDict_Next(pydict, &Position, &Key, &Value))
    {
        object->Add(gcnew String(PyUnicode_AsUnicode(Key)), PyObjectToObject(Value));
    }

    return object;
}

Object^ PyObjectToObject(PyObject *pyobj)
{
    Object ^object;
    PyTypeObject *type;

    type = Py_TYPE(pyobj);

    if (type == &PyUnicode_Type)
    {
        object = gcnew String(PyUnicode_AsUnicode(pyobj));
    }
    else if (type == &PyList_Type)
    {
        object = PyListToArray(pyobj);
    }
    else if (type == &PyTuple_Type)
    {
        object = PyTupleToArray(pyobj);
    }
    else if (type == &PyDict_Type)
    {
        object = PyDictToDictionary(pyobj);
    }
    else if (type == &PyBool_Type)
    {
        object = gcnew Boolean(pyobj == Py_True);
    }
    else if (type == &PyFloat_Type)
    {
        object = gcnew System::Double(PyFloat_AsDouble(pyobj));
    }
    else if (type == &PyLong_Type)
    {
        object = gcnew System::Int64(PyLong_AsSsize_t(pyobj));
    }
    else if (pyobj == Py_None)
    {
        object = nullptr;
    }
    else
    {
        throw gcnew Exception(String::Format(L"unknown py object type: {0}", gcnew String(type->tp_name)));
    }

    return object;
}

NTSTATUS InitializePyAmfBodies(AMFMessage^ Message, PyObject *BodyList)
{
    NTSTATUS Status;
    PyObject *PyBody;
    PyObject *Content, *Target, *Response;

    PyBody      = nullptr;
    Content     = nullptr;
    Target      = nullptr;
    Response    = nullptr;

    SCOPE_EXIT
    {
        PyRelease(PyBody);
        PyRelease(Content);
        PyRelease(Target);
        PyRelease(Response);
    }
    SCOPE_EXIT_END;

    for (ULONG_PTR Index = 0, Count = PyList_Size(BodyList); Index != Count; ++Index)
    {
        PyBody = PyList_GetItem(BodyList, Index);
        if (PyBody == nullptr)
            return STATUS_UNSUCCESSFUL;

        AMFBody^ Body = gcnew AMFBody;

        Target = PyObject_GetAttrString(PyBody, "_Target");
        if (Target == nullptr)
            return STATUS_UNSUCCESSFUL;

        Body->Target = gcnew String(PyUnicode_AsUnicode(Target));

        PyRelease(Target);
        Target = nullptr;

        Response = PyObject_GetAttrString(PyBody, "_Response");
        if (Response == nullptr)
            return STATUS_UNSUCCESSFUL;

        Body->Response = gcnew String(PyUnicode_AsUnicode(Response));

        PyRelease(Response);
        Response = nullptr;

        Content = PyObject_GetAttrString(PyBody, "_Content");
        if (Content == nullptr)
            return STATUS_UNSUCCESSFUL;

        Body->Content = PyObjectToObject(Content);
        Message->AddBody(Body);
    }

    return STATUS_SUCCESS;
}

PyObject* PyAMFSerializer_WriteMessage_Managed(PyObject *self, PyObject *args, PyObject *kwargs)
{
    BOOL        Success;
    NTSTATUS    Status;
    PyObject    *PyAmfMessage, *PyAmfMessageVersion, *PyAmfHeaders, *PyAmfBodies;
    PyObject    *Package;

    static PSTR kwlist[] = { "Message", nullptr };

    if (PyArg_ParseTupleAndKeywords(args, kwargs, "O", kwlist, &PyAmfMessage) == FALSE)
        return nullptr;

    Success = FALSE;

    PyAmfMessageVersion = nullptr;
    PyAmfHeaders        = nullptr;
    PyAmfBodies         = nullptr;

    SCOPE_EXIT
    {
        PyRelease(PyAmfMessageVersion);
        PyRelease(PyAmfHeaders);
        PyRelease(PyAmfBodies);
    }
    SCOPE_EXIT_END;

    LOOP_ONCE
    {
        PyAmfMessageVersion = PyObject_GetAttrString(PyAmfMessage, "_Version");
        if (PyAmfMessageVersion == nullptr)
            break;

        PyAmfHeaders = PyObject_GetAttrString(PyAmfMessage, "_Headers");
        if (PyAmfMessageVersion == nullptr)
            break;

        PyAmfBodies = PyObject_GetAttrString(PyAmfMessage, "_Bodies");
        if (PyAmfMessageVersion == nullptr)
            break;

        Success = TRUE;
    }

    if (Success == FALSE)
    {
        return nullptr;
    }

    PCHAR           Buffer;
    AMFMessage^     message = gcnew AMFMessage();
    MemoryStream^   stream  = gcnew MemoryStream();
    AMFSerializer^  ser     = gcnew AMFSerializer(stream);

    Success = FALSE;

    LOOP_ONCE
    {
        Status = InitializePyAmfBodies(message, PyAmfBodies);
        FAIL_BREAK(Status);

        ser->WriteMessage(message);

        Success = TRUE;
    }

    if (Success == FALSE)
        return nullptr;

    Buffer = (PCHAR)AllocateMemoryP(stream->Length);
    if (Buffer == nullptr)
        return nullptr;

    Marshal::Copy(stream->ToArray(), 0, (IntPtr)Buffer, stream->Length);

    Package = PyBytes_FromStringAndSize(Buffer, stream->Length);

    FreeMemoryP(Buffer);

    return Package;
}
