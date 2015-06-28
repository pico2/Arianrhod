@echo off
cd/d "%~dp0"

call init.bat

cd/d "%~dp1"

go.exe build -ldflags "-s" %1

if not %ERRORLEVEL% == 0 (
    pause
)
