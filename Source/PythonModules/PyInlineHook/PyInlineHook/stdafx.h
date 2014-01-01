#ifndef _STDAFX_H_1aa3d296_04d7_47db_af45_b82eb1c4ef1c_
#define _STDAFX_H_1aa3d296_04d7_47db_af45_b82eb1c4ef1c_

#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text /MERGE:.text1=.text /SECTION:.idata,ERW")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")

#define ML_DISABLE_THIRD_LIB_UCL 1

#include "MyLibrary.h"
#include "PyInlineHookObject.h"

#endif // _STDAFX_H_1aa3d296_04d7_47db_af45_b82eb1c4ef1c_
