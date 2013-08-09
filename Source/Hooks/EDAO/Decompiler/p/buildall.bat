@echo off
cd/d "%~dp0"

for %%i in (scena\*.bin.py) do %%i

fachr176._bn.py
t_name.py
t_dbmon.py
as90010.dat.py
ms90010.py
ms90011.py

move /y *._bn J:\Falcom\ED_AO\patch\system
move /y *._dt J:\Falcom\ED_AO\patch\text
move /y *.bin J:\Falcom\ED_AO\patch\scena
move /y *.dat J:\Falcom\ED_AO\patch\battle\dat

rd/s/q __pycache__
rd/s/q scena\__pycache__
rd/s/q ..\__pycache__

rem start J:\Falcom\ED_AO\ED_AO_CRACK.exe
