#ifndef _QQMETHOD_H_1408431a_e0b5_4df9_a8b5_4f98002b8e00_
#define _QQMETHOD_H_1408431a_e0b5_4df9_a8b5_4f98002b8e00_


/***



***/

#define DECL_STATIC_CTOR(cls, ...) static cls& (FASTCALL *ctor)(cls&)
#define DECL_STATIC_DTOR(cls, ...) static cls& (FASTCALL *dtor)(cls&)
#define DECL_STATIC_METHOD_POINTER(cls, method) static TYPE_OF(&cls::method) Stub##method
#define INIT_STATIC_MEMBER(x) DECL_SELECTANY TYPE_OF(x) x = NULL
#define DETOUR_METHOD(cls, method, addr, ...) TYPE_OF(&cls::method) (method); *(PULONG_PTR)&(method) = addr; return (this->*method)(__VA_ARGS__)


struct CTXStringW
{
    PCWSTR Buffer;

    CTXStringW()
    {
        //this->ctor(*this);
    }

    ~CTXStringW()
    {
        //this->dtor(*this);
    }

    VOID Empty()
    {
        return (this->*StubEmpty)();
    }

    BOOL IsEmpty()
    {
        return (this->*StubIsEmpty)();
    }

    //DECL_STATIC_CTOR(CTXStringW);
    //DECL_STATIC_DTOR(CTXStringW);
    DECL_STATIC_METHOD_POINTER(CTXStringW, Empty);
    DECL_STATIC_METHOD_POINTER(CTXStringW, IsEmpty);
};

//INIT_STATIC_MEMBER(CTXStringW::ctor);
//INIT_STATIC_MEMBER(CTXStringW::dtor);
INIT_STATIC_MEMBER(CTXStringW::StubEmpty);
INIT_STATIC_MEMBER(CTXStringW::StubIsEmpty);

interface ITXBuffer;
interface ITXArrayRead;
interface ITXData;
interface ITXArray;

interface ITXDataRead : IDispatch
{
    virtual HRESULT NTAPI GetBool(BSTR bsParamName, PLONG pbValue);
    virtual HRESULT NTAPI GetByte(BSTR bsParamName, PBYTE pcValue);
    virtual HRESULT NTAPI GetChar(BSTR bsParamName, PCHAR pchValue);
    virtual HRESULT NTAPI GetWord(BSTR bsParamName, PUSHORT pwValue);
    virtual HRESULT NTAPI GetShort(BSTR bsParamName, PSHORT pshValue);
    virtual HRESULT NTAPI GetDWord(BSTR bsParamName, PULONG pdwValue);
    virtual HRESULT NTAPI GetInt(BSTR bsParamName, PINT pnValue);
    virtual HRESULT NTAPI GetInt64(BSTR bsParamName, PINT64 pn64Var);
    virtual HRESULT NTAPI GetDouble(BSTR bsParamName, DOUBLE* pdValue);
    virtual HRESULT NTAPI GetStr(BSTR bsParamName, BSTR* pbsValue);
    virtual HRESULT NTAPI GetBuf(BSTR bsParamName, ITXBuffer** ppBufValue);
    virtual HRESULT NTAPI GetBufTyped(BSTR bsParamName, ITXBuffer** ppBufValue, PULONG pdwSubType);
    virtual HRESULT NTAPI GetDataRead(BSTR bsParamName, ITXDataRead** ppValue);
    virtual HRESULT NTAPI GetArrayRead(BSTR bsParamName, ITXArrayRead** ppValue);
    virtual HRESULT NTAPI GetGuid(BSTR bsParamName, GUID* pGuid);
    virtual HRESULT NTAPI GetInterface(BSTR bsParamName, GUID* riid, PVOID* ppvValue);
    virtual HRESULT NTAPI GetDoc(ITXBuffer** ppBufDoc);
    virtual HRESULT NTAPI CopyTo(ITXData* pData);
    virtual HRESULT NTAPI IsFieldType(BSTR bsParamName, UCHAR cType);
    virtual HRESULT NTAPI GetFieldCount(PUINT puCount);
    virtual HRESULT NTAPI GetFieldName(UINT uIndex, BSTR* pbsFieldName);
    virtual HRESULT NTAPI FieldType(BSTR bsParamName, PBYTE pcType);
    virtual HRESULT NTAPI Equal(ITXDataRead* pData);
    virtual HRESULT NTAPI ZBegReserve();
    virtual HRESULT NTAPI EnterGfMode();
    virtual HRESULT NTAPI LeaveGfMode();
    virtual HRESULT NTAPI FindStringEntry(BSTR bsParamName, PUSHORT* ppv);
    virtual HRESULT NTAPI CopyToNoOverwrite(ITXData* pData);
    virtual HRESULT NTAPI IsFieldTypeEx(BSTR bsParamName, BYTE chType, PBYTE pcCoincident);
    virtual HRESULT NTAPI GetUInt64(BSTR bsParamName, PUINT64 pddwValue);
    //virtual HRESULT NTAPI ZF07Reserve();
    //virtual HRESULT NTAPI ZF08Reserve();
    //virtual HRESULT NTAPI ZF09Reserve();
    //virtual HRESULT NTAPI ZF10Reserve();
    virtual HRESULT NTAPI ZF11Reserve();
    virtual HRESULT NTAPI ZF12Reserve();
    virtual HRESULT NTAPI ZF13Reserve();
    virtual HRESULT NTAPI ZF14Reserve();
    virtual HRESULT NTAPI ZF15Reserve();
    virtual HRESULT NTAPI ZF16Reserve();
    virtual HRESULT NTAPI ZF17Reserve();
    virtual HRESULT NTAPI ZF18Reserve();
    virtual HRESULT NTAPI ZF19Reserve();
    virtual HRESULT NTAPI ZEndReserve();
};


