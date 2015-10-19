@echo off
cd/d "%~dp0"

for /f %%i in ('dir/s/b sysatk*.py') do %%i
::for /f %%i in ('dir/s/b fachr*.py') do %%i
::for /f %%i in ('dir/s/b as*.py') do %%i
::for /f %%i in ('dir/s/b ms*.py') do %%i

move /y *._bn D:\Game\Falcom\ED_AO\patch\system
move /y *._dt D:\Game\Falcom\ED_AO\patch\text
move /y *.bin D:\Game\Falcom\ED_AO\patch\scena
move /y *.dat D:\Game\Falcom\ED_AO\patch\battle\dat
move /y sysatk*.eff D:\Game\Falcom\ED_AO\patch\effect\eff

start D:\Game\Falcom\ED_AO\ED_AO_CRACK.exe

call ..\cleanup.bat
