@echo off
cd/d "%~dp0"

call init.bat
title %arch%

call go install src\reflect
call go build src\cmd\link\main.go
call go build src\cmd\compile\main.go
