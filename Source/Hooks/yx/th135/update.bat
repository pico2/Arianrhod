@echo off

cd/d "%~dp0"

call:do >nul 2>nul

title updating xml
updatexml.py th135_jp.chs.xml xmlcn

title updating pl
xml2pl.py xmlcn

title updating csv
xml2thcsv.py xmlcn

move xmlcn\*.* th135cn
rd/s/q xmlcn

del th135cn\*.xml

title packing

th135_pack.py

goto:eof


:do

md xmlcn

del /q xmlcn\*.*
copy xml\*.* xmlcn

copy /y th135.pak.out\*.pl xmlcn

md th135cn
del /q th135cn\*.*
copy /y images\*.* th135cn
copy /y binary\*.* th135cn
