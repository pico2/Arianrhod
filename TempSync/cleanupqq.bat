@echo off
cd/d "%~dp0\Files\Bin"

copy ..\..\QQ2013\Bin\Amano.dll .

set DEBUG=

for %%f in (auclt.exe QQApp.exe QQExternal.exe QQPI.exe QQSafeUD.exe StorageTool.exe Tencentdl.exe Timwp.exe TXPlatform.exe QScanEngine.dll) do (
    %DEBUG% ren %%f %%~nf2%%~xf
)

cd..

rd/s/q QQProtect

echo D|xcopy /y /e ..\QQ2013\Misc\Sound .\Misc\Sound

del QQUninst.exe txupd.exe

cd Plugin

for %%p in (^
    Com.Tencent.Advertisement ^
    Com.Tencent.CRM ^
    Com.Tencent.GameLife ^
    Com.Tencent.Graffito ^
    Com.Tencent.HRTX ^
    Com.Tencent.Memo ^
    Com.Tencent.MMOG ^
    Com.Tencent.NetBar ^
    Com.Tencent.PaiPai ^
    Com.Tencent.PayCenter ^
    Com.Tencent.QQGame ^
    Com.Tencent.QQLive ^
    Com.Tencent.QQMusic ^
    Com.Tencent.QQPet ^
    Com.Tencent.QQRing ^
    Com.Tencent.QQShow ^
    Com.Tencent.QQWebsite ^
    Com.Tencent.QT ^
    Com.Tencent.Soso ^
    Com.Tencent.SpeedDating ^
    Com.Tencent.Stock ^
    Com.Tencent.Today ^
    Com.Tencent.VAS ^
    Com.Tencent.WBlog ^
    Com.Tencent.WenWen ^
    Com.Tencent.Winks
) do (

    %DEBUG% rd/s/q %%p
)
