diff --git "a/D:\\Desktop\\Python3\\include/cdecl_patch.h" "b/D:\\Desktop\\Python3\\include/cdecl_patch.h"
new file mode 100644
index 0000000..e69de29
diff --git "a/D:\\Dev\\Python\\include/ceval.h" "b/D:\\Desktop\\Python3\\include/ceval.h"
index 6811367..f084212 100644
--- "a/D:\\Dev\\Python\\include/ceval.h"
+++ "b/D:\\Desktop\\Python3\\include/ceval.h"
@@ -39,7 +39,7 @@ PyAPI_FUNC(struct _frame *) PyEval_GetFrame(void);
 PyAPI_FUNC(int) PyEval_MergeCompilerFlags(PyCompilerFlags *cf);
 #endif
 
-PyAPI_FUNC(int) Py_AddPendingCall(int (*func)(void *), void *arg);
+PyAPI_FUNC(int) Py_AddPendingCall(int (__cdecl *func)(void *), void *arg);
 PyAPI_FUNC(int) Py_MakePendingCalls(void);
 
 /* Protection against deeply nested recursive calls
diff --git "a/D:\\Dev\\Python\\include/descrobject.h" "b/D:\\Desktop\\Python3\\include/descrobject.h"
index e2ba97f..28bf7ca 100644
--- "a/D:\\Dev\\Python\\include/descrobject.h"
+++ "b/D:\\Desktop\\Python3\\include/descrobject.h"
@@ -5,8 +5,8 @@
 extern "C" {
 #endif
 
-typedef PyObject *(*getter)(PyObject *, void *);
-typedef int (*setter)(PyObject *, PyObject *, void *);
+typedef PyObject *(__cdecl *getter)(PyObject *, void *);
+typedef int (__cdecl *setter)(PyObject *, PyObject *, void *);
 
 typedef struct PyGetSetDef {
     char *name;
@@ -17,10 +17,10 @@ typedef struct PyGetSetDef {
 } PyGetSetDef;
 
 #ifndef Py_LIMITED_API
-typedef PyObject *(*wrapperfunc)(PyObject *self, PyObject *args,
+typedef PyObject *(__cdecl *wrapperfunc)(PyObject *self, PyObject *args,
                                  void *wrapped);
 
-typedef PyObject *(*wrapperfunc_kwds)(PyObject *self, PyObject *args,
+typedef PyObject *(__cdecl *wrapperfunc_kwds)(PyObject *self, PyObject *args,
                                       void *wrapped, PyObject *kwds);
 
 struct wrapperbase {
diff --git "a/D:\\Dev\\Python\\include/import.h" "b/D:\\Desktop\\Python3\\include/import.h"
index afdfac2..035cba3 100644
--- "a/D:\\Dev\\Python\\include/import.h"
+++ "b/D:\\Desktop\\Python3\\include/import.h"
@@ -98,7 +98,7 @@ PyAPI_FUNC(int) _PyImport_FixupExtensionObject(PyObject*, PyObject *, PyObject *
 
 struct _inittab {
     const char *name;           /* ASCII encoded string */
-    PyObject* (*initfunc)(void);
+    PyObject* (__cdecl *initfunc)(void);
 };
 PyAPI_DATA(struct _inittab *) PyImport_Inittab;
 PyAPI_FUNC(int) PyImport_ExtendInittab(struct _inittab *newtab);
@@ -108,7 +108,7 @@ PyAPI_DATA(PyTypeObject) PyNullImporter_Type;
 
 PyAPI_FUNC(int) PyImport_AppendInittab(
     const char *name,           /* ASCII encoded string */
-    PyObject* (*initfunc)(void)
+    PyObject* (__cdecl *initfunc)(void)
     );
 
 #ifndef Py_LIMITED_API
diff --git "a/D:\\Dev\\Python\\include/methodobject.h" "b/D:\\Desktop\\Python3\\include/methodobject.h"
index 3cc2ea9..a6ca749 100644
--- "a/D:\\Dev\\Python\\include/methodobject.h"
+++ "b/D:\\Desktop\\Python3\\include/methodobject.h"
@@ -15,10 +15,10 @@ PyAPI_DATA(PyTypeObject) PyCFunction_Type;
 
 #define PyCFunction_Check(op) (Py_TYPE(op) == &PyCFunction_Type)
 