typedef struct ITXData : public ITXDataRead
{
/*
    VOID NTAPI SetDword(PCWSTR Name, ULONG Value)
    {
        API_POINTER(ITXData::SetDword) _SetDword;
        *(PVOID *)&_SetDword = *(PVOID *)PtrAdd(*(PVOID *)this, 0xD0);
        return (this->*_SetDword)(Name, Value);
    }
*/
    virtual HRESULT NTAPI SetBool(BSTR bsParamName, LONG bValue);
    virtual HRESULT NTAPI SetByte(BSTR bsParamName, BYTE cValue);
    virtual HRESULT NTAPI SetChar(BSTR bsParamName, CHAR chValue);
    virtual HRESULT NTAPI SetWord(BSTR bsParamName, USHORT wValue);
    virtual HRESULT NTAPI SetShort(BSTR bsParamName, SHORT shValue);
    virtual HRESULT NTAPI SetDWord(BSTR bsParamName, ULONG dwValue);
    virtual HRESULT NTAPI SetInt(BSTR bsParamName, INT iValue);
    virtual HRESULT NTAPI SetStr(BSTR bsParamName, BSTR bsValue);
    virtual HRESULT NTAPI SetBuf(BSTR bsParamName, ITXBuffer* pBufValue);
    virtual HRESULT NTAPI SetInterface(BSTR bsParamName, GUID* riid, IUnknown* pValue);
    virtual HRESULT NTAPI SetNewData(BSTR bsParamName, ITXData** ppValue);
    virtual HRESULT NTAPI SetData(BSTR bsParamName, ITXData* pValue);
    virtual HRESULT NTAPI SetNewArray(BSTR bsParamName, ITXArray** ppValue);
    virtual HRESULT NTAPI SetArray(BSTR bsParamName, ITXArray* pValue);
    virtual HRESULT NTAPI SetGuid(BSTR bsParamName, GUID* guid);
    virtual HRESULT NTAPI SetInt64(BSTR bsParamName, INT64 n64Var);
    virtual HRESULT NTAPI SetDouble(BSTR bsParamName, DOUBLE dValue);
    virtual HRESULT NTAPI SetBufTyped(BSTR bsParamName, ITXBuffer* pBufValue, ULONG dwSubType);
    virtual HRESULT NTAPI SetDoc(ITXBuffer* pBufDoc);
    virtual HRESULT NTAPI SetDoc2(UINT uSize, PBYTE pcDoc);
    virtual HRESULT NTAPI GetData(BSTR bsParamName, ITXData** ppValue);
    virtual HRESULT NTAPI GetArray(BSTR bsParamName, ITXArray** ppValue);
    virtual HRESULT NTAPI RemoveAField(BSTR bsParamName, BYTE cType);
    virtual HRESULT NTAPI Reserve(UINT uSize);
    virtual HRESULT NTAPI SetTextDoc(BSTR bstrTextDoc);
    virtual HRESULT NTAPI SetUInt64(BSTR bsParamName, UINT64 ddwValue);

} ITXData, *PITXData;

