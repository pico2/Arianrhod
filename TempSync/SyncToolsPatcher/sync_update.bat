@echo off
setlocal

start /MIN D:\TortoiseSVN\bin\TortoiseProc.exe /command:update /path:"E:\SyncPrivate\" /closeonend:2

rem "D:\TortoiseGit\bin\TortoiseGitProc.exe" /command:pull /path:"E:\Sync\" /closeonend:2

for /F "delims=" %%I in ("D:\PortableGit") do @set git_install_root=%%~fI
set PATH=%git_install_root%\bin;%git_install_root%\mingw\bin;%git_install_root%\cmd;%PATH%

if not exist "%HOME%" @set HOME=%HOMEDRIVE%%HOMEPATH%
if not exist "%HOME%" @set HOME=%USERPROFILE%

set PLINK_PROTOCOL=ssh

cd %HOME%

cd/d "E:\Sync"

git pull

pause

