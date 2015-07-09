@echo off
cd/d "%~dp0"

if not exist "bin64\" (
    goto:eof
)

ren bin bin32
ren bin64 bin