struct TXReloginMgr : public IUnknown
{
    virtual HRESULT NTAPI Login(PVOID Tray, PITXData Data);
    virtual HRESULT NTAPI Relogin(PVOID Tray, PITXData Data);
};

struct Util
{
    struct ChatSession
    {
        static BOOL (CDECL *OpenContactChatSession)(ULONG_PTR Uin, PVOID TXData);
        static HWND (CDECL *GetContactChatSessionMainHWND)(ULONG_PTR Uin);
    };

    struct Contact
    {
        static ULONG_PTR (*GetSelfUin)();
        static BOOL (CDECL *IsSuperVip)(ULONG_PTR Uin, PULONG_PTR SVipLevel);
    };

    struct Group
    {
        static BOOL (CDECL *CheckMsgImage)(PVOID GroupObject, CTXStringW &Message);
    };

    struct Data
    {
        static BOOL (CDECL *CreateTXData)(PITXData *Data);
    };
};

INIT_STATIC_MEMBER(Util::ChatSession::OpenContactChatSession);
INIT_STATIC_MEMBER(Util::ChatSession::GetContactChatSessionMainHWND);
INIT_STATIC_MEMBER(Util::Contact::GetSelfUin);
INIT_STATIC_MEMBER(Util::Contact::IsSuperVip);
INIT_STATIC_MEMBER(Util::Group::CheckMsgImage);
INIT_STATIC_MEMBER(Util::Data::CreateTXData);


typedef struct
{
    PCWSTR  DllName;
    PCSTR   FunctionName;
    PVOID   FuncAddress;

} FUNCTION_TABLE_INIT_ENTRY, *PFUNCTION_TABLE_INIT_ENTRY;

inline NTSTATUS InitializeQqFunctionTable()
{
    PVOID BaseAddress;
    PFUNCTION_TABLE_INIT_ENTRY Entry;

    static FUNCTION_TABLE_INIT_ENTRY InitEnties[] =
    {
        //{ L"Common.dll",        "?IsEmpty@CTXStringW@@QBE_NXZ",                                         &CTXStringW::ctor },
        //{ L"Common.dll",        "?IsEmpty@CTXStringW@@QBE_NXZ",                                         &CTXStringW::dtor },
        { L"Common.dll",        "?Empty@CTXStringW@@QAEXXZ",                                            &CTXStringW::StubEmpty },
        { L"Common.dll",        "?IsEmpty@CTXStringW@@QBE_NXZ",                                         &CTXStringW::StubIsEmpty },
        { L"Common.dll",        "?CreateTXData@Data@Util@@YAHPAPAUITXData@@@Z",                         &Util::Data::CreateTXData },

        { L"AppUtil.dll",       "?OpenContactChatSession@ChatSession@Util@@YAXKPAUITXData@@@Z",         &Util::ChatSession::OpenContactChatSession },
        { L"AppUtil.dll",       "?GetContactChatSessionMainHWnd@ChatSession@Util@@YAPAUHWND__@@K@Z",    &Util::ChatSession::GetContactChatSessionMainHWND },

        { L"KernelUtil.dll",    "?GetSelfUin@Contact@Util@@YAKXZ",                                      &Util::Contact::GetSelfUin },
        { L"KernelUtil.dll",    "?IsSuperVip@Contact@Util@@YAHKPAK@Z",                                  &Util::Contact::IsSuperVip },
        { L"KernelUtil.dll",    "?CheckMsgImage@Group@Util@@YAHPAUITXMsgPack@@AAVCTXStringW@@@Z",       &Util::Group::CheckMsgImage },
    };


    BaseAddress = nullptr;

    FOR_EACH_ARRAY(Entry, InitEnties)
    {
        if (Entry == InitEnties)
        {
            BaseAddress = Ldr::LoadDll(Entry->DllName);
        }
        else if(Entry->DllName != Entry[-1].DllName)
        {
            BaseAddress = Ldr::LoadDll(Entry->DllName);
        }

        *(PVOID *)Entry->FuncAddress = GetRoutineAddress(BaseAddress, Entry->FunctionName);
    }

    return STATUS_SUCCESS;
}

#endif // _QQMETHOD_H_1408431a_e0b5_4df9_a8b5_4f98002b8e00_
