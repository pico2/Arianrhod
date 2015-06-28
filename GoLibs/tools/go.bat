@echo off
cd/d "%~dp0"

call init.bat

go.exe %*

if not %ERRORLEVEL% == 0 (
    pause
)
