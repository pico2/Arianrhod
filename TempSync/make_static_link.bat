@echo off
cd/d "%~dp0"

mklink /j "AtomConfig" "D:\Dev\Atom\config"
mklink /j "SublimeText Installed Packages" "D:\Dev\SublimeText\Data\Installed Packages"
mklink /j "SublimeText Packages" "D:\Dev\SublimeText\Data\Packages"
mklink /j "VSCodeUserData" "D:\Dev\VSCode\UserData"
mklink /j "edao_savedata" "E:\Game\Falcom\ED_AO\savedata"
mklink /j "D:\Desktop\Python3" "D:\Dev\PortablePython3"
mklink /j "Vim" "D:\Dev\Vim"
