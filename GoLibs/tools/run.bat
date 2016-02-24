@echo off
setlocal ENABLEDELAYEDEXPANSION
cd/d "%~dp0"

if [%1]==[] goto:eof

call init.bat

cd/d "%~dp1"

findstr /C:"package test" "%~f1" >NUL 2>NUL
if %ERRORLEVEL% == 0 (
    call:BUILD_AND_TEST "%~f1"
    goto:EXIT
)

findstr /C:"func main() {" "%~f1" >NUL 2>NUL
if %ERRORLEVEL% == 0 (
    call:BUILD_AND_RUN "%~f1"
    goto:EXIT
)

for /f %%i in ('dir/b *.go') do (
    findstr /C:"func main() {" "%%~fi" >NUL 2>NUL
    if !ERRORLEVEL! == 0 (
        call:BUILD_AND_RUN "%%~fi"
        goto:EXIT
    )
)

echo can't find func main()
pause
goto:eof

:BUILD_AND_RUN
call:DELETE_AUTO_INSTALL_PKGS "%~f1\.."
call:BUILD "%~f1"

if not %ERRORLEVEL% == 0 (
    pause
    goto:eof
)

call:RUN "%~dpn1.exe"
goto:eof

:BUILD_AND_TEST
call:DELETE_AUTO_INSTALL_PKGS "%~f1\.."
go.exe test -v "%~f1"
pause
goto:eof

:DELETE_AUTO_INSTALL_PKGS
call:DELETE_AUTO_INSTALL_PKGS2 "%~f1.x" >NUL 2>NUL
goto:eof

:DELETE_AUTO_INSTALL_PKGS2
set "p=%~dp1"
if [%p:~-4%] == [src\] (
    for /f %%i in ('dir/s/b %~dp1\..\pkg\%~n1') do (
        rd/s/q "%%i"
    )
) else (
    for /f %%i in ('dir/s/b %~dp1\pkg\%~n1') do (
        rd/s/q "%%i"
    )
)
goto:eof

:BUILD
del "%~dpn1.exe" >NUL 2>NUL

call:DELETE_ML_PKG >NUL 2>NUL

:: -H windowsgui  -extldflags=--large-address-aware
rem go.exe build -ldflags "-s" "%~f1"
go.exe build "%~f1"
::go.exe build "%~f1"
goto:eof

:RUN
call "%~f1"
pause
goto:eof

:EXIT
goto:eof

:DELETE_ML_PKG
goto:eof
if [%1] == [] (
    for /f %%i in ('dir/s/b "%~dp0\pkgs\pkg\ml"') do (
        call:DELETE_ML_PKG "%%~fi.a"
        goto:eof
    )
) else (
    del/q "%~f1"
    rd/s/q "%~dpn1"
)

goto:eof
