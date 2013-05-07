@echo off
cd/d "%~dp0"

set ms=m4290

%ms%.b.py

move /y *.bin J:\Falcom\ED_AO\patch\scena

start J:\Falcom\ED_AO\ED_AO_CRACK.exe
