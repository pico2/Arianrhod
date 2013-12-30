@echo off
cd/d "%~dp0"

mklink /j "%~dp0%~n1" %1
