package itunesdll

import (
    "ml/syscall"
)

//go:cgo_import_dynamic ituneslib/itunesdll.Proc_Initialize Initialize "iTunesHelper.dll"
//go:cgo_import_dynamic ituneslib/itunesdll.Proc_FreeMemory FreeMemory "iTunesHelper.dll"
//go:cgo_import_dynamic ituneslib/itunesdll.Proc_iTunesFreeMemory iTunesFreeMemory "iTunesHelper.dll"

//go:cgo_import_dynamic ituneslib/itunesdll.Proc_DeviceNotificationSubscribe DeviceNotificationSubscribe "iTunesHelper.dll"
//go:cgo_import_dynamic ituneslib/itunesdll.Proc_DeviceWaitForDeviceConnectionChanged DeviceWaitForDeviceConnectionChanged "iTunesHelper.dll"

//go:cgo_import_dynamic ituneslib/itunesdll.Proc_iOSDeviceCreate iOSDeviceCreate "iTunesHelper.dll"
//go:cgo_import_dynamic ituneslib/itunesdll.Proc_iOSDeviceClose iOSDeviceClose "iTunesHelper.dll"
//go:cgo_import_dynamic ituneslib/itunesdll.Proc_iOSDeviceConnect iOSDeviceConnect "iTunesHelper.dll"
//go:cgo_import_dynamic ituneslib/itunesdll.Proc_iOSDeviceDisconnect iOSDeviceDisconnect "iTunesHelper.dll"
//go:cgo_import_dynamic ituneslib/itunesdll.Proc_iOSDeviceGetProductType iOSDeviceGetProductType "iTunesHelper.dll"
//go:cgo_import_dynamic ituneslib/itunesdll.Proc_iOSDeviceGetDeviceName iOSDeviceGetDeviceName "iTunesHelper.dll"
//go:cgo_import_dynamic ituneslib/itunesdll.Proc_iOSDeviceGetDeviceClass iOSDeviceGetDeviceClass "iTunesHelper.dll"
//go:cgo_import_dynamic ituneslib/itunesdll.Proc_iOSDeviceGetProductVersion iOSDeviceGetProductVersion "iTunesHelper.dll"
//go:cgo_import_dynamic ituneslib/itunesdll.Proc_iOSDeviceGetCpuArchitecture iOSDeviceGetCpuArchitecture "iTunesHelper.dll"
//go:cgo_import_dynamic ituneslib/itunesdll.Proc_iOSDeviceGetActivationState iOSDeviceGetActivationState "iTunesHelper.dll"
//go:cgo_import_dynamic ituneslib/itunesdll.Proc_iOSDeviceGetUniqueDeviceID iOSDeviceGetUniqueDeviceID "iTunesHelper.dll"
//go:cgo_import_dynamic ituneslib/itunesdll.Proc_iOSDeviceGetUniqueDeviceIDData iOSDeviceGetUniqueDeviceIDData "iTunesHelper.dll"
//go:cgo_import_dynamic ituneslib/itunesdll.Proc_iOSDeviceIsJailBroken iOSDeviceIsJailBroken "iTunesHelper.dll"
//go:cgo_import_dynamic ituneslib/itunesdll.Proc_iOSDeviceAuthorizeDsids iOSDeviceAuthorizeDsids "iTunesHelper.dll"

//go:cgo_import_dynamic ituneslib/itunesdll.Proc_SapCreateSession SapCreateSession "iTunesHelper.dll"
//go:cgo_import_dynamic ituneslib/itunesdll.Proc_SapCloseSession SapCloseSession "iTunesHelper.dll"
//go:cgo_import_dynamic ituneslib/itunesdll.Proc_SapCreatePrimeSignature SapCreatePrimeSignature "iTunesHelper.dll"
//go:cgo_import_dynamic ituneslib/itunesdll.Proc_SapVerifyPrimeSignature SapVerifyPrimeSignature "iTunesHelper.dll"
//go:cgo_import_dynamic ituneslib/itunesdll.Proc_SapExchangeData SapExchangeData "iTunesHelper.dll"
//go:cgo_import_dynamic ituneslib/itunesdll.Proc_SapSignData SapSignData "iTunesHelper.dll"

//go:cgo_import_dynamic ituneslib/itunesdll.Proc_KbsyncCreateSession KbsyncCreateSession "iTunesHelper.dll"
//go:cgo_import_dynamic ituneslib/itunesdll.Proc_KbsyncValidate KbsyncValidate "iTunesHelper.dll"
//go:cgo_import_dynamic ituneslib/itunesdll.Proc_KbsyncGetData KbsyncGetData "iTunesHelper.dll"
//go:cgo_import_dynamic ituneslib/itunesdll.Proc_KbsyncImport KbsyncImport "iTunesHelper.dll"
//go:cgo_import_dynamic ituneslib/itunesdll.Proc_KbsyncCloseSession KbsyncCloseSession "iTunesHelper.dll"
//go:cgo_import_dynamic ituneslib/itunesdll.Proc_KbsyncSaveDsid KbsyncSaveDsid "iTunesHelper.dll"

//go:cgo_import_dynamic ituneslib/itunesdll.Proc_MachineDataStartProvisioning MachineDataStartProvisioning "iTunesHelper.dll"
//go:cgo_import_dynamic ituneslib/itunesdll.Proc_MachineDataFinishProvisioning MachineDataFinishProvisioning "iTunesHelper.dll"
//go:cgo_import_dynamic ituneslib/itunesdll.Proc_MachineDataFree MachineDataFree "iTunesHelper.dll"
//go:cgo_import_dynamic ituneslib/itunesdll.Proc_MachineDataClose MachineDataClose "iTunesHelper.dll"
//go:cgo_import_dynamic ituneslib/itunesdll.Proc_MachineDataGetData MachineDataGetData "iTunesHelper.dll"

var (
    Proc_Initialize,
    Proc_FreeMemory,
    Proc_iTunesFreeMemory,

    Proc_DeviceNotificationSubscribe,
    Proc_DeviceWaitForDeviceConnectionChanged,

    Proc_iOSDeviceCreate,
    Proc_iOSDeviceClose,
    Proc_iOSDeviceConnect,
    Proc_iOSDeviceDisconnect,
    Proc_iOSDeviceGetProductType,
    Proc_iOSDeviceGetDeviceName,
    Proc_iOSDeviceGetDeviceClass,
    Proc_iOSDeviceGetProductVersion,
    Proc_iOSDeviceGetCpuArchitecture,
    Proc_iOSDeviceGetActivationState,
    Proc_iOSDeviceGetUniqueDeviceID,
    Proc_iOSDeviceGetUniqueDeviceIDData,
    Proc_iOSDeviceIsJailBroken,
    Proc_iOSDeviceAuthorizeDsids,

    Proc_SapCreateSession,
    Proc_SapCloseSession,
    Proc_SapCreatePrimeSignature,
    Proc_SapVerifyPrimeSignature,
    Proc_SapExchangeData,
    Proc_SapSignData,

    Proc_KbsyncCreateSession,
    Proc_KbsyncValidate,
    Proc_KbsyncGetData,
    Proc_KbsyncImport,
    Proc_KbsyncCloseSession,
    Proc_KbsyncSaveDsid,

    Proc_MachineDataStartProvisioning,
    Proc_MachineDataFinishProvisioning,
    Proc_MachineDataFree,
    Proc_MachineDataClose,
    Proc_MachineDataGetData syscall.Proc
)
