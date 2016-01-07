package ituneslib

import (
    "syscall"
    "sync"
)

type iTunesHelper struct {
    Initialize                              *syscall.Proc
    FreeMemory                              *syscall.Proc
    iTunesFreeMemory                        *syscall.Proc

    DeviceNotificationSubscribe             *syscall.Proc
    DeviceWaitForDeviceConnectionChanged    *syscall.Proc

    iOSDeviceCreate                         *syscall.Proc
    iOSDeviceClose                          *syscall.Proc
    iOSDeviceConnect                        *syscall.Proc
    iOSDeviceDisconnect                     *syscall.Proc
    iOSDeviceGetProductType                 *syscall.Proc
    iOSDeviceGetDeviceName                  *syscall.Proc
    iOSDeviceGetDeviceClass                 *syscall.Proc
    iOSDeviceGetProductVersion              *syscall.Proc
    iOSDeviceGetCpuArchitecture             *syscall.Proc
    iOSDeviceGetActivationState             *syscall.Proc
    iOSDeviceGetUniqueDeviceID              *syscall.Proc
    iOSDeviceGetUniqueDeviceIDData          *syscall.Proc
    iOSDeviceIsJailBroken                   *syscall.Proc
    iOSDeviceAuthorizeDsids                 *syscall.Proc

    SapCreateSession                        *syscall.Proc
    SapCloseSession                         *syscall.Proc
    SapCreatePrimeSignature                 *syscall.Proc
    SapVerifyPrimeSignature                 *syscall.Proc
    SapExchangeData                         *syscall.Proc
    SapSignData                             *syscall.Proc

    KbsyncCreateSession                     *syscall.Proc
    KbsyncValidate                          *syscall.Proc
    KbsyncGetData                           *syscall.Proc
    KbsyncImport                            *syscall.Proc
    KbsyncCloseSession                      *syscall.Proc
    KbsyncSaveDsid                          *syscall.Proc
}

var lock = sync.Mutex{}
var itunes = iTunesHelper{}
var deviceMap = map[uintptr]*IosDevice{}
var deviceNotifications = map[uintptr]func(device *IosDevice, remove bool){}
