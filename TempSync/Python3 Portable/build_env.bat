@echo off

set vspath=%VS100COMNTOOLS%..\..
set VS100COMNTOOLS=%VS100COMNTOOLS%

call:GET_FULL_PATH vspath "%vspath%"

set arch=x86
call "%vspath%\VC\vcvarsall.bat" %arch%
set LIB=%~dp0libs;%LIB%
set INCLUDE=%~dp0include;%INCLUDE%

set arch=
set vspath=

%comspec% /k

goto:eof

:GET_FULL_PATH
set "%1=%~f2"
goto:eof
