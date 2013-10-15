#ifndef _PYAMFHELPEROBJECT_H_9dcea58b_4fa5_492d_a979_1b835bc7a06d_
#define _PYAMFHELPEROBJECT_H_9dcea58b_4fa5_492d_a979_1b835bc7a06d_

#include "Stdafx.h"
#include <Python.h>
#include <structmember.h>

#define PY_ADD_MEMBER(_name, _type, _offset, _flags, ...) { _name, _type, _offset, _flags, __VA_ARGS__ }
#define PY_ADD_METHOD(_name, _func, _flags, ...) { _name, (PyCFunction)_func, _flags, __VA_ARGS__ }
#define PY_ADD_METHOD_END {}

#define PY_GET_GETTER(_type, _field) _type##_Get_##_field
#define PY_GET_SETTER(_type, _field) _type##_Set_##_field

#define PY_GET_GETTER_METHOD(_type, _field) (getter)PY_GET_GETTER(_type, _field)
#define PY_GET_SETTER_METHOD(_type, _field) (setter)PY_GET_SETTER(_type, _field)

#define PY_ADD_GET_SET(_type, _field, ...) \
            { \
                #_field, \
                IF_EXIST(PY_GET_GETTER(_type, _field)) \
                { \
                    PY_GET_GETTER_METHOD(_type, _field) \
                } \
                IF_NOT_EXIST(PY_GET_GETTER(_type, _field)) \
                { \
                    nullptr \
                }, \
                IF_EXIST(PY_GET_SETTER(_type, _field)) \
                { \
                    PY_GET_SETTER_METHOD(_type, _field) \
                } \
                IF_NOT_EXIST(PY_GET_SETTER(_type, _field)) \
                { \
                    nullptr \
                }, \
                __VA_ARGS__,\
            }

#define PY_DEFINE_GET(_type, _field) PyObject* _type##_Get_##_field(_type* self, PVOID)
#define PY_DEFINE_SET(_type, _field) int _type##_Set_##_field(_type* self, PyObject* value, PVOID)

#define PY_DEFINE_GET_BOOLEAN(_type, _field) \
            PY_DEFINE_GET(_type, _field) \
            { \
                if (self->_field == FALSE) \
                { \
                    Py_RETURN_FALSE; \
                } \
                else \
                { \
                    Py_RETURN_TRUE; \
                } \
            }

#define PY_DEFINE_SET_BOOLEAN(_type, _field) \
            PY_DEFINE_SET(_type, _field) \
            { \
                int result = PyObject_IsTrue(value); \
                if (result == -1) \
                    return -1; \
                self->_field = result == 1; \
                return 0; \
            }


#define PY_DEFINE_GET_OBJECT(_type, _field) \
            PY_DEFINE_GET(_type, _field) \
            { \
                return (PyObject *)self->_field; \
            }

#define PY_DEFINE_SET_OBJECT(_type, _field, _objtype) \
            PY_DEFINE_SET(_type, _field) \
            { \
                if (PyType_IsSubtype(Py_TYPE(value), &_objtype) == FALSE) \
                    return -1; \
                PyAddRef(value); \
                self->_field = (TYPE_OF(self->_field))value; \
                return 0; \
            }

typedef struct
{
    PyObject_HEAD;

    operator PyObject*()
    {
        return &this->ob_base;
    }

} PyObjectBase;


typedef struct
{
    PyObject_VAR_HEAD;

    operator PyObject*()
    {
        return &this->ob_base.ob_base;
    }

} PyVarObjectBase;


VOID PyAddRef(PyObject *Object);
VOID PyRelease(PyObject *Object);


/************************************************************************
  PyAmfHelper_AMFBody
************************************************************************/

typedef struct PyAmfHelper_AMFBody : public PyObjectBase
{
    BOOLEAN         IsEmptyTarget;
    BOOLEAN         IsAuthenticationAction;
    BOOLEAN         IgnoreResults;

    PyUnicodeObject*    Target;
    PyUnicodeObject*    Response;
    PyDictObject*       Content;

} PyAmfHelper_AMFBody, *PPyAmfHelper_AMFBody;


#if CPP_CLI_DEFINED

typedef System::Collections::Generic::Dictionary<System::String^, System::Object^> AMF_CONTENT_VALUE;
typedef FluorineFx::AMF3::ArrayCollection AMF_CONTENT;

#endif

/************************************************************************
  PyAmfHelper_AMFSerializer
************************************************************************/

typedef struct PyAmfHelper_AMFSerializer : public PyObjectBase
{
    
} PyAmfHelper_AMFSerializer, *PPyAmfHelper_AMFSerializer;

PyObject* PyAMFSerializer_WriteMessage_Managed(PyObject *self, PyObject *args, PyObject *kwargs);


extern PyTypeObject PyAMFSerializer_Type;


/************************************************************************
PyAmfHelper_AMFDeserializer
************************************************************************/

typedef struct PyAmfHelper_AMFDeserializer : public PyObjectBase
{

} PyAmfHelper_AMFDeserializer, *PPyAmfHelper_AMFDeserializer;

PyObject* PyAMFDeserializer_ReadMessage_Managed(PyObject *self, PyObject *args, PyObject *kwargs);

extern PyTypeObject PyAMFDeserializer_Type;

#endif // _PYAMFHELPEROBJECT_H_9dcea58b_4fa5_492d_a979_1b835bc7a06d_
