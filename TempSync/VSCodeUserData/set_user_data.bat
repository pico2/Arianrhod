@echo off
cd/d "%~dp0"

rd/s/q "%appdata%\Code\User"
rd/s/q "%userprofile%\.vscode\extensions"

mklink /j "%appdata%\Code\User" .
mklink /j "%userprofile%\.vscode\extensions" .\extensions

pause
