#include "stdafx.h"

#pragma comment(linker, "/EXPORT:Initialize=_Initialize@0")
#pragma comment(linker, "/EXPORT:FreeMemory=_FreeMemory2@4")
#pragma comment(linker, "/EXPORT:iTunesFreeMemory=_iTunesFreeMemory@4")

#pragma comment(linker, "/EXPORT:DeviceNotificationSubscribe=_DeviceNotificationSubscribe@8")
#pragma comment(linker, "/EXPORT:DeviceWaitForDeviceConnectionChanged=_DeviceWaitForDeviceConnectionChanged@4")

#pragma comment(linker, "/EXPORT:iOSDeviceCreate=_iOSDeviceCreate@8")
#pragma comment(linker, "/EXPORT:iOSDeviceClose=_iOSDeviceClose@4")
#pragma comment(linker, "/EXPORT:iOSDeviceConnect=_iOSDeviceConnect@4")
#pragma comment(linker, "/EXPORT:iOSDeviceDisconnect=_iOSDeviceDisconnect@4")
#pragma comment(linker, "/EXPORT:iOSDeviceGetProductType=_iOSDeviceGetProductType@8")
#pragma comment(linker, "/EXPORT:iOSDeviceGetDeviceName=_iOSDeviceGetDeviceName@8")
#pragma comment(linker, "/EXPORT:iOSDeviceGetDeviceClass=_iOSDeviceGetDeviceClass@8")
#pragma comment(linker, "/EXPORT:iOSDeviceGetProductVersion=_iOSDeviceGetProductVersion@8")
#pragma comment(linker, "/EXPORT:iOSDeviceGetCpuArchitecture=_iOSDeviceGetCpuArchitecture@8")
#pragma comment(linker, "/EXPORT:iOSDeviceGetActivationState=_iOSDeviceGetActivationState@8")
#pragma comment(linker, "/EXPORT:iOSDeviceGetUniqueDeviceID=_iOSDeviceGetUniqueDeviceID@8")
#pragma comment(linker, "/EXPORT:iOSDeviceGetUniqueDeviceIDData=_iOSDeviceGetUniqueDeviceIDData@12")
#pragma comment(linker, "/EXPORT:iOSDeviceIsJailBroken=_iOSDeviceIsJailBroken@4")
#pragma comment(linker, "/EXPORT:iOSDeviceAuthorizeDsids=_iOSDeviceAuthorizeDsids@24")

#pragma comment(linker, "/EXPORT:SapCreateSession=_SapCreateSession@8")
#pragma comment(linker, "/EXPORT:SapCloseSession=_SapCloseSession@4")
#pragma comment(linker, "/EXPORT:SapCreatePrimeSignature=_SapCreatePrimeSignature@12")
#pragma comment(linker, "/EXPORT:SapVerifyPrimeSignature=_SapVerifyPrimeSignature@12")
#pragma comment(linker, "/EXPORT:SapExchangeData=_SapExchangeData@28")
#pragma comment(linker, "/EXPORT:SapSignData=_SapSignData@20")

#pragma comment(linker, "/EXPORT:KbsyncCreateSession=_KbsyncCreateSession@16")
#pragma comment(linker, "/EXPORT:KbsyncValidate=_KbsyncValidate@4")
#pragma comment(linker, "/EXPORT:KbsyncGetData=_KbsyncGetData@28")
#pragma comment(linker, "/EXPORT:KbsyncImport=_KbsyncImport@12")
#pragma comment(linker, "/EXPORT:KbsyncCloseSession=_KbsyncCloseSession@4")
#pragma comment(linker, "/EXPORT:KbsyncSaveDsid=_KbsyncSaveDsid@12")

iTunesHelper *helper;

EXTC NTSTATUS NTAPI Initialize()
{
    NTSTATUS status;

    if (helper != nullptr)
        return STATUS_SUCCESS;

    helper = new iTunesHelper;

    DebugLog(L"create iTunesHelper");

    //Rtl::SetExeDirectoryAsCurrent();

    status = helper->iTunesInitialize();
    DebugLog(L"iTunesInitialize return %p", status);
    if (NT_FAILED(status))
    {
        ExceptionBox(L"init iTunes failed");
        return status;
    }

    return status;
}

EXTC VOID NTAPI FreeMemory2(PVOID p)
{
    FreeMemoryP(p);
}

EXTC VOID NTAPI iTunesFreeMemory(PVOID p)
{
    helper->FreeSessionData(p);
}

EXTC
NTSTATUS
NTAPI
DeviceNotificationSubscribe(
    iTunesHelper::DeviceNotificationCallback Callback,
    PVOID Context
)
{
    return helper->DeviceNotificationSubscribe(Callback, Context);
}

