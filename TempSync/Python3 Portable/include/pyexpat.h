/* Stuff to export relevant 'expat' entry points from pyexpat to other
 * parser modules, such as cElementTree. */

/* note: you must import expat.h before importing this module! */

#define PyExpat_CAPI_MAGIC  "pyexpat.expat_CAPI 1.0"
#define PyExpat_CAPSULE_NAME "pyexpat.expat_CAPI"

struct PyExpat_CAPI
{
    char* magic; /* set to PyExpat_CAPI_MAGIC */
    int size; /* set to sizeof(struct PyExpat_CAPI) */
    int MAJOR_VERSION;
    int MINOR_VERSION;
    int MICRO_VERSION;
    /* pointers to selected expat functions.  add new functions at
       the end, if needed */
    const XML_LChar * (__cdecl *ErrorString)(enum XML_Error code);
    enum XML_Error (__cdecl *GetErrorCode)(XML_Parser parser);
    XML_Size (__cdecl *GetErrorColumnNumber)(XML_Parser parser);
    XML_Size (__cdecl *GetErrorLineNumber)(XML_Parser parser);
    enum XML_Status (__cdecl *Parse)(
        XML_Parser parser, const char *s, int len, int isFinal);
    XML_Parser (__cdecl *ParserCreate_MM)(
        const XML_Char *encoding, const XML_Memory_Handling_Suite *memsuite,
        const XML_Char *namespaceSeparator);
    void (__cdecl *ParserFree)(XML_Parser parser);
    void (__cdecl *SetCharacterDataHandler)(
        XML_Parser parser, XML_CharacterDataHandler handler);
    void (__cdecl *SetCommentHandler)(
        XML_Parser parser, XML_CommentHandler handler);
    void (__cdecl *SetDefaultHandlerExpand)(
        XML_Parser parser, XML_DefaultHandler handler);
    void (__cdecl *SetElementHandler)(
        XML_Parser parser, XML_StartElementHandler start,
        XML_EndElementHandler end);
    void (__cdecl *SetNamespaceDeclHandler)(
        XML_Parser parser, XML_StartNamespaceDeclHandler start,
        XML_EndNamespaceDeclHandler end);
    void (__cdecl *SetProcessingInstructionHandler)(
        XML_Parser parser, XML_ProcessingInstructionHandler handler);
    void (__cdecl *SetUnknownEncodingHandler)(
        XML_Parser parser, XML_UnknownEncodingHandler handler,
        void *encodingHandlerData);
    void (__cdecl *SetUserData)(XML_Parser parser, void *userData);
    void (__cdecl *SetStartDoctypeDeclHandler)(XML_Parser parser,
                                       XML_StartDoctypeDeclHandler start);
    enum XML_Status (__cdecl *SetEncoding)(XML_Parser parser, const XML_Char *encoding);
    int (__cdecl *DefaultUnknownEncodingHandler)(
        void *encodingHandlerData, const XML_Char *name, XML_Encoding *info);
    /* always add new stuff to the end! */
};

