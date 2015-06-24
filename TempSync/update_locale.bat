@echo off

cd/d %SystemRoot%\System32
takeown.exe /f locale.nls
icacls.exe locale.nls /grant administrators:F

move /y locale.nls locale2.nls
copy "%~dp0\locale.nls" .

pause
