@echo off
cd/d "%~dp1"
"%~dp0protoc.exe" --python_out=. "%~nx1"
::"%~dp0protoc.exe" --cpp_out=. "%~nx1"

if not %ERRORLEVEL% == 0 pause
