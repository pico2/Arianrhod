package ituneslib

import (
    "reflect"
    "sync/atomic"
    _itunesdll "ituneslib/itunesdll"
)

var itunesInitialized uintptr = 0

func Initialize() {
    if atomic.CompareAndSwapUintptr(&itunesInitialized, 0, 1) == false {
        return
    }

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

    itunes.Initialize.Call()
    sapInitialize()
}

func FreeSessionData(ptr interface{}) {
    itunes.iTunesFreeMemory.Call(reflect.ValueOf(ptr).Pointer())
}

func freeMachineData(ptr interface{}) {
    itunes.MachineDataFree.Call(reflect.ValueOf(ptr).Pointer())
}

func FreeMemory(ptr interface{}) {
    itunes.FreeMemory.Call(reflect.ValueOf(ptr).Pointer())
}

func init() {
    // base := syscall.MustLoadDLL(filepath.Join(os2.ExecutablePath(), "iTunesHelper.dll"))

    // t := reflect.TypeOf(itunes)
    // v := reflect.ValueOf(&itunes).Elem()
    // for i, n := 0, t.NumField(); i != n; i++ {
    //     name := t.Field(i).Name
    //     v.Field(i).Set(reflect.ValueOf(base.MustFindProc(name)))
    // }
}
