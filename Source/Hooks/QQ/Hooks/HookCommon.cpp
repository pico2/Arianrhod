#include "Hooks.h"

BOOL    (CDECL *StubGetPlatformCore)(PVOID *Core);
BOOL    (CDECL *StubInitPluginFileSystem)(PCWSTR PluginName);
HRESULT (NTAPI *StubPlatformCore_QueryInterface)(PVOID Object, REFGUID Guid, PVOID Output);
HRESULT (NTAPI *StubGroupMgr_QueryGroupObject)(PVOID Object, ULONG_PTR GroupUin, PVOID *GroupObject);
HRESULT (NTAPI *StubGroupMgr_GetAdminFlags)(PVOID Object, ULONG_PTR Uin, PBOOL IsAdmin, PBOOL IsCreator);

BOOL CDECL IsTencentTrusted(PCWSTR FileName)
{
    ODS(L"%S", __FUNCTION__);
    return TRUE;
}

BOOL CDECL InitPluginFileSystem(PCWSTR PluginName)
{
    PWSTR       Buffer, Name;
    ULONG_PTR   BufferSize, Length;
    PLDR_MODULE Module;

    static WCHAR PluginPath[] = L"..\\Plugin\\";
    static WCHAR Disabled[] = L"\\Disabled";

    ODS(L"%S", __FUNCTION__);

    Module = FindLdrModuleByHandle(nullptr);
    Length = (StrLengthW(PluginName) + 1) * sizeof(WCHAR);
    BufferSize = Module->FullDllName.Length + Length + sizeof(PluginPath);
    Buffer = (PWSTR)AllocStack(BufferSize + sizeof(Disabled));
    CopyMemory(Buffer, Module->FullDllName.Buffer, Module->FullDllName.Length);

    Name = findnamew(Buffer);
    CopyMemory(Name, PluginPath, sizeof(PluginPath));
    CopyMemory(Name + CONST_STRLEN(PluginPath), PluginName, Length);

    if (Io::IsPathExists(Buffer) == FALSE)
        return FALSE;

    CopyMemory(Name + CONST_STRLEN(PluginPath) + Length / 2 - 1, Disabled, sizeof(Disabled));

    if (Io::IsPathExists(Buffer))
        return FALSE;

    return StubInitPluginFileSystem(PluginName);
}

HRESULT NTAPI GroupMgr_GetAdminFlags(PVOID Object, ULONG_PTR Uin, PBOOL IsAdmin, PBOOL IsCreator)
{
    HRESULT Result;

    Result = StubGroupMgr_GetAdminFlags(Object, Uin, IsAdmin, IsCreator);

    if (Uin == Util::Contact::GetSelfUin()) LOOP_ONCE
    {
        if ((IsAdmin != nullptr && *IsAdmin != FALSE) || (IsCreator != nullptr && *IsCreator != FALSE))
            break;

        if (IsAdmin != nullptr)
        {
            *IsAdmin = TRUE;
            break;
        }

        if (IsCreator != nullptr)
        {
            *IsCreator = TRUE;
            break;
        }
    }

    return S_OK;
}

HRESULT NTAPI GroupMgr_QueryGroupObject(PVOID Object, ULONG_PTR GroupUin, PVOID *GroupObject)
{
    HRESULT Result;

    Result = StubGroupMgr_QueryGroupObject(Object, GroupUin, GroupObject);

    if (SUCCEEDED(Result) && StubGroupMgr_GetAdminFlags == nullptr)
    {
        Mp::PATCH_MEMORY_DATA p[] =
        {
            Mp::FunctionJumpVa(*(PVOID *)PtrAdd(**(PVOID **)GroupObject, 0x5C), GroupMgr_GetAdminFlags, &StubGroupMgr_GetAdminFlags),
        };

        Mp::PatchMemory(p, countof(p));
    }

    return Result;
}

ULONG NTAPI GroupObject_GetAtAllGroupMemberUseTimes(PVOID)
{
    return 1;
}

HRESULT NTAPI GroupObject_QueryInterface(PVOID Object, REFGUID Guid, PVOID *Output)
{
    HRESULT Result;

    Result = StubPlatformCore_QueryInterface(Object, Guid, Output);
    if (FAILED(Result))
        return Result;

    PVOID& GetAtAllGroupMemberUseTimes = *(PVOID *)PtrAdd(**(PVOID **)Output, 0x10);

    if (GetAtAllGroupMemberUseTimes == GroupObject_GetAtAllGroupMemberUseTimes)
        return Result;

    Mp::PATCH_MEMORY_DATA p[] =
    {
        Mp::MemoryPatchVa((ULONG_PTR)GroupObject_GetAtAllGroupMemberUseTimes, sizeof(ULONG_PTR), &GetAtAllGroupMemberUseTimes),
    };

    Mp::PatchMemory(p, countof(p));

    return Result;
}

