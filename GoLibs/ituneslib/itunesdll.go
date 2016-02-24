package ituneslib

import (
    "ml/syscall"
    _itunesdll "ituneslib/itunesdll"
)

type _itunesAPI struct {
    Initialize,
    FreeMemory,
    iTunesFreeMemory,

    DeviceNotificationSubscribe,
    DeviceWaitForDeviceConnectionChanged,

    iOSDeviceCreate,
    iOSDeviceClose,
    iOSDeviceConnect,
    iOSDeviceDisconnect,
    iOSDeviceGetProductType,
    iOSDeviceGetDeviceName,
    iOSDeviceGetDeviceClass,
    iOSDeviceGetProductVersion,
    iOSDeviceGetCpuArchitecture,
    iOSDeviceGetActivationState,
    iOSDeviceGetUniqueDeviceID,
    iOSDeviceGetUniqueDeviceIDData,
    iOSDeviceIsJailBroken,
    iOSDeviceAuthorizeDsids,

    SapCreateSession,
    SapCloseSession,
    SapCreatePrimeSignature,
    SapVerifyPrimeSignature,
    SapExchangeData,
    SapSignData,

    KbsyncCreateSession,
    KbsyncValidate,
    KbsyncGetData,
    KbsyncImport,
    KbsyncCloseSession,
    KbsyncSaveDsid,

    MachineDataStartProvisioning,
    MachineDataFinishProvisioning,
    MachineDataFree,
    MachineDataClose,
    MachineDataGetData syscall.Proc
}

var itunes _itunesAPI

func itunesDllInitialize()  {
    itunes = _itunesAPI{
        _itunesdll.Proc_Initialize,
        _itunesdll.Proc_FreeMemory,
        _itunesdll.Proc_iTunesFreeMemory,
        _itunesdll.Proc_DeviceNotificationSubscribe,
        _itunesdll.Proc_DeviceWaitForDeviceConnectionChanged,
        _itunesdll.Proc_iOSDeviceCreate,
        _itunesdll.Proc_iOSDeviceClose,
        _itunesdll.Proc_iOSDeviceConnect,
        _itunesdll.Proc_iOSDeviceDisconnect,
        _itunesdll.Proc_iOSDeviceGetProductType,
        _itunesdll.Proc_iOSDeviceGetDeviceName,
        _itunesdll.Proc_iOSDeviceGetDeviceClass,
        _itunesdll.Proc_iOSDeviceGetProductVersion,
        _itunesdll.Proc_iOSDeviceGetCpuArchitecture,
        _itunesdll.Proc_iOSDeviceGetActivationState,
        _itunesdll.Proc_iOSDeviceGetUniqueDeviceID,
        _itunesdll.Proc_iOSDeviceGetUniqueDeviceIDData,
        _itunesdll.Proc_iOSDeviceIsJailBroken,
        _itunesdll.Proc_iOSDeviceAuthorizeDsids,
        _itunesdll.Proc_SapCreateSession,
        _itunesdll.Proc_SapCloseSession,
        _itunesdll.Proc_SapCreatePrimeSignature,
        _itunesdll.Proc_SapVerifyPrimeSignature,
        _itunesdll.Proc_SapExchangeData,
        _itunesdll.Proc_SapSignData,
        _itunesdll.Proc_KbsyncCreateSession,
        _itunesdll.Proc_KbsyncValidate,
        _itunesdll.Proc_KbsyncGetData,
        _itunesdll.Proc_KbsyncImport,
        _itunesdll.Proc_KbsyncCloseSession,
        _itunesdll.Proc_KbsyncSaveDsid,
        _itunesdll.Proc_MachineDataStartProvisioning,
        _itunesdll.Proc_MachineDataFinishProvisioning,
        _itunesdll.Proc_MachineDataFree,
        _itunesdll.Proc_MachineDataClose,
        _itunesdll.Proc_MachineDataGetData,
    }
}