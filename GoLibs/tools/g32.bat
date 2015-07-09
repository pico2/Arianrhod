@echo off
cd/d "%~dp0"

if not exist "bin32\" (
    goto:eof
)

ren bin bin64
ren bin32 bin
