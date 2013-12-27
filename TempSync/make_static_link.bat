@echo off
cd/d "%~dp0"

mklink /j "SublimeText Installed Packages" "D:\Dev\SublimeText\Data\Installed Packages"
mklink /j "SublimeText Packages" "D:\Dev\SublimeText\Data\Packages"
mklink /j "edao_savedata" "D:\Game\Falcom\ED_AO\savedata"
mklink /j "python3 portable" "D:\Desktop\python3"
mklink /j "Vim" "D:\Dev\Vim"
