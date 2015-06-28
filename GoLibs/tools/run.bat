@echo off
setlocal ENABLEDELAYEDEXPANSION
cd/d "%~dp0"

call init.bat

cd/d "%~dp1"

for /f %%i in ('dir/b *.go') do (
    findstr /X /B /C:"func main() {" "%%~fi" >NUL 2>NUL
    if !ERRORLEVEL! == 0 (
        call:BUILD_AND_RUN "%%~fi"
        goto:EXIT
    )
)

echo can't find func main()
pause
goto:eof

:BUILD_AND_RUN
call:BUILD "%~f1"

if not %ERRORLEVEL% == 0 (
    pause
    goto:eof
)

call:RUN "%~dpn1.exe"
goto:eof

:BUILD
del "%~dpn1.exe" >NUL 2>NUL
go.exe build -ldflags "-s" "%~f1"
goto:eof

:RUN
call "%~f1"
goto:eof

:EXIT
goto:eof
