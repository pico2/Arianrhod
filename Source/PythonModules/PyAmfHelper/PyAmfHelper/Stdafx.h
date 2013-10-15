// stdafx.h : include file for standard system include files,
// or project specific include files that are used frequently,
// but are changed infrequently

#pragma once

#define ML_DISABLE_THIRD_LIB_UCL 1
#pragma warning(disable:4714)

#include "MyLibrary.h"
#include "PyAmfHelperObject.h"


#define MANAGED_DISABLE managed(push, off)
#define MANAGED_ENABLE  managed(push, on)
#define MANAGED_RESTORE managed(pop)

#define PY_AMF_HELPER_MODULE    "PyAmfHelper"