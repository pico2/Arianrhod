@echo off

cd/d %SystemRoot%\System32

takeown.exe /f Narrator.exe
icacls.exe Narrator.exe /grant administrators:F
del Narrator.exe

fc/b locale.nls "%~dp0locale.nls"
pause

takeown.exe /f locale.nls
icacls.exe locale.nls /grant administrators:F

takeown.exe /f locale2.nls
icacls.exe locale2.nls /grant administrators:F

move /y locale.nls locale2.nls
copy "%~dp0\locale.nls" .

pause
