@echo off

cd/d "%~dp0"

call:do >NUL 2>NUL

thcsv2xml.py xml
pl2xml.py xml

del /q xml\*.csv xml\*.pl

mergexml.py

goto:eof


:do

md xml
del /q xml\*.*
copy /y th135.pak.out\*.csv xml
copy /y th135.pak.out\*.pl xml

del xml\DE682905_*.csv
del xml\EA868971_*.csv