HRESULT NTAPI GroupMgr_QueryInterface(PVOID Object, REFGUID Guid, PVOID *Output)
{
    HRESULT Result;

    Result = StubPlatformCore_QueryInterface(Object, Guid, Output);

    if (SUCCEEDED(Result) && StubGroupMgr_QueryGroupObject == nullptr)
    {
        Mp::PATCH_MEMORY_DATA p[] =
        {
            Mp::FunctionJumpVa(*(PVOID *)PtrAdd(**(PVOID **)Output, 0x24), GroupMgr_QueryGroupObject, &StubGroupMgr_QueryGroupObject),
        };

        Mp::PatchMemory(p, countof(p));
    }

    return Result;
}

// CTXComponentMgr

HRESULT NTAPI PlatformCore_QueryInterface(PVOID Object, REFGUID Guid, PVOID *Output)
{
    static GUID GUID_FilterList[] =
    {
        { 0x41D26ED5, 0x7680, 0x4631, 0xBC, 0xC1, 0x5E, 0x52, 0x30, 0x37, 0xF7, 0x0A }, // GUID_PluginCenter
        { 0x76063A86, 0xD553, 0x44A6, 0xAF, 0x7A, 0x12, 0xAE, 0x87, 0x21, 0x1A, 0xA7 }, // GUID_GroupMgr
        { 0xC8730021, 0xE7DE, 0x4F65, 0x98, 0x8C, 0x7D, 0x69, 0x4C, 0x38, 0x83, 0x6E }, // GUID_DllHashCheckMgr
        { 0x3A990F4E, 0x95BC, 0x4F00, 0xAE, 0x52, 0xFD, 0xD9, 0xFB, 0xFF, 0x30, 0x3E }, // GUID_ReloginMgr
        //{ 0xD302C850, 0x939F, 0x4575, 0x85, 0xBE, 0xE0, 0x45, 0x11, 0x42, 0x1A, 0x75 }, // GUID_GroupObject
    };

    enum
    {
        GUID_PluginCenter,
        GUID_GroupMgr,
        GUID_DllHashCheckMgr,
        GUID_ReloginMgr,
        GUID_GroupObject,
    };

    GUID *Filter;

    LOOP_ONCE
    {
        PLDR_MODULE AppUtil;

        if (Output != nullptr)
            *Output = nullptr;

        FOR_EACH_ARRAY(Filter, GUID_FilterList)
        {
            if (Guid == *Filter)
                break;
        }

        switch (Filter - GUID_FilterList)
        {
            case countof(GUID_FilterList):
                continue;

            case GUID_PluginCenter:
                ODS(L"GUID_PluginCenter");
                //continue;

                AppUtil = FindLdrModuleByHandle(_ReturnAddress());
                if (AppUtil != nullptr && AppUtil->DllBase == AppUtilBase)
                    continue;
                break;

            case GUID_GroupMgr:
                return GroupMgr_QueryInterface(Object, Guid, Output);

            case GUID_ReloginMgr:
            {
#if 1
                continue;
#else

                HRESULT hr = StubPlatformCore_QueryInterface(Object, Guid, Output);

                if (ReloginMgr == nullptr && SUCCEEDED(hr))
                {
                    ReloginMgr = (TXReloginMgr *)*Output;
                    ReloginMgr->AddRef();
                }

                return hr;
#endif

            }

            //case GUID_GroupObject:
                //continue;
                //return GroupObject_QueryInterface(Object, Guid, Output);
        }

        return E_NOINTERFACE;
    }

    return StubPlatformCore_QueryInterface(Object, Guid, Output);
}

BOOL CDECL GetPlatformCore(PVOID *Core)
{
    BOOL Success;

    //AllocConsole();
    //ShowWindow(GetConsoleWindow(), SW_SHOW);
    //PrintConsole(L"%p: query\n", (ULONG)NtGetTickCount());
    NtTestAlert();

    Success = StubGetPlatformCore(Core);
    if (!Success)
        return Success;

    if (StubPlatformCore_QueryInterface != nullptr)
        return Success;

    Mp::PATCH_MEMORY_DATA f[] =
    {
        Mp::FunctionJumpVa(*(PVOID *)PtrAdd(**(PVOID **)Core, 0x20), PlatformCore_QueryInterface, &StubPlatformCore_QueryInterface),
    };

    Mp::PatchMemory(f, countof(f));

    return Success;
}

NTSTATUS HookCommon(PVOID BaseAddress)
{
    Mp::PATCH_MEMORY_DATA Function_Common[] =
    {
        Mp::FunctionJumpVa(LookupExportTable(BaseAddress, "?IsTencentTrusted@Misc@Util@@YAHPB_W@Z"),            IsTencentTrusted),
        Mp::FunctionJumpVa(LookupExportTable(BaseAddress, "?InitPluginFileSystem@Boot@Util@@YAHPA_W@Z"),        InitPluginFileSystem,   &StubInitPluginFileSystem),
        Mp::FunctionJumpVa(LookupExportTable(BaseAddress, "?GetPlatformCore@Core@Util@@YAHPAPAUITXCore@@@Z"),   GetPlatformCore,        &StubGetPlatformCore),
    };

    return Mp::PatchMemory(Function_Common, countof(Function_Common), BaseAddress);
}
