@echo off
setlocal ENABLEDELAYEDEXPANSION

cd/d "%~dp0"

call D:\Dev\go\init.bat

for /f %%i in ('dir/b *.go') do (
    findstr /X /B /C:"func main() {" "%%~fi" >NUL 2>NUL
    if !ERRORLEVEL! == 0 (
        go.exe build "%%~fi"
        goto:END
    )
)

:END

if not %ERRORLEVEL% == 0 (
    pause
)