EXTC NTSTATUS NTAPI DeviceWaitForDeviceConnectionChanged(ULONG Timeout)
{
    return helper->WaitForDeviceConnectionChanged(Timeout);
}

/*++

    iOSDevice

--*/

EXTC NTSTATUS NTAPI iOSDeviceCreate(PIOS_DEVICE Device, iOSDevice **iosDevice)
{
    *iosDevice = new iOSDevice(Device);
    return *iosDevice == nullptr ? STATUS_NO_MEMORY : STATUS_SUCCESS;
}

EXTC NTSTATUS NTAPI iOSDeviceClose(iOSDevice *iosDevice)
{
    delete iosDevice;
    return STATUS_SUCCESS;
}

EXTC NTSTATUS NTAPI iOSDeviceConnect(iOSDevice &Device)
{
    return Device.ConnectDevice();
}

EXTC NTSTATUS NTAPI iOSDeviceDisconnect(iOSDevice &Device)
{
    return Device.DisconnectDevice();
}

NTSTATUS iOSDeviceGetStringValue(iOSDevice &Device, String (iOSDevice::*func)(), PSTR *Output)
{
    const auto &productType = (&Device->*func)().Encode(CP_UTF8);

    *Output = (PSTR)AllocateMemoryP(productType.GetSize());
    if (*Output != nullptr)
        CopyMemory(*Output, productType.GetData(), productType.GetSize());

#if 0

    iOSService house_arrest(Device);
    house_arrest.Start("com.apple.mobile.house_arrest");

    iOSAFC afc;

    afc.CreateConnection(house_arrest);

#endif

    return *Output == nullptr ? STATUS_NO_MEMORY : STATUS_SUCCESS;
}

NTSTATUS iOSDeviceGetDataValue(iOSDevice &Device, CFData (iOSDevice::*func)(), PVOID *Output, PULONG_PTR OutputSize)
{
    CFData data = (&Device->*func)();

    *OutputSize = CFDataGetLength(data);
    *Output = (PSTR)AllocateMemoryP(*OutputSize);
    if (*Output != nullptr)
        CopyMemory(*Output, CFDataGetBytePtr(data), *OutputSize);

    return *Output == nullptr ? STATUS_NO_MEMORY : STATUS_SUCCESS;
}

EXTC NTSTATUS NTAPI iOSDeviceGetProductType(iOSDevice &Device, PSTR *ProductType)
{
    return iOSDeviceGetStringValue(Device, &iOSDevice::GetProductType, ProductType);
}

EXTC NTSTATUS NTAPI iOSDeviceGetDeviceName(iOSDevice &Device, PSTR *DeviceName)
{
    return iOSDeviceGetStringValue(Device, &iOSDevice::GetDeviceName, DeviceName);
}

EXTC NTSTATUS NTAPI iOSDeviceGetDeviceClass(iOSDevice &Device, PSTR *DeviceClass)
{
    return iOSDeviceGetStringValue(Device, &iOSDevice::GetDeviceClass, DeviceClass);
}

EXTC NTSTATUS NTAPI iOSDeviceGetProductVersion(iOSDevice &Device, PSTR *ProductVersion)
{
    return iOSDeviceGetStringValue(Device, &iOSDevice::GetProductVersion, ProductVersion);
}

EXTC NTSTATUS NTAPI iOSDeviceGetCpuArchitecture(iOSDevice &Device, PSTR *DeviceType)
{
    return iOSDeviceGetStringValue(Device, &iOSDevice::GetCPUArchitecture, DeviceType);
}

EXTC NTSTATUS NTAPI iOSDeviceGetActivationState(iOSDevice &Device, PSTR *ActivationState)
{
    return iOSDeviceGetStringValue(Device, &iOSDevice::GetActivationState, ActivationState);
}

EXTC NTSTATUS NTAPI iOSDeviceGetUniqueDeviceID(iOSDevice &Device, PSTR *DeviceID)
{
    return iOSDeviceGetStringValue(Device, &iOSDevice::GetUniqueDeviceID, DeviceID);
}

EXTC NTSTATUS NTAPI iOSDeviceGetUniqueDeviceIDData(iOSDevice &Device, PVOID* Output, PULONG_PTR OutputSize)
{
    return iOSDeviceGetDataValue(Device, &iOSDevice::GetUniqueDeviceIDData, Output, OutputSize);
}

EXTC BOOL NTAPI iOSDeviceIsJailBroken(iOSDevice &Device)
{
    return Device.IsJailbroken() == kAMDSuccess;
}

