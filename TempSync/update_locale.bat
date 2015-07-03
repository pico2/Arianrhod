@echo off

cd/d %SystemRoot%\System32

fc/b locale.nls "%~dp0locale.nls"
pause

takeown.exe /f locale.nls
icacls.exe locale.nls /grant administrators:F

move /y locale.nls locale2.nls
copy "%~dp0\locale.nls" .

pause
