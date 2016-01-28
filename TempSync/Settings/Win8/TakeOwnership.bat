@echo off
cd/d "%~dp0"

takeown /f "%~f1" /r /d y
icacls "%~f1" /grant administrators:F /t

pause
