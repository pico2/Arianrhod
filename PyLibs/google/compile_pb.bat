@echo off
cd/d "%~dp1"
"%~dp0protoc.exe" --python_out=. "%~nx1"