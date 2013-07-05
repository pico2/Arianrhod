@echo off
setlocal

rem start "" /MIN "C:\Program Files\TortoiseSVN\bin\TortoiseProc.exe" /command:update /path:"E:\SyncPrivate\" /closeonend:2

for /F "delims=" %%I in ("F:\PortableGit") do @set git_install_root=%%~fI
set PATH=%git_install_root%\bin;%git_install_root%\mingw\bin;%git_install_root%\cmd;%PATH%

if not exist "%HOME%" @set HOME=%HOMEDRIVE%%HOMEPATH%
if not exist "%HOME%" @set HOME=%USERPROFILE%

set PLINK_PROTOCOL=ssh

cd %HOME%

cd/d "E:\Sync"

git pull

echo.
echo private...
echo.

cd/d "E:\SyncPrivate\"

git pull

pause