-typedef PyObject *(*PyCFunction)(PyObject *, PyObject *);
-typedef PyObject *(*PyCFunctionWithKeywords)(PyObject *, PyObject *,
+typedef PyObject *(__cdecl *PyCFunction)(PyObject *, PyObject *);
+typedef PyObject *(__cdecl *PyCFunctionWithKeywords)(PyObject *, PyObject *,
                                              PyObject *);
-typedef PyObject *(*PyNoArgsFunction)(PyObject *);
+typedef PyObject *(__cdecl *PyNoArgsFunction)(PyObject *);
 
 PyAPI_FUNC(PyCFunction) PyCFunction_GetFunction(PyObject *);
 PyAPI_FUNC(PyObject *) PyCFunction_GetSelf(PyObject *);
diff --git "a/D:\\Dev\\Python\\include/moduleobject.h" "b/D:\\Desktop\\Python3\\include/moduleobject.h"
index f119364..3b0b491 100644
--- "a/D:\\Dev\\Python\\include/moduleobject.h"
+++ "b/D:\\Desktop\\Python3\\include/moduleobject.h"
@@ -32,7 +32,7 @@ PyAPI_FUNC(void*) PyModule_GetState(PyObject*);
 
 typedef struct PyModuleDef_Base {
   PyObject_HEAD
-  PyObject* (*m_init)(void);
+  PyObject* (__cdecl *m_init)(void);
   Py_ssize_t m_index;
   PyObject* m_copy;
 } PyModuleDef_Base;
diff --git "a/D:\\Dev\\Python\\include/object.h" "b/D:\\Desktop\\Python3\\include/object.h"
index 7584d4c..e58853b 100644
--- "a/D:\\Dev\\Python\\include/object.h"
+++ "b/D:\\Desktop\\Python3\\include/object.h"
@@ -162,11 +162,11 @@ NB: the methods for certain type groups are now contained in separate
 method blocks.
 */
 
-typedef PyObject * (*unaryfunc)(PyObject *);
-typedef PyObject * (*binaryfunc)(PyObject *, PyObject *);
-typedef PyObject * (*ternaryfunc)(PyObject *, PyObject *, PyObject *);
-typedef int (*inquiry)(PyObject *);
-typedef Py_ssize_t (*lenfunc)(PyObject *);
+typedef PyObject * (__cdecl *unaryfunc)(PyObject *);
+typedef PyObject * (__cdecl *binaryfunc)(PyObject *, PyObject *);
+typedef PyObject * (__cdecl *ternaryfunc)(PyObject *, PyObject *, PyObject *);
+typedef int (__cdecl *inquiry)(PyObject *);
+typedef Py_ssize_t (__cdecl *lenfunc)(PyObject *);
 typedef PyObject *(*ssizeargfunc)(PyObject *, Py_ssize_t);
 typedef PyObject *(*ssizessizeargfunc)(PyObject *, Py_ssize_t, Py_ssize_t);
 typedef int(*ssizeobjargproc)(PyObject *, Py_ssize_t, PyObject *);
@@ -190,8 +190,8 @@ typedef struct bufferinfo {
     void *internal;
 } Py_buffer;
 
-typedef int (*getbufferproc)(PyObject *, Py_buffer *, int);
-typedef void (*releasebufferproc)(PyObject *, Py_buffer *);
+typedef int (__cdecl *getbufferproc)(PyObject *, Py_buffer *, int);
+typedef void (__cdecl *releasebufferproc)(PyObject *, Py_buffer *);
 
 /* Maximum number of dimensions */
 #define PyBUF_MAX_NDIM 64
@@ -228,9 +228,9 @@ typedef void (*releasebufferproc)(PyObject *, Py_buffer *);
 /* End buffer interface */
 #endif /* Py_LIMITED_API */
 
-typedef int (*objobjproc)(PyObject *, PyObject *);
-typedef int (*visitproc)(PyObject *, void *);
-typedef int (*traverseproc)(PyObject *, visitproc, void *);
+typedef int (__cdecl *objobjproc)(PyObject *, PyObject *);
+typedef int (__cdecl *visitproc)(PyObject *, void *);
+typedef int (__cdecl *traverseproc)(PyObject *, visitproc, void *);
 
 #ifndef Py_LIMITED_API
 typedef struct {
@@ -304,29 +304,29 @@ typedef struct {
 } PyBufferProcs;
 #endif /* Py_LIMITED_API */
 
-typedef void (*freefunc)(void *);
-typedef void (*destructor)(PyObject *);
+typedef void (__cdecl *freefunc)(void *);
+typedef void (__cdecl *destructor)(PyObject *);
 #ifndef Py_LIMITED_API
 /* We can't provide a full compile-time check that limited-API
    users won't implement tp_print. However, not defining printfunc
    and making tp_print of a different function pointer type
    should at least cause a warning in most cases. */
-typedef int (*printfunc)(PyObject *, FILE *, int);
+typedef int (__cdecl *printfunc)(PyObject *, FILE *, int);
 #endif
-typedef PyObject *(*getattrfunc)(PyObject *, char *);
-typedef PyObject *(*getattrofunc)(PyObject *, PyObject *);
-typedef int (*setattrfunc)(PyObject *, char *, PyObject *);
-typedef int (*setattrofunc)(PyObject *, PyObject *, PyObject *);
-typedef PyObject *(*reprfunc)(PyObject *);
-typedef Py_hash_t (*hashfunc)(PyObject *);
-typedef PyObject *(*richcmpfunc) (PyObject *, PyObject *, int);
-typedef PyObject *(*getiterfunc) (PyObject *);
-typedef PyObject *(*iternextfunc) (PyObject *);
-typedef PyObject *(*descrgetfunc) (PyObject *, PyObject *, PyObject *);
-typedef int (*descrsetfunc) (PyObject *, PyObject *, PyObject *);
-typedef int (*initproc)(PyObject *, PyObject *, PyObject *);
-typedef PyObject *(*newfunc)(struct _typeobject *, PyObject *, PyObject *);
-typedef PyObject *(*allocfunc)(struct _typeobject *, Py_ssize_t);
+typedef PyObject *(__cdecl *getattrfunc)(PyObject *, char *);
+typedef PyObject *(__cdecl *getattrofunc)(PyObject *, PyObject *);
+typedef int (__cdecl *setattrfunc)(PyObject *, char *, PyObject *);
+typedef int (__cdecl *setattrofunc)(PyObject *, PyObject *, PyObject *);
+typedef PyObject *(__cdecl *reprfunc)(PyObject *);
+typedef Py_hash_t (__cdecl *hashfunc)(PyObject *);
+typedef PyObject *(__cdecl *richcmpfunc) (PyObject *, PyObject *, int);
+typedef PyObject *(__cdecl *getiterfunc) (PyObject *);
+typedef PyObject *(__cdecl *iternextfunc) (PyObject *);
+typedef PyObject *(__cdecl *descrgetfunc) (PyObject *, PyObject *, PyObject *);
+typedef int (__cdecl *descrsetfunc) (PyObject *, PyObject *, PyObject *);
+typedef int (__cdecl *initproc)(PyObject *, PyObject *, PyObject *);
+typedef PyObject *(__cdecl *newfunc)(struct _typeobject *, PyObject *, PyObject *);
+typedef PyObject *(__cdecl *allocfunc)(struct _typeobject *, Py_ssize_t);
 
 #ifdef Py_LIMITED_API
 typedef struct _typeobject PyTypeObject; /* opaque */
diff --git "a/D:\\Dev\\Python\\include/objimpl.h" "b/D:\\Desktop\\Python3\\include/objimpl.h"
index 3f21b70..7e9281e 100644
--- "a/D:\\Dev\\Python\\include/objimpl.h"
+++ "b/D:\\Desktop\\Python3\\include/objimpl.h"
@@ -204,10 +204,10 @@ typedef struct {
     void *ctx;
 
     /* allocate an arena of size bytes */
-    void* (*alloc) (void *ctx, size_t size);
+    void* (__cdecl *alloc) (void *ctx, size_t size);
 
     /* free an arena */
-    void (*free) (void *ctx, void *ptr, size_t size);
+    void (__cdecl *free) (void *ctx, void *ptr, size_t size);
 } PyObjectArenaAllocator;
 
 /* Get the arena allocator. */
diff --git "a/D:\\Dev\\Python\\include/py_curses.h" "b/D:\\Desktop\\Python3\\include/py_curses.h"
index f2c08f6..ca66585 100644
--- "a/D:\\Dev\\Python\\include/py_curses.h"
+++ "b/D:\\Desktop\\Python3\\include/py_curses.h"
@@ -92,10 +92,10 @@ typedef struct {
 
 static void **PyCurses_API;
 
-#define PyCursesWindow_Type (*(PyTypeObject *) PyCurses_API[0])
-#define PyCursesSetupTermCalled  {if (! ((int (*)(void))PyCurses_API[1]) () ) return NULL;}
-#define PyCursesInitialised      {if (! ((int (*)(void))PyCurses_API[2]) () ) return NULL;}
-#define PyCursesInitialisedColor {if (! ((int (*)(void))PyCurses_API[3]) () ) return NULL;}
+#define PyCursesWindow_Type (__cdecl *(PyTypeObject *) PyCurses_API[0])
+#define PyCursesSetupTermCalled  {if (! ((int (__cdecl *)(void))PyCurses_API[1]) () ) return NULL;}
+#define PyCursesInitialised      {if (! ((int (__cdecl *)(void))PyCurses_API[2]) () ) return NULL;}
+#define PyCursesInitialisedColor {if (! ((int (__cdecl *)(void))PyCurses_API[3]) () ) return NULL;}
 
 #define import_curses() \
     PyCurses_API = (void **)PyCapsule_Import(PyCurses_CAPSULE_NAME, 1);
diff --git "a/D:\\Dev\\Python\\include/pycapsule.h" "b/D:\\Desktop\\Python3\\include/pycapsule.h"
index d9ecda7..71d4ea2 100644
--- "a/D:\\Dev\\Python\\include/pycapsule.h"
+++ "b/D:\\Desktop\\Python3\\include/pycapsule.h"
@@ -20,7 +20,7 @@ extern "C" {
 
 PyAPI_DATA(PyTypeObject) PyCapsule_Type;
 
-typedef void (*PyCapsule_Destructor)(PyObject *);
+typedef void (__cdecl *PyCapsule_Destructor)(PyObject *);
 
 #define PyCapsule_CheckExact(op) (Py_TYPE(op) == &PyCapsule_Type)
 
diff --git "a/D:\\Dev\\Python\\include/pyexpat.h" "b/D:\\Desktop\\Python3\\include/pyexpat.h"
index 44259bf..be93e6a 100644
--- "a/D:\\Dev\\Python\\include/pyexpat.h"
+++ "b/D:\\Desktop\\Python3\\include/pyexpat.h"
@@ -15,38 +15,38 @@ struct PyExpat_CAPI
     int MICRO_VERSION;
     /* pointers to selected expat functions.  add new functions at
        the end, if needed */
-    const XML_LChar * (*ErrorString)(enum XML_Error code);
-    enum XML_Error (*GetErrorCode)(XML_Parser parser);
-    XML_Size (*GetErrorColumnNumber)(XML_Parser parser);
-    XML_Size (*GetErrorLineNumber)(XML_Parser parser);
-    enum XML_Status (*Parse)(
+    const XML_LChar * (__cdecl *ErrorString)(enum XML_Error code);
+    enum XML_Error (__cdecl *GetErrorCode)(XML_Parser parser);
+    XML_Size (__cdecl *GetErrorColumnNumber)(XML_Parser parser);
+    XML_Size (__cdecl *GetErrorLineNumber)(XML_Parser parser);
+    enum XML_Status (__cdecl *Parse)(
         XML_Parser parser, const char *s, int len, int isFinal);
-    XML_Parser (*ParserCreate_MM)(
+    XML_Parser (__cdecl *ParserCreate_MM)(
         const XML_Char *encoding, const XML_Memory_Handling_Suite *memsuite,
         const XML_Char *namespaceSeparator);
-    void (*ParserFree)(XML_Parser parser);
-    void (*SetCharacterDataHandler)(
+    void (__cdecl *ParserFree)(XML_Parser parser);
+    void (__cdecl *SetCharacterDataHandler)(
         XML_Parser parser, XML_CharacterDataHandler handler);
-    void (*SetCommentHandler)(
+    void (__cdecl *SetCommentHandler)(
         XML_Parser parser, XML_CommentHandler handler);
-    void (*SetDefaultHandlerExpand)(
+    void (__cdecl *SetDefaultHandlerExpand)(
         XML_Parser parser, XML_DefaultHandler handler);
-    void (*SetElementHandler)(
+    void (__cdecl *SetElementHandler)(
         XML_Parser parser, XML_StartElementHandler start,
         XML_EndElementHandler end);
-    void (*SetNamespaceDeclHandler)(
+    void (__cdecl *SetNamespaceDeclHandler)(
         XML_Parser parser, XML_StartNamespaceDeclHandler start,
         XML_EndNamespaceDeclHandler end);
-    void (*SetProcessingInstructionHandler)(
+    void (__cdecl *SetProcessingInstructionHandler)(
         XML_Parser parser, XML_ProcessingInstructionHandler handler);
-    void (*SetUnknownEncodingHandler)(
+    void (__cdecl *SetUnknownEncodingHandler)(
         XML_Parser parser, XML_UnknownEncodingHandler handler,
         void *encodingHandlerData);
-    void (*SetUserData)(XML_Parser parser, void *userData);
-    void (*SetStartDoctypeDeclHandler)(XML_Parser parser,
+    void (__cdecl *SetUserData)(XML_Parser parser, void *userData);
+    void (__cdecl *SetStartDoctypeDeclHandler)(XML_Parser parser,
                                        XML_StartDoctypeDeclHandler start);
-    enum XML_Status (*SetEncoding)(XML_Parser parser, const XML_Char *encoding);
-    int (*DefaultUnknownEncodingHandler)(
+    enum XML_Status (__cdecl *SetEncoding)(XML_Parser parser, const XML_Char *encoding);
+    int (__cdecl *DefaultUnknownEncodingHandler)(
         void *encodingHandlerData, const XML_Char *name, XML_Encoding *info);
     /* always add new stuff to the end! */
 };
diff --git "a/D:\\Dev\\Python\\include/pyhash.h" "b/D:\\Desktop\\Python3\\include/pyhash.h"
index a7ca937..1b033e0 100644
--- "a/D:\\Dev\\Python\\include/pyhash.h"
+++ "b/D:\\Desktop\\Python3\\include/pyhash.h"
@@ -87,7 +87,7 @@ PyAPI_DATA(int) _Py_HashSecret_Initialized;
 /* hash function definition */
 #ifndef Py_LIMITED_API
 typedef struct {
-    Py_hash_t (*const hash)(const void *, Py_ssize_t);
+    Py_hash_t (__cdecl *const hash)(const void *, Py_ssize_t);
     const char *name;
     const int hash_bits;
     const int seed_bits;
diff --git "a/D:\\Dev\\Python\\include/pymem.h" "b/D:\\Desktop\\Python3\\include/pymem.h"
index 2372b86..da084e5 100644
--- "a/D:\\Dev\\Python\\include/pymem.h"
+++ "b/D:\\Desktop\\Python3\\include/pymem.h"
@@ -130,13 +130,13 @@ typedef struct {
     void *ctx;
 
     /* allocate a memory block */
-    void* (*malloc) (void *ctx, size_t size);
+    void* (__cdecl *malloc) (void *ctx, size_t size);
 
     /* allocate or resize a memory block */
-    void* (*realloc) (void *ctx, void *ptr, size_t new_size);
+    void* (__cdecl *realloc) (void *ctx, void *ptr, size_t new_size);
 
     /* release a memory block */
-    void (*free) (void *ctx, void *ptr);
+    void (__cdecl *free) (void *ctx, void *ptr);
 } PyMemAllocator;
 
 /* Get the memory block allocator of the specified domain. */
diff --git "a/D:\\Dev\\Python\\include/pyport.h" "b/D:\\Desktop\\Python3\\include/pyport.h"
index c706213..510489a 100644
--- "a/D:\\Dev\\Python\\include/pyport.h"
+++ "b/D:\\Desktop\\Python3\\include/pyport.h"
@@ -737,7 +737,7 @@ extern pid_t forkpty(int *, char *, struct termios *, struct winsize *);
 #if defined(Py_ENABLE_SHARED) || defined(__CYGWIN__)
 #       if defined(HAVE_DECLSPEC_DLL)
 #               ifdef Py_BUILD_CORE
-#                       define PyAPI_FUNC(RTYPE) __declspec(dllexport) RTYPE
+#                       define PyAPI_FUNC(RTYPE) __declspec(dllexport) RTYPE __cdecl
 #                       define PyAPI_DATA(RTYPE) extern __declspec(dllexport) RTYPE
         /* module init functions inside the core need no external linkage */
         /* except for Cygwin to handle embedding */
@@ -753,7 +753,7 @@ extern pid_t forkpty(int *, char *, struct termios *, struct winsize *);
         /* failures similar to those described at the bottom of 4.1: */
         /* http://docs.python.org/extending/windows.html#a-cookbook-approach */
 #                       if !defined(__CYGWIN__)
-#                               define PyAPI_FUNC(RTYPE) __declspec(dllimport) RTYPE
+#                               define PyAPI_FUNC(RTYPE) __declspec(dllimport) RTYPE __cdecl
 #                       endif /* !__CYGWIN__ */
 #                       define PyAPI_DATA(RTYPE) extern __declspec(dllimport) RTYPE
         /* module init functions outside the core must be exported */
@@ -768,7 +768,7 @@ extern pid_t forkpty(int *, char *, struct termios *, struct winsize *);
 
 /* If no external linkage macros defined by now, create defaults */
 #ifndef PyAPI_FUNC
-#       define PyAPI_FUNC(RTYPE) RTYPE
+#       define PyAPI_FUNC(RTYPE) RTYPE __cdecl
 #endif
 #ifndef PyAPI_DATA
 #       define PyAPI_DATA(RTYPE) extern RTYPE
diff --git "a/D:\\Dev\\Python\\include/pystate.h" "b/D:\\Desktop\\Python3\\include/pystate.h"
index 4992c22..96b1e1d 100644
--- "a/D:\\Dev\\Python\\include/pystate.h"
+++ "b/D:\\Desktop\\Python3\\include/pystate.h"
@@ -51,7 +51,7 @@ struct _frame; /* Avoid including frameobject.h */
 
 #ifndef Py_LIMITED_API
 /* Py_tracefunc return -1 when raising an exception, or 0 for success. */
-typedef int (*Py_tracefunc)(PyObject *, struct _frame *, int, PyObject *);
+typedef int (__cdecl *Py_tracefunc)(PyObject *, struct _frame *, int, PyObject *);
 
 /* The following values are used for 'what' for tracefunc functions: */
 #define PyTrace_CALL 0
@@ -131,7 +131,7 @@ typedef struct _ts {
      * weakref-to-lock (on_delete_data) argument, and release_sentinel releases
      * the indirectly held lock.
      */
-    void (*on_delete)(void *);
+    void (__cdecl *on_delete)(void *);
     void *on_delete_data;
 
     /* XXX signal handlers should also be here */
diff --git "a/D:\\Dev\\Python\\include/pythonrun.h" "b/D:\\Desktop\\Python3\\include/pythonrun.h"
index 2fc5578..15328d1 100644
--- "a/D:\\Dev\\Python\\include/pythonrun.h"
+++ "b/D:\\Desktop\\Python3\\include/pythonrun.h"
@@ -170,9 +170,9 @@ PyAPI_FUNC(void) PyErr_Display(PyObject *, PyObject *, PyObject *);
  * exit functions.
  */
 #ifndef Py_LIMITED_API
-PyAPI_FUNC(void) _Py_PyAtExit(void (*func)(void));
+PyAPI_FUNC(void) _Py_PyAtExit(void (__cdecl *func)(void));
 #endif
-PyAPI_FUNC(int) Py_AtExit(void (*func)(void));
+PyAPI_FUNC(int) Py_AtExit(void (__cdecl *func)(void));
 
 PyAPI_FUNC(void) Py_Exit(int);
 
@@ -269,7 +269,7 @@ PyAPI_DATA(PyThreadState *) _Py_Finalizing;
 #ifndef Py_LIMITED_API
 PyAPI_FUNC(char *) PyOS_Readline(FILE *, FILE *, const char *);
 #endif
-PyAPI_DATA(int) (*PyOS_InputHook)(void);
+PyAPI_DATA(int) (__cdecl *PyOS_InputHook)(void);
 PyAPI_DATA(char) *(*PyOS_ReadlineFunctionPointer)(FILE *, FILE *, const char *);
 #ifndef Py_LIMITED_API
 PyAPI_DATA(PyThreadState*) _PyOS_ReadlineTState;
@@ -291,7 +291,7 @@ PyAPI_FUNC(int) PyOS_CheckStack(void);
 #endif
 
 /* Signals */
-typedef void (*PyOS_sighandler_t)(int);
+typedef void (__cdecl *PyOS_sighandler_t)(int);
 PyAPI_FUNC(PyOS_sighandler_t) PyOS_getsig(int);
 PyAPI_FUNC(PyOS_sighandler_t) PyOS_setsig(int, PyOS_sighandler_t);
 
diff --git "a/D:\\Dev\\Python\\include/pythread.h" "b/D:\\Desktop\\Python3\\include/pythread.h"
index 6e9f303..79c4004 100644
--- "a/D:\\Dev\\Python\\include/pythread.h"
+++ "b/D:\\Desktop\\Python3\\include/pythread.h"
@@ -18,7 +18,7 @@ typedef enum PyLockStatus {
 } PyLockStatus;
 
 PyAPI_FUNC(void) PyThread_init_thread(void);
-PyAPI_FUNC(long) PyThread_start_new_thread(void (*)(void *), void *);
+PyAPI_FUNC(long) PyThread_start_new_thread(void (__cdecl *)(void *), void *);
 PyAPI_FUNC(void) PyThread_exit_thread(void);
 PyAPI_FUNC(long) PyThread_get_thread_ident(void);
 
diff --git "a/D:\\Dev\\Python\\include/ucnhash.h" "b/D:\\Desktop\\Python3\\include/ucnhash.h"
index 8de9ba0..3ed2c88 100644
--- "a/D:\\Dev\\Python\\include/ucnhash.h"
+++ "b/D:\\Desktop\\Python3\\include/ucnhash.h"
@@ -16,15 +16,15 @@ typedef struct {
     int size;
 
     /* Get name for a given character code.  Returns non-zero if
-       success, zero if not.  Does not set Python exceptions. 
+       success, zero if not.  Does not set Python exceptions.
        If self is NULL, data come from the default version of the database.
        If it is not NULL, it should be a unicodedata.ucd_X_Y_Z object */
-    int (*getname)(PyObject *self, Py_UCS4 code, char* buffer, int buflen,
+    int (__cdecl *getname)(PyObject *self, Py_UCS4 code, char* buffer, int buflen,
                    int with_alias_and_seq);
 
     /* Get character code for a given name.  Same error handling
        as for getname. */
-    int (*getcode)(PyObject *self, const char* name, int namelen, Py_UCS4* code,
+    int (__cdecl *getcode)(PyObject *self, const char* name, int namelen, Py_UCS4* code,
                    int with_named_seq);
 
 } _PyUnicode_Name_CAPI;