EXTC NTSTATUS NTAPI iOSDeviceAuthorizeDsids(iOSDevice &Device, PCSTR SCInfoPath, PULONG64 Dsids, ULONG Count, PULONG64* Authed, PULONG AuthedCount)
{
    NTSTATUS status;
    GrowableArray<ULONG64> dsidToAuth, dsidAuthed;

    for (; Count; --Count)
        dsidToAuth.Add(*Dsids++);

    status = Device.AuthorizeDsids(helper, SCInfoPath, dsidToAuth, dsidAuthed);
    if (status != STATUS_SUCCESS)
        return status;

    if (Authed != nullptr && dsidAuthed.GetSize() != 0)
    {
        ULONG_PTR size = dsidAuthed.GetSize() * sizeof(*Dsids);

        *Authed = (PULONG64)AllocateMemoryP(size);
        if (*Authed == nullptr)
            return STATUS_NO_MEMORY;

        CopyMemory(*Authed, dsidAuthed.GetData(), size);
        *AuthedCount = (ULONG)dsidAuthed.GetSize();
    }

    return status;
}

/*++

    sap

--*/

EXTC NTSTATUS NTAPI SapCreateSession(PHANDLE SapSession, PFAIR_PLAY_HW_INFO DeviceId)
{
    return helper->SapCreateSession(SapSession, DeviceId);
}

EXTC NTSTATUS NTAPI SapCloseSession(HANDLE SapSession)
{
    return helper->SapCloseSession(SapSession);
}

EXTC NTSTATUS NTAPI SapCreatePrimeSignature(HANDLE SapSession, PVOID* Output, PULONG_PTR OutputSize)
{
    return helper->SapCreatePrimeSignature(SapSession, Output, OutputSize);
}

EXTC NTSTATUS NTAPI SapVerifyPrimeSignature(HANDLE SapSession, PVOID Signature, ULONG_PTR SignatureSize)
{
    return helper->SapVerifyPrimeSignature(SapSession, Signature, SignatureSize);
}

EXTC
NTSTATUS
NTAPI
SapExchangeData(
    HANDLE              SapSession,
    ULONG_PTR           CertType,
    PFAIR_PLAY_HW_INFO  DeviceId,
    PVOID               CertData,
    ULONG_PTR           CertSize,
    PVOID*              Output,
    PULONG_PTR          OutputSize
)
{
    return helper->SapExchangeData(CertType, DeviceId, SapSession, CertData, CertSize, Output, OutputSize);
}

EXTC
NTSTATUS
NTAPI
SapSignData(
    HANDLE      SapSession,
    PVOID       Data,
    ULONG_PTR   DataSize,
    PVOID*      Signature,
    PULONG_PTR  SignatureSize
)
{
    return helper->SapSignData(SapSession, Data, DataSize, Signature, SignatureSize);
}

EXTC
NTSTATUS
NTAPI
KbsyncCreateSession(
    PHANDLE             kbsyncSession,
    PFAIR_PLAY_HW_INFO  machineId,
    PFAIR_PLAY_HW_INFO  machineId2,
    PCSTR               scInfoPath
)
{
    FAIR_PLAY_HW_INFO localMachineId[2];

    if (machineId == nullptr && machineId2 == nullptr)
    {
        machineId = &localMachineId[0];
        machineId2 = &localMachineId[1];

        helper->GetDeviceId(machineId, machineId2);
    }
    //else if (machineId == nullptr || machineId2 == nullptr)
    //{
    //    return STATUS_INVALID_PARAMETER;
    //}

    return helper->KbsyncCreateSession(kbsyncSession, machineId, machineId2, scInfoPath);
}

EXTC
NTSTATUS
NTAPI
KbsyncValidate(
    HANDLE kbsyncSession
)
{
    return helper->KbsyncValidate(kbsyncSession);
}

EXTC
NTSTATUS
NTAPI
KbsyncGetData(
    HANDLE      kbsyncSession,
    ULONG64     dsid,
    ULONG       quickTimeVersion,
    ULONG       syncType,
    PVOID*      output,
    PULONG_PTR  outputSize
)
{
    return helper->KbsyncGetData(kbsyncSession, dsid, quickTimeVersion, syncType, output, outputSize);
}

EXTC
NTSTATUS
NTAPI
KbsyncSaveDsid(
    HANDLE      kbsyncSession,
    ULONG64     dsid
)
{
    return helper->KbsyncSaveDsid(kbsyncSession, dsid);
}

EXTC
NTSTATUS
NTAPI
KbsyncImport(
    HANDLE      kbsyncSession,
    PVOID       keybag,
    ULONG_PTR   size
)
{
    return helper->KbsyncImport(kbsyncSession, keybag, size);
}

EXTC
NTSTATUS
NTAPI
KbsyncCloseSession(
    HANDLE session
)
{
    return helper->KbsyncCloseSession(session);
}
