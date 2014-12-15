Windows Registry Editor Version 5.00

/*

@echo off
cls
cd/d "%~dp0"

regedit -s %0

copy /y ShimEng.sdb "%windir%\AppPatch\Custom\{994cb191-ae13-4e75-a12c-014e8354a668}.sdb" >NUL 2>NUL
copy /y ShimEngine.dll "%windir%\AppPatch\" >NUL 2>NUL

wmic ENVIRONMENT where "name='__COMPAT_LAYER'" delete >NUL 2>NUL
WMIC ENVIRONMENT create name="__COMPAT_LAYER",username="<SYSTEM>",VariableValue="# AmanoShimLayer" >NUL 2>NUL
Notify.exe

echo press any key to uninstall

pause >NUL

wmic ENVIRONMENT where "name='__COMPAT_LAYER'" delete >NUL 2>NUL
Notify.exe

reg delete "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Custom\Layers\AmanoShimLayer" /f >NUL 2>NUL
reg delete "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\InstalledSDB\{994cb191-ae13-4e75-a12c-014e8354a668}" /f >NUL 2>NUL

del /q "%windir%\AppPatch\Custom\{994cb191-ae13-4e75-a12c-014e8354a668}.sdb" >NUL 2>NUL
del /q "%windir%\AppPatch\ShimEngine.dll" >NUL 2>NUL

goto:eof

*/

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Custom\Layers\AmanoShimLayer]
"{994cb191-ae13-4e75-a12c-014e8354a668}.sdb"=hex(b):44,88,34,e0,39,4c,cd,01

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\InstalledSDB\{994cb191-ae13-4e75-a12c-014e8354a668}]
"DatabasePath"="C:\\Windows\\AppPatch\\Custom\\{994cb191-ae13-4e75-a12c-014e8354a668}.sdb"
"DatabaseType"=dword:00010000
"DatabaseDescription"="AmanoShimEngineSdb"
"DatabaseInstallTimeStamp"=hex(b):58,cf,5f,b7,64,4c,cd,01

