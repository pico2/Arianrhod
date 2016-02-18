@echo off
cd/d "%~dp0"

PUSHD %CD%

call init.bat
title %arch%

call go install reflect

cd/d "%~dp0src\cmd\link\"
call go build -o link.exe
move link.exe "%~dp0"

cd/d "%~dp0src\cmd\compile\"
call go build -o compile.exe
move compile.exe "%~dp0"

cd/d "%~dp0src\cmd\go\"
call go build -o go.exe
move go.exe "%~dp0"

POPD
