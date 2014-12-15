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

//#define PrintLog(...) PrintConsole(__VA_ARGS__)
#define PrintLog(...)

/************************************************************************
managed function
************************************************************************/

PyObject* ObjectToPyObject(Object ^object);

PyObject* StringToPyUnicode(String ^str)
{
    PyObject *unicode;
    IntPtr ptr;

    ptr = Marshal::StringToHGlobalUni(str);
    unicode = PyUnicode_FromUnicode((PWSTR)ptr.ToPointer(), str->Length);
    Marshal::FreeHGlobal(ptr);

    return unicode;
}

PyObject* DictionaryToPyDict(IDictionary<String^, Object^> ^object)
{
    PyObject *dict, *key, *value;
    int result;

    dict = PyDict_New();
    if (dict == nullptr)
        return nullptr;

    SCOPE_EXIT
    {
        PyRelease(dict);
    }
    SCOPE_EXIT_END;

    for each (auto item in object)
    {
        key = StringToPyUnicode(item.Key);
        if (key == nullptr)
            return nullptr;

        value = ObjectToPyObject(item.Value);
        if (value == nullptr)
        {
            PyRelease(key);
            return nullptr;
        }

        result = PyDict_SetItem(dict, key, value);
        PyRelease(key);
        PyRelease(value);

        if (result != 0)
        {
            return nullptr;
        }
    }

    PyAddRef(dict);

    return dict;
}

PyObject* ArrayToPyList(System::Collections::IEnumerable ^arr)
{
    NTSTATUS Status;
    PyObject *Array, *Value;

    Array = PyList_New(0);
    if (Array == nullptr)
        return nullptr;

    SCOPE_EXIT
    {
        PyRelease(Array);
    }
    SCOPE_EXIT_END;

    for each (Object ^object in arr)
    {
        Value = ObjectToPyObject(object);
        if (Value == nullptr)
            return nullptr;

        Status = PyList_Append(Array, Value);
        PyRelease(Value);

        if (Status != 0)
            return nullptr;
    }

    PyAddRef(Array);

    return Array;
}

PyObject* ObjectToPyObject(Object ^object)
{
    PyObject*       Value;
    Type^           ValueType;
    System::Double  Number;

    if (object == nullptr)
    {
        Py_RETURN_NONE;
    }

    ValueType = object->GetType();

    if (ValueType == String::typeid)
    {
        Value = StringToPyUnicode((String ^)object);
    }
    else if (ValueType == ArrayCollection::typeid ||
             ValueType == array<Object^, 1>::typeid)
    {
        Value = ArrayToPyList((System::Collections::IEnumerable ^)object);
    }
    else if (ValueType == ASObject::typeid ||
             ValueType == Dictionary<String^, Object^>::typeid)
    {
        Value = DictionaryToPyDict((IDictionary<String^, Object^> ^)object);
    }
    else if (ValueType == Boolean::typeid)
    {
        Value = PyBool_FromLong((Boolean)object);
    }
    else if (System::Double::TryParse(object->ToString(), Number))
    {
        if (ValueType == System::Double::typeid)
        {
            Value = PyFloat_FromDouble(Number);
        }
        else
        {
            Value = PyLong_FromDouble(Number);
        }
    }
    else
    {
        throw gcnew Exception(String::Format(L"unknown object type: {0}", ValueType->ToString()));
    }

    return Value;
}

NTSTATUS FillMessageBodies(PyObject *PyMessage, AMFMessage ^Message)
{
    NTSTATUS Status;
    PyObject *PyBody, *PyBodies, *Value;

    PyBodies = PyList_New(0);
    if (PyBodies == nullptr)
        return STATUS_NO_MEMORY;

    Status = PyDict_SetItemString(PyMessage, "Bodies", PyBodies);
    PyBody = nullptr;

    SCOPE_EXIT
    {
        PyRelease(PyBodies);
        PyRelease(PyBody);
    }
    SCOPE_EXIT_END;

    if (Status != 0)
        return STATUS_UNSUCCESSFUL;

    for each (AMFBody ^Body in Message->Bodies)
    {
        PyBody = PyDict_New();
        if (PyBody == nullptr)
            return STATUS_NO_MEMORY;

        Value = StringToPyUnicode(Body->Target);
        if (Value == nullptr)
            return STATUS_NO_MEMORY;

        Status = PyDict_SetItemString(PyBody, "Target", Value);
        PyRelease(Value);
        if (Status != 0)
            return STATUS_UNSUCCESSFUL;

        Value = StringToPyUnicode(Body->Response);
        if (Value == nullptr)
            return STATUS_NO_MEMORY;

        Status = PyDict_SetItemString(PyBody, "Response", Value);
        PyRelease(Value);
        if (Status != 0)
            return STATUS_UNSUCCESSFUL;

        Value = ObjectToPyObject(Body->Content);
        if (Value == nullptr)
            return STATUS_UNSUCCESSFUL;

        Status = PyDict_SetItemString(PyBody, "Content", Value);
        PyRelease(Value);
        if (Status != 0)
            return STATUS_UNSUCCESSFUL;

        Status = PyList_Append(PyBodies, PyBody);
        if (Status != 0)
            return STATUS_UNSUCCESSFUL;

        PyRelease(PyBody);
    }

    PyBody = nullptr;

    return STATUS_SUCCESS;
}

PyObject* PyAMFDeserializer_ReadMessage_Managed(PyObject *self, PyObject *args, PyObject *kwargs)
{
    NTSTATUS        Status;
    PyObject       *PyAmfResponseData;
    PyObject       *Value, *PyMessage;
    PBYTE           MessageBuffer;
    Py_ssize_t      Length;

    static PSTR kwlist[] = { "ResponseData", nullptr };

    if (PyArg_ParseTupleAndKeywords(args, kwargs, "O", kwlist, &PyAmfResponseData) == FALSE)
        return nullptr;

    PyMessage = nullptr;

    PyAddRef(PyAmfResponseData);

    SCOPE_EXIT
    {
        PyRelease(PyAmfResponseData);
        PyRelease(PyMessage);
    }
    SCOPE_EXIT_END;

    PyMessage = PyDict_New();
    if (PyMessage == nullptr)
        return nullptr;

    if (PyBytes_AsStringAndSize(PyAmfResponseData, (PCHAR *)&MessageBuffer, &Length) != 0)
        return nullptr;

    auto buffer = gcnew array<BYTE, 1>(Length);

    Marshal::Copy((IntPtr)MessageBuffer, buffer, 0, Length);

    auto stream = gcnew MemoryStream(buffer, 0, Length);
    auto deser = gcnew AMFDeserializer(stream);
    auto msg = deser->ReadAMFMessage();

    PrintLog(L"package len = 0x%X\n", stream->Length);
    PrintLog(L"header count = %d\n", msg->HeaderCount);
    PrintLog(L"body count = %d\n", msg->BodyCount);

    Value = PyLong_FromLong(msg->Version);
    if (Value == nullptr)
        return nullptr;

    Status = PyDict_SetItemString(PyMessage, "Version", Value);
    PyRelease(Value);

    PrintLog(L"set ver st = %p\n", Status);

    if (Status != 0)
        return nullptr;

    Status = FillMessageBodies(PyMessage, msg);

    PrintLog(L"FillMessageBodies st = %p\n", Status);

    if (NT_FAILED(Status))
        return nullptr;

    PyAddRef(PyMessage);

    return PyMessage;
}
