package ituneslib

import (
    "ml/syscall"
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
